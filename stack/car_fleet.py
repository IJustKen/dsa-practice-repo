# logic is as follows: the car at the very front is a possible fleet leader. It takes t time to reach target
# if within that t time the car behind reaches it, it becomes part of the fleet too. So assuming it catches up within that time. This means that
# the time taken by that car to reach the target is bounded by the time taken by the car ahead. So now for the next car behind too, we check from the
# leader's POV, if again it can reach target before leader reaches target, then it will become part of the fleet.

# but if the car behind will not catch up with the leader in t time, then it is itself a leader and potentially block others behind
# so this is a new fleet leader and so on
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = len(speed)  # initially there are as many fleets as cars
        cars = list(zip(position, speed))  # this pairs up position and corresponding speed and gives an object with (position, speed) pairs
        cars.sort()  # then i sorted it 
        
        leader_finish_time = (target - cars[-1][0])/cars[-1][1]  # time taken by fleet leader to reach target
      
        for i in range(len(speed)-2,-1,-1):
            curr_finish_time = (target - cars[i][0])/cars[i][1]  # time taken by current car to reach target
            if curr_finish_time <= leader_finish_time:  # if the curr one, can reach the leader before or on that time, it becomes part of the fleet
                res -= 1  # hence decrement
            else:
                leader_finish_time = curr_finish_time  # otherwise if it cannot reach, it won't be part of the fleet in front of it, rather it is itself a fleet leader now
        
        return res

# Stack approach (takes a stack to track fleets), basically whenever a new fleet leader is discovered we push it to the stack that is all
# previous approach actually faster cuz we are just maintaining the one variable leader finish time.
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort()

        fleets = [cars[-1]]    # tracks number of fleets leaders, thus number of fleets

        for i in range(len(speed)-2,-1,-1):
            curr_finish_time = (target - cars[i][0])/cars[i][1]
            leader_finish_time = (target - fleets[-1][0])/fleets[-1][1]    # current fleet leader is the latest pushed car in the fleets stack
            if curr_finish_time > leader_finish_time:
                fleets.append(cars[i])
        
        return len(fleets)
