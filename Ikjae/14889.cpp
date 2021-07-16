#include <bits/stdc++.h>
using namespace std;
int nbs[21][21];

void permute(int &ans, vector<int> &tmp, int n, int cur, int nb){
	if(nb == 0){
		vector<int> v;
		for(int j=1;j<=n;++j){
			bool found = false;
			for(auto ele : tmp){
				if(ele == j){
					found = true;
				}
			}
			if(!found){
				v.push_back(j);
			}
		}
		int total = 0;
		for(int j=0;j<n/2;++j){
			for(int k=0;k<n/2;++k){
				if(j != k){
					total += nbs[tmp[j]][tmp[k]];	
					total -= nbs[v[j]][v[k]];
				}
			}
		}
		ans = min(ans, abs(total));
	}else{
		for(int i=cur;i<=n;++i){
			tmp.push_back(i);
			permute(ans, tmp, n, i+1, nb-1);
			tmp.pop_back();
		}
	}
}

int main(){
	int n,i,j;
	cin >> n;
	for(i=1;i<=n;++i){
		for(j=1;j<=n;++j){
			cin >> nbs[i][j];
		}
	}
	int ans = 20000;
	vector<int> tmp;
	permute(ans, tmp, n, 1, n/2);
	cout << ans;
	return 0;
}
