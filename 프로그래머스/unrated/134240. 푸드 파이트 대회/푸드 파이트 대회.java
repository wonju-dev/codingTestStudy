class Solution {

    public static void main(String[] args) {
        int[] foods = {1, 3, 4, 6};
        solution(foods);
    }

    public static String solution(int[] food) {
        String front = "";
        for (int i = 1; i < food.length; i++) {
            front += multiply(food[i] / 2, i);
        }
        return front + "0" + reverse(front);
    }

    private static String multiply(int count, int number) {
        String s = "";
        for (int i =0  ; i < count; i++) {
            s += number;
        }
        return s;
    }

    private static String reverse(String front) {
        String reverse = "";
        for (int i = front.length() - 1; i >= 0; i--) {
            reverse += front.charAt(i);
        }
        return reverse;
    }
}