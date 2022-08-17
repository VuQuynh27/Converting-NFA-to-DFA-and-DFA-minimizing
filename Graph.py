from collections import defaultdict


# Class biểu diễn 1 đồ thị có hướng, không trọng số
# sử dụng biểu diễn danh sách kề
class Graph:

    def __init__(self):
        # dùng default dictionary để lưu trữ đồ thị
        self.reachable_states = []
        self.graph = defaultdict(list)

    # hàm thêm cạnh vào đồ thị
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # hàm in BFS của đồ thị
    def BFS(self, s):

        # đánh dấu tất cả các đỉnh là chưa được thăm (not visited)
        visited = [False] * (max(self.graph) + 1)

        # tạo queue cho BFS
        queue = []

        # đánh dấu đỉnh bắt đầu là visited và enqueue đỉnh này
        queue.append(s)
        visited[s] = True

        while queue:

            # Dequeue 1 đỉnh từ queue và in ra
            s = queue.pop(0)
            self.reachable_states.append(s)
            # print (s, end = " ")

            # lấy tất cả đỉnh kề của đỉnh s được dequeu.
            # nếu đỉnh kề chưa được thăm (visited),
            # đánh dấu là visited và enqueue nó.
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True