#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;
int one(vector<int> const& in);
int two(vector<int> const& in);

const string inputname = "1.in";

int main(int argc, char **kwargs)
{
    ifstream infile(inputname);
    string line;
    vector<int> ls;
    while (infile >> line)
    {
        ls.push_back(std::stoi(line));
    }

    cout << "one = " << one(ls) << '\n';
    cout << "two = " << two(ls) << '\n';

    return 0;
}

int one(vector<int> const& ls)
{
    for (int i = 0; i < ls.size(); ++i)
    {
        for (int j = 0; j < ls.size(); ++j) 
        {
            if ((i!=j) && (ls[i]+ls[j] == 2020))
            {
                return ls[i]*ls[j];
            }
        }
    }
    return -1;
}

int two(vector<int> const& ls)
{
    for (int i = 0; i < ls.size(); ++i)
    {
        for (int j = 0; j < ls.size(); ++j) 
        {
            for (int k = 0; k < ls.size(); ++k) 
            {
                if ((i!=j) && (j!=k) && (ls[i]+ls[j]+ls[k] == 2020))
                {
                    return ls[i]*ls[j]*ls[k];
                }
            }
        }
    }
    return -1;
}