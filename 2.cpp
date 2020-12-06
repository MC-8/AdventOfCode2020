#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <regex>
#include <algorithm>

using namespace std;

const string inputname = "2.in";

string one(vector<string> & ls)
{
    int valid = 0;
    for (auto & l: ls)
    {
        regex r("(\\d+)-(\\d+) (\\S{1}): (\\S+)");
        smatch m;
        regex_search(l, m, r);
        int min_occ = stoi(m[1]);
        int max_occ = stoi(m[2]);
        string letter = m[3];
        string password = m[4];
        auto pwd_count = count(password.begin(), password.end(), letter[0]);
        if ((min_occ <= pwd_count) && (pwd_count <= max_occ))
        {
            valid++;
        }
    }
    return to_string(valid);
}

string two(vector<string> & ls)
{
    int valid = 0;
    for (auto & l: ls)
    {
        regex r("(\\d+)-(\\d+) (\\S{1}): (\\S+)");
        smatch m;
        regex_search(l, m, r);
        int min_occ = stoi(m[1]);
        int max_occ = stoi(m[2]);
        string letter = m[3];
        string password = m[4];
        auto pwd_count = count(password.begin(), password.end(), letter[0]);
        if ((password[min_occ-1]==letter[0]) ^ (password[max_occ-1]==letter[0]) )
        {
            valid++;
        }
    }
    return to_string(valid);
}


int main(int argc, char **kwargs)
{
    ifstream infile(inputname);
    string line;
    vector<string> ls;
    while( getline( infile, line ) ) // for each line read from the file
    {
        ls.push_back(line);
    }

    cout << "one = " << one(ls) << '\n'; // 603
    cout << "two = " << two(ls) << '\n'; // 404

    return 0;
}
