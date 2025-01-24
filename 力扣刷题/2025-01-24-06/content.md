# 「每日一题」力扣 220 存在重复元素 III

你好啊，我是蓝莓，今天是每日一题的第 32 天。

**题目清单**：[一起刷力扣](https://blueberry-universe.cn/lc/index.html)

**引用力扣题目**：[220 存在重复元素 III](https://leetcode.cn/problems/contains-duplicate-iii/description/)





## 题目描述

给你一个整数数组 `nums` 和两个整数 `indexDiff` 和 `valueDiff` 。

找出满足下述条件的下标对 `(i, j)`：

- `i != j`,
- `abs(i - j) <= indexDiff`
- `abs(nums[i] - nums[j]) <= valueDiff`

如果存在，返回 `true` *；*否则，返回 `false` 。

 

**示例 1：**

```
输入：nums = [1,2,3,1], indexDiff = 3, valueDiff = 0
输出：true
解释：可以找出 (i, j) = (0, 3) 。
满足下述 3 个条件：
i != j --> 0 != 3
abs(i - j) <= indexDiff --> abs(0 - 3) <= 3
abs(nums[i] - nums[j]) <= valueDiff --> abs(1 - 1) <= 0
```

**示例 2：**

```
输入：nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3
输出：false
解释：尝试所有可能的下标对 (i, j) ，均无法满足这 3 个条件，因此返回 false 。
```

 

**提示：**

- `2 <= nums.length <= 105`
- `-109 <= nums[i] <= 109`
- `1 <= indexDiff <= nums.length`
- `0 <= valueDiff <= 109`





## 实现

**思路**

- 这个题目设计到了二分搜索树的有序性，在 `C++` 中的 `set` 底层是使用红黑树实现的，而 `unordered_set` 的底层是使用哈希表实现的
- 所以，我们可以使用 `set`，一旦它维护的元素有了顺序之后，我们就可以针对某个数值 `key` 去更快的寻找最接近 `key` 且大于或等于 `key` 的那个数值
- 在 `C++` 中的 `set` 提供了 `lower_bound` 方法来来寻找大于等于 `key` 的数值





**C++ 代码实现**

```c++
class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int indexDiff, int valueDiff) {
        set<int> record;

        for( int i = 0 ; i < nums.size() ; i++ ) {
            // 对于给定的 nums[i] 查找 record 中是否存在一个数组 num
            // nums[i] - valueDiff <= num <= nums[i] + valueDiff
            // 转换成寻找一个最接近 nums[i] - valueDiff 但是大于等于 nums[i] - valueDiff 的值
            // 而且这个值小于等于 nums[i] + valueDiff

            int key = nums[i] - valueDiff;
            int upper = nums[i] + valueDiff;
            if( record.lower_bound(key) != record.end() && *record.lower_bound(key) <= upper ) {
                return true;
            }

            record.insert( nums[i] );
            // 因为 valueDiff 最小的数值为 0
            // 如果 set 中存在了相同的元素
            // 那么就一定会满足题意 所以只要算法还在进行
            // 就说明一定没有向 set 添加过重复的元素
            if( record.size() == indexDiff + 1 ) {
                record.erase(nums[i-indexDiff]);
            }
        }

        return false;
    }
};
```

