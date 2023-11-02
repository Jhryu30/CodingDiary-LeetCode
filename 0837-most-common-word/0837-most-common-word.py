from collections import defaultdict

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        my_dict = defaultdict(int)
        
        paragraph_word = []
        for para in paragraph.lower().split(' '):
          para_temp = [p for p in para.split(',') if len(p)>0]
          paragraph_word += para_temp
          
        for para in paragraph_word:
            word_lst = [p for p in para.lower() if p.isalnum()]
            word = ''.join(word_lst)
            my_dict[word] += 1

        for banned_word in banned:
            my_dict[banned_word] = 0

        my_word = [[w,c] for w,c in my_dict.items()]
        my_word.sort(key=lambda x:x[1], reverse=True)
        
        answer = my_word[0][0]

        return answer