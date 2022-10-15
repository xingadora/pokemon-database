import requests
from bs4 import BeautifulSoup
from htmltojson import *
from getlinkandoutput import *

outputFile = 'a'
link = 'b'


def generate_stats(generation):

    getlinkandoutput(generation)

    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.table
    thead = table.thead
    tbody = table.tbody
    rows = tbody.find_all('tr')
    # row = rows[2]

    nonestr = 'None'


    tt = thead.find_all('th')[2]
    tag = soup.new_tag('th')
    tag.string = 'type2'
    atag = tt.insert_after(tag)

    tr = tt.string.replace_with('type1')


    for row in rows:

        t = row.find(class_='cell-icon').find_all('a')

        type1tag = t[0].wrap(soup.new_tag('td'))
        type2tag = soup.new_tag('td')
        type2tag.string = nonestr
        if 1 < len(t):
            type2tag = t[1].wrap(soup.new_tag('td'))

        rp = row.find_all('td')[2]
        rc = rp.replace_with(type1tag)

        a = row.find_all('td')[2]
        a.insert_after(type2tag)



    with open(outputFile, "a") as o:
        o.write(html_to_json(table))