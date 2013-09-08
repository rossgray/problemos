/* Function to calculate how many characters need to be removed from a string before that
string is a palindrome */

#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int kPalindrome(string iStr)
{
    unsigned int i=0, j=iStr.size()-1, n1, n2;

    // if string is only one char long then return 0
    if (j==0)
        return 0;

    for (; i<j; ++i,--j)
    {
        // Work towards centre of string starting from each end
        // If chars are not the same, then consider kPalindrome by removing i and j
        // Take minimum result
        if (iStr[i]!=iStr[j])
        {
           string str = iStr.substr(i+1,j-i);
           n1 = kPalindrome(str);
           str = iStr.substr(i,j-i);
           n2 = kPalindrome(str);
           return 1+min(n1,n2);
        }        
    }

    // If we make it all the way into the centre then the string is a pure plaindrome
    // so we can return 0
    return 0;
}


int main()
{
    // Test

    cout << "afggfa = " << kPalindrome("afggfa") << endl;
    cout << "afgafa = " << kPalindrome("afgafa") << endl;
    cout << "afgfaic = " << kPalindrome("afgfaic") << endl;
    cout << "bfilfgfb = " << kPalindrome("bfilfgfb") << endl;
    cout << "abcde = " << kPalindrome("abcde") << endl;

}