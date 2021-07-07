#include <bits/stdc++.h>
using namespace std;
vector<long long> dp(1001);
vector<long long> ans(1001);
int main(){
	int n, a, i, j, best;
	cin >> n;
	for(i=1;i<=n;++i) cin >> dp[i];
	ans[1] = dp[1];
	for(i=2;i<=n;++i){
		best = 0;
		for(j=1;j<=i-1;++j){
			if(dp[i] > dp[j] && ans[j] > best){
				best = ans[j];
			}
		}
		ans[i] = best + dp[i];
	}
	best = -1;
	for(i=1;i<=n;++i){
		if(best < ans[i]){
			best = ans[i];
		}
	}
	cout << best;
	return 0;
}
