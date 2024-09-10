""" 
def precedes(one_string, another_string):
    lower1 = one_string.lower()
    lower2 = another_string.lower()
    for letteridx in range(min(len(lower1), len(lower2))):
        if letteridx + 1 == len(lower1):
            return one_string
        elif letteridx + 1 == len(lower2):
            return another_string
        
        if lower1[letteridx] == lower2[letteridx]:
            continue
        elif lower1[letteridx] < lower2[letteridx]:
            return one_string
        else:
            return another_string
            
 """

def precedes(one_string, another_string):
    if one_string.lower() < another_string.lower():
        return one_string
    else:
        return another_string