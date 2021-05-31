# BoxCalculator.py
# Returns number of boxes needed for number of items provided by user
# @author: Junzhong Loo
# 18/5/2021

def main():
    # Fixed variables for max items per box
    BIG_BOX_MAX_ITEMS = 5
    MID_BOX_MAX_ITEMS = 3
    SMALL_BOX_MAX_ITEMS = 1
    
    def boxes_required_for(number_of_items):
        """
        Calculate big boxes first, then use remainder to calculated mid boxes
        then small boxes.

        Returns total number of boxes
        """
        big_boxes = number_of_items // BIG_BOX_MAX_ITEMS
        number_of_items %= BIG_BOX_MAX_ITEMS
        mid_boxes = number_of_items // MID_BOX_MAX_ITEMS
        number_of_items %= MID_BOX_MAX_ITEMS
        small_boxes = number_of_items // SMALL_BOX_MAX_ITEMS

        total_number_of_boxes = big_boxes + mid_boxes + small_boxes
        return total_number_of_boxes

    # START
    print("Hi, welcome to The Box Company!")

    # Loop validates and gets user input as long as user input is not the correct format
    is_validated = False
    while not is_validated:
        try:
            number_of_items = int(input("Please type in the number of items you wish to store: "))
            
            # negative number
            if number_of_items < 0:
                print("Positive numbers only")
                continue

            # break loop
            is_validated = True

        # non integer input
        except TypeError as err:       
            print(err)
            continue

        # decimal user input
        except ValueError as err:
            print(err)
            continue
    
    total_number_of_boxes = boxes_required_for(number_of_items)

    print("Total number of boxes needed:", total_number_of_boxes)
    print("Thank you for using The Box Company")


if __name__ == "__main__":
    main()
