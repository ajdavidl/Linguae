"""
Module that convert integer numbers in its spelling.
"""


def num2words(lang, num):
    if lang == 'en':
        return __num2wordsEng(num)
    elif lang == 'es':
        return __num2wordsSpa(num)
    elif lang == 'pt':
        return __num2wordsPor(num)
    else:
        return "Sorry, language not supported."


def __num2wordsEng(num):
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
            return 'number out of range'


def __num2wordsSpa(num):
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
            return 'Out of range.'


def __num2wordsPor(num):
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
            return 'fora de alcance'
