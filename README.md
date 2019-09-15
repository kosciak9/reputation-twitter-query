Twitter posts collector
=======================


Usage:

```sh
python3.6 -m virtualenv env
source env/bin/activate
pip install -r requirements.txt

python app.js
```

Notice that

```sh
flask run
```

will start without scraper routine!

### Testing

```sh
# run `proof of concept' app
python scraper/main_test.py
```

Start scraper routine:

```py
from scraper import run
run(5) # arg is probing interval in minutes
```
