from flask import Flask
app = Flask(__name__)


@app.route("/")
def test():
    return "<p> Hello this is awesome</p>"


if __name__ == '__main__':
    app.run(debug=True)