# 「每日一题」力扣 49 字母异位词分组

你好啊，我是蓝莓，今天是每日一题的第 29 天。

**题目清单**：[一起刷力扣](https://blueberry-universe.cn/lc/index.html)

**引用力扣题目**：[49 字母异位词分组](https://leetcode.cn/problems/group-anagrams/description/)





## 题目描述

给你一个字符串数组，请你将 **字母异位词** 组合在一起。可以按任意顺序返回结果列表。

**字母异位词** 是由重新排列源单词的所有字母得到的一个新单词。

 

**示例 1:**

```
输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

**示例 2:**

```
输入: strs = [""]
输出: [[""]]
```

**示例 3:**

```
输入: strs = ["a"]
输出: [["a"]]
```

 

**提示：**

- `1 <= strs.length <= 104`
- `0 <= strs[i].length <= 100`
- `strs[i]` 仅包含小写字母





## 实现

**思路**

- 我们需要对每一个单词进行归类
- 归类的标准是这个单词用到的字母所属的集合是相同的；其实这个说法还是不太严谨，因为如果同时出现了两个相同的字母，我们是不能去重的；
- 所以呢，我们可以对每个单词的字母按照字典序进行排序，如果排序后展现出来的是同样的内容，那么它们就是同一个类别的





**C++ 代码实现**

```c++
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> record;

        for( int i = 0 ; i < strs.size() ; i++ ) {
            string s = strs[i];
            sort(s.begin(), s.end());
            record[s].push_back(strs[i]);
        }

        vector<vector<string>> res;

        for( auto iter = record.begin() ; iter != record.end() ; iter++ ) {
            res.push_back(iter->second);
        }

        return res;
    }
};
```

