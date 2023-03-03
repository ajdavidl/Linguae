## Sphinx documentation

It uses the [sphinx](https://www.sphinx-doc.org/en/master/) package.

### Requirements:

It's necessary to install two additional packages:

```bash
pip install sphinx-rtd-theme
pip install sphinx-markdown-builder
```

### Update `rst` files:

```bash
sphinx-apidoc -o . ..
```

### Create documentation

In html:

```bash
make html
```
In markdown

```bash
make markdown
```
