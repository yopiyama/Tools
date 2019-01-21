package util;

/**
 * GrayImgEditor
 */
public class GrayImgEditor extends ImgUtil {

	public GrayImgEditor(String fileName) {
		super(fileName, ImgUtil.TYPE_GRAY);
	}

	@Override
	public void invertColor() {
		int color = 0;
		for (int x = 0; x < this.inImg.getWidth(); x++) {
			for (int y = 0; y < this.inImg.getHeight(); y++) {
				color = this.getColor(x, y)[0];
				color = 255 - color;
				this.setColor(x, y, color);
			}
		}
	}
}