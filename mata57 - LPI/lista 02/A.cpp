#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int N;
    cin >> N;
    cin.ignore(); 

    vector<string> playlist;

    for (int i = 0; i < N; i++) {
        string musica;
        getline(cin, musica);
        playlist.push_back(musica);
    }

    sort(playlist.begin(), playlist.end());

    for (const string& musica : playlist) {
        cout << musica << endl;
    }

    return 0;
}
