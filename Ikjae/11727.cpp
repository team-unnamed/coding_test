#include <bits/stdc++.h>
using namespace std;
int dp[1002];
int main(){
	int n, i;
	cin >> n;
	dp[1] = 1;
	dp[2] = 3;
	for(i=3;i<=n;++i)
		dp[i] = (dp[i-1] + 2 * dp[i-2]) % 10007;	
	cout << dp[n];
	return 0;
}