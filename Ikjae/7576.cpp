#include <bits/stdc++.h>
using namespace std;
int m, n;
int b[1000][1000];
int p[1000][1000];
int main(){
	cin >> m >> n;
	int i,j;
	queue<int> q;
	for(i=0;i<n;++i){
		for(j=0;j<m;++j){
			cin >> b[i][j];
			if(b[i][j] == 1) q.push(i * m + j);
			p[i][j] = 0;
			if(b[i][j] == -1) p[i][j] = -1;
		}
	}
	int x, y;
	while(!q.empty()){
		x = q.front() / m;
		y = q.front() % m;
		q.pop();
		if(x - 1 >= 0 && ((p[x-1][y] == 0 && b[x-1][y]==0)|| p[x-1][y] > p[x][y] + 1)){
			p[x-1][y] = p[x][y] + 1;
			q.push((x-1) * m + y);
		}
		if(x + 1 < n && ((p[x+1][y] == 0&&b[x+1][y]==0)|| p[x+1][y] > p[x][y] + 1)){
			p[x+1][y] = p[x][y] + 1;
			q.push((x+1) * m + y);
		}
		if(y - 1 >= 0 && ((p[x][y-1] == 0&&b[x][y-1]==0) || p[x][y-1] > p[x][y] + 1)){
			p[x][y-1] = p[x][y] + 1;
			q.push(x * m + y - 1);
		}
		if(y + 1 < m && ((p[x][y+1] == 0&&b[x][y+1]==0) || p[x][y+1] > p[x][y] + 1)){
			p[x][y+1] = p[x][y] + 1;
			q.push(x * m + y + 1);
		}
	}
	int zero = 0;
	int ans = 0;
	for(i=0;i<n;++i){
		for(j=0;j<m;++j){
			if(p[i][j] == 0 && b[i][j] == 0) ++zero;
			ans = max(ans, p[i][j]);
		}
	}
	if(zero > 0) cout << -1;
	else cout << ans;
	return 0;
}
