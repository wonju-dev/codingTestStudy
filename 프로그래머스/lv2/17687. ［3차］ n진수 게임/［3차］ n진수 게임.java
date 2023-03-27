import java.util.Map;

class Solution {

    static Map<Integer, Character> map = Map.of(10, 'A', 11, 'B', 12, 'C', 13, 'D', 14, 'E', 15, 'F');

    public String solution(int n, int t, int m, int p) {
        String numbers = "";
        int maxNumber = t * m;
        for (int i = 0; i < maxNumber; i++) {
            String convert = convert(i, n);
            // System.out.println("i: " + i + " " + "convert: " + convert);
            numbers += convert;
        }
        // System.out.println(numbers);
        // numbers에서 p번째 사람의 숫자를 t개를 찾아야 함
        int count = 0;
        int order = 1;
        int index = 0;
        StringBuilder sb = new StringBuilder();
        while (count < t) {
            if (order == p) {
                sb.append(numbers.charAt(index));
                count++;
            }
            order++;
            index++;
            if (order > m) {
                order = 1;
            }
        }
        return sb.toString();
    }


    private String convert(int i, int std) {
        StringBuilder converted = new StringBuilder();

        if (std > 10) {
            while (i >= std) {
                int remainder = i % std;
                if (remainder >= 10) {
                    converted.append(map.get(remainder));
                } else {
                    converted.append(remainder);
                }
                i = i / std;
            }
            if (i >= 10) {
                converted.append(map.get(i));
            } else {
                converted.append(i);
            }
        } else {
            while (i >= std) {
                converted.append(i % std);
                i = i / std;
            }
            converted.append(i);
        }
        return converted.reverse().toString();
    }
}