import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;


class Solution {
    public int solution(int[] elements) {
        List<Integer> numbers = init(elements);
        Set<Integer> set = new HashSet<>();

        for (int size = 1; size <= elements.length; size++) {
            for (int i = 0 ; i < elements.length; i++) {
                set.add(numbers.subList(i, i + size).stream().collect(Collectors.summingInt(Integer::valueOf)));
            }
        }

        return set.size();
    }

    private List<Integer> init(int[] elements) {
        List<Integer> numbers = new ArrayList<>();
        for (int element : elements) {
            numbers.add(element);
        }
        for (int element : elements) {
            numbers.add(element);
        }
        return numbers;
    }
}