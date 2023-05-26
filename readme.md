# Pre-Requisites -

The prerequisites for running the Python code for the robot simulation are:

1.  Python: Ensure that you have Python installed on your system. You can download and install Python from the official Python website (https://www.python.org/). The code provided is compatible with Python 3.x versions.

2.  Text Editor or IDE: You will need a text editor or an integrated development environment (IDE) to write and save the Python code. There are many options available, such as Visual Studio Code, PyCharm, Sublime Text, Atom, or Notepad++. Choose the one you are comfortable with or prefer.

3.  Command Prompt or Terminal: To execute the Python code, you will need a command prompt (Windows) or terminal (Mac or Linux). These are standard command-line interfaces where you can run commands.

4.  Basic Python Knowledge: Familiarity with the basics of the Python programming language will be beneficial in understanding and modifying the code if needed. Understanding concepts such as variables, loops, conditionals, functions, and lists will be helpful.

By fulfilling these prerequisites, you will be ready to run the Python code for the robot simulation and interact with the program to provide the grid dimensions and instructions for the robot.


# To run the code -

1.  Open a text editor or an integrated development environment (IDE) of your choice.

2.  Create a new Python file and copy the code into the file.

3.  Save the file with a .py extension, for example, robot_simulation.py.

4.  Open a command prompt or terminal.

5.  Navigate to the directory where you saved the Python file using the cd command. For example:

    `cd /path/to/directory`

6.  Run the Python file using the python command followed by the file name. For example:

    `python robot_simulation.py`

7.  The program will prompt you to enter the number of rows and columns for the grid. Provide the desired dimensions and press Enter.

8.  Next, the program will ask you to enter a command of instructions for the robot. Input the instructions and press Enter.

9.  The program will display the current location of the robot and the visual representation of the grid with the robot's position.

10. You can repeat steps 8-9 to run the simulation with different commands.

11. You can exit the simulation by either entering 0 or Exit in the command.

12. To re-run the simulation, repeat steps 6-9.

That's it! You have successfully run the code for the robot simulation.


# Code and Functionality Explaination -

1.  The code defines a class named Robot, which represents a robot that can move on a 2D grid.

2.  In the constructor (__init__ method) of the Robot class, the following attributes are initialized:

    - directions: A list of directions (N, E, S, W).
    - direction_index: An index representing the current direction the robot is facing.
    - row and column: The current position of the robot on the grid.
    - num_rows and num_cols: The dimensions of the grid.
    - grid: A 2D list representing the grid, initially filled with empty spaces.

3.  The move method takes a string of instructions and iterates over each instruction.

    - If the instruction is 'M' (movement), the _move_forward method is called to move the robot one step in the current direction.
    - If the instruction is a directional instruction (N, E, S, W), the _change_direction method is called to update the direction of the robot.

4.  The _move_forward method checks the current direction of the robot and moves it one step forward in the grid if possible. It takes into account the grid boundaries and prevents the robot from moving outside the grid.

5.  The _change_direction method updates the direction of the robot based on the given instruction. It only changes the direction if the instruction is different from the current direction.

6.  The get_current_location method returns a string representing the current location of the robot in the format (row, column, direction).

7.  The print_grid method prints a visual representation of the grid and the current position of the robot. It iterates over each row and column in the grid, printing the grid boundaries, empty spaces, and the robot's position (denoted by 'R').

8.  The program prompts the user to input the number of rows and columns for the grid and the command of instructions for the robot.

9.  An instance of the Robot class is created with the provided grid dimensions.

10. The move method is called on the robot instance with the given command, which updates the robot's position based on the instructions.

11. The get_current_location method is called to retrieve and print the current location of the robot.

12. The print_grid method is called to display the visual representation of the grid and the robot's position.

Overall, this code simulates a robot moving on a grid based on given instructions and provides the final location of the robot. It also visually represents the grid and the robot's position for better understanding and visualization.


# COmpute Time Complexity of Code -

The move method iterates over each instruction in the command and performs constant time operations based on the
instruction. Therefore, the time complexity of the move method is still O(n), where n is the length of the command.

The print_grid method loops over each row and column in the grid, which has a size of num_rows x num_cols. There
fore, the time complexity of the print_grid method is O(num_rows x num_cols).

The rest of the operations in the code, such as changing direction or obtaining the current location, are consta
nt time operations and do not depend on the size of the grid or the length of the command.

Hence, the `overall time complexity` of the modified code remains `O(n + num_rows x num_cols)`, where n is the length
of the command and num_rows and num_cols are the dimensions of the grid.
