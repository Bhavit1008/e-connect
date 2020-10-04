#include <bits/stdc++.h>

using namespace std;

// Complete the pangrams function below.
string pangrams(string s) {
    transform(s.begin(),s.end(),s.begin(),::tolower);
    cout<<s;
    set<char> s_set(s.begin(),s.end());
    if(s_set.size() == 27){
        return "pangram";
    }
    else{
        return "not pangram";
    }
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    string result = pangrams(s);

    fout << result << "\n";

    fout.close();

    return 0;
}
