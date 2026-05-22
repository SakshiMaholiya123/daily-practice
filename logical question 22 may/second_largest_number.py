#Given a list of numbers, find the second largest number without sorting the list.
def second_largest(list):
    largest=list[0]
    second_largest=list[0]
    for num in list:
        if num> largest:
            second_largest=largest
            largest=num

        else:
            if largest>num and num>second_largest:
                second_largest=num
        
    return second_largest


list=[1,2,3,4,54,78]
obj=second_largest(list)
print(obj)
        