# QuickRead News Summarizer
QuickRead is a full-stack web app that summarizes news articles using Hugging Face’s BART transformer model.

It combines a **Python Flask** backend for summarization with a compact lightweight **Node.js + Express** frontend that serves as the UI and proxies API requests.

## Features
- Paste any online news article URL and get an informing summary in seconds
- Clean, responsive UI built with TailwindCSS
- Summarization powered by facebook/bart-large-cnn
- Flask backend for NLP + Node/Express server for static hosting and proxying
- Copy-to-clipboard support for summaries

## Installation & Setup
**1.** Clone the local repository
```
git clone https://github.com/kalenmcmillan/news-summarizer.git
cd news-summarizer
```
**2.** Setup the python summarization backend
```
cd core-service
python -m venv venv
source venv/bin/activate   # (use venv\Scripts\activate on Windows)
pip install -r requirements.txt
python app.py
```
This starts flask on `http://localhost:3001`

**3.** Set up the Node.js frontend server
```
npm install
npm start
```
This runs the Express server on `http://localhost:3000`

### License
MIT License © 2025 Kalen McMillan