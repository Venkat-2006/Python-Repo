import java.util.Scanner;

public class StringProtocol {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        for (int t = 0; t < T; t++) {
            int N = scanner.nextInt();
            String S = scanner.next();
            int time = 0;
            for (int i = 0; i < N; i++) {
                if (i < N - 1 && S.charAt(i) == S.charAt(i + 1)) {
                    time++;
                    i++;
                } else {
                    time++;
                }
            }
            System.out.println(time);
        }
        scanner.close();
    }
}
