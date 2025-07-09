from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)
df = pd.read_csv('movies.csv')

@app.route('/', methods=['GET', 'POST'])
def recommend():
    recommendations = []
    selected_genre = ""
    if request.method == 'POST':
        selected_genre = request.form['genre'].strip().lower()
        recommendations = df[df['genre'].str.lower() == selected_genre]['title'].tolist()
    return render_template('recommendations.html', movies=recommendations, genre=selected_genre)

if __name__ == '__main__':
    app.run(debug=True)
