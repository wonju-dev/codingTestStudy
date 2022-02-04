class Solution {
    public int solution(String s) {
        return s.substring(0,1).equals('-') ? -1 * Integer.parseInt(s) : Integer.parseInt(s);
    }
}
