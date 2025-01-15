# 「每日一题」力扣 451 根据字符出现频率排序

你好啊，我是蓝莓，今天是每日一题的第 23 天。

**题目清单**：[一起刷力扣](https://blueberry-universe.cn/lc/index.html)

**引用力扣题目**：[451 根据字符出现频率排序](https://leetcode.cn/problems/sort-characters-by-frequency/description/)





## 题目描述

给定一个字符串 `s` ，根据字符出现的 **频率** 对其进行 **降序排序** 。一个字符出现的 **频率** 是它出现在字符串中的次数。

返回 *已排序的字符串* 。如果有多个答案，返回其中任何一个。

 

**示例 1:**

```
输入: s = "tree"
输出: "eert"
解释: 'e'出现两次，'r'和't'都只出现一次。
因此'e'必须出现在'r'和't'之前。此外，"eetr"也是一个有效的答案。
```

**示例 2:**

```
输入: s = "cccaaa"
输出: "cccaaa"
解释: 'c'和'a'都出现三次。此外，"aaaccc"也是有效的答案。
注意"cacaca"是不正确的，因为相同的字母必须放在一起。
```

**示例 3:**

```
输入: s = "Aabb"
输出: "bbAa"
解释: 此外，"bbaA"也是一个有效的答案，但"Aabb"是不正确的。
注意'A'和'a'被认为是两种不同的字符。
```

 

**提示:**

- `1 <= s.length <= 5 * 105`
- `s` 由大小写英文字母和数字组成





## 实现

**思路**

- 首先使用哈希表来统计每个字符出现的频率，这里使用 `unordered_map` 就可以了
- 统计好频率之后，我们需要按照频率的递减顺序依次向字符串中追加字符
- 可以使用 `map` 来实现，它的底层数据结构是使用平衡二叉树来实现的
- 根据平衡二叉树的性质，我们可以知道，按照一定的顺序进行遍历各个节点的话，那么它是有序的
- 由于可能存在多个字符出现的频率都是相同的，所以我们要是用 `频率` 到 `字符数组` 的方式来存储





**C++ 代码实现**

```c++
class Solution {
public:
    string frequencySort(string s) {
        unordered_map<char, int> record;
        map<int, vector<char>> sorted_record;
        
        // 先统计各个字符的频率 字符 -> 频率 的映射关系存储
        for( int i = 0 ; i < s.size() ; i++ ) {
            record[s[i]]++;
        }

        // 按照 频率 -> 字符 的映射关系存储
        for( auto iter = record.begin() ; iter != record.end() ; iter++ ) {
            sorted_record[iter->second].push_back(iter->first);
        }

        string res = "";

        // 按照 频率 从大到小的顺序遍历 sorted_record
        for( auto iter = sorted_record.rbegin() ; iter != sorted_record.rend() ; iter++ ) {
            int freq = iter->first;  // 取出这组字符的频率
            vector<char>& arr = iter->second;  // 获取这组字符

            for( int i = 0 ; i < arr.size() ; i++ ) {
                // 把出现频率相同的字符全部都添加 freq 次到 res 的末尾
                for( int k = 0 ; k < freq ; k++ ) {
                    res.push_back(arr[i]);
                }
            }
        }

        return res;
    }
};
```

