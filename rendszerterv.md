# Rendszerterv

## Rendszer célja

A rendszer célja egy olyan webes alkalmazás létrehozása, amely interaktív és felhasználóbarát módon támogatja a felhasználók angol nyelvi készségeinek fejlesztését. A rendszer elsődleges funkciója a kvízalapú tanulás, amelynek segítségével a felhasználók játékos formában gyakorolhatják az angol szókincset, nyelvtant és kifejezéseket. A tanulási folyamat motivációját a folyamatos visszajelzés, a pontszámok és a statisztikai nyilvántartás biztosítja.

A rendszer fejlesztésének alapvető célja, hogy a hagyományos nyelvtanulási módszereknél vonzóbb, könnyebben elérhető alternatívát kínáljon, mindezt úgy, hogy közben elősegítse a tartós tudás kialakítását. A játékosított kvízkérdések segítségével a felhasználó nem csupán passzívan tanul, hanem aktívan részt vesz a feladatmegoldásban. Nem a vizsgákra való felkészülés a fő hangsúly, hanem az, hogy a felhasználók valódi, mindennapi helyzetekben magabiztosan és helyesen tudjanak kommunikálni angolul. A rendszer használatával a tanulók fokozatosan fejlődhetnek, gyakorlati alkalmazhatóságra és a kommunikációs készség fejlesztésére koncentrál, miközben nyomon követhetik eredményeiket és teljesítményüket.

A rendszer további célkitűzése a személyre szabottság magas szintje. Ez a cél nem csupán a hatékonyság növelését, hanem a felhasználó számára azt az érzetet kelti, hogy a rendszer kifejezetten őt támogatja egyéni útján, ezzel is erősítve a kapcsolatot a felhasználó és az alkalmazás között.

A rendszer célcsoportját elsősorban diákok és nyelvtanulók alkotják, akik szívesen egészítik ki iskolai tanulmányaikat önálló gyakorlással. Emellett a rendszer alkalmas lehet olyan felhasználók számára is, akik munkahelyi vagy mindennapi kommunikációhoz szeretnék erősíteni angoltudásukat. Az egyszerű felépítésű kezelőfelületnek köszönhetően a rendszer széles körben elérhető, kezdő és haladó nyelvtanulók számára egyaránt.

A projekt célkitűzései közé tartozik egy olyan technológiailag korszerű, megbízható és könnyen bővíthető alkalmazás létrehozása, amely biztosítja az adatok biztonságos kezelését, valamint a folyamatosan frissíthető kérdésbankot.

Összességében a rendszer célja egy motiváló, modern és rugalmas tanulási környezet kialakítása, amely támogatja az angol nyelvtanulást, elősegíti a folyamatos fejlődést, és élvezetesebbé teszi a gyakorlást.

## Üzleti folyamatok modellje

### DIÁK szerepkör
![student-role](./rendszerterv%20ábrák/student-role.png)

### Kvíz menete
![quiz-session](./rendszerterv%20ábrák/quiz-session.png)

## Követelmények
### Funkcionális követelmények

A rendszernek a felhasználók igényeihez és a nyelvtanulás céljához igazodva a következő funkciókat kell biztosítania:
- Felhasználói kezelés
    - Regisztráció és egyedi felhasználónév létrehozása.
    - Bejelentkezés és munkamenet-kezelés.
    - Saját profil megtekintése, statisztikák és eredmények visszanézése.
    - A rendszernek ellenőriznie kell, hogy a megadott felhasználónév egyedi és megfelel-e az előre meghatározott formátumnak (pl. minimum 3, maximum 20 karakter, ékezetek nélkül).

- Kvízfunkciók
    - Feleletválasztós kvízek kitöltése.
    - Kétirányú gyakorlás (angol-magyar, magyar-angol).
    - A kérdéseket nehézségi szint (alap, középhaladó, haladó) szerint kell besorolni, ami lehetővé teszi a szűrést és a testreszabott kvízösszeállítást.
    - Progress bar a haladás vizuális jelzésére.
    - Azonnali visszajelzés minden kérdés után (helyes/hibás megoldás, helyes válasz megjelenítése).
    - Időmérő alkalmazása a kitöltés közben.
    - A kvíz befejezésekor (az utolsó kérdés megválaszolásakor) az időmérőnek automatikusan le kell állnia, és a pontos időt rögzítenie kell.

- Eredmények és naplózás
    - Összesítő statisztikák megjelenítése (helyes és helytelen válaszok száma, kitöltési idő).
    - Toplista vezetése a felhasználók pontszámai alapján.

