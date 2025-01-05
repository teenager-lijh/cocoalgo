# 「每日一题」力扣 3 无重复字符的最长子串

你好啊，我是蓝莓，今天是每日一题的第 13 天。

**题目清单**：[一起刷力扣](https://blueberry-universe.cn/lc/index.html)

**引用力扣题目**：[189 轮转数组](https://leetcode.cn/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150)





## 题目描述

给定一个字符串 `s` ，请你找出其中不含有重复字符的 **最长子串**

 的长度。



**示例 1:**

```
输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
```

**示例 2:**

```
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
```

**示例 3:**

```
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
```

 

**提示：**

- `0 <= s.length <= 5 * 104`
- `s` 由英文字母、数字、符号和空格组成





## 实现

**思路**

- 使用滑动窗口 + 记录每个字符在窗口内出现的次数
- 使用索引 `i` 代表窗口的左边界，使用索引 `j` 代表窗口的右边界，维护区间 `[i...j]` 为窗口
- 当纳入新的元素到窗口中的时候，如果发现该元素已经出现过一次了，那就从窗口的左侧开始缩小窗口，直到将该元素移出窗口的范围





**C++ 代码实现**

```c++
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int res = 0;
        int record[256];

        for( int k = 0 ; k < 256 ; k++ ) {
            record[k] = 0;
        }

        // 维护闭区间 [i...j] 为窗口
        for( int i = 0, j = 0 ; j < s.size() ; j++ ) {
            record[s[j]]++;
			
            // 跳过重复元素
            while(record[s[j]] > 1) record[s[i++]]--;
            
            res = max(res, j-i+1);
        }

        return res;
    }
};
```



