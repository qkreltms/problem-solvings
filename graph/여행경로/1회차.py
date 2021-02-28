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
#1
값이 들어오면
이차원 배열에 key, value형식으로 저장해 놓는다. value는 누적된다.

다 끝나면 key를 돌면서 value를 정렬한다.

queue에 ICN를 넣는다.
ICN를 팝하고 ans에 append한다.
ICN의 value중 [0] 번째 값을 pop한 후 queue에 넣는다.
queue가 빌 때까지 반복한다.

#2
이 문제는 일반적인 DFS,BFS알고리즘을 사용해야 될 뿐만아니라
백트레킹을 사용해야한다. 키워드는 "모든 도시를 방문할 수 없는 경우는 주어지지  않습니다."
이 말은 갈수 있는 모든 경로를 찾고 그 중 알파벳정렬 순인것을 반환해야한다. 
또한 dic으로 저장해놓는 형태보다 배열을 모두 순회하며 visited 체크를 해야한다.
'''




import copy
def dfs(ticket, paths, tickets):
    global ans, visited
    # 주어진 경로를 다 순회했다.
    if len(paths) == len(tickets):
        # 마지막 값은 더 이상 순회할 수 없으므로 바로 넣어준다.
        ans.append(copy.deepcopy([*paths, ticket]))
        return

    for j in range(0, len(tickets)):
        # 주어진 키 값이 일치하면 갈 경로를 찾았다.
        if tickets[j][0] == ticket and visited[j] == False:
            # 키 값을 갈 경로에 추가한다.
            visited[j] = True
            paths.append(ticket)
            dfs(tickets[j][1], paths, tickets)
            # 백트레킹
            visited[j] = False
            paths.pop()


def solution(tickets):
    global visited, ans
    ans = []
    visited = [False for _ in range(len(tickets))]

    dfs('ICN', [], tickets)
    return min(ans)


print(solution([["ICN", "JFK"], ['HND', 'IAD'], ['JFK', 'HND']]),
      "\n",['ICN', 'JFK', 'HND', 'IAD'])
print(solution([['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], [
      'ATL', 'SFO']]), "\n",['ICN', 'ATL', 'ICN', 'SFO', 'ATL', 'SFO'])
print(solution([['ICN', 'B'], ['B', 'ICN'], ['ICN', 'A'], [
      'A', 'D'], ['D', 'A']]), "\n",['ICN', 'B', 'ICN', 'A', 'D', 'A'])
print(solution([['ICN', 'SFO'], ['SFO', 'ICN'], ['ICN', 'SFO'],
                ['SFO', 'JFK']]), "\n",['ICN', 'SFO', 'ICN', 'SFO', 'JFK'])
print(solution([['ICN', 'A'], ['ICN', 'A'], ['A', 'ICN'],
                ['A', 'C']]), "\n",['ICN', 'A', 'ICN', 'A', 'C'])
print(solution([['ICN', 'A'], ['A', 'ICN'], ['A', 'B'],
                ['ICN', 'A']]), "\n",['ICN', 'A', 'ICN', 'A', 'B'])
print(solution([['ICN', 'BBB'], ['AAA', 'ICN'], ['ICN', 'AAA']]),
      "\n",['ICN', 'AAA', 'ICN', 'BBB'])
print(solution([['ICN', 'ABB'], ['AAA', 'ICN'], ['ICN', 'AAA'], ['ICN', 'ADD'], [
      'ABB', 'ICN']]), "\n",['ICN', 'AAA', 'ICN', 'ABB', 'ICN', 'ADD'])
print(solution([['ICN', 'AAA'], ['ICN', 'AAA'], ['AAA', 'ICN'],
                ['AAA', 'CCC']]), "\n",['ICN', 'AAA', 'ICN', 'AAA', 'CCC'])
print(solution([['ICN', 'AAA'], ['ICN', 'AAA'], ['ICN', 'AAA'],
                ['AAA', 'ICN'], ['AAA', 'ICN']]), "\n", ['ICN', 'AAA', 'ICN', 'AAA', 'ICN', 'AAA'])
# 출발지가 항상 첫번째 인덱스는 아니다.
print(solution([['ICN', 'A'], ['ICN', 'B'], ['B', 'ICN']]),
      "\n", ['ICN', 'B', 'ICN', 'A'])
print(solution([['ICN', 'A'], ['A', 'C'], ['ICN', 'B'], ['B', 'ICN']]),
      "\n", ['ICN', 'B', 'ICN', 'A', 'C'])
# 백트래킹으로 구현되어있는가?
print(solution([['ICN', 'BOO'], ['ICN', 'COO'], ['COO', 'DOO'], ['DOO', 'COO'], [
      'BOO', 'DOO'], ['DOO', 'BOO'], ['BOO', 'ICN'], ['COO', 'BOO']]), "\n", ['ICN', 'BOO', 'DOO', 'BOO', 'ICN', 'COO', 'DOO', 'COO', 'BOO'])
