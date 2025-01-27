# 「每日一题」力扣 231 2的幂

你好啊，我是蓝莓，今天是每日一题的第 38 天。

**题目清单**：[一起刷力扣](https://blueberry-universe.cn/lc/index.html)

**引用力扣题目**：[231 2的幂](https://leetcode.cn/problems/power-of-two/description/)





## 题目描述

给你一个整数 `n`，请你判断该整数是否是 2 的幂次方。如果是，返回 `true` ；否则，返回 `false` 。

如果存在一个整数 `x` 使得 `n == 2x` ，则认为 `n` 是 2 的幂次方。

 

**示例 1：**

```
输入：n = 1
输出：true
解释：20 = 1
```

**示例 2：**

```
输入：n = 16
输出：true
解释：24 = 16
```

**示例 3：**

```
输入：n = 3
输出：false
```

 

**提示：**

- `-231 <= n <= 231 - 1`

 

**进阶：**你能够不使用循环/递归解决此问题吗？





## 实现

**思路**

- 从整型在机器码的表示上来看，如果这个数值是 2 的整数幂的话，在数值为正的情况下低 31 个比特位只会出现一个比特位为 1 ，其余的比特位都为 0
- 2 的 0 次幂是一个特殊的情况可以单独进行判断
- 另外就是排除 n 为负数的情况





**C++ 代码实现**

```c++
class Solution {
public:
    bool isPowerOfTwo(int n) {
        
        // 排序 n 小于 0 的情况
        if( n < 0 ) {
            return false;
        }
        
        int nums = 0;

        // 统计非符号位上比特位为 1 的个数
        for( int size = 0 ; size < 31 ; size++ ) {
            if( n >> size & 0x1 ) {
                nums++;
            }
        }

        if( nums > 1 || nums == 0 ) {
            return false;
        }

        return true;
    }
};
```

