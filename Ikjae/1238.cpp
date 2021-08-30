#include <bits/stdc++.h>
using namespace std;
int N, M, X;
vector<vector<pair<int, int>>> adj(1001);
int dijkstra(int source, int target){
	priority_queue<pair<int,int>,
		vector<pair<int,int>>,
		greater<pair<int,int>>> pq;
	pq.push({0, source});
	vector<int> dist(N + 1, -1);
	dist[source] = 0;
	bool visited = false;
	while(!pq.empty() && !visited){
		int cur = pq.top().second;
		int cost = pq.top().first;
		pq.pop();
		if(cur == target) visited = true;
		if(!visited){
			for(auto pos : adj[cur]){
				int nxt = pos.first;
				int nxtCost= cost + pos.second;
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
	int A, B, T, i;
	cin >> N >> M >> X;
	for(i=0;i<M;++i){
		cin >> A >> B >> T;
		adj[A].push_back({B, T});
	}
	int longest = 0;
	for(i=1;i<=N;++i){
		int tmp = 0;
		tmp += dijkstra(i, X);
		tmp += dijkstra(X, i);
		longest = max(longest, tmp);
	}
	cout << longest;
	return 0;
}
