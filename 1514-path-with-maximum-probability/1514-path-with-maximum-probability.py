class Solution:
  def maxProbability(
      self,
      n: int,
      edges: list[list[int]],
      succProb: list[float],
      start: int,
      end: int,
  ) -> float:
    graph = [[] for _ in range(n)]  
    maxHeap = [(-1.0, start)] 
    seen = [False] * n

    for i, ((u, v), prob) in enumerate(zip(edges, succProb)):
      graph[u].append((v, prob))
      graph[v].append((u, prob))

    while maxHeap:
      prob, u = heapq.heappop(maxHeap)
      prob *= -1
      if u == end:
        return prob
      if seen[u]:
        continue
      seen[u] = True
      for nextNode, edgeProb in graph[u]:
        if seen[nextNode]:
          continue
        heapq.heappush(maxHeap, (-prob * edgeProb, nextNode))

    return 0