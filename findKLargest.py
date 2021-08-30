# def findKthLargest(nums,k):
#         quickSort(nums,0,len(nums)-1)

#         return nums[-k]

# def quickSort(arr, left, right):
#     if left<right:
#         i=partition(arr,left,right)
#         quickSort(arr,left,i-1)
#         quickSort(arr,i+1,right)
    
# def partition(arr, left, right):
#     p=right
#     i=left
#     j=left

#     while(j<len(arr)):
#         if arr[j]<arr[p]:
#             temp=arr[i]
#             arr[i]=arr[j]
#             arr[j]=temp
#             i+=1
#         j+=1
#     temp=arr[i]
#     arr[i]=arr[p]
#     arr[p]=temp
    
#     return i

def findKthLargest(nums,k):
        quickSort(nums,0,len(nums)-1)

        return nums[-k]
        
def quickSort(arr, left, right):
    if left<right:
        p=right
        i=left
        j=left

        for j in range(left,len(arr)):
            if arr[j]<arr[p]:
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
                i+=1
        temp=arr[i]
        arr[i]=arr[p]
        arr[p]=temp
        
        quickSort(arr,left,i-1)
        quickSort(arr,i+1,right)
        

    

print(findKthLargest([3,2,1,5,6,4],2))