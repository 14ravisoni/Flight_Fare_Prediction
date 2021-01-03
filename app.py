from datetime import datetime
from flask import Flask
from flask import request, render_template
from models import get_dummy_data
import pandas as pd
from models import prepare_dataframe

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/show_flights', methods=['GET', 'POST'])
def flights():
    if request.method == 'POST':
        airlines = request.form['airlines']
        flying_from = request.form['flying_from']
        flying_to = request.form['flying_to']
        dep_date = datetime.strptime(request.form['dep_date'], '%Y-%m-%d')

        flights = get_dummy_data.get_final_data(airlines, flying_from, flying_to, dep_date)
        df = pd.DataFrame(flights)
        df = prepare_dataframe.process_dataframe(df)
        print(df)

    return "Success"


if __name__ == '__main__':
    app.run(debug=True)

