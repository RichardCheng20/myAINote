import random
import os
import signal
import time
from copy import deepcopy


# min and max of the evaluate function is -24 and 24
MIN = -10000
MAX = 10000


def readInput(n, path="input.txt"):
    with open(path, 'r') as f:
        lines = f.readlines()

        piece_type = int(lines[0])

        previous_board = [[int(x) for x in line.rstrip('\n')] for line in lines[1:n + 1]]
        board = [[int(x) for x in line.rstrip('\n')] for line in lines[n + 1: 2 * n + 1]]

        return piece_type, previous_board, board


def writeOutput(result, path="output.txt"):
    res = ""
    if result == "PASS":
        res = "PASS"
    else:
        res += str(result[0]) + ',' + str(result[1])

    with open(path, 'w') as f:
        f.write(res)


def compare_board(board1, board2):
    for i in range(5):
        for j in range(5):
            if board1[i][j] != board2[i][j]:
                return False
    return True


def read_move_count():
    if not os.path.exists('./move.txt'):
        write_move_count(1)
        return 1
    with open('./move.txt', 'r') as f:
        return int(f.readline())


def write_move_count(count):
    with open('./move.txt', 'w') as f:
        f.write(str(count))


def increase_move_count():
    cur_move = read_move_count() + 1
    write_move_count(cur_move)


def copy_board(board):
    return deepcopy(board)


def find_neighbors(i, j):
    neighbors = []
    if i > 0:
        neighbors.append((i - 1, j))
    if j > 0:
        neighbors.append((i, j - 1))
    if i < 4:
        neighbors.append((i + 1, j))
    if j < 4:
        neighbors.append((i, j + 1))
    return neighbors


def set_timeout(num, callback):
    def wrap(func):
        def handle(signum, frame):
            raise RuntimeError

        def to_do(*args, **kwargs):
            try:
                signal.signal(signal.SIGALRM, handle)
                signal.alarm(num)
                # print('start alarm signal.')
                r = func(*args, **kwargs)
                # print('close alarm signal.')
                signal.alarm(0)
                return r
            except RuntimeError as e:
                callback()

        return to_do

    return wrap


def after_timeout():  # 超时后的处理函数
    print("Time out!")


# def create_new_log():
#     with open("./timeCost.txt", 'w') as f:
#         f.write("")


def save_log(time_cost):
    if os.path.exists("./timeCost.txt"):
        append_write = 'a'  # append if already exists
    else:
        append_write = 'w'  # make a new file if no
    with open("./timeCost.txt", append_write) as f:
        f.write(time_cost + "\n")


