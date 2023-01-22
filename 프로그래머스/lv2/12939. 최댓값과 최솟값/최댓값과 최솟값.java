import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

class Solution {
    public String solution(String s) {
        List<String> collect = Arrays.stream(s.split(" ")).sorted(Comparator.comparing(Integer::valueOf)).collect(Collectors.toList());
        return collect.get(0) + " " + collect.get(collect.size() - 1);
    }
}