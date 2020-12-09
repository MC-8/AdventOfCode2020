#include "aoc.hpp"

using namespace std;

const string inputname = "7.in";
using bag_t = string;
using tree_bag_t = unordered_map<bag_t, vector<pair<bag_t,int>>>;
using sol_t = int;
tree_bag_t tree_bag;
sol_t one()
{
    std::set<bag_t> wcsg{};
    std::set<bag_t> to_find{"shiny gold"};
    bool repeat = true;
    while (repeat)
    {
        repeat = false;
        for (auto & r: tree_bag)
        {
            for (auto & c: tree_bag[r.first])
            {
                if ((to_find.find(c.first)!=to_find.end()) &&
                    (to_find.find(r.first)==to_find.end()))
                {
                    wcsg.insert(r.first);
                    to_find.insert(r.first);
                    repeat = true;
                }
            }
        }
    }
    return wcsg.size();
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
    bag_t s, key, bag_name;
    regex rc("(\\d)|(\\S+ \\S+)(?:(?!bags contain)\\w)+"); // it should not work, but it sort of does  [muted white] [bags contain] [3] [muted tomato] [5] [light black] [4] [pale black] [5] [shiny gold]
    while( getline( infile, s ) ) // fo r each line read from the file
    {
        std::regex_token_iterator<std::string::iterator> rend;
        std::regex_token_iterator<std::string::iterator> b ( s.begin(), s.end(), rc);
        bag_t parent = *b++;
        //skip "bags contain", god forbid I managed to remove with the regex
        b++;
        vector<pair<bag_t,int>> child_bags{};

        if ((*b).str()!="no other")
        {
            while (b!=rend)
            {
                pair<bag_t,int> bp;
                bp.second = stoi((*b++).str());
                bp.first = (*b++).str();
                child_bags.push_back(bp);
            }
        }
        tree_bag[parent] = child_bags;
    }
    std::cout << "one = " << one() << '\n'; // 
    std::cout << "two = " << two() << '\n'; // 

    return 0;
}

