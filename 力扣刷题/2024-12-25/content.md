# 「每日一题」力扣 125 验证回文串

你好啊，我是蓝莓，今天是每日一题的第 7 天。

**题目清单**：https://blueberry-universe.cn/lc/index.html

**引用力扣题目**：https://leetcode.cn/problems/valid-palindrome/description/





## 题目描述

如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，短语正着读和反着读都一样。则可以认为该短语是一个 **回文串** 。

字母和数字都属于字母数字字符。

给你一个字符串 `s`，如果它是 **回文串** ，返回 `true` ；否则，返回 `false` 。

 

**示例 1：**

```
输入: s = "A man, a plan, a canal: Panama"
输出：true
解释："amanaplanacanalpanama" 是回文串。
```

**示例 2：**

```
输入：s = "race a car"
输出：false
解释："raceacar" 不是回文串。
```

**示例 3：**

```
输入：s = " "
输出：true
解释：在移除非字母数字字符之后，s 是一个空字符串 "" 。
由于空字符串正着反着读都一样，所以是回文串。
```

 

**提示：**

- `1 <= s.length <= 2 * 105`
- `s` 仅由可打印的 ASCII 字符组成



## 实现

- 这个题目是使用双指针的方法来实现，类似的还有这篇文章 [「每日一题」力扣 167 两数之和 II - 输入有序数组](https://mp.weixin.qq.com/s/iVi7FMz_zsnpK95uaLUiAA)

- 使用索引 `i` 从字符串的左侧开始遍历，使用索引 `j` 从字符串的右侧开始遍历
- 将`s[i]` 和 `s[j]`先转换为小写字母后，判断是不是相等，如果不相等的话说明不满足，返回 `false` 即可
- 但是在移动索引 `i` 和 `j` 的过程中要记得每次做完是否相等的判断后，还需要跳过那些不满足大小写字母和数字的字符；为了判断当前字符是是大小写字母或者数字，我做了一个函数 `isValidChar` 来判断





**Python 代码实现**

```python
class Solution:
    def isValidChar(self, c: str) -> bool:
        return ('A' <= c <= 'Z') or ('a' <= c <= 'z') or ('0' <= c <= '9')

    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        while i <= j and not self.isValidChar(s[i]):
            i += 1
        while i <= j and not self.isValidChar(s[j]):
            j -= 1

        while i <= j:
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
            while i <= j and not self.isValidChar(s[i]):
                i += 1
            while i <= j and not self.isValidChar(s[j]):
                j -= 1

        return True
```





**C++ 代码实现**

```c++
class Solution {
public:
    bool isValidChar(char c) {
        if( (c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z') || ( c >= '0' && c <= '9') ) {
            return true;
        }

        return false;
    }

    bool isPalindrome(string s) {
        int i = 0;
        int j = s.size() - 1;
        
        while( i <= j && !isValidChar(s[i]) ) i++;
        while( i <= j && !isValidChar(s[j]) ) j--;

        while( i <= j ) {
            if( tolower(s[i]) != tolower(s[j]) ) return false;

            i++;
            j--;

            while( i <= j && !isValidChar(s[i]) ) i++;
            while( i <= j && !isValidChar(s[j]) ) j--;
        }

        return true;
    }
};
```





**Java 代码实现**

```java
class Solution {
    private boolean isValidChar(char c) {
        return (c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z') || (c >= '0' && c <= '9');
    }

    public boolean isPalindrome(String s) {
        int i = 0, j = s.length() - 1;

        while (i <= j && !isValidChar(s.charAt(i))) {
            i++;
        }
        while (i <= j && !isValidChar(s.charAt(j))) {
            j--;
        }

        while (i <= j) {
            if (Character.toLowerCase(s.charAt(i)) != Character.toLowerCase(s.charAt(j))) {
                return false;
            }
            i++;
            j--;
            while (i <= j && !isValidChar(s.charAt(i))) {
                i++;
            }
            while (i <= j && !isValidChar(s.charAt(j))) {
                j--;
            }
        }

        return true;
    }
}
```





**Golang 代码实现**

```go
func isValidChar(c rune) bool {
    return unicode.IsLetter(c) || unicode.IsDigit(c)
}

func isPalindrome(s string) bool {
    i, j := 0, len(s)-1

    for i <= j {
        for i <= j && !isValidChar(rune(s[i])) {
            i++
        }
        for i <= j && !isValidChar(rune(s[j])) {
            j--
        }
        if i <= j {
            if unicode.ToLower(rune(s[i])) != unicode.ToLower(rune(s[j])) {
                return false
            }
            i++
            j--
        }
    }

    return true
}
```

