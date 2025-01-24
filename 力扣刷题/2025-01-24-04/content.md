# 「每日一题」力扣 219 存在重复元素 II

你好啊，我是蓝莓，今天是每日一题的第 32 天。

**题目清单**：[一起刷力扣](https://blueberry-universe.cn/lc/index.html)

**引用力扣题目**：[219 存在重复元素 II](https://leetcode.cn/problems/contains-duplicate-ii/description/)





## 题目描述

给你一个整数数组 `nums` 和一个整数 `k` ，判断数组中是否存在两个 **不同的索引** `i` 和 `j` ，满足 `nums[i] == nums[j]` 且 `abs(i - j) <= k` 。如果存在，返回 `true` ；否则，返回 `false` 。

 

**示例 1：**

```
输入：nums = [1,2,3,1], k = 3
输出：true
```

**示例 2：**

```
输入：nums = [1,0,1,1], k = 1
输出：true
```

**示例 3：**

```
输入：nums = [1,2,3,1,2,3], k = 2
输出：false
```

 

 

**提示：**

- `1 <= nums.length <= 105`
- `-109 <= nums[i] <= 109`
- `0 <= k <= 105`





## 实现

**思路**

- 题目要求寻找两个重复的元素，并且这两个元素之间的距离不超过 `k`
- 我们可以维护一个滑动窗口，使用哈希表记录这个滑动窗口内的每个元素出现的次数
- 如果当前没有出现重复的元素，那么就向右滑动一下，扔掉旧的元素，纳入新的元素，并检查纳入新的元素后是否出现了重复的元素
- 这时候，如果出现了重复元素就可以直接返回成功了
- 如果没有出现，那就需要继续滑动窗口
- 如果所有的元素都扫过了一遍还是没成功，那肯定就是失败了





**C++ 代码实现**

```c++
class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        
        int l = 0;
        int r = k < nums.size() - 1 ? k : nums.size() - 1;

        // num -> freq 
        unordered_map<int, int> record;
        
        for( int i = 0 ; i <= r ; i++ ) {
            if(++record[nums[i]] >= 2) {
                return true;
            }
        }

        for( int i = r+1 ; i < nums.size() ; i++ ) {
            // 扔掉以前的元素
            record[nums[l++]]--;
            
            // 加入新的元素
            if(++record[nums[i]] >= 2) {
                return true;
            }
        }

        return false;
    }
};
```

