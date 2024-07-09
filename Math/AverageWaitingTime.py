class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        average = 0
        cur = customers[0][0]
        for arrival, time in customers:
          # if the customer has already arrived
            if arrival <= cur:
                average += (cur + time) - arrival
                cur += time
            else:
              # if the customer arrives when the chef is idle
                average += time
                cur = arrival + time
        return average / len(customers)
            

        
