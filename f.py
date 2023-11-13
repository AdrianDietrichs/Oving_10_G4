def longestZeroSequence(array: list):
    longest = 0
    current = 0

    for n in array:
        if n == 0:
            current += 1
        else: 
            current = 0
        
        if current > longest:
            longest = current

    return longest


arr1 = [1,2,3,4,5,6,7,8,9,0]#1
arr2 = [1,5,0,0,2,4,0,1,2,0,0,0,2]#3
arr3 = [1,2,3,4,5]

print(longestZeroSequence(arr1))
print(longestZeroSequence(arr2))
print(longestZeroSequence(arr3))
