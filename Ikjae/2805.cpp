#include <bits/stdc++.h>
using namespace std;
long long n, m, tree[1'000'000];
int main(){
	cin >> n >> m;
	long long i, l, r, mid, total, ans;
	l = r = ans = 0;
	for(i=0;i<n;++i) cin >> tree[i];
	for(i=0;i<n;++i) r = max(r, tree[i]);
	while(l <= r){
		mid = (l + r) / 2;
		total = 0;
		for(i=0;i<n;++i){
			if(tree[i] > mid) total += tree[i] - mid;
		}
		if(total >= m){
			ans = max(ans, mid);
			l = mid + 1;
		}else{
			r = mid - 1;
		}
	}
	cout << ans;
	return 0;
}
