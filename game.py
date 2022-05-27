import json

map_maze = [
    [[1, 0, 1, 0], [1, 1, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 1, 1, 0], [1, 0, 0, 1], [1, 1, 0, 0], [1, 0, 1, 1],
     [1, 1, 0, 0]],
    [[1, 0, 0, 1], [0, 1, 1, 0], [0, 0, 1, 1], [1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 0, 0], [0, 0, 1, 1], [1, 0, 1, 0],
     [0, 1, 1, 0]],
    [[0, 0, 1, 1], [1, 0, 0, 0], [1, 0, 1, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 1, 0, 1], [1, 0, 1, 1], [1, 0, 1, 0],
     [1, 1, 0, 0]],
    [[1, 1, 0, 1], [0, 1, 0, 1], [1, 0, 0, 1], [1, 0, 1, 0], [0, 1, 0, 0], [0, 0, 1, 1], [1, 0, 1, 0], [1, 0, 1, 0],
     [0, 1, 1, 0]],
    [[0, 0, 1, 1], [0, 1, 1, 0], [0, 1, 0, 1], [1, 1, 0, 1], [0, 0, 1, 1], [1, 0, 0, 0], [1, 0, 1, 0], [1, 0, 1, 0],
     [1, 1, 0, 0]],
    [[1, 0, 0, 1], [1, 0, 1, 0], [0, 1, 1, 0], [0, 1, 0, 1], [1, 1, 0, 1], [0, 0, 1, 1], [1, 1, 0, 0], [1, 0, 0, 1],
     [0, 1, 1, 0]],
    [[0, 1, 0, 1], [1, 0, 0, 1], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 1],
     [1, 1, 0, 0]],
    [[0, 1, 0, 1], [0, 1, 0, 1], [1, 0, 1, 1], [1, 1, 0, 0], [0, 1, 0, 1], [1, 1, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0],
     [0, 1, 0, 1]],
    [[0, 1, 0, 1], [0, 0, 1, 1], [1, 1, 0, 0], [0, 1, 0, 1], [0, 1, 0, 1], [0, 0, 1, 1], [0, 0, 1, 0], [1, 1, 0, 0],
     [0, 1, 1, 1]],
    [[0, 0, 1, 1], [1, 0, 1, 0], [0, 0, 1, 0], [0, 1, 1, 0], [0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 1, 0], [0, 0, 1, 1],
     [1, 0, 1, 0]]
]
start_position_row = 0
start_position_column = 0
wrong_step = [[3, 1], [1, 3], [1, 4], [3, 3], [5, 5], [8, 5], [6, 8]]
finish_step = [9, 8]


class Game(object):

    def __init__(self, maze, start_position_row, start_position_column):
        self.maze = maze
        self.current_position_row = start_position_row
        self.current_position_column = start_position_column
        self.previus_step = []
        self.saved_game = {}

    def start_game(self):
        confirm = input('Hello, you wish continue? Y/N: ')

        if confirm == 'y' or confirm == 'Y':
            self.launch_round()
        elif confirm == 'n' or confirm == 'N':
            print('Ok, goodbye..')

    def save_game(self):
        confirm = input('You want to save this game, and start from this step? Y/N: ')

        if confirm == 'y' or confirm == 'Y':
            game = {
                "current_position_row": self.current_position_row,
                "current_position_column": self.current_position_column
            }
            self.saved_game = json.dumps(game)
        elif confirm == 'n' or confirm == 'N':
            self.saved_game = {}

    def restart_game(self):
        confirm = input('You want a new chance? Y/N: ')

        if confirm == 'y' or confirm == 'Y':
            self.current_position_row = 0
            self.current_position_column = 0
            self.previus_step = []

            if len(self.saved_game):
                print('You have saved game! Download them..')
                downloaded_game = json.loads(self.saved_game)
                self.current_position_row = downloaded_game['current_position_row']
                self.current_position_column = downloaded_game['current_position_column']
                print('Your last position is:', [self.current_position_row, self.current_position_column])

            self.launch_round()
        elif confirm == 'n' or confirm == 'N':
            print('Ok, goodbye..')


    def launch_round(self):
        if not len(self.previus_step):
            print('Please, use W,A,S,D buttons: ')

        self.ask_for_user_step()

    def ask_for_user_step(self):
        user_keypress = input('Where will you go?: ')
        self.check_user_step(user_keypress)

    def check_user_step(self, direction):
        if direction == 'w' or direction == 'W':
            result = self.maze[self.current_position_row][self.current_position_column][0]
            self.user_step_result_action(result, direction)

        elif direction == 'd' or direction == 'D':
            result = self.maze[self.current_position_row][self.current_position_column][1]
            self.user_step_result_action(result, direction)

        elif direction == 's' or direction == 'S':
            result = self.maze[self.current_position_row][self.current_position_column][2]
            self.user_step_result_action(result, direction)

        elif direction == 'a' or direction == 'A':
            result = self.maze[self.current_position_row][self.current_position_column][3]
            self.user_step_result_action(result, direction)

        else:
            print('No no no, you should use only W,A,S,D buttons!')
            self.ask_for_user_step()

    def user_step_result_action(self, result, direction):
        if result:
            print('Wall.. end game!')
            self.save_game()
            self.restart_game()
        else:
            self.update_user_previus_position(self.current_position_row, self.current_position_column)
            self.update_user_position(direction)

            if [self.current_position_row, self.current_position_column] in self.previus_step:
                print('You chickened out')
                self.save_game()
                self.restart_game()
                return

            if [self.current_position_row, self.current_position_column] in wrong_step:
                print('You turned to a deadlock')
                self.restart_game()
                return

            if [self.current_position_row, self.current_position_column] == finish_step:
                print('Congratulations! You have completed the maze!')
                return

            print('Very good..')
            self.launch_round()

    def update_user_position(self, direction):
        if direction == 'w' or direction == 'W':
            self.current_position_row = self.current_position_row - 1
        elif direction == 'd' or direction == 'D':
            self.current_position_column = self.current_position_column + 1
        elif direction == 's' or direction == 'S':
            self.current_position_row = self.current_position_row + 1

        elif direction == 'a' or direction == 'A':
            self.current_position_column = self.current_position_column - 1

    def update_user_previus_position(self, row, column):
        self.previus_step.append([row, column])


game = Game(map_maze, start_position_row, start_position_column)
game.start_game()
