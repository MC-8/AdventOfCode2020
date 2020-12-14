#include "aoc.hpp"

const string inputname = "11.in";
using sol_t = long long;
using joltage_t = long long;
using seat_map_t = vector<string>;

seat_map_t seat_map{{}};

sol_t one(seat_map_t lin)
{

    bool changeflag = true;
    auto cidc = 0;
    seat_map_t nl{};
    seat_map_t ls = lin;
    while (changeflag)
    {
        cidc += 1;
        cout << cidc << '\n';
        changeflag = false;
        auto ir = 0;
        auto ic = 0;
        nl = {};
        for (auto & row:ls)
        {
            auto r = "";
            ic = 0;
            for(auto & col: row)
            {
                if (*col=="L")
                {
                    auto count = 0;
                    vector<int> s{-1,0,1};
                    for (auto &dc: s)
                    {
                        for (auto &dr: s)
                        {
                            if ((ic+dc)==row.size()), break;
                            if ((ir+dr)==ls.size()), break;
                            if ((ir+dr)==-1), break;
                            if ((ic+dc)==-1), break;
                            if ((dc==dr) &&(dr==0)), break;
                            if (ls[ir+dr][ic+dc] == "#")
                            {
                                count+=1;
                            }
                        }
                    }
                    if (count==0)
                    {
                        r+="#";
                        changeflag = true;
                    }
                    else
                    {
                        r+="L"
                    }
                }
                else if (col=="#")
                {
                    auto count = 0;
                    vector<int> s{-1,0,1};
                    for (auto &dc: s)
                    {
                        for (auto &dr: s)
                        {
                            if (ic+dc)==len(row), break;
                            if (ir+dr)==len(ls), break;
                            if (ir+dr)==-1, break;
                            if (ic+dc)==-1, break;
                            if (dc==dr) &&(dr==0), break;
                            if ls[ir+dr][ic+dc] == "#"
                            {
                                count+=1;
                            }
                        }
                    }
                    if (count>=4)
                    {
                        r+="L";
                        changeflag = true;
                    }
                    else
                    {
                        r+="#";
                    }
                }
                else
                {
                    r+=ls[ir][ic];
                }
                ic+=1;
            }
            nl.push_back(r);
            ir+=1;
        }
        ls = nl;
    }
    auto cc = 0;
    for (auto & row: nl)
    {
        for (auto & col: row)
        {
            if (col == '#')
            {
                ++cc;
            }
        }
    }
    return cc;
}

sol_t two(seat_map_t lin)
{
    return 0;
}

int main()
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
        seat_map.push_back(s);
    }
    cout << "one = " << one(seat_map) << '\n'; // 
    cout << "two = " << two(seat_map) << '\n'; // 
    return 0;
}