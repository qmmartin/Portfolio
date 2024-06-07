public class connect4Board {
    private final int ROWS = 6;
    private final int COLS = 7;
    public int[][] board;

    public connect4Board() {
        board = new int[ROWS][COLS];
        for (int row = 0; row < ROWS; row++) {
            for (int col = 0; col < COLS; col++) {
                board[row][col] = 0;
            }
        }
    }

    public void clearBoard() {
        for (int row = 0; row < board.length; row++) {
            for (int col = 0; col < board[0].length; col++) {
                board[row][col] = 0;
            }
        }
    }

    public void printBoard() {
        System.out.println("-----------------------------");
        for (int row = 0; row < ROWS; row++) {
            System.out.print("| ");
            for (int col = 0; col < COLS; col++) {
                System.out.print(board[row][col] + " | ");
            }
            System.out.println();
            System.out.println("-----------------------------");
        }
    }

    public boolean isValidMove(int col) {
        if (col < 1 || col > COLS) {
            return false;
        }
        if (board[0][col-1] != 0) {
            return false;
        }
        return true;
    }
    public int getCurrentPlayer() {
        int numPieces = 0;
        for (int row = 0; row < ROWS; row++) {
            for (int col = 0; col < COLS; col++) {
                if (board[row][col] != 0) {
                    numPieces++;
                }
            }
        }
        if(numPieces % 2 ==0){
            return(1);
        }
        else if(numPieces % 2 ==1){
            return(2);
        }
        return(0);
        
    }
    public void makeMove(int col) {
        for (int row = ROWS - 1; row >= 0; row--) {
            if (board[row][col-1]==0) {
                board[row][col-1] = getCurrentPlayer();
                break;
            }
        }
        printBoard();
    }

    public int getPiece(int row, int col) {
        if (row < 0 || row >= board.length || col < 0 || col >= board[0].length) {
            // index out of bounds
            return 0;
        }
        return board[row][col];
    }
    
    public int getLowestOpenRow(int col) {
        for (int i = ROWS - 1; i >= 0; i--) {
            if (board[i][col] == 0) {
                return i;
            }
        }
        return -1;
    }

    public boolean isBoardFull() {
        for (int col = 0; col < COLS; col++) {
            if (board[0][col] == 0) {
                return false;
            }
        }
        return true;
    }
    
    public boolean hasPlayerWon(int player) {
        // Check horizontal
        for (int row = 0; row < ROWS; row++) {
            for (int col = 0; col <= COLS - 4; col++) {
                if (board[row][col] == player && board[row][col+1] == player &&
                    board[row][col+2] == player && board[row][col+3] == player) {
                    return true;
                }
            }
        }

        // Check vertical
        for (int row = 0; row <= ROWS - 4; row++) {
            for (int col = 0; col < COLS; col++) {
                if (board[row][col] == player && board[row+1][col] == player &&
                    board[row+2][col] == player && board[row+3][col] == player) {
                    return true;
                }
            }
        }

        // Check diagonal (top left to bottom right)
        for (int row = 0; row <= ROWS - 4; row++) {
            for (int col = 0; col <= COLS - 4; col++) {
                if (board[row][col] == player && board[row+1][col+1] == player && board[row+2][col+2] == player && board[row+3][col+3] == player) {
                    return true;
                }
            }
        }

        // Check diagonal (top right to bottom left)
        for (int row = 0; row <= ROWS - 4; row++) {
            for (int col = 3; col < COLS; col++) {
                if (board[row][col] == player && board[row+1][col-1] == player &&
                    board[row+2][col-2] == player && board[row+3][col-3] == player) {
                    return true;
                }
            }
        }
        return false;
    }
}