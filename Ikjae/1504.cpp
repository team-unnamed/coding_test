#include <bits/stdc++.h>
using namespace std;
int N, E, u, v;
vector<vector<pair<int,int>>> adj(801);
int dijkstra(int source, int target){
	vector<int> dist(N+1, -1);
	dist[source] = 0;
	priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>> pq;
	pq.push({0,source});
	bool visited = false;
	while(!pq.empty() && !visited){
		int node = pq.top().second;
		int cost = pq.top().first;
		pq.pop();
		if(dist[node] < cost) continue;
		if(node == target) visited = true;
		if(!visited){
			for(auto pos : adj[node]){
				int nxt = pos.first;
				int nxtCost = cost + pos.second;
				if(dist[nxt] > nxtCost || dist[nxt] == -1){
					dist[nxt] = nxtCost;
					pq.push({nxtCost, nxt});
				}
			}
		}
	}
	return dist[target];
}
int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	int i, a, b, c;
	cin >> N >> E;
	for(i=0;i<E;++i){
		cin >> a >> b >> c;
		adj[a].push_back({b,c});
		adj[b].push_back({a,c});
	}
	cin >> u >> v;
	int ans1, ans2, tmp;
	ans1 = ans2 = 0;
	tmp = dijkstra(1, u);
	if(tmp != -1){
		ans1 += tmp;
		tmp = dijkstra(u, v);
		if(tmp != -1){
			ans1 += tmp;
			tmp = dijkstra(v, N);
			if(tmp != -1) ans1 += tmp;
			else ans1 = -1;
		}else ans1 = -1;
	}else ans1 = -1;
	tmp = dijkstra(1, v);
	if(tmp != -1){
		ans2 += tmp;
		tmp = dijkstra(v, u);
		if(tmp != -1){
			ans2 += tmp;
			tmp = dijkstra(u, N);
			if(tmp != -1) ans2 += tmp;
			else ans2 = -1;
		}else ans2 = -1;
	}else ans2 = -1;
	if(ans1 == -1 && ans2 == -1) cout << -1;
	else if(ans1 == -1 && ans2 != -1) cout << ans2;
	else if(ans1 != -1 && ans2 == -1) cout << ans1;
	else cout << min(ans1, ans2);
	return 0;
}
