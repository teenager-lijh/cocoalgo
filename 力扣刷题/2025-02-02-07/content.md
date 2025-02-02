# 「每日一题」力扣 20 有效的括号

你好啊，我是蓝莓，今天是每日一题的第 51 天。

**题目清单**：[一起刷力扣](https://blueberry-universe.cn/lc/index.html)

**引用力扣题目**：[20 有效的括号](https://leetcode.cn/problems/valid-parentheses/description/)





## 题目描述

给定一个只包括 `'('`，`')'`，`'{'`，`'}'`，`'['`，`']'` 的字符串 `s` ，判断字符串是否有效。

有效字符串需满足：

1. 左括号必须用相同类型的右括号闭合。
2. 左括号必须以正确的顺序闭合。
3. 每个右括号都有一个对应的相同类型的左括号。

 

**示例 1：**

**输入：**s = "()"

**输出：**true

**示例 2：**

**输入：**s = "()[]{}"

**输出：**true

**示例 3：**

**输入：**s = "(]"

**输出：**false

**示例 4：**

**输入：**s = "([])"

**输出：**true

 

**提示：**

- `1 <= s.length <= 104`
- `s` 仅由括号 `'()[]{}'` 组成





## 实现

**思路**

- 这是一个应用栈的简单题
- （1）在遍历字符串 `s` 的过程中，如果我们遇到的是括号的左半部分，那么我们就把这个括号压入栈中
- （2）如果在遍历的过程中，我们遇到的是括号的有半部分，那么我们就和栈顶的括号进行比对，看看是不是能够匹配成为一个完整的括号





**C++ 代码实现**

```c++
class Solution {
public:
    bool isValid(string s) {
        stack<char> record;

        for( int i = 0 ; i < s.size(); i++ ) {
            if( s[i] == '(' || s[i] == '{' || s[i] == '[' ) {
                record.push(s[i]);
            } else {
                if( record.empty() ) {
                    return false;
                }

                char top = record.top();
                record.pop();
                bool c1 = (top == '(' && s[i] == ')');
                bool c2 = (top == '{' && s[i] == '}');
                bool c3 = (top == '[' && s[i] == ']');

                if( c1 || c2 || c3 ) {
                    continue;
                } else {
                    return false;
                }
            }
        }

        if( record.size() == 0 ) {
            return true;
        } else {
            return false;
        }
    }
};
```

