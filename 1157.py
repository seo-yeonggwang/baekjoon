def MaxAlphabet(word):
    Alphabet_count = [0] * 26 # 알파벳 개수
    
    for i in word:
        num = ord(i) - ord('A') # ord를 통해 유니코드 사용
        Alphabet_count[num] += 1
    
    max_count = max(Alphabet_count)
    max_index = Alphabet_count.index(max_count)
    
    if Alphabet_count.count(max_count) > 1:
        print("?")
    else:
        most_common_letter = chr(max_index + ord('A'))
        print(most_common_letter)
        
    return 0

word = input().upper()
MaxAlphabet(word)