class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        if len(A) < 2:
            return 0
        if len(B) < 2:
            return 0
        x = A[0]
        y = B[0]
        steps = 0

        for i in range(1, len(A)):
            x_next = A[i]
            y_next = B[i]
			# since we can travel diagonally, we can cover 1 x and 1 y distance in a single diagonal step.
            # hence steps required to go from point(x,y) to point (x_next, y_netx) is the maximum of x coordinate difference or y coordinate difference.			
            steps += max (abs(x - x_next), abs(y-y_next))
            x = x_next
            y = y_next

        return steps