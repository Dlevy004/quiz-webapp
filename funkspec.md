# Funkcionális Specifikáció

## Áttekintés

- Az alkalmazás egy modern, interaktív webalapú kvízjáték, melynek elsődleges célja, hogy a felhasználók számára szórakoztató és hatékony eszközt nyújtson az angol és magyar szókincs tanulásához, gyakorlásához és fejlesztéséhez.

- A projekt fő küldetése, hogy a nyelvtanulást élvezetesebbé és motiválóbbá tegye, miközben lehetőséget biztosít a felhasználóknak arra, hogy játékos keretek között, folyamatos visszajelzés mellett gyakorolhassák a nyelvet.

- A hagyományos tanulási módszerekkel ellentétben a platform a játékosítást (gamification) helyezi előtérbe, ezzel motiválva a felhasználókat, hogy rendszeresen gyakoroljanak.

- Az alkalmazás központi funkciója a kvíz, amelyben a felhasználók különböző nehézségű kérdéseket kapnak. A kérdések iránya (angol &rarr; magyar vagy magyar &rarr; angol) véletlenszerűen generált, így változatos gyakorlási élményt biztosít.

- A rendszer azonnali visszajelzést ad a válaszokról: helyes válasz esetén zöld kiemelést, hibás esetben piros kiemelést jelenít meg, emellett megmutatja a helyes megoldást. Ez segíti a tanulókat abban, hogy ne csak gyakoroljanak, hanem közvetlenül tanuljanak is a hibáikból.

- A játékélményt több kiegészítő funkció támogatja:

  - időkorlátos kérdések, amelyek fokozzák az izgalmat és a koncentrációt, mindezt úgy, hogy közben ösztönzi a felhasználót a gyors és határozott döntéshozatalra
  - a rendszer folyamatosan vezeti a szerzett pontok összesített számát, amely egy külön eredmények menüpontban tekinthető meg, így a felhasználó nyomon követheti a fejlődését
  - progress bar, amely vizuálisan mutatja az előrehaladást,
  - nehézségi szintek (alap, középhaladó, haladó), amelyek lehetővé teszik a fokozatos fejlődést,
  - világos/sötét mód váltás, amely növeli a felhasználói élményt.

- Az alkalmazás webes környezetben érhető el, reszponzív kialakítással, tehát egyaránt használható számítógépen, tableten és mobiltelefonon. Ez biztosítja, hogy a felhasználók bármikor, bárhonnan hozzáférhessenek, így a nyelvtanulás könnyen beépíthető a mindennapjaikba.

- A felületet egy modern, letisztult design jellemzi, amely magában foglal egy felhasználóbarát navigációt és egy világos/sötét téma közötti választási lehetőséget, ezzel személyre szabva a felhasználói élményt és védve a szemeket a hosszantartó használat során.

- A felület vizuális elemekkel támogatja a szókincs elsajátítását. Az alkalmazásban nemcsak szöveges, hanem képes kérdések is helyet kapnak, így a vizuális tanulók számára is hatékony eszközzé válik.

- A projekt fejlesztése során hangsúlyt kap a korszerű munkaszervezés és eszközhasználat. A kódkezeléshez Git és GitHub verziókövetőt alkalmazunk, a feladatok menedzseléséhez pedig Trellót, ami lehetővé teszi a csapatmunka hatékony koordinálását és a kódverziók ellenőrzött kezelését. A dokumentáció markdown formátumban készül, amely átlátható és könnyen karbantartható.

- Végső soron az alkalmazás célja, hogy egy minőségi, élvezetes és magas hatékonyságú nyelvtanulási segédeszközzé váljon, amely pozitív hatással van a felhasználók nyelvtudására és tanulási szokásaira, és technikailag is korszerű megoldásokat nyújt.

## Jelenlegi helyzet

- A nyelvtanulás, különösen a szókincsfejlesztés terén, a hagyományos módszerek ma is széleskörűen elterjedtek, azonban számos kihívást és hiányosságot rejtenek magukban, amelyek érintik a tanulók motivációját és a tanulási folyamat hatékonyságát.

