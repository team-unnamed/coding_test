#include <bits/stdc++.h>
using namespace std;
long long dp[103][10];

int main(){
	int n, i, j;
	cin >> n;
	dp[1][0]=0;
	for(i=1;i<=9;++i){
		dp[1][i] = 1;
	}
	for(i=2;i<=n;++i){
		for(j=0;j<=9;++j){
			if(j==0){
				dp[i][j] = dp[i-1][j+1];
			}else if(j==9){
				dp[i][j] = dp[i-1][j-1];
			}else{
				dp[i][j] = (dp[i-1][j-1]+dp[i-1][j+1]) % 1000000000;
			}
		}
	}
	long long ans=0;
	for(i=0;i<=9;++i){
		ans += dp[n][i];
	} 
	cout << ans % 1000000000;
	return 0;
}
