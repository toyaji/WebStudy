# -*- coding: utf-8 -*-

############Module import############
from __future__ import print_function
import json
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
############Module import############

app = Flask(__name__)

firstMenu = ["인사"]


@app.route("//message", methods=['GET', 'POST'])
@app.route("/message", methods=['GET', 'POST'])
def message():
    userRequest = json.loads(request.get_data())

    ##메시지 부분 예시
    if userRequest['content'] == u"인사":
        return """{"message": {"text":" 안녕하세오 카톡봇이에오."},"keyboard":\
  {      "type": "buttons","buttons": """ + '["' + '","'.join(firstMenu) + '"]' + """ }}"""


    else:
        return """{"message": {"text":" 지원하지 않는 기능입니다.."},"keyboard": {  "type": "buttons","buttons": """ + '["' + '","'.join(
            firstMenu) + '"]' + """ }}"""


@app.route("//keyboard", methods=['GET', 'POST'])
@app.route("/keyboard", methods=['GET', 'POST'])
def key():
    return """{ "type" : "buttons", "buttons" : """ + '["' + '","'.join(firstMenu) + '"]' + """}"""


if __name__ == "__main__":
    app.run(host="192.168.0.51", port=5000, threaded=True)
