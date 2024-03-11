class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counts = Counter(s)
        ordered_set = set(order)
        first = []
        second = []
        for char in order:
            if char in counts:
                first.append(char * counts[char])
        for key, val in counts.items():
            if key not in ordered_set:
                second.append(key * val)
        return ''.join(first) + ''.join(second)