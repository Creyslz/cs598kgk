from flask import Flask
from flask import render_template
from flask import request

title = [
'Prosecutors Say Trump Directed Illegal Payments During Campaign',
2,
3,
4,
5,
6,
]
website = [
'https://www.nytimes.com/2018/12/07/nyregion/michael-cohen-sentence.html',
2,
3,
4,
5,
6,
]


app = Flask(__name__)

@app.route('/')
def intro():
  return render_template('intro.html')

@app.route('/input.html', methods=['POST'])
def hello_world():
  step = int(request.form['step'])
  link = {'link':website[step-1], 'title':title[step-1]}
  return render_template('article_page.html', link = link, step=step)

@app.route('/confirm.html', methods=['POST'])
def my_form_post():
  step = int(request.form['step'])
  text = request.form['text']
  if step > 5:
    next_page = 'final.html'
  else:
    next_page = 'input.html'
  return render_template('confirm_page.html', content=text, step=step+1, next_page=next_page)

@app.route('/final.html', methods=['POST'])
def final_check():
  return render_template('survey.html')

@app.route('/finish.html', methods=['POST'])
def finish():
  return render_template('thanks.html')

@app.route('/test.html', methods=['POST'])
def testing():
  decision = request.form['action']
  return decision

















