import java.util.Arrays;
import java.util.Comparator;
import java.nio.charset.StandardCharsets;

class Solution {
    public long solution(long n) {
        
        String[] numberChunks = Long.toString(n).split("");
        
        Arrays.sort(numberChunks, new Comparator<String>() {
            public int compare(String s1, String s2) {
                return (s1.getBytes(StandardCharsets.US_ASCII)[0] >= s2.getBytes(StandardCharsets.US_ASCII)[0]) ? -1 : 1; 
            }
        });
        
        return Long.parseLong(String.join("",numberChunks));
    }
}
