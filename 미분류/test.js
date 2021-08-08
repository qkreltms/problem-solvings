function solution(money, cost) {
    let si=0
    let ei=0
    let s=0
    let ans=0
    while(true) {
        if (s<=money) {
            ans=Math.max(ans,ei-si)
            s+=cost[ei]
            if (ei===cost.length) {
                return ans
            }
            ei+=1
        }
        else if(si===cost.length) {
            return ans
        }
        else {
            s-=cost[si]
            si+=1
            ei=si
        }
    }
}

solution(420, [0, 900, 0, 200, 150, 0, 30, 50])