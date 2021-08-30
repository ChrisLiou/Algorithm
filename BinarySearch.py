import math

def binarySearch(arr,target):
    l=0
    r=len(arr)-1

    while l<=r:
        mid=math.floor((l+r)/2)
        if target>arr[mid]:
            l=mid+1
        elif target<arr[mid]:
            r=mid-1
        else:
            return mid

print(binarySearch([1,2,3,4,5,6,7],7))