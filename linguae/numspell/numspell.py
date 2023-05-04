"""
Module that converts integer numbers in its spelling.
"""


def num2words(lang, num):
    """
    This function takes a language and an integer between 0 and 999,999 and returns a string with the cardinal number spelling for that language.

    Parameters
    ----------
    language : str
        Language desired.
        example: 'en', 'pt', 'es', 'it'
    num : int 
        The integer to be converted to words. Must be between 0 and 999,999.

    Returns
    -------
    str: A string with the cardinal number spelling in the languages asked.

    Examples
    --------
    >>> linguae.num2words('en', 123456)
    'one hundred twenty three thousand four hundred fifty six'
    >>> linguae.num2words('es', 123456)
    'ciento veinte y tres mil cuatrocientos cincuenta y seis'
    >>> linguae.num2words('pt',123456)
    'cento e vinte e três mil quatrocentos e cinquenta e seis'
    """
    if lang == 'en':
        return __num2wordsEng(num)
    elif lang == 'es':
        return __num2wordsSpa(num)
    elif lang == 'pt':
        return __num2wordsPor(num)
    elif lang == 'it':
        return __num2wordsIta(num)
    else:
        return "Sorry, language not supported."


def __num2wordsEng(num):
    """
    This function takes an integer between 0 and 999,999 and returns a string with the cardinal number spelling in English.

    Parameters
    ----------
    num : int 
        The integer to be converted to words. Must be between 0 and 999,999.

    Returns
    -------
    str: A string with the cardinal number spelling in English.

    Examples
    --------
    >>> linguae.numspell.numspell.__num2wordsEng(123456)
    'one hundred twenty three thousand four hundred fifty six'
    """
    ones = ['', 'one', 'two', 'three', 'four',
            'five', 'six', 'seven', 'eight', 'nine']
    tens = ['', '', 'twenty', 'thirty', 'forty',
            'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
             'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    if num == 0:
        return 'zero'
    elif num < 0:
        return 'minus ' + __num2wordsEng(abs(num))
    else:
        if num < 10:
            return ones[num]
        elif num < 20:
            return teens[num - 10]
        elif num < 100:
            return tens[num // 10] + ' ' + ones[num % 10]
        elif num < 1000:
            return ones[num // 100] + ' hundred ' + __num2wordsEng(num % 100)
        elif num < 1000000:
            return __num2wordsEng(num // 1000) + ' thousand ' + __num2wordsEng(num % 1000)
        else:
            return 'Number out of range.'


def __num2wordsSpa(num):
    """
    This function takes an integer between 0 and 999,999 and returns a string with the cardinal number spelling in Spanish.

    Parameters
    ----------
    num : int 
        The integer to be converted to words. Must be between 0 and 999,999.

    Returns
    -------
    str: A string with the cardinal number spelling in Spanish.

    Examples
    --------
    >>> linguae.numspell.numspell.__num2wordsSpa(123456)
    'ciento veinte y tres mil cuatrocientos cincuenta y seis'
    """
    ones = ['', 'uno', 'dos', 'tres', 'cuatro',
            'cinco', 'seis', 'siete', 'ocho', 'nueve']
    tens = ['', '', 'veinte', 'treinta', 'cuarenta',
            'cincuenta', 'sesenta', 'setenta', 'ochenta', 'noventa']
    teens = ['diez', 'once', 'doce', 'trece', 'catorce', 'quince',
             'dieciséis', 'diecisiete', 'dieciocho', 'diecinueve']
    if num == 0:
        return 'cero'
    elif num < 0:
        return 'menos ' + __num2wordsSpa(abs(num))
    else:
        if num < 10:
            return ones[num]
        elif num < 20:
            return teens[num - 10]
        elif num < 100:
            return tens[num // 10] + ' y ' + ones[num % 10] if ones[num % 10] != 'uno' and ones[num % 10] != '' else tens[num // 10] + ones[num % 10]
        elif num < 1000:
            if num % 100 == 0:
                if num // 100 == 1:
                    return 'cien'
                else:
                    return ones[num // 100] + 'cientos'
            else:
                if num // 100 == 1:
                    return 'ciento ' + __num2wordsSpa(num % 100)
                else:
                    return ones[num // 100] + 'cientos ' + __num2wordsSpa(num % 100)
        elif num < 1000000:
            if num % 1000 == 0:
                if num // 1000 == 1:
                    return 'mil'
                else:
                    return __num2wordsSpa(num // 1000) + ' mil'
            else:
                if num // 1000 == 1:
                    return 'mil ' + __num2wordsSpa(num % 1000)
                else:
                    return __num2wordsSpa(num // 1000) + ' mil ' + __num2wordsSpa(num % 1000)
        else:
            return 'Number out of range.'


def __num2wordsPor(num):
    """
    This function takes an integer between 0 and 999,999 and returns a string with the cardinal number spelling in Portuguese.

    Parameters
    ----------
    num : int 
        The integer to be converted to words. Must be between 0 and 999,999.

    Returns
    -------
    str: A string with the cardinal number spelling in Portuguese.

    Examples
    --------
    >>> linguae.numspell.numspell.__num2wordsPor(123456)
    'cento e vinte e três mil quatrocentos e cinquenta e seis'
    """
    ones = ['', 'um', 'dois', 'três', 'quatro',
            'cinco', 'seis', 'sete', 'oito', 'nove']
    tens = ['', '', 'vinte', 'trinta', 'quarenta', 'cinquenta',
            'sessenta', 'setenta', 'oitenta', 'noventa']
    teens = ['dez', 'onze', 'doze', 'treze', 'catorze', 'quinze',
             'dezesseis', 'dezessete', 'dezoito', 'dezenove']
    hundreds = ['', 'cento', 'duzentos', 'trezentos', 'quatrocentos',
                'quinhentos', 'seiscentos', 'setecentos',
                'oitocentos', 'novecentos']
    if num == 0:
        return 'zero'
    elif num < 0:
        return 'menos ' + __num2wordsPor(abs(num))
    else:
        if num < 10:
            return ones[num]
        elif num < 20:
            return teens[num - 10]
        elif num < 100:
            return tens[num // 10] + ' e ' + ones[num % 10] if ones[num % 10] != '' else tens[num // 10] + ones[num % 10]
        elif num < 1000:
            if num % 100 == 0:
                if num // 100 == 1:
                    return 'cem'
                else:
                    return hundreds[num // 100]
            else:
                return hundreds[num // 100] + ' e ' + __num2wordsPor(num % 100)
        elif num < 1000000:
            if num % 1000 == 0:
                if num // 1000 == 1:
                    return 'mil'
                else:
                    return __num2wordsPor(num // 1000) + ' mil'
            else:
                if num // 1000 == 1:
                    return 'mil ' + __num2wordsPor(num % 1000)
                else:
                    return __num2wordsPor(num // 1000) + ' mil ' + __num2wordsPor(num % 1000)
        else:
            return 'Number out of range.'


def __num2wordsIta(num):
    """
    This function takes an integer between 0 and 999,999 and returns a string with the cardinal number spelling in Italian.

    Parameters
    ----------
    num : int 
        The integer to be converted to words. Must be between 0 and 999,999.

    Returns
    -------
    str: A string with the cardinal number spelling in Italian.

    Examples
    --------
    >>> linguae.numspell.numspell.__num2wordsIta(123456)
    'centoventitremilaquattrocentocinquantasei'
    """
    ones = ['', 'uno', 'due', 'tre', 'quattro',
            'cinque', 'sei', 'sette', 'otto', 'nove']
    tens = ['', 'dieci', 'venti', 'trenta', 'quaranta',
            'cinquanta', 'sessanta', 'settanta', 'ottanta', 'novanta']
    teens = ['dieci', 'undici', 'dodici', 'tredici', 'quattordici',
             'quindici', 'sedici', 'diciassette', 'diciotto', 'diciannove']
    if num == 0:
        return 'zero'
    elif num < 0:
        return 'meno ' + __num2wordsIta(abs(num))
    elif num < 10:
        return ones[num]
    elif num < 20:
        return teens[num - 10]
    elif num < 100:
        if num % 10 == 1 or num % 10 == 8:
            return tens[num // 10][:-1] + ones[num % 10]
        else:
            return tens[num // 10] + ones[num % 10]
    elif num < 1000:
        if num % 100 == 0:
            if num // 100 == 1:
                return 'cento'
            else:
                return ones[num // 100] + 'cento'
        elif num % 100 < 10:
            if num // 100 == 1:
                return 'cento' + ones[num % 100]
            else:
                return ones[num // 100] + 'cento' + ones[num % 100]
        elif num % 100 < 20:
            if num // 100 == 1:
                return 'cento' + teens[num % 10]
            else:
                return ones[num // 100] + 'cento' + teens[num % 10]
        else:
            if num // 100 == 1:
                if num % 10 == 1 or num % 10 == 8:
                    return 'cento' + tens[(num % 100) // 10][:-1] + ones[num % 10]
                else:
                    return 'cento' + tens[(num % 100) // 10] + ones[num % 10]
            else:
                if num % 10 == 1 or num % 10 == 8:
                    return ones[num // 100] + 'cento' + tens[(num % 100) // 10][:-1] + ones[num % 10]
                else:
                    return ones[num // 100] + 'cento' + tens[(num % 100) // 10] + ones[num % 10]
    elif num < 1000000:
        if num % 1000 == 0:
            if num // 1000 == 1:
                return 'mille'
            else:
                return __num2wordsIta(num // 1000) + 'mila'
        else:
            if num // 1000 == 1:
                return 'mille' + __num2wordsIta(num % 1000)
            else:
                return __num2wordsIta(num // 1000) + 'mila' + __num2wordsIta(num % 1000)
    else:
        return 'Number out of range.'
