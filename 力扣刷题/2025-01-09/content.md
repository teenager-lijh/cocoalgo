# 「每日一题」力扣 350 两个数组的交集 II

你好啊，我是蓝莓，今天是每日一题的第 19 天。

**题目清单**：[一起刷力扣](https://blueberry-universe.cn/lc/index.html)

**引用力扣题目**：[350 两个数组的交集 II](https://leetcode.cn/problems/intersection-of-two-arrays-ii/description/)





## 题目描述

给你两个整数数组 `nums1` 和 `nums2` ，请你以数组形式返回两数组的交集。返回结果中每个元素出现的次数，应与元素在两个数组中都出现的次数一致（如果出现次数不一致，则考虑取较小值）。可以不考虑输出结果的顺序。

 

**示例 1：**

```
输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]
```

**示例 2:**

```
输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[4,9]
```

 

**提示：**

- `1 <= nums1.length, nums2.length <= 1000`
- `0 <= nums1[i], nums2[i] <= 1000`

 

***\*进阶\**：**

- 如果给定的数组已经排好序呢？你将如何优化你的算法？
- 如果 `nums1` 的大小比 `nums2` 小，哪种方法更优？
- 如果 `nums2` 的元素存储在磁盘上，内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？





## 实现

**方法 1 思路**

- 这是一个评分为简单的题目。
- 最简单的方法，我们使用分别使用 `map1`  和 `map2` 来统计 `nums1` 和 `nums1` 中每个数值出现的次数
- 然后，遍历 `map1` 或者 `map2` 任意一个都是可以的，我们需要找到既存在 `map1` 中也存在 `map2` 中的 `key`，然后向结果中添加两者出现的 `key` 的次数较小的那个作为添加的次数即可
- 这个题目其实主要是让我们熟悉使用 `map` 这种数据结构；在 `C++` 的代码中，如果 `map[key]` 这个元素不存在的话，那么就会自动在数据结构中添加键为 `key` 并且初始值为 `0` 的值 （这是对于 key 和 value 都是 int 类型而言的），所以我的代码才写成了这样

**C++ 代码实现**

```c++
class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int, int> map1;
        unordered_map<int, int> map2;
        vector<int> res;

        for( int i = 0 ; i < nums1.size() ; i++ ) {
            map1[nums1[i]]++;
        }

        for( int i = 0 ; i < nums2.size() ; i++ ) {
            map2[nums2[i]]++;
        }

        // 遍历 map1
        for( auto iter = map1.begin() ; iter != map1.end() ; iter++ ) {
            int key = iter->first;
            int value = iter->second;

            if( map2.find(key) != map2.end() ) {
                int sz = min(value, map2[key]);
                for( int k = 0 ; k < sz ; k++ ) {
                    res.push_back( key );
                }
            }
        }

        return res;
    }
};
```





**方法 2 思路**

- 我们也可以只统计 `nums1` 数组中每个元素出现的次数
- 然后我们遍历 `nums2` 数组就可以了，每当我们遍历到一项的时候，我们就去 `map` 数据结构中找一找，看看 `nums1` 中存不存在这个数？如果存在的话我们就把这个数添加到结果中去
- 但是，这里要注意了，比如 `10` 这个数在 `nums1` 中出现了 20 次，但是在 `nums2` 中出现了 `30` 次，那么我们就会在 `nums2` 中遍历到 `30` 次这个数了。这样就会在结果中添加 `30` 次，显然不符合题意。
- 所以，我们每次添加完成一个数的时候，我们就把 `map` 中的计数减少 1，只有我们查找到的这个数在 `nums1` 的 `map` 剩余的次数大于 0 的时候，我们才把这个数纳入结果中去

```c++
class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        // 时间复杂度 : O(1)
        unordered_map<int, int> record;

        for( int i = 0 ; i < nums1.size(); i++ ) {
            if( record.find(nums1[i]) == record.end() ) {
                record.insert( make_pair(nums1[i], 1) );
            } else {
                record[nums1[i]] ++;
            }
        }

        vector<int> res;

        for( int i = 0 ; i < nums2.size() ; i++ ) {
            if( record.find( nums2[i] ) != record.end() && record[nums2[i]] > 0 ) {
                record[nums2[i]] --;
                res.push_back( nums2[i] );
                if( record[nums2[i]] == 0 ) {
                    record.erase( nums2[i] );
                }
            }
        }

        return res;
    }
};
```

