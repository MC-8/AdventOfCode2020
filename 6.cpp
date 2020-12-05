#include "aoc.hpp"

using namespace std;

const string inputname = "6.in";
using input_list_t = set<int>;
using solution_t = int;

solution_t one(input_list_t & sids)
{
    return -1;
}

solution_t two(input_list_t & sids)
{
    return -1;
}

set<int> sids;
int main(int argc, char **kwargs)
{
    ifstream infile(inputname);
    string s;
    while( getline( infile, s ) )
    {
        //
    }
         
    std::cout << "one = " << one(sids) << '\n'; // 980
    std::cout << "two = " << two(sids) << '\n'; // 607

    return 0;
}

