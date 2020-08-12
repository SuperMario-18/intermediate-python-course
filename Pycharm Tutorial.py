    r = random.randint(1, upper)
    resturn r

def main():
    run = TRUE
    num1 = generateRandom(10)
    num2 = generateRandom(10)
    result = num1 * num2
    while run:
        ans = input("What is " + str(num1) + " x " + str(num2) + "? ")

        if and.isdigit():
            if int(ans) == result:
                print("Correct")
                run = False
            else:
                print("Answer must be a positive number, try again.")


# global vars
times = 10

for x in range(times):
    main()