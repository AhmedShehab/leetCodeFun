def lengthOfLastWord(s: str) -> int:
    # Pop the space element in the string if the flag is not raised
    # Else if the string ends or a space is found Return Count
    
    # Declaring flag [indicates that the last word ended] and counter variables 
    flag = 0
    count = 0
    
    for i in range(0,len(s)):
        last_element = s[-1 * (i+1)]
        if last_element == "" and flag == 0:
            continue 
            
        elif last_element == "" and flag == 1:
            break 
            
        elif last_element != "":
            flag = 1
            count +=1   
            
    return count


print(lengthOfLastWord("Hello World"))