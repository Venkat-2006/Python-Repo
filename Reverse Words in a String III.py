import java.util.Scanner;
public class ReverseWords {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        String[] words = input.split(" ");

        for (String word : words) {
            StringBuilder reversed = new StringBuilder(word).reverse();
            System.out.print(reversed + " ");
        }
    }
}
