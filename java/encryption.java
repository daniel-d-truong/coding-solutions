//https://www.hackerrank.com/challenges/encryption/problem

//decent solution but does not account for all cases. My guess is that this is too slow

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;
import java.util.List;
import java.util.stream.Collectors;

public class Solution {

    // Complete the encryption function below.
    static String encryption(String s) {
        String newS = s.replaceAll("\\s", "");
        int rows = (int) Math.sqrt(newS.length());
        int columns = (int) Math.sqrt(newS.length()) + 1;
        if (rows*columns < newS.length())
            rows++;

        char[][] list = new char [rows][columns];
        int index = 0;

//         int start = 0;
//         int end = start+columns;
//         for (int i = 0; i < rows; i++){
//             String temp = newS.substring(start,end);
//             List<Character> chars = temp.chars()
//                                     .mapToObj(e -> (char) e)
//                                     .collect(Collectors.toList());
//             //http://www.techiedelight.com/convert-string-list-characters-java/
//         }

        System.out.println(newS);
        for (int r = 0; r < rows; r++){
            for (int c = 0; c<columns; c++){
                list[r][c] = newS.charAt(index);
                System.out.println(list[r][c]);
                System.out.println("Index: " + index);
                System.out.println("Row, Column: " + r +","+c);
                index++;
                if (index == newS.length())
                    break;

            }
        }


        String end = "";
        for (int c = 0; c < columns; c++){
            for (int r = 0; r < rows; r++){
                if ((list[r][c] == Character.UNASSIGNED)){ //biggest issue figuring out that list[r][c] was a null value, not a space            
                    System.out.println();
                    break;
                }
                end+=list[r][c];
            }
            end+=" ";
        }

        return end;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String s = scanner.nextLine();

        String result = encryption(s);

        bufferedWriter.write(result);
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
