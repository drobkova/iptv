import json
import argparse
from urllib.request import urlopen


parser = argparse.ArgumentParser()
parser.add_argument('-i', '--init_data', action='store_true')
parser.add_argument('-u', '--update_data', action='store_true')
args = parser.parse_args()


def update_data(url):
    if not url:
        url = "https://gist.githubusercontent.com/nextsux/f6e0327857c88caedd2dab13affb72c1/raw/04441487d90a0a05831835413f5942d58026d321/videos.json"

    response = urlopen(url)
    data = json.loads(response.read())
    fixtures = []
    fields = {}
    for i, entry in enumerate(data):
        fixture = {"pk":     i,
                   "model":  "movies.movie",
                   "fields": entry}

        fixtures.append(fixture)
        for field in entry:
            fields.setdefault(field, set()).add(type(entry[field]))

    with open('fixtures/data.json', 'w') as data_file:
        data_file.write(json.dumps(fixtures, indent=2))

    return fields


def init_data():
    fields = update_data()

    maximum = max([len(x) for x in fields.keys()])
    for field in fields:
        offset = (maximum - len(field)) * ' '
        print(f"{field}{offset} = models.JSONField(null=True, blank=True) #{fields[field]}")

    print(fields.keys())


if args.init_data:
    init_data()
elif args.update_data:
    update_data(None)
