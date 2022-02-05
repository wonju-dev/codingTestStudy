class Solution {
    public long solution(long n) {
        double square = (long) Math.sqrt(n);
        return Math.pow(square, 2) == n ? (long) Math.pow(square+1, 2) : (long) -1;
    }
}
