import pytest # Testing API.
import requests # HTTP library.
import distutils # distutils library.
from distutils import util


target_endpoint = 'http://127.0.0.1:5000'
dir_test_list = 'test_list.txt'

# Simple function to call the target API.
def api_get(path, params = None):
    req = requests.get(target_endpoint + path, params)
    return req

# Validate whether a request is valid.
def is_valid_request(req):
    if req.status_code != 200: # If the request was successful.
        return False
    elif isJSON(req) and 'error' in req.json(): # If the returned JSON has an 'error' attribute.
        return False
    elif isJSON(req) and 'name' in req.json() and 'description' in req.json(): # If the returned JSON has a 'name' and a 'description' attribute.
        return True
    else: # Else...
        return False

# Checks if an HTTP response is JSON.
def isJSON(response):
    if response is None:
        return False
    return response.headers.get('content-type') == 'application/json'

# Simple single test.
def test():
    assert is_valid_request(api_get('/pokemon/charizard'))
    
# Extract a list of paths to test, and the expected result, from a file and test them against the API.
def test_list():
    with open(dir_test_list, 'r') as f:
        tests = f.read().splitlines()
        for test in tests:
            path, result = test.replace(' ', '').split(',')
            assert is_valid_request(api_get(path)) == bool(distutils.util.strtobool(result))
