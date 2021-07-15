#include <bits/stdc++.h>
using namespace std;
vector<int> numbers(13);
void permute(vector< vector< int > > &ans,
		vector<int> &s,
		int k,
		int i,
		int nb
		){
	if(nb == 0){
		ans.push_back(s);
	}else{
		for(int j=i;j<k;++j){
			s.push_back(numbers[j]);
			permute(ans,s,k,j+1,nb-1);
			s.pop_back();
		}
	}
}

vector< vector< int > > permute_prep(int k){
	vector< vector< int > > ans;
	vector<int> s;
	permute(ans, s, k, 0, 6);
	return ans;
}

int main(){
	while(1){
		int k;
		cin >> k;
		if(k == 0){
			break;
		}
		for(int i=0;i<k;++i){
			cin >> numbers[i];
		}
		vector< vector< int > > ans;
		ans = permute_prep(k);
		for(auto v : ans){
			for(auto ele : v){
				cout << ele << " ";
			}
			cout << "\n";
		}
		cout << "\n";
	}
	return 0;
}
