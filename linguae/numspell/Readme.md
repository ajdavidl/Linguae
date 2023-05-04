# Numspell module

Number spelling module. It converts integer numbers in its spelling.

Main function:

```
linguae.num2words : takes a language and an integer between 0 and 999,999 and returns a string with the cardinal number spelling for that language.
```

Examples:

```python
>>> linguae.num2words('en', 123456)
'one hundred twenty three thousand four hundred fifty six'
>>> linguae.num2words('es', 123456)
'ciento veinte y tres mil cuatrocientos cincuenta y seis'
>>> linguae.num2words('pt',123456)
'cento e vinte e três mil quatrocentos e cinquenta e seis'
```


