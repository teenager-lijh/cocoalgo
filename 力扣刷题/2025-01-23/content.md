# 「每日一题」力扣 16 最接近的三数之和

你好啊，我是蓝莓，今天是每日一题的第 27 天。

**题目清单**：[一起刷力扣](https://blueberry-universe.cn/lc/index.html)

**引用力扣题目**：[16 最接近的三数之和](https://leetcode.cn/problems/3sum-closest/description/)





## 题目描述

给你一个长度为 `n` 的整数数组 `nums` 和 一个目标值 `target`。请你从 `nums` 中选出三个整数，使它们的和与 `target` 最接近。

返回这三个数的和。

假定每组输入只存在恰好一个解。

 

**示例 1：**

```
输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2)。
```

**示例 2：**

```
输入：nums = [0,0,0], target = 1
输出：0
解释：与 target 最接近的和是 0（0 + 0 + 0 = 0）。
```

 

**提示：**

- `3 <= nums.length <= 1000`
- `-1000 <= nums[i] <= 1000`
- `-104 <= target <= 104`





## 实现

**思路**

- 这仍然是一个数字和的问题，只是这一次并不是去寻找一个 `三元组` 并且使得三元组中的几个数值的和为 `target`，而是寻找一个接近 `target` 的值，所以我们没有办法使用 `哈希表` 来优化最内层的循环了，因为我们计算出的那个数值在哈希表中查找不到并不意味着不存在一个数值使得他们相加后接近于 `target`。
- 在使用对撞指针的过程中，我们是通过不断的逼近 `target` 从而来寻找一个值的。这就意味着，对撞指针不仅能够用来精确的寻找一个值，而且也能用来寻找一个 `接近` 的值。
- 在这个题目中，对撞指针是同时引用了两个值，所以原本的三层循环让我们变成了一个外层循环加上一层对撞指针的循环。因此时间复杂度可从 `O(N^3)` 优化为 `O(N^2)`





**C++ 代码实现**

```c++
class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        // 对撞指针

        // 排序
        sort(nums.begin(), nums.end());

        // 初始化 这是被搜索到的第一组值
        int sum = nums[0] + nums[1] + nums[nums.size() - 1];

        // 搜索
        for( int k = 0 ; k < nums.size() ; k++ ) {

            // 对撞指针搜索 nums[k+1...nums.size()-1]
            // 从而不断的趋近 target 寻找最接近的值
            int i = k+1;
            int j = nums.size() - 1;

            while( i < j ) {
                int temp = nums[k] + nums[i] + nums[j];
                if( abs(temp - target) < abs(sum - target) ) {
                    sum = temp;
                }

                if( temp > target ) {
                    j--;
                } else {
                    // temp < target
                    i++;
                }
            }
        }

        return sum;
    }
};
```

