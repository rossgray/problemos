// Push all the zero's of a given array to the end of the array. In place only.
// Ex 1,2,0,4,0,0,8 becomes 1,2,4,8,0,0,0

#include <iostream>

using namespace std;

void push_zeros(int* ioArr, int iLen)
{
    if (!ioArr || iLen < 1)
        return;

    int start0;

    // find first zero
    for (start0=0; start0<iLen; ++start0)
    {
        if (ioArr[start0] == 0)
            break;
    }

    // continuously swap non-zeros with first zero until we 
    // get to the end of the array
    for (int i=start0+1; i<iLen; ++i)
    {
        if (ioArr[i] != 0)
        {
            ioArr[start0] = ioArr[i];
            ioArr[i] = 0;
            start0++;
        }
    }

    return;
}

void print_arr(int* iArr, int iLen)
{
    for (int i=0; i<iLen; ++i)
    {
        cout << iArr[i] << ", ";
    }
    cout << endl;
}


int main()
{
    const int arr_len = 15; 
    int arr[arr_len] = {0, 0, 1, 2, 0, 0, 4, 6, 0, 7, 0, 0, 0, 10, 0};
    cout << "Input array: " << endl;
    print_arr(arr, arr_len);

    // push zeros to back
    push_zeros(arr, arr_len);

    // print result
    cout << "Output array: " << endl;
    print_arr(arr, arr_len);

    return 0;
}
