from flask import Flask, request, jsonify
from newspaper import Article
from transformers import pipeline

app = Flask(__name__)
summarizer = pipeline('summarization', model = 'facebook/bart-large-cnn')

@app.route('/summarize', methods = ['POST'])
def summarize():
    data = request.get_json()
    url = data.get('url')
    if not url:
        return jsonify({'error': 'No URL Provided'}), 400

    article = Article(url)
    try:
        article.download()
        article.parse()
    except Exception as e:
        return jsonify({'error': 'Error Downlinading Article'}), 500

    text = article.text
    summary = summarizer(text, max_length = 150, min_length = 30, do_sample = False)
    
    return jsonify({'summary': summary[0]['summary_text']})

if __name__ == '__main__':
    app.run(port = 5001)
