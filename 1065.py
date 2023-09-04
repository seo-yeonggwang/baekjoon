def is_hansu(x):
    digits = [int(digit) for digit in str(x)]

    if len(digits) <= 2:
        return True
    
    dif = digits[1] - digits[0]
    
    for i in range(1, len(digits) - 1):
        if digits[i + 1] - digits[i] != dif:
            return False
    
    return True

N = int(input())
count = 0

for i in range(1, N + 1):
    if is_hansu(i):
        count += 1

print(count)
