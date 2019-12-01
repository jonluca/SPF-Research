import json
from collections import Counter

top100 = json.loads(open('fortune.json').read())

has_dnssec = 0
all_alls = []
for domain in top100.keys():
    if top100[domain]['dnssec']:
        has_dnssec += 1
    if top100[domain]['spf'] is not None and 'parsed' in top100[domain]['spf']:
        append = ''
        if 'include' in top100[domain]['spf']['record']:
            append = '_with_include'
        all_alls.append(top100[domain]['spf']['parsed']['all']+append)
c = Counter(all_alls)
print(c)
print(has_dnssec)
