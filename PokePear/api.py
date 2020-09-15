import flask # Web Framework.
from flask import request
from flask import jsonify
import pokebase # PokeAPI wrapper.
import requests # HTTP library.
import re # Regex library.


app = flask.Flask(__name__) # Create Flask application object.
app.config['DEBUG'] = True # Show Flask request errors.
app.config['JSON_SORT_KEYS'] = False # Prevent Flask from sorting JSON responses.
app_host = '127.0.0.1' # Default server host.
app_port = 5000 # Default server port.

API_SHAKESPEAR = 'https://api.funtranslations.com/translate/shakespeare.json' # Shakespear API endpoint.

# Route root GET requests to 'home' function.
# This is the root index page.
@app.route('/', methods=['GET'])
def home():
    pokemon = pokebase.pokemon_species('charizard')
    
    return '<h1>PokePear API</h1><p>Use this API to search for a pokemon and display its description as written by Shakespear.</br>Example usage: <a href=\'/pokemon/ditto\'>http://127.0.0.1:5000/pokemon/ditto</a></p>'


# Route 'pokemon' GET requests to 'pokemon' function.
# Receives a pokemon name as input and returns a JSON with its description.
@app.route('/pokemon/<name>', methods=['GET'])
@app.route('/pokemon/', methods=['GET'])
def pokemon(name = None):
    # Validate input name.
    if (name is None or len(name)<=0):
        return custom_error('Please specify a pokemon name.')

    # Retrieve pokemon description from pokemon api.
    pokemon = pokebase.pokemon_species(name)
    if (not hasattr(pokemon, 'id')): # Check if pokemon exists.
        return custom_error('Pokemon not found.')
    poke_desc = pokemon.flavor_text_entries[6].flavor_text
    
    # Format and normalize the description string.
    poke_desc = re.sub('[\s]', ' ', poke_desc) # Replace new lines with spaces.
    poke_desc = re.sub('[^a-zA-Z0-9-_*. ]', '', poke_desc) # Remove other special characters.
    
    # Shakespear it.
    req = requests.get(API_SHAKESPEAR, {'text': poke_desc})
    if (req.status_code != 200): # Confirm if the request was successful.
        return jsonify(req.json())
    elif (req.json()['success']['total'] != 1):
        return custom_error('Unknown error.')
    poke_desc_shpear = (req.json()['contents']['translated']) # Deserialise result.
    
    # Return JSON response.
    return jsonify({'name': pokemon.name, 'description': poke_desc_shpear})

# Returns a custom HTTP 500 error message in JSON format.
# Receives an error string as input.
def custom_error(message):
    return jsonify({'error': {'code': 500, 'message': message}})

app.run(host=app_host, port=app_port) # Run Flask.