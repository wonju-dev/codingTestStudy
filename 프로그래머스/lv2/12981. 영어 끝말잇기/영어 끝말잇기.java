import java.util.HashSet;
import java.util.Set;

class Solution {
public int[] solution(int n, String[] words) {
        int[] answer = {0, 0};
        Set<String> usedWords = new HashSet<>();
        int user = 2;
        int loop = 1;

        String lastWord = words[0];
        usedWords.add(words[0]);
        for (int i = 1; i < words.length; i++) {
            String word = words[i];
            if (lastWord.charAt(lastWord.length() - 1) != word.charAt(0)) {
                answer[0] = user;
                answer[1] = loop;
                return answer;
            }
            if (usedWords.contains(word)) {
                answer[0] = user;
                answer[1] = loop;
                return answer;
            }
            usedWords.add(word);
            lastWord = word;

            loop += user == n ? 1 : 0;
            user = user == n ? 1 : user + 1;
        }

        return answer;
    }
}