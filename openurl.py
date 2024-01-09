import webbrowser

urls = """
https://en.pons.com/translate/german-greek/Gipfel
https://en.pons.com/translate/german-greek/marschieren
https://en.pons.com/translate/german-greek/Aufstieg
https://en.pons.com/translate/german-greek/haupts%C3%A4chlich?q=hauptsachlich
https://en.pons.com/translate/german-greek/schmankerin?bidir=1
https://en.pons.com/translate/german-greek/deftiges
https://en.pons.com/translate/german-greek/fairen
https://en.pons.com/translate/german-greek/rosshutte?bidir=1
https://en.pons.com/translate/german-greek/Ausstellung
https://en.pons.com/translate/german-greek/exponaten
https://en.pons.com/translate/german-greek/naturschutzer?bidir=1
https://en.pons.com/translate/german-greek/ausbeitung?bidir=1
https://en.pons.com/translate/german-greek/Aufsicht
https://en.pons.com/translate/german-greek/archivierung?bidir=1
https://en.pons.com/translate/german-greek/Verf%C3%BCgung?q=verfugung
https://en.pons.com/translate/german-greek/mindestalters
https://en.pons.com/translate/german-greek/erreichen
https://en.pons.com/translate/german-greek/Besitz
https://en.pons.com/translate/german-greek/gelten
https://en.pons.com/translate/german-greek/Einlass
https://en.pons.com/translate/german-greek/Hinweise
https://en.pons.com/translate/german-greek/Sterne
https://en.pons.com/translate/german-greek/fahrgelegenheit?bidir=1
https://en.pons.com/translate/german-greek/Reinigung
https://en.pons.com/translate/german-greek/Fleck
https://en.pons.com/translate/german-greek/wahrscheinlich
https://en.pons.com/translate/german-greek/schweib?bidir=1
https://en.pons.com/translate/german-greek/laufen
https://en.pons.com/translate/german-greek/wedding?bidir=1
https://en.pons.com/translate/german-greek/Umgebung
https://en.pons.com/translate/german-greek/versorgt
https://en.pons.com/translate/german-greek/selbst
https://en.pons.com/translate/german-greek/betriebe
https://en.pons.com/translate/german-greek/Anbaufl%C3%A4che?q=anbauflache
https://en.pons.com/translate/german-greek/underschiedliche?bidir=1
https://en.pons.com/translate/german-greek/betrieben
https://en.pons.com/translate/german-greek/Bauern
https://en.pons.com/translate/german-greek/H%C3%A4ndler?q=handler
https://en.pons.com/translate/german-greek/autorenrechte?bidir=1
https://en.pons.com/translate/german-greek/quellen
https://en.pons.com/translate/german-greek/verfungung?bidir=1
https://en.pons.com/translate/german-greek/Betrag
https://en.pons.com/translate/german-greek/weutem?bidir=1
https://en.pons.com/translate/german-greek/niedrig
https://en.pons.com/translate/german-greek/verlage
https://en.pons.com/translate/german-greek/profitiert
https://en.pons.com/translate/german-greek/H%C3%A4lfte?q=halfte
https://en.pons.com/translate/german-greek/Betrachtung
https://en.pons.com/translate/german-greek/reiche
https://en.pons.com/translate/german-greek/bewahrheitet
https://en.pons.com/translate/german-greek/eingesetzt
https://en.pons.com/translate/german-greek/Erreichte
https://en.pons.com/translate/german-greek/verteilt
https://en.pons.com/translate/german-greek/Gegenwart
https://en.pons.com/translate/german-greek/unterliegen
https://en.pons.com/translate/german-greek/%C3%BCberlegen?q=uberlegen
https://en.pons.com/translate/german-greek/vermutilich?bidir=1
https://en.pons.com/translate/german-greek/Vergangenheit
https://en.pons.com/translate/german-greek/Ged%C3%A4chtnis?q=gedachtnis
https://en.pons.com/translate/german-greek/Gehirn
https://en.pons.com/translate/german-greek/wandeln
https://en.pons.com/translate/german-greek/folgen
https://en.pons.com/translate/german-greek/niedrige
https://en.pons.com/translate/german-greek/oberstes
https://en.pons.com/translate/german-greek/Gebot
https://en.pons.com/translate/german-greek/einverstandiserklarung?bidir=1
https://en.pons.com/translate/german-greek/Zeichen
https://en.pons.com/translate/german-greek/ganze
https://en.pons.com/translate/german-greek/wesentlich
https://en.pons.com/translate/german-greek/enorm
https://en.pons.com/translate/german-greek/unvertraglichkeiten?bidir=1
https://en.pons.com/translate/german-greek/mehrheitlich
https://en.pons.com/translate/german-greek/schwellungen
https://en.pons.com/translate/german-greek/blutungen
https://en.pons.com/translate/german-greek/schadigungen?bidir=1
https://en.pons.com/translate/german-greek/segelschifte?bidir=1
https://en.pons.com/translate/german-greek/wellen
https://en.pons.com/translate/german-greek/Erfindung
https://en.pons.com/translate/greek-german/dampfantriebs?bidir=1
https://en.pons.com/translate/german-greek/tief
https://en.pons.com/translate/german-greek/Versorgung
https://en.pons.com/translate/german-greek/ungem%C3%BCtlich?q=ungemutlich
https://en.pons.com/translate/german-greek/Richtung
https://en.pons.com/translate/german-greek/vergn%C3%BCgen?q=vergnugen
https://en.pons.com/translate/german-greek/unternahmen
https://en.pons.com/translate/german-greek/bermogenden?bidir=1
https://en.pons.com/translate/german-greek/Kundschaft
https://en.pons.com/translate/german-greek/folgten
https://en.pons.com/translate/german-greek/vergnugungsfahrten?bidir=1
https://en.pons.com/translate/german-greek/begeistert
https://en.pons.com/translate/german-greek/reedereien
https://en.pons.com/translate/german-greek/vergugte?bidir=1
https://en.pons.com/translate/german-greek/vergn%C3%BCgte?q=vergnugte
https://en.pons.com/translate/greek-german/deck?bidir=1
https://en.pons.com/translate/german-greek/nobel
https://en.pons.com/translate/german-greek/assortieren?bidir=1
https://en.pons.com/translate/german-greek/berfugung?bidir=1
https://en.pons.com/translate/german-greek/bermeintlicher?bidir=1
https://en.pons.com/translate/german-greek/wegwerfware?bidir=1
https://en.pons.com/translate/german-greek/aambiente?bidir=1
https://en.pons.com/translate/german-greek/kerzen
https://en.pons.com/translate/german-greek/backsteinwanden?bidir=1
https://en.pons.com/translate/german-greek/keuchel?bidir=1
https://en.pons.com/translate/german-greek/berein?bidir=1
https://en.pons.com/translate/german-greek/Verein
https://en.pons.com/translate/german-greek/erhailt?bidir=1
https://en.pons.com/translate/german-greek/umsonst
https://en.pons.com/translate/german-greek/besch%C3%A4digten?q=beschadigten
https://en.pons.com/translate/german-greek/Gerichte
https://en.pons.com/translate/german-greek/Zutaten
https://en.pons.com/translate/german-greek/besondere
https://en.pons.com/translate/german-greek/M%C3%B6bel?q=mobel
https://en.pons.com/translate/german-greek/wertchatzung?bidir=1
https://en.pons.com/translate/german-greek/weggeschickt
https://en.pons.com/translate/german-greek/%C3%BCbrig?q=ubrig
https://en.pons.com/translate/german-greek/%C3%84u%C3%9Ferungen?q=ausserungen
https://en.pons.com/translate/german-greek/Vermeidung
https://en.pons.com/translate/german-greek/fehldeutungen
https://en.pons.com/translate/german-greek/Zweck
https://en.pons.com/translate/german-greek/verf%C3%BCgen?q=verfugen
https://en.pons.com/translate/german-greek/angelerntes
https://en.pons.com/translate/german-greek/Grunde
https://en.pons.com/translate/german-greek/vorwiegend
https://en.pons.com/translate/german-greek/aufmerksam
https://en.pons.com/translate/german-greek/aussagen
https://en.pons.com/translate/german-greek/fragend
https://en.pons.com/translate/german-greek/borsichtiger?bidir=1
https://en.pons.com/translate/german-greek/Druck
https://en.pons.com/translate/german-greek/schwaachen?bidir=1
https://en.pons.com/translate/german-greek/anzugreufen?bidir=1
https://en.pons.com/translate/german-greek/geringeres
https://en.pons.com/translate/german-greek/Hoffnung
https://en.pons.com/translate/german-greek/unnotiges?bidir=1
https://en.pons.com/translate/german-greek/anliegen
https://en.pons.com/translate/german-greek/aufdringlich
https://en.pons.com/translate/german-greek/heftung?bidir=1
https://en.pons.com/translate/german-greek/Aufbewahrung
https://en.pons.com/translate/german-greek/Sprungbrett
https://en.pons.com/translate/german-greek/anweisungen
https://en.pons.com/translate/german-greek/Folge
https://en.pons.com/translate/german-greek/herumrennen
https://en.pons.com/translate/german-greek/Rutschgefahr
https://en.pons.com/translate/german-greek/Windel
https://en.pons.com/translate/german-greek/pfeifen
"""

# Split the URLs into a list
urls = urls.strip().split('\n')

group_size = 10
num_groups = len(urls) // group_size + 1

for group_index in range(num_groups):
    start_index = group_index * group_size
    end_index = min(start_index + group_size, len(urls))
    group_urls = urls[start_index:end_index]

    for url in group_urls:
        webbrowser.open(url)

    if group_index < num_groups - 1:
        input("Press Enter to continue to the next group of URLs...")
