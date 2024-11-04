import chess
import chess.engine

board = chess.Board()
print(board)

def evaluate_board(board):
    piece_vals = {
        chess.PAWN : 1,
        chess.KNIGHT : 3,
        chess.BISHOP : 3,
        chess.ROOK : 5,
        chess.QUEEN : 9,
        chess.KING : 0
    }

    score = 0

    for piece_type in piece_vals:
        score += len(board.pieces(piece_type,chess.WHITE)) * piece_vals[piece_type]
        score -= len(board.pieces(piece_type,chess.BLACK)) * piece_vals[piece_type]

    return score


def minimax_alpha_beta (board,depth,alpha,beta,is_max):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)
    
    if is_max:
        max_eval = -float("inf")
        for move in board.legal_moves:
            board.push(move)
            eval = minimax_alpha_beta(board,depth,-1,alpha,beta,False)
            board.pop()
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    
    else:
        min_eval = float("inf")
        for move in board.legal_moves:
            board.push(move)
            eval = minimax_alpha_beta(board,depth,-1,alpha,beta,True)
            board.pop()
            min_eval = min(min_eval, eval)
            beta = min(beta,eval)
            if beta <= alpha:
                break
        
        return min_eval

def best_move(board, depth):
    best_move = None
    best_val = -float("inf")

    for move in board.legal_moves:
        board.push(board)
        move_val = minimax_alpha_beta(board,depth,-1,-float("inf"), float("inf"),False)
        board.pop()

        if move_val > best_val:
            best_val = move_val
            best_move = move

    return best_move

