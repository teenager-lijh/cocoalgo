# 「每日一题」力扣 345 反转字符串中的元音字母

你好啊，我是蓝莓，今天是每日一题的第 10 天。



从明天开始，题解的文章就只在我的博客更新啦，暂时不会把每个题目的题解都更新在公众号了。

如果你对刷力扣的题目感兴趣，**欢迎你添加我的微信，我拉你进群一起刷题**。添加微信的方法是在我的微信公众号下方点击 **联系我** 可以收到我的微信二维码。

题目清单就是我的博客对应的力扣题目的地址啦。



**题目清单**：https://blueberry-universe.cn/lc/index.html

**引用力扣题目**：https://leetcode.cn/problems/reverse-vowels-of-a-string/description/





## 题目描述

给你一个字符串 `s` ，仅反转字符串中的所有元音字母，并返回结果字符串。

元音字母包括 `'a'`、`'e'`、`'i'`、`'o'`、`'u'`，且可能以大小写两种形式出现不止一次。

 

**示例 1：**

**输入：**s = "IceCreAm"

**输出：**"AceCreIm"

**解释：**

`s` 中的元音是 `['I', 'e', 'e', 'A']`。反转这些元音，`s` 变为 `"AceCreIm"`.

**示例 2：**

**输入：**s = "leetcode"

**输出：**"leotcede"

 

**提示：**

- `1 <= s.length <= 3 * 105`
- `s` 由 **可打印的 ASCII** 字符组成





## 实现

**思路**

- 这个题目仍然是使用双指针，同样使用双指针的题目还有以下两篇文章

[**「每日一题」力扣 167 两数之和 II - 输入有序数组**](https://mp.weixin.qq.com/s/iVi7FMz_zsnpK95uaLUiAA)

[**「每日一题」力扣 125 验证回文串**](https://mp.weixin.qq.com/s/qkX1T4AqnCmYhTCxtYuY9Q)

- 使用索引 `i` 从左侧开始遍历，它的初始值为 `0`
- 使用索引 `j` 从右侧开始遍历，它的初始值为 `n-1`；这里的 n 代表字符串的长度
- 交换 `i` 和 `j` 所指向的元音字母的位置，然后再让两个索引继续跳转到下一个原因字母即可
- 使用 `isVowelLetter` 函数来判断当前字符是否是元音字母





**Python 代码实现**

```python
class Solution:
    def reverseVowels(self, s: str) -> str:

        def is_vowel_letter(letter: str) -> bool:
            letter = letter.lower()
            return letter in {'a', 'e', 'i', 'o', 'u'}
        
        s = list(s)
        i, j = 0, len(s) - 1

        while i < j and not is_vowel_letter(s[i]):
            i += 1
        while i < j and not is_vowel_letter(s[j]):
            j -= 1
        
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
            
            while i < j and not is_vowel_letter(s[i]):
                i += 1
            while i < j and not is_vowel_letter(s[j]):
                j -= 1

        return ''.join(s)
```





**C++ 代码实现**

```c++
class Solution {
public:
    bool isVowelLetter(char letter) {
        letter = tolower(letter);
        return letter == 'a' || letter == 'e' || letter == 'i' || letter == 'o' || letter == 'u';
    }

    string reverseVowels(string s) {
        int i = 0;
        int j = s.size() - 1;

        while( i < j && !isVowelLetter(s[i]) ) i++;
        while( i < j && !isVowelLetter(s[j]) ) j--;

        while( i < j ) {
            swap(s[i], s[j]);

            i++;
            j--;

            while( i < j && !isVowelLetter(s[i]) ) i++;
            while( i < j && !isVowelLetter(s[j]) ) j--;
        }

        return s;
    }
};
```





**Java 代码**

```java
class Solution {
    private boolean isVowel(char letter) {
        letter = Character.toLowerCase(letter);
        return letter == 'a' || letter == 'e' || letter == 'i' || letter == 'o' || letter == 'u';
    }

    public String reverseVowels(String s) {


        char[] chars = s.toCharArray();
        int i = 0, j = chars.length - 1;

        while (i < j && !isVowel(chars[i])) i++;
        while (i < j && !isVowel(chars[j])) j--;

        while (i < j) {
            char temp = chars[i];
            chars[i] = chars[j];
            chars[j] = temp;
            i++;
            j--;

            while (i < j && !isVowel(chars[i])) i++;
            while (i < j && !isVowel(chars[j])) j--;
        }

        return new String(chars);
    }
}
```





**Golang 代码实现**

```golang
func isVowelLetter(c byte) bool {
	c = byte(unicode.ToLower(rune(c)))
	return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'
}

func reverseVowels(s string) string {
	bytes := []byte(s)
	i, j := 0, len(bytes)-1

    for i < j && !isVowelLetter(bytes[i]) {
        i++
    }
    
    for i < j && !isVowelLetter(bytes[j]) {
        j--
    }

	for i < j {
        bytes[i], bytes[j] = bytes[j], bytes[i]
			i++
			j--

	}

	return string(bytes)
}
```

