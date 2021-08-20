from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField(label='Cafe name', validators=[DataRequired()])
    url = StringField(label='Cafe location on google map(URL)', validators=[DataRequired(), URL()])
    opening_time = StringField(label='Opening time. eg: 8AM', validators=[DataRequired()])
    closing_time = StringField(label='Closing time. eg: 11PM', validators=[DataRequired()])
    coffee = SelectField(label='Coffee Rating', validators=[DataRequired()], choices=[('☕'), ('☕☕'), ('☕☕☕'), ('☕☕☕☕'), ('☕☕☕☕☕')], )
    wifi = SelectField(label='Wifi Strength Rating', validators=[DataRequired()], choices=[('✘'), ('💪'), ('💪💪'), ('💪💪💪'), ('💪💪💪💪'), ('💪💪💪💪💪')], )
    socket = SelectField(label='Power Socket Availability', validators=[DataRequired()], choices=[('✘'), ('🔌'), ('🔌🔌'), ('🔌🔌🔌'), ('🔌🔌🔌🔌'), ('🔌🔌🔌🔌🔌')], )


    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['POST', 'GET'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        # field_names = ['Cafe Name', 'Location', 'Open', 'Close', 'Coffee', 'Wifi', 'Power']
        # form_data_dict = {
        #     "Cafe Name": form.cafe.data,
        #     "Location": form.url.data,
        #     "Open": form.opening_time.data,
        #     "Close": form.closing_time.data,
        #     "Coffee": form.coffee.data,
        #     "Wifi": form.wifi.data,
        #     "Power": form.socket.data
        # }
        with open('cafe-data.csv', 'a', newline='', encoding="utf8") as csv_data:
            writer = csv.writer(csv_data)
            writer.writerow([f'{form.cafe.data}', f'{form.url.data}', f'{form.opening_time.data}', f'{form.closing_time.data}', f'{form.coffee.data}', f'{form.wifi.data}', f'{form.socket.data}'])
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open(r"C:\Users\uzzal\Downloads\Compressed\coffee-and-wifi\cafe-data.csv", newline='', encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
