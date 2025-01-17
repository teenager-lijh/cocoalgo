# 「每日一题」力扣 15 三数之和

你好啊，我是蓝莓，今天是每日一题的第 25 天。

**题目清单**：[一起刷力扣](https://blueberry-universe.cn/lc/index.html)

**引用力扣题目**：[15 三数之和](https://leetcode.cn/problems/3sum/description/)





## 题目描述

给你一个整数数组 `nums` ，判断是否存在三元组 `[nums[i], nums[j], nums[k]]` 满足 `i != j`、`i != k` 且 `j != k` ，同时还满足 `nums[i] + nums[j] + nums[k] == 0` 。请你返回所有和为 `0` 且不重复的三元组。

**注意：**答案中不可以包含重复的三元组。

 

 

**示例 1：**

```
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
注意，输出的顺序和三元组的顺序并不重要。
```

**示例 2：**

```
输入：nums = [0,1,1]
输出：[]
解释：唯一可能的三元组和不为 0 。
```

**示例 3：**

```
输入：nums = [0,0,0]
输出：[[0,0,0]]
解释：唯一可能的三元组和为 0 。
```

 

**提示：**

- `3 <= nums.length <= 3000`
- `-105 <= nums[i] <= 105`





## 实现

**思路 1**

- 在 `力扣 1 两数之和` 题目中，我们已经知道了如何使用哈希表来减少一层循环的开销技巧
- 那么这个题目，依旧可以使用这个思路
- 最常规的做法是来三次循环，搜索所有可能的 `三元组`
- 那么，使用类似的方法，我们使用两个循环搜索所有的 `二元组`，在最内层使用哈希表来减少最内层的开销
- 这样一来，时间复杂度可从 `O(N^3)` 降低为 `O(N^2)`





**C++ 代码实现**

```c++
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        unordered_map<int, int> record;

        // 统计各个元素出现的次数
        for( int i = 0 ; i < nums.size() ; i++ ) {
            record[nums[i]] += 1;
        }

        // 排序
        sort(nums.begin(), nums.end());

        // 对排序后的元素去重
        auto iter = unique(nums.begin(), nums.end());
        nums.erase(iter, nums.end());

        // 保存结果
        vector<vector<int>> res;

        // 某个元素使用 3 次得到 0 的只有 0 本身
        if( record[0] >= 3 ) {
            res.push_back(vector<int>({0, 0, 0}));
        }

        for( int i = 0 ; i < nums.size() && nums[i] <= 0 ; i++ ) {
            for( int j = i+1 ; j < nums.size() ; j++ ) {

                // 1 nums[i] 使用两次的情况 && nums[j] 使用一次的情况
                if( record[nums[i]] >= 2 && 2 * nums[i] + nums[j] == 0 ) {
                    res.push_back(vector<int>({nums[i], nums[i], nums[j]}));
                }

                // 2 nums[j] 使用两次的情况 && nums[i] 使用一次的情况
                if( record[nums[j]] >= 2 && 2 * nums[j] + nums[i] == 0 ) {
                    res.push_back(vector<int>({nums[i], nums[j], nums[j]}));
                }

                // 3 nums[i] 和 nums[j] 只使用一次 剩余的一个元素从 nums[j] 的右侧寻找
                int target = - ( nums[i] + nums[j] );
                if( target > nums[j] && record.find(target) != record.end() ) {
                    res.push_back(vector<int>({nums[i], nums[j], target}));
                }
            }
        }

        return res;
    }
};
```





**思路 2**

- 遍历最左侧的元素 `nums[i]` 然后使用双指针的方法去寻找右边的两个元素，分别是 `nums[l]` 和 `nums[r]`
- 会出现重复的情况有两种
- 第一种就是遍历 `nums[i]` 的时候，最左侧已经用过一次这个值了，下一次又用到了这个值，就会导致重复的情况出现，因为双指针寻找的是 `nums[i+1]` 右侧的值，寻找的内容还是相同的，所以肯定会造成重复
- 第二种重复的情况是在双指针寻找的过程中，当我们寻找到一个成功的组合后，我们应该让 `l` 和 `r` 都向内靠拢一次，也就是 `l++` 和 `r--` 一次，但是有一种可能就是 `nums[l+1]` 的值等于 `nums[l]` 并且 `nums[r-1]` 的值等于 `nums[r]` ，这时候 `nums[i]` 没有变，那么势必也会造成重复的组合出现





**C++ 代码实现**

```c++
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        // 排序
        sort(nums.begin(), nums.end());

        // 保存结果
        vector<vector<int>> res;

        for( int i = 0 ; i < nums.size() ; i++ ) {
            // 防止 0 0 0 1 2 3 4 5 这种情况的去重 此时 i 指向最左侧的 0
            if( i > 0 && nums[i] == nums[i-1] ) continue;

            int l = i+1;
            int r = nums.size() - 1;

            while( l < r ) {
                int target = - nums[i];
                if( nums[l] + nums[r] == target ) {
                    res.push_back(vector<int>({nums[i], nums[l], nums[r]}));
                    // 防止 -1 0 0 0 1 2 3 4 5 这种情况去重 此时 l 指向最左侧的 0
                    // 双指针指向的下一个元素 不能再和当前的元素一致了
                    while( l < r && nums[l+1] == nums[l] ) l++;
                    while( l < r && nums[r-1] == nums[r] ) r--;

                    // 发现下一个元素已经和当前元素不同的时候 更新 l 和 r
                    l++;
                    r--;
                } else if( nums[l] + nums[r] > target ) {
                    r--;
                } else {
                    l++;
                }
            }
        }

        return res;
    }
};
```

