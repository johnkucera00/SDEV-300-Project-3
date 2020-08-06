"""
__filename__ = "us_states_info.py"
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
    US States Info main
    """
    # Dictionary Creation
    state_capitals = {'Alabama': 'Montgomery',
                      'Alaska': 'Juneau',
                      'Arizona': 'Phoenix',
                      'Arkansas': 'Little Rock',
                      'California': 'Sacramento',
                      'Colorado': 'Denver',
                      'Connecticut': 'Hartford',
                      'Delaware': 'Dover',
                      'Florida': 'Tallahassee',
                      'Georgia': 'Atlanta',
                      'Hawaii': 'Honolulu',
                      'Idaho': 'Boise',
                      'Illinois': 'Springfield',
                      'Indiana': 'Indianapolis',
                      'Iowa': 'Des Moines',
                      'Kansas': 'Topeka',
                      'Kentucky': 'Frankfort',
                      'Louisiana': 'Baton Rouge',
                      'Maine': 'Augusta',
                      'Maryland': 'Annapolis',
                      'Massachusetts': 'Boston',
                      'Michigan': 'Lansing',
                      'Minnesota': 'St. Paul',
                      'Mississippi': 'Jackson',
                      'Missouri': 'Jefferson City',
                      'Montana': 'Helena',
                      'Nebraska': 'Lincoln',
                      'Nevada': 'Carson City',
                      'New Hampshire': 'Concord',
                      'New Jersey': 'Trenton',
                      'New Mexico': 'Santa Fe',
                      'New York': 'Albany',
                      'North Carolina': 'Raleigh',
                      'North Dakota': 'Bismarck',
                      'Ohio': 'Columbus',
                      'Oklahoma': 'Oklahoma City',
                      'Oregon': 'Salem',
                      'Pennsylvania': 'Harrisburg',
                      'Rhode Island': 'Providence',
                      'South Carolina': 'Columbia',
                      'South Dakoda': 'Pierre',
                      'Tennessee': 'Nashville',
                      'Texas': 'Austin',
                      'Utah': 'Salt Lake City',
                      'Vermont': 'Montpelier',
                      'Virginia': 'Richmond',
                      'Washington': 'Olympia',
                      'West Virginia': 'Charleston',
                      'Wisconsin': 'Madison',
                      'Wyoming': 'Cheyenne'
                     }

    state_birds = {'Alabama': 'Yellowhammer',
                   'Alaska': 'Willow Ptarmigan',
                   'Arizona': 'Cactus Wren',
                   'Arkansas': 'Mockingbird',
                   'California': 'California Valley Quail',
                   'Colorado': 'Lark Bunting',
                   'Connecticut': 'Robin',
                   'Delaware': 'Blue Hen',
                   'Florida': 'Mockingbird',
                   'Georgia': 'Brown Thrasher',
                   'Hawaii': 'Nene',
                   'Idaho': 'Mountain Bluebird',
                   'Illinois': 'Cardinal',
                   'Indiana': 'Cardinal',
                   'Iowa': 'Eastern Goldfinch',
                   'Kansas': 'Western Meadowlark',
                   'Kentucky': 'Cardinal',
                   'Louisiana': 'Eastern Brown Pelican',
                   'Maine': 'Chickadee',
                   'Maryland': 'Baltimore Oriole',
                   'Massachusetts': 'Chickadee',
                   'Michigan': 'Robin',
                   'Minnesota': 'Common Loon',
                   'Mississippi': 'Mockingbird',
                   'Missouri': 'Bluebird',
                   'Montana': 'Western Meadowlark',
                   'Nebraska': 'Western Meadowlark',
                   'Nevada': 'Mountain Bluebird',
                   'New Hampshire': 'Purple Finch',
                   'New Jersey': 'Eastern Goldfinch',
                   'New Mexico': 'Roadrunner',
                   'New York': 'Bluebird',
                   'North Carolina': 'Cardinal',
                   'North Dakota': 'Western Meadowlark',
                   'Ohio': 'Cardinal',
                   'Oklahoma': 'Scissor-Tailed Flycatcher',
                   'Oregon': 'Western Meadowlark',
                   'Pennsylvania': 'Ruffed Grouse',
                   'Rhode Island': 'Rhode Island Red',
                   'South Carolina': 'Great Carolina Wren',
                   'South Dakoda': 'Ring-Necked Pheasant',
                   'Tennessee': 'Mockingbird',
                   'Texas': 'Mockingbird',
                   'Utah': 'California Seagull',
                   'Vermont': 'Hermit Thrush',
                   'Virginia': 'Cardinal',
                   'Washington': 'Willow Goldfinch',
                   'West Virginia': 'Cardinal',
                   'Wisconsin': 'Robin',
                   'Wyoming': 'Western Meadowlark'
                  }
    # List Creation
    states = list(state_capitals.keys())
    capitals = list(state_capitals.values())
    birds = list(state_birds.values())

    # Menu
    print('*****Welcome to the US State Capital and Bird Database!*****')

    is_valid = False
    while not is_valid:
        try:
            selection = int(input('\nSelect from the following menu:\n'
                                  '\t1. Display all U.S. States in alphabetical'
                                  ' order along with Capital and Bird\n'
                                  '\t2. Search for a specific State and display'
                                  ' the appropriate Capital and Bird\n'
                                  '\t3. Update a Bird for a specific State\n'
                                  '\t4. Exit the program\n'))
        except ValueError:
            print('You must enter 1, 2, 3, or 4. Please try again.')
        else:
            if selection >= 1 and selection <= 4:
                is_valid = True
                break
            else:
                print('You must enter 1, 2, 3, or 4. Please try again.')

    # Sentinel While loop
    while selection != 4:

        # Option 1
        if selection == 1:
            print('You selected 1. Here is a list of all U.S. States in'
                  ' alphabetical order along with Capital and Bird:\n')
            for i in range(len(states)):
                print(states[i], end=', ')
                print(capitals[i], end=', ')
                print(birds[i], end='\n')

            # Menu
            is_valid = False
            while not is_valid:
                try:
                    selection = int(input('\nSelect from the following menu:\n'
                                          '\t1. Display all U.S. States in'
                                          ' alphabetical order along with'
                                          ' Capital and Bird\n'
                                          '\t2. Search for a specific State and'
                                          ' display the appropriate Capital'
                                          ' and Bird\n'
                                          '\t3. Update a Bird for a specific'
                                          ' State\n'
                                          '\t4. Exit the program\n'))
                except ValueError:
                    print('You must enter 1, 2, 3, or 4. Please try again.')
                else:
                    if selection >= 1 and selection <= 4:
                        is_valid = True
                        break
                    else:
                        print('You must enter 1, 2, 3, or 4. Please try again.')

        # Option 2
        elif selection == 2:
            selected_state = str(input('You selected 2. Please enter a State:\n'))
            if selected_state.title() in states:
                print(states[states.index(selected_state.title())], end=': ')
                print(capitals[states.index(selected_state.title())], end=', ')
                print(birds[states.index(selected_state.title())], end='\n')

                # Menu
                is_valid = False
                while not is_valid:
                    try:
                        selection = int(input('\nSelect from the following menu:\n'
                                              '\t1. Display all U.S. States in'
                                              ' alphabetical order along with'
                                              ' Capital and Bird\n'
                                              '\t2. Search for a specific State and'
                                              ' display the appropriate Capital'
                                              ' and Bird\n'
                                              '\t3. Update a Bird for a specific'
                                              ' State\n'
                                              '\t4. Exit the program\n'))
                    except ValueError:
                        print('You must enter 1, 2, 3, or 4. Please try again.')
                    else:
                        if selection >= 1 and selection <= 4:
                            is_valid = True
                            break
                        else:
                            print('You must enter 1, 2, 3, or 4. Please try again.')
            else:
                print('Not a valid U.S. State. Please try again.')

        # Option 3
        elif selection == 3:
            selected_state = str(input('You selected 3. Please enter a State:\n'))
            if selected_state.title() in states:
                bird_update = str(input('What would you like to change the bird'
                                        ' of this State to?\n'))
                state_birds.update(selected_state=bird_update)
                birds[states.index(selected_state.title())] = bird_update.title()
                print('The bird of', selected_state.title(), 'has been changed'
                      ' to the', birds[states.index(selected_state.title())], '.')

                # Menu
                is_valid = False
                while not is_valid:
                    try:
                        selection = int(input('\nSelect from the following menu:\n'
                                              '\t1. Display all U.S. States in'
                                              ' alphabetical order along with'
                                              ' Capital and Bird\n'
                                              '\t2. Search for a specific State and'
                                              ' display the appropriate Capital'
                                              ' and Bird\n'
                                              '\t3. Update a Bird for a specific'
                                              ' State\n'
                                              '\t4. Exit the program\n'))
                    except ValueError:
                        print('You must enter 1, 2, 3, or 4. Please try again.')
                    else:
                        if selection >= 1 and selection <= 4:
                            is_valid = True
                            break
                        else:
                            print('You must enter 1, 2, 3, or 4. Please try again.')
            else:
                print('Not a valid U.S. State. Please try again.')

    # Option 4
    print('You selected 4.')
    print('Thank you for trying the US State Capital and Bird Database.')
    print('**************************************************')
    return

if __name__ == "__main__":
    main()
