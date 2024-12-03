import json

PATH_TO_JSON = 'docs/publications.json'
PATH_TO_BIB = 'docs/publications.bib'

input = open(PATH_TO_JSON, 'r')
output = open(PATH_TO_BIB, 'w')


data = json.load(input)
pubs = data['publications']




article = lambda citekey, title, author, journal, volume, number, pages, year, url: f'''@article{{{citekey},
  title = {{{title}}},
  author = {{{" and ".join(author)}}},
  journal = {{{journal}}},
  volume = {{{volume}}},
  number = {{{number}}},
  pages = {{{pages}}},
  year = {{{year}}},
  url = {{{url}}},
}}

'''

inproceedings = lambda citekey, title, author, booktitle, year, url: f'''@inproceedings{{{citekey},
  title = {{{title}}},
  author = {{{" and ".join(author)}}},
  booktitle = {{{booktitle}}},
  year = {{{year}}},
  url = {{{url}}},
}}

'''

misc = lambda citekey, title, author, year, url: f'''@misc{{{citekey},
  title = {{{title}}},
  author = {{{" and ".join(author)}}},
  year = {{{year}}},
  url = {{{url}}},
}}

'''


thesis = lambda citekey, title, author, school, year, url: f'''@thesis{{{citekey},
  title = {{{title}}},
  author = {{{" and ".join(author)}}},
  school = {{{school}}},
  year = {{{year}}},
  url = {{{url}}},
}}

'''


for pub in pubs:
    if pub['type'] == 'article':
        output.write(article(pub['citekey'], pub['title'], pub['author'], pub['journal'], pub['volume'], pub['number'], pub['pages'], pub['year'], pub['url']))
    elif pub['type'] == 'inproceedings':
        output.write(inproceedings(pub['citekey'], pub['title'], pub['author'], pub['booktitle'], pub['year'], pub['url']))
    elif pub['type'] == 'misc':
        output.write(misc(pub['citekey'], pub['title'], pub['author'], pub['year'], pub['url']))
    elif pub['type'] == 'thesis':
        output.write(thesis(pub['citekey'], pub['title'], pub['author'], pub['school'], pub['year'], pub['url']))
    else:
        raise ValueError(f"Unknown type: {pub['type']}")

input.close()
output.close()


