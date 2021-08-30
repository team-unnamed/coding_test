#include <bits/stdc++.h>
using namespace std;
int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	int N, M, i, A, B, C;
	cin >> N >> M;
	vector<vector<pair<int,int>>> adj(1001);
	for(i=0;i<M;++i){
		cin >> A >> B >> C;
		adj[A].push_back({B,C});
		adj[B].push_back({A,C});
	}
	vector<int> dist(N + 1, -1);
	dist[1] = 0;
	priority_queue<pair<int,pair<int,int>>, 
		vector<pair<int,pair<int,int>>>,
		greater<pair<int,pair<int,int>>>> pq;
	pq.push({0,{-1,1}});
	vector<pair<int,int>> ans;
	while(!pq.empty()){
		int cur = pq.top().second.second;
		int pst = pq.top().second.first;
		int cost = pq.top().first;
		pq.pop();
		if(dist[cur] < cost) continue;
		else if(pst != -1) ans.push_back({pst, cur});
		for(auto pos : adj[cur]){
			int nxt = pos.first;
			int nxtCost = cost + pos.second;
			if(dist[nxt] > nxtCost || dist[nxt] == -1){
				dist[nxt] = nxtCost;
				pq.push({nxtCost,{cur,nxt}});
			}
		}
	}
	cout << ans.size() << "\n";
	for(auto ele : ans){
		cout << ele.first << " " << ele.second << "\n";
	}
	return 0;
}
