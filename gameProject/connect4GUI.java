
import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
import java.awt.geom.*;

public class connect4GUI {
    public static void main(String[] args) {
        connect4Board board = new connect4Board();
        JFrame frame = new JFrame("Connect 4");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        MyPanel panel = new MyPanel(board);
        panel.setPreferredSize(new Dimension(520, 440));
        panel.addMouseMotionListener(panel);
        panel.addMouseListener(panel);
        Timer timer = new Timer(1, panel);
        timer.start();
        frame.addKeyListener(panel);
        frame.add(panel);
        frame.pack();
        frame.setVisible(true);

    }
}

class MyPanel extends JPanel implements MouseMotionListener, KeyListener, MouseListener, ActionListener {
    connect4Board board;
    int ROWS=6;
	int COLS=7;
    int col;
    int player=1;
    Point2D transform = new Point2D.Double(-20, -20);

    public MyPanel(connect4Board board) {
        this.board = board;
    }
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        Graphics2D g2 = (Graphics2D) g;
        RenderingHints rh = new RenderingHints(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
        g2.setRenderingHints(rh);
        g2.setColor(new Color(100, 120, 245));
        g2.fillRect(0, 0, 520, 440);
        g2.setColor(new Color(100, 50, 245));
        int x = 20;
        int y = 20;
        if (board.hasPlayerWon(1)) {
            g2.setColor(Color.BLACK);
            g2.setFont(new Font("Arial", Font.BOLD, 30));
            g2.drawString("Player 1 has won!", 140, 220);
            g2.setFont(new Font("ArialSmall", Font.PLAIN, 20));
            g2.drawString("Press any key to play again.", 140, 240);
            
        } else if (board.hasPlayerWon(2)) {
            g2.setColor(Color.BLACK);
            g2.setFont(new Font("Arial", Font.BOLD, 30));
            g2.drawString("Player 2 has won!", 140, 220);
            g2.setFont(new Font("ArialSmall", Font.PLAIN, 20));
            g2.drawString("Press any key to play again.", 140, 240);
        }
        if(board.isBoardFull()){
            g2.setColor(Color.BLACK);
            g2.setFont(new Font("Arial", Font.BOLD, 30));
            g2.drawString("It's a Tie!", 200, 220);
            g2.setFont(new Font("ArialSmall", Font.PLAIN, 20));
            g2.drawString("Press any key to play again.", 140, 240);
        }
        if((board.hasPlayerWon(1)==false)&&(board.hasPlayerWon(2)==false)&&(board.isBoardFull()==false)){
        for (int i = 0; i < ROWS; i++) {
            for (int j = 0; j < COLS; j++) {
                g2.setColor(new Color(100, 50, 245));
                g2.fillOval(x, y, 50, 50);
                if (board.getPiece(i, j) == 1) {
                    g2.setColor(Color.RED);
                    g2.fillOval(x + 5, y + 5, 40, 40);
                } else if (board.getPiece(i, j) == 2) {
                    g2.setColor(Color.YELLOW);
                    g2.fillOval(x + 5, y + 5, 40, 40);
                }
                x += 70;
            }
            x = 20;
            y += 70;
        }
        if (col >= 0 && col < COLS) {
            g2.setColor(new Color(255, 255, 255, 128));
            int lowestOpenRow = board.getLowestOpenRow(col);
            g2.fillOval(20 + col * 70 + 5, 20 + lowestOpenRow * 70 + 5, 40, 40);
        }
    }
}
    public void mouseMoved(MouseEvent e) {
        Point mousePos = e.getPoint();
        int x = (int) mousePos.getX();
        int y = (int) mousePos.getY();
        col = (x - 20) / 70;
        transform = new Point2D.Double(20 + col * 70, -20);
        repaint();
    }
    public void mousePressed(MouseEvent e) {
        int col = (e.getX() - 20) / 70; 
        board.makeMove(col+1);
        repaint();
        }
    public void mouseDragged(MouseEvent e) {
    }
    public void keyReleased(KeyEvent e) {
    }
    public void keyPressed(KeyEvent e) {
        if(board.hasPlayerWon(1)||board.hasPlayerWon(2)||board.isBoardFull()){
            board = new connect4Board();
            repaint();
        }
    }
    public void keyTyped(KeyEvent e) {
    }
    public void mouseExited(MouseEvent e) {
    }
    public void mouseEntered(MouseEvent e) {
	}
    public void mouseReleased(MouseEvent e) {
    }
    public void mouseClicked(MouseEvent e) {
    }
    public void actionPerformed(ActionEvent e) {
    }
}
