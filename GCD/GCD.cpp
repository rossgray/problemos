// Function to compute the greatest common denominator of two positive integers

// Worst-case and average-case complexity of solution is O(log(n)), where n is the larger of a and b
// This is because by using the fact that GCD(a, b) == GCD(b, a mod b) and GCD(a, 0) = a
// we have a recursion, where at each step of the recursion, the size of the input parameters
// at least halves (due to the a % b), until one of them is equal to zero.


#include <iostream>

using namespace std;


int GCD(int a, int b)
{
    // check input parameters
    if (a < 0 || b < 0)
    {
        cout << "Invalid input parameters!" << endl;
        return 0;
    }

    // we can use the fact that GCD(a, 0) = a
    if (a == 0)
    {
        return b;
    }
    else if (b == 0)
    {
        return a;
    }

    // make sure a is the highest integer
    if (b > a)
    {
        int tmp = a;
        a = b;
        b = tmp;
    }

    // using fact that GCD(a, b) == GCD(b, a mod b)
    return GCD(b, a%b);

}


int main()
{
    cout << "GCD of 10000 & 6792 = " << GCD(10000,6792) << endl;
    cout << "GCD of 16 & 6 = " << GCD(16,6) << endl;
    cout << "GCD of 100 & 51 = " << GCD(100,51) << endl;
    cout << "GCD of 0 & 1 = " << GCD(0,1) << endl;
    cout << "GCD of 1 & 6 = " << GCD(1,6) << endl;
    cout << "GCD of 160 & 8 = " << GCD(160,8) << endl;
    cout << "GCD of 9 & 3 = " << GCD(9,3) << endl;
    cout << "GCD of -1 & 8 = " << GCD(-1,8) << endl;
    cout << "GCD of 16 & 4 = " << GCD(16,4) << endl;
}