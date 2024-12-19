# 「每日一题」力扣 80 删除有序数组中的重复项 II

你好啊，我是蓝莓，今天是每日一题的第 4 天。

**题目清单**：https://blueberry-universe.cn/lc/index.html

**引用力扣题目**：https://leetcode.cn/problems/remove-duplicates-from-sorted-array-ii/description/





## 题目描述

给你一个有序数组 `nums` ，请你**[ 原地](http://baike.baidu.com/item/原地算法)** 删除重复出现的元素，使得出现次数超过两次的元素**只出现两次** ，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 **[原地 ](https://baike.baidu.com/item/原地算法)修改输入数组** 并在使用 O(1) 额外空间的条件下完成。

 

**说明：**

为什么返回数值是整数，但输出的答案是数组呢？

请注意，输入数组是以**「引用」**方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

你可以想象内部操作如下:

```
// nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
int len = removeDuplicates(nums);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中 该长度范围内 的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
```

 

**示例 1：**

```
输入：nums = [1,1,1,2,2,3]
输出：5, nums = [1,1,2,2,3]
解释：函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3。 不需要考虑数组中超出新长度后面的元素。
```

**示例 2：**

```
输入：nums = [0,0,1,1,1,1,2,3,3]
输出：7, nums = [0,0,1,1,2,3,3]
解释：函数应返回新长度 length = 7, 并且原数组的前七个元素被修改为 0, 0, 1, 1, 2, 3, 3。不需要考虑数组中超出新长度后面的元素。
```

 

**提示：**

- `1 <= nums.length <= 3 * 104`
- `-104 <= nums[i] <= 104`
- `nums` 已按升序排列





## 实现

**思路**

这个题目和以下三个题目的思路是差不多的，链接如下：

[**「每日一题」力扣 283 移动零**](https://mp.weixin.qq.com/s/6dayzKs2SNl0-nHz9pyP6g)

[**「每日一题」力扣 27 移动元素**](https://mp.weixin.qq.com/s/BjGwnxNO1I_NVJpM_86ZYQ)

[**「每日一题」力扣 26 删除有序数组中的重复项**](https://mp.weixin.qq.com/s/qI9AiL30bZzI0DWuF2meTQ)

-  `nums[0...k)` 区间为这个题目的结果，这个区间中允许每个数值最多出现 2 次，超过 2 次的是不会出现在这个区间中的
- k` 的初始值依然为 0，这代表在算法开始之前，`nums[0...k)`  这个区间是一个空区间
- 用索引 `i` 遍历 `nums` 数组，每当我们发现一个数值实在 `nums[0...k)` 区间中出现的次数不超过 2 次的，我们就把这个元素纳入到 `nums[0...k)` 区间中
-最后一个问题就是：我们如何判断当前遍历到的元素 `nums[i]` 在当前的区间 `nums[0...k)` 中出现的次数是小于 2 次的 ？ 因为题目给出的数组 `nums` 的元素是按照从小到大的顺序排序好的，所以如果是连续出现的数值，必然被我们纳入到 `nums[0...k)` 区间中也是连续的，所以我们可以直接判断：是不是 `nums[k-2] != nums[i]`。如果 是不是 `nums[k-2] != nums[i]` 是成立的，那么我们就可以把当前这个元素纳入到 `nums[0...k)` 区间中了。`nums[k-2]` 代表的就是这个区间中的倒数第二个元素，当我们发现 `nums[i]` 和倒数第一个元素相等是没关系的，因为在我们维护的区间中每个元素最多可以出现两次，可是一旦这个元素和倒数第二个元素相等，那就不行了。
- 越界处理：由于当 `k == 0` 或者 `k == 1` 的时候 `nums[k-2]` 的访问是越界的，然而这个题目又允许每个元素最多可以出现两次，所以当当 `k == 0` 或者 `k == 1` 的时候直接无脑将 `nums[i]` 纳入到我们维护的区间即可。





**Python 代码实现**

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 维护 nums[0...k) 区间为出现小于等于 2 次的元素
        k = 0

        for i in range(len(nums)):
            # 只要 nums[i] 不等于 nums[0...k) 区间中的倒数第2个元素即可
            if k == 0 or k == 1 or nums[i] != nums[k-2]:
                nums[k] = nums[i]
                k += 1

        return k
```





**C++ 代码实现**

```c++
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        // 维护 nums[0...k) 区间为出现小于等于 2 次的元素
        int k = 0;

        for( int i = 0 ; i < nums.size() ; i++ ) {
            // 只要 nums[i] 不等于 nums[0...k) 区间中的倒数第2个元素即可
            if( k == 0 || k == 1 || nums[i] != nums[k-2]) {
                nums[k++] = nums[i];
            }
        }

        return k;
    }
};
```





**Java 代码实现**

```java
class Solution {
    public int removeDuplicates(int[] nums) {
        // 维护 nums[0...k) 区间为出现小于等于 2 次的元素
        int k = 0;

        for( int i = 0 ; i < nums.length ; i++ ) {
            // 只要 nums[i] 不等于 nums[0...k) 区间中的倒数第2个元素即可
            if( k == 0 || k == 1 || nums[i] != nums[k-2] ) {
                nums[k++] = nums[i];
            }
        }

        return k;
    }
}
```





**Golang 代码实现**

```go
func removeDuplicates(nums []int) int {
    // 维护 nums[0...k) 区间为出现小于等于 2 次的元素
    k := 0

    for i := 0 ; i < len(nums) ; i++ {
        // 只要 nums[i] 不等于 nums[0...k) 区间中的倒数第2个元素即可
        if k == 0 || k == 1 || nums[i] != nums[k-2] {
            nums[k] = nums[i]
            k += 1
        }
    }

    return k;
}
```



