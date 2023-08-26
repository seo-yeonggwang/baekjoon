def AlphabetCheak(word):
    arr = [-1] * 26
    
    for i in range(len(word)):
        index = ord(word[i]) - ord('a')
        
        if arr[index] == -1:
            arr[index] = i
        else:
            continue
    
    for j in range(len(arr)):
        print(arr[j], end = " ")
    
    return 0

word = input()
AlphabetCheak(word)
            