def romanToInt(s: str) -> int:
    # Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
    # These are there valuse
    romanNumerals = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000} 
    number = 0 
    track = 0
    for i in range(len(s)-1,-1,-1):
        digit = romanNumerals[s[i]]
        if track != 0:
            if digit < romanNumerals[s[i+1]]:
                number -= digit
            else:
                number += digit
        else:
            number +=digit
        track += 1
    return number