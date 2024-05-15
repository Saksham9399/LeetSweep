class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a","e","i","o","u","A","E","I","O","U"]
        vowels_list = []
        final_list = []
        for char in s:
            if char in vowels:
                vowels_list.append(char)
        for vowel in s:
            if vowel in vowels:
                final_list.append(vowels_list.pop())
            else:
                final_list.append(vowel)
        s = "".join(final_list)
        return s



        