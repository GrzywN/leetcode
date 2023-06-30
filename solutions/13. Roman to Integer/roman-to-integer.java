class Solution {
    public int romanToInt(String s) {
        Map<Character, Integer> romanToInt = Map.of(
            'I', 1,
            'V', 5,
            'X', 10,
            'L', 50,
            'C', 100,
            'D', 500,
            'M', 1000
        );

        int result = 0;

        for (int i = 0, n = s.length(); i < n; i++) {
            boolean isNextLetterAvailable = i + 1 < n;
            int currentValue = romanToInt.get(s.charAt(i));
            int nextValue = isNextLetterAvailable ? romanToInt.get(s.charAt(i + 1)) : 0;

            if (currentValue < nextValue) {
                result -= currentValue;
            } else {
                result += currentValue;
            }
        }

        return result;
    }
}
