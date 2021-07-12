#include <bits/stdc++.h>
using namespace std;
int vec[10001];
int main(){
	int n,i;
	cin >> n;
	for(i=1;i<=n;++i){
		cin >> vec[i];
	}
	int dp[3] = {0, vec[1], 0};
	int tmp[3];
	for(i=2;i<=n;++i){
		tmp[0] = dp[1] + vec[i];
		tmp[1] = dp[2] + vec[i];
		tmp[2] = max(dp[0], max(dp[1], dp[2]));
		dp[0] = tmp[0];
		dp[1] = tmp[1];
		dp[2] = tmp[2];
	}
	cout << max(dp[0], max(dp[1], dp[2]));
	return 0;
}
