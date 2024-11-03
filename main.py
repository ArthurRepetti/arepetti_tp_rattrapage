from flask import Flask
from flask_cors import CORS
from booking_controller import booking_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(booking_bp)

@app.get('/hello')
def hello_world():
  return {"message": "Hello World"}

if __name__ == "__main__":
    app.run(debug=False)