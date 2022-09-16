# Complete the solution so that the function will break up camel casing, using a space between words.
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""
import re

reg_ex = re.compile('([A-Z])')
def solution(s):
    
    if s.islower():
        return s
    else:
        split_s = ''
        for x in reg_ex.split(s):
            if x.isupper():
                split_s = split_s + ' ' + x
            else:
                split_s = split_s + x
        return split_s

solution('camelCaseSub')
