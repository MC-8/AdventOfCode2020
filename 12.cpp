#include "aoc.hpp"

const string inputname = "12.in";
using cmd_t = pair<char,int>;
using program_t = vector<cmd_t>;
using seat_map_t = vector<string>;
using sol_t = int;

unordered_map<char,char> bl{{'E','N'},
                            {'N','W'},
                            {'W','S'},
                            {'S','E'}};
unordered_map<char,char> br{{'N','E'},
                            {'W','N'},
                            {'S','W'},
                            {'E','S'}};
program_t program{};

sol_t one(const program_t & program)
{
    auto facing = 'E';
    auto sE = 0;
    auto sN = 0;
    for (auto & x: program)
    {
        //cout << x.first << ' ' << x.second << '\n'; 
        //
        // I'll not use curly brackets in this switch to improve readability.
        // exactly one instruction is performed in for loops and if/then/else
        // conditions.
        switch (x.first) 
        { 
            case 'L':
                for (int i = 0; i < x.second/90; ++i) facing = bl[facing];
                break;
            case 'R':
                for (int i = 0; i < x.second/90; ++i) facing = br[facing];
                break;
            case 'F':
                if (facing=='E')        sE += x.second;
                else if (facing=='W')   sE -= x.second;
                else                    sE = sE;
                
                if (facing=='N')        sN += x.second;
                else if (facing=='S')   sN -= x.second;
                else                    sN = sN;
                
                break;
            default:
                if (x.first=='E')       sE += x.second;
                else if (x.first=='W')  sE -= x.second;
                else                    sE = sE;
                
                if (x.first=='N')       sN += x.second;
                else if (x.first=='S')  sN -= x.second;
                else sN =               sN;
                
                break;
        }
    }
    return abs(sE) + abs(sN);
}

sol_t two(const program_t & program)
{
    auto facing = 'E';
    auto wE = 10;
    auto wN = 1;
    auto sE = 0;
    auto sN = 0;
    for (auto & x: program)
    {
        //cout << x.first << ' ' << x.second << '\n'; 
        //
        // I'll not use curly brackets in this switch to improve readability.
        // exactly one instruction is performed in for loops and if/then/else
        // conditions.
        switch (x.first) 
        { 
            case 'L':
                for (int i = 0; i < x.second/90; ++i)
                {
                    swap(wE,wN);
                    wE *= -1;
                }
                break;
            case 'R':
                for (int i = 0; i < x.second/90; ++i)
                {
                    swap(wE,wN);
                    wN *= -1;
                }
                break;
            case 'F':
                sE += wE*x.second;
                sN += wN*x.second;
                break;
            default:
                if (x.first=='E')       wE += x.second;
                else if (x.first=='W')  wE -= x.second;
                else                    wE = wE;
                
                if (x.first=='N')       wN += x.second;
                else if (x.first=='S')  wN -= x.second;
                else                    wN = wN;
                
                break;
        }
    }
    return abs(sE) + abs(sN);
}

int main()
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
        program.push_back(make_pair((char)s[0], stoi(s.substr(1))));
    }
    cout << "one = " << one(program) << '\n'; // 
    cout << "two = " << two(program) << '\n'; // 
    return 0;
}