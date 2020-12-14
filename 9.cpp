#include "aoc.hpp"

using namespace std;

const string inputname = "9.in";
using sol_t = long long;
using num_t = long long;
using mem_t = vector<num_t>;
using buff_t = deque<num_t>;

num_t any_2_sum(buff_t b, num_t n)
{
    for (size_t i = 0; i < b.size(); ++i)
    {
        for (size_t j = 0; j < b.size(); ++j)
        {
            if ((i!=j) && (b[i]+b[j]==n))
            {
                return n;
            }
        }
    }
    return -1;
}

sol_t one(mem_t & mem)
{
    constexpr int maxlen = 25;
    deque<num_t> buff{};
    for (auto & n: mem)
    {
        if (buff.size()==maxlen)
        {
            if (!(any_2_sum(buff,n)==n))
            {
                return n;
            }
            buff.pop_front();
        }
        buff.push_back(n);
    }
    return -1;
}


sol_t two(mem_t & mem, num_t n)
{
    buff_t s;
    for (auto &x: mem)
    {
        s.push_back(x);
        while(accumulate(s.begin(), s.end(), 0) > n)
        {
            s.pop_front();
        }
        if (accumulate(s.begin(), s.end(), 0)==n)
        {
            return(min_element(s.begin(), s.end())[0] + max_element(s.begin(), s.end())[0]);
        }
    }
    return -1;
}

mem_t mem{};

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
        // cout << s << '\n';
        mem.push_back(stoll(s));
    }
    cout << "one = " << one(mem) << '\n'; // 1492208709
    cout << "two = " << two(mem, one(mem)) << '\n'; // 238243506

    return 0;
}

