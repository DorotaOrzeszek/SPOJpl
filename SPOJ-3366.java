import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException {
	    BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
	    String testcases = in.readLine();
		int t = Integer.parseInt(testcases);
		for (int s = 0; s < t; s++) {
			int[][] sudoku = new int[9][9];
			for (int p = 0; p < 9; p++) {
				String line = in.readLine();
				// System.out.println("reading p = "+p+" : "+line);
				String[] numbers = line.split(" ");
				for (int q = 0; q < 9; q++) {
					sudoku[p][q] = Integer.parseInt(numbers[q]);
				}				
			}
			if (s < t-1) {
				String blank = in.readLine();
			}
			boolean isSudoku = true;
			// checking row & column sums
			for (int i = 0; i < 9; i++) {
				int rowsum = 0;
				int colsum = 0;
				for (int j = 0; j < 9; j++) {
					rowsum += sudoku[i][j];
					colsum += sudoku[j][i];
				}
				if (rowsum != 45 || colsum != 45) {
					isSudoku = false;
					// System.out.println("NIE");
					break;
				}
			}
			// checking box sums
			for (int i = 0; i < 9; i += 3) {
				for (int j = 0; j < 9; j += 3) {
					int boxsum;
					boxsum = sudoku[i][j] + sudoku[i][j+1] + sudoku[i][j+2] + sudoku[i+1][j] + sudoku[i+1][j+1] + sudoku[i+1][j+2] + sudoku[i+2][j] + sudoku[i+2][j+1] + sudoku[i+2][j+2];
					if (boxsum != 45) {
						isSudoku = false;
						break;
					}
				}
				if (isSudoku == false) {
					break;
				}
			}
			if (isSudoku == false) {
				System.out.println("NIE");
			} else {
				System.out.println("TAK");
			}
		}
	}
}
