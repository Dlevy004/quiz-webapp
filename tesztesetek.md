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