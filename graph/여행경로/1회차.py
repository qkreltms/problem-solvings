# 문제
'''
항상 ICN에서 출발하는 항공편이있다
항공권 정보가 담긴 2차원 배열 tickets가 주어진다.
값은 [[ICN, JFK], [HND, IAD], [JFK, HND]]와 같다.
이 때 아래와 같이 경로를 출력하라
ICN => JFK => HND => IAD

제한사항
주어진 항공권은 모두 사용해야 합니다.
만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.
'''
# 풀이 법
'''
값이 들어오면
이차원 배열에 key, value형식으로 저장해 놓는다. value는 누적된다.

다 끝나면 key를 돌면서 value를 정렬한다.

queue에 ICN를 넣는다.
ICN를 팝하고 ans에 append한다.
ICN의 value중 [0] 번째 값을 pop한 후 queue에 넣는다.
queue가 빌 때까지 반복한다.
'''


def solution(tickets):
    table = {}
    for key, value in tickets:
        if key in table:
            table[key].append(value)
        else:
            table[key] = [value]

    for _, values in table.items():
        values.sort()

    ans = []
    queue = [["ICN", "ICN"]]
    while queue:
        key, parent = queue.pop(0)
        ans.append(key)
        if key in table and table[key]:
          queue.append([table[key].pop(0), key])
        elif table[parent]:
          queue.append([table[parent].pop(0), parent])
    
    # for i, a in enumerate(ans, start=1):
    #   if a == "ICN" and (i)%2==0:
    #     temp = ans[i-2]
    #     ans[i-2] = "ICN"
    #     ans[i-1] = temp

    return ans


print(solution([["ICN", "JFK"], ['HND', 'IAD'], ['JFK', 'HND']]), "\n['ICN', 'JFK', 'HND', 'IAD']")
print(solution([['ICN','SFO'],['ICN','ATL'],['SFO','ATL'],['ATL','ICN'],['ATL','SFO']]), "\n['ICN', 'ATL', 'ICN', 'SFO', 'ATL', 'SFO']")
print(solution([['ICN','SFO'],['ICN','ATL']]), "\n['ICN', 'ATL', 'SFO']")
print(solution([['ICN','JFK'],['JFK','NYC'], ['JFK','CNN'], ['JFK', 'ZZZ']]), "\n['ICN', 'JFK', 'CNN', 'NYC', 'ZZZ']")
print(solution([['ICN','A'],['ICN','B'], ['B','ICN']]), "\n['ICN', 'A', 'ICN', 'B']")
print(solution([['ICN','A'],['ICN','A'], ['A','ICN'], ['A', 'C']]), "\n['ICN', 'A', 'ICN', 'A', 'C']")
