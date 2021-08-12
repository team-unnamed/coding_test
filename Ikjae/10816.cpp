#include <bits/stdc++.h>
using namespace std;
int n,m;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
	cin >> n;
	int i, tmp;
	map<int, int> cnt;
	for(i=0;i<n;++i){
		cin >> tmp;
		if(cnt.find(tmp) == cnt.end()) cnt[tmp] = 1;
		else cnt[tmp] = cnt[tmp] + 1;
	}
	cin >> m;
	for(i=0;i<m;++i){
		cin >> tmp;
		if(cnt.find(tmp) == cnt.end()) cout << 0 << " ";
		else cout << cnt[tmp] << " ";
	}
	return 0;
}
