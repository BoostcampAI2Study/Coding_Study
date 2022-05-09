"""
TOPOLOGY SORT: BFS using queue
"""
import collections, sys
N, M = map(int, sys.stdin.readline().rstrip().split())
in_degree, ADJ_GRAPH = [0]*(N+1), collections.defaultdict(list)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    ADJ_GRAPH[a].append(b)
    in_degree[b] += 1

def topology_sort():
    global N, in_degree, ADJ_GRAPH
    SORTED_STUDENTS, queue = [], collections.deque()

    for student_node in range(1, N+1):
        if in_degree[student_node] == 0: queue.append(student_node)
    
    for _ in range(N):
        if len(queue) == 0: raise Exception('Not DAG; a cycle exists, cannot do topology sort.')

        student_node = queue.popleft()
        SORTED_STUDENTS.append(str(student_node))
        for following_student_node in ADJ_GRAPH[student_node]:
            in_degree[following_student_node] -= 1
            if in_degree[following_student_node] == 0: queue.append(following_student_node)
    print(' '.join(SORTED_STUDENTS))

topology_sort()


"""
TOPOLOGY SORT: DFS using stack
"""
import collections, sys
N, M = map(int, sys.stdin.readline().rstrip().split())
ADJ_GRAPH = collections.defaultdict(list)
visited, STACK = [False]*(N+1), []

for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    ADJ_GRAPH[a].append(b)

def topology_sort(student_node):
    global N, ADJ_GRAPH, visited, STACK

    visited[student_node] = True

    for following_student_node in ADJ_GRAPH[student_node]:
        if not visited[following_student_node]:
            topology_sort(following_student_node)
    
    STACK.append(str(student_node))

for student_node in range(1, N+1):
    if not visited[student_node]:
        topology_sort(student_node)
print(' '.join(reversed(STACK)))
