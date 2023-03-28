import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] solution(int[] numbers, int num1, int num2) {
        List<Integer> list = toList(numbers);
        return list.subList(num1, num2 + 1).stream().mapToInt(Integer::valueOf).toArray();
    }

    private List<Integer> toList(int[] numbers) {
        List<Integer> list = new ArrayList<>();
        for (int number : numbers) {
            list.add(number);
        }
        return list;
    }
}