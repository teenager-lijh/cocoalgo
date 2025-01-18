# 「每日一题」力扣 18 四数之和

你好啊，我是蓝莓，今天是每日一题的第 26 天。

**题目清单**：[一起刷力扣](https://blueberry-universe.cn/lc/index.html)

**引用力扣题目**：[18 四数之和](https://leetcode.cn/problems/4sum/description/)





## 题目描述

给你一个由 `n` 个整数组成的数组 `nums` ，和一个目标值 `target` 。请你找出并返回满足下述全部条件且**不重复**的四元组 `[nums[a], nums[b], nums[c], nums[d]]` （若两个四元组元素一一对应，则认为两个四元组重复）：

- `0 <= a, b, c, d < n`
- `a`、`b`、`c` 和 `d` **互不相同**
- `nums[a] + nums[b] + nums[c] + nums[d] == target`

你可以按 **任意顺序** 返回答案 。

 

**示例 1：**

```
输入：nums = [1,0,-1,0,-2,2], target = 0
输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
```

**示例 2：**

```
输入：nums = [2,2,2,2,2], target = 8
输出：[[2,2,2,2]]
```

 

**提示：**

- `1 <= nums.length <= 200`
- `-109 <= nums[i] <= 109`
- `-109 <= target <= 109`





## 实现

**思路**

- 这个题目同样可以使用查找表优化
- 需要注意的是，由于这个需要使用四个数值组成一个 `四元组` 所以情况相对复杂一些
- 由于每个数值出现在 `nums` 数组中的次数可以有多次，所以组成四元组的方式主要有 4 种
- （1）四元组中有一个互不相同的数值，并且满足要求的；
- （2）四元组中有两个互不相同的数值，并且满足要求的；
- （3）四元组中有三个互不相同的数值，并且满足要求的；
- （4）四元组中有四个互不相同的数值，并且满足要求的；





**C++ 代码实现**

```c++
class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        unordered_map<int, int> record;

        // 统计每个数值出现的次数
        for( int i = 0 ; i < nums.size() ; i++ ) {
            record[nums[i]]++;
        }

        // 排序
        sort(nums.begin(), nums.end());

        // 去重
        auto iter = unique(nums.begin(), nums.end());
        nums.erase(iter, nums.end());

        // 保存结果
        vector<vector<int>> res;

        for( int i = 0 ; i < nums.size() ; i++ ) {
            // 只有一个不同数字的情况
            if( record[nums[i]] >= 4 && 4 * (long long)nums[i] == target ) {
                res.push_back(vector<int>({nums[i], nums[i], nums[i], nums[i]}));
            }

            for( int j = i+1 ; j < nums.size() ; j++ ) {
                // 两个不同数字的情况
                if( record[nums[i]] >= 3 && 3 * (long long)nums[i] + (long long)nums[j] == target ) {
                    res.push_back(vector<int>({nums[i], nums[i], nums[i], nums[j]}));
                }

                if( record[nums[j]] >= 3 && (long long)nums[i] + 3 * (long long)nums[j] == target ) {
                    res.push_back(vector<int>({nums[i], nums[j], nums[j], nums[j]}));
                }

                if( record[nums[i]] >= 2 && record[nums[j]] >= 2 && 2 * (long long)nums[i] + 2 * (long long)nums[j] == target ) {
                    res.push_back(vector<int>({nums[i], nums[i], nums[j], nums[j]}));
                }

                for( int k = j+1 ; k < nums.size() ; k++ ) {
                    // 3 个不同数字的情况
                    if( record[nums[i]] >= 2 && 2 * (long long)nums[i] + (long long)nums[j] + (long long)nums[k] == target ) {
                        res.push_back(vector<int>({nums[i], nums[i], nums[j], nums[k]}));
                    }

                    if( record[nums[j]] >= 2 && (long long)nums[i] + 2 * (long long)nums[j] + (long long)nums[k] == target ) {
                        res.push_back(vector<int>({nums[i], nums[j], nums[j], nums[k]}));
                    }

                    if( record[nums[k]] >= 2 && (long long)nums[i] + (long long)nums[j] + 2 * (long long)nums[k] == target ) {
                        res.push_back(vector<int>({nums[i], nums[j], nums[k], nums[k]}));
                    }

                    // 4 个不同数字的情况 使用哈希表优化一层循环
                    int num = target - (long long)(nums[i] + nums[j] + nums[k]);
                    if( record.find(num) != record.end() && num > nums[k] ) {
                        res.push_back(vector<int>({nums[i], nums[j], nums[k], num}));
                    }
                }
            }
        } 

        return res;
    }
};
```















