from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Här lagrar vi inkommande sensordata
sensor_data = []

# Route för att ta emot sensordata via POST
@app.route('/sensor', methods=['POST'])
def receive_sensor_data():
    data = request.get_json()
    if "temperature" in data and "humidity" in data:
        # Lägg till datan i vår lista
        sensor_data.append(data)
        return jsonify({"status": "success", "data_received": data}), 200
    else:
        return jsonify({"status": "error", "message": "Invalid data"}), 400

# Route för att visa sensordatan
@app.route('/')
def index():
    return render_template('index.html', sensor_data=sensor_data)

if __name__ == '__main__':
    app.run(debug=True)
