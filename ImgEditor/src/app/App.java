package app;

import util.ColorImgEditor;
import util.GrayImgEditor;

public class App {
	public static void main(String[] args) {
		String ext = "png";

		String inImgName = "./img/lena.png";
		String outImgName = "./img/out_lena.png";
		ColorImgEditor sImg = new ColorImgEditor(inImgName);
		sImg.invertColor();
		sImg.saveImg(outImgName, ext);
		// new MyFrame(inImgName, sImg.getSize(), inImgName, outImgName);

		String inGrayImg = "./img/lena_gray.png";
		String outGrayImg = "./img/out_lena_gray.png";
		GrayImgEditor grayImg = new GrayImgEditor(inGrayImg);
		// grayImg.invertColor();
		// grayImg.setBlurFilter();
		grayImg.setLaplacianFilter();
		grayImg.applyFilter();
		grayImg.saveImg(outGrayImg, ext);
		new MyFrame(inGrayImg, grayImg.getSize(), inGrayImg, outGrayImg);
	}
}
