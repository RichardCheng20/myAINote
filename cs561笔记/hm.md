# Linux 

#### 复制文件

![image-20210913075919399](hm.assets/image-20210913075919399.png)

#### 跑python

`python3 homework3.py`

`diff -u output.txt output5.txt` 



cp resource/asnlib/public/myplayer_play/random_player.py work

设置断点调试

```python
import pdb
pdb.set_trace() #添加断点
n到下一个语句
s进入函数
c继续执行
q退出pdb 
```

```python
b
b lineno
b filename:lineno 
b functionname
filename文件名，断点添加到哪个文件，如test.py
lineno断点添加到哪一行nn
function：函数名，在该函数执行的第一行设置断点

cl
cl filename:lineno
cl bpnumber [bpnumber ...]
bpnumber 断点序号（多个以空格分隔）

p expression # expression Python表达式



c 持续执行下去，直到遇到一个断点
unt lineno 持续执行直到运行到指定行（或遇到断点）

```

# General AI

1. heuristic for the given graph **admissible?**  如果预测的比真实cost还要大那就不admissible

   NO.  Actual cost for node E is 1, but heuristic cost is 3 which is overestimated

<img src="hm.assets/image-20210928183628869.png" alt="image-20210928183628869" style="zoom:50%;" />

2. heuristic for the given graph **consistent**?如果当前结点J加上自己预测的cost比自己父节点预测还要小,说明不行

NO. Heuristic cost for node F is 4, heuristic cost for node J is 2, actual cost from F to J is 1. Triangle inequality is not satisfied.

9. A* graph search is optimal when the heuristic is consistent. An addimissible heuristic is need to guarantee an opt solution. 如果不admissible那么就不能保证opt!!! 但是也是有可能的. Inadmissible不会改变completeness但是会改变optimality

<img src="hm.assets/image-20210929081800104.png" alt="image-20210929081800104" style="zoom:50%;" />

<img src="hm.assets/image-20210929084525887.png" alt="image-20210929084525887" style="zoom:50%;" />

9. A genetic algorithm with a population of 1 is equivalent to a random walk. 
10. BFS is optimal if the path cost is a **nondecreasing function** of the depth of the node

![image-20210928180530423](hm.assets/image-20210928180530423.png)





# Problem formulation 

## millennial to apt 

A millennial (M), apartment (A) to a selfie-themed party (P).  has three things, a cat (C), a hamster (H), and a bag of organic kale (K)

- Give the initial and goal **states**

The initial state {M, C, H, K}. goal state: {} 

-  all the legal states

{M,C,H,K} , {M,C,H} {C,K} {M,H,K} {M,C,K} {H} {C} {M,H} {K}{}

- action 

Move one thing (or nothing) to the other side. 

- The problem can be represented as a graph which contains the **states as nodes**, and the state **transitions as edges**

![image-20210928133749562](hm.assets/image-20210928133749562.png)

- Provide one sequence of actions that solves this problem with the fewest trips by M. 

<img src="hm.assets/image-20210928133837588.png" alt="image-20210928133837588" style="zoom:25%;" />

In a **deterministic enviroment** any action has a single guranteed effect, and no failure or uncertainty. **In a non-deterministic environment**, the same task performed twice may produce different results or may even fail completely. Thus, robot picking parts is a stochastic environment. 

In a **episodic environment**, each agent's performance is the result of a series of independent tasks performed. There is no link between the agent's performance and other different scenarios. In other words, the agent decides which action is best to take, it will only <u>consider the task at hand and doesn't have to consider the effect it may have on future tasks.</u> 

# spacecraft  

1. 飞机只能带一个
2. AB 有导航
3. 如果对角线ac要同步必须有b或者d的帮助

<img src="hm.assets/image-20210928181509035.png" alt="image-20210928181509035" style="zoom:25%;" />

1. Write down the initial and goal states.  
   Initial state: {A=E, B=E, C=E, D=E} 

   Goal state: {A=M, B=M, C=M, D=M}

