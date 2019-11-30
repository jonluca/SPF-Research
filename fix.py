top100 = open('fortune.json').read()

import json

top100 = json.loads(top100)

for domain in top100.keys():
    top100[domain] = json.loads(top100[domain])

with open('fortune.json','w') as out:
    out.write(json.dumps(top100))
    out.close
