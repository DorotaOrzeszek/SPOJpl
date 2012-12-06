import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException {
	    BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
	    
	    while (true) {
			try {
				String line = in.readLine();
				String[] parts = line.split(" ");
				String operator = parts[0];
				int a = Integer.parseInt(parts[1]);
				int b = Integer.parseInt(parts[2]);
				if (operator.equals("+")) {
					System.out.println(a+b);
				} else if (operator.equals("-")) {
					System.out.println(a-b);
				} else if (operator.equals("*")) {
					System.out.println(a*b);
				} else if (operator.equals("/")) {
					System.out.println(a/b);
				} else if (operator.equals("%")) {
					System.out.println(a%b);
				} 
			} catch (Exception IOException) {
				break;
			}
		}
	}
}

