#include <bits/stdc++.h>
using namespace std;

int main(){
	string s;
	cin >> s;
	int i,j,tmp,ans,found,n = s.size();
	i=ans=found=0;
	while(i < n){
		j = i;
		while(isdigit(s[j])) ++j;
		if(i != j) tmp = stoi(s.substr(i,j-i));
		else if(s[i] == '-')
			found = 1;
		if((i != j) && (i == 0 || !found)){
			ans += tmp;
		}else if(i != j){
			ans -= tmp;
		}
		if(i == j) ++j;
		i = j;
	}
	cout << ans;
	return 0;
}
