import random
import numpy as np
import time
import signal
from copy import deepcopy
import json

draw_reward = 0
win_reward = 100
lose_reward = -100

boardSize = 5

blank_space = 0
black = 1
white = 2
IN_PLAY = 1
DRAW = 0
WIN = 1
LOSE = -1
MIN = -9999
MAX = 9999

fpath = "./"


def set_timeout(num, callback):
    def wrap(function):
        def handle(signum, frame):
            raise RuntimeError

        def to_do(*args, **kwargs):
            try:
                signal.signal(signal.SIGALRM, handle)
                signal.alarm(num)
                print('开始计时')
                result = function(*args, **kwargs)
                print('停止计时')
                signal.alarm(0)
                return result
            except RuntimeError as e:
                callback()

        return to_do

    return wrap


def callback():  # 超时后的处理函数
    path = fpath + "cresult.txt"
    f = open(path, "a+")
    print("Time out!, play random step")
    print("Time out!, play random step", file=f)
    f.close()


def readInput(path=fpath + "input.txt"):
    with open(path, 'r') as input:
        lines = input.readlines()
        # black or white represents 1 or 2
        side = int(lines[0])

        last_board = [[int(x) for x in line.rstrip('\n')] for line in lines[1:6]]
        current_board = [[int(x) for x in line.rstrip('\n')] for line in lines[6:11]]

        return side, last_board, current_board


def read_moves(path=fpath + "moves.txt"):
    with open(path, 'r') as input:
        lines = input.readlines()
        current_moves = int(lines[0])
        return current_moves


def write_moves(result, path=fpath + "moves.txt"):
    with open(path, 'w') as output:
        output.write(result)


def increase_move():
    current_moves = read_moves()
    current_moves += 1
    write_moves(str(current_moves))


def writeOutput(result, path=fpath + "output.txt"):
    with open(path, 'w') as output:
        if (result == "PASS"):
            output.write("PASS")
        else:
            output.write('' + str(result[0]) + ',' + str(result[1]))


class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


