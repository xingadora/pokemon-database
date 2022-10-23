# credit: https://github.com/mdminhazulhaque/html-table-to-json

import json


def html_to_json(content, indent=None):
    soup = content
    rows = soup.find_all("tr")

    headers = {}
    thead = soup.find("thead")
    if thead:
        thead = thead.find_all("th")
        for i in range(len(thead)):
            headers[i] = thead[i].text.strip().lower()
    data = []
    for row in rows:
        cells = row.find_all("td")
        if thead:
            items = {}
            l1 = []
            l2 = {}
            if len(cells) > 0:
                for index in headers:
                    l1.append(headers[index])
                fixDupes(l1, l2)
                for index in l2:
                    items[l2[index]] = cells[index].text
        else:
            items = []
            for index in cells:
                items.append(index.text.strip())
        if items:
            data.append(items)
    return json.dumps(data, indent=indent)


def fixDupes(l1, l2):
    for i, v in enumerate(l1):
        totalcount = l1.count(v)
        count = l1[:i].count(v)
        l2[i] = int(v) + count if totalcount > 1 else v