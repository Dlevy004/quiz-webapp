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

    - A rugalmasság szempontja: Számos digitális alkalmazás csak egyirányú fordításra korlátozódik (pl. csak angolról magyarra), ami nem készíti fel eléggé a felhasználót a valódi, spontán kommunikációra. Megoldásunk véletlenszerűen váltogatja a kérdések irányát, kényszerítve a felhasználót a rugalmasabb és aktívabb szófelidézésre, ami közelebb visz a folyékony nyelvhasználathoz.

    - A motivációvesztés és az unalom kockázata: Az ismétlődő tanulási formák gyorsan elveszíthetik a felhasználó érdeklődését. Alkalmazásunk beépített játékelemekkel (gamification) harcol az unalom ellen: egy pontozási rendszer, időkorlát és vizuális progress bar izgalmassá teszi a folyamatot, és kihívást jelent, ami ösztönzi a felhasználót, hogy jobb eredményt érjen el, mint legutóbb.

    - A személyre szabottság hiánya: A tanulók szókincsi szintje nagyon változó. Egy kezdőt elbátortalaníthat egy haladó szintű feladat, míg egy haladót untathat egy túl egyszerű gyakorlat. Rendszerünk több nehézségi szintet kínál, lehetővé téve a felhasználó számára, hogy olyan kihívást válasszon, amely megfelel aa aktuális képességeinek, és fokozatosan lépjen tovább, ezzel is erősítve a tanulási önbizalmát.

    - A haladás nyomon követésének nehézsége: Nehéz mérni a fejlődést papíralapú rendszerekkel. A felhasználónak nincs könnyen hozzáférhető adata arról, mennyit javult. Ez a webalkalmazás automatikusan naplózza és statisztikákat készít a teljesítményről, áttekinthető formában megjelenítve a szerzett pontszámokat és a tanulási előrehaladást, ami egy erős motivációs eszközzé válhat.

## Igényelt üzleti folyamatok

- A program célja, hogy játékos és interaktív módon segítse a diákok nyelvtanulását a modern digitális környezetben.

- Az adminisztrátornak elegendő egyszer feltölteni a feladatsort a rendszerbe, megadni a helyes válaszokat és beállítani a kvíz paramétereit (pl. időkorlát, pontozás), így a későbbi feladatkezelés egyszerű és gyors.

- A rendszer automatikusan értékeli a kvízeket, így nem szükséges minden feladatot kézzel átnézni vagy pontozni, ami jelentős időmegtakarítást biztosít.

- A diákok a teszt kitöltése után azonnal láthatják az eredményüket, valamint visszajelzést kapnak a hibás válaszokra, így azonnal tanulhatnak a saját hibáikból.

- A feladatokhoz tartozó statisztikák és toplisták motiválják a tanulókat, és lehetővé teszik a saját teljesítmény másokkal való összehasonlítását.

- A tanulás egyszerű és kényelmes, mivel a diákok bármikor előkereshetik a feladott leckéket, gyakorolhatják azokat, és azonnal ellenőrizhetik magukat.

- Nem kell könyveket vagy tankönyvi fejezeteket lapozgatni, minden tananyag és kvíz online, könnyen hozzáférhető.

- A rendszer támogatja a különböző tanulási szinteket és nyelvi témaköröket, így minden diák a saját tempójában haladhat.
