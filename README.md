# Remind train

## What is it?
An service that provide train(s) that the worker can take after work.

## Tech/framework

* Language: ``Python``

## installation (via virtual environment)

```
$ virtualenv .venv

$ source .venv/bin/activate

$ python -m pip install -r requirements.txt

$ python main.py
```

## Utilisation

* In the file "constante.py", you can set the information about the worker (The time that he should reach the station, the latitude of work's address, longitude of work's address and the id of his home address).
* Once you set up everythings, launch the command : python main.py