- Alkalmazásunk ezen problémákra nyújt megoldást:

    - Az azonnali visszajelzés hiánya: A hagyományos módszerek (pl. szókártyák, jegyzetelés, nyomtatott könyvek) esetében a felhasználó gyakran órákra, napokra akár el van zárva a válaszok ellenőrzésétől és a hibák kijavításától. Ez azt eredményezi, hogy a tévesen megtanult vagy rosszul memorizált szó rögződik. Rendszerünk azonnali visszajelzést ad, ezzel megerősítve a helyes ismereteket és korrigálva a hibákat a memorizálás folyamatának legelején.

    - A rugalmasság szempontja: Számos digitális alkalmazás csak egyirányú fordításra korlátozódik (pl. csak angolról magyarra), ami nem készíti fel eléggé a felhasználót a valódi, spontán kommunikációra. Megoldásunk véletlenszerűen váltogatja a kérdések irányát, kényszerítve a felhasználót a rugalmasabb és aktívabb szófelidézésre, ami közelebb visz a folyékony nyelvhasználathoz.Jelenlegi üzleti folyamatok modellje:

    - A motivációvesztés és az unalom kockázata: Az ismétlődő tanulási formák gyorsan elveszíthetik a felhasználó érdeklődését. Alkalmazásunk beépített játékelemekkel (gamification) harcol az unalom ellen: egy pontozási rendszer, időkorlát és vizuális progress bar izgalmassá teszi a folyamatot, és kihívást jelent, ami ösztönzi a felhasználót, hogy jobb eredményt érjen el, mint legutóbb.

    - A személyre szabottság hiánya: A tanulók szókincsi szintje nagyon változó. Egy kezdőt elbátortalaníthat egy haladó szintű feladat, míg egy haladót untathat egy túl egyszerű gyakorlat. Rendszerünk több nehézségi szintet kínál, lehetővé téve a felhasználó számára, hogy olyan kihívást válasszon, amely megfelel aa aktuális képességeinek, és fokozatosan lépjen tovább, ezzel is erősítve a tanulási önbizalmát.

    - A haladás nyomon követésének nehézsége: Nehéz mérni a fejlődést papíralapú rendszerekkel. A felhasználónak nincs könnyen hozzáférhető adata arról, mennyit javult. Ez a webalkalmazás automatikusan naplózza és statisztikákat készít a teljesítményről, áttekinthető formában megjelenítve a szerzett pontszámokat és a tanulási előrehaladást, ami egy erős motivációs eszközzé válhat.

## Követelménylista

