import java.util.*;
import java.util.Arrays;

public class connect4Game {
    private connect4Board board;
    private final int ROWS = 6;
    private final int COLS = 7;

    public connect4Game() {
        board = new connect4Board();
        System.out.println("Welcome to Connect4!");
    }

    public int getWinner(){
        if(board.hasPlayerWon(1)){
            return(1);
        }
        if(board.hasPlayerWon(2)){
            return(2);
        }
        return(0);
    }

    

    public void play(int col) {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            board.printBoard();

            // Check if column is valid 
            

            // Make move

            // Check for win
            if (board.hasPlayerWon(board.getCurrentPlayer())) {
                System.out.println("Player " + board.getCurrentPlayer() + " wins!");
                board.printBoard();
            }

          
            
            
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Scanner yn = new Scanner(System.in);
        connect4Game game = new connect4Game();
        boolean playAgain = true;
        while(playAgain){
            while(game.getWinner()==0){
                game.board.printBoard();
                System.out.println("The current player is "+game.board.getCurrentPlayer());
                System.out.print("Enter a column number:");
                game.board.makeMove(sc.nextInt());
            }
            if(game.getWinner()==1){
                game.board.printBoard();
                System.out.println("Player 1 Wins!");
            }
            else if(game.getWinner()==2){
                game.board.printBoard();
                System.out.println("Player 2 Wins!");
            }
            System.out.print("Do you want to play again? (y/n): ");
            String answer = yn.nextLine();
            if(answer.equalsIgnoreCase("y")){
                game.board.clearBoard();
            } else {
                playAgain = false;
            }
        }
        System.out.println("Thanks for Playing!");
    }
}
