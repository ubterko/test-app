from flask import Flask 
app = Flask(__name__)

@app.route("/")

if __name__ == '__main__':
    print("App running at port: 8080")