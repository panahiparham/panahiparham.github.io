

def generate_publication_entry(pub: dict[str, str], link: bool = False) -> str:
    entry = ''
    entry += ', '.join(pub['author'])
    entry += '. '
    entry += f'({pub["year"]}). '
    if link:
        entry += f'<a href="{pub.get("url", "#")}">{pub["title"]}</a>. '
    else:
        entry += f'{pub["title"]}. '

    match pub['type']:
        case 'inproceedings':
            venue = pub['booktitle']
        case 'article':
            venue = pub['journal']
        case 'misc':
            venue = pub['venue']
        case 'thesis':
            venue = pub['school']
        case _:
            raise ValueError(f"Unknown type: {pub['type']}")

    entry += f'<i>{venue}</i>.'
    return entry




index_template: str
publications_template: str

def populate_template(template: str) -> str:
    return template

with open('src/template/index_template.html', 'r') as input:
    index_template = input.read()


with open('src/template/publications_template.html', 'r') as input:
    publications_template = input.read()

publications = populate_template(publications_template)
index = index_template.replace('[[publications]]', publications)


with open('index.html', 'w') as output:
    output.write(index)


import json

with open('docs/publications.json', 'r') as f:
    pubs = json.load(f)['publications']

    for pub in pubs:
        print(generate_publication_entry(pub, link = True))
