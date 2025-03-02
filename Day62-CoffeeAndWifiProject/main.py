# Udemy: Master Python by building 100 projects in 100 days
# Mar 01, 2025
# Day 62 - Coffee and Wifi project
# Completed by me (Alex Mai)
import re

from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.fields import TimeField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6dozWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe_name = StringField('Name', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired(), URL()])
    open_time = TimeField('Open', validators=[DataRequired()])
    close_time = TimeField('Close', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee',
                                choices=['✘', '☕️', '☕️☕️', '☕️☕️☕️', '☕️☕️☕️☕️', '☕️☕️☕️☕️☕️'],
                                validators=[DataRequired()])
    wifi = SelectField('Wifi',
                       choices=['✘️', '💪', '💪💪', '💪💪💪'],
                       validators=[DataRequired()])
    power = SelectField('Power',
                        choices=['✘️', '🔌', '🔌🔌', '🔌🔌🔌'],
                        validators=[DataRequired()])
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('cafe-data.csv', 'a', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([form.cafe_name.data, form.location.data, form.open_time.data, form.close_time.data,
                                 form.coffee_rating.data, form.wifi.data, form.power.data])
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', 'r', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.DictReader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)

        for cafe in list_of_rows:
            cafe['is_link'] = bool(re.match(r'https:', cafe['Location']))
        # print(list_of_rows)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
