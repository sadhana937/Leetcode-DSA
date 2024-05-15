class Solution1:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(x) for x in version1.split('.')]
        v2 = [int(x) for x in version2.split('.')]

        # Extend the shorter version list with zeros to match the length of the longer one
        max_len = max(len(v1), len(v2))
        v1.extend([0] * (max_len - len(v1)))
        v2.extend([0] * (max_len - len(v2)))

        # Compare each corresponding part of the version numbers
        for i in range(max_len):
            if v1[i] < v2[i]:
                return -1
            elif v1[i] > v2[i]:
                return 1
        
        return 0

class Solution2:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')

        m = len(v1)
        n = len(v2)
        i, j = 0, 0

        while i < m and j < n:
            if int(v1[i]) < int(v2[j]):
                return -1
            elif int(v1[i]) > int(v2[j]):
                return 1
            else:
                i += 1
                j += 1
        
        while i < m and int(v1[i]) == 0:
            i += 1
        if i < m:
            return 1
        
        while j < n and int(v2[j]) == 0:
            j += 1
        if j < n:
            return -1
        
        return 0

class Solution3:
    def compareVersion(self, version1: str, version2: str) -> int:
        n = len(version1)
        m = len(version2)
        i, j = 0, 0
        
        while i < n and j < m:
            if version1[i] == '.':
                i += 1
                while i < m and version1[i] == '0':
                    i += 1

            if version2[j] == '.':
                j += 1
                while j < n and version2[j] == '0':
                    j += 1

            str1 = ''
            str2 = ''

            while i < n and version1[i] != '.':
                str1 += str(version1[i])
                i += 1

            while j < m and version2[j] != '.':
                str2 += str(version2[j])
                j += 1

            if int(str1) < int(str2):
                return -1
            elif int(str1) > int(str2):
                return 1
            else:
                i += 1
                j += 1

        
        while i < n and (version1[i] == '0' or version1[i] == '.'):
            i += 1

        if i < n:
            return 1
        
        while j < m and (version2[j] == '0' or version2[j] == '.'):
            j += 1

        if j < m:
            return -1
        
        return 0
