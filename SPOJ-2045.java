import java.io.*;
import java.util.Hashtable;

public class Main {

	public static void main(String[] args) throws IOException {
	    BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
	    String[] coordinates1 = in.readLine().split(" ");
	    String[] coordinates2 = in.readLine().split(" ");
	    int x1a = Integer.parseInt(coordinates1[0]);
	    int y1a = Integer.parseInt(coordinates1[1]);
	    int x2a = Integer.parseInt(coordinates1[2]);
	    int y2a = Integer.parseInt(coordinates1[3]);
	    int x1b = Integer.parseInt(coordinates2[0]);
	    int y1b = Integer.parseInt(coordinates2[1]);
	    int x2b = Integer.parseInt(coordinates2[2]);
	    int y2b = Integer.parseInt(coordinates2[3]);
	    int areaA = (x2a - x1a) * (y2a - y1a);
	    int areaB = (x2b - x1b) * (y2b - y1b);
	    int areaC;
	    int x1c = Math.max(x1a, x1b);
	    int y1c = Math.max(y1a, y1b);
	    int x2c = Math.min(x2a, x2b);
	    int y2c = Math.min(y2a, y2b);
	    int cx = x2c - x1c;
	    int cy = y2c - y1c;
	    if (cx > 0 && cy > 0) {
	    	areaC = cx * cy;
	    } else {
	    	areaC = 0;
	    }
	    int areaAB = areaA + areaB - areaC;
	    System.out.println(areaAB);
	}
}
