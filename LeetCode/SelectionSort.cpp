// C++ program to implement Selection Sort
#include <bits/stdc++.h>

using namespace std;

void printArray(vector<int> &arr){
    for(int &val : arr){
        cout << val << " ";
    }
    cout << endl;
}

void selectionSort(vector<int> &arr){
    int n = arr.size();

    for(int i = 0; i < n; i++){
        int min_idx=i;

        for(int j = i+1; j < n;++j){
            if(arr[j] < arr[min_idx]){
                min_idx = j;
            }
        }
        swap(arr[i], arr[min_idx]);
    }
}

int main(){
    vector<int> arr = {64,25,12,22,11};
    cout << "original array:";
    printArray(arr);
    selectionSort(arr);
    cout << "sorted array:";
    printArray(arr);
    return 0;
}