- Tartalomkezelés (ADMIN)
    - Kérdések karbantartása (új kérdések, nehézségi szintek).
    - Riportok és statisztikák exportálása (pl. CSV, PDF).

- Felület és felhasználói élmény
    - Reszponzív design, amely támogatja a különböző kijelzőméreteket (desktop, tablet, mobil).
    - Világos/sötét mód váltási lehetősége.
    - Képes kérdések támogatása a vizuális tanulás érdekében.

### Nem funkcionális követelmények

A rendszernek a működés minőségére, teljesítményére és biztonságára vonatkozó elvárások:
- Biztonság
    - A felhasználói adatokhoz csak a jogosult személyek férhetnek hozzá.
    - A jelszavakat titkosított formában kell tárolni.
    - HTTPS titkosítás kötelező.

- Adatvédelem
    - Egy felhasználó nem férhet hozzá más felhasználók személyes adataihoz a felhasználónevén kívül.
    - A statisztikák és anonimizált adatokat jeleníthetnek meg.

- Teljesítmény
    - Az oldal betöltési ideje ne haladja meg az 1-2 másodpercet átlagos internetkapcsolaton.
    - A felhasználói felületnek gyorsan kell betöltődnie, a válaszok elküldése és az új kérdések megjelenítése közötti késleltetésnek minimálisnak kell lennie.

- Használhatóság
    - Az alkalmazás legyen könnyen kezelhető.
    - A felület feleljen meg az alapvető akadálymentességi elvárásoknak.
    - A vizuális visszajelzések (színek, ikonok) minden felhasználó számára egyértelműek legyenek.

- Karbantarthatóság és bővíthetőség
    - A rendszerhez később új funkciókkal (pl. további nyelvek, tanári szerepkör) is bővülhet.
    - A kódnak tiszta szerkezetűnek kell lennie, ami megkönnyíti a karbantartást és a hibakeresést.
    - Verziókövetés (Git) használata kötelező.

### Törvényi előírások, szabványok

A rendszernek a fejlesztés és üzemeltetés során az alábbi jogszabályoknak és szabványoknak kell megfelelnie:
- GDPR (Általános Adatvédelmi Rendelet):
    - Személyes adatok kezelése (regisztráció, eredmények, statisztikák) jogszerűen, tisztességesen, átláthatóan.
    - Adatok minimalizálása: csak a szükséges adatokat gyűjtjük.
    - Felhasználói jogok biztosítása: hozzáférés, törlés, helyesbítés, tiltakozás.

- Infotv. (2011. évi CXII. törvény):
    - A magyar jogszabályok szerinti adatkezelési előírások betartása.

- Szerzői jogi szabályozás:
    - A kvízkérdések, képek, tananyagok nem sérthetik harmadik felek szerzői jogait.
    - Csak jogtiszta, engedélyezett vagy saját készítésű tartalom használható.

- Cookie-kra vonatkozó szabályozás:
    - A rendszernek kezelnie kell a sütiket (cookie-k) a felhasználói hozzájárulásnak megfelelően, különös tekintettel az EU-s szabályozásokra.

- Webes szabványok:
    - Az alkalmazásnak meg kell felelnie a modern webes szabványoknak (pl. HTML5, CSS3), hogy a különböző böngészőkben is hibamentesen fusson.

## Funkcionális terv

### Rendszerszereplők

- Admin
- Felhasználó (Diák)

### Rendszerhasználati esetek és lefutásaik

#### ADMIN

- Beléphet bármilyen szerepkörbe, teljes hozzáférése van.
- Felhasználói adatokat láthat és módosíthat.
- Felhasználók hozzáadása, törlése.
- Kvízek és tesztek létrehozása, módosítása, törlése (angol–magyar témakörökben).
- Feladatok szerkesztése (pl. szókincs, fordítás, nyelvtan).
- Eredmények és statisztikák megtekintése.

#### DIÁK (Felhasználó)

- Képes kvízt kitölteni (angol ↔ magyar irányban).
- Pontokat, eredményeket szerez a kvízek után.
- Látja a saját statisztikáit (pl. helyes válaszok száma, fejlődés).
- Elérheti a toplistát.
- Megtekintheti és módosíthatja a személyes adatait.

![usecase](./rendszerterv%20ábrák/usecase.png)

### Menü-hierarchiák

- **Bejelentkezés**
  - Bejelentkezés
  - Regisztráció
  - Help

- **Main Menü**
  - Kvíz indítása
  - Teszt felület (komplexebb feladatsorok)
  - Eredmények / statisztikák
  - Toplista
  - Profil (személyes adatok)
  - Kijelentkezés

![menu_hierarchy](./rendszerterv%20ábrák/menu_hierarchy.png)
