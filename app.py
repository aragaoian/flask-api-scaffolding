from dotenv import load_dotenv
load_dotenv()

import os
from flask import render_template
from App import create_app

app = create_app()

APP_PORT = os.getenv("APP_PORT")


@app.route("/")  # default endpoint
def index():
    return render_template("Index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=APP_PORT, debug=True)
    # serve(app, host="0.0.0.0", port=APP_PORT)
