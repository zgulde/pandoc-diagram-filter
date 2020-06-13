# Pandoc Diagram Filter

A pandoc filter that renders graphviz and plantuml diagrams in code blocks and
embeds them through base64 encoding in HTML output.

Not tested for other output formats.

## Installation

1. Install `graphviz` and/or `plantuml` (depending on which you plan to use)

1. Install python3 and panflute

    ```
    python3 -m pip install panflute
    ```

1. Install this filter

    ```
    # clone this repo
    git clone https://github.com/zgulde/pandoc-diagram-filter.git
    # cd to the repo
    cd pandoc-diagram-filter
    # install the filter
    make install
    ```

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
