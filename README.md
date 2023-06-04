# Liikuntaharrastussovellus

Sovelluksessa pystyy selaamaan tietyn alueen liikuntaharrastuspaikkoja ja lukemaan niistä tietoa ja arvosteluja. Jokainen käyttäjä on peruskäyttäjä tai ylläpitäjä.

## Toiminnallisuudet

- Käyttäjä voi luoda uuden tunnuksen ja kirjautua sisään ja ulos. *(tehty)*
- Käyttäjä näkee erilaisia liikuntaharrastuspaikkoja kartalla ja voi painaa tietyn palvelun kohdalta, jolloin hänelle näytetään enemmän tietoa esim. kuvaus ja aukioloajat.
- Käyttäjä voi antaa arvioita sanallisesti ja tähdillä sekä lukea muiden antamia arvioita. *(tehty)*
- Ylläpitäjä voi lisätä ja poistaa palvelussa näytettäviä liikuntaharrastuspaikkoja ja määrittämään niistä näytettävät tiedot. *(tehty)*
- Käyttäjä voi etsiä liikuntaharrastuspaikkoja, joiden kuvauksessa esiintyy tietty sana. *(tehty)*
- Käyttäjä näkee listan, jossa on kaikki liikuntaharrastuspaikat arvioiden mukaisessa paremmuusjärjestyksessä. *(tehty)*
- Ylläpitäjällä on mahdollisuus poistaa käyttäjän antama arvio.
- Ylläpitäjä voi luoda ryhmiä, joihin erilaisia liikuntaharrastuspaikkoja voi luokitella. Jokainen sovelluksessa esiintyvä liikuntaharrastuspaikka voi kuulua yhteen tai useampaan ryhmään. *(tehty)*

## Testaaminen

Sovellusta voi testata vain paikallisesti. Toimi näin:

1) Kloonaa repostiorio koneellesi ja siirry sen juurihakemistoon.
2) Luo sinne ```.env``` tiedosto.
3) Määritä sen sisältö:  
 DATABASE_URL='tietokannan-paikallinen-osoite'  
 SECRET_KEY='salainen-avain'
4) Seuraavaksi aktivoi virtuaaliympäristö ja asenna riippvuudet:  
*python3 -m venv venv*  
*source venv/bin/activate*  
*pip install -r ./requirements.txt*
5) Määritä vielä tietokannan skeema:  
*psql < schema.sql*
6) Käynnistö komennolla:  
*flask run*
