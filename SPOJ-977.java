import java.io.*;
import java.util.ArrayList;
import java.util.Collections;

public class Main {

	public static void main(String[] args) throws IOException {
	    BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
	    ArrayList<Integer> data = new ArrayList<Integer>();
	    String line = in.readLine();
		String[] numbers = line.split(" ");
		for (int i = 0; i < numbers.length; i++) {
			data.add(Integer.parseInt(numbers[i]));
		}
		Collections.reverse(data);
		for (int j = 0; j < numbers.length; j++) {
			System.out.print(data.get(j)+" ");
		}
	}
}
