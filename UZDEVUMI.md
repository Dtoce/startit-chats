# Posmi un atbilstošie zari

- **master** - zars ar dokumentāciju un minimālo sākuma kodu, lai strādātu Heroku aplikācija. Šis ir zars kurā jūs varat strādāt visu laiku. Pārējie zari ir domāti gadījumā, ja kaut kas nesanāca vai pietrūka laika pabeigt posmu - lai varētu turpināt sekot uzdevumiem.
- **0.1-sakums** - zars ar sākuma kodu, mapju un failu struktūra un "sveika pasaule" kodu, lai pārbaudītu Heroku servera uzstādījumus
- **0.2-servera-puse** - chata rindu lasīšanas/raksīšanas funkcionalitāte servera pusē (Python), pārbaudāma un lietojama caur Postman vai Developer Tools
- **0.3-klienta-puse** - vienkāršu chata rindu lasīšanas/raksīšanas funkcionalitāte klienta (pārlūkprogrammas) pusē (HTML/Javascript)
- **0.4-klienta-izskata-uzlabojumi** - chata izskata uzlabojumi (HTML/CSS)
- **0.5-OOP-modelis** - refaktorēšana uz OOP modeli
- **0.6-komandas-un-varda-nomaina** - jauna funkcionalitāte servera un klienta pusē - komandu apstrāde, konkrēti - iespēja nomainīt vārdu un izdrukāt palīdzību
- **0.7-versiju-parbaude** - jauna funkcionalitāte - servera un klienta versiju sakritības pārbaude
- **0.8-chata-laika-zimogs** - jauna funkcionalitāte - laika zīmogs ziņām

# Uzdevumi pa posmiem

## 0.1 - Sākums

Ņemot par paraugu esošo projektu, izveidot mapju un failu struktūru Flask projektam, kas izmanto HTML templates

1. Izveido Flask izmantoto mapju struktūru: `templates` un `static` mapes
1. Izveido pamata template failu `index.html` template mapē
1. Izveido js (un favicon) failus static mapē
1. Izmaina `main.py`, lai tas izmantotu index.html template
1. Pievieno jaunu import `render_template`
1. Pievieno servera monitorēšanas route /health, kas atbild ar "OK"
1. Pārbauda darbību palaižot un atverot <http://127.0.0.1:5000/> un <http://127.0.0.1:5000/health> adreses

## 0.2 - Servera puses pamata funkcionalitāte

Turpinot iepriekšējā posmā paveikto, pievienot servera pusē čata pamata funkcionalitāti - iespēju saņemt esošu čata tekstu, kā arī pievienot jaunu čata tekstu. Funkcionalitātes nodrošināšanai čata tekstu nepieciešams ierakstīt logfailā.

1. Izveido divas jaunas routes - `/chats/sanjemt` un `/chats/suutit` ar attiecīgam funkcijām.
1. Izveido chata logfailu `chats.log`, kurā ieraksta dažas rindiņas ar tekstu (turpmāk vienu chata rindiņu sauksim par *ziņu*)
1. Izveido jaunu Python failu `chats.py`, kurā raksta funkcijas `ielasit_chatu` un `ierakstit_zinju`
1. `ielasit_chatu` jāatver chata logfails, jāielasa saturs un jāpārveido json. Izsauc šo funkciju no routes **/chats/sanjemt**
1. Pārbauda darbību caur Developer Tools vai Postman
1. `ierakstit_zinju` jāatver chata logfails un jāpievieno jauna rindiņa.Izsauc šo funkciju no routes **/chats/suutit**
1. Pārbauda darbību caur Developer Tools vai Postman
