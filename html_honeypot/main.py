from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/validate', methods=["POST"])
def validate():
    data = request.form
    if data.get('fake_name') or data.get('fake_email'):
        return redirect(url_for('bot'))
    return redirect(url_for('person'))

@app.route('/person')
def person():
    return render_template('ok_person.html')

@app.route('/bot')
def bot():
    return render_template('error_bot.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")