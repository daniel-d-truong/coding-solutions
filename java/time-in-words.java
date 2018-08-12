//https://www.hackerrank.com/challenges/the-time-in-words/problem

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the timeInWords function below.
    static String timeInWords(int h, int m) {
        Map <Integer, String> hashMap = new HashMap<Integer, String>() //learned how to create hashMap!!
        {{ //puts numbers from 1-30 in hashMap
            put(1, "one");
            put(2, "two");
            put(3, "three");
            put(4, "four");
            put(5, "five");
            put(6, "six");
            put(7, "seven");
            put(8, "eight");
            put(9, "nine");
            put(10, "ten");
            put(11, "eleven");
            put(12, "twelve");
            put(13, "thirteen");
            put(14, "fourteen");
            put(15, "quarter");
            put(16, "sixteen");
            put(17, "seventeen");
            put(18, "eighteen");
            put(19, "nineteen");
            put(20, "twenty");
            put(21, "twenty one");
            put(22, "twenty two");
            put(23, "twenty three");
            put(24, "twenty four");
            put(25, "twenty five");
            put(26, "twenty six");
            put(27, "twenty seven");
            put(28, "twenty eight");
            put(29, "twenty nine");
            put(30, "half");
        }};


        String preposition = "";
        String min = "";
        if (m >30){ //if m > 30, takes equivalent minute to the hour
            h++;
            if (h >12) //if hour is 12, next hour would be 1, not 13
                h-=12;
            m=60-m;
            preposition = "to";
        }
        else if (m > 0){
            preposition = "past";
        }
        else if (m==0){
            return hashMap.get(h) + " " + "o' clock";
        }

        if (m == 1){
            min = " minute";
        }
        else if (m > 1 && m!=15 & m!=30){ //must consider cases where m is 15 or m is 30, because those minutes use special words 
            min = " minutes";
        }

        System.out.println(min);
        String fin = hashMap.get(m) + min + " " + preposition + " " + hashMap.get(h);
        return fin;

    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int h = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int m = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        String result = timeInWords(h, m);

        bufferedWriter.write(result);
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
