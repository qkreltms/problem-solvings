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
def solution(tickets):
    table = {}
    for key, value in tickets:
        if key in table:
            table[key].append(value)
        else:
            table[key] = [value]
        table[key].sort()

    copiedTable = copy.deepcopy(table)
    for _ in range(len(table['ICN'])):
        ans = []
        queue = ['ICN']
        while queue:
            key = queue.pop(0)
            ans.append(key)
            if key in copiedTable and copiedTable[key]:
                item = ''
                if 'ICN' in copiedTable[key]:
                    item = copiedTable[key].pop(table[key].index('ICN'))
                else:
                    item = copiedTable[key].pop(0)
                queue.append(item)
            else:
                flag = False
                for _, v in copiedTable.items():
                    if v:
                        copiedTable = copy.deepcopy(table)
                        copiedTable['ICN'].append(copiedTable['ICN'].pop(0))
                        flag = True
                        break
                if not flag:
                    return ans


# print(solution([["ICN", "JFK"], ['HND', 'IAD'], ['JFK', 'HND']]),
#       "\n['ICN', 'JFK', 'HND', 'IAD']")
# print(solution([['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], [
#       'ATL', 'SFO']]), "\n['ICN', 'ATL', 'ICN', 'SFO', 'ATL', 'SFO']")
# print(solution([['ICN', 'B'], ['B', 'ICN'], ['ICN', 'A'], [
#       'A', 'D'], ['D', 'A']]), "\n['ICN', 'B', 'ICN', 'A', 'D', 'A']")


# print('출발지와 도착지가 같은게 여러개일 경우')
# print(solution([['ICN', 'SFO'], ['SFO', 'ICN'], ['ICN', 'SFO'],
#                 ['SFO', 'JFK']]), "\n['ICN', 'SFO', 'ICN', 'SFO', 'JFK']")

# print('ICN을 항상 먼저 방문한다.')
# print(solution([['ICN', 'A'], ['ICN', 'A'], ['A', 'ICN'],
#                 ['A', 'C']]), "\n['ICN', 'A', 'ICN', 'A', 'C']")
# print(solution([['ICN', 'A'], ['A', 'ICN'], ['A', 'B'],
#                 ['ICN', 'A']]), "\n['ICN', 'A', 'ICN', 'A', 'B']")

# print('출발지가 항상 첫번째 인덱스는 아니다.')
# print(solution([['ICN', 'A'], ['ICN', 'B'], ['B', 'ICN']]),
#       "\n['ICN', 'B', 'ICN', 'A']")
# print(solution([['ICN', 'A'], ['A', 'C'], ['ICN', 'B'], ['B', 'ICN']]),
#       "\n['ICN', 'B', 'ICN', 'A', 'C']")
# print(solution([['ICN', 'BBB'], ['AAA', 'ICN'], ['ICN', 'AAA']]),
#       "\n['ICN', 'AAA', 'ICN', 'BBB']")
# print(solution([['ICN', 'ABB'], ['AAA', 'ICN'], ['ICN', 'AAA'], ['ICN', 'ADD'], [
#       'ABB', 'ICN']]), "\n['ICN', 'AAA', 'ICN', 'ABB', 'ICN', 'ADD']")

# print(solution([['ICN', 'AAA'], ['ICN', 'AAA'], ['AAA', 'ICN'],
#                 ['AAA', 'CCC']]), "\n['ICN', 'AAA', 'ICN', 'AAA', 'CCC']")
# print(solution([['ICN', 'AAA'], ['ICN', 'AAA'], ['ICN', 'AAA'],
#                 ['AAA', 'ICN'], ['AAA', 'ICN']]), "\n['ICN', 'AAA', 'ICN', 'AAA', 'ICN', 'AAA']")

print(solution([['ICN', 'BOO'], ['ICN', 'COO'], ['COO', 'DOO'], ['DOO', 'COO'], [
      'BOO', 'DOO'], ['DOO', 'BOO'], ['BOO', 'ICN'], ['COO', 'BOO']]), ['ICN', 'BOO', 'DOO', 'BOO', 'ICN', 'COO', 'DOO', 'COO', 'BOO'])
