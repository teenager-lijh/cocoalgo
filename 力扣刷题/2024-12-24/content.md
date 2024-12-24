# 「每日一题」力扣 167 两数之和 II - 输入有序数组

你好啊，我是蓝莓，今天是每日一题的第 8 天。

题目清单非常重要，每个题目都是经过分类的，可以有针对性的使用这些题目进行练习，可以看看。

**题目清单**：[点我](https://blueberry-universe.cn/lc/index.html)

**引用力扣题目**：[点我](https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/description/)





## 题目描述

给你一个下标从 **1** 开始的整数数组 `numbers` ，该数组已按 **非递减顺序排列** ，请你从数组中找出满足相加之和等于目标数 `target` 的两个数。如果设这两个数分别是 `numbers[index1]` 和 `numbers[index2]` ，则 `1 <= index1 < index2 <= numbers.length` 。

以长度为 2 的整数数组 `[index1, index2]` 的形式返回这两个整数的下标 `index1` 和 `index2`。

你可以假设每个输入 **只对应唯一的答案** ，而且你 **不可以** 重复使用相同的元素。

你所设计的解决方案必须只使用常量级的额外空间。

 

**示例 1：**

```
输入：numbers = [2,7,11,15], target = 9
输出：[1,2]
解释：2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。返回 [1, 2] 。
```

**示例 2：**

```
输入：numbers = [2,3,4], target = 6
输出：[1,3]
解释：2 与 4 之和等于目标数 6 。因此 index1 = 1, index2 = 3 。返回 [1, 3] 。
```

**示例 3：**

```
输入：numbers = [-1,0], target = -1
输出：[1,2]
解释：-1 与 0 之和等于目标数 -1 。因此 index1 = 1, index2 = 2 。返回 [1, 2] 。
```

 

**提示：**

- `2 <= numbers.length <= 3 * 104`
- `-1000 <= numbers[i] <= 1000`
- `numbers` 按 **非递减顺序** 排列
- `-1000 <= target <= 1000`
- **仅存在一个有效答案**





## 实现

**思路**

- 这个题目开始会有四个使用双指针的题目
- 对于这个题目来说，最容易想到的暴力解法就是使用两层循环，遍历所有的两个数值为一对的组合
- 对于组合来说相信并不陌生，最简单的代码实现可能是下面这样子的

```c++
// 寻找组合的两层循环

for( int i = 0 ; i < len(numbers) ; i++ ) {
    for( int j = i+1 ; j < len(numbers) ; j++ ) {
        // 在这里写对于每一对的要进行判断的逻辑
        // 你可以在这里判断 numbers[i] 和 numbers[j] 相加后的结果是否满足 target
        // 并做一些必要的处理
    }
}
```

- 你可以很容易的发现，这里的 `i` 是永远小于 `j` 的，这样可以保证我们不会寻找出重复的组合
- 对于经典的两层循环的代码可能是下面这样的

```c++
// 经典的两层循环
for( int i = 0 ; i < len(numbers) ; i++ ) {
	for( int j = 0 ; j < len(numbers) ; j++ ) {
		// 在这里写对于每一对的要进行判断的逻辑
        // 你可以在这里判断 numbers[i] 和 numbers[j] 相加后的结果是否满足 target
        // 并做一些必要的处理
	}
}
```

- `经典的两层循环` 和 `寻找组合的两层循环` 有什么区别 ？ 区别就在于 `经典的两层循环` 会寻找出重复的情况，比如对于一对组合 `numbers[5]` 和 `numbers[10]` ，我们可以让 `i` 和 `j` 分别等于 `5` 和 `10` 这就会出现重复的情况了。所以防止不出现重复的情况，我们应该使用 `寻找组合的两层循环` 这种写法，这种写法既不会出现 `i` 等于 `j` 的情况，也不会出现重复的情况
- 虽然说我们使用了 `寻找组合的两层循环` 可以降低很多不必要的操作，但是它依然是 O(N^2) 的时间复杂度
-  对于这个题目，我们要设计一个在 O(N) 的时间复杂度就可以完成的算法。双指针是什么 ？
- 我们设置索引 `i` 并设置初始值为 `0`
- 我们设置索引 `j` 并设置初始值为 `len(numbers) - 1` 也就是让 `j` 指向数组中的最后一个元素
- 我们检查 `numbers[i] + numbers[j]` 的值是不是等于 `target` 的值，如果相等的话，就说明我们找到了，如果不相等的话，只有可能出现两种情况。
- 第一种情况：`numbers[i] + numbers[j]` 的值大于 `target`，这种情况下可以选择让 `j` 的索引向左移动一下。因为数组是从小到大排序的，所以让 `j` 向左移动可以减小 `numbers[i] + numbers[j]`  的值。为什么我们不让 `i` 向右移动？因为如果让 `i` 向右移动势必会让  `numbers[i] + numbers[j]`  的值增大。也就是说：我们可以排除掉所有固定 `j` 的情况下， `i < j` 的情况下 `numbers[i] + numbers[j]` 的值了。通过这种方法，我们进一步缩小了搜索的空间。
- 第二种情况：`numbers[i] + numbers[j] ` 的值小于 `target`，这种情况下可以选择让 `i` 的索引向右移动一下。这样，`numbers[i] + numbers[j] `  就会增大一些。同理，我们思考一下，为什么这种情况下不能让 `j` 来向左移动？因为在固定 `i` 的情况下，所有 `j > i` 情况下的 `numbers[i] + numbers[j]` 的值都只会比当前的值更小。
- 相比于使用 `寻找组合的两层循环` 来说，在数组有序的情况下使用双指针可以让我们进一步的减小搜索空间。
- 在力扣上有一个题解很不错，使用了图解的方式对：为什么双指针不会漏掉一些情况的问题 ，进行了讲解。
- 题解链接：[点我](https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/solutions/87919/yi-zhang-tu-gao-su-ni-on-de-shuang-zhi-zhen-jie-fa/)





**Python 代码实现**

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while i < j:
            if numbers[i] + numbers[j] == target:
                return i+1, j+1
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1

        return 0, 0
```





**C++ 代码实现**

```c++
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int i = 0;
        int j = numbers.size() - 1;

        while( i < j ) {
            if( numbers[i] + numbers[j] == target ) {
                return vector({i+1, j+1});
            } else if( numbers[i] + numbers[j] > target ) {
                j--;
            } else {
                // numbers[i] + numbers[j] < target
                i++;
            }
        }

        return vector({0, 0});
    }
};
```





**Java 代码实现**

```java
class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int i = 0;
        int j = numbers.length - 1;

        while( i < j ) {
            if( numbers[i] + numbers[j] == target ) {
                return new int[]{i+1, j+1};
            }  else if( numbers[i] + numbers[j] > target ) {
                j -= 1;
            } else {
                // numbers[i] + numbers[j] < target 
                i += 1;
            }
        }

        return new int[]{0, 0};
    }
}
```





**Golang 代码实现**

```go
func twoSum(numbers []int, target int) []int {
    i := 0
    j := len(numbers) - 1

    for i < j {
        if numbers[i] + numbers[j] == target {
            return []int{i+1, j+1}
        } else if numbers[i] + numbers[j] > target {
            j--
        } else {
            i++
        }
    }

    return []int{0, 0}
}
```





