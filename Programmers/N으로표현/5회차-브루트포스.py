def solution(n, number):
    def f():
        if n == number:
            return 1
        nums=[]
        for i in range(1,9):
            nums.append(set({int(str(n)*i)}))
        for i in range(1,8):
            for j in range(i):
                for k in nums[j]:
                    for l in nums[i-1-j]:
                        nums[i].add(k+l)
                        nums[i].add(k-l)                        
                        nums[i].add(k*l)     
                        if l!=0:
                            nums[i].add(int(k/l))
            if number in nums[i]:
                return i+1
            
        return -1
    return f()