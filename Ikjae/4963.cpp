#include <bits/stdc++.h>
using namespace std;
int main(){
	int w, h,i,j;
	bool done = false;
	int m[50][50];
	int nx[] = {1, 1, 1, 0, 0, -1, -1, -1};
	int ny[] = {-1, 0, 1, -1, 1, -1, 0, 1};
	while(!done){
		cin >> w >> h;
		stack<int> s;
		if(w == 1 && h == 1){
			cin >> m[0][0];
			if(m[0][0] == 0) cout << 0 << "\n";
			else cout << 1 <<"\n";
		}else if(w == 0 && h == 0){
			done = true;
		}else{
			int c=0;
			for(i=0;i<h;++i){
				for(j=0;j<w;++j){
					cin >> m[i][j];
					if(m[i][j] == 1) ++c;
				}
			}
			for(i=0;i<h;++i){
				for(j=0;j<w;++j){
					if(m[i][j] == 1){
						s.push(i * w + j);
						m[i][j] = c;
						--c;
					}
				}
			}
			int x,y;
			while(!s.empty()){
				x = s.top() / w;
				y = s.top() % w;
				s.pop();
				for(i=0;i<8;++i){
					if(x + nx[i] >= 0 &&
							x + nx[i] < h &&
							y + ny[i] >= 0 &&
							y + ny[i] < w &&
							m[x + nx[i]][y + ny[i]] > m[x][y]){
						m[x + nx[i]][y + ny[i]] = m[x][y];
						s.push( (x + nx[i]) * w + y + ny[i]);
					}
				}
			}
			set<int> ans;
			for(i=0;i<h;++i){
				for(j=0;j<w;++j){
					if(m[i][j] != 0) ans.insert(m[i][j]);
				}
			}
			cout << ans.size() << "\n";
		}
	}
	return 0;
}