class MyPlayer3:
    def __init__(self, board_manage, side):
        self.board_manage = board_manage
        self.side = side
        self.search_depth = 3
        self.moveCount = read_move_count()

    def move(self):
        self.moveCount = read_move_count()
        if self.moveCount <= 4:
            good_places = [(2, 2), (1, 2), (3, 2), (2, 1), (2, 3), (1, 1), (1, 3), (3, 1), (3, 3)]
            for place in good_places:
                if self.board_manage.valid_place_check(place[0], place[1], self.side):
                    action = place
                    increase_move_count()
                    log_str = "Move count " + str(self.moveCount) + "  Move: " + str(action) + "   "
                    save_log(log_str)
                    return action

        if self.moveCount >= 8:
            self.search_depth += 1

        start = time.time()
        action = self.mini_max_search_with_Alpha_Beta()
        end = time.time()

        log_str = "Move count " + str(self.moveCount)

        # timeout solution
        if action is None:
            log_str += "   随机选择   "
            action = random.choice(self.board_manage.valid_places())

        log_str += ("Move: " + str(action) + "    " + "time cost is {}".format(end - start))
        save_log(log_str)
        # print("Move")
        # print(action)
        # print("time cost is {}".format(end - start))
        increase_move_count()
        return action

    @set_timeout(8, after_timeout)
    def mini_max_search_with_Alpha_Beta(self):
        if not self.board_manage.valid_places():
            print("no valid places:PASS")
            return "PASS"

        # return Max of mini_value
        values = []
        for move in self.board_manage.valid_places():
            values.append(self.mini_value(MIN, MAX, (move[0], move[1]), self.moveCount, self.board_manage, 0))
        move_index = values.index(max(values))
        return self.board_manage.valid_places()[move_index]

    def mini_value(self, alpha, beta, action, moveCount, last_board_manage, depth):
        # check if end
        if self.check_if_end(depth, last_board_manage.last_board, last_board_manage.board, action, moveCount):
            return self.heuristic_evaluate(last_board_manage)

        # current state board
        cur_board_manage = last_board_manage.copy_board_manage()
        cur_board_manage.side = 3 - last_board_manage.side
        cur_board_manage.last_board = copy_board(cur_board_manage.board)
        if action != "PASS":
            cur_board_manage.move_one_step(action[0], action[1], last_board_manage.side)

        if not cur_board_manage.valid_places():
            return self.max_value(alpha, beta, "PASS", moveCount + 1, cur_board_manage, depth + 1)
        value = MAX

        # loop for max_value
        for move in cur_board_manage.valid_places():
            value = min(value,
                        self.max_value(alpha, beta, (move[0], move[1]), moveCount + 1, cur_board_manage, depth + 1))
            if value <= alpha:
                return value
            beta = min(beta, value)
        return value

    def max_value(self, alpha, beta, action, moveCount, last_board_manage, depth):
        # check if end
        if self.check_if_end(depth, last_board_manage.last_board, last_board_manage.board, action, moveCount):
            return self.heuristic_evaluate(last_board_manage)

        # current state board
        cur_board_manage = last_board_manage.copy_board_manage()
        cur_board_manage.side = 3 - last_board_manage.side
        cur_board_manage.last_board = copy_board(cur_board_manage.board)
        if action != "PASS":
            cur_board_manage.move_one_step(action[0], action[1], last_board_manage.side)

        if not cur_board_manage.valid_places():
            return self.mini_value(alpha, beta, "PASS", moveCount + 1, cur_board_manage, depth + 1)
        value = MIN

        # loop for max_value
        for move in cur_board_manage.valid_places():
            value = max(value,
                        self.mini_value(alpha, beta, (move[0], move[1]), moveCount + 1, cur_board_manage, depth + 1))
            if value >= beta:
                return value
            alpha = max(alpha, value)
        return value

    def check_if_end(self, depth, last_board, board, action, moveCount):
        # Case 1: max move reached
        if depth >= self.search_depth or moveCount > 12:
            return True
        # Case 2: two players all pass the move.
        if compare_board(last_board, board) and action == "PASS":
            return True
        return False

    # heuristic, may change later
    def heuristic_evaluate(self, board_manage):
        black_place = set()
        white_place = set()
        empty_place = set()

        liberty_black = 0
        liberty_white = 0

        num_black = 0
        num_white = 0

        acquired_black = 0
        acquired_white = 0

        for i in range(5):
            for j in range(5):
                if board_manage.board[i][j] == 1:
                    num_black += 1
                    black_place.add((i, j))
                elif board_manage.board[i][j] == 2:
                    num_white += 1
                    white_place.add((i, j))
                else:
                    empty_place.add((i, j))
                    if board_manage.is_acquired_position(i, j, 1):
                        acquired_black += 1
                    if board_manage.is_acquired_position(i, j, 2):
                        acquired_white += 1

        # calculate liberty
        for blank_chess in empty_place:
            blank_neighbors = find_neighbors(blank_chess[0], blank_chess[1])
            for neighbor in blank_neighbors:
                in_black_flag = False
                in_white_flag = False
                common_flag = False
                if neighbor in black_place and neighbor not in white_place:
                    liberty_black += 1
                    in_black_flag = True
                if neighbor in white_place and neighbor not in black_place:
                    liberty_white += 1
                    in_white_flag = True
                if neighbor in white_place and neighbor in black_place:
                    liberty_black -= 0.5
                    liberty_white -= 0.5
                    common_flag = True
                if in_black_flag or in_white_flag or common_flag:
                    break

        black_score = num_black + liberty_black * 0.125 + acquired_black * 0.55
        white_score = num_white + liberty_white * 0.125 + acquired_white * 0.55

        if self.side == 1:
            return black_score - white_score
        else:
            return white_score - black_score


