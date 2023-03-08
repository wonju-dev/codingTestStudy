import java.util.ArrayDeque;
import java.util.HashSet;
import java.util.Queue;
import java.util.Set;

class Solution {
    public int solution(String begin, String target, String[] words) {
        Queue<Data> q = new ArrayDeque<>();
        q.add(new Data(begin, 0, new HashSet<>()));

        while (!q.isEmpty()) {
            Data data = q.poll();
            // System.out.println("data.word: " + data.word);
            if (data.word.equals(target)) {
                return data.count;
            }
            for (String word : words) {
                if (diffOnlyOne(data.word, word) && !data.usedWords.contains(word)) {
                    // System.out.println("comparing word: " + word);
                    data.usedWords.add(word);
                    q.add(new Data(word, data.count + 1, data.usedWords));
                }
            }
        }
        return 0;
    }

    private boolean diffOnlyOne(String word, String word1) {
        int diffCount = 0;
        for (int i = 0; i < word.length(); i++) {
            if (word.charAt(i) != word1.charAt(i)) {
                diffCount++;
            }
            if (diffCount > 1) {
                return false;
            }
        }
        return true;
    }

    private class Data {
        String word;
        int count;
        Set<String> usedWords;

        public Data(String word, int count, Set<String> usedWords) {
            this.word = word;
            this.count = count;
            this.usedWords = usedWords;
        }
    }
}