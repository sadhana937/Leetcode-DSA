'''
This code doesn't work for testcase -> "SSSPPPSPPSPSSSSSSPPPSPP" and
"SSPSSSPSSSPPSPSSPPPPPSPSSPPPPPSPSSPSPPPPPSPSPSSSPSPSSSPPPPPPPSSPSSSPPSPSPSPPSPSPPPSPPSSPSSSPPSPPSPPPPPSPSPSPPSPPPSPPSSPSSPPPSSPSPSPPSPSSSPSPPSPPSSPPSSPPPPSSSPPSSSPSPPSSPPPPPSSPSSPSSPSPSSSSPSSPPSSPPPPSSSPPSSPPPSPSSSSPSPSPSPPSSPSSSSPSSPPPPPPSSSPPSPPSPSPSPSPSPPPSPSSPPPPSSSSPSSPSSPSPSSSSSPPPSSPSSPPSPSSSSSPSPPPPPPPSSPPSPSSPSSSSPPSSPPSPSSPSSSPSPSPPPPPSPSSPSSPPPSSSPPPPSPSSSPSSSPSPSSPPSSSSPPPSPSPPPSSSPSPSPPPPPPPSPPPSSSSPSPPPPPSSSPSSSSSPSPPPSPPSPPSSPSSSPPSSSPSSPPSSPPPPPSPSSPPSPSSSPSPSPPSPSPPSPPSPSSSPPPSPSPPPPPPS...

class Solution:
    def numberOfWays(self, corridor: str) -> int:
        num_of_seats = corridor.count('S')
        if num_of_seats < 2:
            return 0
        elif num_of_seats == 2:
            return 1
        
        s_prev_index = 0
        s_count = 0
        answer = 0
        for i in range(len(corridor)):
            if corridor[i] == 'S' and s_count == 0:
                s_count += 1
            elif corridor[i] == 'S' and s_count == 1:
                s_count += 1
                s_prev_index = i
            elif corridor[i] == 'S' and s_count == 2:
                s_count = 1
                answer = (answer + i - s_prev_index) % (10 ** 9 + 7)
                s_prev_index = i

        return answer % (10 ** 9 + 7)
                
'''

class Solution:
    def numberOfWays(self, corridor: str) -> int:
        # Store 1000000007 in a variable for convenience
        MOD = 1_000_000_007

        # Initial values of three variables
        zero = 0
        one = 0
        two = 1

        # Compute using derived equations
        for thing in corridor:
            if thing == "S":
                zero = one
                one, two = two, one
            else:
                two = (two + zero) % MOD

        # Return the result
        return zero
