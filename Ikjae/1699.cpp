#include <bits/stdc++.h>
using namespace std;
vector<int> dp(100003);
int main(){
	int n,i,j;
	cin >> n;
	dp[0] = 0;
	for(i=0;i<=n;++i) dp[i]=i;
	for(i=4;i<=n;++i){
		for(j=2;j*j<=i;++j){
			dp[i] = min(dp[i], dp[i-j*j] + 1);
		}
	}
	cout << dp[n];
	return 0;
}
