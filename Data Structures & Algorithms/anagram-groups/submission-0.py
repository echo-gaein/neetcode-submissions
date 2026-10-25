class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for x in strs:
            category = [0] * 26

            for char in x:
                index = ord(char) - ord("a")
                category[index] += 1
            
            res[tuple(category)].append(x)
        
        return list(res.values())
