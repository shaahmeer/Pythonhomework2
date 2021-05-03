dict = {
    'а': 'a',
    'б': 'b',
    'в': 'v',
    'г': 'g',
    'д': 'd',
    'е': 'e',
    'ё': 'e',
    'ж': 'z',
    'з': 'z',
    'и': 'i',
    'й': 'i',
    'к': 'k',
    'л': 'l',
    'м': 'm',
    'н': 'n',
    'о': 'o',
    'п': 'p',
    'р': 'r',
    'с': 's',
    'т': 't',
    'у': 'y',
    'ф': 'f',
    'х': 'h',
    'ц': 'ts',
    'ч': 'ch',
    'ш': 'sh',
    'щ': 'sh',
    'ь': '',
    'ы': 'i',
    'ъ': '',
    'э': 'e',
    'ю': 'y',
    'я': 'a',
}

for d in dict.copy():
    dict[d.upper()] = dict[d].capitalize()

str = list(input())
for i, s in enumerate(str):
    if s in dict:
        str[i] = dict[s]
print(''.join(str))
