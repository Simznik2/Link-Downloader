Návod na použitie
1. Stiahnutie a inštalácia
Stiahnutie súborov:

Stiahni všetky súbory do jedného priečinka:

directory_maker.py

gui_downloader.py

link_downloader.py

requirements.txt

Inštalácia závislostí:

Uisti sa, že máš nainštalovaný Python (najlepšie verziu 3.7 a vyššiu).

Otvor príkazový riadok alebo terminál a prejdite do adresára, kde sa nachádzajú tieto súbory.

Spusti príkaz:
pip install -r requirements.txt
Tento príkaz nainštaluje všetky potrebné knižnice: customtkinter, yt-dlp, pyperclip.

2. Spustenie aplikácie
Spustenie downloadera:

Pre spustenie aplikácie klikni pravým tlačidlom myši na súbor gui_downloader.py a vyber možnosť Spustiť alebo v príkazovom riadku napíš:
python gui_downloader.py
Používanie aplikácie:

URL Frame: Do textového poľa vlož URL videa, ktoré chceš stiahnuť. Môžeš tiež kliknúť na tlačidlo "Paste", aby sa URL automaticky vložila z clipboardu (skopírované URL).

Formát: Vyber formát, v akom chceš video stiahnuť:

MP4 (Video) – stiahne video (s audiom, ak zvolíš).

MP3 (Audio) – stiahne len zvuk.

Kvalita: Vyber požadovanú kvalitu videa (napr. 360p, 480p, 720p, 1080p).

Adresár: Vyber adresár, kam sa má stiahnuť súbor.

Stiahnuť: Po zadaní všetkých údajov klikni na tlačidlo Download. Aplikácia začne sťahovať súbor podľa tvojich preferencií.

Folder Creator:

Ak potrebuješ, môžeš si vytvoriť dve samostatné zložky pre video a audio súbory.

Klikni na tlačidlo "Browse" a vyber adresár, kde sa vytvoria podpriečinky video/ a audio/.

3. Poznámky
Oprava súborov:

Ak si vyberieš MP3, aplikácia stiahne len zvuk a uloží ho ako .mp3.

Ak si vyberieš MP4, aplikácia stiahne video (s audiom) vo formáte MP4.

Ak sťahuješ video vo formáte MP4, ale nechceš zvuk, môžeš vybrať možnosť MP4 (Video) a nastaviť kvalitu videa na požadovanú hodnotu (napr. 720p).

Postprocessing a FFmpeg:

Pre formát MP3 je potrebné mať FFmpeg na tvojom systéme, aby mohol prekonvertovať zvuk do požadovaného formátu.

Ak chceš používať FFmpeg, stiahni a nainštaluj ho z oficiálnej stránky FFmpeg. Potom nastav cestu k FFmpeg vo svojich systémových premenných alebo v nastaveniach aplikácie.

Oprava chýb:

Ak sa zobrazí chyba pri sťahovaní, skontroluj URL alebo vyber iný formát alebo kvalitu.

4. Pokročilé nastavenia
Použitie rôznych formátov:

Ak si želáš stiahnuť len zvuk, vyber formát MP3.

Ak chceš stiahnuť celé video, vyber formát MP4 a nastav požadovanú kvalitu.

FFmpeg pre MP3:

Ak používaš FFmpeg na konverziu zvuku do MP3, môžeš si stiahnuť FFmpeg a nastaviť ho v nastaveniach.

5. Riešenie problémov
Problém s FFmpeg: Ak aplikácia vyhodí chybu o chýbajúcom FFmpeg, skontroluj, či máš túto aplikáciu správne nainštalovanú a že je pridaná do systémovej cesty.

URL príliš dlhé: Aplikácia umožňuje vloženie URL až do 100 znakov. Ak je URL dlhšia, aplikácia vráti varovanie.