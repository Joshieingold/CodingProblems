import java.util.Scanner;  // Import the Scanner class
public class meddelande {
    public static void main (String args[]) {
        // Final output
        StringBuilder output = new StringBuilder();
        
        // Makes a scanner to read inputs.
        Scanner myScanner = new Scanner(System.in);  // Create a Scanner object
        
        // Gets the first line of code stipulating the data
        String rawBoxSize = myScanner.nextLine();
        String[] dimensionArray = rawBoxSize.split(" ");
        int length = Integer.valueOf(dimensionArray[0]);
        int width = Integer.valueOf(dimensionArray[1]);
        
        // going through the next inputs.
        for (int i = 0; i < length; i++) {
            String testCase = myScanner.nextLine();
            for (int j = 0; j < width; j++) {
                if (testCase.charAt(j) != '.') {
                    output.append(testCase.charAt(j));
                }
            }
        }
        myScanner.close();
        System.out.println(output);
    }
}
