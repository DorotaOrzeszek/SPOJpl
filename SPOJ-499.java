import java.io.*;
import java.util.Hashtable;

public class Main {
	public static Hashtable<Long,Long> memory = new Hashtable<Long,Long>();
	
	public static long power(long a, long b) {
		if (b == 0) {
    		return 1;
    	} else if (b == 1) {
    		return a;
    	} else if (memory.containsKey(b)) {
    		return (Long) memory.get(b);
    	} else {
    		// mem[b] = ( power(a, b/2) * power(a, b-b/2) ) % 10
    		long answer = ( power(a,b/2) * power(a,b-b/2) ) % 10;
    		memory.put(b, answer);
    		return answer;
    	}
	}
	
	public static void main(String[] args) throws IOException {
	    BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
	    String line1 = in.readLine();
	    long D = Long.parseLong(line1);
	    for (long i = 0; i < D; i++) {
	    	String line2 = in.readLine();
	    	String[] parts = line2.split(" ");
	    	long x = Long.parseLong(parts[0]);
	    	long y = Long.parseLong(parts[1]);
	    	long z = power(x,y);
	    	System.out.println(z);
	    	memory.clear();
	    }
	}
}
