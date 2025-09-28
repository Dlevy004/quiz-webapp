import json, random
from datetime import datetime
from flask import Blueprint, request, jsonify
from sqlalchemy import func

from quizapp import db
from quizapp.models_quiz import Word, Quiz, QuizItem, Attempt, Answer

bp = Blueprint('quiz_api', __name__)  # ezt fogjuk beregisztrálni az __init__.py-ban

def _shuffle(arr):
    """Egyszerű keverés: stabil és determinisztika nélkül, de elég nekünk."""
    tmp = [(random.random(), x) for x in arr]
    tmp.sort(key=lambda t: t[0])
    return [x for _, x in tmp]

@bp.get('/api/quiz')
def get_quiz():
    """
    Kvíz generálása.
    Query paramok:
      - direction: 'HU_EN' vagy 'EN_HU' (alapértelmezett: HU_EN)
      - limit: hány kérdés (alap: 10)
      - level: 'easy' | 'medium' | 'hard' (opcionális – ha nincs, vegyes)
    """
    direction = request.args.get('direction', 'HU_EN')
    try:
        limit = int(request.args.get('limit', 10))
    except ValueError:
        limit = 10
    level = request.args.get('level')  # None vagy 'easy'|'medium'|'hard'

    # Alap lekérdezés, opcionálisan szintre szűrve
    q = Word.query
    if level in ('easy', 'medium', 'hard'):
        q = q.filter(Word.level == level)

    # Véletlen válogatás
    words = q.order_by(func.random()).limit(limit).all()
    if not words:
        return jsonify({"error": "Nincsenek szavak (vagy ezen a szinten nincsenek)."}), 400

    # Létrehozzuk a Quiz rekordot, hogy legyen azonosító és később statisztikázható legyen
    quiz = Quiz(direction=direction)
    db.session.add(quiz)
    db.session.flush()  # kell a quiz.id

    items = []
    for w in words:
        # A félrevezető opciók pool-ját is ugyanarra a szintre szűrjük, ha kértek szintet
        pool_q = Word.query.filter(Word.id != w.id)
        if level in ('easy', 'medium', 'hard'):
            pool_q = pool_q.filter(Word.level == level)

        if direction == 'HU_EN':
            prompt, correct = w.hu, w.en
            pool = [x.en for x in pool_q.order_by(func.random()).limit(50)]
        else:
            prompt, correct = w.en, w.hu
            pool = [x.hu for x in pool_q.order_by(func.random()).limit(50)]

        # Distractorok: 3 eltérő válasz
        distractors = [p for p in pool if p != correct][:3]
        choices = _shuffle([correct] + distractors)
        correct_index = choices.index(correct)

        # Mentjük az itemet a DB-be (későbbi elemzéshez)
        qi = QuizItem(
            quiz_id=quiz.id,
            word_id=w.id,
            prompt=prompt,
            correct_index=correct_index,
            choices_json=json.dumps(choices, ensure_ascii=False)
        )
        db.session.add(qi)
        db.session.flush()

        # Amit a kliensnek visszaadunk
        items.append({
            "id": qi.id,
            "prompt": prompt,
            "choices": choices,
            "correctIndex": correct_index
        })

    db.session.commit()
    return jsonify({
        "id": quiz.id,
        "direction": direction,
        "items": items
    })

@bp.post('/api/submit')
def submit_quiz():
    """
    Eredmény beküldése.
    Body (JSON):
      {
        "quizId": "...",
        "answers": [
          {"itemId":"...", "chosenIndex":1, "timeMs":1234},
          ...
        ]
      }
    Válasz: { "score": 80, "correctCount": 8, "total": 10 }
    """
    data = request.get_json(force=True)
    quiz_id = data.get('quizId')
    answers = data.get('answers', [])

    if not quiz_id or not answers:
        return jsonify({"error": "quizId és answers kötelező"}), 400

    # Az adott kvíz itemjei (helyes indexekhez)
    items = {row.id: row for row in QuizItem.query.filter_by(quiz_id=quiz_id).all()}
    correct_count = 0

    for a in answers:
        it = items.get(a.get('itemId'))
        if not it:
            continue
        if int(a.get('chosenIndex', -1)) == int(it.correct_index):
            correct_count += 1

    total = len(answers)
    score = round((correct_count / total) * 100) if total else 0

    # Attempt mentése
    attempt = Attempt(
        quiz_id=quiz_id,
        user_id=None,  # ide később jöhet current_user.get_id() ha bejelentkezéshez kötitek
        started_at=datetime.utcnow(),
        finished_at=datetime.utcnow(),
        score=score,
        correct_count=correct_count,
        total=total
    )
    db.session.add(attempt)
    db.session.flush()

    # Answer rekordok mentése
    for a in answers:
        it = items.get(a.get('itemId'))
        if not it:
            continue
        db.session.add(Answer(
            attempt_id=attempt.id,
            item_id=it.id,
            chosen_index=int(a.get('chosenIndex', -1)),
            time_ms=int(a.get('timeMs', 0)),
            is_correct=(int(a.get('chosenIndex', -1)) == int(it.correct_index))
        ))

    db.session.commit()
    return jsonify({"score": score, "correctCount": correct_count, "total": total})
