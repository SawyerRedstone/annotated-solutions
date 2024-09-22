# A pangram is a sentence where every letter of the English alphabet appears at least once.
# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        """ 
        Time: O(n) - Making a set from the n letters in sentence.
        Space: O(1) - At most, set will contain 26 elements, one for each letter.
        """
        # A pangram contains 26 unique letters.
        return len(set(sentence)) == 26