| Modul        |  ID  | Név                     |  v. | Kifejtés |
|--------------|------|------------------------ |-----|----------|
| Jogosultság  |  K1  | Felhasználónév megadása | 1.0 | A diákok egyetlen, egyedi felhasználónév megadásával léphetnek be a rendszerbe. A rendszer ezen a néven azonosítja őket, és ehhez a névhez fűződnek majd az eredmények az Elektronikus Naplóban.|
| Feladattípus |  K2  | Kvíz                    | 1.0 | A kvíz alapvető feladattípusa egy feleletválasztós teszt, amely több kérdésből áll. Minden kérdéshez legalább négy lehetséges válasz tartozik, amelyek közül egy a helyes.|
| Feladattípus |  K3  | Kétirányú kvíz          | 1.0 | A kétirányú gyakorlás lehetővé teszi a felhasználóknak, hogy angolról magyarra és magyarról angolra is tesztelhessék a tudásukat. A rendszernek képesnek kell lennie a szavak és kifejezések mindkét irányú lekérdezésére.|
| Feladattípus |  K4  | Nehézségi szintek       | 1.0 | A kérdéseket nehézség szerint kell csoportosítani, ami lehetővé teszi a felhasználóknak, hogy a tudásszintjüknek megfelelő feladatokat válasszanak. Szintek: alap, középhaladó, és haladó. Ez a szűrés javítja a felhasználói élményt és a tanulás hatékonyságát.|
| Adatkezelés  |  K5  | Elektronikus Napló      | 1.0 | Az Elektronikus Napló funkcióval a felhasználók nyomon követhetik a fejlődésüket. A naplóban meg kell jelennie az elért pontszámnak, a kvíz kitöltésére fordított időnek, valamint a helyes és helytelen válaszok számának. A napló grafikus megjelenítése tovább növelheti a felhasználói motivációt.|
| Adatkezelés  |  K6  | Eredmények mentése      | 1.0 | A rendszer minden kvíz befejezése után automatikusan elmenti a felhasználó pontszámát, a hozzárendelt felhasználónévhez. Ez az adatbázis-kezelési funkció alapvető fontosságú a felhasználói előrehaladás rögzítéséhez és az Elektronikus Napló feltöltéséhez.|
| Felület      |  K7  | Sötét/Világos Mód       | 1.0 | A felhasználók beállíthatják az alkalmazás megjelenését, választhatnak a világos és a sötét mód között. Ez a funkció növeli a felhasználói kényelmet, különösen gyenge fényviszonyok mellett.|
| Felület      |  K8  | Időmérő                 | 1.0 | A kvíz kitöltése alatt egy vizuálisan is látható időmérő számlálja a felhasználó által eltöltött időt. Bár a pontszámot nem befolyásolja, az idő adatai megjelennek a naplóban, segítve a felhasználókat az önértékelésben és a tempójuk monitorozásában.|
| Felület      |  K9  | Vizuális visszajelzés   | 1.0 | A felhasználók azonnali, vizuális visszajelzést kapnak a válaszaikról. Például a helyes válasz zöld színnel, míg a helytelen piros színnel jelenik meg, így segítve a tanulást és a hibák gyors felismerését.|
| Felület      |  K10 | Progress bar            | 1.0 | A progress bar vizuálisan jelzi a felhasználónak a kvíz előrehaladását, például a már megválaszolt kérdések számát a teljes kérdésszámhoz viszonyítva. Ez a funkció segít a felhasználónak felmérni, hogy mennyi van még hátra a kvízből.|
| Felület      |  K11 | Reszponzív kialakítás   | 1.0 | A felhasználói felület reszponzív kialakítása biztosítja, hogy az alkalmazás automatikusan alkalmazkodjon a különböző eszközök (asztali gép, mobil, tablet) képernyőméretéhez és tájolásához. Ez a kulcsfontosságú funkció a széles körű felhasználói hozzáférhetőség biztosításához.|
| Felület      |  K12 | Bejelentkezés           | 1.0 | A felhasználók a főoldalon a felhasználónév megadásával jutnak be az alkalmazás felületére. Ez a lépés indítja el a felhasználói munkamenetet, és teszi lehetővé a személyre szabott adatok (pl. napló) elérését.|

## Jelenlegi üzleti folyamatok modellje

- A jelenlegi oktatási rendszerben a tanulás alapvetően egyirányú és passzív folyamat.

- A diákok kizárólag hagyományos, statikus tananyagokból, például tankönyvekből sajátítanak el tudást.

- Az egyéni tanulási stílusok, mint a vizuális vagy auditív tanulás, nem kapnak elegendő figyelmet.

- Ez a megközelítés szinte semmilyen lehetőséget nem biztosít a személyre szabott tanulásra, hiszen a tanároknak a teljes osztály átlagához kell igazodniuk.

- A tanulási folyamat nem skálázható. A tanároknak nincs kapacitásuk arra, hogy minden egyes diák egyéni tempóját és igényeit figyelembe vegyék.

- Ez a helyzet a gyengébben teljesítő diákok lemaradását és a tehetségesebbek unatkozását eredményezi.

- A jelenlegi oktatási modell merev és rugalmatlan, így nem képes hatékonyan alkalmazkodni a diákok egyéni igényeihez és képességeihez.

- A tanulás unalmas rutinná válik, ahelyett, hogy interaktív és szórakoztató élmény lenne.

- A hagyományos tankönyvek tartalma elavult lehet, és nem reflektál a mai nyelvi trendekre, szlengre vagy kulturális változásokra.

- A tanároknak rengeteg órát kell a dolgozatok kézi javításával és az adminisztrációval tölteniük, ami elvonja a figyelmet az érdemi oktatómunkától.

- Emiatt a diákok olyan nyelvezetet tanulnak, ami nem feltétlenül tükrözi a mai angol nyelvet.

- A hagyományos rendszerek nem fejlesztik azokat a digitális készségeket, amelyekre a jövőben szükség lesz.

- A tankönyvek tartalma gyakran nem frissül elég gyorsan, ami a gyorsan változó világban komoly hátrányt jelent.

- A tudás számonkérése is nagyrészt papíralapú dolgozatok és vizsgák formájában történik.

- A diákok nehezen követik nyomon saját fejlődésüket, mivel nincsenek részletes statisztikák és visszajelzések a teljesítményükről.

