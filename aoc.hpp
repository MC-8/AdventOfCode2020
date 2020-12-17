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
#include <iomanip>

using namespace std;

bool is_numeric(string s)
{
    return !s.empty() && s.find_first_not_of("0123456789") == string::npos;
}

int bin_str_to_int(string s)
{
    return static_cast<int>(bitset<32>(s).to_ulong());
}

unsigned long long bin_str_to_ull(string s)
{
    return static_cast<unsigned long long>(bitset<64>(s).to_ullong());
}

string int_to_bin_str(unsigned long long s)
{
    return static_cast<string>(bitset<32>(s).to_string());
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

// http://reedbeta.com/blog/python-like-enumerate-in-cpp17/
#include <tuple>

template <typename T,
          typename TIter = decltype(std::begin(std::declval<T>())),
          typename = decltype(std::end(std::declval<T>()))>
constexpr auto enumerate(T && iterable)
{
    struct iterator
    {
        size_t i;
        TIter iter;
        bool operator != (const iterator & other) const { return iter != other.iter; }
        void operator ++ () { ++i; ++iter; }
        auto operator * () const { return std::tie(i, *iter); }
    };
    struct iterable_wrapper
    {
        T iterable;
        auto begin() { return iterator{ 0, std::begin(iterable) }; }
        auto end() { return iterator{ 0, std::end(iterable) }; }
    };
    return iterable_wrapper{ std::forward<T>(iterable) };
}