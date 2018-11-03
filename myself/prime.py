def prime(num):
    for n in range(2,num):
        if num%n == 0:
            # print('\n')
            print('\n{} is divided by {}'.format(num, n))
            return False 
    return True 

print(prime(11))
print(prime(49))
print(prime(5738947298735891))