# projekt_flask

Uruchom wirtualne srodowisko:
tworzymy hermetyczne środowisko dla bibliotek aplikacji:

$ python3 -m venv .venv

aktywowanie hermetycznego środowiska

$ source .venv/bin/activate


Instalacja requirements:
$ pip install -r requirements.txt

Zobacz
$ pip list

Aby uruchomic aplikacje:
przed utworzeniem pliku .flaskenv

$ FLASK_APP=microweb.py
$ flask run

po utworzeniu :

$ flask run

Aplikacja dziala na localhost:
http://localhost:5000/
