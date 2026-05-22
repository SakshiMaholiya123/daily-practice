#Check whether a given string is a palindrome or not.

def palindrome(str):
    left=0
    right=len(str)-1

    while(left<right):
        if str[left]!=str[right]:
            return False
        left+=1
        right-=1
    
    return True

str='palindrom'
obj=palindrome(str)
print(obj)

    