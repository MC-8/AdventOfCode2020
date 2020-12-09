#include "aoc.hpp"

using namespace std;

const string inputname = "8.in";
using sol_t = int;
using instruction_t = std::pair<std::string,int>;
using program_t = std::vector<instruction_t>;

sol_t one(program_t & program)
{
    int acc = 0;
    int idx = 0;
    auto ni = program[idx];
    set<int> executed{};
    while (executed.find(idx)==executed.end())
    {
        if (program[idx].first == "acc")
        {
            acc += program[idx].second;
            executed.insert(idx);
            ++idx;
        }
        else if (program[idx].first == "nop")
        {
            executed.insert(idx);
            ++idx;
        }
        else if (program[idx].first == "jmp")
        {
            executed.insert(idx);
            idx+=program[idx].second;
        }
        else
        {
            std::cout << "INVALID INSTRUCTION AT LINE: " << idx << '\n';
        }
    }
    return acc;
}

std::pair<int,int> run_and_change(program_t program, int idx_c )
{
    if (program[idx_c].first == "nop")
    {
        program[idx_c].first = "jmp";
    }
    if (program[idx_c].first == "jmp")
    {
        program[idx_c].first = "nop";
    }
    int acc = 0;
    int idx = 0;
    int ni = program[idx].second;
    int li = idx;
    
    std::set<int> executed{};
    while ((executed.find(idx)==executed.end()) && (idx < program.size()) || (idx==(program.size()-1)))
    {
        if (program[idx].first == "acc")
        {
            acc += program[idx].second;
            executed.insert(idx);
            li = idx;
            ++idx;
        }
        else if (program[idx].first == "nop")
        {
            executed.insert(idx);
            li = idx;
            ++idx;
        }
        else if (program[idx].first == "jmp")
        {
            executed.insert(idx);
            li = idx;
            idx+=program[idx].second;
        }
        else
        {
            std::cout << "INVALID INSTRUCTION AT LINE: " << idx << '\n';
        }
    }
    return std::pair<int, int>{acc, li};
}

sol_t two(program_t & program)
{
    for (int i = 0; i < program.size()-1; ++i)
    {
        auto p = run_and_change(program, i);
        if (p.second==program.size()-1)
        {
            return p.first;
        }
    }
    return 0;
}

program_t program{};

int main(int argc, char **kwargs)
{
    ifstream infile(inputname);
    string s;
    while( getline( infile, s ) ) // fo r each line read from the file
    {
        auto pieces = split_string(s, ' ');
        instruction_t instruction{pieces[0],stoi(pieces[1])};
        program.push_back(instruction);
    }
    std::cout << "one = " << one(program) << '\n'; // 1217
    std::cout << "two = " << two(program) << '\n'; // 501

    return 0;
}

