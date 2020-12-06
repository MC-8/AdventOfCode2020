#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <regex>
#include <algorithm>

using namespace std;

const string inputname = "3.in";

int count_trees(vector<string> & ls, int right_inc, int down_inc)
{
    int col=0, row=0, trees=0;
    int h = ls.size();
    int w = ls[0].length();
    while (row+down_inc<h)
    {
        if (ls[row][col%w]=='#')
        {
            trees+=1;
        }
        row+=down_inc;
        col+=right_inc;
    }
    return trees;
}

string one(vector<string> & ls)
{
    return to_string(count_trees(ls, 3, 1));
}

string two(vector<string> & ls)
{
    int x = 1;
    vector<vector<int>> pairs = {{1,1},{3,1},{5,1},{7,1},{1,2}};
    for (auto & p: pairs) 
    {
        x *= count_trees(ls, p[0], p[1]);
    }
    return to_string(x);
}


int main(int argc, char **kwargs)
{
    ifstream infile(inputname);
    string s;
    vector<string> ls;
    std::string chars = "\n\r";

    while( getline( infile, s ) ) // for each line read from the file
    {
        for (char c: chars)
        {
            s.erase(std::remove(s.begin(), s.end(), c), s.end());
        }
        ls.push_back(s);
    }

    cout << "one = " << one(ls) << '\n'; // 164
    cout << "two = " << two(ls) << '\n'; // 5007658656

    return 0;
}
