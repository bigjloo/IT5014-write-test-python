# GradeCalculator.py
# Returns a grade base on scores provided by user
# @author: Junzhong Loo
# 18/5/2021

def main():
    # Elements to count towards final score. (element, weight)
    CONTRIBUTING_SCORE_TO_FINAL = [
        ("Project", 0.5),
        ("Exam", 0.5),
        ]

    def get_grade(total_final_score):
        """ Returns grade base on score table """
        if total_final_score >= 80:
            final_grade = "A"
        elif total_final_score < 50:
            final_grade = "Fail"
        elif total_final_score >= 70:
            final_grade = "B"
        elif total_final_score >= 60:
            final_grade = "C"
        else:
            final_grade = "D"
        return final_grade

    # START
    print("Enter scores in whole positive integers from 0-100.\n \
            Example:\n \
            80% -> 80\n \
            45% -> 45"
            )
        
    total_final_score = 0.0

    # Get score from user for every contributing score element
    for (element, weight) in CONTRIBUTING_SCORE_TO_FINAL:
        
        is_validated = False

        # Get input from user and validate
        while not is_validated:
            try:
                # Get score from user
                request_input_message = "{} score: ".format(element)
                score_from_user = int(input(request_input_message))

                # Score not between 0-100
                if not 0 <= score_from_user <= 100:
                    print("0-100 only!")
                    continue
                
                is_validated = True

            except ValueError as err:
                print(err)
                continue

            except TypeError as err:
                print(err)
                continue
        
        # calculate total final score
        total_final_score += score_from_user * weight 

    # Return grade base on final score
    final_grade = get_grade(total_final_score)

    # Final score and grade
    print("Final score: {}%".format(total_final_score))
    print("Final grade:", final_grade)


if __name__ == "__main__":
    main()
