import requests
import json
from flask import Flask


def get_valutes_list():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url)
    data = json.loads(response.text)
    valutes = list(data['Valute'].values())
    return valutes


app = Flask(__name__)


def create_html(valutes):
    text = '<h1>Курс валют</h1>'
    text += '<table>'
    text += '<tr>'
    for _ in valutes[0]:
        text += f'<th><th>'
    text += '</tr>'

    for valute in valutes:
        if 'USD' == valute['CharCode']:
            color = '<font color="Red">'
        elif 'EUR' == valute['CharCode']:
            color = '<font color="Blue">'
        elif 'GBP' == valute['CharCode']:
            color = '<font color="magenta">'
        else:
            continue

        text += '<tr>'
        for v in valute.values():
            text += f'<td>{color}{v}</font></td>'
        text += '</tr>'

    text += '</table>'
    return text


@app.route("/")
def index():
    valutes = get_valutes_list()
    html = create_html(valutes)
    return html


if __name__ == "__main__":
    app.run()
