# 「每日一题」力扣 454 四数相加 II

你好啊，我是蓝莓，今天是每日一题的第 28 天。

**题目清单**：[一起刷力扣](https://blueberry-universe.cn/lc/index.html)

**引用力扣题目**：[454 四数相加 II](https://leetcode.cn/problems/4sum-ii/description/)





## 题目描述

给你四个整数数组 `nums1`、`nums2`、`nums3` 和 `nums4` ，数组长度都是 `n` ，请你计算有多少个元组 `(i, j, k, l)` 能满足：

- `0 <= i, j, k, l < n`
- `nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0`

 

**示例 1：**

```
输入：nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
输出：2
解释：
两个元组如下：
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0
```

**示例 2：**

```
输入：nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
输出：1
```

 

 **提示：**

- `n == nums1.length`
- `n == nums2.length`
- `n == nums3.length`
- `n == nums4.length`
- `1 <= n <= 200`
- `-228 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 228`





## 实现

**思路**

- 这个情况，我们依然可以使用查找表对暴力方法进行优化
- 在以往的解题过程中，我们都是使用查找表对最内层的循环进行优化
- 对于四个数值的组合而言，优化后可以从 `O(N^4)` 降低到 `O(N^3)` 这个复杂度
- 其实我们还有更好的查找表使用技巧
- 我们可以先遍历 两两成对 的情况
- （1）对 `nums1` 和 `nums2` 的数值组合成包含两个元素的元组和
- （2）对 `nums3` 和 `nums4` 的数值组合成包含两个元素的元组和
- （3）最后我们对所有的包含两个元组的元组和进行组合，组合成包含 4 个元素的元组和





**C++ 代码实现**

```c++
class Solution {
public:
    int fourSumCount(vector<int>& nums1, vector<int>& nums2, vector<int>& nums3, vector<int>& nums4) {
        unsigned int n = nums1.size();

        unordered_map<int, int> record1;
        unordered_map<int, int> record2;

        for( int i = 0 ; i < n ; i++ ) {
            for( int j = 0 ; j < n ; j++ ) {
                record1[nums1[i] + nums2[j]] += 1;
                record2[nums3[i] + nums4[j]] += 1;
            }
        }

        int counter = 0;

        for( auto iter = record1.begin() ; iter != record1.end() ; iter++ ) {
            int k1 = iter->first;
            int v1 = iter->second;

            int k2 = -k1;
            if( record2.find(k2) != record2.end() ) {
                int v2 = record2[k2];
                counter += v1 * v2;
            }
        }

        return counter;
    }
};
```

