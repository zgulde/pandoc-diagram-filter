#!/usr/bin/env python3

from base64 import b64encode
from time import strftime
import panflute
from subprocess import check_output

# PLANTUML_COMMAND = 'java -jar plantuml.jar -tsvg -pipe'.split()
PLANTUML_COMMAND = 'plantuml -tsvg -pipe'.split()
GRAPHVIZ_COMMAND = 'dot -Tsvg'.split()

def log(msg):
    with open('debug.log', 'a+') as f:
        f.write('\n[{}] {}'.format(strftime('%Y-%m-%d %H:%M:%S'), msg))

def action(elem, doc):
    if isinstance(elem, panflute.CodeBlock) and 'graphviz' in elem.classes:
        svg = check_output(GRAPHVIZ_COMMAND, input=elem.text.encode('utf8'))
        b64data = b64encode(svg).decode('utf8')
        url = 'data:image/svg+xml;base64,{}'.format(b64data)
        return panflute.Para(panflute.Image(url=url))
    elif isinstance(elem, panflute.CodeBlock) and 'uml' in elem.classes:
        svg = check_output(PLANTUML_COMMAND, input=elem.text.encode('utf8'))
        b64data = b64encode(svg).decode('utf8')
        url = 'data:image/svg+xml;base64,{}'.format(b64data)
        return panflute.Para(panflute.Image(url=url))

def main(doc=None):
    return panflute.run_filter(action, doc)

if __name__ == '__main__':
    main()

