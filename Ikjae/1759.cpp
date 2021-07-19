#include <bits/stdc++.h>
using namespace std;
vector<char> v;
void comb(vector<char> &s,
		int c,
		int cur,
		int l){
	if(l == 0){
		int aeiou = 1;
		int rest = 2;
		for(auto ele : s){
			if(ele == 'a'||
				ele == 'e'||
				ele == 'i'||
				ele == 'o'||
				ele == 'u'){
				aeiou -= 1;
			}else{
				rest -= 1;
			}
		}
		if(aeiou <= 0 && rest <= 0){
			for(auto ele : s){
				cout << ele;
			}
			cout << "\n";
		}
	}else{
		for(int idx=cur;idx<c;++idx){
			s.push_back(v[idx]);
			comb(s,c,idx+1,l-1);
			s.pop_back();
		}
	}
}

int main(){
	int l, c, i, j;
	cin >> l >> c;
	for(i=0;i<c;++i){
		char tmp;
		cin >> tmp;
		v.push_back(tmp);
	}
	sort(v.begin(), v.end());
	vector<char> s;
	comb(s,c,0,l);
	return 0;
}
