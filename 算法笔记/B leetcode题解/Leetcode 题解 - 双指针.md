#### [167. 两数之和 II - 输入有序数组](https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/)

> 给定一个已按照 `升序排列`  的整数数组 numbers ，请你从数组中找出两个数满足相加之和等于目标数 target 。
>
> 函数应该以长度为 2 的整数数组的形式返回这两个数的下标值。numbers 的下标 从 1 开始计数 ，所以答案数组应当满足 1 <= answer[0] < answer[1] <= numbers.length 。
>
> 你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
>
> Input: numbers={2, 7, 11, 15}, target=9
> Output: index1=1, index2=2

使用双指针，一个指针指向值较小的元素，一个指针指向值较大的元素。指向较小元素的指针从头向尾遍历，指向较大元素的指针从尾向头遍历。

- 如果两个指针指向元素的和 sum == target，那么得到要求的结果；
- 如果 sum > target，移动较大的元素，使 sum 变小一些；
- 如果 sum < target，移动较小的元素，使 sum 变大一些。

数组中的元素最多遍历一次，时间复杂度为 O(N)。只使用了两个额外变量，空间复杂度为 O(1)。

```java
public class Solution {
	public int[] twoSum(int[] nums, int target) {
        if (nums == null) {
            return null;
        }
        int small = 0;
        int large = nums.length - 1;
        while (small < fast) {
            int sum = nums[small] + nums[large];
            if (sum == target) {
                return new int[] {small + 1, large + 1}; //题目要求返回下标加一
            } else if (sum < target) {
                small++;
            } else {
                large--;
            }
        }
        return null;
    }
}
```

#### [633. 平方数之和](https://leetcode-cn.com/problems/sum-of-square-numbers/)

>给定一个非负整数 `c` ，你要判断是否存在两个整数 `a` 和 `b`，使得 `a2 + b2 = c` 。

可以看成是在元素为 `0~target `的有序数组中查找两个数，使得这两个数的平方和为 target，如果能找到，则返回 true，表示 target 是两个整数的平方和。

本题的关键是右指针的初始化，实现剪枝，从而降低时间复杂度。设右指针为 x，左指针固定为 0，为了使 02 + x2 的值尽可能接近 target，我们可以将 x 取为` sqrt(target)`。

因为最多只需要遍历一次 0~sqrt(target)，所以`时间复杂度为 O(sqrt(target))`。又因为只使用了两个额外的变量，因此空间复杂度为 `O(1)`。

```java
class Solution {
    public boolean judgeSquareSum(int c) {
        if (c == 0) {
            return true;
        }
        int small = 0;
        int large = (int)Math.sqrt(c);
        while(small <= large) {
            int powSum = small * small + large * large;
            if (powSum == c) {
                return true;
            } else if (powSum < c) {
                small++;
            } else {
                large--;
            }
        }
        return false;
    }
}
```

#### [345. 反转字符串中的元音字母](https://leetcode-cn.com/problems/reverse-vowels-of-a-string/)

> 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

使用双指针，一个指针从头向尾遍历，一个指针从尾到头遍历，当两个指针都遍历到元音字符时，交换这两个元音字符。

为了快速判断一个字符是不是元音字符，我们将全部元音字符添加到集合 HashSet 中，从而以 O(1) 的时间复杂度进行该操作。

- 时间复杂度为 O(N)：只需要遍历所有元素一次
- 空间复杂度 O(1)：只需要使用两个额外变量

```java
private final static HashSet<Character> vowels = new HashSet<>(
        Arrays.asList('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'));

public String reverseVowels(String s) {
    if (s == null) return null;
    int i = 0, j = s.length() - 1;
    char[] result = new char[s.length()];
    while (i <= j) {
        char ci = s.charAt(i);
        char cj = s.charAt(j);
        if (!vowels.contains(ci)) {
            result[i++] = ci;
        } else if (!vowels.contains(cj)) {
            result[j--] = cj;
        } else {
            result[i++] = cj;
            result[j--] = ci;
        }
    }
    return new String(result);
}

```



