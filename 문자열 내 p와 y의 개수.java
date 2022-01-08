class Solution {
    boolean solution(String s) {
        int isEqual = 0;
        s = s.toUpperCase();
        for (int i = 0 ; i < s.length() ; i++) {
            char character = s.charAt(i);
            if (character == 'P') isEqual ++;
            else if (character == 'Y') isEqual --;
        }
        return isEqual == 0 ? true : false;
    }
}
