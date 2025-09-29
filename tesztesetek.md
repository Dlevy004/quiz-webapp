# Tesztesetek

## Bejelentkezés oldal

|Leírás|Lépések|Várt eredmény|Állapot|
|------|-------|-------------|--------|
|Email mező kötelező|Üresen hagy|Sikertelen bejelentkezés, hibaüzenettel|Sikeres|
|Hibás email formátum|`test@` beírása|Sikertelen bejelentkezés, hibaüzenettel|Sikeres|
|Helyes email + üres jelszó|`test@domain.com`, jelszó üres|"A jelszót kötelező megadni" hibaüzenet|Sikeres|
|Helyes adatok megadása|`test@domain.com`, jelszó = `test`|Átirányít `index.html`-re|Sikeres|
|Checkbox működés|Rákattintás|Be-/kikapcsol|Sikeres|
|Tab sorrend|Tab-bal mozogj a mezőkön|Fókusz sorrend: email &rarr; jelszó &rarr; checkbox &rarr; link &rarr; gomb &rarr; link|Sikeres|
|Átlépés signup oldalra|Klikk a "Nincs fiókod? Regisztráció" linkre|Átvált a signup form-ra|Sikeres|

## Regisztrációs oldal

|Leírás|Lépések|Várt eredmény|Állapot|
|------|-------|-------------|--------|
|Username üres|A felhasználónév mező üresen hagyása|Sikertelen regisztráció, hibaüzenettel|Sikeres|
|Érvényes email ellenőrzése|`test@domain.com` beírása|Mező zöld lesz, nincs hibaüzenet|Sikeres|
|Rossz email formátum|`test@` beírása|Mező piros, hibaüzenet|Sikeres|
|Hibás jelszó|`abc` beírása|Sikertelen regisztráció, hibaüzenettel|Sikeres|
|Nem egyező jelszó ismétlés|`abcdef`, majd `abcdeg` jelszavak beírása|Hibaüzenet: "A két jelszó nem egyezik"|Sikeres|
|Sikeres regisztráció|Helyes username, email, jelszó, jelszó megerősítés megadása|Alert és átirányítás történik a bejelentkezésre|Sikeres|

## Bejelentkezés és regisztráció: design és reszponzív megjelenés

|Leírás|Lépések|Várt eredmény|Állapot|
|------|-------|-------------|--------|
|Mobil nézet (320px-425px)|Kis képernyőn való megnyitás|Container teljes szélesség, border-radius nincs|Sikeres|
|Tablet nézet (768px)|Közepes képernyőn való ellenőrzés|Container középen, kerekített szélekkel|Sikeres|
|Desktop nézet (>1024px)|Széles képernyőn való megtekintés|Layout középen, margók rendben|Sikeres|
|Gomb hover effekt|Login/Signup gomb fölé a kurzor|Színe megváltozik hover esetén|Sikeres|

## Hero oldal

|Leírás|Lépések|Várt eredmény|Állapot|
|------|-------|-------------|--------|
|Hero oldal, cím, leírás megjelenítése|Oldal megnyitása böngészőben, Live Serverrel|A hero szekció látható, a cím nagyobb betűmérettel jelenik meg, a "Tanulj angolul" szó nem törik sorba, a leírás is olvasható|Sikeres|
|Kvíz indítása gomb működése|Gombra kattintás|Gomb vizuálisan reagál hover/focus/active állapotokra|Sikeres|
|Lottie animáció megjelenítése|A `<dotlottie-wc>` animáció ellenőrzése|Animáció látható, autoplay és loop működik|Sikeres|
|Navigáció fix pozíció|Görgetés az oldalon|Navbar fixen marad a képernyő tetején, nem fedik el a tartalmat|Sikeres|
|Kijelentkezés gomb működése|Gombra kattintás|Gomb vizuálisan reagál hover/focus/active állapotokra, irányítson át a `login.html`-re|Sikeres|

## Footer

|Leírás|Lépések|Várt eredmény|Állapot|
|------|-------|-------------|--------|
|Footer, wave megjelenítése|Oldal megnyitása böngészőben, Live Serverrel|3 oszlopban jelenik meg a footer-top és két sorban a footer-bottom|Sikeres|
|Oldal tetejére való ugrás|Kattintás a footerben lévő logora|Visszagörget a lap tetejére|Sikeres|
|Ikonok animációja|Hover az ikonokra|Felúsznak az ikonok 5 pixellel|Sikeres|

## Főoldal, navbar, footer: design és reszponzív megjelenés

|Leírás|Lépések|Várt eredmény|Állapot|
|------|-------|-------------|--------|
|Mobil nézet (320px-425px)|Kis képernyőn való megnyitás|A főoldal egymás alá helyezi a két szekciót|Sikeres|
|Tablet és desktop nézet|Közepes és nagy képernyőn való ellenőrzés|A főoldal egymás mellé helyezi a két szekciót, a footer elrendezése is megváltozik|Sikeres|

## Profil oldal

