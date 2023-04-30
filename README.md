# List-Manipulation-with-JSON-Storage

This is a simple Python program that allows the user to manipulate a list of items by adding, removing, displaying, clearing or quitting the program. The list data is stored in a JSON file for persistence across program executions.

## Getting Started
### Prerequisites
To run this program, you need to have Python 3.x installed on your system. You can download the latest version of Python from the official website: https://www.python.org/downloads/

### Installing
To install this program, simply clone this repository to your local machine:

`git clone https://github.com/<username>/python-list-manipulation.git`

### Running the Program
To run the program, navigate to the project directory in a terminal and run the following command:

`python list_manipulation.py`

### Usage
When the program starts, it loads the list data from the "list.JSON" file (if it exists), or creates an empty list if the file does not exist.

The program then prompts the user to choose from the following 5 options:

1. Add an element to the list
2. Remove an element from the list
3. Display the list
4. Clear the list
5. Quit

The user can enter the corresponding number to choose an option. If the input is not valid, the program displays an error message and prompts the user to try again.

If the user chooses to add an element to the list, the program prompts the user to enter the name of the element. The element is then added to the list and a confirmation message is displayed.

If the user chooses to remove an element from the list, the program prompts the user to enter the name of the element. If the element is in the list, it is removed and a confirmation message is displayed. Otherwise, an error message is displayed.

If the user chooses to display the list, the program shows the content of the list with each element numbered.

If the user chooses to clear the list, the program removes all elements from the list and displays a confirmation message.

If the user chooses to quit the program, the program saves the list data to the "list.JSON" file and exits.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
This program was created as a learning exercise for basic Python programming and file I/O with JSON. It can be used as a starting point for more complex list manipulation programs with persistent data storage.
