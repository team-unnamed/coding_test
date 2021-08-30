#include <bits/stdc++.h>
using namespace std;
int main(){
	bool finished = false;
	int problem = 1;
	int dx[] = {-1,0,1,0};
	int dy[] = {0,-1,0,1};
	while(!finished){
		int N;
		cin >> N;
		if(N == 0) finished = true;
		else cout << "Problem " << problem++ << ": ";
		if(!finished){
			int i, j, board[N][N];
			for(i=0;i<N;++i){
				for(j=0;j<N;++j) cin >> board[i][j];
			}
			vector<int> dist(N * N, -1);
			dist[0] = 0;
			priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;
			pq.push({0,0});
			bool visited = false;
			while(!pq.empty() && !visited){
				int position = pq.top().second;
				int cost = pq.top().first;
				pq.pop();
				if(dist[position] < cost) continue;
				if(position == N * N - 1) visited = true;
				if(!visited){
					int x = position % N;
					int y = position / N;
					int dcnt;
					for(dcnt=0;dcnt<4;++dcnt){
						if(x + dx[dcnt] < 0 || x + dx[dcnt] >= N) continue;
						if(y + dy[dcnt] < 0 || y + dy[dcnt] >= N) continue;
						int nxtPosition = (y + dy[dcnt]) * N + x + dx[dcnt];
						int nxtCost = board[y + dy[dcnt]][x + dx[dcnt]] + cost;
						if(dist[nxtPosition] > nxtCost || dist[nxtPosition] == -1){
							dist[nxtPosition] = nxtCost;
							pq.push({nxtCost, nxtPosition});
						}
					}
				}
			}
			cout << dist[N * N - 1] + board[0][0] << "\n";
		}
	}	
	return 0;
}
