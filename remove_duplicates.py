#Remove Duplicates from Sorted Array


def remove_duplicates(arr:int):
    Set=set()
    for i in range(len(arr)):
        Set.add(arr[i])

    return Set

arr=[1,2,2,3,4,4,5,6,6,7,8,9,10,10]
obj =remove_duplicates(arr)
print(obj)