#include <bits/stdc++.h>
using namespace std;
int main(){
	string s, t;
	cin >> s >> t;
	bool opt, flip;
	int tsize,i;
	opt = true;
	flip = false;
	while(s.size() != t.size() && opt){
		opt = false;
		tsize = t.size();
		if(!flip && t[tsize-1] == 'A'){
			opt = true;
			t = t.substr(0, tsize - 1);
		}else if(!flip && t[tsize-1] == 'B'){
			opt = flip = true;
			t = t.substr(0, tsize - 1);
		}else if(flip && t[0] == 'A'){
			opt = true;
			t = t.substr(1, tsize - 1);
		}else if(flip && t[0] == 'B'){
			opt = true;
			flip = false;
			t = t.substr(1, tsize - 1);
		}
	}
	opt = true;
	if(t.size() != s.size()) opt = false;
	else if(!flip){
		for(i=0;i<t.size();++i){
			if(t[i] != s[i]) opt = false;
		}
	}else{
		tsize = t.size();
		for(i=0;i<t.size();++i){
			if(t[i] != s[tsize - i - 1]) opt = false;
		}
	}
	if(opt) cout << 1;
	else cout << 0;
	return 0;
}
