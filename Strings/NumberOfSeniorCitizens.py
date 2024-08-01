class Solution:
    def countSeniors(self, details: List[str]) -> int:
        age = []
        for i in details:
            age.append(int(i[11:13]))
        
        count = 0
        for i in age:
            if i > 60:
                count += 1

        return count
