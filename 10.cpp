#include "aoc.hpp"

using namespace std;

const string inputname = "10.in";
using sol_t = long long;
using joltage_t = long long;
using bag_t = vector<joltage_t>;


sol_t one(bag_t & bag)
{
    sol_t one_diffs = 0;
    sol_t three_diffs = 0;
    joltage_t current_jolt = 0;
    bag_t l = bag;
    for (auto x = 1LL; x < (max_element(l.begin(), l.end())[0]+1); ++x)
    {
        if (find(l.begin(), l.end(), current_jolt+1) != l.end())
        {
            ++one_diffs;
            l.erase(find(l.begin(), l.end(),current_jolt+1));
            current_jolt+=1;
        }
        else if (find(l.begin(), l.end(), current_jolt+2) != l.end())
        {
            l.erase(find(l.begin(), l.end(),current_jolt+2));
            current_jolt+=2;
        }
        else if (find(l.begin(), l.end(), current_jolt+3) != l.end())
        {
            ++three_diffs;
            l.erase(find(l.begin(), l.end(),current_jolt+3));
            current_jolt+=3;
        }
    }
    return one_diffs*(three_diffs+1); // +1 to include the final jump
}


sol_t two(bag_t & bag, joltage_t n)
{
    bag_t sl = bag;
    sl.push_back(max_element(bag.begin(), bag.end())[0]);
    sl.push_back(0);
    sort(sl.begin(), sl.end());
    vector<joltage_t> ones_count{};
    vector<long long> exps{};
    int e = 0;
    for (size_t i = 0; i < sl.size()-1; ++i)
    {
        if (sl[i+1] - sl[i] == 1)
        {
            e+=1;
        }
        else
        {
            if (e>1)
            {
                ones_count.push_back(e-1);
            }
            e = 0;
        }
    }
    for (auto & x: ones_count)
    {
        exps.push_back(pow(2,x)-max(0LL,x-2));
    }
    return accumulate(exps.begin(), exps.end(), 1LL, multiplies<long long>());
}

bag_t bag{};

int main(int argc, char **kwargs)
{
    ifstream infile(inputname);
    string s;
    string chars = "\n\r";

    while( getline( infile, s ) ) // for each line read from the file
    {
        for (char c: chars)
        {
            s.erase(remove(s.begin(), s.end(), c), s.end());
        }
        bag.push_back(stoll(s));
    }
    cout << "one = " << one(bag) << '\n';           // 2516
    cout << "two = " << two(bag, one(bag)) << '\n'; // 296196766695424

    return 0;
}

