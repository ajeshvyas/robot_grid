Pseudo step for the Program :

1.  Define a class called Robot with the following attributes:

    - directions: A list of directions (N, E, S, W).
    - direction_index: An index representing the current direction the robot is facing.
    - row and column: The current position of the robot on the grid.
    - num_rows and num_cols: The dimensions of the grid.
    - grid: A 2D list representing the grid, initially filled with empty spaces.

2.  Create an instance of the Robot class.

3.  Prompt the user to enter the number of rows and columns for the grid.

4.  Prompt the user to enter a command of instructions for the robot.

5.  Call the move method on the robot instance and pass the command of instructions as an argument.

6.  Inside the move method, iterate over each instruction in the command:

    - If the instruction is 'M', call the _move_forward method.
    - If the instruction is a directional instruction (N, E, S, W), call the _change_direction method.

7.  Inside the _move_forward method, check the current direction of the robot:

    - If the current direction is 'N' and the row is greater than 0, decrease the row by 1.
    - If the current direction is 'E' and the column is less than num_cols - 1, increase the column by 1.
    - If the current direction is 'S' and the row is less than num_rows - 1, increase the row by 1.
    - If the current direction is 'W' and the column is greater than 0, decrease the column by 1.

8.  Inside the _change_direction method, check the instruction:

    - If the instruction is 'N' and the current direction is not 'N', set the direction index to 0.
    - If the instruction is 'E' and the current direction is not 'E', set the direction index to 1.
    - If the instruction is 'S' and the current direction is not 'S', set the direction index to 2.
    - If the instruction is 'W' and the current direction is not 'W', set the direction index to 3.
    
9.  After the move method is executed, call the get_current_location method to get the current location of the robot.

10. Print the current location of the robot.

11. Call the print_grid method to display the visual representation of the grid and the robot's position.