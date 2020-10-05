#include <bits/stdc++.h>

using namespace std;

// Complete the theLoveLetterMystery function below.
int theLoveLetterMystery(string s) {
    //reversing the string
    string rev = string(s.rbegin(),s.rend()); 
    cout<<rev;
    int total=0;
    int n = s.size();
    for (int i = 0;i<n;i++){
        total += abs(s[i] - rev[i]);
    }
    return (total/2);
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int q;
    cin >> q;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    for (int q_itr = 0; q_itr < q; q_itr++) {
        string s;
        getline(cin, s);

        int result = theLoveLetterMystery(s);

        fout << result << "\n";
    }

    fout.close();

    return 0;
}
