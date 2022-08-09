from flask import Flask, render_template
from kafka import KafkaConsumer
app = Flask(__name__)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

@app.route("/")
def index():
    return render_template('index.html')
