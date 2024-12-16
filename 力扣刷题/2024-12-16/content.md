# 「每日一题」力扣 283 移动零





## 题目描述

> 给定一个数组 `nums`，编写一个函数将所有 `0` 移动到数组的末尾，同时保持非零元素的相对顺序。
>
> **请注意** ，必须在不复制数组的情况下原地对数组进行操作。
>
> **示例 1:**
>
> ```
> 输入: nums = [0,1,0,3,12]
> 输出: [1,3,12,0,0]
> ```
>
> **示例 2:**
>
> ```
> 输入: nums = [0]
> 输出: [0]
> ```
>
> **提示**:
>
> - `1 <= nums.length <= 104`
> - `-231 <= nums[i] <= 231 - 1`
>
> **代码**:
>
> ```C++
> class Solution {
> public:
>     void moveZeroes(vector<int>& nums) {
>         
>     }
> };
> ```





## 方法一

**思路**

方法一和题目的要求不太符合，题目说了：在不复制数组的情况下原地完成，咱们先使用一个更简单的方法来实现

把所有的非零元素从 nums 里面拿出来放在 nonZeroNums 中，然后再把 nonZeroNums 中的元素放回 nums，nums 的其他元素赋值为 0

**代码实现**

```C++
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        vector<int> nonZeroNums;

        for( int i = 0 ; i < nums.size() ; i++ ) {
            if( nums[i] != 0 )
                nonZeroNums.push_back( nums[i] );
        }

        for( int i = 0 ; i < nonZeroNums.size() ; i++ ) {
            nums[i] = nonZeroNums[i];
        }

        for( int i = nonZeroNums.size() ; i < nums.size() ; i++ ) {
            nums[i] = 0;
        }
    }
};
```





## 方法二

**思路**

* 维护一个区间，我们规定 nums 数组的 `[0...r)` 表示的是非零元素的部分，在算法初始化的时候 r 的值等于 0，所以这样一个左闭右开的区间再算法一开始表达的是一个空区间的意思。

* 使用一个索引 i 从 0 开始遍历整个 nums 数组，如果 i 遇到的这个位置的元素是非零元素，那么就把这个元素放在 r 索引的位置，然后再让 r 索引向右移动一个位置，扩大非零元素的区间（因为我们向非零元素的区间添加了一个非零元素，当然就要扩大啦），你可以发现 r 这个索引指向的始终是下一次我们发现非零元素的时候要放的位置。
* 最后，我们全都遍历完了，我们就要把 nums 数组从 r 一直到最后的全部元素赋值为 0

**代码实现**

```C++
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        // [0...r) 是非零元素的区间
        // [0...0) 表示空区间

        int r = 0;
        for( int i = 0 ; i < nums.size() ; i++ ) {
            if( nums[i] != 0 ) {
                nums[r++] = nums[i];
            }
        }

        for( int i = r ; i < nums.size() ; i++ ) {
            nums[i] = 0;
        }
    }
};
```





## 方法三

**思路**

* 在方法二中你可能会发现，最后赋值 0 的过程有些多余，所以我们还可以改一下，写成方法三的样子，我们直接在遍历非零元素的时候就把 0 给赋值上去，要注意 r 和 i 如果指向的是同一个元素的话，我们是不能赋值为 0 的，不然我们就把非零元素给覆盖掉了

**代码实现**

```C++
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        // [0...r) 是非零元素的区间
        // [0...0) 表示空区间

        int r = 0;
        for( int i = 0 ; i < nums.size() ; i++ ) {
            if( nums[i] != 0 ) {
                nums[r] = nums[i];
                if( r != i) {
                    nums[i] = 0;
                }
                r++;
            }
        }
    }
};
```

