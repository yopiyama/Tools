package util;

import java.awt.Color;
import java.awt.image.BufferedImage;
import java.io.File;

import javax.imageio.ImageIO;

/**
 * ImgUtil
 */
public abstract class ImgUtil {

	protected BufferedImage inImg;
	protected BufferedImage outImg;

	protected static final int TYPE_RGBA = BufferedImage.TYPE_INT_ARGB;
	protected static final int TYPE_GRAY = BufferedImage.TYPE_BYTE_GRAY;

	public ImgUtil(String fileName, int type) {
		try {
			this.inImg = ImageIO.read(new File(fileName));
		} catch (Exception e) {
			e.printStackTrace();
		}
		this.outImg = new BufferedImage(inImg.getWidth(), inImg.getHeight(), type);
	}

	public void saveImg(String saveFileName, String ext) {
		try {
			ImageIO.write(this.outImg, ext, new File(saveFileName));
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	public BufferedImage getInImg() {
		return this.inImg;
	}

	public BufferedImage getOutImg() {
		return this.outImg;
	}

	public int[] getSize() {
		int[] size = new int[2];
		size[0] = inImg.getWidth();
		size[1] = inImg.getHeight();
		return size;
	}

	protected int[] getColor(int x, int y) {
		Color color = new Color(inImg.getRGB(x, y));
		int[] colorArray = new int[4];
		colorArray[0] = color.getRed();
		colorArray[1] = color.getGreen();
		colorArray[2] = color.getBlue();
		colorArray[3] = color.getAlpha();
		return colorArray;
	}

	protected void setColor(int x, int y, int... color) {
		int rgb = this.intToRgb(color);
		this.outImg.setRGB(x, y, rgb);
	}

	protected int intToRgb(int[] intColor) {
		Color color;
		if (intColor.length == 1) {
			color = new Color(intColor[0], intColor[0], intColor[0], 255);
		} else {
			color = new Color(intColor[0], intColor[1], intColor[2], intColor[3]);
		}
		return color.getRGB();
	}

	public abstract void invertColor();
}