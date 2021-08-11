#include <bits/stdc++.h>
using namespace std;
int n, m, board[500][500];
int x[19][4] = {{0,1,2,3}, {0,0,0,0}, 
	{0,1,0,1}, 
	{0,1,2,2}, {0,0,1,2}, {0,1,2,0}, {0,1,2,2},
	{0,1,0,0}, {0,1,1,1}, {0,0,0,1}, {0,1,1,1},
	{0,1,2,1}, {0,0,0,1}, {0,1,2,1}, {0,1,1,1},
	{0,0,1,1}, {0,0,-1,-1}, {0,1,1,2}, {0,1,1,2}};
int y[19][4] = {{0,0,0,0}, {0,1,2,3}, 
	{0,0,1,1}, 
	{0,0,0,1}, {0,1,1,1}, {0,0,0,1}, {0,0,0,-1},
	{0,0,1,2}, {0,0,1,2}, {0,1,2,2}, {0,0,-1,-2},
	{0,0,0,-1}, {0,1,2,1}, {0,0,0,1}, {0,-1,0,1},
	{0,1,1,2}, {0,1,1,2}, {0,0,1,1}, {0,0,-1,-1}};
int main(){
	cin >> n >> m;

	int i, j;
	for(i=0;i<n;++i) for(j=0;j<m;++j) cin >> board[i][j];

	int ans, numShape, k, l, shapeSize, total;
	bool valid;
	ans = 0;
	numShape = 19;
	shapeSize = 4;
	
	for(i=0;i<n;++i){
		for(j=0;j<m;++j){
			for(k=0;k<numShape;++k){
				valid = true;
				total = 0;
				for(l=0;l<shapeSize;++l){
					if(x[k][l] + j < 0 || x[k][l] + j >= m) valid = false;
					if(y[k][l] + i < 0 || y[k][l] + i >= n) valid = false;
				}
				if(valid){
					for(l=0;l<shapeSize;++l){
						total += board[y[k][l] + i][x[k][l] + j];
					}
					ans = max(ans,total);
				}
			}
		}
	}
	cout << ans;
	return 0;
}
