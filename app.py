import os
import socket

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    message = os.environ.get("MESSAGE", "Hello")
    return f"""<!doctype html>
<html lang="pl">
<head><meta charset="utf-8"><title>SKNI Kod demo</title></head>
<body style="font-family: sans-serif; background: #11161d; color: #f0eee8; padding: 4rem;">
  <h1>{message}</h1>
  <p>Kontener: {socket.gethostname()}</p>
</body>
</html>"""


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
