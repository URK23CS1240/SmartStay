from flask import Flask, render_template, request

app = Flask(__name__)

rooms = {"101": "Available", "102": "Available"}

@app.route('/')
def home():
    return render_template('index.html', rooms=rooms)

@app.route('/book', methods=['POST'])
def book():
    room = request.form['room']
    if rooms[room] == "Available":
        rooms[room] = "Booked"
    return render_template('index.html', rooms=rooms)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)