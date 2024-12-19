import java.util.Scanner;  // Import the Scanner class
public class isithalloween {
    public static void main (String args[]) {
        Scanner myScanner = new Scanner(System.in);
        String dateAsked = myScanner.nextLine();
        String[] dateAskedArray = dateAsked.split(" ");
        if (dateAskedArray[0].equals("OCT") && (Integer.valueOf(dateAskedArray[1])).equals(31)) {
            System.out.println("yup");
        }
        else if (dateAskedArray[0].equals("DEC") && (Integer.valueOf(dateAskedArray[1])).equals(25)) {
            System.out.println("yup");
        }
        else {
            System.out.println("nope");
        }
        myScanner.close();
    }
}