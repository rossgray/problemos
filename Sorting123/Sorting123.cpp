/*
 * You are given an array of 1's 2's and 3's. Sort this list so the 1's are first, the 2's come second, and the 3's come third. 
 *
 * Ex: Input [1, 3, 3, 2, 1] 
 * Output [1, 1, 2, 3, 3] 
 *
 * But there is a catch!! The algorithm must be one pass, which means no merge/quick sort. Also no extra list allocations are allowed, which means no bucket/radix/counting sorts. 
 *
 * You are only permitted to swap elements.
 *
 *  INPUT:  first line = length of array
 *          second line = list of array elements seperated by spaces
 *
 *  OUTPUT: sorted list        
 *
 */

#include <iostream>
#include <vector>

using namespace std;

int main()
{
    // put data into vector

    int array_len, curr_item;
    cin >> array_len;
    cin.ignore();

    vector<int> vector2sort;

    for(int i=0; i<array_len; ++i)
    {
        cin >> curr_item;
        vector2sort.push_back(curr_item);
    }

    
    // perform sort of vector in one pass
    int low = 0, high = array_len-1, tmp;
    curr_item = 0;

    while(curr_item <= high)
    {
        if(vector2sort[curr_item] > 2)
        {
            // swap curr item with high index
            tmp = vector2sort[curr_item];
            vector2sort[curr_item] = vector2sort[high];
            vector2sort[high--] = tmp;
        }
        else if(vector2sort[curr_item] < 2)
        {
            // swap curr item with low index 
            tmp = vector2sort[curr_item];
            vector2sort[curr_item] = vector2sort[low];
            vector2sort[low++] = tmp;
            curr_item++;
        }
        else
            // just increment curr item
            curr_item++;
    }

    // output answer
    cout << "Sorted array:" << endl;
    for(int i=0; i<array_len; ++i)
    {
        cout << vector2sort[i] << " ";
    }

}