- A tanulók nem kapnak azonnali visszajelzést a hibáikról, ami lassítja a tanulási folyamatot és csökkenti a motivációt.

- A diákok érdeklődése hamar alábbhagy a motiváció hiánya miatt, ami a megszerzett tudás felszínes maradását eredményezi.

- Az oktatás nem nyújt megfelelő felkészülést a valós életre, mert hiányzik a gyakorlati, interaktív tudáselsajátítás.

- A diákok megtanulják a szabályokat, de nem tudják azokat alkalmazni a mindennapi kommunikációban.

- A felmérések nem csupán elavultak, de rendkívül idő és energiaigényesek a pedagógusok számára.

- A tanároknak rengeteg órát kell a dolgozatok kézi javításával és az adminisztrációval tölteniük, ami elvonja a figyelmet az érdemi oktatómunkától.

- A papíralapú oktatás jelentős nyomdai és terjesztési költségeket generál az iskoláknak, ami gazdaságilag fenntarthatatlan.

- Környezeti terhelést is jelent a felhasznált papír mennyisége miatt.

- A fenntarthatóság kérdése egyre fontosabb a társadalomban, és a jelenlegi rendszer ezzel szembemegy.

- Összességében a tradicionális oktatás elavult keretei akadályozzák a hatékony és élvezetes tudásszerzést.

## Igényelt üzleti folyamatok

- A program célja, hogy játékos és interaktív módon segítse a diákok nyelvtanulását a modern digitális környezetben.

- Az adminisztrátornak elegendő egyszer feltölteni a feladatsort a rendszerbe, megadni a helyes válaszokat és beállítani a kvíz paramétereit (pl. időkorlát, pontozás), így a későbbi feladatkezelés egyszerű és gyors.

- A rendszer automatikusan értékeli a kvízeket, így nem szükséges minden feladatot kézzel átnézni vagy pontozni, ami jelentős időmegtakarítást biztosít.

- A diákok a teszt kitöltése után azonnal láthatják az eredményüket, valamint visszajelzést kapnak a hibás válaszokra, így azonnal tanulhatnak a saját hibáikból.

- A feladatokhoz tartozó statisztikák és toplisták motiválják a tanulókat, és lehetővé teszik a saját teljesítmény másokkal való összehasonlítását.

- A tanulás egyszerű és kényelmes, mivel a diákok bármikor előkereshetik a feladott leckéket, gyakorolhatják azokat, és azonnal ellenőrizhetik magukat.

- Nem kell könyveket vagy tankönyvi fejezeteket lapozgatni, minden tananyag és kvíz online, könnyen hozzáférhető.

- A rendszer támogatja a különböző tanulási szinteket és nyelvi témaköröket, így minden diák a saját tempójában haladhat.

## Használati esetek

#### ADMIN szerepkör

- Az Admin bármely más szerepkörbe beléphet, hogy ellenőrizze a rendszer hibamentes működését.

- Felelős a rendszer problémamentes üzemeltetéséért és karbantartásáért.

- Teljes hozzáféréssel rendelkezik az alkalmazás minden funkciójához és adatához.

- Hozzáfér a felhasználók listájához, ahol módosíthatja a profiladatokat (felhasználónév, jelszó, szerepkör, jogosultságok).

- Új felhasználókat tud regisztrálni, valamint törölni a rendszerből.

- Képes új nyelvi kvízkérdéseket és feladatokat létrehozni, hasonlóan a tanárokhoz.

- Üzenetet küldhet egyes felhasználóknak vagy globális értesítést az összes felhasználónak egyszerre.

- A diákok eredményeit és pontszámait csak az Admin tudja módosítani, miután a Tanár értékelést adott.

#### DIÁK szerepkör

- A Diák feladata a rendszerben elérhető nyelvi kvízek és feladatok kitöltése.

- Regisztráció után saját profillal rendelkezik, amely tartalmazza az eredményeit, pontszámait és toplistás helyezését.

- Azonnali visszajelzést kap a kitöltött feladatokra, így azonnal láthatja az eredményt és a helyes megoldásokat.

- Gyakorolhat különböző nehézségi szinteken, így a saját tudásszintjének megfelelő feladatokat választhatja.

- Nyomon követheti saját fejlődését statisztikák és teljesítményriportok segítségével.

