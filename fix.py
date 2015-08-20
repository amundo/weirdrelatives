import json

db = json.load(open('db.json'))

def remove(o, attr, nukeme):
  if attr in o: 
    o[attr] = o[attr].replace(nukeme, '')
  return o

def nodash(o): 
  return remove(o, 'source', u'\u2014')

def noparen(o): 
  o = remove(o, 'note', u'(')
  return remove(o, 'note', u')')

db = map(nodash, db)
db = map(noparen, db)

print json.dumps(db , indent=2)
