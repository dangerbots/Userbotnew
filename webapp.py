from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def start():
    return "DANGERCAT Started Successfully"

os.system("python3 -m TelethonCat")
app.run(port=5000)
