def printWords(words):
    s = words.upper()
    vocal = ['A', 'E', 'I', 'U', 'O']
    voc = ''
    kons = ''

    for i in range(len(s)):
        if s[i] in vocal:
            voc = voc + s[i]+'\n'
        else: 
            kons = kons + s[i]+'\n'
    print(voc+kons)

printWords('ARKADEMY')