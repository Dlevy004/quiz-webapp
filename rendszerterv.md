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

## Fizikai környezet

- Az alkalmazás webes platformra készül, asztali böngészőből elérhető.
- A szerver oldali futtatás felhőalapú környezetben történik.
- HTTPS titkosítás engedélyezve van a biztonság érdekében.
- Tűzfal és alapvető hálózati biztonsági szabályok beállítva.
- Nincsenek megvásárolt komponensek, minden használt technológia nyílt forráskódú.

### Fejlesztői eszközök

- Visual Studio Code
- Flask (backend keretrendszer Python nyelvhez)
- JavaScript, HTML, CSS (frontend elkészítéséhez)
- Git & GitHub (verziókezelés)

## Architekturális terv

### Backend

- A rendszerhez szükség van egy adatbázis szerverre, ebben az esetben MySQL-t használunk.
- A backend Python Flask keretrendszerrel készül.
- A kliens oldali kéréseket REST API szolgálja ki.
- Felhasználói autentikáció: bejelentkezés után session alapú vagy token alapú azonosítás biztosítja a jogosultságokat.

### Web kliens

- A webes felület HTML, CSS és JavaScript segítségével készül.
- A kliens a Flask REST API-hoz kapcsolódik, amelyen keresztül eléri a kvízeket, eredményeket és felhasználói adatokat.
- Az adatforgalom HTTPS protokollon keresztül zajlik, az illetéktelen hozzáférések ellen védve.
- A felhasználói interakciók egyszerű és letisztult UI-n keresztül történnek (pl. kvíz kitöltés, toplista megtekintés, profil módosítás).

## Implementációs terv

### Web:
- A rendszer felhasználói felülete teljes egészében webes technológiákra épül, mivel ez biztosítja a könnyű hozzáférést és a platformfüggetlen működést. 
- A felület kialakításához HTML-t használunk, amely a tartalom és a szerkezet megjelenítéséért felelős. 
- A weboldal megjelenését és stílusát CSS segítségével valósítjuk meg. 
- Ezzel biztosítható a reszponzív működés, vagyis a rendszer különböző képernyőméreteken (asztali számítógép, laptop, tablet, mobiltelefon) is megfelelően fog kinézni. 
- Az interaktív funkciókat JavaScript nyelven implementáljuk. 
- A JavaScript gondoskodik arról, hogy a kvíz kitöltése közben azonnali visszajelzést kapjon a felhasználó, például jelezze a helyes és helytelen válaszokat. 
- Emellett ezen keresztül valósul meg a pontszámítás, a progress bar működése, valamint az időmérés és annak kijelzése. 
- A három technológia együttese teszi lehetővé, hogy a felület egyszerre legyen modern, letisztult és könnyen kezelhető.

### Backend:
- A szerveroldali működést a Python nyelvhez tartozó Flask keretrendszer biztosítja. 
- A Flask egy könnyű, de rugalmas megoldás, amely kifejezetten alkalmas kisebb webes alkalmazások gyors fejlesztésére. 
- A Flask egyik legfontosabb feladata a REST API-k létrehozása. 
- Ezeken keresztül a kliensoldali alkalmazás kapcsolatot tud teremteni az adatbázissal, és képes adatokat küldeni vagy fogadni. 
- Például a kvíz indításakor a kliens lekéri az aktuális kérdéseket, a válaszadás után pedig visszaküldi az eredményt, amelyet a rendszer rögzít. 
- A Flask előnye, hogy jól illeszkedik a Python ökoszisztémához, így egyszerűen bővíthető új funkciókkal, és könnyen integrálható más könyvtárakkal vagy adatbáziskezelőkkel is. 
- Ezáltal hosszú távon is megbízható alapot ad a rendszernek.

### Adatbázis:
- Az adatok kezelésére és tárolására MySQL adatbázist alkalmazunk. 
- Az adatbázis tartalmazza a kvízkérdéseket, a lehetséges válaszokat, valamint az ezekhez tartozó nehézségi szinteket. 
- Emellett itt kerülnek rögzítésre a felhasználók eredményei is, amelyek később felhasználhatók statisztikák készítéséhez vagy a toplista megjelenítéséhez. 
- A MySQL kiválóan alkalmas strukturált adatok tárolására, mivel táblákban, jól meghatározott kapcsolatokkal lehet benne rendszerezni az információkat. 
- Az adatbázis segítségével könnyedén lekérdezhető például, hogy egy adott diák mennyi helyes választ adott, mennyi idő alatt töltötte ki a tesztet, vagy éppen hogyan változott a teljesítménye az elmúlt időszakban.
- A MySQL választását az is indokolja, hogy stabil, megbízható, széles körben elterjedt és nyílt forráskódú rendszer, amely hosszú távon is biztos alapot nyújt a projekt működéséhez.

