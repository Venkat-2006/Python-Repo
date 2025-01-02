import java.util.Scanner;

public class SalaryCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        float basicSalary = scanner.nextFloat();
        float hra = scanner.nextFloat();
        float da = scanner.nextFloat();
        
        float pf = 0.12f * basicSalary;
        float grossSalary = basicSalary + hra + da + pf;
        
        System.out.printf("%.2f\n", pf);
        System.out.printf("%.2f\n", grossSalary);
        
        scanner.close();
    }
}
