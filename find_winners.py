# You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.
# Return a list answer of size 2 where:
# answer[0] is a list of all players that have not lost any matches.
# answer[1] is a list of all players that have lost exactly one match.
# The values in the two lists should be returned in increasing order.


from collections import defaultdict

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        """
        Time: O(nlogn) - Looping through list is O(n). Sorting keys is O(nlogn). O(n + nlogn) == O(nlogn).
        Space: O(n) - loss_count dict contains all n players.
        """
        # Keep track of how many times each player lost.
        loss_count = defaultdict(int)
        for winner, loser in matches:
            # Make sure winner is in dict without changing how many times they've lost.
            loss_count[winner] += 0
            loss_count[loser] += 1
            
        # Now that dict is created, use it to find answer.
        no_loss = []
        one_loss = []
        # Sort keys so answer will be in increasing order.
        for player in sorted(loss_count.keys()):
            if loss_count[player] == 0:
                no_loss.append(player)
            elif loss_count[player] == 1:
                one_loss.append(player)
                
        return [no_loss, one_loss]
        
