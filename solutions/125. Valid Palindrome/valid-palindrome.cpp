class Solution {
    public: bool isPalindrome(string s) {
        int l = 0;
        int r = s.length() - 1;

        while (l < r) {
            if (isalnum(s[l]) && isalnum(s[r])) {
                if (tolower(s[l]) != tolower(s[r])) return false;

                l++;
                r--;
            } else if (isalnum(s[l])) {
                r--;
            } else {
                l++;
            }
        }

        return true;
    }
};
