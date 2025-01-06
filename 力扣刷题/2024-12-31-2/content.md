# 「每日一题」力扣 189 轮转数组

你好啊，我是蓝莓，今天是每日一题的第 14 天。

**题目清单**：[一起刷力扣](https://blueberry-universe.cn/lc/index.html)

**引用力扣题目**：[189 轮转数组](https://leetcode.cn/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150)





## 题目描述

给定一个整数数组 `nums`，将数组中的元素向右轮转 `k` 个位置，其中 `k` 是非负数。

 

**示例 1:**

```
输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右轮转 1 步: [7,1,2,3,4,5,6]
向右轮转 2 步: [6,7,1,2,3,4,5]
向右轮转 3 步: [5,6,7,1,2,3,4]
```

**示例 2:**

```
输入：nums = [-1,-100,3,99], k = 2
输出：[3,99,-1,-100]
解释: 
向右轮转 1 步: [99,-1,-100,3]
向右轮转 2 步: [3,99,-1,-100]
```

 

**提示：**

- `1 <= nums.length <= 105`
- `-231 <= nums[i] <= 231 - 1`
- `0 <= k <= 105`

 

**进阶：**

- 尽可能想出更多的解决方案，至少有 **三种** 不同的方法可以解决这个问题。
- 你可以使用空间复杂度为 `O(1)` 的 **原地** 算法解决这个问题吗？





## 实现

**思路**

- k 对 `len(nums)` 取模，保证 `k` 是在有必要的轮转范围内
- 第一步，翻转整个数组
- 第二步，翻转前 k 个元素
- 第三步，翻转后 n-k 个元素





**C++ 代码实现**

```c++
class Solution {
public:
    void rotate(vector<int>& nums, int k) {

        k = k % nums.size();

        // 1. 翻转整个数组
        reverse( nums, 0, nums.size() - 1 );

        // 2. 翻转前 k 个
        reverse( nums, 0, k-1);

        // 3. 翻转后 n-k 个
        reverse( nums, k, nums.size() - 1 );

    }

    void reverse( vector<int>& nums, int i, int j ) {
        while( i < j ) {
            swap(nums[i++], nums[j--]);
        }
    }
};
```

