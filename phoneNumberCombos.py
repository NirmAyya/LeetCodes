
'''
Given a string containing digits from 2-9 inclusive, return all 
possible letter combinations that the number could represent. Return the answer in any order.
A mapping of digit to letters (just like on the telephone buttons) 
is given below. Note that 1 does not map to any letters.
'''


class Solution:
    def letterCombinations(self, D: str) -> List[str]:
        # store length of given word, and make a list to story combos
        lenD, ans = len(D), []
        #if given empty string return empty list
        if D == "": return []
        #iteratre through the combos
        def bfs(pos: int, st: str):
            if pos == lenD: ans.append(st)
            else:
                letters = L[D[pos]]
                for letter in letters:
                    bfs(pos+1,st+letter)
        bfs(0,"")
        return ans