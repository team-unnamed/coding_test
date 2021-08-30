#include <bits/stdc++.h>
using namespace std;
int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	int N, M, S, T, i, A, B, C;
	cin >> N >> M;
	vector<vector<pair<int, int>>> adj(1001);
	for(i=0;i<M;++i){
		cin >> A >> B >> C;
		adj[A].push_back({B, C});
	}
	cin >> S >> T;
	vector<int> dist(N + 1, -1);
	dist[S] = 0;
	priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int, int>>> pq;
	pq.push({0, S});
	bool visited = false;
	while(!pq.empty() && !visited){
		int node = pq.top().second;
		int cost = pq.top().first;
		pq.pop();
		if(dist[node] < cost) continue;
		if(node == T) visited = true;
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
	cout << dist[T];
	return 0;
}
