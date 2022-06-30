  # heap 저장 시 가장 아래에 값을 넣고, 부모 노드와 크기를 비교하여 부모 노드보다 값이 크면 swap 한다
  # heap 삭제 시 루트값을 지운다. 그 후 그 자리에 자식중 가장 큰 값을 올려준다
  # heap은 주로 array를 이용하여 구현한다.
  # heap[k] 의 자식 노드는 heap[2*k + 1] 과 heap[2*k + 2]
  # https://github.com/python/cpython/blob/main/Lib/heapq.py
  # https://velog.io/@emplam27/%ED%8C%8C%EC%9D%B4%EC%8D%AC-heapq-%EB%AA%A8%EB%93%88-%EC%BD%94%EB%93%9C-%EB%9C%AF%EC%96%B4%EB%B3%B4%EA%B8%B0