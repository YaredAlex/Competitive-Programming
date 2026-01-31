class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        # linear search algorithm
        for char in letters:
            if ord(char)>ord(target):
                return char
        return letters[0]