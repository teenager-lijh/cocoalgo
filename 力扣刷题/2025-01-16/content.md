# 「每日一题」力扣 1 两数之和

你好啊，我是蓝莓，今天是每日一题的第 24 天。

**题目清单**：[一起刷力扣](https://blueberry-universe.cn/lc/index.html)

**引用力扣题目**：[1 两数之和](https://leetcode.cn/problems/two-sum/description/)





## 题目描述

给定一个整数数组 `nums` 和一个整数目标值 `target`，请你在该数组中找出 **和为目标值** *`target`* 的那 **两个** 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。

你可以按任意顺序返回答案。

 

**示例 1：**

```
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
```

**示例 2：**

```
输入：nums = [3,2,4], target = 6
输出：[1,2]
```

**示例 3：**

```
输入：nums = [3,3], target = 6
输出：[0,1]
```

 

**提示：**

- `2 <= nums.length <= 104`
- `-109 <= nums[i] <= 109`
- `-109 <= target <= 109`
- **只会存在一个有效答案**

 

**进阶：**你可以想出一个时间复杂度小于 `O(n2)` 的算法吗？





## 实现

**思路**

- 对于这个问题，你在第一时间想到的最简单的方法或许就是遍历所有成对的组合，然后依次检查他们是否符合要求
- 其实，我们可以使用 `查找表` 来代替寻找组合过程中的一层 `for` 循环，可以使 `O(N^2)` 的时间复杂度变为 `O(N)`
- 当我们拿到 `nums` 数组中的一个值的时候，我们这时候希望知道的是，这个数组中是不是存在另外一个数值 `v` ，是的 `nums[i] + v` 等于 `target` ？那么这个 `v` 其实就是 `target - nums[i]`，其实就是在询问，在 `nums` 中是否存在一个数值为 `target - nums[i]` 呢？
- 对于这个询问，我们可以将 `nums` 中的值存储在 `map` 中，其中 `key` 是数组中的每个值，`value` 是数组中这个值对应的 `index`。这样，我们就成功的把内层使用循环遍历查找的方式转换成了访问哈希表的方式，哈希表的查找效率是 `O(1)` ，因此时间复杂度可以降维 `O(N)`





**C++ 代码实现 1**

- 在代码实现上，我们先看一个比较粗糙的实现
- 在这个实现中，我们假设 `nums[i]` 对应的是两个满足要求的数值中在数组的左侧的那个值
- 我们询问查找表的那个值是位于 `nums` 数组右侧的那个值
- 但是你会发现，查找表中存储了 `nums` 数组中所有的值，这不科学，哈哈哈
- 但是这个并不会影响正确性，比如我问访问到 `nums[10]` 的时候询问查找表，发现没有满足要求的另一个数值，那么，当我们遍历到 `10` 以后的数值的时候，是不可能认为 `nums[10]` 是满足要求的，因为它是在全部的元素中进行询问的，如果 `nums[10]` 就是其中一个满足要求的值，那么必然我们遍历到 `nums[10]` 的时候就一定会得到答案

```c++
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> record;

        // 构建查找表
        for( int i = 0 ; i < nums.size() ; i++ ) {
            record[nums[i]] = i;
        }

        for( int i = 0 ; i < nums.size() ; i++ ) {
            // 对整个 nums 数组询问是否存在 target - nums[i] 这个值 ？
            if(record.find(target - nums[i]) != record.end()) {
                if( i != record[target - nums[i]] ) {
                    return vector<int>({i, record[target-nums[i]]});
                }
            }
        }

        return vector<int>({-1, -1});        
    }
};
```





**C++ 代码实现 2**

- 其实我们没有必要对全局进行询问的，如果假设遍历过程中的 `nums[i]` 是两个满足要求的数值中靠右的那个元素，那么我们只需要对每个 `nums[i]` 去询问它左侧的所有的元素是否满足要求就可以了，这时候我们可以正向的遍历数组，同时构建哈希表即可
- 当然，如果我们假设遍历过程中的 `nums[i]` 是靠近数组左侧的那个满足要求的值，那么我们就需要反向的遍历 `nums` 数组，因为我们需要把它右侧的值都添加到查找表中

```c++

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // 使用查找表
        unordered_map<int, int> record;

        for( int i =  0 ; i < nums.size() ; i++ ) {
            int v = nums[i];

            if( record.find( target - v ) != record.end() ) {
                int res[2] = {record[target-v], i};
                return vector<int>(res, res+2);
            }

            record[v] = i;
        }

        return vector<int>();
    }
};
```

