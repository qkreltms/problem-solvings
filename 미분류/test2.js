function solution(k, rates) {
    let ans=0
    function f(rate,s,hasDollar,cnt) {
        if(rate > s && !hasDollar) {
            return
        }
        if (!hasDollar) {
            s-=rate
            hasDollar=true
        } else {
            s+=rate
            hasDollar=false
        }
        if (cnt===rates.length) {
            ans=Math.max(ans,s)
            return
        }
        let t= rates.slice(cnt)
        t.forEach((i, index) => {
            f(i,s,hasDollar,index+1+cnt)
        }) 
    }
    let cnt=0
    for(let i of rates) {
        f(i, k, false,cnt+=1)
    }
    // 이익을 낼 수 없을 경우
    if (ans < k) {
        return k
    }
    return ans
}

solution(1000, [1200, 1000, 1100, 1200, 900, 1000, 1500, 900, 750, 1100])
solution(1000, [1200, 1000, 1100, 1200])
solution(1500, [1500, 1400, 1300, 1200])