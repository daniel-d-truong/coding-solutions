//https://www.hackerrank.com/challenges/mark-and-toys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

//selection sort algorithm
public class Solution {
    
    //selection sort
    static void sort(int[] array) {
        for (int i = 1; i < array.length; i++){
            int min = array[i];
            int minIndex = i; 
            
            //finds the minimum from array[k...length]
            for (int k = i+1; k < array.length; k++){
                if (array[k] < min){
                    min = array[k];
                    minIndex = k; 
                }
            }
            
            array[minIndex] = array[i];
            array[i] = min; 
            
        }
    }
    
    // Complete the maximumToys function below.
    static int maximumToys(int[] prices, int k) {
        //k is the total price mark has to spend
        sort(prices);
        for (int x: prices){
            System.out.println(x);
        }
        int countPrices = k; 
        int counter = 0; 
        for (int x: prices){
            countPrices-=x;
            if (countPrices >= 0)
                counter++;
            else
                return counter; 
        }
        return counter; 
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String[] nk = scanner.nextLine().split(" ");

        int n = Integer.parseInt(nk[0]);

        int k = Integer.parseInt(nk[1]); //price

        int[] prices = new int[n];

        String[] pricesItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < n; i++) {
            int pricesItem = Integer.parseInt(pricesItems[i]);
            prices[i] = pricesItem;
        }

        int result = maximumToys(prices, k);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}

//not the most successful solution but this implements selection sort 
