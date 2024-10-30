#include <iostream>
#include <cassert>
#include <ctime>
using namespace std;

// 在包含 n 个元素的数组 arr 中寻找目标值 target 的下标
int binarySearch(const int* arr, int n, int target) {
    // 在区间 [l...r] 这个区间内寻找 target
    int l = 0, r = n-1;

    // 在没有找到并且 [l...r] 区间内仍然是有元素的情况下继续查找
    while( l <= r ) {
        int mid = (l+r) / 2;
        if( arr[mid] == target ) {
            return mid;
        } else if( target > arr[mid] ) {
            l = mid+1;
        } else {
            // target < arr[mid]
            r = mid-1;
        }
    }

    return -1;
}

int main() {

    const int n = 1000000;
    int* arr = new int[n];

    // 生成一个包含 n 个元素的完全有序的数组 arr
    for(int i = 0; i < n; i++) {
        arr[i] = i;
    }

    // 对 arr 中的每一次元素都进行查找
    clock_t start_time = clock();
    for(int i = 0; i < n; i++) {
        assert(i == binarySearch(arr, n, i));
    }
    clock_t end_time = clock();

    // 计算查找 n 次所需要的时间
    cout << "Time: " << double(end_time - start_time) / CLOCKS_PER_SEC << endl;
    cout << "done!" << endl;
    return 0;
}
