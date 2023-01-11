#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 09:02:23 2023

@author: sabrinajones
"""
from flask import Flask, render_template

app = Flask(__name__, template_folder='/Users/sabrinajones/Desktop/templates')

@app.route('/')
def map():
    return render_template('map.html')

if __name__ == '__main__':
    app.run(port=9000)

import os

print(os.path.dirname(os.path.abspath(__file__)))