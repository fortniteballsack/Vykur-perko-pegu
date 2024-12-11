# Skript na psaní

Tento program používá library `pynput` k simulaci psaní na klávesnici. Můžeš přizpůsobit text, který má být napsán, a rychlost psaní.

## Funkce

- Simuluje psaní textu znak po znaku.
- Nastavitelná rychlost psaní (zpoždění mezi jednotlivými znaky).

## Požadavky

- Python 3.x
- Knihovna `pynput`

## Instalace

1. Nainstaluj Python. Můžeš jej stáhnout z [python.org](https://www.python.org/).
2. Nainstaluj knihovnu `pynput` tímto příkazem v příkazovém řádku:
   ```bash
   pip install pynput
   ```

## Použití

1. Otevři soubor `main.py`.
2. Uprav proměnnou `text`, aby obsahovala text, který chceš napsat. Příklad:
   ```python
   text = ("Ahoj, toto je test psaní!")
   ```
3. Uprav hodnotu `time.sleep(0.280)` pro nastavení rychosti opisu (např. `0.1` pro rychlejší psaní nebo `0.5` pro pomalejší psaní).
4. Spusť skript příkazem:
   ```bash
   python main.py
   ```
   Nebo pravým tlačítkem myši klikni na soubor a vyber Spustit pomocí Python.
5. Přepni se do aplikace, kde chceš, aby se text napsal (máš 2 sekundy po spuštění skriptu).

Pokud potřebuješ opsat nějáký text z okna, udělej screenshot a vlož ho do této stránky: [imagetotext.info](https://www.imagetotext.info/)
Poté dáš pouze zkopírovat a máš to. Pozor ale občas ale stránka rozpozná třeba ů jako přehláskované ü nebo dá nové odstavce tam kde nemá. 
To je na tobě a musíš tyto malé chyby opravit manuálně. Většinou jich není moc. A tak lepší opravit pár chyb než to opisovat celý jak magor ne? :)

Také když něco píšeš na přesnost tak nebuď magor a neposílej to všechno s neuvěřitelnou rychlostí a 100% přesností. Nech v textu schválně pár chyb nebo pár jich tam přidej.
Pro rychlost je něco okolo těch 0.280 pomalé a tak můžeš si s tím pohrát a uvidíš
Bohužel při opisování musíš zůstat na okně které opisuješ a nemůžeš dělat na kompu u toho nic jiného :(

## Příklad

Zde je ukázkové nastavení:
```python
from pynput.keyboard import Controller
import time

keyboard = Controller()

# Text k napsání
text = ("Ahoj, světe!")

# Zpoždění před startem
time.sleep(2)

# Smyčka psaní
for char in text:
  keyboard.type(char)
  # Zpoždění mezi jednotlivými znaky v sekundách
  time.sleep(0.280)
```

Po spuštění skriptu bude napsáno `Ahoj, světe!` se zpožděním 0,28 sekundy mezi jednotlivými znaky.

## Poznámky

- Ujisti se, že aplikace, kde má být text napsán, je aktivní před začátkem psaní skriptu.
- Přizpůsob si zpoždění a text podle svých potřeb.
