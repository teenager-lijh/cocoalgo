# 「每日一题」力扣 290 单词规律

你好啊，我是蓝莓，今天是每日一题的第 22 天。

**题目清单**：[一起刷力扣](https://blueberry-universe.cn/lc/index.html)

**引用力扣题目**：[290 单词规律](https://leetcode.cn/problems/word-pattern/description/)





## 题目描述

给定一种规律 `pattern` 和一个字符串 `s` ，判断 `s` 是否遵循相同的规律。

这里的 **遵循** 指完全匹配，例如， `pattern` 里的每个字母和字符串 `s` 中的每个非空单词之间存在着双向连接的对应规律。

 

**示例1:**

```
输入: pattern = "abba", s = "dog cat cat dog"
输出: true
```

**示例 2:**

```
输入:pattern = "abba", s = "dog cat cat fish"
输出: false
```

**示例 3:**

```
输入: pattern = "aaaa", s = "dog cat cat dog"
输出: false
```

 

**提示:**

- `1 <= pattern.length <= 300`
- `pattern` 只包含小写英文字母
- `1 <= s.length <= 3000`
- `s` 只包含小写英文字母和 `' '`
- `s` **不包含** 任何前导或尾随对空格
- `s` 中每个单词都被 **单个空格** 分隔





## 实现

**思路**

- 按照题目的要求来做这个题目就可以了
- 需要我们使用两个 `map` 来记录映射关系
- 第一个映射关系是从 `pattern` 中的单个 `char` 到 `s` 字符串中的单个 `word`
- 第二个映射关系是从 `s` 中的单个 `word` 到 `pattern` 中的单个 `char`
- 为什么需要记录两次映射关系？
- 这是为了保证映射的唯一，因为 `a` 可能映射到 `dog` 也可能存在 `cat` 和 `a` 是对应的
- 如果我们不同时记录两个方向的映射的话，我们就没办法保证这个映射是唯一的
- 在代码中使用 `forward` 记录第一个映射关系，使用 `backward` 记录第二个映射关系
- 遍历 `p` 字符串并且在遍历的过程中去 `s` 字符串中寻找当 `start` 指向的起始位置的这个单词的结束位置的下一个位置 `end`





**C++ 代码实现** 

```c++
class Solution {
public:
    bool wordPattern(string pattern, string s) {

        unordered_map<char, string> forward;  // 从 char 到 word 的映射
        unordered_map<string, char> backward;  // 从 word 到 char 的映射

        int start = 0;
        int end = 0;
        int wordCount = 0;  // 统计遍历过的 s 中的 word 的数量

        for( int i = 0 ; i < pattern.size() && end < s.size() ; i++, wordCount++ ) {

            // 寻找下一个单词
            while( s[end] != ' ' && end < s.size() ) end++;

            // 提取出这次找到的单词
            string word = s.substr(start, end-start);

            // 为再次寻找下一个单词做准备
            end += 1;
            start = end;

            if( forward.find(pattern[i]) != forward.end() && backward.find(word) != backward.end() ) {
                // 映射关系不唯一 返回失败
                if( forward[pattern[i]] != word || backward[word] != pattern[i] ) return false;
            } else {

                // 双向没有同时存在映射的情况下 若其中一个方向存在映射则失败
                if( forward.find(pattern[i]) != forward.end() || backward.find(word) != backward.end() ) {
                    return false;
                }

                // 两个方向都没有映射 就可以放心的添加映射了
                forward[pattern[i]] = word;
                backward[word] = pattern[i];
            }
        }

        // 如果 s 中的单词没有全部遍历完 或者 两者应该对应的单词的数量不一致 则返回失败
        if( end < s.size() || pattern.size() != wordCount ) {
            return false;
        }

        return true;
    }
};
```

