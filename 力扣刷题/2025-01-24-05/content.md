# 「每日一题」力扣 219 存在重复元素 II

你好啊，我是蓝莓，今天是每日一题的第 32 天。

**题目清单**：[一起刷力扣](https://blueberry-universe.cn/lc/index.html)

**引用力扣题目**：[217 存在重复元素](https://leetcode.cn/problems/contains-duplicate/description/)





## 题目描述

给你一个整数数组 `nums` 。如果任一值在数组中出现 **至少两次** ，返回 `true` ；如果数组中每个元素互不相同，返回 `false` 。

 

**示例 1：**

**输入：**nums = [1,2,3,1]

**输出：**true

**解释：**

元素 1 在下标 0 和 3 出现。

**示例 2：**

**输入：**nums = [1,2,3,4]

**输出：**false

**解释：**

所有元素都不同。

**示例 3：**

**输入：**nums = [1,1,1,3,3,4,3,2,4,2]

**输出：**true

 

**提示：**

- `1 <= nums.length <= 105`
- `-109 <= nums[i] <= 109`





## 实现

**思路**

- 这是一个简单题，直接使用哈希表来记录每个遍历过得元素出现的次数就可以
- 当我们将一个新的元素加入到哈希表的统计后，我们就看看当前这个元素的出现次数是不是大于或等于 2 了，如果是的话，直接返回成功，不然继续遍历
- 如果遍历完所有的元素后都没有成功，那就说明不存在重复的元素，返回失败





**C++ 代码实现**

```c++
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, int> record;

        for( int num : nums ) {
            if( ++record[num] >= 2 ) {
                return true;
            }
        }

        return false;
    }
};
```

