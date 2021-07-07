#include <bits/stdc++.h>
using namespace std;

int dp[100002][2];

int main(){
	int n,i;
	cin >> n;
	dp[1][0] = 1;
	dp[1][1] = 2;
	for(i=2;i<=n;++i){
		dp[i][0] = (dp[i-1][0]+dp[i-1][1]) % 9901;
		dp[i][1] = (dp[i-1][1] +dp[i-1][0]*2) % 9901;
	}
	cout << (dp[n][0] + dp[n][1] ) % 9901;
	return 0;
}
