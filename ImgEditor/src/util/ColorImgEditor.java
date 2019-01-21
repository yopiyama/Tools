package util;

/**
 * ColorImgEditor
 */
public class ColorImgEditor extends ImgUtil {

	public ColorImgEditor(String fileName) {
		super(fileName, ImgUtil.TYPE_RGBA);
	}

	@Override
	public void invertColor() {
		int[] colorArray = new int[4];
		for (int x = 0; x < this.inImg.getWidth(); x++) {
			for (int y = 0; y < this.inImg.getHeight(); y++) {
				colorArray = this.getColor(x, y);
				for (int i = 0; i < 3; i++) {
					colorArray[i] = 255 - colorArray[i];
				}
				this.setColor(x, y, colorArray);
			}
		}
	}
}