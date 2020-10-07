#include <bits/stdc++.h>

using namespace std;

// Complete the stringConstruction function below.
int stringConstruction(string s) {
    string p = "";
    int c = 0;
    for(int i=0;i<s.size();i++){
        if(p.find(s[i]) != std::string::npos){
            
        }
        else{
            p = p + s[i];
            c = c + 1;
        }
    }
    return c;
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

        int result = stringConstruction(s);

        fout << result << "\n";
    }

    fout.close();

    return 0;
}
