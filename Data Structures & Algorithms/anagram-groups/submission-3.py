class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        dictionary = {}
        for string in strs:
            count = [0] * 26
            for char in string:
                index = ord(char) - ord('a')
                count[index] += 1
            
            key = tuple(count)
            if key in dictionary.keys():
                dictionary[key].append(string)
            else:
                new = []
                new.append(string)
                dictionary[key] = new

        for key in dictionary:
            answer.append(dictionary[key])
        return answer