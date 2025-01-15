# 「每日一题」力扣 205 同构字符串

你好啊，我是蓝莓，今天是每日一题的第 23 天。

**题目清单**：[一起刷力扣](https://blueberry-universe.cn/lc/index.html)

**引用力扣题目**：[205 同构字符串](https://leetcode.cn/problems/isomorphic-strings/description/)





## 题目描述

给定两个字符串 `s` 和 `t` ，判断它们是否是同构的。

如果 `s` 中的字符可以按某种映射关系替换得到 `t` ，那么这两个字符串是同构的。

每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。

 

**示例 1:**

```
输入：s = "egg", t = "add"
输出：true
```

**示例 2：**

```
输入：s = "foo", t = "bar"
输出：false
```

**示例 3：**

```
输入：s = "paper", t = "title"
输出：true
```

 

**提示：**



- `1 <= s.length <= 5 * 104`
- `t.length == s.length`
- `s` 和 `t` 由任意有效的 ASCII 字符组成





## 实现

**思路**

- 这个题目和 `290` 号题目是一样的思路
- 使用 `map` 维护一个双向的数据结构就可以了
- 而且这个题目还不需要自己去拆分字符串中的单词
- 它只需要让字符之间拥有映射关系即可





**C++ 代码实现**

```c++
class Solution {
public:
    bool isIsomorphic(string s, string t) {
        unordered_map<char, char> forward;
        unordered_map<char, char> backward;

        // 起码长度是要相等的
        if( s.size() != t.size() ) {
            return false;
        }

        for( int i = 0 ; i < s.size() ; i++ ) {
            // 看看当前是不是双向都有映射关系
            if( forward.find(s[i]) != forward.end() && backward.find(t[i]) != backward.end() ) {
                if( forward[s[i]] != t[i] || backward[t[i]] != s[i] ) return false;
            } else {
                // 如果不是双向都有映射关系 但是其中一个方向出现了映射 那必然是错的
                if( forward.find(s[i]) != forward.end() || backward.find(t[i]) != backward.end() ) return false;

                // 如果都没有映射关系那么就保存当前发现的映射关系
                forward[s[i]] = t[i];
                backward[t[i]] = s[i];
            }
        }

        return true;
    }
};
```