- Részt vehet pontgyűjtő és toplistás versenyben, amely motiválja a folyamatos tanulásra.

- Hozzáfér a feladott leckékhez és bármikor újra megoldhatja a gyakorló kvízeket.





## Forgatókönyv – Kvíz indítása és kitöltése
Szereplők:
- Felhasználó (Diák) – a rendszer végfelhasználója, aki gyakorolni szeretne.
- Rendszer (Webalkalmazás) – a kvízjáték platform, amely a kérdéseket szolgáltatja, értékel, és visszajelzést ad.


Előfeltételek:
- A felhasználó rendelkezik egy választott felhasználónévvel.
- A rendszerben vannak elérhető kérdések és nehézségi szintek.


Fő folyamat:
- Bejelentkezés
    - A felhasználó megnyitja az alkalmazást.
    - A kezdőlapon beírja a felhasználónevét, majd rákattint a „Belépés” gombra.
    - A rendszer ellenőrzi, hogy a felhasználónév létezik-e, és belépteti a felhasználót.
    
- Kvíz indítása
    - A felhasználó kiválasztja a kvíz nehézségi szintjét (alap, középhaladó, haladó).
    - A rendszer összeállít egy kérdéssort a választott szintnek megfelelően.
    - A rendszer véletlenszerűen meghatározza a kérdésirányokat (angol → magyar vagy magyar → angol).

- Kérdések megválaszolása
    - A rendszer megjeleníti az első kérdést, és elindítja az időmérőt.
    - A felhasználó kiválasztja a helyesnek vélt választ.
    - A rendszer azonnali vizuális visszajelzést ad (zöld = helyes, piros = hibás), és mutatja a helyes választ.
    - A progress bar előrehalad, jelezve a kérdéssor állását.
    - Ez ismétlődik, amíg a felhasználó az összes kérdést meg nem válaszolja.

-  Eredmények összesítése
    - A rendszer kiszámítja a pontszámot és a helyes válaszok arányát.
    - Megjeleníti a kvíz teljes kitöltési idejét.
    - A felhasználó egy összesítő képernyőt lát (pontszám, hibák, helyes válaszok).

- Eredmények naplózása
    - A rendszer elmenti az eredményt az Elektronikus Naplóba a felhasználónévhez rendelve.
    - A felhasználó bármikor visszanézheti korábbi eredményeit a „Napló” menüpontban.


Alternatív folyamatok:
- Hibás bejelentkezés: ha a felhasználónév nem megfelelő, a rendszer hibaüzenetet küld, és nem enged belépni.
- Kvíz megszakítása: a felhasználó bármikor kiléphet, ekkor a rendszer nem menti az eredményt.


Utófeltételek:
- A felhasználó eredménye rögzítve van az Elektronikus Naplóban.
- A toplista (ha van) frissül az új pontszám alapján.

## Fogalomtár

- Adminisztrátor (Admin)
Olyan felhasználó, aki kérdésbankot és kvízparamétereket kezelhet (létrehozás, módosítás, törlés), riportokat tekinthet meg, és rendszerszintű beállításokat végezhet.

- Alkalmazás (Rendszer)
A webalapú kvízplatform teljes egésze: front-end, back-end, adatbázis és admin felület.

- Angol → magyar / Magyar → angol (Kérdésirány)
A feladatok fordítási iránya. A rendszer véletlenszerűen választja ki kérdésenként.

- API
A back-end által biztosított programozott hozzáférési pontok összessége, amelyen keresztül a front-end adatot kér és küld.

- Autentikáció / Bejelentkezés
A felhasználó azonosítása (jelen rendszerben egyedi felhasználónévvel). Sikeres azonosítás után indul a munkamenet.

- Beállítások
Felhasználói preferenciák (pl. sötét/világos mód, nyelvi beállítások), amelyek lokálisan vagy profilhoz kötötten tárolódnak.

- Elektronikus Napló
A felhasználó kvíz-előzményeinek és teljesítménymutatóinak (pontszám, idő, helyes/hibás válaszok) strukturált tára és megjelenítése.

- Eredmény
Egy kitöltött kvíz aggregált kimenete: pontszám, helyes válaszok aránya, teljes kitöltési idő, nehézségi szint.

- Feladat (Kérdés)
A kvíz egysége: kérdés szövegével, opcionális képi elemmel és több válaszlehetőséggel; pontosan egy helyes megoldással.

