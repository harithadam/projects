from random import randint

def main():
    n = randint(2,100)
    print(f"Selected number is {n}")
    counter = 0

    while n != 1:
        if n % 2 == 0:
            n = n / 2
        
        else:
            n = 3 * n + 1

        counter += 1

    print(f"Number of steps to reach 1 is {counter}")


if __name__ == "__main__":
    main()