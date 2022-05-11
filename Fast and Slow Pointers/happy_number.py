def is_happy(num):
    slow, fast = num, num

    while True:
        slow = find_square_sum(slow)
        fast = find_square_sum(find_square_sum(fast))

        if slow == fast:
            break

    return slow == 1

def find_square_sum(num):
    running_sum = 0
    while num > 0:
        last_digit = num % 10
        running_sum += last_digit * last_digit
        num = num // 10
    return running_sum + num

print(is_happy(23))
print(is_happy(12))