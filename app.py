from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/ip', methods=['GET'])
def get_ip():
    # Make a GET request to the ipify service to retrieve the public IP address
    response = requests.get('https://api.ipify.org')
    ip = response.text
    return jsonify({"ip": ip})

if __name__ == '__main__':
    app.run(debug=True)