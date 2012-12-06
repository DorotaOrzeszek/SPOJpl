import java.io.*;
import java.util.Hashtable;

public class Main {

	public static void main(String[] args) throws IOException {
	    Hashtable<String, Integer> ht = new Hashtable<String, Integer>();
		String[] letters = {"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"};
	    int[] numbers = {2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9};
	    for (int k = 0; k < letters.length; k++) {
	    	ht.put(letters[k],numbers[k]);
	    }
	    BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
	    int N = Integer.parseInt(in.readLine());
	    for (int n = 0; n < N; n++) {
	    	String number = "";
	    	String chars = in.readLine();
	    	for (int i = 0; i < chars.length(); i++) {
	    		number += ht.get(""+chars.charAt(i));
	    	}
	    	System.out.println(number);
	    }
	}
}
