#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <regex>
#include <algorithm>
#include <unordered_map>
#include <set>
#include <deque>
#include <numeric>
#include <cmath>
#include <functional>

using namespace std;

bool is_numeric(string s)
{
    return !s.empty() && s.find_first_not_of("0123456789") == string::npos;
}

int bin_str_to_int(string s)
{
    return static_cast<int>(bitset<32>(s).to_ulong());
}

std::vector<std::string> split_string(const std::string& str, char delim)
{
  std::vector<std::string> tokens;
  
  if (str == "") return tokens;
  
  std::string currentToken;
  
  std::stringstream ss(str);
  
  while (std::getline(ss, currentToken, delim))
  {
    tokens.push_back(currentToken);
  }
  
  return tokens;
}