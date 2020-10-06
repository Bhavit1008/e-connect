#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);

// Complete the beautifulTriplets function below.

int main()
{
    int n, d;
cin >> n >> d;

vector<int> vals(n);
for (auto& val : vals)
    cin >> val;

auto exists = [&](int val)
{ return binary_search(begin(vals), end(vals), val); };

auto result = count_if(
    begin(vals), end(vals),
    [&](int val) {
        return exists(val + d) && exists(val + 2 * d);
    });

cout << result << endl;
}
