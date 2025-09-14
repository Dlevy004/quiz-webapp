# Követelmény Specifikáció

## Áttekintés

- Az alkalmazás célja egy interaktív kvízfelület létrehozása, amely az angol és magyar szókincs fejlesztését teszi lehetővé, mindezt játékos formában.

- A rendszer célja, hogy a felhasználók motiváltan, szórakoztató módon tudják gyakorolni a nyelvet, miközben nyomon követhetik a fejlődésüket.

- A rendszer webes környezetben működik, reszponzív kialakítással, így asztali gépen, mobilon és tableten egyaránt kényelmesen használható.

- A felhasználói felület modern, sötét és világos módot is támogat, valamint vizuális visszajelzésekkel segíti a tanulást.

- A felhasználók kérdésekre adhatnak választ, amelyek lehetnek angol &rarr; magyar, illetve magyar &rarr; angol irányban is.

- A kérdések irányát a rendszer véletlenszerűen generálja.

- A quiz során a játékosok időkorláttal megadott kérdéseket kapnak, amelyekért pontokat gyűjthetnek a helyesség alapján.

- Az eredmények azonnal visszajelzésre kerülnek (zöld/piros színezés, helyes válasz megjelenítése), valamint a rendszer összesített pontszámot vezet, amely megtekinthető egy külön menüpontban.

- A kérdések nehézség szerint csoportosíthatók (pl. alap szókincs, középhaladó, haladó). A játékélményt további funkciók egészítik ki, mint a visszaszámláló, progress bar a kérdések előrehaladásáról, valamint világos/sötét mód váltás.

- A projekt során a fejlesztéshez verziókövető rendszert (Git, GitHub) és feladatkezelő rendszert (Trello) használunk, a dokumentáció markdown formátumban készül.

- A cél egy könnyen kezelhető, szórakoztató és motiváló nyelvi quiz alkalmazás létrehozása, amely minőségi felhasználói élményt nyújt.

## Jelenlegi helyzet

- A mai angol nyelvtanulás során a hallgatók gyakran unalmas és statikus módszerekkel tanulnak szavakat és kifejezéseket, például jegyzetekből vagy nyomtatott listákból, amelyek a motiváció csökkentéséhez és a tudás megszerzésének nehézségéhez vezethetnek. A mi alkalmazásunk ezekre a problémákra kínál megoldást:

    - A tanulók nem kapnak azonnali visszajelzést a válaszaikról, így nem tudják, hol hibáztak vagy mit kellene jobban átismételniük. A mi alkalmazásunk azonnali visszajelzést ad, ami segíti a felhasználókat a tanulási folyamatban.

    - A meglévő nyelvi alkalmazások sokszor nem rugalmasak: nem teszik lehetővé a kétirányú gyakorlást. Emellett az eredmények nyomon követése és a fejlődés vizualizálása hiányzik, ami csökkenti a tanulók motivációját.

    - Nehéz felmérni a megszerzett szókincset anélkül, hogy bonyolult teszteket kellene kitölteni. Egy egyszerű kvíz gyors és hatékony módja a tudásfelmérésnek.

    - A diákok gyakran nem kapnak lehetőséget a saját szókincsük szintjének megfelelő nehézségű feladatok gyakorlására. A rendszerünk nehézségi szintek szerint kínál kvízeket, így mindenki a saját tudásszintjének megfelelő kihívást találhat.

    - A jelenlegi nyelvi gyakorló eszközök ritkán tartalmaznak játékos elemeket vagy motivációs eszközöket (pontozás, toplista, visszaszámláló), pedig ezek növelik az elköteleződést és a rendszeres tanulást.

    - Sok esetben nincs lehetőség a haladás nyomon követésére és az eredmények megosztására másokkal, ami csökkenti a közösségi és versenyszerű tanulás élményét.

    - A szókincsfejlesztő eszközök sokszor csak szöveges alapon működnek, figyelmen kívül hagyva a vizuális tanulók igényeit. A rendszerünk képekkel is támogatná a szavak jelentésének megerősítését, ami segít a szavak könnyebb megjegyzésében.

    - Webalkalmazásunk segítségével a felhasználó a saját idejében és a saját érdeklődési körének megfelelő nehézségi szinten gyakorolhat.

