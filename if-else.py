# Check given number is even or odd

number = input('Enter the number to guess')

try:
    x = int(number)
    if x % 2 == 0:
        print("{}, is even".format(x))
    else:
        print("{}, is odd".format(x))
except:
    print('Please pass only numbers')
