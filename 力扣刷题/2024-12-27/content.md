# 「每日一题」力扣 11 盛最多水的容器

你好啊，我是蓝莓，今天是每日一题的第 11 天。

**题目清单**：[一起刷力扣](https://blueberry-universe.cn/lc/index.html)

**引用力扣题目**：[力扣 11 盛最多水的容器](https://leetcode.cn/problems/container-with-most-water/description/)





## 题目描述

给定一个长度为 `n` 的整数数组 `height` 。有 `n` 条垂线，第 `i` 条线的两个端点是 `(i, 0)` 和 `(i, height[i])` 。

找出其中的两条线，使得它们与 `x` 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

**说明：**你不能倾斜容器。

**示例 1：**

![img](content.assets/question_11.jpg)

```
输入：[1,8,6,2,5,4,8,3,7]
输出：49 
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
```

**示例 2：**

```
输入：height = [1,1]
输出：1
```

 

**提示：**

- `n == height.length`
- `2 <= n <= 105`
- `0 <= height[i] <= 104`



## 实现

**思路**

- 这是一个使用双指针的题目
- 使用索引 `i` 从 `height` 数组的左侧开始遍历，`i` 的初始值为 0
- 使用索引 `j` 从 `height` 数组的右侧开始遍历，`j` 的初始值为 n - 1，其中 n 为数组长度
- 使用 `res` 保存当前的最大值，如果 `min(height[i], height[j]) * (j-i)` 大于当前的 `res` 那么就更新 `res` 的值
- 如果这时候 `height[i]` 更短一些，那么就尝试着向右移动 `i` 去寻找更长的左侧板子
- 如果这时候 `height[j]` 更短一些，那么就尝试着向左移动 `j` 去寻找更长的右侧板子
- 关于这种操作会不会漏掉一些其他的情况：当 `height[i]` 更短一些的时候，如果我们不选择移动 `i` 而是选择向左移动 `j`，那么你可以知道，底边的长度是必然会变小的，然而在向左移动 `j` 的过程中只会出现两种情况
- （1）`height[j]` 变得更长了，但是这并没有用，因为`height[i]` 是短板，而且底边也在变小，所以并不能使得 `res` 变大；
- （2）`height[j]` 变得更短了，甚至比 `height[i]` 还要短，这就更糟糕了，因为 `height[j]` 变成了短板，而且底边也在不断的变小；
- 经过以上分析，我们可以知道，我们可以直接排除掉这些不必要的运算过程，所以我们的方法是没有问题的。
- 关于这一点，在力扣上有一个题解很不错，可以参考：

题解传送门：[11 盛最多水的容器题解](https://leetcode.cn/problems/container-with-most-water/solutions/11491/container-with-most-water-shuang-zhi-zhen-fa-yi-do/)





**C++ 代码实现**

```c++
class Solution {
public:
    int maxArea(vector<int>& height) {
        int i = 0;
        int j = height.size() - 1;

        int res = 0;

        while( i < j ) {
            if( height[i] > height[j] ) {
                res = max(res, (j-i) * height[j]);
                j--;
            } else {
                // height[i] < height[j]
                res = max(res, (j-i) * height[i]);
                i++;
            }
        }

        return res;
    }
};
```

