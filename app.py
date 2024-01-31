from flask import Flask, render_template, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/')
def current_price():
    response = requests.get('https://min-api.cryptocompare.com/data/price?fsym=XMR&tsyms=EUR').json()
    monero_price = round(response['EUR'], 2)
    return render_template('index.html', monero_price=monero_price)

@app.route('/refresh')
def refresh():
    return redirect(url_for('current_price'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
