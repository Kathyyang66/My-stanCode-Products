"""
File: class_reviews.py
Name: Kathy Yang
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""
EXIT = '-1'

def main():
    """
    TODO: Calculating maximum, minimum, and average scores among different classes.
    """
    max_1 = 0
    min_1 = 100
    num_1 = 0
    total_1 = 0

    max_2 = 0
    min_2 = 100
    total_2 = 0
    num_2 = 0
    c = input('Which class? ').lower()
    if c == EXIT:
        print('No class scores were entered')
    else:
        score = int(input('Score: '))
        if c == 'sc001':
            max_1 = score
            min_1 = score
            num_1 = 1
            total_1 = score
        elif c == 'sc101':
            max_2 = score
            min_2 = score
            total_2 = score
            num_2 = 1
        while True:
            c = input('Which class? ').lower()
            if c == EXIT:
                break
            else:
                score = int(input('Score: '))
                if c == 'sc001':
                    if score > max_1:
                        max_1 = score
                    if score < min_1:
                        min_1 = score
                    num_1 += 1
                    total_1 += score
                elif c == 'sc101':
                    if score > max_2:
                        max_2 = score
                    if score < min_2:
                        min_2 = score
                    num_2 += 1
                    total_2 += score
        print('============='+'SC001'+'=============')
        if num_1 == 0:
            print('No score for SC001')
        else:
            print('Max (001): '+str(max_1))
            print('Min (001): '+str(min_1))
            print('Avg (001): '+str(total_1/num_1))
        print('=============' + 'SC101' + '=============')
        if num_2 == 0:
            print('No score for SC101')
        else:
            print('Max (101): ' + str(max_2))
            print('Min (101): ' + str(min_2))
            print('Avg (101): ' + str(total_2 / num_2))


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
