__author__ = 'trinhkhanh'
while True:
    number = int(input("Input an odd number: "))
    if number%2 != 0 and number >= 7:

        for i in reversed(range(1, number+1)):
                if i%2 != 0:
                    list = ''.join(map(str, [i]*i))

                    print(list.center(number*len(str(number))))
    else:
        print("Sorry, the number you enter is even number")
