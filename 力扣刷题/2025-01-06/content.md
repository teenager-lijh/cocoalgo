# 「每日一题」力扣 438 找到字符串中所有字母异位词

你好啊，我是蓝莓，今天是每日一题的第 16 天。

**题目清单**：[一起刷力扣](https://blueberry-universe.cn/lc/index.html)

**引用力扣题目**：[438 找到字符串中所有字母异位词](https://leetcode.cn/problems/find-all-anagrams-in-a-string/description/)





## 题目描述

给定两个字符串 `s` 和 `p`，找到 `s` 中所有 `p` 的 

**异位词**

 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。



 

**示例 1:**

```
输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
```

 **示例 2:**

```
输入: s = "abab", p = "ab"
输出: [0,1,2]
解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
```

 

**提示:**

- `1 <= s.length, p.length <= 3 * 104`
- `s` 和 `p` 仅包含小写字母





## 实现

**思路**

- 使用定长的滑动窗口，滑动窗口的长度为我们要寻找的异位词的字符串的长度，也就是字符串 p 的长度
- 使用 `record` 数组来记录对每个 p 字符串中的字符，每个字符还需要多少个才能满足要求
- 在字符串 s 上进行滑动，每个被我们滑进窗口的字符对应在 `record` 中的记录就减少 1 ，因为这时候我们已经找到了一个字符。当然啦，有的字符可能是不需要的，一开始的需求量就是 0，所以这时候某些字符会的需求量会变为负数，也就是需求过剩了
- 每当我们完成一次滑动之后，我们就检查这个 `record` 中的记录是否都为 0，如果不是都为 0 的话，说明是不匹配的
- 窗口的长度已经固定了，所以只有 `record` 中的记录都为 0 的时候才是满足要求的

**C++ 代码实现**

```c++
class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        
        // 保证 p 的长度是小于等于 s 的
        if(p.size() > s.size()) {
            return vector<int>();
        }
        
        int record[26];  // 分别对 26 个字母还需要多少
        vector<int> res;  // 保存结果

        // 数组置空
        memset(record, 0, sizeof(record));

        // 记录原始需求
        for( int i = 0 ; i < p.size() ; i++ ) {
            record[p[i]-'a']++;
        }

        // 使用定长的滑动窗口
        // 初始化一开始的窗口中的记录
        for( int i = 0 ; i < p.size() ; i++ ) {
            record[s[i]-'a']--;
        }

        // 窗口的区间是 [l...r]
        int l = 0;
        int r = p.size() - 1;

        while( true ) {
            // 检查当前是否满足要求
            int ok = true;
            for( int i = 0 ; i < 26 ; i++ ) {
                if(record[i] != 0) {
                    ok = false;
                    break;
                }
            }

            if(ok) {
                res.push_back(l);
            }
            
            if(r+1 < s.size()) {
                // 将左侧的字母移除, 对该字母的需求恢复 1
                record[s[l++]-'a']++;
                // 纳入新的元素到窗口中, 说明对该字母的需求减少 1
                record[s[++r]-'a']--;
            } else {
                // 说明已经滑动结束了
                break;
            }
        }

        return res;
    }
};
```

