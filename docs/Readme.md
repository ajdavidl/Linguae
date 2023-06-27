## Sphinx documentation

It uses the [sphinx](https://www.sphinx-doc.org/en/master/) package.

### Requirements:

It's necessary to install two additional packages:

```bash
pip install sphinx-rtd-theme
pip install sphinx-markdown-builder
```

### Update `rst` files:

Run the following commands to create the rst files of the new modules.

```bash
cd docs/
sphinx-apidoc -o . ..
```
Edit the `linguae.rst` file to include new modules in the subpackage index.

### Create documentation

In html:

```bash
make html
```
In markdown:

```bash
make markdown
```
