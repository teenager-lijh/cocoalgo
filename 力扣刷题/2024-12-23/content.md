# 「每日一题」力扣 215 数组中的第k个最大的元素

你好啊，我是蓝莓，今天是每日一题的第 7 天。

**题目清单**：https://blueberry-universe.cn/lc/index.html

**引用力扣题目**：https://leetcode.cn/problems/kth-largest-element-in-an-array/description/





## 题目描述

给定整数数组 `nums` 和整数 `k`，请返回数组中第 `**k**` 个最大的元素。

请注意，你需要找的是数组排序后的第 `k` 个最大的元素，而不是第 `k` 个不同的元素。

你必须设计并实现时间复杂度为 `O(n)` 的算法解决此问题。

 

**示例 1:**

```
输入: [3,2,1,5,6,4], k = 2
输出: 5
```

**示例 2:**

```
输入: [3,2,3,1,2,4,5,5,6], k = 4
输出: 4
```

 

**提示：**

- `1 <= k <= nums.length <= 105`
- `-104 <= nums[i] <= 104`





## 实现

**思路**

- 最简单的思路应该是将整个 `nums` 数组进行排序，然后计算出第 k 大的元素所在的位置，就可以求解出结果了
- 另一种思路，我们可以使用 `快速排序` + `分治` 的方法实现
- 回忆快速排序中 `partition` 的操作需要传入一个 `nums` 数组以及一个数值 `v` ，我们会根据 `v` 的值将所有小于它的放在左边，大于它的放在右边，等于`v` 的值放在中间。也就是说中间的这部分值是已经完成排序的，如果中间这部分的某个元素的小标刚好就是我们要找的第 k 大的元素的下标，那么算法就已经结束了
- 如果我们要找的元素的下标在中间这部分元素的右侧，那么我们只需要对右侧的部分再继续使用 `partition` 操作即可，接着只需要重复上面的过程
- 如果我们要找的元素的下标在中间这部分元素的左侧，那么我们只需要对左侧的这部分元素再继续使用 `partition` 操作即可，接着继续重复上述操作
- 如果我们一旦找到了指定元素就直接返回就可以了
- 这里的 `partition` 操作的过程可参考这篇文章 [「每日一题」力扣 75 颜色分类](https://mp.weixin.qq.com/s/rTfC5UCxsZ7HomMGDUx6TA) ，我只是在 `partition` 操作返回的时候，返回了中间那部分的区间，其他的都是一模一样的抄了过来





**Python 代码实现**

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        l = 0
        r = len(nums) - 1
        # 第 k 大的元素所在 nums 数组中的位置 (按照从小到大的顺序摆放)
        p = len(nums) - k

        while l <= r:
            pivot = random.choice(nums[l:r+1])  # 在 nums 中随机选取一个数值
            first, second = self.partition(nums, pivot, l, r)
            if first <= p and second >= p:
                # 如果 p 落在 interval 表示的中间部分的区间里
                # 说明第 k 大的元素已经被放在了正确的位置
                return nums[p]
            elif first > p:
                # 说明应该在左边继续寻找
                r = first - 1
            else:
                # interval.second < p
                # 说明应该在右边继续寻找
                l = second + 1

    def partition(self, nums: List[int], v: int, l: int, r: int) -> Tuple:
        i = l
        j = l
        k = r

        while j <= k:
            if nums[j] < v:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[j] > v:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1
            else:
                j += 1

        # 返回区别 nums[i, j-1] 代表等于数值 v 的区间
        return i, j-1
```





**C++ 代码实现**

```c++
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        int l = 0;
        int r = nums.size() - 1;
        // 第 k 大的元素所在 nums 数组中的位置 (按照从小到大的顺序摆放)
        int p = nums.size() - k;

        srand(time(nullptr)); // 使用当前时间初始化随机种子

        while( l <= r ) {
            int select = l + rand() % (r - l + 1); // 生成 [l, r] 的随机整数
            pair<int, int> interval = partition(nums, nums[select], l, r);
            if( interval.first <= p && interval.second >= p ) {
                // 如果 p 落在 interval 表示的中间部分的区间里
                // 说明第 k 大的元素已经被放在了正确的位置
                return nums[p];
            } else if( interval.first > p ) {
                // 说明应该在左边继续寻找
                r = interval.first - 1;
            } else {
                // interval.second < p
                // 说明应该在右边继续寻找
                l = interval.second + 1;
            }
        }

        return -1;
    }

    pair<int, int> partition(vector<int>& nums, int v, int l, int r) {
        // 维护 nums[l...i) 为小于 v 的数值所在区间
        // 维护 nums[l...j) 为等于 v 的数值所在区间
        // 维护 nums(k...r] 为大于 v 的数值所在区间

        int i = l;
        int j = l;
        int k = r;

        while( j <= k ) {
            if( nums[j] < v ) {
                // 从 nums[i...j) 区间中 为 nums[0...i) 区间让出一个位置
                swap(nums[i++], nums[j++]);
            } else if( nums[j] > v ) {
                // nums[cur] > v
                swap(nums[k--], nums[j]);
            } else {
                j++;
            }
        }

        // 返回区别 nums[i, j-1] 代表等于数值 v 的区间
        return make_pair(i, j-1);
    }
};
```





**Java 代码实现**

```java
class Solution {
    public int findKthLargest(int[] nums, int k) {
        int l = 0;
        int r = nums.length - 1;
        // 第 k 大的元素所在 nums 数组中的位置 (按照从小到大的顺序摆放)
        int p = nums.length - k;

        Random random = new Random();

        while( l <= r ) {
            int select = random.nextInt(r - l + 1) + l; // 生成 [l, r] 的随机整数
            int[] interval = partition(nums, nums[select], l, r);
            if( interval[0] <= p && interval[1] >= p ) {
                // 如果 p 落在 interval 表示的中间部分的区间里
                // 说明第 k 大的元素已经被放在了正确的位置
                return nums[p];
            } else if( interval[0] > p ) {
                // 说明应该在左边继续寻找
                r = interval[0] - 1;
            } else {
                // interval[1] < p
                // 说明应该在右边继续寻找
                l = interval[1] + 1;
            }
        }

        return -1;
    }

