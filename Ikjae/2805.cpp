#include <bits/stdc++.h>
using namespace std;
int main(){
	int n, m, i, cut, arr[1000000];
	cin >> n >> m;
	for(i=0;i<n;++i) cin >> arr[i];
	
	sort(arr, arr+n, greater<int>());
	
	i = 0;
	cut = arr[0];
	while(i < n && i * (cut - arr[i]) <= m){
		m -= i * (cut - arr[i]);
		cut = arr[i];
		++i;
	}
	if(m > 0){
		cut -= (m / i);
		if(m % i != 0) cut -= 1;
	}
	cout << cut;
	return 0;
}
