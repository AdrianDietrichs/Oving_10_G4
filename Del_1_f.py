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
