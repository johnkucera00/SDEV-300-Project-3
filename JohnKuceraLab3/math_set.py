"""
__filename__ = "math_set.py"
__coursename__ = "SDEV 300 6380 - Building Secure Web Applications (2198)"
__author__ = "John Kucera"
__copyright__ = "None"
__credits__ = ["John Kucera"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "John Kucera"
__email__ = "johnkucera00@gmail.com"
__status__ = "Test"
"""

def main():
    """
    Math Set main
    """
    # List Creation
    numbers = list(range(1, 101))
    sqrd_numbers_list = [i ** 2 for i in numbers]
    cbd_numbers_list = [i ** 3 for i in numbers]

    # Set Creation
    og_numbers = set(numbers)
    sqrd_numbers = set(sqrd_numbers_list)
    cbd_numbers = set(cbd_numbers_list)

    # Menu
    print('*****Welcome to the Math Set Application!*****')
    is_valid = False
    while not is_valid:
        try:
            selection = int(input('\nSelect from the following menu:\n'
                                  '\t1. Display the Square and Cube for Integers'
                                  ' ranging from 1 to 100\n'
                                  '\t2. Search the sets for a specific Integer'
                                  ' and display the Square and Cube values\n'
                                  '\t3. Display the Union of Square and Cube sets\n'
                                  '\t4. Display the Intersection of Square and '
                                  'Cube sets\n'
                                  '\t5. Display the Difference of Square and '
                                  'Cube sets\n'
                                  '\t6. Exit the program\n'))
        except ValueError:
            print('You must enter 1, 2, 3, 4, 5, or 6. Please try again.')
        else:
            if selection >= 1 and selection <= 6:
                is_valid = True
                break
            else:
                print('You must enter 1, 2, 3, 4, 5, or 6. Please try again.')

    # Sentinel While loop
    while selection != 6:

        # Option 1
        if selection == 1:
            print('You selected 1. Here are the Square and Cube for Integers '
                  'ranging from 1 to 100:\n')
            for i in range(len(numbers)):
                print(numbers[i], '=>')
                print('Square =', numbers[i], '^ 2 =', sqrd_numbers_list[i])
                print('Cube =', numbers[i], '^ 3 =', cbd_numbers_list[i], '\n')
            is_valid = False
            while not is_valid:
                try:
                    selection = int(input('\nSelect from the following menu:\n'
                                          '\t1. Display the Square and Cube for Integers'
                                          ' ranging from 1 to 100\n'
                                          '\t2. Search the sets for a specific Integer'
                                          ' and display the Square and Cube values\n'
                                          '\t3. Display the Union of Square and Cube sets\n'
                                          '\t4. Display the Intersection of Square and '
                                          'Cube sets\n'
                                          '\t5. Display the Difference of Square and '
                                          'Cube sets\n'
                                          '\t6. Exit the program\n'))
                except ValueError:
                    print('You must enter 1, 2, 3, 4, 5, or 6. Please try again.')
                else:
                    if selection >= 1 and selection <= 6:
                        is_valid = True
                        break
                    else:
                        print('You must enter 1, 2, 3, 4, 5, or 6. Please try again.')

        # Option 2
        elif selection == 2:
            valid_int = False
            while not valid_int:
                try:
                    selected_integer = int(input('You selected 2. Which integer '
                                                 'would you like to see the Square '
                                                 'and Cube of?\n'))
                    if selected_integer in og_numbers:
                        print('\n', selected_integer, '=>')
                        print('Square =', selected_integer, '^ 2 =', selected_integer ** 2)
                        print('Cube =', selected_integer, '^ 3 =', selected_integer ** 3, '\n')
                        valid_int = True
                        break
                    else:
                        print('You must enter an Integer between 1 and 100. '
                              'Please try again.')
                except ValueError:
                    print('You must enter an Integer between 1 and 100. '
                          'Please try again.')
            is_valid = False
            while not is_valid:
                try:
                    selection = int(input('\nSelect from the following menu:\n'
                                          '\t1. Display the Square and Cube '
                                          'for Integers ranging from 1 to 100\n'
                                          '\t2. Search the sets for a specific Integer'
                                          ' and display the Square and Cube values\n'
                                          '\t3. Display the Union of Square '
                                          'and Cube sets\n'
                                          '\t4. Display the Intersection of Square and '
                                          'Cube sets\n'
                                          '\t5. Display the Difference of Square and '
                                          'Cube sets\n'
                                          '\t6. Exit the program\n'))
                except ValueError:
                    print('You must enter 1, 2, 3, 4, 5, or 6. Please try again.')
                else:
                    if selection >= 1 and selection <= 6:
                        is_valid = True
                        break
                    else:
                        print('You must enter 1, 2, 3, 4, 5, or 6. Please try again.')

        # Option 3
        elif selection == 3:
            big_union_set = sqrd_numbers | cbd_numbers
            big_union_list = list(big_union_set)
            big_union_list.sort()
            print('You selected 3. Here is the Union of Square and Cube sets:')
            print(big_union_list)
            is_valid = False
            while not is_valid:
                try:
                    selection = int(input('\nSelect from the following menu:\n'
                                          '\t1. Display the Square and Cube for Integers'
                                          ' ranging from 1 to 100\n'
                                          '\t2. Search the sets for a specific Integer'
                                          ' and display the Square and Cube values\n'
                                          '\t3. Display the Union of Square and Cube sets\n'
                                          '\t4. Display the Intersection of Square and '
                                          'Cube sets\n'
                                          '\t5. Display the Difference of Square and '
                                          'Cube sets\n'
                                          '\t6. Exit the program\n'))
                except ValueError:
                    print('You must enter 1, 2, 3, 4, 5, or 6. Please try again.')
                else:
                    if selection >= 1 and selection <= 6:
                        is_valid = True
                        break
                    else:
                        print('You must enter 1, 2, 3, 4, 5, or 6. Please try again.')

        # Option 4
        elif selection == 4:
            big_inter_set = sqrd_numbers & cbd_numbers
            big_inter_list = list(big_inter_set)
            big_inter_list.sort()
            print('You selected 4. Here is the Intersection of Square and Cube sets:')
            print(big_inter_list)
            is_valid = False
            while not is_valid:
                try:
                    selection = int(input('\nSelect from the following menu:\n'
                                          '\t1. Display the Square and Cube for Integers'
                                          ' ranging from 1 to 100\n'
                                          '\t2. Search the sets for a specific Integer'
                                          ' and display the Square and Cube values\n'
                                          '\t3. Display the Union of Square and Cube sets\n'
                                          '\t4. Display the Intersection of Square and '
                                          'Cube sets\n'
                                          '\t5. Display the Difference of Square and '
                                          'Cube sets\n'
                                          '\t6. Exit the program\n'))
                except ValueError:
                    print('You must enter 1, 2, 3, 4, 5, or 6. Please try again.')
                else:
                    if selection >= 1 and selection <= 6:
                        is_valid = True
                        break
                    else:
                        print('You must enter 1, 2, 3, 4, 5, or 6. Please try again.')

        # Option 5
        elif selection == 5:
            big_diff_set = sqrd_numbers - cbd_numbers
            big_diff_list = list(big_diff_set)
            big_diff_list.sort()
            print('You selected 5. Here is the Difference of Square and Cube sets:')
            print(big_diff_list)
            is_valid = False
            while not is_valid:
                try:
                    selection = int(input('\nSelect from the following menu:\n'
                                          '\t1. Display the Square and Cube for Integers'
                                          ' ranging from 1 to 100\n'
                                          '\t2. Search the sets for a specific Integer'
                                          ' and display the Square and Cube values\n'
                                          '\t3. Display the Union of Square and Cube sets\n'
                                          '\t4. Display the Intersection of Square and '
                                          'Cube sets\n'
                                          '\t5. Display the Difference of Square and '
                                          'Cube sets\n'
                                          '\t6. Exit the program\n'))
                except ValueError:
                    print('You must enter 1, 2, 3, 4, 5, or 6. Please try again.')
                else:
                    if selection >= 1 and selection <= 6:
                        is_valid = True
                        break
                    else:
                        print('You must enter 1, 2, 3, 4, 5, or 6. Please try again.')

    # Option 6
    print('You selected 6.')
    print('Thank you for trying the Math Set Application.')
    print('**************************************************')
    return

if __name__ == "__main__":
    main()
