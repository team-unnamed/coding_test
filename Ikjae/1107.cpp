#include <bits/stdc++.h>
using namespace std;
vector<bool> functional(10, true);
int pos(int i){
	if(i == 0 && functional[0]){
		return 1;
	}else if(i == 0 && !functional[0]){
		return -1;
	}
	int cnt = 0;
	while(i > 0){
		if(functional[i % 10]){
			i /= 10;
			cnt += 1;
		}else{
			return -1;
		}
	}
	return cnt;
}	


int main(){
	int n,m,i,tmp,best;
	cin >> n >> m;
	for(i=0;i<m;++i){
		cin >> tmp;
		functional[tmp] = false;
	}
	best = abs(100 - n);
	for(i=0;i<=1000000;++i){
		tmp = pos(i);
		if(tmp > 0){
			best = min(best, abs(i-n) + tmp);
		}
	}
	cout << best;
	return 0;
}
