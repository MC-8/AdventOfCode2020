#include "aoc.hpp"

const string inputname = "15.in";
using num_t = unsigned long long;
using sol_t = num_t;
using num_list_t = vector<num_t>;

sol_t one(const num_list_t & ls)
{
    sol_t sol = 0;
    num_list_t to_speak = ls;
    num_list_t spoken = {};
    for (size_t i=0; i <2020; ++i)
    {
        if (i<to_speak.size())
        {
            spoken.push_back(to_speak[i]);
        }
        else
        {
            // Last element is new
            bool found = false;
            int distance = 0;
            for (int i = spoken.size()-2, j=1; i >=0 ; --i,++j)
            {
                if (spoken[spoken.size()-1]==spoken[i])
                {
                    found = true;
                    distance = j;
                    break;
                }
            }
            if (!found)
            {
                spoken.push_back(0);
            }
            else
            {
                spoken.push_back(distance);
            }
        }
    }
    return *spoken.rbegin();
}

sol_t two(const num_list_t & ls)
{
    sol_t sol = 0;
    num_list_t to_speak = ls;
    num_list_t spoken = {};
    unordered_map<num_t,num_t> d{};
    auto start = chrono::system_clock::now();
    auto last=-1;
    auto first_time = true;
    auto last_index = 0;
    auto n = 0;
    constexpr auto IMAX = 30'000'000ULL;
    for (size_t i=0; i <IMAX; ++i)
    {
        if (i<to_speak.size())
        {
            n = to_speak[i];
        }
        else
        {
            if (first_time)
            {
                n = 0;
            }
            else
            {
                n = d[last]-last_index;
            }
        }
        first_time = d.find(n)==d.end();
        if (!first_time)
        {
            last_index = d[n];
        }
        d[n]=i;
        last = n;
        // Show progress
        if ((chrono::duration_cast<chrono::milliseconds>(chrono::system_clock::now() - start).count() > 250) ||
            (i==IMAX-1))
        {
            printProgress((double)(i+1)/IMAX);
            start=chrono::system_clock::now();
        };
    }
    cout << '\n';
    return last;
}

int main()
{
    ifstream infile(inputname);
    string s;
    num_list_t ls{};
    string chars = "\n\r";
    regex e("(\\d+)");
    while( getline( infile, s ) ) // for each line read from the file
    {
        // default constructor = end-of-sequence:
        std::regex_token_iterator<std::string::iterator> rend;
        std::regex_token_iterator<std::string::iterator> a ( s.begin(), s.end(), e );
        // Empty line, start a new dictionary
        while (a!=rend)
        {
            ls.push_back(stoull(*a++));
        }
    }
    cout << "one = " << one(ls) << '\n'; //
    auto twores = two(ls);
    cout << "two = " << twores << '\n'; // 
    return 0;
}