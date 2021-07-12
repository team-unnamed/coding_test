#include <bits/stdc++.h>
using namespace std;
int vec[202][202];
int main(){
	int n,k,i,j;
	cin >> n >> k;
	for(i=1;i<=n;++i){
		vec[i][1] = 1;
	}
	for(i=1;i<=k;++i){
		vec[1][i] = i;
	}
	for(i=2;i<=n;++i){
		for(j=2;j<=k;++j){
			vec[i][j] = (vec[i-1][j] + vec[i][j-1]) % 1000000000;
		}
	}
	cout << vec[n][k];
	return 0;
}
