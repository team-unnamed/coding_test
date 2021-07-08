#include <bits/stdc++.h>
using namespace std;
int main(){
	int n, i, r, g, b, t1, t2, t3, r0, g0, b0;
	cin >> n >> r >> g >> b;
	for(i=2;i<=n;++i){
		cin >> t1 >> t2 >> t3;
		r0 = t1 + min(g, b);
		g0 = t2 + min(r, b);
		b0 = t3 + min(r, g);
		r = r0;
		b = b0;
		g = g0;
	}
	cout << min(r, min(g, b));
	return 0;
}
