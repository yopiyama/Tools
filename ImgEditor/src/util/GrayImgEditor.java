package util;

/**
 * GrayImgEditor
 */
public class GrayImgEditor extends ImgUtil {

	private double[][] filter = new double[3][3];
	private int coef = 1;
	private int offset = 0;

	public GrayImgEditor(String fileName) {
		super(fileName, ImgUtil.TYPE_GRAY);

		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				filter[i][j] = 1.0;
			}
		}
		this.coef = 9;
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

	public void applyFilter() {
		double color = 0.0;
		for (int x = 0; x < this.getSize()[0]; x++) {
			for (int y = 0; y < this.getSize()[1]; y++) {
				color = 0.0;
				for (int i = -1; i <= 1; i++) {
					for (int j = -1; j <= 1; j++) {
						int tmpX = x + i;
						int tmpY = y + j;
						if (!(tmpX < 0 || tmpY < 0 || tmpX == this.getSize()[0] || tmpY == this.getSize()[1])) {
							color += filter[i + 1][j + 1] * this.getColor(tmpX, tmpY)[0];
						}
					}
				}
				color /= this.coef;
				color += this.offset;
				if (color > 255) {
					color = 255.0;
				} else if (color < 0) {
					color = 0.0;
				}
				// System.out.println(color);
				this.setColor(x, y, (int) color);
			}
		}
	}

	public void setBlurFilter() {
		this.filter = new double[][] { { 0.0, 1.0, 0.0 }, { 1.0, 1.0, 1.0 }, { 0.0, 1.0, 0.0 } };
		this.coef = 5;
		this.offset = 0;
	}

	public void setLaplacianFilter() {
		this.filter = new double[][] { { 0.0, 1.0, 0.0 }, { 1.0, -4.0, 1.0 }, { 0.0, 1.0, 0.0 } };
		this.coef = 1;
		this.offset = 0;
	}

}