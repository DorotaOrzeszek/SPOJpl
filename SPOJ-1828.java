import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException {
	    BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
	    String input1 = in.readLine();
	    String input2 = in.readLine();
	    String input3 = in.readLine();
	    int a = Integer.parseInt(input1);
	    int b = Integer.parseInt(input2);
	    int c = Integer.parseInt(input3);
	    int abc = a + b + c; 
	    System.out.println(abc);
	}
}
