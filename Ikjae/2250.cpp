#include <bits/stdc++.h>
using namespace std;
int n;
pair< int, int > t[10001];
int main(){
	cin >> n;
	int par[n+1], absPos[n+1], relPos[n+1], levels[n+1];
	int i,a,x,y, root;
	for(i=1;i<=n;++i) par[i] = relPos[i] = absPos[i] = 0;
	for(i=1;i<=n;++i){
		cin >> a >> x >> y;
		t[a] = make_pair(x,y);
		if(x != -1) par[x] = a;
		if(y != -1) par[y] = a;
	}
	for(i=1;i<=n;++i)if(par[i] == 0) root = i;
	

	levels[root] = 1;
	stack<int> s;
	s.push(root);
	while(!s.empty()){
		a = s.top();
		x = t[a].first;
		y = t[a].second;
		if(x == -1 && y == -1){
			s.pop();
			relPos[a] = 1;
		}else if((x == -1 || relPos[x] != 0) && (y == -1 || relPos[y] != 0) && x != y){
			s.pop();
			if(x != -1) relPos[a]+=relPos[x];
			if(y != -1) relPos[a]+=relPos[y];
			++relPos[a];
		}else{
			if(t[a].second != -1) s.push(t[a].second);
			if(t[a].first != -1) s.push(t[a].first);
		}
	}
	if(t[root].first != -1) absPos[root] = relPos[t[root].first] + 1;
	else absPos[root] = 1;
	int parent,left,right,tmp;
	queue<int> q;
	q.push(root);
	while(!q.empty()){
		tmp = q.front();
		q.pop();
		parent = par[tmp];
		left = t[tmp].first;
		right = t[tmp].second;
		if(parent != 0){
			if(t[parent].first == tmp){
				if(right != -1) absPos[tmp] = absPos[parent] - relPos[right] -1;
				else absPos[tmp] = absPos[parent] - 1;
			}else{
				if(left != -1) absPos[tmp] = absPos[parent] + relPos[left] + 1;
				else absPos[tmp] = absPos[parent] + 1;
			}
			levels[tmp] = levels[parent] + 1;
		}
		if(left != -1) q.push(left);
		if(right != -1) q.push(right);
	}

	int maxLevel = 1;
	int maxDiff = 1;
	pair<int, int> diff[n+1];
	for(i=1;i<=n;++i){
		diff[i].first = 100000;
		diff[i].second = 0;
	}
	int cur;
	for(i=1;i<=n;++i){
		cur = levels[i];
		if(diff[cur].first > absPos[i]) diff[cur].first = absPos[i];
		if(diff[cur].second < absPos[i]) diff[cur].second = absPos[i];
		if(diff[cur].second - diff[cur].first + 1 > maxDiff){
			maxDiff = diff[cur].second - diff[cur].first + 1;
		}
		maxLevel = max(maxLevel, cur);
	}
	cur = 1;
	maxDiff = 1;
	for(i=1;i<=maxLevel;++i){
		if(diff[i].second - diff[i].first + 1 > maxDiff){
			cur = i;
			maxDiff = diff[i].second - diff[i].first + 1;
		}
	}
	cout << cur << " " << maxDiff;
	return 0;
}
