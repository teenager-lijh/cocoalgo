# 「每日一题」力扣 76 最小覆盖子串

你好啊，我是蓝莓，今天是每日一题的第 17 天。

**题目清单**：[一起刷力扣](https://blueberry-universe.cn/lc/index.html)

**引用力扣题目**：[76 最小覆盖子串](https://leetcode.cn/problems/minimum-window-substring/description/)





## 题目描述

给你一个字符串 `s` 、一个字符串 `t` 。返回 `s` 中涵盖 `t` 所有字符的最小子串。如果 `s` 中不存在涵盖 `t` 所有字符的子串，则返回空字符串 `""` 。

 

**注意：**

- 对于 `t` 中重复字符，我们寻找的子字符串中该字符数量必须不少于 `t` 中该字符数量。
- 如果 `s` 中存在这样的子串，我们保证它是唯一的答案。

 

**示例 1：**

```
输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。
```

**示例 2：**

```
输入：s = "a", t = "a"
输出："a"
解释：整个字符串 s 是最小覆盖子串。
```

**示例 3:**

```
输入: s = "a", t = "aa"
输出: ""
解释: t 中两个字符 'a' 均应包含在 s 的子串中，
因此没有符合条件的子字符串，返回空字符串。
```

 

**提示：**

- `m == s.length`
- `n == t.length`
- `1 <= m, n <= 105`
- `s` 和 `t` 由英文字母组成





## 实现

**思路**

- 使用可变的滑动窗口
- 这个题目和 438 号题目的题解类似，我们使用 `record` 记录对于每个字符的需求量
- 首先使用 `t` 字符串初始化一开始对每个字符的需求量都是多大
- 然后遍历 `s` 字符串，在窗口滑动的过程中分为两种情况
- （1）当前如果不满足要求的话，那么就扩大窗口的范围，同时维护 `record` 中的记录
- （2）如果当前已经满足要求了，那么我们就判断下，当前发现的子串的长度是不是比我们之前找到的子串的长度还要小，如果还要小的话就更新一下子串的起始位置和长度。接着，我们这时候不再扩大窗口了，我们尝试着缩小窗口去寻找更短的满足要求的子串





**C++ 代码实现**

```c++
class Solution {
public:
    string minWindow(string s, string t) {
        if( s.size() < t.size() ) {
            return "";
        }

        int record[256];

        // 数组置空
        memset(record, 0, sizeof(record));

        // 初始化原始需求量
        for( int i = 0 ; i < t.size() ; i++ ) {
            record[t[i]]++;
        }

        // 维护区间 [l...r)
        int l = 0;
        int r = 0;

        // 记录最小覆盖子串的起始位置
        int start = -1;
        // 记录最小覆盖子串的长度
        int minimum_size = INT_MAX;

        while( r <= s.size() ) {
            bool ok = true;

            // 检查是否满足要求
            for( int i = 'A' ; i <= 'z' ; i++ ) {
                if( record[i] > 0 ) {
                    ok = false;
                    break;
                }
            }

            if(ok) {
                // 记录当前的最小字符串
                if( minimum_size > r-l ) {
                    minimum_size = r-l;
                    start = l;
                }

                // 当前已经满足要求 尝试缩小窗口的大小
                record[s[l++]]++;
            } else {
                // 继续扩大窗口
                // 纳入新的元素到 record
                // 对该元素的需求减少 1
                record[s[r++]]--;
            }
        }
        
        if( start == -1 ) {
            return "";
        }

        return s.substr(start, minimum_size);
    }
};
```

