#include <bits/stdc++.h>

using namespace std;

// Complete the marsExploration function below.
int marsExploration(string s) {
    int l = s.size();
    int no = l/3;
    string msg = "";
    int c =0;
    for(int i=0;i<no;i++){
        msg = "SOS" + msg;
    }

    for (int i=0;i<l;i++){
        if(s[i] != msg[i]){
            c = c + 1;
        }
    }

    cout<< msg;
    return c;

}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    int result = marsExploration(s);

    fout << result << "\n";

    fout.close();

    return 0;
}
