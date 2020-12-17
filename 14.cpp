#include "aoc.hpp"

const string inputname = "14.in";
using num_t = unsigned long long;
using sol_t = num_t;
using mem_t = unordered_map<num_t, num_t>;
using mask_t = string;

num_t apply_mask(const string numstr, const string mask)
{
    string new_num{};
    for (int i = 0; i < mask.size(); ++i)
    {
        if ((mask[i]=='0') || (mask[i]=='1'))
        {
            new_num+=mask[i];
        }
        else
        {
            new_num+=numstr[i];
        }
    }
    return bin_str_to_ull(new_num);
}

vector<num_t> apply_mask2(const string numstr, const string mask)
{
    string new_num{};
    for (auto [i,n] : enumerate(mask))
    {
        if (n=='1')
        {
            new_num+='1';
        }
        else if (n=='0')
        {
            new_num+=numstr[i];
        }
        else
        {
            new_num+='X';
        }
    }
    auto nx = count( new_num.begin(), new_num.end(), 'X');
    vector<num_t> nums{};
    
    for (int poss=0; poss< pow(2,nx); ++poss)
    {
        string digits = static_cast<string>(bitset<36>(poss).to_string());
        digits = digits.substr(36-nx);
        auto idigit = 0;
        string new_addr = "";
        for (auto &d: new_num)
        {
            if (d=='X')
            {
                new_addr+=digits[idigit];
                ++idigit;
            }
            else
            {
                new_addr+=d;
            }
        }
        nums.push_back(bin_str_to_ull(new_addr));
    }
    return nums;
}


sol_t one()
{
    ifstream infile(inputname);
    string s;
    mem_t mem;
    getline( infile, s );
    bool loop = true;
    sol_t total = 0;
    while (loop)
    {
        regex e ("(mask = )(\\S+)");
        string msk;
        smatch matches;
        if(regex_search(s, matches, e))
        {
            msk = matches[2].str();
        }
        bool found;
        do
        {
            regex e ("\\[(\\d+)\\] \\= (\\d+)");
            if (!getline( infile, s )) 
            {
                loop = false;
                break;
            }
            found = regex_search(s, matches, e);
            if(found)
            {
                auto n_dec = matches[2].str();
                auto n_bin = static_cast<string>(bitset<36>(stoull(n_dec)).to_string());
                auto val = apply_mask(n_bin, msk);
                mem[stoull(matches[1].str())] =  val;
                // cout << stoull(matches[1].str()) << " : " << setprecision(36) << apply_mask(n_bin, msk) << '\n';
            }
        } while (found);
    }
    for (auto & x: mem)
    {
        total+=x.second;
    }
    return total;
}

sol_t two()
{
    ifstream infile(inputname);
    string s;
    mem_t mem;
    getline( infile, s );
    bool loop = true;
    sol_t total = 0;
    while (loop)
    {
        regex e ("(mask = )(\\S+)");
        string msk;
        smatch matches;
        if(regex_search(s, matches, e))
        {
            msk = matches[2].str();
        }
        bool found;
        do
        {
            regex e ("\\[(\\d+)\\] \\= (\\d+)");
            if (!getline( infile, s )) 
            {
                loop = false;
                break;
            }
            found = regex_search(s, matches, e);
            if(found)
            {
                auto n_dec = matches[1].str();
                auto n_bin = static_cast<string>(bitset<36>(stoull(n_dec)).to_string());
                auto addr = n_bin;
                auto new_addr = apply_mask2(addr, msk);
                n_dec = matches[2].str();
                n_bin = static_cast<string>(bitset<36>(stoull(n_dec)).to_string());
                auto val = n_bin;
                for (auto & a: new_addr)
                {
                    mem[a] = static_cast<unsigned long long>(bitset<36>(val).to_ullong());
                }
            }
        } while (found);
    }
    for (auto & x: mem)
    {
        total+=x.second;
    }
    return total;
}

int main()
{
    cout << "one = " << one() << '\n'; // 15018100062885
    cout << "two = " << two() << '\n'; // 5724245857696
    return 0;
}