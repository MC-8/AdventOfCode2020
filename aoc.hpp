#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <regex>
#include <algorithm>
#include <unordered_map>
#include <set>
using namespace std;

bool is_numeric(string s)
{
    return !s.empty() && s.find_first_not_of("0123456789") == string::npos;
}

int bin_str_to_int(string s)
{
    return static_cast<int>(bitset<32>(s).to_ulong());
}