class Board:
    def __init__(self, size=5):

        self.size = size
        self.num_moves = 0
        self.max_moves = 12
        self.game_state = IN_PLAY
        self.dead_pieces = []
        self.komi = size / 2
        self.me_passed_move = False
        self.op_passed_move = False
        self.capture_reward = 0

    def set_board(self, side, previous_board, current_board):
        self.side = side
        self.current_board = current_board
        self.previous_board = previous_board

    def set_passed_step(self, side):
        if side == self.side:
            self.me_passed_move = True
        else:
            self.op_passed_move = True

    def if_first_play(self):
        return self.side == black

    def get_dead_pieces(self, side):
        dead_pieces = []
        for row in range(boardSize):
            for col in range(boardSize):
                if self.current_board[row][col] == side:
                    if not self.has_liberty(row, col):
                        dead_pieces.append((row, col))
        return dead_pieces

    def remove_dead_pieces(self, side):
        dead_pieces = []
        for row in range(self.size):
            for col in range(self.size):
                if self.current_board[row][col] == side:
                    if not self.has_liberty(row, col):
                        dead_pieces.append((row, col))
        # clean the deads
        for dead in dead_pieces:
            self.current_board[dead[0]][dead[1]] = blank_space

            # every time eliminate an opponent the capture reward+1
            # self.capture_reward += 1

    def current_score_without_komi(self):
        my_score = 0
        op_score = 0
        for row in range(boardSize):
            for col in range(boardSize):
                if self.current_board[row][col] == self.side:
                    my_score += 1
                elif self.current_board[row][col] == (3 - self.side):
                    op_score += 1
        return my_score, op_score

    def black_white_score(self):
        black = 0
        white = 0
        for row in range(boardSize):
            for col in range(boardSize):
                if self.current_board[row][col] == 1:
                    black += 1
                elif self.current_board[row][col] == 2:
                    white += 1
        return black, white

    def update_game_state(self):
        # remove dead pieces
        self.remove_dead_pieces(3 - self.side)
        status = self.check_game_status()
        self.game_state = status

    def check_game_status(self):
        my_score, op_score = self.current_score_without_komi()
        result = IN_PLAY
        if self.side == white:
            my_score += self.komi
        else:
            op_score += self.komi

        # judge if the game is ended
        if not self.is_game_ended():
            return IN_PLAY
        else:
            if my_score > op_score:
                result = WIN
            elif my_score < op_score:
                result = LOSE
            else:
                result = DRAW
        return result

    def is_same_board(self):

        for row in range(self.size):
            for col in range(self.size):
                if self.current_board[row][col] != self.previous_board[row][col]:
                    return False
        return True

    def get_board_diff_step(self):

        if not self.is_same_board():
            for row in range(self.size):
                for col in range(self.size):
                    if self.current_board[row][col] != self.previous_board[row][col]:
                        return row, col
        else:
            return -1, -1

    def is_start_of_game(self):
        chess_count = 0
        chess_color = 0
        for row in range(self.size):
            for col in range(self.size):
                if self.previous_board[row][col] != 0:
                    chess_count += 1
                    chess_color = self.previous_board[row][col]
        if chess_count == 0:
            return True
        if chess_count == 1 and chess_color != self.side:
            return True
        return False

    def is_game_ended(self):
        # exceeded the maximum moevs
        self.num_moves = read_moves()

        if self.num_moves >= self.max_moves or (self.op_passed_move and self.me_passed_move):
            return True
        return False

    # put a stone on self board
    def place_stone(self, row, col):
        # place a stone
        self.current_board[row][col] = self.side

        # #check if the move create capture reward
        # if self.capture_reward != 0:
        #     reward = self.capture_reward
        #     self.capture_reward = 0
        #     return reward

    def create_next_state(self, side, row, col):
        # make a copy of current board
        test_board = deepcopy(self)
        # set the previous board
        test_board.previous_board = test_board.current_board
        # make a move
        test_board.current_board[row][col] = side
        # remove opponent's dead pieces
        test_board.remove_dead_pieces(3 - side)
        # change the next state to opponent's side
        test_board.side = 3 - side

        return test_board

    def find_neighbors(self, row, col):
        neighbors = []
        if row > 0:
            neighbors.append((row - 1, col))
        if col > 0:
            neighbors.append((row, col - 1))
        if row < boardSize - 1:
            neighbors.append((row + 1, col))
        if col < boardSize - 1:
            neighbors.append((row, col + 1))
        return neighbors

    def all_allies(self, row, col):
        # a queue for dfs
        dfs_stack = [(row, col)]
        allies = []
        while dfs_stack:
            ally = dfs_stack.pop()
            allies.append(ally)
            neighbor_allies = self.get_neighbor_ally(ally[0], ally[1])
            for neighbor_allay in neighbor_allies:
                if neighbor_allay not in allies and neighbor_allay not in dfs_stack:
                    dfs_stack.append(neighbor_allay)
        return allies

    def get_neighbor_ally(self, row, col):

        board = self.current_board
        neighbors = self.find_neighbors(row, col)
        neighbor_allies = []
        # Iterate through neighbors
        for piece in neighbors:
            # Add to allies list if having the same color
            if board[piece[0]][piece[1]] == board[row][col]:
                neighbor_allies.append(piece)
        return neighbor_allies

    # check if the move is valid
    def is_valid_place(self, row, col):
        if not self.isOccupied(row, col) or not self.isInBound(row, col):
            return False

        test = deepcopy(self)
        test.current_board[row][col] = test.side
        # check if is an eye
        # if self.is_an_eye(row,col):
        #     return False

        if test.has_liberty(row, col):
            return True

        test.remove_dead_pieces(3 - test.side)
        if not test.has_liberty(row, col):
            return False
        else:
            # check ko rule
            violate = True
            for row in range(boardSize):
                for col in range(boardSize):
                    if test.current_board[row][col] != test.previous_board[row][col]:
                        violate = False
            if violate:
                return False
        return True

    def legal_moves(self):
        moves = []
        for row in range(self.size):
            for col in range(self.size):
                if (self.is_valid_place(row, col)):
                    point = (row, col)
                    moves.append(point)
        return moves

    def isOccupied(self, row, col):
        return self.current_board[row][col] == blank_space

    def isInBound(self, row, col):
        return row < boardSize and col < boardSize and row >= 0 and col >= 0

    def is_acquired_position(self, row, col, side):

        neighbors = self.find_neighbors(row, col)
        for neighbor in neighbors:
            if self.current_board[neighbor[0]][neighbor[1]] != side:
                return False
        return True

    def is_an_eye(self, row, col):
        if not self.isInBound(row, col) or self.isOccupied(row, col):
            return False
        # 检测周围的棋子都是己方棋子
        neighbors = self.find_neighbors(row, col)
        for neighbor in neighbors:
            if self.current_board[neighbor[0]][neighbor[1]] != self.side:
                return False

        # 得到4个角的坐标
        corners = [(row - 1, col - 1), (row + 1, col + 1), (row - 1, col + 1), (row + 1, col - 1)]
        friend_corners = 0
        out_of_board_corners = 0

        # 检测四个角的棋子至少有三个是己方棋子
        for point in corners:
            if self.isInBound(point[0], point[1]):
                if self.current_board[point[0]][point[1]] == self.side:
                    friend_corners += 1
            else:
                out_of_board_corners += 1
        if out_of_board_corners > 0:
            if friend_corners + out_of_board_corners == 4:
                return True
        return friend_corners >= 3

    def has_liberty(self, row, col):
        flag = False
        allies = self.all_allies(row, col)
        for ally in allies:
            neighbors = self.find_neighbors(ally[0], ally[1])
            for neighbor in neighbors:
                if self.current_board[neighbor[0]][neighbor[1]] == blank_space:
                    return True
        return False

    def string_liberty_count(self, row, col):
        count = 0
        flag = False
        counted = []
        allies = self.all_allies(row, col)
        for ally in allies:
            neighbors = self.find_neighbors(ally[0], ally[1])
            for neighbor in neighbors:
                if self.current_board[neighbor[0]][neighbor[1]] == blank_space and neighbor not in counted:
                    count += 1
                    counted.append(neighbor)
        return count

    def is_cornor(self, row, col):
        if row == 0 and col == 0:
            return True
        if row == 0 and col == 4:
            return True
        if row == 4 and col == 0:
            return True
        if row == 4 and col == 4:
            return True
        return False

    @set_timeout(9, callback)  # 限时 9 秒超时
    def alpha_beta_search(self, state, max_depth, branching_factor, current_move):

        path = fpath + "cresult.txt"
        f = open(path, "a+")
        ans_move = None
        move_dic = dict()
        best_score = np.inf
        possible_moves = state.legal_moves()
        print("possible moves {}".format(possible_moves))
        alpha = MIN
        beta = MAX
        value = MIN

        self_killing_move = []

        max_kill = 0
        one_kill_move = None

        # count how many deads we will have
        max_dead = 0
        saving_move = None
        if current_move == 0:
            return 2, 2
        if current_move <= branching_factor:
            while True:
                point = random.choice(possible_moves)
                if boardSize - 1 > point[0] > 0 < point[1] < boardSize - 1:
                    print("-------------this move is made by random----------------")
                    return point[0], point[1]

        for move in possible_moves:

            # 首先计算这步如果被敌人下会杀掉我方多少，如果发现这步敌人下了我方死一大片，则返回
            op_view = deepcopy(state)
            op_view.current_board[move[0]][move[1]] = 3 - state.side
            dead_num = len(op_view.get_dead_pieces(state.side))

            if dead_num > max_dead:
                print("find one_step saving move {}".format(move))
                print("find one_step saving move {}".format(move), file=f)
                max_dead = dead_num
                saving_move = move
            if max_dead >= 2:
                print("find big saving move {}".format(move))
                print("find big saving move {}".format(move), file=f)
                return saving_move

            next_state = deepcopy(state)
            next_state.previous_board = state.current_board

            # make a move
            next_state.place_stone(move[0], move[1])

            op_deads = next_state.get_dead_pieces(3 - state.side)
            max_kill = len(op_deads)

            # if max killing number bigger than 2 then just return the move
            if max_kill >= 2:
                print("find big killing move {}".format(move))
                print("find big killing move {}".format(move), file=f)
                # print("-------------this move is made by greedy----------------")
                return move

            # if only one dead piece found save it for later use
            if max_kill == 1:
                print("find one step killing move {}".format(move), file=f)
                one_kill_move = move

            liberty_count = next_state.string_liberty_count(move[0], move[1])
            # neighbors = next_state.get_neighbor_ally(move[0],move[1])
            # neighbor_num = len(neighbors)
            if liberty_count == 1 and max_kill == 0:
                print("move {} is a self-killing move".format(move))
                print("move {} is a self-killing move".format(move), file=f)
                self_killing_move.append(move)
                continue

            next_state.remove_dead_pieces(3 - state.side)
            next_state.side = 3 - state.side

            # run minmax
            value = Min_value(next_state, alpha, beta, max_depth, evaluation, 0)
            move_dic.setdefault(value, []).append(move)

            # print("current move in ab search {} value {}".format(move,value))
            # print("current dic {} ".format(move_dic))
            print("current move in ab search {} value {}".format(move, value), file=f)

            if best_score >= value:
                best_score = value
            else:
                alpha = max(alpha, value)
            # print("best_score{},move{}".format(best_score, move))
        # print("current dic {} ".format(move_dic),file=f)

        print("-------------this move is made by alpha_beta----------------")
        print("-------------this move is made by alpha_beta----------------", file=f)
        # 能杀则杀
        if one_kill_move:
            if one_kill_move in move_dic[best_score] or current_move >= 8:
                print("do one kill move")
                print("do one kill move", file=f)
                f.close()
                return one_kill_move
        if saving_move:
            if saving_move not in self_killing_move:
                if saving_move in move_dic[best_score] or current_move >= 8:
                    print("do one saving move")
                    print("do one saving move", file=f)
                    f.close()
                    return saving_move
        f.close()
        if best_score == np.inf:
            if self_killing_move:
                if current_move == 11:
                    return random.choice(self_killing_move)
                else:
                    return (-1, -1)
        # 如果是已经占领的位置则没必要优先选择
        elif len(move_dic[best_score]) > 1:
            # 去掉所有的已经被我方棋子占领的位置，得到一个list
            ans_list = [best_move for best_move in move_dic[best_score] if
                        not state.is_acquired_position(best_move[0], best_move[1], state.side)]
            # 如果这个list存在则返回这个list中随机的一个位置
            if ans_list:
                # print("ans_list is{}".format(ans_list))
                if len(ans_list) > 1:
                    # 去掉所有是角落的位置
                    new_list = [best_move for best_move in ans_list if not state.is_cornor(best_move[0], best_move[1])]
                    if new_list:
                        # print("new_list is{}".format(new_list))
                        return random.choice(new_list)
                return random.choice(ans_list)
        return random.choice(move_dic[best_score])


