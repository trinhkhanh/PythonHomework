__author__ = 'trinhkhanh'
while True:
<<<<<<< HEAD
    number = int(input("Input an odd number: "))
    if number%2 != 0 and number >= 7:
=======
    number = int(input("Enter a integer: "))
    if number%2 != 0:
>>>>>>> origin/master

        for i in reversed(range(1, number+1)):
                if i%2 != 0:

<<<<<<< HEAD
                    print(format([i]*i), end=" ")
=======
                    print(format([i]*i, ''), end=" ")
>>>>>>> origin/master
                print()
    else:
        print("Sorry, the number you enter is even number")