#Jak zajistit aby se zobrazily nové ikonky a fanart doplňků.

# Aktualizace náhledů doplňků #

XBMC uchovává náhledy doplňků a fanartu v cache, ta se nepromaže ani při odstranění a opětovné instalaci doplňku ani při aktualizaci doplňku.
Pokud přesto chcete vidět nové ikonky a fanart, proveďte následující:

Smažte soubor Textures.db, který najdete v adresáři:

**Windows**
c:/Users/Vaše jméno/Data aplikací/XBMC/Userdata/Database/

**Linux**
/home/Vaše jméno/.xbmc/Userdata/Database

V případě spouštění z OpenELEC lze smazat přímo z XBMC pomocí správce souborů. Databázy náhledů pak najdete pod:

Složka profilu/Database/