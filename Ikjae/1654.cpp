#include <bits/stdc++.h>
using namespace std;
long long k, n, lan[10000];
int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	cin >> k >> n;
	long long i, l, r, mid, ans, cnt;
	l = r = ans = 1;
	for(i=0;i<k;++i) cin >> lan[i];
	for(i=0;i<k;++i) r = max(r, lan[i]);
	while(l <= r){
		mid = (l + r) / 2;
		cnt = 0;
		for(i=0;i<k;++i) cnt += lan[i] / mid;
		if(cnt >= n){
			ans = max(ans, mid);
			l = mid + 1;
		}else{
			r = mid - 1;
		}
	}
	cout << ans;
	return 0;
}
