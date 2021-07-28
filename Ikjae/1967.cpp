#include <bits/stdc++.h>
#define X first
#define Y second
using namespace std;
int n,r;
pair<int, int> p{-1,-1};
vector< pair< int, int > > children(1,p);
vector< vector< pair< int, int > > > t(10001,children);
int post(int node, int weight){
	int i, numChild, st, nd, res;
	numChild = t[node].size();
	st = nd = 0;
	for(i = 1; i < numChild; ++i){
		res = post(t[node][i].X, t[node][i].Y);
		if(res > st && res > nd) {
			nd = st;
			st = res;
		}
		else if(st >= res && res > nd) nd = res;
	}
	r = max(r, st + nd);
	return st + weight;
}
int main(){
	cin >> n;
	r = 0;
	int i, parent, child, weight;
	for(i=0;i<n-1;++i){
		cin >> parent >> child >> weight;
		t[parent].push_back(make_pair(child, weight));
	}
	cout << max(post(1,0),r);
	return 0;
}
