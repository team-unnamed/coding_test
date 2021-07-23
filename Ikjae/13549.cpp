#include <bits/stdc++.h>
using namespace std;
vector<int> l(100001,300000);
int main(){
	int n,k;
	cin >> n >> k;
	if(n >= k) cout << n - k;
	else{
		l[n] = 0;
		queue<int> q;
		if(n - 1 >= 0) {
			q.push(n-1);
			l[n-1] = 1;
		}
		if(n + 1 <= 100001) {
			q.push(n+1);
			l[n+1] = 1;
		}
		if(n * 2 <= 100001 && n != 0){
			q.push(2 * n);
			l[2*n] = 0;
		}
		while(!q.empty()){
			n = q.front();
			q.pop();
			if(n + 1 <= 100001 && l[n+1] > l[n] + 1){
				if(n + 1 != k) q.push(n+1);
				l[n+1] = l[n] + 1;
			}
			if(n - 1 >= 0 && l[n-1] > l[n] + 1){
				if(n - 1 != k) q.push(n-1);
				l[n-1] = l[n] + 1;
			}
			if(n != 0 && 2 * n <= 100001 && l[2*n] > l[n]){
				if(2 * n != k) q.push(n*2);
				l[2*n] = l[n];
			}
		}
		cout << l[k];
	}
	return 0;
}
