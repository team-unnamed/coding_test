#include<bits/stdc++.h>
using namespace std;

vector<string> coin;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int answer = 400;

	int N;
	cin >> N;

	string s;
	for (int i = 0; i < N; i++) {
		cin >> s;
		coin.push_back(s);
	}

	for (int bit = 0; bit < (1 << N); bit++) {
		vector<vector<char> > v2(N, vector<char>(N, '0'));

		for (int i = 0; i < N; i++) { // ���� �������� ������ ������ ��� ����� ���� ����
			if (bit & (1 << i)) {
				for (int j = 0; j < N; j++) {
					if (coin[i][j] == 'H') v2[i][j] = 'T';
					else v2[i][j] = 'H';
				}
			}
			else {
				for (int j = 0; j < N; j++) {
					if (coin[i][j] == 'H') v2[i][j] = 'H';
					else v2[i][j] = 'T';
				}
			}
		}

		int cnt = 0;
		for (int i = 0; i < N; i++) { // ���� �������� ������ �������鼭 �޸��� ���� ���ϴ� ������ ������ �ּ�ȭ
			int t_cnt = 0, h_cnt = 0;
			for (int j = 0; j < N; j++) {
				if (v2[j][i] == 'T') t_cnt++;
				else h_cnt++;
			}
			cnt += (t_cnt < h_cnt) ? t_cnt : h_cnt;
		}

		answer = (cnt < answer) ? cnt : answer;
	}
	cout << answer;

	return 0;
}