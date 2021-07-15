#include <bits/stdc++.h>
using namespace std;
vector<int> heights(9);
void permute(vector< vector< int > > &ans,
		vector<int> &s,
		int i,
		int nb
		){
	if(nb == 0){
		ans.push_back(s);
	}else{
		for(int j=i;j<9;++j){
			s.push_back(heights[j]);
			permute(ans,s,j+1,nb-1);
			s.pop_back();
		}
	}
}

vector< vector< int > > permute_prep(){
	vector< vector< int > > ans;
	vector<int> s;
	permute(ans, s, 0, 7);
	return ans;
}

int main(){
	for(int i=0;i<9;++i){
		cin >> heights[i];
	}
	vector< vector< int > > ans;
	ans = permute_prep();
	for(auto v : ans){
		int tmp=0;
		for(auto ele : v){
			tmp += ele;
		}
		if(tmp == 100){
			sort(v.begin(), v.end());
			for(auto ele : v){
				cout << ele << "\n";
			}
			break;
		}
	}


	return 0;
}
