import pickle

ids = [1]
for part_id in ids:
  for content in ['_responses.p', '_decisions.p', '_final.p', '_survey.p']:
    print(str(pickle.load(open('pickle/' + str(part_id) + content, 'rb'))))