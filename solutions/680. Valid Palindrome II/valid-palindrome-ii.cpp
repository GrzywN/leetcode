class Solution {
    public: bool validPalindrome(string s) {
        int l = 0;
        int r = s.length() - 1;

        while (l < r) {
            if (s[l] != s[r]) {
                bool skipped_left = Solution::is_palindromic(s, l + 1, r);
                bool skipped_right = Solution::is_palindromic(s, l, r - 1);

                if (skipped_left || skipped_right) {
                    return true;
                } else {
                    return false;
                }
            }

            l++;
            r--;
        }

        return true;
    }

    bool is_palindromic(string s, int l, int r) {
        while (l < r) {
            if (s[l] != s[r]) {
                return false;
            }

            l++;
            r--;
        }

        return true;
    }
};
