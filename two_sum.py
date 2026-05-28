#Find two numbers whose sum equals target.

def two_sum(arr:int,target:int):
    arr.sort()
    left=0
    right=len(arr)-1
   
    while(left<right):
        if arr[left]+arr[right]==target:
           return [arr[left], arr[right]] 
        elif arr[left]+arr[right]>target:
            right-=1
        else:
            left+=1


    return []

arr=[45,3,6,5,12]
target=18

obj=two_sum(arr,target)
print(obj)
    

