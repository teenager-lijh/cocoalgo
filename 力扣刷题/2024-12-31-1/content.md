# 「每日一题」力扣 209 长度最小的子数组

你好啊，我是蓝莓，今天是每日一题的第 13 天。

**题目清单**：[一起刷力扣](https://blueberry-universe.cn/lc/index.html)

**引用力扣题目**：[169 多数元素](https://leetcode.cn/problems/majority-element/?envType=study-plan-v2&envId=top-interview-150)





## 题目描述

给定一个大小为 `n` 的数组 `nums` ，返回其中的多数元素。多数元素是指在数组中出现次数 **大于** `⌊ n/2 ⌋` 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

 

**示例 1：**

```
输入：nums = [3,2,3]
输出：3
```

**示例 2：**

```
输入：nums = [2,2,1,1,1,2,2]
输出：2
```

 

**提示：**

- `n == nums.length`
- `1 <= n <= 5 * 104`
- `-109 <= nums[i] <= 109`

 

**进阶：**尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。





## 实现

**思考**

- 使用 哈希表 来记录扫描过程中每个元素出现的次数
- 如果的统计过程中，发现某个元素的出现次数已经属于多数元素了，直接返回即可





**C++ 代码实现**

```c++
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> record;
        int target = nums.size() / 2;

        for( int i = 0 ; i < nums.size() ; i++ ) {
            record[nums[i]]++;
            if( record[nums[i]] > target ) {
                return nums[i];
            }
        }

        return -1;
    }
};
```