### Fejlesztői eszközök:

- A fejlesztés során Visual Studio Code programot használunk, amely egy modern, gyors és jól testreszabható fejlesztői környezet. 
- Segítségével egyszerre több programozási nyelven is kényelmesen lehet dolgozni, valamint bővítmények révén hatékonyabbá teszi a fejlesztést. 
- A forráskód kezelése Git verziókövető rendszerrel történik. 
- Ez biztosítja, hogy minden változtatás naplózva legyen, és bármikor vissza lehessen állni egy korábbi állapotra. 
- A közös munkát a GitHub támogatja, amely lehetővé teszi a csapattagok számára, hogy egyszerre dolgozzanak ugyanazon a projekten. 
- Ezzel átláthatóbbá válik a munka, könnyebb a feladatok felosztása, és a hibák kijavítása is gyorsabban megtörténhet.

![implementation-plan](./rendszerterv%20ábrák/implementation-plan.png)

### Összefoglalás:

- Az alkalmazás megvalósítása során olyan technológiákat és eszközöket választottunk, amelyek egyszerre teszik lehetővé a könnyű használatot és a hatékony fejlesztést. 
- A HTML, CSS és JavaScript biztosítja a felhasználóbarát, reszponzív és interaktív webes felületet. 
- A Flask keretrendszer gondoskodik a szerveroldali logikáról és az adatforgalom kezeléséről, míg a MySQL adatbázis biztosítja az információk biztonságos és rendszerezett tárolását. 
- A fejlesztői eszközök, mint a Visual Studio Code és a GitHub, támogatják a csapatmunkát és a projekt hosszú távú fenntarthatóságát. 
- Ezeknek a technológiáknak a kombinációja garantálja, hogy a rendszer könnyen kezelhető, bővíthető és megbízható legyen, miközben hatékonyan szolgálja a nyelvtanulást.

![database_plan](./rendszerterv%20ábrák/database_plan.png)

## Tesztterv

A tesztelés célja a rendszer és komponensei működésének ellenőrzése, hibák feltárása, valamint annak biztosítása, hogy a funkciók a követelményeknek megfelelően valósuljanak meg. A tesztelés során kiemelt figyelmet kap a felhasználói élmény, a teljesítmény, valamint az adatok helyes kezelése.

### Tesztelési időszak és célok

- Fejlesztés közbeni tesztelés: minden új funkció implementálása után alapvető egységtesztek futtatása.
- Alfa teszt: a fejlesztők és belső tesztelők végzik, célja a fő funkciók ellenőrzése és a hibák javítása.
- Béta teszt: külső felhasználók bevonásával történik, célja a valós környezetben való kipróbálás és a felhasználói visszajelzések gyűjtése.

### Tesztelési környezet

- Böngészők: Google Chrome, Mozilla Firefox, Microsoft Edge, Safari (legfrissebb verziók).
- Eszközök: Asztali számítógép, laptop, tablet, mobiltelefon.
- Képernyőméretek: 1280x720, 1366x768, 1920x1080, valamint mobil eszközök tipikus méretei.
- Operációs rendszerek: Windows 10/11, Android, iOS.

### Backend tesztelés

- Unit tesztek: Minden backend funkcióhoz külön unit tesztek írása
    - Service réteg tesztelése mock adatokkal
    - Adatbázis műveletek tesztelése in-memory adatbázissal
    - API végpontok tesztelése integrációs tesztekkel
    - Hibakezelés tesztelése különböző hibás forgatókönyvekkel
- Tesztlefedettség: Minimum 80% kódlefedettség célja
- Automatizálás: Tesztesetek futtatása CI/CD folyamat részeként

### Frontend tesztelés

- Live Server tesztelés:
    - Alkalmazás indítása live serverrel lokálisan
    - Manuális vizuális ellenőrzés minden komponens megjelenéséről
    - Interakciók tesztelése (gombnyomások, navigáció, űrlapkitöltés)
