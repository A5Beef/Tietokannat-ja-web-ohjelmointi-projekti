# Tietokannat-ja-web-ohjelmointi-projekti

A program to chart bars/restaurants.

- Users can explore added locations and the draft drinks that are served there.
- Users can register, log in, log out.
- Users can add comments to locations.
- Users can edit and delete their comments.
- Users can search for locations or comments with keywords.
- Users can add new locations, their addresses, names, served draft drinks, extra info and benefits.
- Users can see added locations and the comments under that location. 
- Users can explore other user profiles.




Under construction:
- Adding a rating system (1-5 stars) to locations.
- editing and deleting locations
- user ratings
- some other data like avg.rating on bars and even users.
- visuals, clarity
- favourite bars
- following other users
- sort by price,location,rating
- original idea of having a map. google map/api?
- picture functionality on locations/ front



--------------------------------------------------------------------------------------------
Instructions on installing the program:

1. download files
2. terminal: cd (your folder location)
3. terminal: python3 -m venv venv
4. terminal: source venv/bin/activate
5. terminal: pip install flask
6. terminal: sqlite3 database.db
7.  paste schema.sql to terminal

8. exit and repeat instructions until step 4
9. terminal: flask run
10. access the program on a browser with the provided address





--------------------------------------------------------------------------------------------

Original thought/plans and "diary":


Bisse sovellus
- Sovelluksessa on kartta, johon käyttäjät voi lisätä baareja. Tähän pitäisi sitten vielä olla joku systeemi vahinko inputeille, sulkeutuneille baareille, etc..
- Kartassa kun painelee sijainteja, niin voi nähdä baarin hanatuotteiden hintoja.
- Käyttäjät voivat luoda tunnuksen ja kirjautumaan sisään, vain rekisteröidyt käyttäjät voivat lisätä baareja ja muutella tuotteiden hintoja.
- Sovelluksessa voi etsiä baarin nimiä.
- Sovelluksessa voi katsoa käyttäjäsivua, josta näkee paljon käyttäjä on "kontribuoinut". määrä lisätyistä baareista, hintojen muutoksista, hintojen tarkkuudesta... Käyttäjä sivuissa voi olla myös esim. käyttäjä rating.
- Sovelluksissa voisi olla "opiskelija ystävälliset" baarit eri merkkauksilla. Esim. hyväksyvät haalarit sisään, opiskelija alennukset, haalarimerkkien myynti
- Sijaintien hanajuomissa, myös minkä panimon tuotteita, tai useammankin, juoman tilavuus (koko). (Hartwall, koff.....)
- Sijainteihin voi jättää kommentteja ja arvosteluita...? Ja niiden keskiarvosana.


Edit:

Kartan implementointi vaikuttaa nyt tosi vaikeelta. Ehkä vaihdan projektia niin, että se toimii ilman karttaa. Sovelluksessa voi nyt kirjautua sisään, rekisteröityä, kirjautua ulos. Sivustoissa lisätty sidebar/navigointi hommeli josta voi päästä sivulta toiseen. Sovelluksessa on sivu, jossa voi luoda uuden tietokohteen, mutta tietokohdetta ei lisätä tietokantaan, eikä sitä voi muokata/poistaa/lähettää (on vain sivusto). Luonti sivu on vaikea, paljon vaihoehtoja hanajuomista. Mietityttää, että olisiko jotenkin järkevämmin voinut laittaa noi ja vielä niin, että olisi helppo implementoida tuo tietokantaan...


edit:

Yritin saada tietokannan toimimaan... Ehkä toimii. Tietokohteita voi lisätä, mutta result page eli sellanen recappi siitä mitä on lisännyt ei toimi kunnolla. Vaikuttaa ainakin siltä, että tietokantaan menevät kuitenkin tiedot, onkohan rakenteesta kiinni. Tietokohteita ei voi nähdä vielä, ei voi muokata eikä poistaa. Ei myöskään voi hakea tai lajitella tai mitenkään. Yötöissä yritin taistella sovelluksen kanssa ja saamaan toimimaan, tuntuu siltä että tein siitä vain hankalemman ja koodi on nyt jotenkin tosi vaikea...

Mitä vielä haluaisin ehkä lisätä:
- lempi lokaatiot/baarit
- rating
- lajittelu systeemi, hinta/rating/...

edit:

Ei paljon muutoksia, henkilökohtaisista syistä + muutto


edit:

Highest priority: ability to edit location and its data, visual clearness and aesthetics, user interface..?
