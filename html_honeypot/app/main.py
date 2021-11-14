from flask import Flask, render_template, request, redirect, url_for
from flask.helpers import make_response

app = Flask(__name__)

ips = set()

@app.route('/form')
def form():
    return render_template('form.html')

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
        return redirect(url_for('bot'))
    return redirect(url_for('person'))

@app.route('/person')
def person():
    return render_template('ok_person.html')

@app.route('/bot')
def bot():
    return make_response(render_template('error_bot.html'), 404)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")