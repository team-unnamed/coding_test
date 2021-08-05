#include <bits/stdc++.h>
#define neg first
#define zero second.first
#define pos second.second

using namespace std;
int n, b[2188][2188];

void rec(int x, int y, int w, pair<int, pair<int, int>> &cnt){
	int i,j,endx,endy, cntn, cntp, cntz;
	i = x;
	j = y;
	endx = x + w;
	endy = y + w;
	cntn = cntp = cntz = 0;
	while((cntn == cntp || cntn == cntz || cntp == cntz) && i < endx){
		j = y;
		while((cntn==cntp || cntn==cntz || cntp==cntz) && j < endy){
			if(b[i][j] == 0) ++cntz;
			if(b[i][j] == 1) ++cntp;
			if(b[i][j] == -1) ++cntn;
			++j;
		}
		++i;
	}
	if(cntn == w * w){
		++cnt.neg;
	}else if(cntz == w * w){
		++cnt.zero;
	}else if(cntp == w * w){
		++cnt.pos;
	}else{
		w = w / 3;
		for(i=0;i<3;++i){
			for(j=0;j<3;++j){
				rec(x + i * w, y + j * w, w, cnt);
			}
		}
	}
}

int main(){
	ios_base::sync_with_stdio(false);
    	cin.tie(nullptr);
	cout.tie(nullptr);
	cin >> n;
	int i,j;
	for(i=1;i<=n;++i){
		for(j=1;j<=n;++j) cin >> b[i][j];
	}
	pair<int, pair<int, int>> cnt;
	cnt.neg = cnt.zero = cnt.pos = 0;
	rec(1, 1, n, cnt);
	cout << cnt.neg << "\n";
	cout << cnt.zero << "\n";
	cout << cnt.pos << "\n";
	return 0;
}
