#include <bits/stdc++.h>
using namespace std;
int n, m, nb[5000];
int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	cin >> n >> m;
	int i, l, r, mid, ans, cnt, sm, lg;
	l = r = 0;
	ans = 10001;
	for(i=0;i<n;++i) cin >> nb[i];
	for(i=0;i<n;++i) r = max(r, nb[i]);
	while(l <= r){
		mid = (l + r) / 2;
		cnt = 1;
		sm = 10001;
		lg = 0;
		for(i=0;i<n;++i){
			sm = min(sm, nb[i]);
			lg = max(lg, nb[i]);
			if(lg - sm > mid){
				++cnt;
				sm = lg = nb[i];
			}
		}
		if(cnt > m){
			l = mid + 1;
		}else{
			r = mid - 1;
			ans = min(ans, mid);
		}
	}
	cout << ans;
	return 0;
}
