#include <bits/stdc++.h>
using namespace std;
int main(){
	int t,n,i,j;
	cin >> t;
	while(t--){
		long long vec[3][100002];
		cin >> n;
		for(i=1;i<=2;++i){
			for(j=1;j<=n;++j){
				cin >> vec[i][j];
			}
		}
		long long dp[3],tmp[3];
		dp[0] = 0;
		dp[1] = vec[1][1];
		dp[2] = vec[2][1];
		for(i=2;i<=n;++i){
			tmp[0] = max(dp[0],max(dp[1],dp[2]));
			tmp[1] = max(dp[0],dp[2]) + vec[1][i];
			tmp[2] = max(dp[0],dp[1]) + vec[2][i];
			dp[0] = tmp[0];
			dp[1] = tmp[1];
			dp[2] = tmp[2];
		}
		cout << max(dp[0], max(dp[1], dp[2])) << "\n";
	}
	return 0;
}
