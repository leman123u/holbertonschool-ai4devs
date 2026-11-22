
public class Bug3 {
    public static double calculateAverage(int[] grades) {
        if (grades == null || grades.length == 0) {
            return 0;
        }

        int sum = 0;

        for (int grade : grades) {
            sum += grade;
        }

        int average = sum / grades.length;

        return average;
    }

    public static void main(String[] args) {
        int[] grades = {75, 80, 90};

        double result = calculateAverage(grades);

        System.out.println("Average grade: " + result);
    }
}
