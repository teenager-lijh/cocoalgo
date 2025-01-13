# 「每日一题」力扣 202 快乐数

你好啊，我是蓝莓，今天是每日一题的第 21 天。

**题目清单**：[一起刷力扣](https://blueberry-universe.cn/lc/index.html)

**引用力扣题目**：[202 快乐数](https://leetcode.cn/problems/happy-number/description/)





## 题目描述

编写一个算法来判断一个数 `n` 是不是快乐数。

**「快乐数」** 定义为：

- 对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
- 然后重复这个过程直到这个数变为 1，也可能是 **无限循环** 但始终变不到 1。
- 如果这个过程 **结果为** 1，那么这个数就是快乐数。

如果 `n` 是 *快乐数* 就返回 `true` ；不是，则返回 `false` 。

 

**示例 1：**

```
输入：n = 19
输出：true
解释：
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
```

**示例 2：**

```
输入：n = 2
输出：false
```

 

**提示：**

- `1 <= n <= 231 - 1`





## 实现

**思路**

- 这是一个简单题，只需要按着题目来做即可
- 主要可以学习一下怎么取一个数值的十进制表示情况下的各个位置上的数值
- 为了防止死循环，我们需要对之前已经迭代过得数值做一个记录，直接使用 哈希表 即可





**C++ 代码实现**

```c++
class Solution {
public:
    bool isHappy(int n) {
        
        unordered_set<int> record;
        record.insert(n);

        // 假设上一次得到的数值为 sum
        int sum = n;

        while( true ) {
            
            // 把上一次得到的数值 sum 放在 n 里面
            n = sum;
            // 重新计算各个位置上的数值平方的和
            sum = 0;

            // 只要 n 还是大于 0 的 那就不停地取末尾数值
            while( n > 0 ) {
                int res = n % 10;
                n = n / 10;
                sum += res * res;    
            }

            // 如果已经发现等于 1 了 说明是快乐数 直接返回
            if( sum == 1 ) return true;

            // 如果发现这个数值 在之前已经得到过了 那就没必要继续下去了
            // 会造成死循环 说明这不是一个快乐数
            if( record.find(sum) != record.end() ) {
                return false;
            }

            // 记录下当前迭代到的数值 sum
            record.insert( sum );
        }

        return false;
    }
};
```

