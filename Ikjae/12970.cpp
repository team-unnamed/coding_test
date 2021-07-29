#include <bits/stdc++.h>
using namespace std;
int n, k;
int main(){
	cin >> n >> k;
	int cnt = n * (n / 2) - (n/2)*(n/2);
	if(cnt < k){
		cout << -1;
	}else{
		char tmp, ans[n];
		int i, cur, numB;
		for(i=0;i<n;++i){
			if(i < n/2) ans[i] = 'A';
			else ans[i] = 'B';
		}
		cur = n / 2;
		numB = 0;
		while(cnt != k){
			tmp = ans[cur + numB];
			ans[cur + numB] = ans[cur + numB - 1];
			ans[cur + numB - 1] = tmp;
			--cur;
			--cnt;
			if(cur == 0){
				++numB;
				cur = n / 2;
			}
		}
		for(char ch : ans){
			cout << ch;
		}
	} 
	return 0;
}