- Böngésző DevTools használata:
    - Console naplók ellenőrzése hibákért és figyelmeztetésekért
    - Network panel monitorozása API hívások és válaszidők ellenőrzéséhez
    - Elements panel használata DOM struktúra és stílusok ellenőrzéséhez
    - Performance panel használta teljesítmény elemzéshez
    - Application panel használata local storage és session storage ellenőrzéséhez
- Reszponzív tesztelés:
    - DevTools eszközzel különböző készülékméretek szimulálása
    - Touch események tesztelése mobil eszközökhöz

### Alfa teszt

- Az alfa teszt célja a fő funkciók (belépés, kvíz kitöltés, toplista, statisztikák megjelenítése) helyes működésének ellenőrzése. 
- A tesztet a fejlesztők és kijelölt belső tesztelők végzik. 
- Hibák esetén a fejlesztési ciklus rövid idő alatt korrigálásra kerül.

### Béta teszt

- A béta teszt célja a felhasználói élmény vizsgálata valós környezetben. 
- Külső tesztelők kapják meg a hozzáférést, akik különböző eszközökön próbálják ki az alkalmazást. 
- A visszajelzéseket rögzítjük, és a leggyakrabban előforduló problémák kijavításra kerülnek.

### Tesztelendő funkciók

#### Backend Service:

- Rendszer válaszideje megfelelő legyen (max. 1–2 másodperc).
- Adatbázisban az adatok helyesen kerüljenek mentésre és visszaadásra.
- REST API helyes működése: minden kérést pontos válasszal teljesít.

#### Frontend:

- Kvíz kérdések és válaszok megjelenítése hibátlanul.
- Progress bar megfelelő működése.
- Azonnali visszajelzés helyessége minden válasz után.
- Reszponzív design ellenőrzése (mobil, tablet, asztali).
- Világos/sötét mód helyes váltása.

#### Kvízfunkciók:

- Angol → Magyar és Magyar → Angol irány helyes működése.
- Különböző nehézségi szintek (alap, középhaladó, haladó) szerinti szűrés.
- Időmérő működése (indítás, leállítás, pontos idő rögzítése).
- Helyes és helytelen válaszok helyes kiértékelése.

#### Statisztikák és toplista:

- Összesítő statisztikák helyes számítása (jó/rossz válaszok, kitöltési idő).
- Toplista helyes sorrendben való megjelenítése.

#### Hibakezelés

- Hibás adatok esetén a rendszer figyelmeztető üzenetet ad.
- Sikertelen adatbázis-művelet esetén nem engedi tovább a felhasználót.
- A hibaüzenetek egyértelműek, informatívak, és nem tartalmaznak bizalmas technikai információt.
- Minden teszteset eredménye dokumentálásra kerül
- Hibák rögzítése és nyomon követése bug tracking rendszerben
- Végteszt jelentés készítése a tesztelés lezárásakor

![test-plan](./rendszerterv%20ábrák/test-plan.png)




## Telepítési terv - Webes alkalmazás

- A szoftver webes felületéhez csak egy ajánlott böngésző telepítése szükséges (Google Chrome, Mozilla Firefox, Microsoft Edge, Safari).
- Külön kliensoldali szoftver telepítése nem szükséges.
- A felhasználók közvetlenül az internetről, a megadott URL címen keresztül érik el az alkalmazást.
- A kapcsolat HTTPS protokollon keresztül történik.
- A megfelelő működéshez JavaScript és cookie-k engedélyezése javasolt a böngészőben.
- Az alkalmazás reszponzív, asztali gépen, tableten és mobiltelefonon is használható.
  

## Karbantartási terv

- Az alkalmazás folyamatos üzemeltetése és karbantartása szükséges, amely magában foglalja a programhibák kijavítását, az új igények miatti módosításokat, valamint a környezeti változásokhoz való alkalmazkodást.
- Rendszeresen ellenőrizni kell a böngészőkkel és az operációs rendszerekkel való kompatibilitást.
- Időszakosan új kérdéskörökkel és feladatokkal kell bővíteni a kvízbankot, hogy fenntartsuk a felhasználók érdeklődését és motivációját.
- A karbantartás típusai:
    - Corrective Maintenance: a felhasználók által jelzett hibák javítása.
    - Adaptive Maintenance: a rendszer naprakészen tartása, új környezeti követelményekhez igazítás.
    - Perfective Maintenance: új funkciók és fejlesztések hozzáadása a jobb felhasználói élmény érdekében.
    - Preventive Maintenance: olyan problémák elhárítása, amelyek jelenleg nem okoznak hibát, de később komoly gondot jelenthetnek.
