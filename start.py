from flask import Flask
from flask import render_template
from flask import request
import pickle

title = [
'Prosecutors Say Trump Directed Illegal Payments During Campaign',
'Chinese researcher claims first gene-edited babies',
'Migrant group demands Trump either let them in or pay them each $50G to turn around: report',
'Michael Cohen, Trump’s Ex-Lawyer Who Implicated Him in Hush-Money Scandal, Sentenced to 3 Years',
'Korean border troops verify removal of each other\'s posts',
'Health experts offer solutions for unintended consequences of opioid crackdown',
]
website = [
'https://www.nytimes.com/2018/12/07/nyregion/michael-cohen-sentence.html',
'https://apnews.com/4997bb7aa36c45449b488e19ac83e86d',
'https://www.foxnews.com/politics/caravan-migrants-in-mexico-demand-trump-either-let-them-in-u-s-or-pay-them-50000-each-to-go-back-home',
'https://www.nytimes.com/2018/12/12/nyregion/michael-cohen-sentence-trump.html',
'https://www.apnews.com/955d1db2ad1b4788b77d00d5a56bc273',
'https://www.foxnews.com/health/undoing-the-harm-of-the-response-to-the-opioid-overdose-epidemic-health-experts-suggest-solutions',
]

time_limits = [
90,
90,
90,
90,
90,
90,
]

app = Flask(__name__)
debug = False

def getNewPartID():
  if debug:
    return -1
  return pickle.load(open('/home/keydex/cs598kgk/pickle/part_id.p', 'rb'))

def setPartID(a):
  if debug:
    return
  pickle.dump(a, open('/home/keydex/cs598kgk/pickle/part_id.p', 'wb'))
  return

def getPartID():
  return int(request.form['uid'])

def loadResponses(part_id):
  try:
    return pickle.load(open('/home/keydex/cs598kgk/pickle/' + str(part_id) + '_responses.p', 'rb'))
  except:
    return []

# response is expected to be a string.
def saveResponse(response, part_id):
  responses = loadResponses(part_id)
  responses.append(response)
  pickle.dump(responses, open('/home/keydex/cs598kgk/pickle/' + str(part_id) + '_responses.p', 'wb'))

def loadDecisions(part_id):
  try:
    return pickle.load(open('/home/keydex/cs598kgk/pickle/' + str(part_id) + '_decisions.p', 'rb'))
  except:
    return []

#decision is expected to be a string (Yes/No).
def saveDecisions(decision, part_id):
  decisions = loadDecisions(part_id)
  decisions.append(decision)
  print(decisions)
  pickle.dump(decisions, open('/home/keydex/cs598kgk/pickle/' + str(part_id) + '_decisions.p', 'wb'))

def saveFinal(final, part_id):
  pickle.dump(final, open('/home/keydex/cs598kgk/pickle/' + str(part_id) + '_final.p', 'wb'))
  return

def saveSurvey(survey, part_id):
  pickle.dump(survey, open('/home/keydex/cs598kgk/pickle/' + str(part_id) + '_survey.p', 'wb'))
  return




@app.route('/')
def intro():
  return render_template('intro.html')

@app.route('/survey.html', methods=['POST'])
def survey():
  return render_template('survey.html')

@app.route('/intro.html', methods=['POST'])
def instructions():
  participant_id = getNewPartID() + 1
  setPartID(participant_id)

  survey_results = []

  for quest in ['login', 'post', 'time', 'reasons', 'others', 'regret']:
    survey_results.append(request.form[quest])
  saveSurvey(survey_results, participant_id)
  return render_template('instructions.html', uid=participant_id)

@app.route('/input.html', methods=['POST'])
def hello_world():
  participant_id = getPartID()
  step = int(request.form['step'])

  if step > 1:
    decision = request.form['action']
    saveDecisions(decision, getPartID())

  link = {'link':website[step-1], 'title':title[step-1]}
  return render_template('article_page.html', link = link, step=step, time_limit=time_limits[step-1], uid=participant_id)

@app.route('/confirm.html', methods=['POST'])
def my_form_post():
  participant_id = getPartID()
  print (participant_id)
  step = int(request.form['step'])
  text = request.form['text']
  saveResponse(text, getPartID())
  if step > 5:
    next_page = 'final.html'
  else:
    next_page = 'input.html'
  if (((participant_id % 2 == 0) and step <= 3 ) or ((participant_id % 2 == 1) and step >= 4 )):
    play_voice = 1
  else:
    play_voice = 0
  return render_template('confirm_page.html', content=text, step=step+1, next_page=next_page, play_voice=play_voice, uid=participant_id)

@app.route('/final.html', methods=['POST'])
def final_check():
  participant_id = getPartID()
  decision = request.form['action']
  saveDecisions(decision, getPartID())
  responses = loadResponses(getPartID())
  return render_template('results.html', responses = responses, uid=participant_id)

@app.route('/finish.html', methods=['POST'])
def finish():
  final = []
  for i in range(6):
    final.append(request.form[str(i) + '_choice'])
  saveFinal(final, getPartID())
  #return str(loadDecisions(getPartID())) + '\n' + str(final)
  return render_template('thanks.html')

@app.route('/test.html', methods=['POST'])
def testing():
  decision = request.form['action']
  return decision

















