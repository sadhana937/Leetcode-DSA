class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = 0
        while students and sandwiches:
            if sandwiches[0] not in students:
                break
            if students[0] == sandwiches[0]:
                count += 1
                students.remove(students[0])
                sandwiches.remove(sandwiches[0])
            else:
                temp = students[0]
                students.remove(temp)
                students.append(temp)

        return len(students)

            
