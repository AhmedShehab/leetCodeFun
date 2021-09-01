def plusOne(digits):
        # Iterate the array from the least significant digit
        # if the number is less than 9 then increment and return

        # Declare a flag to indicate if the array should be extended 
        flag = 0
        for i in range(len(digits)-1,-1,-1):
            if digits[i] < 9:
                digits[i] += 1 
                return digits
            
            elif digits[i] == 9 and flag != len(digits) - 1:
                digits[i] = 0 

            else:
                digits[i] = 0
                digits.insert(0,1)
                return digits

            flag += 1

print(plusOne([9]))