def Min_value(state, a, b, max_depth, eva_function, layer):
    possible_moves = state.legal_moves()
    # if read_moves() + layer >= state.max_moves or len(possible_moves)==0 or max_depth==0:
    #     return eva_function(state)

    if read_moves() + layer >= state.max_moves or len(possible_moves) == 0:
        result = state.check_game_status()
        black_s, white_s = state.black_white_score()
        if result == WIN:
            return abs(black_s - white_s) + state.komi
        elif result == LOSE:
            return -abs(black_s - white_s) - state.komi
        elif result == DRAW:
            return 0

    elif max_depth == 0:
        result = eva_function(state)
        return result

    value = MAX

    for move in possible_moves:
        next_state = state.create_next_state(state.side, move[0], move[1])
        value = min(value, Max_value(next_state, a, b, max_depth - 1, eva_function, layer + 1))
        if value <= a:
            return value
        b = min(b, value)
    return value


def Max_value(state, a, b, max_depth, eva_function, layer):
    possible_moves = state.legal_moves()
    # if read_moves() + layer >= state.max_moves or len(possible_moves)==0 or max_depth==0:
    #     return eva_function(state)
    if read_moves() + layer >= state.max_moves or len(possible_moves) == 0:
        result = state.check_game_status()
        black_s, white_s = state.black_white_score()
        if result == WIN:
            return abs(black_s - white_s) + state.komi
        elif result == LOSE:
            return -abs(black_s - white_s) - state.komi
        elif result == DRAW:
            return 0

    elif max_depth == 0:
        result = eva_function(state)
        return result

    value = MIN

    for move in possible_moves:
        next_state = state.create_next_state(state.side, move[0], move[1])
        value = max(value, Min_value(next_state, a, b, max_depth - 1, eva_function, layer + 1))
        if value >= b:
            return value
        a = max(a, value)
    return value


