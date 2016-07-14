import binascii
import re

def EnglishFullToHalf(StrIn):
    
    def transform(ele):
        alphabetInt = int(repr(ele.group('number'))[4:8],16)
        transAlphabeInt = alphabetInt - 65248
        return binascii.a2b_hex(hex(transAlphabeInt)[2:4])
    pattern = re.sub(u'(?P<number>[\uff21-\uff3a\uff41-\uff5a])', transform, StrIn)
    
    return pattern

str1=u'ABC123ＡＢＣ１２３'
EnglishFullToHalf(str1)