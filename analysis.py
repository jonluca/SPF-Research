import json
from collections import Counter

top100 = json.loads(open('top100.json').read())

has_dnssec = 0
all_alls = []
ptags = []
valid = 0
for domain in top100.keys():
    if top100[domain]['dnssec']:
        has_dnssec += 1
    if top100[domain]['spf'] is not None and 'parsed' in top100[domain]['spf']:
        append = ''
        if 'include' in top100[domain]['spf']['record']:
            append = '_with_include'
        all_alls.append(top100[domain]['spf']['parsed']['all'] + append)
    # if not top100[domain]['spf']['valid']:
    # print(domain)
    # print(top100[domain]['spf']['record'])
    # print(top100[domain]['spf']['error'])
    # print()
    # if top100[domain]['spf']['record'] is None:
    # valid += 1

    if top100[domain]['dmarc']['record'] is not None and top100[domain]['dmarc']['valid']:
        valid += 1
        ptags.append(top100[domain]['dmarc']['tags']['adkim']['value'])
        print(top100[domain]['dmarc'])

print(valid)
print(ptags)
print(len(ptags))
c = Counter(ptags)
print(c)
# print(valid)
# print(has_dnssec)
