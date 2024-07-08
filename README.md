벨만 포드 알고리즘은 그래프에서 시작 정점으로부터 다른 정점까지의 최단 경로를 찾기 위한 알고리즘이다. 벨만 포드 알고리즘의 특징은 다음과 같다.

<ul>
  <li>음수 가중치가 있는 그래프의 시작 정점에서 다른 정점까지의 최단 거리를 구할 수 있다.</li>
  <li>음수 사이클 존재의 여부를 알 수 있다.</li>
</ul>
음수 사이클 안에서 무한으로 뺑뺑이 도는 경우를 알 수 있는 방법은, 그래프 정점의 개수를 V라고 할 때 인접 간선을 검사하고 거리 값을 갱신하는 과정을 V-1번으로 제한하면 가능해진다. 그래프의 시작 정점에서 특정 정점까지 도달하기 위해 거쳐 가는 최대 간선 수는 V-1개이기 때문에 V번째 간선이 추가되는 순간 사이클이라고 판단할 수 있게 된다.

벨만 포드 알고리즘의 시간 복잡도는 O(VE)이다.

## 벨만 포드 알고리즘 프로세스
<ol type='1'>
  <li>시작 정점을 결정한다.</li>
  <li>시작 정점에서 각각 다른 정점까지의 거리 값을 무한대로 초기화한다.<br>(시작 정점이 a라면, distance[b] = a->b의 거리를 뜻함)<br>시작 정점 -> 시작 정점은 0으로 초기화한다.</li>
  <li>현재 정점에서 모든 인접 정점들을 탐색하며, 기존에 저장되어 있는 인접 정점까지의 거리(distance[a])보다 현재 정점을 거쳐 인접 정점에 도달하는 거리가 더 짧을 경우 짧은 거리로 갱신해준다.</li>
  <li>3번의 과정을 V-1번 반복한다.</li>
  <li>위 과정을 모두 마치고 난 후 거리가 갱신되는 경우가 생긴다면 그래프에 음수 사이클이 존재한다는 것이다.</li>
</ol>
<hr>
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=http%3A%2F%2Fcfile2.uf.tistory.com%2Fimage%2F9987253359DAD57120F171"><br>
시작점이 1일 때, Dist[1]만 0으로 놓고 나머지는 무한대로 설정한다.

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=http%3A%2F%2Fcfile6.uf.tistory.com%2Fimage%2F9947943359DAD5E5249EAC"> <br>
시작점 1의 인접 정점들을 탐색하며, Dist[노드]에 저장되어 있는 값보다 정점 1을 거쳐 가는 값이 더 작을 경우 그 값으로 업데이트한다. 여기서는 모두 INF 무한대 값보다 작기 때문에 다 업데이트하게 된다.

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=http%3A%2F%2Fcfile9.uf.tistory.com%2Fimage%2F9941353359DAD6612E0F0B"> <br>
정점 2의 인접 정점들을 탐색한다. 현재 정점(2)를 거쳐 정점 4로 가는 것이 정점 2를 거치지 않는 것보다 더 비용이 적게 들기 때문에 업데이트해준다.

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=http%3A%2F%2Fcfile27.uf.tistory.com%2Fimage%2F996D4C3359DAD6E72F40BC">
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=http%3A%2F%2Fcfile30.uf.tistory.com%2Fimage%2F993D073359DAD6FC371758">
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=http%3A%2F%2Fcfile3.uf.tistory.com%2Fimage%2F99B1663359DAD70D270EFB">

계속해서 V-1번이 될 때까지 반복해준다. 최종적으로 {0, -4, 5, -5, 1}이 나오게 된다.

## 음수 사이클
V-1번 반복이 끝난 이후, 한 번 더 위의 과정을 돌려주었을 때 값이 바뀐다면 음수 사이클이 있는 그래프임을 알 수 있다. (distance[a]에 저장되어 있는 값보다 현재 정점을 거쳐 가는 비용이 더 작다고 판별될 경우) 음수 사이클이 존재하는 경우에는 음수 가중치를 계속해서 더해주게 되어 최단 거리를 구할 수 없는 무한 루프에 빠지게 된다.
