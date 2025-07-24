from typing import List
import sys
sys.setrecursionlimit(10000)

class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        from collections import defaultdict
        
        n = len(nums)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        xor_subtree = [0] * n
        time_in = [0] * n
        time_out = [0] * n
        timer = [0]

        def dfs(node, parent):
            xor_val = nums[node]
            timer[0] += 1
            time_in[node] = timer[0]
            for neighbor in graph[node]:
                if neighbor != parent:
                    dfs(neighbor, node)
                    xor_val ^= xor_subtree[neighbor]
            xor_subtree[node] = xor_val
            timer[0] += 1
            time_out[node] = timer[0]

        dfs(0, -1)
        total_xor = xor_subtree[0]
        min_score = float('inf')

        edge_nodes = []

        def collect_edges(node, parent):
            for neighbor in graph[node]:
                if neighbor != parent:
                    edge_nodes.append((node, neighbor))
                    collect_edges(neighbor, node)

        collect_edges(0, -1)

        def is_ancestor(u, v):
            return time_in[u] <= time_in[v] and time_out[v] <= time_out[u]

        for i in range(len(edge_nodes)):
            for j in range(i + 1, len(edge_nodes)):
                _, u = edge_nodes[i]
                _, v = edge_nodes[j]

                if is_ancestor(u, v):
                    xor1 = xor_subtree[v]
                    xor2 = xor_subtree[u] ^ xor_subtree[v]
                    xor3 = total_xor ^ xor_subtree[u]
                elif is_ancestor(v, u):
                    xor1 = xor_subtree[u]
                    xor2 = xor_subtree[v] ^ xor_subtree[u]
                    xor3 = total_xor ^ xor_subtree[v]
                else:
                    xor1 = xor_subtree[u]
                    xor2 = xor_subtree[v]
                    xor3 = total_xor ^ xor_subtree[u] ^ xor_subtree[v]

                max_x = max(xor1, xor2, xor3)
                min_x = min(xor1, xor2, xor3)
                min_score = min(min_score, max_x - min_x)

        return min_score

