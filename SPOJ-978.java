import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException {
	    BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
	    int[] stack = new int[10];
	    int i = 0;
	    while (true) {
	    	String command = in.readLine();
	    	if (command == null) {
	    		break;
	    	}
	    	if (command.equals("+")) {
	    		String value = in.readLine();
	    		int newvalue = Integer.parseInt(value);
	    		if (i < 10) {
	    			stack[i] = newvalue;
	    			i += 1;
	    			System.out.println(":)");
	    		} else {
	    			System.out.println(":(");
	    		}
	    	} else if (command.equals("-")) {
	    		if (i > 0) {
	    			i -= 1;
	    			System.out.println(stack[i]);
	    		} else {
	    			System.out.println(":(");
	    		}
	    	}

	    }
	}
}
