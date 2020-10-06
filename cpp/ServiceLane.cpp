#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);

// Complete the serviceLane function below.

int main()
{
    int n;
    int t;
    cin >> n >> t;
    vector<int> width(n);
    for(int width_i = 0;width_i < n;width_i++){
        cin >> width[width_i];
    }
    for(int a0 = 0; a0 < t; a0++){
        int i;
        int j;
        cin >> i >> j;
        int pass = INT_MAX;
        for(int l = i; l  <= j; l++){
            if(width[l] <= pass)pass = width[l];
        }
        cout << pass << endl;
    }
    return 0;
}
