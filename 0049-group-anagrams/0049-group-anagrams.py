from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        my_dict = defaultdict(list)

        for word in strs:
            my_dict[''.join(sorted(word))].append(word)
        
        answer = list(my_dict.values())
        

        return answer