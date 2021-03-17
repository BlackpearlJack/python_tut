book = {}
book['tom'] = {
    "name": "tom",
    "address": "1 red street, NY",
    "phone": 23423423
}

book['bob'] = {
    "name": "bob",
    "address": "1 green street, NY",
    "phone": 75846932
}


import json
s=json.dumps(book)
with open("C:/Users/ICTA NOC/Documents/data/book.txt","w") as f:
    f.write(s)