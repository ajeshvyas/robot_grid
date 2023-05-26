class Robot:
    # Constructor to initialize the initial state of Robot
    def __init__(self, num_rows, num_cols):
        self.directions = ["N", "E", "S", "W"]  # North, East, South, West
        self.direction_index = 2  # Starting direction is South
        self.row = 0
        self.column = 0
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.grid = [[" " for _ in range(num_cols)] for _ in range(num_rows)]

    # Driver method to fetch the instructions and get them executed by other methods
    def move(self, instructions):
        for instruction in instructions:
            if instruction == "M":
                self._move_forward()
            else:
                self._change_direction(instruction)

    # Method to move the Robot according to the current position and Command
    def _move_forward(self):
        if self.directions[self.direction_index] == "N" and self.row > 0:
            self.row -= 1
        elif (
            self.directions[self.direction_index] == "E"
            and self.column < self.num_cols - 1
        ):
            self.column += 1
        elif (
            self.directions[self.direction_index] == "S"
            and self.row < self.num_rows - 1
        ):
            self.row += 1
        elif self.directions[self.direction_index] == "W" and self.column > 0:
            self.column -= 1

    # Method to change the Direction of Robot according to the command and current direction
    def _change_direction(self, instruction):
        if instruction == "N" and self.directions[self.direction_index] != "N":
            self.direction_index = 0
        elif instruction == "E" and self.directions[self.direction_index] != "E":
            self.direction_index = 1
        elif instruction == "S" and self.directions[self.direction_index] != "S":
            self.direction_index = 2
        elif instruction == "W" and self.directions[self.direction_index] != "W":
            self.direction_index = 3

    # Method to get current location of Robot in (Row, Column, Direction) format
    def get_current_location(self):
        return f"Robot Location: ({self.row},{self.column},{self.directions[self.direction_index]})"

    # Method to print the 2D Grid View with Robot's current location
    def print_grid(self):
        print("   ", end="")
        for col in range(self.num_cols):
            print(f"{col}  ", end="")  # Print column numbers
        print()
        for row in range(self.num_rows):
            print("  ", "+--" * self.num_cols)
            print(f"{row} ", end="")  # Print row number
            for col in range(self.num_cols):
                if row == self.row and col == self.column:
                    print("| R", end="")
                else:
                    print("|  ", end="")
            print("|")
        print("  ", "+--" * self.num_cols)


# Driver Code to initiate and Run the Robot class

start = True  # Initializing variable for looping over the move method
try:
    rows = int(input("Enter the Grid Rows : "))  # Number of rows of grid
    columns = int(input("Enter the Grid Columns: "))  # Number of columns of grid
    if not rows or not columns:  # Raise value error if the rows or columns are 0
        raise ValueError()
    robot = Robot(rows, columns)  # Object of Robot class
except ValueError:
    start = False
    print("Please enter a Valid Integer !")

while start:
    print("Enter 0 or Exit to exit the code.")  # Information to exit the simulation
    command = input("Enter the command: ")  # Input of the user for command
    if (
        command == "0" or command.lower() == "exit"
    ):  # If entered 0 or exit, it will break the loop and exit the simulation
        print("Thanks for visiting !")
        break
    robot.move(
        command.upper()
    )  # Calling move with command, taking upper to avoid any case sensitivity
    print(
        robot.get_current_location()
    )  # Print the current location of Robot in terms of (Row,Column,Direction)
    robot.print_grid()  # Print the Grid with Robot's current location
