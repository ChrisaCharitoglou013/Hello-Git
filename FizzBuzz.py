def FizzBuzz(n):
    for i in range (1, n+1):
        if (int(i/3)==(i/3)) and (int(i/5)==(i/5)) :
            print ('FizzBuzz')
        elif int(i/3)==(i/3):
            print ('Fizz')
        elif int(i/5)==(i/5):
            print ('Buzz')
        else:
            print (i)



FizzBuzz(50)
