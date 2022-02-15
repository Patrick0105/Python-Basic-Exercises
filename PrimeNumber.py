def is_prime(number):
    flag = True
    for i in range(2,number):
        if number % i == 0:
            flag = False
    if flag:
        print('是質數')
    else:
        print('不是質數')

is_prime(100)