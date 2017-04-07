// Read data 

import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.Scanner;
import java.util.HashMap;
import java.util.ArrayList;
import java.lang.Object;

public class read_data {
	public static void main(String[] args) throws FileNotFoundException{

		ArrayList<String> array = new ArrayList<String>();
		Scanner in = new Scanner(new File("ES.asc"));
		//PrintWriter out = new PrintWriter("ES.asc");
		int row = 0;
		while(in.hasNextLine() && row < 10) {
			array.add(String.parseDouble(in.nextLine()));
			row++;
		}

	}


}