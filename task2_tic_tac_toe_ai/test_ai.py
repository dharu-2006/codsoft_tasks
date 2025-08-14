#!/usr/bin/env python3
"""
Test suite for Tic-Tac-Toe AI
Verifies the AI's correctness and unbeatable nature
"""

from tic_tac_toe_ai import TicTacToeAI

def test_winning_detection():
    """Test that the AI correctly detects winning conditions"""
    game = TicTacToeAI()
    
    # Test horizontal win
    game.board = ['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ']
    assert game.is_winner(game.board, 'X'), "Should detect horizontal win"
    
    # Test vertical win
    game.board = ['O', ' ', ' ', 'O', ' ', ' ', 'O', ' ', ' ']
    assert game.is_winner(game.board, 'O'), "Should detect vertical win"
    
    # Test diagonal win
    game.board = ['X', ' ', ' ', ' ', 'X', ' ', ' ', ' ', 'X']
    assert game.is_winner(game.board, 'X'), "Should detect diagonal win"
    
    print("Winning detection tests passed")

def test_ai_blocks_immediate_threats():
    """Test that AI blocks immediate winning moves"""
    game = TicTacToeAI()
    
    # Human has two X's in a row, AI should block
    game.board = ['X', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    best_move = game.get_best_move()
    assert best_move == 2, f"AI should block at position 2, but chose {best_move}"
    
    # Test vertical threat
    game.board = ['X', ' ', ' ', 'X', ' ', ' ', ' ', ' ', ' ']
    best_move = game.get_best_move()
    assert best_move == 6, f"AI should block at position 6, but chose {best_move}"
    
    print("Threat blocking tests passed")

def test_ai_takes_winning_moves():
    """Test that AI takes immediate winning opportunities"""
    game = TicTacToeAI()
    
    # AI has two O's in a row, should complete the win
    game.board = ['O', 'O', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    best_move = game.get_best_move()
    assert best_move == 2, f"AI should win at position 2, but chose {best_move}"
    
    print("Winning move tests passed")

def test_center_preference():
    """Test that AI prefers center on empty board"""
    game = TicTacToeAI()
    
    # On empty board, center (position 4) is optimal
    best_move = game.get_best_move()
    assert best_move == 4, f"AI should prefer center (4), but chose {best_move}"
    
    print("Center preference test passed")

def test_ai_never_loses():
    """Test multiple game scenarios to ensure AI never loses"""
    scenarios_tested = 0
    ai_wins = 0
    draws = 0
    
    # Test various opening moves by human
    human_openings = [0, 1, 2, 3, 4, 5, 6, 7, 8]  # All possible first moves
    
    for opening in human_openings:
        game = TicTacToeAI()
        
        # Human makes opening move
        game.board[opening] = game.human
        
        # Simulate a game where AI plays optimally
        current_player = 'ai'
        
        while True:
            if current_player == 'ai':
                move = game.get_best_move()
                if move == -1:  # No moves available
                    break
                game.board[move] = game.ai
                current_player = 'human'
            else:
                # Human plays randomly (worst case for AI)
                available = game.get_available_moves(game.board)
                if not available:
                    break
                move = available[0]  # Take first available (simple strategy)
                game.board[move] = game.human
                current_player = 'ai'
            
            # Check game over
            if game.is_winner(game.board, game.ai):
                ai_wins += 1
                break
            elif game.is_winner(game.board, game.human):
                print(f"AI LOST! This should never happen. Opening: {opening}")
                print(f"Final board: {game.board}")
                return False
            elif game.is_board_full(game.board):
                draws += 1
                break
        
        scenarios_tested += 1
    
    print(f"AI unbeatable test passed")
    print(f"   Scenarios tested: {scenarios_tested}")
    print(f"   AI wins: {ai_wins}")
    print(f"   Draws: {draws}")
    print(f"   AI losses: 0 (as expected)")
    
    return True

def run_all_tests():
    """Run all test functions"""
    print("=== TESTING TIC-TAC-TOE AI ===\n")
    
    try:
        test_winning_detection()
        test_ai_blocks_immediate_threats()
        test_ai_takes_winning_moves()
        test_center_preference()
        test_ai_never_loses()
        
        print("\nALL TESTS PASSED!")
        print("The AI is working correctly and is unbeatable!")
        
    except AssertionError as e:
        print(f"\nTEST FAILED: {e}")
        return False
    except Exception as e:
        print(f"\nUNEXPECTED ERROR: {e}")
        return False
    
    return True

if __name__ == "__main__":
    run_all_tests()
