#!/usr/bin/env python3
"""
Tic-Tac-Toe AI with Minimax Algorithm and Alpha-Beta Pruning
A minimal, unbeatable AI implementation
"""

class TicTacToeAI:
    def __init__(self):
        self.board = [' '] * 9  # 3x3 board represented as 1D list
        self.human = 'X'
        self.ai = 'O'
    
    def print_board(self):
        """Display the current board state"""
        print("\n Current Board:")
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("-----------")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("-----------")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} ")
        print("\n Positions (1-9):")
        print(" 1 | 2 | 3 ")
        print("-----------")
        print(" 4 | 5 | 6 ")
        print("-----------")
        print(" 7 | 8 | 9 ")
        print()
    
    def is_winner(self, board, player):
        """Check if a player has won"""
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        return any(all(board[i] == player for i in combo) for combo in winning_combinations)
    
    def is_board_full(self, board):
        """Check if the board is full"""
        return ' ' not in board
    
    def get_available_moves(self, board):
        """Get list of available positions"""
        return [i for i, spot in enumerate(board) if spot == ' ']
    
    def minimax(self, board, depth, is_maximizing, alpha, beta):
        """
        Minimax algorithm with Alpha-Beta pruning
        Returns the best score for the current position
        """
        # Terminal states
        if self.is_winner(board, self.ai):
            return 10 - depth  # Prefer faster wins
        if self.is_winner(board, self.human):
            return depth - 10  # Prefer slower losses
        if self.is_board_full(board):
            return 0  # Draw
        
        if is_maximizing:  # AI's turn (maximize)
            max_eval = float('-inf')
            for move in self.get_available_moves(board):
                board[move] = self.ai
                eval_score = self.minimax(board, depth + 1, False, alpha, beta)
                board[move] = ' '  # Undo move
                max_eval = max(max_eval, eval_score)
                alpha = max(alpha, eval_score)
                if beta <= alpha:  # Alpha-Beta pruning
                    break
            return max_eval
        else:  # Human's turn (minimize)
            min_eval = float('inf')
            for move in self.get_available_moves(board):
                board[move] = self.human
                eval_score = self.minimax(board, depth + 1, True, alpha, beta)
                board[move] = ' '  # Undo move
                min_eval = min(min_eval, eval_score)
                beta = min(beta, eval_score)
                if beta <= alpha:  # Alpha-Beta pruning
                    break
            return min_eval
    
    def get_best_move(self):
        """Find the best move for AI using Minimax"""
        best_score = float('-inf')
        best_move = -1
        
        # Position preferences for tie-breaking (center > corners > edges)
        position_values = [3, 2, 3, 2, 5, 2, 3, 2, 3]  # Center=5, Corners=3, Edges=2
        
        for move in self.get_available_moves(self.board):
            self.board[move] = self.ai
            score = self.minimax(self.board, 0, False, float('-inf'), float('inf'))
            self.board[move] = ' '  # Undo move
            
            # Add small position preference for tie-breaking
            adjusted_score = score + position_values[move] * 0.01
            
            if adjusted_score > best_score:
                best_score = adjusted_score
                best_move = move
        
        return best_move
    
    def make_human_move(self):
        """Handle human player's move"""
        while True:
            try:
                position = int(input("Enter your move (1-9): ")) - 1
                if 0 <= position <= 8 and self.board[position] == ' ':
                    self.board[position] = self.human
                    break
                else:
                    print("Invalid move! Choose an empty position (1-9).")
            except ValueError:
                print("Please enter a valid number (1-9).")
    
    def make_ai_move(self):
        """Handle AI player's move"""
        print("AI is thinking...")
        move = self.get_best_move()
        self.board[move] = self.ai
        print(f"AI chooses position {move + 1}")
    
    def check_game_over(self):
        """Check if game is over and return winner"""
        if self.is_winner(self.board, self.human):
            return 'human'
        elif self.is_winner(self.board, self.ai):
            return 'ai'
        elif self.is_board_full(self.board):
            return 'draw'
        return None
    
    def play_game(self):
        """Main game loop"""
        print("=== TIC-TAC-TOE AI ===")
        print("You are X, AI is O")
        print("The AI uses Minimax with Alpha-Beta pruning - it's unbeatable!")
        
        # Ask who goes first
        while True:
            first = input("\nWho goes first? (h)uman or (a)i: ").lower()
            if first in ['h', 'human']:
                human_first = True
                break
            elif first in ['a', 'ai']:
                human_first = False
                break
            else:
                print("Please enter 'h' for human or 'a' for AI")
        
        current_player = 'human' if human_first else 'ai'
        
        while True:
            self.print_board()
            
            # Make move based on current player
            if current_player == 'human':
                self.make_human_move()
                current_player = 'ai'
            else:
                self.make_ai_move()
                current_player = 'human'
            
            # Check game over
            result = self.check_game_over()
            if result:
                self.print_board()
                if result == 'human':
                    print("Congratulations! You won! (This shouldn't happen if AI is working correctly)")
                elif result == 'ai':
                    print("AI wins! Better luck next time!")
                else:
                    print("It's a draw!")
                break
        
        # Ask to play again
        if input("\nPlay again? (y/n): ").lower().startswith('y'):
            self.__init__()  # Reset game
            self.play_game()

def main():
    """Entry point of the program"""
    game = TicTacToeAI()
    game.play_game()

if __name__ == "__main__":
    main()
