
# def linear_search(list,value):
# The algorithm is iterative as it searchs for value by value in the list
#     for i in range(len(list)-1):
#         if(list[i]==value):
#             return i
#     return None
# def Binary_search(list,value):
# #this algorithm searchs for the value by decreasing the search range
# #using iterative method
#     first=0
#     last=len(list)-1
#     while first<=last:
#         midpoint=(first+last)//2
#         if list[midpoint]==value:
#             return midpoint
#         elif list[midpoint]<value:
#             first=midpoint+1
#         else:
#             last=midpoint-1
#     return None
# #using recursive method
# def recursive_binary_search(list,value):
#     if (len(list)==0):
#         return True
#     else:
#         midpoint=len(list)//2
#         if (list[midpoint]<value):
#             return recursive_binary_search(list[midpoint+1:],value)
#         else:
#             return recursive_binary_search(list[:midpoint],value)

    
# print(linear_search([5,2,9,10,7,6],10))
# print(Binary_search([2,5,6,7,9,10],10))
# print(recursive_binary_search([5,2,9,10,7,6],10))

#uncomplete
'''merge_sort'''
def split(list):
    '''
    Divide: the unsorted list into sublists
    returns two sublists which are left and right
    '''
    mid=len(list)//2
    left=list[:mid]
    right=list[mid:]
    return left,right
def Merge(left,right):
    '''
    Merges two lists(arrays),sorting them in the process
    Returns a new merged list
    '''
    lst=[] #define an empty list
    i,j=0
    while(i<len(left) and j<len(right)):
        if left[i]<right[j]:
            lst.append(left[i])
            i+=1
        else:
            lst.append[right[i]]
            j+=1
    while(i<len(left)):
        lst.append(left[i])
        i+=1
    while(j<len(right)):
        lst.append(right[j])
        j+=1
    return lst
def merge_sort(list):
    '''
    Sorts a list in ascending order then returns a new sorted list

    Divide:Find the midpoint of the list and divide into sublists
    Conquer:Recursivly sort the sublists created in previous step
    Conquer:Merge the sorted sublists created in previous step
    '''
    if (len(list)<=1):
        return list
    left_half=split(list)
    right_half=split(list)
    left=merge_sort(left_half)
    right=merge_sort(right_half)
    return Merge(left,right)

alist=[54,62,93,17,77,31,44,55,20]
l=merge_sort(alist)
print(l)