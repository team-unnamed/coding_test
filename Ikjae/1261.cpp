#include <bits/stdc++.h>
using namespace std;

int main(){
	int n,m;
	cin >> n >> m;
	if(n == 1 && m == 1){
		cout << 0;
		return 0;
	}
	int i,j,k,b[m][n],c[m][n];
	int nx[] = {1, -1, 0, 0};
	int ny[] = {0,0,-1,1};
	char tmp;
	for(i=0;i<m;++i){
		for(j=0;j<n;++j){
			cin >> tmp;
			b[i][j] = tmp - '0';
			c[i][j] = -1;
		}
	}
	c[0][0] = 0;
	queue<int> q;
	if(n >= 2) {
		q.push(1);
		c[0][1] = b[0][1];
	}
	if(m >= 2){
		q.push(n);
		c[1][0] = b[1][0];
	}
	while(!q.empty()){
		i = q.front() / n;
		j = q.front() % n;
		q.pop();
		for(k=0;k<4;++k){
			if(i + nx[k] >= 0 &&
					i + nx[k] < m &&
					j + ny[k] >=0 &&
					j + ny[k] < n &&
					(c[i+nx[k]][j+ny[k]] == -1 || 
					 c[i+nx[k]][j+ny[k]] > c[i][j] + b[i+nx[k]][j+ny[k]])){
				c[i+nx[k]][j+ny[k]] = c[i][j] + b[i+nx[k]][j+ny[k]];
				q.push( (i+nx[k]) * n + j + ny[k]);
			}
		}
	}
	cout << c[m-1][n-1];
	return 0;
}
