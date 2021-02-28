def solution(tickets):
    memo = dict()

    for start,dest in tickets:
        if start not in memo:
            memo[start] = [dest]
        else :
            memo[start].append(dest)

    for k in memo.keys():
        memo[k].sort(reverse=True)
    st=['ICN']
    answer = []
    while st:
        top = st[-1]
        if top not in memo or len(memo[top]) == 0:
            answer.append(st.pop())
        else:
            st.append(memo[top].pop())


    answer.reverse()

    return answer