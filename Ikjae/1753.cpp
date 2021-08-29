#include <bits/stdc++.h>
using namespace std;
int main(){
	int V, E, s, u, v, w, i;
	cin >> V >> E >> s;
	vector<vector<pair<int, int>>> adj(V + 1);
	for(i=0;i<E;++i){
		cin >> u >> v >> w;
		adj[u].push_back({v, w});
	}
	vector<int> dist(V + 1, -1);
	dist[s] = 0;
	priority_queue< pair<int, int>, vector<pair<int, int> >, greater<pair<int, int> > > pq;
	pq.push({0, s});
	while(!pq.empty()){
		int cost = pq.top().first;
		int node = pq.top().second;
		pq.pop();
		for(auto pos : adj[node]){
			int nxt = pos.first;
			int nxtCost = cost + pos.second;
			if(dist[nxt] > nxtCost || dist[nxt] == -1){
				dist[nxt] = nxtCost;
				pq.push({nxtCost, nxt});
			}
		}
	}
	for(int i=1;i<=V;++i){
		if(dist[i] == -1) cout << "INF\n";
		else cout << dist[i] << "\n";
	}
	return 0;
}
