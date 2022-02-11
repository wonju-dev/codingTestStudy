import java.util.Arrays;
import java.util.stream.IntStream;

class Solution {
    public int[] solution(int[] arr) {
        if (arr.length == 1) return new int[] {-1};
        
        int index = getMinIndex(arr);
        return returnAnswer(arr, index);
    }
    
    public int getMinIndex(int[] arr) {
        int index = 0;
        int min = arr[0];
        for (int i = 0 ; i < arr.length ; i++) {
            if (min >= arr[i]) {
                min = arr[i];
                index = i;
            }
        }
        return index;
    }
    
    public int[] returnAnswer (int[] arr, int index) {
        return Arrays.stream(arr).filter((num) -> num != arr[index]).toArray();
    }
}
