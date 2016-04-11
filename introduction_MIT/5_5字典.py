#encoding:utf8
#5.5字典

# monthNumbers={'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,
#               1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May'}
#
# print 'The third month is '+monthNumbers[3]
# dist=monthNumbers['Apr']-monthNumbers['Jan']
# print 'Apr and Jan are',dist,'months apart'
# print monthNumbers.keys()
#
# keys=[]
# for e in monthNumbers:
#     keys.append(e)
# keys.sort()
# print keys


#文本翻译
EtoF={'bread':'pain','wine':'vin','with':'avec','I':'Je','eat':'mange',
      'drink':'bois','John':'Jean','friends':'amis','and':'et','of':'du','red':'rouge'}
FtoE={v:k for k,v in EtoF.items()}
dicts={'English to French':EtoF,'French to English':FtoE}

def translateWord(word,dictionary):
    if word in dictionary.keys():
        return dictionary[word]
    elif word!='':
        return '"' + word + '"'
    return word

def translate(phrase,dicts,direction):
    UCLetters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LCLetters='abcdefghijklmnopqrstuvwxyz'
    letters=UCLetters+LCLetters
    dictionary=dicts[direction]
    translation=''
    word=''
    for c in phrase:
        if c in letters:
            word=word+c
        else:
            translation=translation+translateWord(word,dictionary)+c
            word=''
    return translation + ' '+translateWord(word,dictionary)

print translate('I drink good red wine,and eat break.',dicts,'English to French')
print translate('Je bois du vin rouge.',dicts,'French to English')


def keySearch(l,k):
    for elem in l:
        if elem[0]==k:
            return elem[1]
    return None
