# Pandoc Diagram Filter

## Installation

```
# clone this repo
git clone https://github.com/zgulde/pandoc-diagram-filter.git
# cd to the repo
cd pandoc-diagram-filter
# install the filter
make install
```

Make sure you have `graphviz` and `plantuml` installed (you only have to have
one or the other if you only plan to use one or the other).

## Usage

```
pandoc --filter diagram doc.md
```

Any code blocks in `doc.md` with the language of `graphviz` will be run through
`dot` and embedded in the html output as a base64 encoded svg within an `img` tag.

Any code blocks in `doc.md` with the language of `uml` will be run through
`plantuml` and embedded in the the same way.

## Examples

See `example.md` and `example.html`.

`example.html` is rendered with the command below:

```
pandoc --filter diagram example.md > example.html
```
