from flask import Flask, jsonify
import requests

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/zip/<zipcode>')
def get_city_state(zipcode):
    url = 'https://api.zippopotam.us/us/'+str(zipcode)
    response = requests.get(url)
    data = response.json()
    city = data['places'][0]['place name']
    state = data['places'][0]['state abbreviation']
    city_state = f"{city}, {state}"
    return jsonify({'city_state': city_state})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)