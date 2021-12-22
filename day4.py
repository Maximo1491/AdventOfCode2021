import helper

class Board:
    def __init__(self, input):
        self.play_board = []
        for line in input:
            self.play_board += [[int(s) for s in line.split() if s.isdigit()]]
        self.rows = [0,0,0,0,0]
        self.columns = [0,0,0,0,0]

    def check_draw(self, draw):
        for x in range(len(self.play_board)):
            for y in range(len(self.play_board[x])):
                if self.play_board[x][y] == draw:
                    self.rows[x] += 1
                    self.columns[y] += 1

    def check_bingo(self) -> bool:
        for i in self.rows:
            if i == 5:
                return True
        for i in self.columns:
            if i == 5:
                return True
        return False

class Bingo:
    def __init__(self, input):
        self.draw = [int(x) for x in input[0].split(',')]
        input = input[2:]
        self.boards = []
        self.current_draw = 0
        board = []
        for line in input:
            if line == '':
                self.boards += [Board(board)]
                board = []
                continue
            
            board += [line]

    def update_boards(self, draw):
        for board in self.boards:
            board.check_draw(draw)

        bingo_boards = []
        for board in self.boards:
            if board.check_bingo():
                bingo_boards += [board]

        return bingo_boards

    def update_draw(self):
        boards = self.update_boards(self.draw[self.current_draw])
        if self.current_draw < len(self.draw)-1:
            self.current_draw += 1
        return boards

def part1():
    bingo = Bingo(helper.get_daily_input_strings())
    while range(len(bingo.draw)):
        boards = bingo.update_draw()
        if len(boards) > 0:
            for board in boards:
                drawn_numbers = bingo.draw[:bingo.current_draw]
                sum = 0
                for x in range(len(board.play_board)):
                    for y in range(len(board.play_board[x])):
                        if board.play_board[x][y] not in drawn_numbers:
                            sum += board.play_board[x][y]
                
                return sum * bingo.draw[bingo.current_draw-1]

    return "failed to bingo :("

def part2():
    bingo = Bingo(helper.get_daily_input_strings())
    while range(len(bingo.draw)):
        boards = bingo.update_draw()
        if len(boards) > 0:
            for board in boards:
                bingo.boards.remove(board)
                if len(bingo.boards) == 0:
                    drawn_numbers = bingo.draw[:bingo.current_draw]
                    sum = 0
                    for x in range(len(board.play_board)):
                        for y in range(len(board.play_board[x])):
                            if board.play_board[x][y] not in drawn_numbers:
                                sum += board.play_board[x][y]
                    
                    return sum * bingo.draw[bingo.current_draw-1]

    return "failed to bingo :("