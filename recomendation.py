from flask import Flask, render_template, url_for, request, redirect, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///HiTech.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Cards(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    price = db.Column(db.Integer)
    property_1 = db.Column(db.String())
    image_link = db.Column(db.String())
    prod_link = db.Column(db.String())


def FindPatter(card):
    pattern_string = ''

    title = card[0].prod_link
    title = title.split('/')

    rem_mas = [1, 0, -1]
    [title.pop(i) for i in range(0, len(title) - 1) if len(title[i]) == 0]
    [title.pop(i) for i in rem_mas]

    for el in title:
        pattern_string += f'{el}/'

    search = "%{}%".format(pattern_string)

    cards = Cards.query.filter(Cards.prod_link.like(search)).all()
    card += cards
    return card


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        value = request.form['Value']
        cards = []

        if len(value) > 0:
            # cards = Cards.query.limit(10).all()
            cards = Cards.query.filter_by(id=value).all()
            cards = FindPatter(cards)

        return render_template('index.html', cards=cards, value=value)
    else:
        return render_template('base.html')


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
