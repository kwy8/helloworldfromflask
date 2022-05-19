from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "im having a lot of fun!"

if __name__ == "__main__":
    app.run()

