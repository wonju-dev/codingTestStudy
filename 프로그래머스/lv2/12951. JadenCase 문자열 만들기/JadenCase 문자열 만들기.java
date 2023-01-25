
class Solution {
    public String solution(String s) {
        s = s.toLowerCase();
        byte[] bytes = s.getBytes();

        for (int i = 0; i < bytes.length; i++) {
            if (Character.isDigit(bytes[i])) {
                continue;
            }
            else if (i == 0) {
                if (Character.isLetter(bytes[i])) {
                    bytes[i] = (byte) Character.toUpperCase(bytes[i]);
                }
            } else {
                if (Character.isSpaceChar(bytes[i-1]) && Character.isLetter(bytes[i])) {
                    bytes[i] = (byte) Character.toUpperCase(bytes[i]);
                }
            }
        }

        return new String(bytes);
    }
}