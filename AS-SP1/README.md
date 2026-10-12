U třídy je mezera u jednoho řádku navíc.
Velikosti některých písmen jsou malé místo velkých a opačně.
Zarovnání u některých buněk je jiné než u ostatních.

prihlasky   id_prihlasky 1-12
zaci    id_zaka 1-6
krouzky id_krouzku  1-4

erDiagram
    ZAK ||--o{ PRIHLASKA : "podava"
    KROUZEK ||--o{ PRIHLASKA : "ma"

    ZAK {
        int id_zak PK
        string jmeno
        string prijmeni
    }

    KROUZEK {
        int id_krouzek PK
        string nazev
        string kapacita
    }

    PRIHLASKA {
        int id_prihlaska PK
        int id_zak FK
        int id_krouzek FK
    }

    SELECT nazev, cena 
FROM krouzky 
WHERE cena > 500;

