# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
# You can use each character in text at most once. Return the maximum number of instances that can be formed.


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        """
        Time: O(N) - Looping through the N letters in text.
        Space: O(1) - Dict only contains 5 keys.
        """
        # Store the number of times each letter in "balloon" shows up in the text.
        balloon_freq = {"b":0, "a":0, "l":0, "o":0, "n":0}
        for letter in text:
            if letter in balloon_freq:
                balloon_freq[letter] += 1
        # L and O show up twice in the word balloon.
        # Divide their freq by 2 to find how many times the word Balloon can be made with them.     
        balloon_freq["l"] //= 2
        balloon_freq["o"] //= 2
        # Balloon can only be spelled as many times as its least occuring letter.
        return min(balloon_freq.values())
