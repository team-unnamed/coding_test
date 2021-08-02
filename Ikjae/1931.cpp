#include <bits/stdc++.h>
using namespace std;
int n;
vector< pair< int, int > > v;
bool sortbysec(pair<int, int> &a,
	       pair<int, int> &b){
	if(a.second == b.second){
		return (a.first < b.first);
	}else{
		return (a.second < b.second);
	}
}
int main(){
	int i,start,end,ans;
	cin >> n;
	for(i=0;i<n;++i){
		cin >> start >> end;
		v.push_back(make_pair(start, end));
	}
	sort(v.begin(), v.end(), sortbysec);
	ans = end = 0;
	for(i=0;i<n;++i){
		if(v[i].first >= end){
			++ans;
			end = v[i].second;
		}
	}
	cout << ans;
	return 0;
}
