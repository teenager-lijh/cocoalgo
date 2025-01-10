# 「每日一题」力扣 242 有效的字母异位词

你好啊，我是蓝莓，今天是每日一题的第 20 天。

**题目清单**：[一起刷力扣](https://blueberry-universe.cn/lc/index.html)

**引用力扣题目**：[242 有效的字母异位词](https://leetcode.cn/problems/valid-anagram/description/)





## 题目描述

给定两个字符串 `s` 和 `t` ，编写一个函数来判断 `t` 是否是 `s` 的 

字母异位词

。



 

**示例 1:**

```
输入: s = "anagram", t = "nagaram"
输出: true
```

**示例 2:**

```
输入: s = "rat", t = "car"
输出: false
```

 

**提示:**

- `1 <= s.length, t.length <= 5 * 104`
- `s` 和 `t` 仅包含小写字母





## 实现

**思路**

- 这是一个简单题，可以用来练习使用 `map` 
- 我们可以先使用 `map` 统计字符串 `s` 中每个字符出现的频率
- 然后，遍历字符串 `t` ，对于 `t` 中出现的字符是必须在 `s` 中出现相同次数的，每遍历到一个字符，我们就对 `map` 中统计到的频率进行减1的操作
- 如果我们发现一个字符在 `map` 中的频率已经小于等于 0 了，那就说明 `s` 字符串中的字符的个数不满足要求，就可以直接返回 `false` 了





**C++ 代码实现**

```c++
class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> record;
		
        // 首先要保证 s 和 t 的长度是一直的才行
        if( s.size() != t.size() ) {
            return false;
        }

        for( int i = 0 ; i < s.size() ; i++ ) {
            record[s[i]]++;
        }

        for( int i = 0 ; i < t.size() ; i++ ) {
            if( record.find(t[i]) != record.end() && record[t[i]] > 0 ) {
                // 匹配的情况下对频率进行减 1 操作
                record[t[i]]--;
            } else {
                // 比匹配的情况下返回 false
                return false;
            }
        }
		
        // 如果字符串 t 已经遍历完了也没有发现不匹配的则说明匹配成功
        return true;
    }
};
```

