package app;

import javax.swing.ImageIcon;
import javax.swing.JLabel;
import javax.swing.JPanel;

/**
 * MyPanel
 */
public class MyPanel extends JPanel {

	private static final long serialVersionUID = 8246534783728771486L;

	public MyPanel(String imgName) {
		JLabel label = new JLabel();
		ImageIcon icon = new ImageIcon(imgName);
		label.setIcon(icon);
		this.add(label);
	}
}