# Leetcode 题解 - 二分查找

**正常实现**

```
Input : [1,2,3,4,5]
key : 3
return the index : 2
```

```java
public class Solution {
    public int binarySearch(int[] array, int target) {
        if (array == null || array.length == 0) {
            return -1;
        }
        int left = 0;
        int right = array.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (array[mid] == target) {
                return mid;
            } else if (array[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return -1;
    }
}
```

**变种**

二分查找可以有很多变种，实现变种要注意边界值的判断。例如在一个有重复元素的数组中查找 key 的最左位置的实现如下：

```
public int binarySearch(int[] nums, int key) {
    int l = 0, h = nums.length;
    while (l < h) {
        int m = l + (h - l) / 2;
        if (nums[m] >= key) {
            h = m;
        } else {
            l = m + 1;
        }
    }
    return l;
}

```

#### [69. x 的平方根](https://leetcode-cn.com/problems/sqrtx/)

>实现 int sqrt(int x) 函数。
>
>计算并返回 x 的平方根，其中 x 是非负整数。
>
>由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

```
输入: 8
输出: 2
说明: 8 的平方根是 2.82842..., 
     由于返回类型是整数，小数部分将被舍去。
```

一个数 x 的开方 sqrt 一定在 0 ~ x 之间，并且满足 sqrt == x / sqrt。可以利用二分查找在 0 ~ x 之间查找 sqrt。

对于 x = 8，它的开方是 2.82842...，最后应该返回 2 而不是 3。在循环条件为 l <= h 并且循环退出时，h 总是比 l 小 1，也就是说 h = 2，因此最后的返回值应该为 h 而不是 l。

```java
class Solution {
    public int mySqrt(int x) {
        if (x <= 1) {
            return x;
        }
        int left = 1, right = x;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            int sqrt = x / mid;
            if (sqrt == mid) {
                return mid;
            } else if (mid > sqrt) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return right;
    }
}
```

#### [744. 寻找比目标字母大的最小字母](https://leetcode-cn.com/problems/find-smallest-letter-greater-than-target/)

>给你一个排序后的字符列表 letters ，列表中只包含小写英文字母。另给出一个目标字母 target，请你寻找在这一有序列表里比目标字母大的最小字母。
>
>在比较时，字母是依序循环出现的。举个例子：
>
>如果目标字母 target = 'z' 并且字符列表为 letters = ['a', 'b']，则答案返回 'a' (没有出现的情况就直接返回第一个字母)

`letters[m] <= target` 字母顺序可以直接比较大小

```java
class Solution {
    public char nextGreatestLetter(char[] letters, char target) {
       int n = letters.length;
       int l = 0;
       int h = n - 1;
       while (l <= h) {
           int m = l + (h - l) / 2;
           if (letters[m] <= target) {
               l = m + 1;
           } else {
               h = m - 1;
           }
       }
       return l < n ? letters[l] : letters[0];
    }
}
```

#### [540. 有序数组中的单一元素](https://leetcode-cn.com/problems/single-element-in-a-sorted-array/)

给定一个只包含整数的有序数组，每个元素都会出现两次，唯有一个数只会出现一次，找出这个数。

```
输入: [1,1,2,3,3,4,4,8,8]
输出: 2
```
令 index 为 Single Element 在数组中的位置。在 index 之后，数组中原来存在的成对状态被改变。如果 m 为偶数，并且 m + 1 < index，那么 nums[m] == nums[m + 1]；m + 1 >= index，那么 nums[m] != nums[m + 1]。

从上面的规律可以知道，如果 nums[m] == nums[m + 1]，那么 index 所在的数组位置为 [m + 2, h]，此时令 l = m + 2；如果 nums[m] != nums[m + 1]，那么 index 所在的数组位置为 [l, m]，此时令 h = m。

因为 h 的赋值表达式为 h = m，那么循环条件也就只能使用 l < h 这种形式。

1,1,2,3,3             1,1,2,3,3,4,4 

l            h		     l    m          h

​      m

```java
public int singleNonDuplicate(int[] nums) {
    int l = 0, h = nums.length - 1;
    while (l < h) {
        int m = l + (h - l) / 2;
        if (m % 2 == 1) { //mid下标奇数就左移一格
            m--;   // 保证 l/h/m 都在偶数位，使得查找区间大小一直都是奇数
        }
        if (nums[m] == nums[m + 1]) { //nums[m] == nums[m + 1]，m是双字的前一位
            l = m + 2;//mid之后出现单个元素
        } else {//mid之前出现了单个元素
            h = m;
        }
    }
    return nums[l];
}

```

#### [278. 第一个错误的版本](https://leetcode-cn.com/problems/first-bad-version/)

>假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。
>
>你可以通过调用 bool isBadVersion(version) 接口来判断版本号 version 是否在单元测试中出错。实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。
>

```
输入：n = 5, bad = 4 
1 2 3 4 5 
输出：4
解释：
调用 isBadVersion(3) -> false 
调用 isBadVersion(5) -> true 
调用 isBadVersion(4) -> true
所以，4 是第一个错误的版本。
```

```java
public int firstBadVersion(int n) {
    int l = 1, h = n;
    while (l < h) {
        int mid = l + (h - l) / 2;
        if (isBadVersion(mid)) {
            h = mid;
        } else {
            l = mid + 1;
        }
    }
    return l;
}
```

#### [153. 寻找旋转排序数组中的最小值](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/)

>已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。例如，原数组 nums = [0,1,2,4,5,6,7] 在变化后可能得到：
>若旋转 4 次，则可以得到 [4,5,6,7,0,1,2]
>若旋转 7 次，则可以得到 [0,1,2,4,5,6,7]
>
>```
>Input: [3,4,5,1,2],
>		l       h
>			m
>		      l h
>		      m
>		      
>		      lh
>		      m
>Output: 1
>```

```java
 public int findMin(int[] nums) {
            int l = 0, h = nums.length - 1;
            while (l < h) {
                int m = l + (h - l) / 2;
                if (nums[m] <= nums[h]) {
                    h = m; //保留最小值
                } else {
                    l = m + 1; //说明nums[m] > nums[h], 那么后面的mid后面的数字更小了，左边界到后面去
                }
            }
            return nums[l];
        }
```

#### [34. 在排序数组中查找元素的第一个和最后一个位置](https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

>给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
>
>如果数组中不存在目标值 target，返回 [-1, -1]。
>
>```
>输入：nums = [5,7,7,8,8,10], target = 8
>输出：[3,4]
>```

先定义`findFirst()`用于返回nums中第一个出现target元素的index，需要注意的是如果target元素比较大的时候，超出了nums中的最大元素我们返回的是nums.length。 这样做的原因是当我们找最后出现该元素last位置时候，我们巧妙的利用了`findFirst(nums, target + 1) - 1` 所以我们有可能找到数组外面去。

```java
class Solution {
        public int[] searchRange(int[] nums, int target) {
            // 5,7,7,8,8,10
            // l          r
            //       m
            int first = findFirst(nums, target);
            int last = findFirst(nums, target + 1) - 1;
            if (first == nums.length || nums[first] != target) {
                return new int[] {-1, -1};
            } else {
                return new int[] {first, Math.max(first, last)};
            }
        }

        private int findFirst(int[] nums, int target) {
            int left = 0;
            int right = nums.length;
            while (left < right) {
                int mid = left + (right - left) / 2;
                if (nums[mid] >= target) {
                    right = mid;
                } else {
                    left = mid + 1;
                }
            }
            return left;
        }
    }
```
