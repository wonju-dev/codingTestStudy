class Solution {
    public int[] solution(long n) {
        String[] array = Long.toString(n).split("");
        return reverse(array);
    }
    
    private int[] reverse(String[] array) {
        int[] reversed = new int[array.length];
        for (int i = 0 ; i <= array.length / 2 ; i++) {
            int backIndex = array.length -i -1;
            int front = Integer.parseInt(array[i]);
            int back = Integer.parseInt(array[backIndex]);

            reversed[i] = back;
            reversed[backIndex] = front;
        }
        return reversed;
    }    
}