#### [680. 验证回文字符串 Ⅱ](https://leetcode-cn.com/problems/valid-palindrome-ii/)

>给定一个非空字符串 `s`，**最多**删除一个字符。判断是否能成为回文字符串。

使用双指针可以很容易判断一个字符串是否是回文字符串：令一个指针从左到右遍历，一个指针从右到左遍历，这两个指针同时移动一个位置，每次都判断两个指针指向的字符是否相同，如果都相同，字符串才是具有左右对称性质的回文字符串。在试着删除字符时，我们既可以删除左指针指向的字符，也可以删除右指针指向的字符。

```java
class Solution {
    public boolean validPalindrome(String s) {
        for (int i = 0,j = s.length() - 1; i < j; i++, j--) {
            if (s.charAt(i) != s.charAt(j)) { //只判断中间不是回文的部分
                return isPalindrome(s, i, j - 1) || isPalindrome(s, i + 1, j);
            }
        }
        return true;
    }
    private boolean isPalindrome(String s, int i, int j) {
        while (i < j) {
            if (s.charAt(i++) != s.charAt(j--)) {
                return false;
            }
        }
        return true;
    }
}
```

#### [88. 合并两个有序数组](https://leetcode-cn.com/problems/merge-sorted-array/)

>给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
>
>初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。你可以假设 nums1 的空间大小等于 m + n，这样它就有足够的空间保存来自 nums2 的元素。
>

==需要从尾开始遍历==

```java
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int index1 = m - 1;
        int index2 = n - 1;
        int mergeIndex = m + n - 1;//依然在nums1后面
        while(index2 >= 0) {
            if (index1 < 0) {
                nums1[mergeIndex--] = nums2[index2--];
            } else if (nums1[index1] > nums2[index2]) {
                nums1[mergeIndex--] = nums1[index1--];
            } else {
                 nums1[mergeIndex--] = nums2[index2--];
            }
        }
    }
}
```

#### [141. 环形链表](https://leetcode-cn.com/problems/linked-list-cycle/)

```java
public class Solution {
   public boolean hasCycle(ListNode head) {
        if (head == null || head.next == null) {
            return false;
        }
        ListNode slow = head;
        ListNode fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {
                return true;
            }
        }
        return false;
    }
}
```

#### [524. 通过删除字母匹配到字典里最长单词](https://leetcode-cn.com/problems/longest-word-in-dictionary-through-deleting/)

>给你一个字符串 s 和一个字符串数组 dictionary 作为字典，找出并返回字典中**最长的字符串**，该字符串可以通过删除 s 中的某些字符得到。
>
>如果答案不止一个，**返回长度最长且字典序最小**的字符串。如果答案不存在，则返回空字符串。
>
>>Input:
>>s = "abpcplea", d = ["ale","apple","monkey","plea"]
>>
>>Output:
>>"apple"

通过删除字符串 s 中的一个字符能得到字符串 t，可以认为 t 是 s 的子序列，我们可以使用双指针来判断一个字符串是否为另一个字符串的子序列。

s = "abpcplea", d = ["ale","apple","monkey","plea"] 中ale, apple, plea都是s的substring但是我们取apple 

abpcplea			apple

​             i                           j



**字典序比较**

`longestWord.compareTo(target) < 0`

```java
public String findLongestWord(String s, List<String> d) {
    String longestWord = ""; //c
    for (String target : d) { //target代表字典中的每一个单词
        int l1 = longestWord.length(), l2 = target.length();
        if (l1 > l2 || (l1 == l2 && longestWord.compareTo(target) < 0)) { //满足较长 || 满足同长条件字母序小continue查找
            continue;
        }
        if (isSubstr(s, target)) { 
            longestWord = target;
        }
    }
    return longestWord;
}

//eg. s = abpcplea target = apple 可以看出target是s的substring
private boolean isSubstr(String s, String target) { //substring都用这个方法, 字典条件j++, 待匹配一直i++ 
    int i = 0, j = 0;
    while (i < s.length() && j < target.length()) {
        if (s.charAt(i) == target.charAt(j)) {
            j++; //满足条件才j++
        }
        i++;
    }
    return j == target.length();
}

```



