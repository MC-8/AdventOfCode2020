#include "aoc.hpp"

const string inputname = "13.in";
using bus_t = int;
using timetable_t = vector<bus_t>;
using sol_t = double;
using timestamp_t = int;
using bus_offset_pair_t = pair<int,int>;

sol_t one(const timetable_t & tt, const timestamp_t T)
{
    auto wait_time = 1e9;
    auto bus_nr = 0;
    for (auto & bus_line: tt)
    {
        auto new_wait = 1e9;
        if (bus_line!=0)
        {
            new_wait = bus_line - T%bus_line;
        }
        if (new_wait < wait_time)
        {
            wait_time = new_wait;
            bus_nr = bus_line;
        }
    }
    return bus_nr*wait_time;
}

pair<bool,timestamp_t> ok_mod(sol_t base, timestamp_t n, timestamp_t mod)
{
    if (base<n)
    {
        return make_pair(false,n);
    }
    else
    {
        return make_pair(fmod(base+mod,n)==0,n);
    }
    
}

sol_t two(const timetable_t & tt)
{
    vector<bus_offset_pair_t> bus_offset_pairs{};
    set<bus_offset_pair_t> to_jmp{};
    set<bus_offset_pair_t> tmp_jmp{};
    set<timestamp_t> succ_base{};
    for (auto [i, b]: enumerate(tt))
    {
        if(b>0)
        {
            bus_offset_pair_t pbi = make_pair(b,i);
            bus_offset_pairs.push_back(pbi);
            to_jmp.insert(pbi);
            tmp_jmp.insert(pbi);
        }
    }
    auto allmods_ok = false;
    sol_t base = 0;
    while (!allmods_ok)
    {
        allmods_ok = true;
        for (auto & bop: to_jmp)
        {
            auto [res, inc_base] = ok_mod(base, bop.first, bop.second);
            if (res)
            {
                succ_base.insert(inc_base);
                tmp_jmp.erase(bop); //erase(remove(tmp_jmp.begin(), tmp_jmp.end(), bop), tmp_jmp.end());
            }
            allmods_ok &= res;
        }
        to_jmp = tmp_jmp;
        // copy(tmp_jmp.begin(), tmp_jmp.end(), to_jmp.begin());
        if (!allmods_ok)
        {
            sol_t prod = 1;
            for (auto & x: succ_base) //13,19,23,37,41
            {
                prod*=x;
            }
            base+= prod; //0,1,2,3... ~20 -> 322, 621, 11684, 465267, 9083344
        }
    }
    return base;
}

int main()
{
    ifstream infile(inputname);
    string s;
    string chars = "\n\r";
    std::regex e ("(\\d+)|(x)");
    timestamp_t T;
    regex_token_iterator<string::iterator> rend;
    getline( infile, s );
    std::regex_token_iterator<std::string::iterator> a ( s.begin(), s.end(), e );
    T = stoi(*a);
    getline( infile, s );
    std::regex_token_iterator<std::string::iterator> b ( s.begin(), s.end(), e );
    timetable_t timetable{};
    while (b!=rend)
    {
        auto val = *b++;
        if (val.str()=="x")
        {
            timetable.push_back(0);
        }
        else
        {
            timetable.push_back(stoi(val));
        }
        
    } 

    cout << "one = " << one(timetable, T) << '\n'; // 2298
    cout << "two = " << setprecision(16) << two(timetable) << '\n'; // 783685719679632
    return 0;
}