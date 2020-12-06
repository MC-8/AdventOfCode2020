#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

const string inputname = "1.in";

template <typename T>
T one(vector<T> & ls)
{
    sort(ls.begin(), ls.end());
    for (int i = 0; i < ls.size(); ++i)
    {
        for (int j = i+1; j < ls.size(); ++j) 
        {
            if (ls[i]+ls[j] > 2020) break;
            if ((i!=j) && (ls[i]+ls[j] == 2020))
            {
                return ls[i]*ls[j];
            }
        }
    }
    return -1;
}

template <typename T>
T two(vector<T> & ls)
{
    sort(ls.begin(), ls.end());
    for (int i = 0; i < ls.size(); ++i)
    {
        for (int j = i+1; j < ls.size(); ++j) 
        {
            for (int k = j+1; k < ls.size(); ++k) 
            {
                if (ls[i]+ls[j]+ls[k] > 2020) break;
                if ((i!=j) && (j!=k) && (ls[i]+ls[j]+ls[k] == 2020))
                {
                    return ls[i]*ls[j]*ls[k];
                }
            }
        }
    }
    return -1;
}


int main(int argc, char **kwargs)
{
    ifstream infile(inputname);
    string line;
    vector<int> ls;
    while (infile >> line)
    {
        ls.push_back(std::stoi(line));
    }

    cout << "one = " << one(ls) << '\n'; // 494475
    cout << "two = " << two(ls) << '\n'; // 267520550

    return 0;
}
