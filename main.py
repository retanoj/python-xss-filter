#!/usr/bin/env python
#coding=utf-8
__author__ = 'Phtih0n'
import pxfilter
from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    html = {
        'originHtml': '',
        'cleanHtml': ''
    }
    if request.method == 'POST' and request.form.get("content"):
        content = request.form.get("content")
        html['originHtml'] = content
        parser = pxfilter.XssHtml()
        parser.feed(content)
        parser.close()
        html['cleanHtml'] = parser.getHtml()

    return render_template('xsshtml.html', html=html)

if __name__ == "__main__":
    app.run(debug=True)