

# 「每日一题」力扣 349 两个数组的交集

你好啊，我是蓝莓，今天是每日一题的第 18 天。

**题目清单**：[一起刷力扣](https://blueberry-universe.cn/lc/index.html)

**引用力扣题目**：[349 两个数组的交集](https://leetcode.cn/problems/intersection-of-two-arrays/description/)





## 题目描述

给定两个数组 `nums1` 和 `nums2` ，返回 *它们的* 

*交集*

 。输出结果中的每个元素一定是 **唯一** 的。我们可以 **不考虑输出结果的顺序** 。



 

**示例 1：**

```
输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2]
```

**示例 2：**

```
输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[9,4]
解释：[4,9] 也是可通过的
```

 

**提示：**

- `1 <= nums1.length, nums2.length <= 1000`
- `0 <= nums1[i], nums2[i] <= 1000`



## 实现

**思路**

- 这是一个简单题，可以通过这个题目熟悉一下编程语言中集合的使用方法
- 最简单的思路就是使用两个 `set` 分别对 `nums1` 和 `nums2` 去重
- 然后求两个集合的交集即可





**C++ 代码实现**

```c++
class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        set<int> record1;
        set<int> record2;
        
        vector<int> res;

        // 对 nums1 去重
        for( int num : nums1 ) {
            record1.insert(num);
        }

        // 对 nums2 去重
        for( int num : nums2 ) {
            record2.insert(num);
        }

        // 遍历集合 record2 中的元素，看看是不是在 record1 集合中也出现了
        // 如果同时满足 则这个就纳入 res 中
        for( set<int>::iterator iter = record2.begin() ; iter != record2.end() ; iter++ ) {
            if( record1.find(*iter) != record1.end() ) {
                res.push_back(*iter);
            }
        }

        return res;
    }
};
```

