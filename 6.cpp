#include "aoc.hpp"

using namespace std;

const string inputname = "6.in";
using pass_answ_t = char;
using group_answ_t = set<pass_answ_t>;
using input_list_1_t = vector<group_answ_t>;
using input_list_2_t = vector<input_list_1_t>;
using sol_t = int;

sol_t one(const input_list_1_t & ls)
{
    sol_t tot = 0;
    for (auto & l: ls)
    {
        tot+= l.size();
    }
    return tot;
}

sol_t two(const input_list_2_t & ls)
{
    sol_t tot = 0;
    for (auto & ll: ls)
    {
        if (ll.empty()) continue;
        group_answ_t sint = ll[0];
        for (auto & s: ll)
        {
            if (!s.empty() && !sint.empty())
            {
                group_answ_t sint_temp{};
                std::set_intersection(sint.begin(), sint.end(),
                                      s.begin(), s.end(),
                                      std::inserter(sint_temp, sint_temp.begin()));
                sint = sint_temp;
            }
        }
        tot += sint.size();
    }
    return tot;
}

set<int> sids;
int main(int argc, char **kwargs)
{
    ifstream infile(inputname);
    string s;
    group_answ_t q{};
    input_list_1_t l1;
    input_list_1_t l2;
    input_list_2_t l3;
    
    while( getline( infile, s ) ) // for each line read from the file
    {
        for (char & c: s)
        {
            if (c)
            {
                q.insert(c);
            }
        }
        if (s=="")
        {
            l1.push_back(q);
            q = {};
        }
    }
    l1.push_back(q);
    q = {};
    infile.clear();
    infile.seekg(0);
    while( getline( infile, s ) ) // for each line read from the file
    {
        for (char & c: s)
        {
            if (c)
            {
                q.insert(c);
            }
        }
        l2.push_back(q);
        q = {};
        if (s=="")
        {
            l3.push_back(l2);
            l2 = {};
        }
    }
    l3.push_back(l2);
         
    std::cout << "one = " << one(l1) << '\n'; // 6249
    std::cout << "two = " << two(l3) << '\n'; // 3103

    return 0;
}

