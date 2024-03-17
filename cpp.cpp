#include <iostream>
using namespace std;
int main()
{
    bool ItsPrime = true;
    int arr[] = {10, 22, 53, 84, 5, 86, 72, 18, 19};
    for (int i = 0; i <9; i++)
    {
        bool ItsPrime = true;
        for (int j = 2; j < arr[i]; j++)

            if (arr[i] % j == 0)
                ItsPrime = false;
        if (ItsPrime)
            cout << arr[i] << " prime number" << endl;
        else
            cout << arr[i] << " not prime number" << endl;
        
    }
}