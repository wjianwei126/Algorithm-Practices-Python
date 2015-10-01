# given a list of tasks and a cooldown time, the same task can not be done within a shorter
# period of the cooldown time. Return the time needed to handle all the tasks
# e.g. tasks [1,2,1,2] cooldown 3  output:[1,2,_,_,1,2] => 6

class Solution:
    def taskCooldown(self, tasks, cooldown):
    	"O(n) time, O(n) space" 
        if not tasks or len(tasks) == 0: return 0
        _dict = {}
        totaltime = 0
        for i in range(len(tasks)):
            if tasks[i] in _dict:
                if totaltime - _dict[tasks[i]] > cooldown:
                    _dict[tasks[i]] = totaltime
                else:
                    totaltime = cooldown + _dict[tasks[i]] + 1
                    _dict[tasks[i]] = totaltime
            else:
                _dict[tasks[i]] = totaltime
            totaltime += 1
        return totaltime
    def usingQ(self, tasks, cooldown):
    	"O(n) time, O(cooldown) space"
        if not tasks or len(tasks) == 0: return 0
        queue = []
        i = 0
        total = 0
        while i < len(tasks):
            if len(queue) == 0 or tasks[i] not in queue:
                queue.append(tasks[i])
                total += 1
                i += 1
            else:
                queue.append(None)
                total += 1
            
            if len(queue) > cooldown:
                queue.pop(0)
        return total
        

if __name__ == "__main__":
    
    A = [1,2,1,2]
    cooldown = 3
    
    solu = Solution()
    print solu.taskCooldown(A, cooldown)
    print solu.usingQ(A, cooldown)