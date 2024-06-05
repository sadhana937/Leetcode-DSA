class Solution1:
    def commonChars(self, words: List[str]) -> List[str]:
        # Initialize the counter with the character counts of the first word
        common_count = Counter(words[0])

        # Iterate through the rest of the words
        for word in words[1:]:
            # Update the counter with the intersection of the current common count and the new word's count
            common_count &= Counter(word)

        # Expand the characters based on their counts and return the result as a list
        result = list(common_count.elements())
        return result


class Solution2:
    def commonChars(self, words: List[str]) -> List[str]:
        possiblity = list(words[0])
        n = len(words)

        aux = [0] * n

        for i in range(len(words)):
            aux[i] = list(words[i])
        
        for char in words[0]:
            count = 0
            for auxy in aux:
                if char in auxy:
                    count += 1
                    auxy.remove(char)
            
            if count != n:
                possiblity.remove(char)
            count = 0
        

        return possiblity
