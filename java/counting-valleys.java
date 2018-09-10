//https://www.hackerrank.com/challenges/counting-valleys/problem

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the countingValleys function below.
    static int countingValleys(int n, String s) {
        int level = 0; 
        int countValleys = 0; 
        char[] array = s.toCharArray();
        for (char x: array){
            boolean goingUp = true; 
            if (x == 'U'){
                level+=1;
                goingUp = true; 
            }
            else if (x == 'D'){
                level-=1;
                goingUp = false; 
            }
            
            if (level == 0 && goingUp){
                countValleys++;
            }
        }
        return countValleys; 

    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = scanner.nextInt(); //number of symbols in string s
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        String s = scanner.nextLine();

        int result = countingValleys(n, s);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}

//solution works! 
