#include <bits/stdc++.h>
using namespace std;
int n, k;
vector< pair< int, int > > mv;
vector<int> c;
int main(){
	cin >> n >> k;
	int i,j,ans,tmp0,tmp1;
	for(i=0;i<n;++i){ 
		cin >> tmp0 >> tmp1;
		mv.push_back(make_pair(tmp0, tmp1));
	}
	for(i=0;i<k;++i) {
		cin >> tmp0;
		c.push_back(tmp0);
	}
	
	sort(mv.begin(), mv.end());
	sort(c.begin(), c.end());
	
	j = ans = 0;
	priority_queue<int> q;
	for(i=0;i<k;++i){
		while(j < n && mv[j].first <= c[i]){
			q.push(mv[j].second);
			++j;
		}
		if(!q.empty()){
			ans += q.top();
			q.pop();
		}
	}
	cout << ans;
	return 0;
}
