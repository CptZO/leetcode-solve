class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss = defaultdict(int)
        for w, l in matches:
            loss[w] += 0
            loss[l] += 1

        undefeated = []
        for player, lost in loss.items():
            if lost == 0:
                undefeated.append(player)
        lostexone = []
        for player, lost in loss.items():
            if lost == 1:
                lostexone.append(player)
        return [sorted(undefeated), sorted(lostexone)]
