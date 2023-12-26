def palindrome_checker(num):
    rev = 0
    org_num = num
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
    if rev == org_num:
        return True
    else:
        return False


print(palindrome_checker(121))