或者 Initial state: E = {ABCD}, S = { }, M = { }, Goal state: E = { }, S = { }, M = {ABCD}

2. For each restriction (1, 2, and 3 in the list above), write down two **illegal states** that violate it (6 illegal states in total).
   - 三个人在飞机上(S, S, S, E) , (S, S, M, S)
   - ab不在飞机  (E, E, S, S),  (E, E, E, S) 
   - a b d 不在同一个地方 (S, E, S, M), (E, S, E, M)
3.  action(s) you can use to solve this problem. 

Move one or two robots from one place to another place. 

4. Provide a possible sequence of actions that solve this problem. Provide the corresponding sequence of state transitions resulting from your answer to the previous question (Q3.5).

<img src="hm.assets/image-20210928182818181.png" alt="image-20210928182818181" style="zoom:50%;" />







# CSP

先选取minimum remaining value

## 1 pacman 

![image-20210928173108478](hm.assets/image-20210928173108478.png)

根据风来判断出口,要求出口不相邻

1.  State the **binary** and **unary constraints** for this CSP

<img src="hm.assets/image-20210928173304392.png" alt="image-20210928173304392" style="zoom:50%;" />

2. Cross out the values from the domains of the variables that will be deleted in enforcing both node and arc consistency.

<img src="hm.assets/image-20210928173713867.png" alt="image-20210928173713867" style="zoom:50%;" />

3. [xx%] According to MRV (Minimum Remaining Values), which variable(s) could the **solver assign first?**
X1 or X5



## 2 price lunar year party

<img src="hm.assets/image-20210928201041895.png" alt="image-20210928201041895" style="zoom:50%;" />

with the price on the tag coming from the more expensive of the two food compartments it is placed between. 

1. [2%] Write down the variables and their domains in this CSP.

   Variables: x1, x2, x3, x4, x5, x6

   Domains {A, B, C, D}

2. constraints

<img src="hm.assets/image-20210928230723210.png" alt="image-20210928230723210" style="zoom:50%;" />

<img src="hm.assets/image-20210928230754423.png" alt="image-20210928230754423" style="zoom:50%;" />





# problem solving 

## three black and three white

1. size of the state space

7! /(3! 3!) = 140.

2. number of successors

Max: six; Min: three; Branching factor: (3+4+5+6+5+4+3)/7 or ~ 4.3 or 30/7

3. heuristic: = the number of tiles that would have to be moved (by any number of spaces) for a state “s” to become a goal state.

   h(BBXBWWW) = 5, because every piece but the rightmost black one must move to make a goal state. 

   h(BBBXWWW) = 6, the other two equal to 5.

4. Is this heuristic admissible?

Yes, because the heuristic is less than or equal to the cost.