def evaluation(state):
    black_liberty = 0
    white_liberty = 0

    black_num = 0
    white_num = 0

    black_acquired = 0
    white_acquired = 0

    black_pos = set()
    white_pos = set()
    blank_pos = set()
    for r in range(boardSize):
        for c in range(boardSize):
            if state.current_board[r][c] == white:
                white_num += 1
                white_pos.add((r, c))

            elif state.current_board[r][c] == black:
                black_num += 1
                black_pos.add((r, c))
            else:
                blank_pos.add((r, c))
                if state.is_acquired_position(r, c, black):
                    black_acquired += 1
                if state.is_acquired_position(r, c, white):
                    white_acquired += 1

    # 计算空白格属于什么棋子的liberty
    for blank_chess in blank_pos:
        blank_neighbors = state.find_neighbors(blank_chess[0], blank_chess[1])
        for neighbor in blank_neighbors:
            in_black_flag = False
            in_white_flag = False
            common_flag = False
            if neighbor in black_pos and neighbor not in white_pos:
                black_liberty += 1
                in_black_flag = True
            if neighbor in white_pos and neighbor not in black_pos:
                white_liberty += 1
                in_white_flag = True
            if neighbor in white_pos and neighbor in black_pos:
                black_liberty -= 0.5
                white_liberty -= 0.5
                common_flag = True
            if in_black_flag or in_white_flag or common_flag:
                break

    black_score = black_num + black_liberty * 0.12 + black_acquired * 0.5  # - 0.8 * black_eyes
    white_score = white_num + white_liberty * 0.12 + white_acquired * 0.5  # - 0.8 * white_eyes

    diff = black_score - white_score
    if state.side == black:
        return diff
    return -1 * diff


