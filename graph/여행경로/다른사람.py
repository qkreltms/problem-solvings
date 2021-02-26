# https://programmers.co.kr/questions/10332
import copy


def solution(tickets):

    print(f"tickets is {tickets}")
    route_lst = []
    for i in range(len(tickets)):
        route = []
        visited = [False] * len(tickets)
        if tickets[i][0] == "ICN":
            route.extend(tickets[i])
            dfs(tickets, i, visited, route, route_lst)

    answer = min(route_lst)

    return answer


def dfs(tickets, idx, visited, route, route_lst):
    #current = tickets[idx]
    visited[idx] = True

    #print(f" len(route) is {len(route)} and len(tickets)+1 {len(tickets)+1}")
    if len(route) == len(tickets)+1:
        if route:
            route_copy = copy.deepcopy(route)
            route_lst.append(route_copy)
        return

    for i in range(len(tickets)):
        # 시작[1]에 맞는 데이터를 찾는다.
        if route[len(route)-1] == tickets[i][0] and visited[i] == False:

            route.extend([tickets[i][1]])

            dfs(tickets, i, visited, route, route_lst)
            route.pop()
            visited[i] = False

# print(solution([['ICN', 'BOO'], ['ICN', 'COO'], ['COO', 'DOO'], ['DOO', 'COO'], [
#       'BOO', 'DOO'], ['DOO', 'BOO'], ['BOO', 'ICN'], ['COO', 'BOO']]), 
#       "\n 답:",['ICN', 'BOO', 'DOO', 'BOO', 'ICN', 'COO', 'DOO', 'COO', 'BOO'])
print(solution([['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], [
      'ATL', 'SFO']]), "\n['ICN', 'ATL', 'ICN', 'SFO', 'ATL', 'SFO']")