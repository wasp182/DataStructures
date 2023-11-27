def get_int(n):
    rev = 0
    while n > 0 :
        rev = rev * 10 + (n % 10)
        n = n//10
    print(rev)
    return rev

get_int(198)

get_int(100)