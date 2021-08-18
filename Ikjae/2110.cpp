#include <bits/stdc++.h>
using namespace std;
int n, c, h[200'000];
int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	cin >> n >> c;
	int i, l, r, mid, ans, cnt, base;
	for(i=0;i<n;++i) cin >> h[i];
	
	sort(h, h + n);

	l = r = ans = 0;
	for(i=0;i<n;++i) r = max(r, h[i]);

	while(l <= r){
		mid = (l + r) / 2;
		cnt = 1;
		base = h[0];
		for(i=0;i<n;++i){
			if(h[i] - base >= mid){
				++cnt;
				base = h[i];
			}
		}
		if(cnt < c){
			r = mid - 1;
		}else{
			l = mid + 1;
			ans = max(ans, mid);
		}
	}
	cout << ans;
	return 0;
}
