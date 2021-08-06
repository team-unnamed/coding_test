#include <bits/stdc++.h>
using namespace std;
long long n, r, c, ans;
void rec(long long r, long long c, long long n, long long &ans){
	long long tmpn = n / 2;
	long long block = (n / 2) * (n / 2);
	if(r <= tmpn && c <= tmpn){
		if(n == 2) ans += 1;
		else{
			rec(r, c, tmpn, ans);
		}
	}else if(r <= tmpn && c > tmpn){
		if(n == 2) ans += 2;
		else{
			ans += block;
			rec(r, c - tmpn, tmpn, ans);
		}
	}else if(r > tmpn && c <= tmpn){
		if(n == 2) ans += 3;
		else{
			ans += block * 2;
			rec(r - tmpn, c, tmpn, ans);
		}
	}else{ //r > tmpn && c > tmpn
		if(n == 2) ans += 4;
		else{
			ans += block * 3;
			rec(r - tmpn, c - tmpn, tmpn, ans);
		}
	}
}
int main(){
	cin >> n >> r >> c;
	n = pow(2, n);
	++r; ++c; ans = 0;
	rec(r,c,n,ans);
	cout << ans - 1;
	return 0;
}
