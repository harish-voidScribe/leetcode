class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        res = 0
        score = 0
        l, r = 0, len(tokens) - 1
        while l <= r:
            if tokens[l] <= power:
                score += 1
                power -= tokens[l]
                l += 1
            elif score:
                score -= 1
                power += tokens[r]
                r -= 1
            else:
                return res
            res = max(res, score)
        return res