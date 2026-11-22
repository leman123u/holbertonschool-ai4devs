
public class Bug3Fixed {

    public static double calculateAverage(int[] grades) {
        if (grades == null || grades.length == 0) {
            return 0;
        }

        int sum = 0;

        for (int grade : grades) {
            sum += grade;
        }

        double average = (double) sum / grades.length;

        return average;
    }

    public static void main(String[] args) {
        int[] grades1 = {75, 80, 90};
        int[] grades2 = {10, 20};
        int[] grades3 = {};

        System.out.println(calculateAverage(grades1));
        System.out.println(calculateAverage(grades2));
        System.out.println(calculateAverage(grades3));
    }
}