```python
import os
import random
import signal
import sys
from copy import deepcopy
from datetime import time

from read import readInput
from write import writeOutput


MIN = -10000
MAX = 10000

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

def save_log(time_cost):
    if os.path.exists("./timeCost.txt"):
        append_write = 'a'  # append if already exists
    else:
        append_write = 'w'  # make a new file if no
    with open("./timeCost.txt", append_write) as f:
        f.write(time_cost + "\n")

class myBoard:
    def __init__(self, n):
        self.size = n
        # self.previous_board = None # Store the previous board
        self.X_move = True  # X chess plays first
        self.died_pieces = []  # Intialize died pieces to be empty
        self.n_move = 0  # Trace the number of moves
        self.max_move = n * n - 1  # The max movement of a Go game


    def set_board(self, piece_type, previous_board, board):
        for i in range(self.size):
            for j in range(self.size):
                if previous_board[i][j] == piece_type and board[i][j] != piece_type:
                    self.died_pieces.append((i, j))

        # self.piece_type = piece_type
        self.previous_board = previous_board
        self.board = board


    def compare_board(self, board1, board2):
        for i in range(self.size):
            for j in range(self.size):
                if board1[i][j] != board2[i][j]:
                    return False
        return True


    def copy_board(self):
        return deepcopy(self)


    def detect_neighbor(self, i, j):
        board = self.board
        neighbors = []
        # Detect borders and add neighbor coordinates
        if i > 0: neighbors.append((i - 1, j))
        if i < len(board) - 1: neighbors.append((i + 1, j))
        if j > 0: neighbors.append((i, j - 1))
        if j < len(board) - 1: neighbors.append((i, j + 1))
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


    def remove_died_pieces(self, piece_type):
        died_pieces = self.find_died_pieces(piece_type)
        if not died_pieces: return []
        self.remove_certain_pieces(died_pieces)
        return died_pieces


    def remove_certain_pieces(self, positions):
        board = self.board
        for piece in positions:
            board[piece[0]][piece[1]] = 0
        self.update_board(board)


    def place_chess(self, i, j, piece_type):
        board = self.board

        valid_place = self.valid_place_check(i, j, piece_type)
        if not valid_place:
            return False
        self.previous_board = deepcopy(board)
        board[i][j] = piece_type
        self.update_board(board)
        # Remove the following line for HW2 CS561 S2020
        # self.n_move += 1
        return True


    def valid_place_check(self, i, j, piece_type):
        board = self.board
        # Check if the place is in the board range
        if not (i >= 0 and i < len(board)):
            return False
        if not (j >= 0 and j < len(board)):
            return False

        # Check if the place already has a piece
        if board[i][j] != 0:
            return False

        # Copy the board for testing
        test_go = self.copy_board()
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
            if self.died_pieces and self.compare_board(self.previous_board, test_go.board):
                return False
        return True


    def update_board(self, new_board):
        self.board = new_board


    def game_end(self, piece_type, action="MOVE"):
        # Case 1: max move reached
        if self.n_move >= self.max_move:
            return True
        # Case 2: two players all pass the move.
        if self.compare_board(self.previous_board, self.board) and action == "PASS":
            return True
        return False


class myPlayer:
    def __init__(self, my_board = None, piece_type = None):
        self.my_board = my_board
        self.piece_type = piece_type
        self.search_depth = 3
        self.moveCount = 0

    def move(self):
        if self.moveCount <= 4:
            good_places = [(2, 2), (1, 2), (3, 2), (2, 1), (2, 3), (1, 1), (1, 3), (3, 1), (3, 3)]
            for place in good_places:
                if self.myBoard.valid_place_check(place[0], place[1], self.side):
                    action = place
                    log_str = "Move count " + str(self.moveCount) + "  Move: " + str(action) + "   "
                    self.moveCount += 1
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
            action = random.choice(self.myBoard.valid_places())

        log_str += ("Move: " + str(action) + "    " + "time cost is {}".format(end - start))
        save_log(log_str)
        # print("Move")
        # print(action)
        # print("time cost is {}".format(end - start))
        self.moveCount += 1
        return action

    @set_timeout(8, after_timeout)
    def mini_max_search_with_Alpha_Beta(self):
        if not self.myBoard.valid_places():
            print("no valid places:PASS")
            return "PASS"

        # return Max of mini_value
        values = []
        for move in self.myBoard.valid_places():
            values.append(self.mini_value(MIN, MAX, (move[0], move[1]), self.moveCount, self.myBoard, 0))
        move_index = values.index(max(values))
        return self.myBoard.valid_places()[move_index]

    def mini_value(self, alpha, beta, action, moveCount, last_board_manage, depth):
        # check if end
        if self.check_if_end(depth, last_board_manage.last_board, last_board_manage.board, action, moveCount):
            return self.heuristic_evaluate(last_board_manage)

        # current state board
        myBoard = last_board_manage.copy_board_manage()
        myBoard.side = 3 - last_board_manage.side
        myBoard.last_board = copy_board(myBoard.board)
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




if __name__ == "__main__":
    N = 5
    piece_type, previous_board, board = readInput(N)
    my_board = myBoard(N)
    my_board.set_board(piece_type, previous_board, board)
    player = myPlayer(my_board, piece_type)
    action = player.move()
    writeOutput(action)
```