class BoardManage:
    def __init__(self):
        self.size = 5
        self.last_board = None
        self.board = None
        self.side = None
        self.died_pieces = []

    def set_board(self, side, last_board, board):
        self.side = side

        for i in range(self.size):
            for j in range(self.size):
                if previous_board[i][j] == side and board[i][j] != side:
                    self.died_pieces.append((i, j))

        self.last_board = last_board
        self.board = board

    def valid_places(self):
        places = []
        for i in range(5):
            for j in range(5):
                if self.valid_place_check(i, j, self.side):
                    places.append((i, j))
        return places

    def valid_place_check(self, i, j, piece_type):
        board = self.board

        # Check if the place is in the board range
        if not (0 <= i < len(board)):
            return False
        if not (0 <= j < len(board)):
            return False

        # Check if the place already has a piece
        if board[i][j] != 0:
            return False

        # Copy the board for testing
        test_go = self.copy_board_manage()
        test_board = test_go.board

        # Check if the place has liberty
        test_board[i][j] = piece_type
        test_go.update_board(test_board)
        if test_go.find_liberty(i, j):
            return True

        # If not, remove the died pieces of opponent and check again
        test_go.remove_died_pieces(3 - piece_type)
        if not test_go.find_liberty(i, j):
            return False

        # Check special case: repeat placement causing the repeat board state (KO rule)
        else:
            if self.died_pieces and compare_board(self.last_board, test_go.board):
                return False
        return True

    def move_one_step(self, i, j, side):
        self.place_stone(i, j, side)
        self.remove_died_pieces(3 - side)

    def is_acquired_position(self, i, j, side):
        neighbors = find_neighbors(i, j)
        for neighbor in neighbors:
            if self.board[neighbor[0]][neighbor[1]] != side:
                return False
        return True

    def update_board(self, new_board):
        self.board = new_board

    def check_start(self):
        chess_count = 0
        chess_color = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.last_board[i][j] != 0:
                    chess_count += 1
                    chess_color = self.last_board[i][j]
        if chess_count == 0:
            return True
        if chess_count == 1 and chess_color != self.side:
            return True
        return False

    def place_stone(self, i, j, side):
        self.board[i][j] = side

    def copy_board_manage(self):
        return deepcopy(self)

    def find_liberty(self, i, j):
        board = self.board
        ally_members = self.ally_dfs(i, j)
        for member in ally_members:
            neighbors = self.detect_neighbor(member[0], member[1])
            for piece in neighbors:
                # If there is empty space around a piece, it has liberty
                if board[piece[0]][piece[1]] == 0:
                    return True
        # If none of the pieces in a allied group has an empty space, it has no liberty
        return False

    def ally_dfs(self, i, j):
        stack = [(i, j)]  # stack for DFS serach
        ally_members = []  # record allies positions during the search
        while stack:
            piece = stack.pop()
            ally_members.append(piece)
            neighbor_allies = self.detect_neighbor_ally(piece[0], piece[1])
            for ally in neighbor_allies:
                if ally not in stack and ally not in ally_members:
                    stack.append(ally)
        return ally_members

    def detect_neighbor(self, i, j):
        board = self.board
        neighbors = []
        if i > 0:
            neighbors.append((i - 1, j))
        if i < len(board) - 1:
            neighbors.append((i + 1, j))
        if j > 0:
            neighbors.append((i, j - 1))
        if j < len(board) - 1:
            neighbors.append((i, j + 1))
        return neighbors

    def detect_neighbor_ally(self, i, j):
        board = self.board
        neighbors = self.detect_neighbor(i, j)  # Detect neighbors
        group_allies = []
        # Iterate through neighbors
        for piece in neighbors:
            # Add to allies list if having the same color
            if board[piece[0]][piece[1]] == board[i][j]:
                group_allies.append(piece)
        return group_allies

    def remove_died_pieces(self, piece_type):
        died_pieces = self.find_died_pieces(piece_type)
        if not died_pieces: return []
        self.remove_certain_pieces(died_pieces)
        return died_pieces

    def find_died_pieces(self, piece_type):
        board = self.board
        died_pieces = []

        for i in range(len(board)):
            for j in range(len(board)):
                # Check if there is a piece at this position:
                if board[i][j] == piece_type:
                    # The piece die if it has no liberty
                    if not self.find_liberty(i, j):
                        died_pieces.append((i, j))
        return died_pieces

    def remove_certain_pieces(self, positions):
        board = self.board
        for piece in positions:
            board[piece[0]][piece[1]] = 0
        self.update_board(board)


if __name__ == "__main__":
    p_type, previous_board, cur_board = readInput(5)
    b_manage = BoardManage()
    b_manage.set_board(p_type, previous_board, cur_board)
    player = MyPlayer3(b_manage, p_type)
    if player.board_manage.check_start():
        print("start")
        write_move_count(1)

    act = player.move()

    writeOutput(act)
