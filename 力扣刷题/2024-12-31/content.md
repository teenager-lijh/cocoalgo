

# 「每日一题」力扣 209 长度最小的子数组

你好啊，我是蓝莓，今天是每日一题的第 11 天。

**题目清单**：[一起刷力扣](https://blueberry-universe.cn/lc/index.html)

**引用力扣题目**：[209 长度最小的子数组](https://leetcode.cn/problems/minimum-size-subarray-sum/description/)





## 题目描述

给定一个含有 `n` 个正整数的数组和一个正整数 `target` **。**

找出该数组中满足其总和大于等于 `target` 的长度最小的 

**子数组**

`[numsl, numsl+1, ..., numsr-1, numsr]` ，并返回其长度**。**如果不存在符合条件的子数组，返回 `0` 。

 

**示例 1：**

```
输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
```

**示例 2：**

```
输入：target = 4, nums = [1,4,4]
输出：1
```

**示例 3：**

```
输入：target = 11, nums = [1,1,1,1,1,1,1,1]
输出：0
```

 

**提示：**

- `1 <= target <= 109`
- `1 <= nums.length <= 105`
- `1 <= nums[i] <= 104`

 

**进阶：**

- 如果你已经实现 `O(n)` 时间复杂度的解法, 请尝试设计一个 `O(n log(n))` 时间复杂度的解法。





## 实现

**思路**

- 使用滑动窗口
- 使用索引 `l` 代表窗口的左边界
- 使用索引 `r` 代表窗口的右边界
- 区间 `nums[l...r)` 代表窗口内的元素，`r-l` 是窗口的大小，`r` 的取值应该小于等于 `len(nums)`
- 使用 `sum` 记录窗口内元素的总和
- 当 `sum` 的值小于 `target` 的时候，说明窗口内的元素不够，这时候应该向右移动 `r` 来扩大窗口
- 当 `sum` 的值大于等于 `target` 的时候，比较当前的窗口长度是不是更小了，如果更小则更新窗口的最小长度，否则的话不需要更新；然后尝试着减小窗口的大小，也就是向右移动 `l`； 
- 关于这种方法的正确性依然可以使用搜索空间的角度来思考
- 因为一开始的时候，`nums[l...r)` 内的元素总和不够，所以只能向右移动 `r` 扩展区间的大小，进而让总和变得更大
- 当总和满足要求的时候，我们为了找到更小的长度，这时候尝试着让 `l` 向右移动
- 这时候会漏掉一些情况吗？不会的，因为只要 `r` 不在当前位置，而是向左缩了一点，都不可能让这个区间内的元素总和满足要求的，所以我们可以排除掉很多的选项。





**C++ 代码实现**

```c++
class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int l = 0;
        int r = 0;

        int sum = 0;
        int res = INT_MAX;
        
        // 维护区间 nums[l...r)
        while( l < nums.size() ) {
            if( sum < target ) {
                // sum < target 但是 已经没法再继续扩展了
                if( r >= nums.size() ) break;

                r++;
                sum += nums[r-1];
            } else {
                res = min(res, r-l);
                sum -= nums[l];
                l++;
            }
        }

        if( res == INT_MAX ) return 0;
        
        return res;
    }
};
```

