#include "aoc.hpp"

using namespace std;

const string inputname = "7.in";
using bag_t = string;
using tree_bag_t = unordered_map<bag_t, vector<pair<bag_t,int>>>;
using sol_t = int;
tree_bag_t tree_bag;
sol_t one()
{
    sol_t tot = 0;
    return tot;
}

int count_bags_in(bag_t bag)
{
    auto children = tree_bag[bag];
    int sum = 0;
    for (auto & c: children)
    {
        sum += c.second*(1+count_bags_in(c.first));
    }
    return sum;
}

sol_t two()
{
    return count_bags_in("shiny gold");
}


int main(int argc, char **kwargs)
{
    ifstream infile(inputname);
    string s, key, bag_name;
    regex e("((\\S+ \\S+) (?:bags? contain){1}|(\\d) (\\S+ \\S+) (?:bags?))");
    while( getline( infile, s ) ) // for each line read from the file
    {
        // default constructor = end-of-sequence:
        std::regex_token_iterator<std::string::iterator> rend;

        int submatches[] = {2, 3, 4, 5 };
        std::regex_token_iterator<std::string::iterator> c ( s.begin(), s.end(), e, submatches );
        
        // Empty line, start a new dictionary
        vector<pair<bag_t,int>> child_bags{};
        while (c!=rend)
        {
            bag_name = *c++;
            (void)bag_name;
            key = bag_name;
            // int bag_nr = stoi(string(*c++));
            // child_bags.push_back(make_pair(bag_name.first, bag_nr.second));
        }
        // tree_bag[key] = child_bags;
    }
    return stoi(key);
    std::cout << "one = " << one() << '\n'; // 
    std::cout << "two = " << two() << '\n'; // 

    return 0;
}

