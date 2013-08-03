// Project Euler - Problem 15: Lattice paths
// http://projecteuler.net/problem=15

#include <iostream>

using namespace std;

// Function to find combinations (courtesy of Donald Knuth)
uint64_t Combinations(unsigned int n, unsigned int k)
{
	if (k > n)
	     return 0;
	uint64_t r = 1;
	for (unsigned int d = 1; d <= k; ++d)
	{
	    r *= n--;
	    r /= d;
	}
	return r;
}

int main()
{
	const int max_size = 20;
	uint64_t result = 0, tmp_result;

	// For each 20 C k  way of getting to the bottom of the grid, there are
	// 20 C k  ways to get to the right of the grid
	for (int i=0; i<=max_size; ++i)
	{
		tmp_result = Combinations(max_size, i);
		result += tmp_result*tmp_result;
	}

	cout << "Result = " << result << endl;

	return result;

}
