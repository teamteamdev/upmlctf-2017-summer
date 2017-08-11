#!/bin/env python

import bcrypt
from flask import Flask,request,abort,send_from_directory

application = Flask(__name__)

USAGE = 'I\'ll serve a file to those who know how to ask.'

@application.route('/',methods=['GET'])
def serious_server():
    return USAGE

@application.route('/blabla',methods=['GET'])
def seriuos_server2():
    foo = request.args.get('foo','')
    if bcrypt.checkpw(bytes(foo,'utf-8'),b'$2b$12$vxa5YDm8oU0hloltpVybn.j0U7t0RO1yVrYRfbJxChalsbXIVmTXu'):
        return send_from_directory('/tmp', 'flag')
    else:
        abort(403)

    abort(400)
