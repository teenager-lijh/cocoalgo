# 「每日一题」力扣 71 简化路径

你好啊，我是蓝莓，今天是每日一题的第 53 天。

**题目清单**：[一起刷力扣](https://blueberry-universe.cn/lc/index.html)

**引用力扣题目**：[71 简化路径](https://leetcode.cn/problems/evaluate-reverse-polish-notation/description/)





## 题目描述

给你一个字符串 `path` ，表示指向某一文件或目录的 Unix 风格 **绝对路径** （以 `'/'` 开头），请你将其转化为 **更加简洁的规范路径**。

在 Unix 风格的文件系统中规则如下：

- 一个点 `'.'` 表示当前目录本身。
- 此外，两个点 `'..'` 表示将目录切换到上一级（指向父目录）。
- 任意多个连续的斜杠（即，`'//'` 或 `'///'`）都被视为单个斜杠 `'/'`。
- 任何其他格式的点（例如，`'...'` 或 `'....'`）均被视为有效的文件/目录名称。

返回的 **简化路径** 必须遵循下述格式：

- 始终以斜杠 `'/'` 开头。
- 两个目录名之间必须只有一个斜杠 `'/'` 。
- 最后一个目录名（如果存在）**不能** 以 `'/'` 结尾。
- 此外，路径仅包含从根目录到目标文件或目录的路径上的目录（即，不含 `'.'` 或 `'..'`）。

返回简化后得到的 **规范路径** 。

 

**示例 1：**

**输入：**path = "/home/"

**输出：**"/home"

**解释：**

应删除尾随斜杠。

**示例 2：**

**输入：**path = "/home//foo/"

**输出：**"/home/foo"

**解释：**

多个连续的斜杠被单个斜杠替换。

**示例 3：**

**输入：**path = "/home/user/Documents/../Pictures"

**输出：**"/home/user/Pictures"

**解释：**

两个点 `".."` 表示上一级目录（父目录）。

**示例 4：**

**输入：**path = "/../"

**输出：**"/"

**解释：**

不可能从根目录上升一级目录。

**示例 5：**

**输入：**path = "/.../a/../b/c/../d/./"

**输出：**"/.../b/d"

**解释：**

`"..."` 在这个问题中是一个合法的目录名。

 

**提示：**

- `1 <= path.length <= 3000`
- `path` 由英文字母，数字，`'.'`，`'/'` 或 `'_'` 组成。
- `path` 是一个有效的 Unix 风格绝对路径。





## 实现

**思路**

- 这是一个力扣的中等题
- 对于这个题目来说，我们先将 `path` 字符串按照 `/` 拆分，然后遍历拆分后的结果，对于每一个拆分后的结果判断需要做什么操作
- （1）如果当前项是 `..` 说明我们要返回到当前所在目录的上一级目录，那其实就是把记录中的刚访问过的那个目录的名字给它删掉就好了
- （2）如果当前的项是 `.` 说明我们要访问当前所在的目录，这说明我们什么都不用做，静静的待在当前所在的目录就可以了，直接跳过就 ok
- （3）如果当前访问到的是以上两种情况以外的项，那么说明我们应该访问当前的这个项，所以这时候我们应该在结果中添加这一项
- 还有更多的细节都在代码中啦！





**C++ 代码实现**

```c++
class Solution {
public:
    string simplifyPath(string path) {
        // 先讲 path 按照 '/' 字符进行拆分
        vector<string> names = split(path, '/');
        // result 保留最后的路径中所包含的项
        vector<string> result;

        for( string name : names ) {
            if( name == ".." ) {
                // 如果是 .. 说明我们应该跳转到当前访问的目录的上一级目录
                // 所以直接将当前访问的目录给 pop 出去就可以了
                // 注意检查是不是当前目录就是根目录了
                // 如果当前目录就是根目录，说明 result 里面没有元素
                if( result.size() >= 1 ) {
                    result.pop_back();
                }
            } else if( name == "." ){
                // 如果是访问当前目录，那就直接跳过好啦
                continue;
            } else {
                // 将要访问的新的目录名纳入结果中
                result.push_back(name);
            }
        }

        // 使用 res 来拼接最终简化后的字符串
        string res = "";
        for( string name : result ) {
            res += "/" + name;
        }
        
        // 很有可能简化后的字符串就是根目录
        // 所以我们应该看看 res 是不是为空
        //  如果为空的话，我们直接返回根目录就可以了
        if( res == "" ) {
            return "/";
        }

        // 不为空则返回 res
        return res;
    }

    vector<string> split(const string& str, char delimiter) {
        // 按照 delimiter 字符将 str 字符串拆拆分为多个子串
        // 若拆分出来的某个子串为空串的话 ==> 直接丢弃
        vector<string> slices;
        int start = 0;

        while( start < str.size() ) {
            // start 是上一次的拆分点的下一个字符
            // 寻找到拆分点 end
            int end = str.find(delimiter, start);
            if( end == -1 ) break;
            // 取 str[start, end) 这个区间内的元素
            string slice = str.substr(start, end-start);
            start = end + 1; // 让 start 移动到这一次的拆分点的下一个字符
            // 丢弃空串
            if( slice.empty() ) continue;
            // 保留非空串
            slices.push_back(slice);
        }

        // 很有可能最后一个子串没有被装进结果中 ==> 做一次特殊的检查
        if( start < str.size() && !str.substr(start, str.size()-start).empty() ) {
            slices.push_back(str.substr(start, str.size()-start));
        }

        return slices;
    }
};
```

