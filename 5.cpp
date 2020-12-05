#include "aoc.hpp"

using namespace std;

const string inputname = "5.in";
using input_list_t = set<int>;
using solution_t = int;

solution_t one(input_list_t & sids)
{
    // set is implemented with ascending order by specification
    // So the last element (right-begin) is the highest
    return *sids.rbegin();
}

solution_t two(input_list_t & sids)
{
    // Scan the set from the min to max values in the set until the missing
    // element is found
    for (int X=*sids.begin(); X <= *sids.rbegin(); ++X)
    {
        if (sids.find(X) == sids.end())
        {
            return(X);
        }
    }
    return(0);
}

set<int> sids;
int main(int argc, char **kwargs)
{
    ifstream infile(inputname);
    string s;
    while( getline( infile, s ) )
    {
        std::replace( s.begin(), s.end(), 'F','0'); 
        std::replace( s.begin(), s.end(), 'B','1'); 
        std::replace( s.begin(), s.end(), 'L','0'); 
        std::replace( s.begin(), s.end(), 'R','1'); 
        sids.insert(bin_str_to_int(s));
    }
         
    std::cout << "one = " << one(sids) << '\n'; // 980
    std::cout << "two = " << two(sids) << '\n'; // 607

    return 0;
}