class Alpha_beta_player:
    def __init__(self, board=None, side=None):
        self.board = board
        self.side = side

    def make_one_move(self, row, col):
        if row == col == -1:
            self.board.set_passed_step(self.side)
            return "PASS"
        else:
            self.board.place_stone(row, col)
            # check if has dead_piece and update the board
            self.board.update_game_state()
            return row, col

    def get_best_move(self):

        legal_moves = self.board.legal_moves()

        # 如果没有legal move就返回pass
        if not legal_moves:
            return -1, -1

        current_move = read_moves()
        # set different depth factor by the current move count
        depth_factor = 0
        if current_move <= 7:
            depth_factor = 2
        elif current_move >= 8:
            depth_factor = 2

        # calculate the time once the time is higher than 9 second run a greedy algorithm to choose move kills most opponents
        start = time.time()
        branch_factor = 4
        # alpha-beta search
        point = self.board.alpha_beta_search(self.board, depth_factor, branch_factor, current_move)
        end = time.time()
        print("time cost is {}".format(end - start))

        if point == None:
            max_kill = 0
            kill_step = None
            for move in legal_moves:
                next_state = deepcopy(self.board)
                next_state.place_stone(move[0], move[1])
                op_deads = next_state.get_dead_pieces(3 - self.board.side)
                if len(op_deads) > max_kill:
                    max_kill = len(op_deads)
                    kill_step = move
            if kill_step:
                return kill_step
            else:
                return random.choice(legal_moves)

        return point[0], point[1]

    def play(self):

        path = fpath + "cresult.txt"
        f = open(path, "a+")

        # check if the game is on the first step
        if self.board.is_start_of_game():
            write_moves("0")
            row, col = self.get_best_move()
            action = self.make_one_move(row, col)
            # update the current moves number of our side
            increase_move()
            print("current_moves: {}".format(self.board.num_moves))
        else:  # the game is not the first step
            # if the same board then the op is passed
            if self.board.is_same_board():
                self.board.op_passed_move = True

            # get the best move
            action = self.get_best_move()
            # if the action is pass then pass and increase move count by 1
            if action[0] == -1 and action[1] == -1:
                self.board.set_passed_step(self.side)
                increase_move()
                # set the num_moves since pass also count
                self.board.num_moves = read_moves()
                action = "PASS"

                # check if game is ended
                if self.board.is_game_ended():
                    result = self.board.check_game_status()
                    # print("predicted result: {}".format(result))
            else:
                # make a move and increased the move count
                action = self.make_one_move(action[0], action[1])
                increase_move()
                print("total_moves: {} this move {}".format(self.board.num_moves, (action[0], action[1])))
                print("total_moves: {} this move {}".format(self.board.num_moves, (action[0], action[1])), file=f)

                # check if game is ended after the move,train if game is ended
                if self.board.is_game_ended():
                    result = self.board.check_game_status()
                    print("predicted result: {}".format(result))

        return action


if __name__ == "__main__":
    # initialize the board
    side, last_board, current_board = readInput()
    board = Board(boardSize)
    board.set_board(side, last_board, current_board)
    # create a player
    player = Alpha_beta_player(board, side)
    action = player.play()
    # output the move
    writeOutput(action)