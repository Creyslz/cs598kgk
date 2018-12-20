import pickle

ids = [0,1,2,3,4,5,7,8,10,11]
for part_id in ids:
  #print('\n' + str(part_id))
  for content in ['_survey.p']:#['_responses.p', '_decisions.p', '_final.p', '_survey.p']:
    data = pickle.load(open('pickle/' + str(part_id) + content, 'rb'))
    print(str(part_id) + ' & ' + ' & '.join(data))
    #print(str(pickle.load(open('pickle/' + str(part_id) + content, 'rb'))))
