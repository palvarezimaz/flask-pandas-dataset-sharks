from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)


@app.route('/')
def home():
    results = None

    if request.args.get('year'):
        results = request.args.get('year')
        print(results)
        path = 'file://localhost/Users/user/fun-projects/flask-dataset-sharks/database/fatal_shark_attacks.xls'

        results = int(results)
        df = pd.read_excel(io=path)
        years = df.loc[df['Year'] == results]
        years = years.drop(columns=["Date", "Time"]).to_dict('index')
        years = list(years.values())
        cases = len(years)
        print(cases)

        try:
            for y in years:
                y["state"] = y["state"].replace("_", ' ')
                y["Activity"] = y["Activity"].replace("_", ' ')
                y["Activity"] = y["Activity"][0].lower() + y["Activity"][1:]
        except:
            pass

        return render_template('index.html', results=results, years=years, cases=cases)

    else:
        return render_template('index.html')


# @app.route('/results')
# def results():
#     results = request.args.get('year')

#     path = 'file://localhost/Users/user/fun-projects/flask-dataset-sharks/database/fatal_shark_attacks.xls'

#     # results = int(results)
#     df = pd.read_excel(io=path)
#     years = df.loc[df['Year'] == results]
#     years = years.drop(columns=["Date", "Time"]).to_dict('index')
#     years = list(years.values())
#     cases = len(years)

#     for y in years:
#         y["state"] = y["state"].replace("_", ' ')

#     return render_template('results.html', results=results, years=years, cases=cases)
