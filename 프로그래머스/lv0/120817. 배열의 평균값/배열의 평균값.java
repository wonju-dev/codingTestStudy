import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public double solution(int[] numbers) {
        return Arrays.stream(numbers).average().getAsDouble();
    }
}