- Feladattípus: Kvíz
Feleletválasztós feladatsor, fix kérdésszámmal vagy előre definiált időkerettel.

- Felhasználó
A rendszer aktív használója (diák/tanuló), akinek kvíz-eredményei naplózásra kerülnek.

- Felhasználónév
Egyedi szöveges azonosító, amelyhez a rendszer a teljesítményadatokat rendeli.

- Frontend
A kliensoldali alkalmazás (UI), amelyet a felhasználó a böngészőben használ.

- Gamification (Játékosítás)
Motivációs mechanizmusok összessége (pontozás, progress bar, toplista, időzítő), amelyek növelik az elköteleződést.

- Időkorlát / Időmérő
A kérdések vagy a teljes kvíz megválaszolására rendelkezésre álló idő kezelése és vizuális visszajelzése.

- Kérdésbank
Az admin által karbantartott strukturált gyűjtemény kérdésekkel, válaszokkal, metaadatokkal (nehézségi szint, téma, címkék).

- Kérdésirány
Lásd: Angol → magyar / Magyar → angol.

- Kétirányú kvíz
Kvízmód, amelyben a rendszer vegyesen ad angol → magyar és magyar → angol kérdéseket.

- Lokalizáció (i18n)
A felület és a tartalmak nyelvi/kulturális adaptálása (HU/EN feliratok, formátumok).

- Nehézségi szint
A kérdések bonyolultsági kategóriája: alap, középhaladó, haladó.

- Pontszám
A kvíz során elért teljesítmény numerikus értéke; alapja a helyes válaszok száma, és opcionálisan az időfelhasználás.

- Progress bar (Előrehaladás-jelző)
Vizuális komponens, amely jelzi a kvízben megtett előrehaladást (megválaszolt / összes kérdés arány).

- Reszponzív felület
UI-kialakítás, amely különböző kijelzőméreteken és tájolásokban is optimalizáltan jelenik meg (mobil, tablet, desktop).

- Riport
Összegző nézet vagy kimutatás (felhasználói eredmény, kérdés-nehézség, időfelhasználás, toplista), szűrésekkel és exporttal.

- Sötét/Világos mód (Téma)
Váltható megjelenési témák a vizuális komfort és az akadálymentesség érdekében.

- Szókincs adatbázis (Szólista)
A kérdésbank alapját képező lexikai elemek (szavak, kifejezések), fordításokkal és metaadatokkal.

- Szűrők
Riportokban és listanézetekben alkalmazható feltételek (időszak, nehézségi szint, téma, felhasználó).

- Téma / Kategória
Tartalmi csoportosítás a kérdésbankban (pl. mindennapi élet, utazás, munka, iskola).

- Toplista
Ranglista, amely a felhasználókat pontszám, helyességi arány vagy más mutató szerint rendezi.

- UI (Felhasználói felület)
A vizuális és interakciós elemek összessége, amelyekkel a felhasználó a rendszerrel kommunikál.

- Validáció
Beviteli adatok ellenőrzése (kötelező mezők, formátum, egyediség), hibaüzenetek biztosítása.

- Vizuális visszajelzés
Azonnali jelzés a válasz helyességéről (zöld/piros kiemelés, helyes megoldás megjelenítése).

- Backend
Szerveroldali komponensek: üzleti logika, perzisztencia, értékelés, riport-kiszolgálás.

- Adatbázis
Perzisztens tároló a felhasználók, kvízek, kérdések, eredmények és riportok számára.

- Munkamenet (Session)
A bejelentkezett felhasználó aktív interakciós időszaka; a kliens és a szerver közti állapotkezelés.

- Válaszlehetőség
Egy kérdéshez tartozó alternatív opció. Egy opció a helyes.

- Verzió (v.)
Követelmény/elem aktuális kiadási száma a dokumentációban (pl. „1.0”).

- Címke (Tag)
A kérdésbank elemeinek gyors keresését segítő kiegészítő jelölő (pl. „phrasal-verb”, „food”).

- Export
Riportok és naplók letöltése (CSV, PDF), megosztható formában.

- Jogosultságkezelés
Szerepkör- és hozzáférés-szabályok, amelyek meghatározzák, ki milyen műveleteket végezhet (felhasználó vs. admin).