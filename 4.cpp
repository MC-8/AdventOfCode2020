#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <regex>
#include <algorithm>
#include <unordered_map>
#include <set>

using namespace std;
using my_key_t = string;
using my_val_t = string;
using passport_field_value_t = unordered_map<my_key_t,my_val_t>;

const string inputname = "4.in";

bool is_numeric(string s)
{
    return !s.empty() && s.find_first_not_of("0123456789") == std::string::npos;
}

bool validate_byr(string x)
{
    return (x.size()==4) && is_numeric(x) && ((1920<=stoi(x))&&(stoi(x)<=2002));
}

bool validate_iyr(string x)
{
    return (x.size()==4) && is_numeric(x) && ((2010<=stoi(x))&&(stoi(x)<=2020));
}

bool validate_eyr(string x)
{
    return (x.size()==4) && is_numeric(x) && ((2020<=stoi(x))&&(stoi(x)<=2030));
}

bool validate_hgt(string x)
{
    bool valid = false;
    if ((x.size()==4) or (x.size()==5))
    {
        int val = stoi(x.substr(0, x.size()-2));
        if (x.find("in") != std::string::npos)
        {
            valid = (59 <= val) && (val <= 76);
        }
        else if (x.find("cm") != std::string::npos)
        {
            valid = (150 <= val) && (val <= 193);
        }
    }
    return valid;
}

bool validate_hcl(string x)
{
    return regex_search(x,regex{"#([a-f0-9]{6})"});
}

bool validate_ecl(string x)
{
    std::set<string> colours{"amb","blu","brn","gry","grn","hzl","oth"};
    return colours.find(x) != colours.end();
}

bool validate_pid(string x)
{
    return (x.size()==9) && (is_numeric(x));
}

bool validate_cid(string x)
{
    return true;
}


typedef bool (*validator_fcn_t)(string);

unordered_map<string, validator_fcn_t> val_fun = {
    {"byr", validate_byr},
    {"iyr", validate_iyr},
    {"eyr", validate_eyr},
    {"hgt", validate_hgt},
    {"hcl", validate_hcl},
    {"ecl", validate_ecl},
    {"pid", validate_pid},
    {"cid", validate_cid},
    };

int one(vector<passport_field_value_t> & ls)
{
    int valid = 0;
    for (auto & d: ls)
    {
        std::vector<my_key_t> keys;
        keys.reserve(d.size());
        std::vector<my_val_t> vals;
        vals.reserve(d.size());

        for(auto & kv : d)
        {
            keys.push_back(kv.first);
            vals.push_back(kv.second);
        }
        
        if ((keys.size() == 8) ||
            ((keys.size() == 7) && ( std::find(keys.begin(), keys.end(), "cid") == keys.end() )))
        {
            valid += 1;
        }
    }
    return (valid);
}

int two(vector<passport_field_value_t> & ls)
{
    int valid = 0;
    for (auto & d: ls)
    {
        std::vector<my_key_t> keys;
        keys.reserve(d.size());
        std::vector<my_val_t> vals;
        vals.reserve(d.size());

        for(auto & kv : d)
        {
            keys.push_back(kv.first);
            vals.push_back(kv.second);
        }
        
        if ((keys.size() == 8) ||
            ((keys.size() == 7) && ( std::find(keys.begin(), keys.end(), "cid") == keys.end() )))
        {
            bool valid_flag = true;
            for(auto & kv : d)
            {
                valid_flag &= val_fun[kv.first](kv.second);
            }
            if (valid_flag)
            {
                ++valid;
            }
        }
    }
    return (valid);
}


int main(int argc, char **kwargs)
{
    ifstream infile(inputname);
    std::string chars = "\n\r";
    string s;
    passport_field_value_t d;
    vector<passport_field_value_t> ls;
    regex e("(\\S+):(\\S+)");
    while( getline( infile, s ) ) // for each line read from the file
    {
        // default constructor = end-of-sequence:
        std::regex_token_iterator<std::string::iterator> rend;

        int submatches[] = { 1, 2 };
        std::regex_token_iterator<std::string::iterator> c ( s.begin(), s.end(), e, submatches );
        // Empty line, start a new dictionary
        if (c==rend)
        {
            ls.push_back(d);
            d = {};
            continue;
        }
        while (c!=rend)
        {
            auto k = *c++;
            auto v = *c++;
            d[k] = v;
        }
    }
    // Last dictionary not yet added
    ls.push_back(d);
    
    std::cout << "one = " << one(ls) << '\n';
    std::cout << "two = " << two(ls) << '\n';

    return 0;
}

