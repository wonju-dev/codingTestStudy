class Solution {
    public int solution(int[] array, int n) {
        int[] numbers = new int[1001];
        for (int number : array) {
            numbers[number]++;
        }
        return numbers[n];
    }
}