#include <bits/stdc++.h>
using namespace std;
vector<int> dp(22,0);
int main(){
	int n,i,j,t,p;
	cin >> n;
	for(i=1;i<=n;++i){
		cin >> t >> p;
		for(j=1;j<=i;++j){
			dp[i] = max(dp[i], dp[j]);
		}
		dp[i+t] = max(dp[i+t], dp[i] + p);
	}
	int ans=0;
	for(i=1;i<=n+1;++i){
		ans = max(ans, dp[i]);
	}
	cout << ans;
	return 0;
}
