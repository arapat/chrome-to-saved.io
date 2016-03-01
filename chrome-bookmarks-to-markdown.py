
import requests

f = open('<chrome-bookmark-file>')
url = 'http://devapi.saved.io/v1/create'
apikey = '<your_key>'

def parse(w):
    r = {}
    p1, p2, none = w.split(">")
    p2, p3 = p2.split("</")
    r['content'] = p2
    r['type'] = p3
    for s in p1.split()[1:]:
        k, v = s.split('=', 1)
        r[k] = v[1:-1]
    return r


DL = "<DL>"
RDL = "</DL>"
DT = "<DT>"
level = -1

listname = None
data = []
for w in f:
    w = w.strip()
    if w.startswith(DL):
        level = level + 1
    elif w.startswith(RDL):
        level = level - 1
    elif w.startswith(DT):
        w = w[4:]
        info = parse(w)
        if info['type'] == 'A':
            data.append({'title': info['content'], 'url': info['HREF'], 'list': listname})
        elif info['type'] == 'H3':
            listname = info['content']
        else:
            raise

for item in data:
    item['token'] = apikey
    r = requests.post(url, data = item)
    if r.status_code != 200 or eval(r.text.replace('false', "False"))['is_error']:
        print('Failed.')
        print(r.status_code)
        print(r.text)
        break
print('Done.')
