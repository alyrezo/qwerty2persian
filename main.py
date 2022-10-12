qwerty = {'q':'ض','w':'ص','e':'ث','r':'ق','t':'ف','y':'غ','u':'ع','i':'ه','o':'خ','p':'ح','[':'ج',']':'چ','a':'ش','s':'س','d':'ی','f':'ب','g':'ل','h':'ا','j':'ت','k':'ن','l':'م',';':'ک','\'':'گ','z':'ظ','x':'ط','c':'ز','v':'ر','b':'ذ','n':'د','m':'ئ',',':'و','.':'.','\\':'پ',' ':' ','\n':'\n ',}
upper = {'G':'ۀ','H':'آ','Z':'ة','X':'ي','C':'ژ','V':'ؤ','B':'إ','N':'أ','M':'ء',}
while True:
    for word in input('enter: '):
        if word.islower() or word in qwerty.keys():
            print(qwerty[word],end='')
        elif word.isupper() and word in upper.keys():
            print(upper[word],end='')
        else:
            print(word,end='')
    print('\n')
