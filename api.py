from flask import Flask, jsonify, request

app = Flask(__name__)

# Data keys
keys = {
    "WZ3UD-ADZH8-MFYJB-RUGM3-J37TX": {
        "user": "1",
        "expire": "30.09.2024",
    }
}

# Data status default
status_data = {
    "status": "Active"
}

@app.route('/keys', methods=['GET'])
def get_keys():
    # Mengembalikan seluruh data keys
    return jsonify(keys)

@app.route('/keys', methods=['POST'])
def add_key():
    # Mengambil data dari request JSON
    new_key = request.json.get('key')
    new_user = request.json.get('user')
    new_expire = request.json.get('expire')

    # Validasi data
    if new_key and new_user and new_expire:
        keys[new_key] = {
            "user": new_user,
            "expire": new_expire,
            "status": new_status  # Menambahkan status ke data baru
        }
        return jsonify({'result': 'success'}), 201
    else:
        return jsonify({'result': 'failure', 'message': 'Invalid data'}), 400

@app.route('/status', methods=['GET'])
def get_status():
    # Mengembalikan data status
    return jsonify(status_data)

@app.route('/status', methods=['POST'])
def update_status():
    # Mengambil data dari request JSON
    new_status = request.json.get('status')

    if new_status:
        status_data['status'] = new_status
        return jsonify({'result': 'success', 'status': new_status}), 200
    else:
        return jsonify({'result': 'failure', 'message': 'Invalid status data'}), 400

if __name__ == '__main__':
    app.run(debug=True)