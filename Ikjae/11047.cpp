#include <bits/stdc++.h>
using namespace std;

int main(){
	int n, k, i, ans, coins[10];
	cin >> n >> k;
	for(i = 0; i < n; ++i) cin >> coins[i];
	ans = 0;
	for(i = n - 1; i >= 0; --i){
		if(k % coins[i] >= 0){
			ans += k / coins[i];
			k %= coins[i];
		}
	}
	cout << ans;
	return 0;
}