| Leírás                        | Lépések                                              | Várt eredmény                              | Állapot |
|-------------------------------|------------------------------------------------------|--------------------------------------------|---------|
| Mégse gomb                    | Modal megnyitása → „Mégse” gomb                      | Modal bezárul, változtatás nélkül          | Sikeres |
| Bezárás ikon                  | Modal megnyitása → „X” ikon kattintás                | Modal bezárul                              | sikeres |
| Rövid jelszó (pl. „abc”)      | Modal megnyitása → „abc” beírása                     | Mező piros, invalid osztály                | Sikeres |
| Jelszó szám és nagybetű nélkül| „abcdefg!” beírása                                   | Mező piros, invalid osztály                | Sikeres |
| Érvényes jelszó               | „Abc12345!” beírása                                  | Mező zöld, valid osztály                   | Sikeres |
| Nem egyező jelszavak          | „Abc12345!” + megerősítés: „Abc123”                  | „Jelszó megerősítése” piros, invalid       | Sikeres |
| Egyező és érvényes jelszavak  | „Abc12345!” + „Abc12345!”                            | Mindkét mező valid, mentés lehetséges      | Sikeres |
| Mégse gomb                    | Modal megnyitása → „Mégse”                           | Modal bezárul, változtatás nélkül          | Sikeres |
| Bezárás ikon                  | Modal megnyitása → „X” kattintás                     | Modal bezárul                              | Sikeres |
| Súgó ikon                     | Sugó ikonra kattintunk                               | Megjelenik a jelszó követelmények listája  | Sikeres |

## Profil oldal: Reszponzív megjelenés

| Leírás                    | Lépések                        | Várt eredmény                               | Állapot |
|---------------------------|--------------------------------|---------------------------------------------|---------|
| Tablet nézet (768px)      | Közepes képernyőn megnyitás    | Grid tartja az arányokat                    | Sikeres |
| Nagy képernyő (>1024px)   | Teljes képernyőn való megnyitás| Középen igazított kártya                    | Sikeres |
| Gomb hover effekt         | Egérkurzor fölé a gombokra     | Szín- és keretváltozás megjelenik           | Sikeres |

## Authentikáció: Regisztráció

| Leírás                   | Lépések                                       | Várt eredmény                    | Állapot |
|--------------------------|-----------------------------------------------|----------------------------------|---------|
| Megfelelő, új adatokkal  | Regisztráció próba jó adatokkal               | Új felhasználó létrejön          | Sikeres |
| Nem megfelelő adatokkal  | Regisztráció próba rossz adatokkal            | Nem jön létre új felhasználó     | Sikeres |
| Létező email címmel      | Regisztráció próba létező email címmel        | Nem jön létre új felhasználó     | Sikeres |
| Létező felhasználónévvel | Regisztráció próba létező felhasználónévvel   | Nem jön létre új felhasználó     | Sikeres |

## Authentikáció: Bejelentkezés

| Leírás                            | Lépések                        | Várt eredmény                    | Állapot |
|-----------------------------------|--------------------------------|----------------------------------|---------|
| Létező felhasználói adatokkal     | Belépés létező adatokkal       | Bejelentkezés megtörtént         | Sikeres |
| Hibás felhasználói adatokkal      | Belépés nem létező adatokkal   | Bejelentkezés nem történt meg    | Sikeres |
| Hibás jelszóval                   | Belépés rossz jelszóval        | Bejelentkezés nem történt meg    | Sikeres |

## Authentikáció: Profil

| Leírás                                    | Lépés                         | Várt eredmény                 | Állapot |
|-------------------------------------------|-------------------------------|-------------------------------|---------|
| Felhasználónév megjelenítése              | Profil fülre navigálás        | Aktuális név megjelenik       | Sikeres |
| Email cím megjelenítése                   | Profil fülre navigálás        | Aktuális email megjelenik     | Sikeres |
| Profilkép megjelenítése                   | Profil fülre navigálás        | Aktuális kép megjelenik       | Sikeres |
| Felhasználónév változtatás - nem megfelelő| Érvénytelen név megadása      | Hibaüzenet                    | Sikeres |
| Felhasználónév változtatás - foglalt      | Már létező név megadása       | Hibaüzenet                    | Sikeres |
| Felhasználónév változtatás - érvényes     | Szabad név megadása           | Sikeres módosítás             | Sikeres |
| Profilkép változtatás - formátum hiba     | Nem támogatott fájlformátum   | Hibaüzenet                    | Sikeres |
| Profilkép változtatás - érvényes          | Támogatott fájlformátum       | Sikeres módosítás             | Sikeres |


## Kvíz UI – /quiz oldal

| Leírás                                    | Lépés                         | Várt eredmény                                | Állapot |
|-------------------------------------------|-------------------------------|----------------------------------------------|---------|
| Oldal védett (login szükséges)            | Kijelentkezve nyisd meg         | Átirányítás a /auth (login) oldalra                  | Sikeres |
| Oldal betöltése                           | Jelentkezz be → nyisd meg       | Kártya betölt, majd megjelenik az 1. kérdés          | Sikeres |
| Irány: HU→EN                              | HU → EN gombra katt             | Prompt magyar, válaszok angolul                      | Sikeres |
| Irány: EN→HU                              | EN → HU gombra katt             | Prompt angol, válaszok magyarul                      | Sikeres |
| Szint: Könnyű                             | „Könnyű” gombra katt            | Csak „easy” szavakból generál                        | Sikeres |
| Szint: Közepes                            | „Közepes” gombra katt           | Csak „medium” szavakból generál                      | Sikeres |
| Szint: Nehéz                              | „Nehéz” gombra katt             | Csak „hard” szavakból generál                        | Sikeres |
| Válasz kiválasztása                       | Katt egy opcióra                | Következő kérdésre lép, idő mérve                    | Sikeres |
| Kvíz lezárás                              | Válaszolj végig (10 kérdés)     | Összesítés: „Pontszám: X% (Y/10)” + „Új kvíz” gomb   | Sikeres |
| Új kvíz                                   | „Új kvíz” gomb                  | Új kérdéssor (más kérdés ID-k)                       | Sikeres |
| Hiba kezelés – betöltés                   | Állítsd le a szervert, frissíts | „Hiba a kvíz betöltésekor.” üzenet látszik           | Sikeres |
| Reszponzív                                | 320/768/1024 px szélesség       |Elrendezés nem csúszik szét, gombok jól kattinthatók  | Sikeres |
