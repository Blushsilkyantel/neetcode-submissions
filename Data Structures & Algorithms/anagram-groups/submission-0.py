class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            alpha = {}

            for char in s:
                alpha[char] = alpha.get(char, 0) + 1

            # Sort the items so equivalent maps create the same key
            key = tuple(sorted(alpha.items()))

            groups[key].append(s)

        return list(groups.values())


        