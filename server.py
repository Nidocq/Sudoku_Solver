#!/usr/bin/env python3
from flask import Flask
from main import *

app = Flask(__name__)

@app.route('/')
def startup():
    return f"""<p> Here you goooo: 
    </br>
    {server_solve()}
    </p>"""