     public int[] partition(int[] nums, int v, int l, int r) {
        int i = l;
        int j = l;
        int k = r;

        while( j <= k ) {
            if( nums[j] < v ) {
                int temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
                i++;
                j++;
            } else if( nums[j] > v ) {
                int temp = nums[j];
                nums[j] = nums[k];
                nums[k] = temp;
                k--;
            } else {
                j++;
            }
        }
         
		// 返回区别 nums[i, j-1] 代表等于数值 v 的区间
        return new int[]{i, j-1};
    }
}
```





**Golang 代码实现**

```go
func findKthLargest(nums []int, k int) int {
	l := 0
	r := len(nums) - 1
	// 第 k 大的元素所在 nums 数组中的位置 (按照从小到大的顺序摆放)
	p := len(nums) - k

	rand.Seed(time.Now().UnixNano()) // 使用当前时间初始化随机种子

	for l <= r {
		selectIndex := rand.Intn(r-l+1) + l // 生成 [l, r] 的随机整数
		first, second := partition(nums, nums[selectIndex], l, r)
		if first <= p && second >= p {
			// 如果 p 落在 [first, second] 区间内
			// 说明第 k 大的元素已经被放在了正确的位置
			return nums[p]
		} else if first > p {
			// 说明应该在左边继续寻找
			r = first - 1
		} else {
			// second < p
			// 说明应该在右边继续寻找
			l = second + 1
		}
	}

	return -1
}

// partition 函数，将 nums[l:r] 数组划分为小于、等于和大于基准值的部分
func partition(nums []int, v, l, r int) (int, int) {
	i := l
	j := l
	k := r

	for j <= k {
		if nums[j] < v {
			nums[i], nums[j] = nums[j], nums[i]
			i++
			j++
		} else if nums[j] > v {
			nums[j], nums[k] = nums[k], nums[j]
			k--
		} else {
			j++
		}
	}

	// 返回 [i, j-1]，即等于数值 v 的区间
	return i, j - 1
}
```

