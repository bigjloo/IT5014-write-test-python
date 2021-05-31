# BingoGame.py
# BingoGame in Python
# @author: Junzhong Loo  
# 18/5/2021 

def main():
    # Bingo card numbers 
    BINGO_CARD = (
        7, 14, 26, 22, 40, 
        34, 58, 55, 73, 68,
        )

    # Get the total number of bingo numbers
    numbers_left = len(BINGO_CARD)

    # Empty list to store called numbers by user
    called_numbers = []

    # Welcome message and instruction
    print("*** Welcome to BINGO game ***")
    print("There are {} numbers between 1-80 in the BINGO card.".format(numbers_left))
    print("Every time a number called matches the a number in the BINGO card, the number is crossed off.")
    print("When all numbers have been crossed off the BINGO card, you win.")

    # Loop while not bingo
    while numbers_left > 0:
        # Get user input a number between 1 - 80
        try:
            number_from_user = int(input("Enter a number from 1 - 80: "))

        except ValueError as err:
            print(err)
            continue

        except TypeError as err:
            print(err)
            continue

        # Number not in 1-80
        if not 1 <= number_from_user <= 80:
            print("Numbers 1-80 only")
            continue

        # Number that has already been called
        if number_from_user in called_numbers:
            print("Number already called.")
            continue

        # If number called is one of the number in the bingo card, 
        # reduce numbers_left by 1
        if number_from_user in BINGO_CARD: 
            numbers_left -= 1
        
        # Add number called into called_numbers list
        called_numbers.append(number_from_user)

        print("Called numbers:", called_numbers)
        print("Numbers left till BINGO:", numbers_left)


    # Number of bingo numbers left == 0
    print("BINGO!!")


if __name__ == "__main__":
    main()