class AlphaBetaPruning:
    def __init__(self, depth, game_state, player):
        # Initialize depth, game state, and player ('X' for maximizer, 'O' for minimizer)
        self.depth = depth
        self.game_state = game_state
        self.player = player  # 'X' for maximizer, 'O' for minimizer

    def is_terminal(self, state):
        # Check if the game has reached a terminal state (win, lose, or draw)
        # Winning combinations (rows, columns, diagonals)
        win_conditions = [
            [state[0], state[1], state[2]],
            [state[3], state[4], state[5]],
            [state[6], state[7], state[8]],
            [state[0], state[3], state[6]],
            [state[1], state[4], state[7]],
            [state[2], state[5], state[8]],
            [state[0], state[4], state[8]],
            [state[2], state[4], state[6]],
        ]
        
        # Check if any player has won
        if ['X', 'X', 'X'] in win_conditions:
            return True  # Maximizer wins
        if ['O', 'O', 'O'] in win_conditions:
            return True  # Minimizer wins
        if '-' not in state:
            return True  # Draw
        
        return False

    def utility(self, state):
        # Return +1 if 'X' wins, -1 if 'O' wins, 0 for a draw
        win_conditions = [
            [state[0], state[1], state[2]],
            [state[3], state[4], state[5]],
            [state[6], state[7], state[8]],
            [state[0], state[3], state[6]],
            [state[1], state[4], state[7]],
            [state[2], state[5], state[8]],
            [state[0], state[4], state[8]],
            [state[2], state[4], state[6]],
        ]
        
        if ['X', 'X', 'X'] in win_conditions:
            return 1  # Maximizer wins
        elif ['O', 'O', 'O'] in win_conditions:
            return -1  # Minimizer wins
        else:
            return 0  # Draw

    def alphabeta(self, state, depth, alpha, beta, maximizing_player):
        if depth == 0 or self.is_terminal(state):
            return self.utility(state)
        
        if maximizing_player:
            max_eval = float('-inf')
            for child in self.get_children(state, 'X'):
                eval = self.alphabeta(child, depth - 1, alpha, beta, False)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break  # Beta cut-off
            return max_eval
        else:
            min_eval = float('inf')
            for child in self.get_children(state, 'O'):
                eval = self.alphabeta(child, depth - 1, alpha, beta, True)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break  # Alpha cut-off
            return min_eval

    def best_move(self, state):
        # Determine the best move for the current player (AI's turn)
        best_val = float('-inf')
        move = None
        for child in self.get_children(state, 'X'):
            eval = self.alphabeta(child, self.depth - 1, float('-inf'), float('inf'), False)
            if eval > best_val:
                best_val = eval
                move = child
        return move

    def get_children(self, state, player):
        # Generate all possible game states from the current state by making a move
        children = []
        for i in range(len(state)):
            if state[i] == '-':
                new_state = state[:]
                new_state[i] = player
                children.append(new_state)
        return children

# Utility functions to play the game
def print_board(state):
    # Print the Tic-Tac-Toe board
    board = [state[i:i+3] for i in range(0, len(state), 3)]
    for row in board:
        print(' | '.join(row))
        print('---------')

def is_winner(state, player):
    # Check if the given player has won
    win_conditions = [
        [state[0], state[1], state[2]],
        [state[3], state[4], state[5]],
        [state[6], state[7], state[8]],
        [state[0], state[3], state[6]],
        [state[1], state[4], state[7]],
        [state[2], state[5], state[8]],
        [state[0], state[4], state[8]],
        [state[2], state[4], state[6]],
    ]
    return [player, player, player] in win_conditions

def main():
    game_state = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
    print("Initial Board:")
    print_board(game_state)
    
    game = AlphaBetaPruning(9, game_state, 'X')
    while '-' in game_state:
        print("Your Turn! Enter position (1-9):")
        player_move = int(input()) - 1
        if game_state[player_move] == '-':
            game_state[player_move] = 'O'
            if is_winner(game_state, 'O'):
                print("You win!")
                break
        else:
            print("Invalid move. Try again.")
            continue
        
        if '-' not in game_state:
            print("It's a draw!")
            break
        
        # AI's turn
        print("AI is making a move...")
        game_state = game.best_move(game_state)
        print_board(game_state)
        
        if is_winner(game_state, 'X'):
            print("AI wins!")
            break


main()
