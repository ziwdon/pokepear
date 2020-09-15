# PokePear

An API to search for a pokemon and display its description as written by Shakespear.

## Requirements

- Python 3.8;
- pip (package installer);
- Flask (python library);
- PokeBase (python library);
- PyTest (python library).

## Installation

Install [Python 3.8](https://www.python.org/downloads/).
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the following python libraries:
- Flask;
- PokeBase;
- PyTest.

Example:
```bash
pip install flask
```

## Usage

Execute the **api.py** file to start the Flask server: 
```bash
python api.py
```
Once the server is running, you can make a GET request to the API by using the following format **http://<host>:port/pokemon/<pokemon_name>**. A JSON response is returned with the pokemon description in Shakespear language.

By default, the server runs on **127.0.0.1:5000**. If you want to change this, make sure to edit the **api.py** file and edit the **app_host** and **app_port** variables.
  
Example usage:
```bash
http://127.0.0.1:5000/pokemon/charizard
```
Response:
```bash
{
  "name": "charizard", 
  "description": "Charizard flies 'round the sky in search of powerful opponents. 't breathes fire of such most wondrous heat yond 't melts aught. However 't nev'r turns its fiery breath on any opponent weaker than itself."
}
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
