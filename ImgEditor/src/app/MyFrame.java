package app;

import java.awt.BorderLayout;
import javax.swing.JFrame;

/**
 * MyFrame
 */
public class MyFrame extends JFrame {

	private static final long serialVersionUID = -903903387982741341L;

	public MyFrame(String title, int[] size, String inImg, String outImg) {
		super(title);
		this.setDefaultCloseOperation(EXIT_ON_CLOSE);
		this.setSize(size[0] * 2 + 50, size[1] + 50);
		this.add(new MyPanel(inImg), BorderLayout.WEST);
		this.add(new MyPanel(outImg), BorderLayout.EAST);
		this.setVisible(true);
	}
}