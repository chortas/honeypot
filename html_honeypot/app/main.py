from flask import Flask, render_template, request, redirect, url_for, session
from flask.helpers import make_response

app = Flask(__name__)

ACCEPTED_COOKIE = "person-cookie"

BOT_COOKIE = "bot-cookie"

ips = set()

def check_if_not_logged(cookie):
    if not cookie:
        return make_response(redirect(url_for('form')))

def check_if_person(cookie):
    if cookie and cookie == ACCEPTED_COOKIE:
        return make_response(redirect(url_for('person')))

def check_if_bot(cookie):
    if cookie and cookie != ACCEPTED_COOKIE:
        return make_response(redirect(url_for('person')))

@app.route('/')
def home():
    return redirect(url_for('form'))

@app.route('/form')
def form():
    cookie = request.cookies.get('secret')
    resp = check_if_person(cookie) or check_if_bot(cookie)
    return resp or render_template('form.html')

@app.route('/validate', methods=["POST"])
def validate():
    data = request.form
    ip = request.remote_addr
    if ip in ips or data.get('fake_name') or data.get('fake_email'):
        if ip not in ips:
            print("Malicious ip not registered")
            ips.add(ip)
        else:
            print("Already registered malicious ip")
        resp = make_response(redirect(url_for('bot')))
        resp.set_cookie('secret', BOT_COOKIE)
        return resp
    resp = make_response(redirect(url_for('person')))
    resp.set_cookie('secret', ACCEPTED_COOKIE)
    return resp

@app.route('/person')
def person():
    cookie = request.cookies.get('secret')
    resp = check_if_not_logged(cookie) or check_if_bot(cookie)
    return resp or render_template('ok_person.html')

@app.route('/bot')
def bot():
    cookie = request.cookies.get('secret')
    resp = check_if_not_logged(cookie)
    return resp or make_response(render_template('error_bot.html'), 404)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")