from flask import Flask, render_template, request
import requests

app = Flask(__name__)
API_KEY = 'AIzaSyCh_yKuUVwJyiB4jrA7GBQhFRmWNS4lUXY'

@app.route('/', methods=['GET', 'POST'])
def index():
    videos = []
    if request.method == 'POST':
        search_query = request.form['query']
        url = f'https://www.googleapis.com/youtube/v3/search?part=snippet&q={search_query}&type=video&maxResults=5&key={API_KEY}'
        response = requests.get(url)
        data = response.json()
        videos = [{
            'title': item['snippet']['title'],
            'thumbnail': item['snippet']['thumbnails']['medium']['url'],
            'channel': item['snippet']['channelTitle'],
            'videoId': item['id']['videoId']
        } for item in data['items']]
    return render_template('results.html', videos=videos)

if __name__ == '__main__':
    app.run(debug=True)
