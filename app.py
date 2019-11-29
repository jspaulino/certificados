from flask import Flask

app = Flask(__name__,static_folder='front')

if __name__ == "__main__":
    app.run()