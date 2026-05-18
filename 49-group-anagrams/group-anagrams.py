from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[List[str]]]:
        # I'll use a dictionary where the key is the sorted version of the word.
        # All anagrams, when sorted, will look exactly the same.
        anagram_groups = defaultdict(list)
        
        for s in strs:
            # Sort the string to create a unique "signature" for the anagram group.
            # We join it back into a string because lists can't be used as dictionary keys.
            sorted_key = "".join(sorted(s))
            
            # Add the original word to its corresponding group
            anagram_groups[sorted_key].append(s)
            
        # We just need to return the grouped lists
        return list(anagram_groups.values())