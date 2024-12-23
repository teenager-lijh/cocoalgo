# 「每日一题」力扣 88 合并两个有序数组

你好啊，我是蓝莓，今天是每日一题的第 6 天。

**题目清单**：https://blueberry-universe.cn/lc/index.html

**引用力扣题目**：https://leetcode.cn/problems/merge-sorted-array/





## 题目描述

给你两个按 **非递减顺序** 排列的整数数组 `nums1` 和 `nums2`，另有两个整数 `m` 和 `n` ，分别表示 `nums1` 和 `nums2` 中的元素数目。

请你 **合并** `nums2` 到 `nums1` 中，使合并后的数组同样按 **非递减顺序** 排列。

**注意：**最终，合并后数组不应由函数返回，而是存储在数组 `nums1` 中。为了应对这种情况，`nums1` 的初始长度为 `m + n`，其中前 `m` 个元素表示应合并的元素，后 `n` 个元素为 `0` ，应忽略。`nums2` 的长度为 `n` 。

 

**示例 1：**

```
输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]
解释：需要合并 [1,2,3] 和 [2,5,6] 。
合并结果是 [1,2,2,3,5,6] ，其中斜体加粗标注的为 nums1 中的元素。
```

**示例 2：**

```
输入：nums1 = [1], m = 1, nums2 = [], n = 0
输出：[1]
解释：需要合并 [1] 和 [] 。
合并结果是 [1] 。
```

**示例 3：**

```
输入：nums1 = [0], m = 0, nums2 = [1], n = 1
输出：[1]
解释：需要合并的数组是 [] 和 [1] 。
合并结果是 [1] 。
注意，因为 m = 0 ，所以 nums1 中没有元素。nums1 中仅存的 0 仅仅是为了确保合并结果可以顺利存放到 nums1 中。
```

 

**提示：**

- `nums1.length == m + n`
- `nums2.length == n`
- `0 <= m, n <= 200`
- `1 <= m + n <= 200`
- `-109 <= nums1[i], nums2[j] <= 109`

 

**进阶：**你可以设计实现一个时间复杂度为 `O(m + n)` 的算法解决此问题吗？





## 实现

**思路**

- 这个题目是将两个有序的数组合并成一个数组，所以我们直接采用归并排序的思路即可
- 归并排序中的 `merge` 操作做了什么 ？
- 在归并排序中，通常情况下对两个有序的数组进行归并，我们分别使用 `i` 和 `j` 两个索引指向两个数组的开头元素。然后每次选择 `i` 和 `j` 索引指向的较小的元素依次放在最终的结果中。比如我们选择了 `i` 索引所指向的元素，那么我们就让 `i` 索引向右移动一个位置，继续重复刚才的过程即可。
- 需要注意的是，由于是对两个数组进行归并，非常有可能其中一个数组的元素已经遍历完了，但是另一个数组的元素还没有遍历完，所以剩下的另一个数组的元素就直接无脑的依次堆叠在最终的结果中即可。
- 因为题目要求的是我们把最后归并完成的结果放在 `nums1` 数组中，所以在代码实现的最后需要把我们的结果复制进去。
- 在执行归并的过程中，我们使用 `i` 索引遍历 `nums1` 数组；`i` 的初始值为 0，并且小于数组长度 m
- 我们使用 `j` 索引遍历 `nums2` 数组，`j` 的初始值为 0，并且小于数组长度 n
- 定义一个 `res` 数组用来存放最后的结果，它的长度为 `nums1` 的长度 加上 `nums2` 的长度，也就是 `m+n`
- 使用 `cur` 索引遍历 `res` 数组，`res` 的初始值为 0
- 代码中需要注意的一个点是：在归并的时候，我们需要先判断是不是有一个数组已经遍历完了？如果都没有遍历完，我们才能比较大小，一旦有一个数组遍历完了，那么执行比较大小的操作就会越界，所以在 `while` 循环中我把比较大小的那一步放在了后面，而把判断数组遍历是否结束的步骤放在了前面。





**Python 代码实现**

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0

        res = []

        while i < m or j < n:
            if i >= m:
                # nums1 数组已经全部遍历结束 && nums2 数组还没有结束
                res.append(nums2[j])
                j += 1
            elif j >= n:
                # nums2 数组已经全部遍历结束 && nums1 数组还没有结束
                res.append(nums1[i])
                i += 1
            elif nums1[i] < nums2[j]:
                # nums1[i] 的元素较小 选择 nums1[i]
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1

        nums1[:] = res[:]
```





**C++ 代码实现**

```c++
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int i = 0;
        int j = 0;
        
        int cur = 0;
        vector<int> res(m+n, 0);

        while( i < m || j < n ) {
            if( i >= m ) {
                // nums1 数组已经全部遍历结束 && nums2 数组还没有结束
                res[cur++] = nums2[j++];
            } else if( j >= n ) {
                // nums2 数组已经全部遍历结束 && nums1 数组还没有结束
                res[cur++] = nums1[i++];
            } else if( nums1[i] < nums2[j]) {
                // nums1[i] 的元素较小 选择 nums1[i] 
                res[cur++] = nums1[i++];
            } else {
                // nums1[i] > nums2[j]
                res[cur++] = nums2[j++];
            }
        }

        cur = 0;
        while( cur < nums1.size() ) {
            nums1[cur] = res[cur];
            cur++;
        }
    }
};
```





**Java 代码实现**

```java
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i = 0;
        int j = 0;
        
        int cur = 0;
        int[] res = new int[m+n];

        while( i < m || j < n ) {
            if( i >= m ) {
                // nums1 数组已经全部遍历结束 && nums2 数组还没有结束
                res[cur++] = nums2[j++];
            } else if( j >= n ) {
                // nums2 数组已经全部遍历结束 && nums1 数组还没有结束
                res[cur++] = nums1[i++];
            } else if( nums1[i] < nums2[j]) {
                // nums1[i] 的元素较小 选择 nums1[i] 
                res[cur++] = nums1[i++];
            } else {
                // nums1[i] > nums2[j]
                res[cur++] = nums2[j++];
            }
        }

        cur = 0;
        while( cur < nums1.length ) {
            nums1[cur] = res[cur];
            cur++;
        }
    }
}
```





**Golang 代码**

```go
func merge(nums1 []int, m int, nums2 []int, n int)  {
    i := 0;
    j := 0;

    cur := 0;
    res := make([]int, m+n);

    for i < m || j < n {
        if i >= m  {
            // nums1 数组已经全部遍历结束 && nums2 数组还没有结束
            res[cur] = nums2[j];
            j++;
        } else if j >= n {
            // nums2 数组已经全部遍历结束 && nums1 数组还没有结束
            res[cur] = nums1[i];
            i++;
        } else if nums1[i] < nums2[j] {
            // nums1[i] 的元素较小 选择 nums1[i] 
            res[cur] = nums1[i];
            i++;
        } else {
            // nums1[i] > nums2[j]
            res[cur] = nums2[j];
            j++;
        }

        cur++;
    }

    copy(nums1, res);
}
```

