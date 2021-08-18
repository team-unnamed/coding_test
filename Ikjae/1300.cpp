#include <bits/stdc++.h>
using namespace std;
long long n, k;
int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	cin >> n >> k;
	long long i, l, r, ans, cnt, mid;
	l = 1;
	r = k;
	ans = 10'000'000'000;
	while(l <= r){
		mid = (l + r) / 2;
		cnt = 0;
		for(i=1;i<=n;++i) cnt += min(n, mid / i);
		if(cnt < k){
			l = mid + 1;
		}else{
			ans = min(ans, mid);
			r = mid - 1;
		}
	}	
	cout << ans;
	return 0;
}