## Követelménylista

| Modul        |  ID  | Név                     |  v. | Kifejtés |
|--------------|------|------------------------ |-----|----------|
| Jogosultság  |  K1  | Felhasználónév megadása | 1.0 | A diákok egy felhasználónévvel tudnak bejelentkezni.|
| Feladattípus |  K2  | Kvíz                    | 1.0 | A kvíz több kérdésből áll, ahol több lehetőség közül kell a helyes választ kiválasztani.|
| Feladattípus |  K3  | Kétirányú kvíz          | 1.0 | A rendszer lehetővé teszi a kétirányú gyakorlást.|
| Feladattípus |  K4  | Nehézségi szintek       | 1.0 | A kérdések nehézség szerint csoportosíthatók.|
| Adatkezelés  |  K5  | Elektronikus Napló      | 1.0 | A felhasználók láthatják az elért eredményeiket, a kvíz pontszámát és a kitöltésre fordított időt.|
| Adatkezelés  |  K6  | Eredmények mentése      | 1.0 | A rendszer minden kvíz után elmenti a pontszámot a felhasználónévhez.|
| Felület      |  K7  | Sötét/Világos Mód       | 1.0 | A felhasználók választhatnak világos és sötét mód között.|
| Felület      |  K8  | Időmérő                 | 1.0 | A kvíz alatt egy időzítő méri a kitöltés idejét. A végeredményt nem befolyásolja, de a naplóban megjelenik.|
| Felület      |  K9  | Vizuális visszajelzés   | 1.0 | A rendszer azonnali visszajelzést ad a felhasználónak a válaszai helyességéről.|
| Felület      |  K10 | Progress bar            | 1.0 | A kvíz előrehaladását egy progress bar jelzi.|
| Felület      |  K11 | Reszponzív kialakítás   | 1.0 | A webes alkalmazás reszponzív, így asztali gépen, mobilon és tableten egyaránt használható.|
| Felület      |  K12 | Bejelentkezés           | 1.0 | A felhasználók belépnek a felületre.|

## Jelenlegi üzleti folyamatok modellje

- A hagyományos oktatás elavult és passzív.

- A diákok statikus tankönyvekből tanulnak.

- Ezek a tankönyvek nem veszik figyelembe az egyéni tanulási stílusokat.

- A rendszer nem kínál személyre szabott tanulást.

- A tanárok túlterheltek és nincs idejük minden diákkal foglalkozni.

- A tanulás így unalmas rutinná válik, a diákok érdeklődése alábbhagy.

- A tankönyvek tartalma gyakran elavult.

- Ezáltal a diákok nem kapnak valós életre szóló felkészítést.

- A tanárok idejét az adminisztráció és a kézi javítások emésztik fel.

- A hagyományos felmérések lassúak és nem adnak azonnali visszajelzést.

- A diákok nehezen követik nyomon a fejlődésüket, ami demotiváló.

- A papíralapú oktatás drága és környezetszennyező.

- Az oktatás nem fejleszti a digitális készségeket.

- A diákok nem tanulnak meg alkalmazkodni a gyorsan változó világhoz.

- A jelenlegi modell merev és rugalmatlan, ami akadályozza a hatékony tudásszerzést.

## Vágyálom rendszer

- A projekt célja egy olyan rendszer, amely játékos formában segíti a nyelvtanulást és gyakorlást.

- A rendszer több platformon elérhető: weben és androidos alkalmazásként.

- Regisztráció után a felhasználó különböző kvíz- és feladattípusok közül választhat.

- A program színes, látványos felülettel rendelkezik, hogy motiválja és lekösse a tanulókat.

- A feladatok játékos elemeket tartalmaznak, ezzel élvezetesebbé téve a nyelvtanulást.

- A rendszer tárolja a felhasználók teljesítményét (pl. toplista), így lehetőség nyílik másokkal való összehasonlításra.

- A felhasználók pontokat kapnak a helyesen megválaszolt kvízkérdések után.

- A pontozás figyelembe veheti a feladatok megoldására fordított időt is.

- A rendszer admin felülettel rendelkezik, ahol az admin új kvízkérdéseket és feladatokat tölthet fel.
