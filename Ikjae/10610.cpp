#include <bits/stdc++.h>
using namespace std;
int main(){
	string s;
	cin >> s;
	int total, zero,i;
	total = zero = 0;
	sort(s.begin(), s.end(), greater<char>());
	for(i=0;i<s.size();++i){
		if(s[i] == '0') ++zero;
		else total += s[i] - '0';
	}
	if(zero >= 1 && total % 3 == 0) cout << s;
	else cout << -1;
	return 0;
}
