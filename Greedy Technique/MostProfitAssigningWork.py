class Solution1:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        output = 0
        diff_prof = [(difficulty[i], profit[i]) for i in range(len(profit))]
        diff_prof.sort(key = lambda x: x[1])
        for person in worker:
            max_prof = 0
            for i in range(len(diff_prof) - 1, -1, -1):
                if person >= diff_prof[i][0]:
                    output += diff_prof[i][1]   
                    break             
        return output


class Solution2:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # Step 1: Combine and sort the jobs by difficulty
        jobs = sorted(zip(difficulty, profit))
        
        # Step 2: Create a max profit array for each difficulty level
        max_profit = []
        max_so_far = 0
        for d, p in jobs:
            max_so_far = max(max_so_far, p)
            max_profit.append((d, max_so_far))
        
        # Step 3: Sort the workers
        worker.sort()
        
        # Step 4: Calculate the total profit using binary search
        total_profit = 0
        j = 0  # Pointer for max_profit
        
        for w in worker:
            # Use binary search to find the right job for the current worker
            while j < len(max_profit) and w >= max_profit[j][0]:
                j += 1
            if j > 0:
                total_profit += max_profit[j-1][1]
        
        return total_profit
