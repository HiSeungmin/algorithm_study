# Group Anagrams
from collections import defaultdict

def groupAnagrams(strs):
    
    anagrams = defaultdict(list)
    
    for str in strs:
        key_str = ''.join(sorted(str))
        anagrams[key_str].append(str)
    
    return list(anagrams.values())
    
    
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    