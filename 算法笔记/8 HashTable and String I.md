# HashTable and String I 8/23

![image-20210623094338566](8 HashTable and String I.assets/image-20210623094338566.png)

##  [Top K Frequent Words](https://app.laicode.io/app/problem/67?plan=3)

>    Given a composition with different kinds of words, return a list of the top K most frequent words in the composition.
>
> **Assumptions**
>
> - the composition is not null and is not guaranteed to be sorted
> - K >= 1 and K could be larger than the number of distinct words in the composition, in this case, just return all the distinct words
>
> **Return**
>
> - a list of words ordered from most frequent one to least frequent one (the list could be of size K or smaller than K)
>
> **Examples**
>
> - Composition = ["a", "a", "b", "b", "b", "b", "c", "c", "c", "d"], top 2 frequent words are [“b”, “c”]
> - Composition = ["a", "a", "b", "b", "b", "b", "c", "c", "c", "d"], top 4 frequent words are [“b”, “c”, "a", "d"]
> - Composition = ["a", "a", "b", "b", "b", "b", "c", "c", "c", "d"], top 5 frequent words are [“b”, “c”, "a", "d"]
>
> 按顺序返回top k个元素

==思路==：

1. Map<String, Integer> freqMap, 存放String出现的频率，写一个求频率的代码

2. 创建minHeap, 里面存放类型Map.Entry<String, Integer>

3. 遍历然后将大的值放入到minHeap当中

4. minHeap取出元素倒序存入结果string[]

5. **时间复杂度**，假设有m个单词，每一个但是都会做一个put 和 get.

   Step1的时间O(m) in average O(m^2) in worst case. 

   ​            Space: O(m)

   Step2: Extra space: O（k）

   Time = O(k*logk) + (n-k)*logk = O(n*logk)  <要做K次的insert>

```java
public class TopKFrequentWords {
    public String[] topKFrequent(String[] combo, int k) {
        if (combo.length == 0 || k == 0) {
            return new String[0];
        }
        Map<String, Integer> freqMap = getFreMap(combo);
        PriorityQueue<Map.Entry<String, Integer>> minHeap = new PriorityQueue<>(k, new Comparator<Map.Entry<String, Integer>>() {
           @Override
           public int compare(Map.Entry<String, Integer> e1, Map.Entry<String, Integer> e2) {
               return e1.getValue().compareTo(e2.getValue());
           }
        });
        for (Map.Entry<String, Integer> entry : freqMap.entrySet()) {
            if (minHeap.size() < k) {
                minHeap.offer(entry);
            } else if (entry.getValue() > minHeap.peek().getValue()) {
                minHeap.poll();
                minHeap.offer(entry);
            }
        }
        return freqArray(minHeap);
    }
    private Map<String, Integer> getFreMap(String[] combo) {
        Map<String, Integer> freqMap = new HashMap();
        for (String s : combo) {
            Integer freq = freqMap.get(s);
            if (freq == null) {
                freqMap.put(s, 1);
            } else {
                freqMap.put(s, freq + 1);
            }
        }
        return freqMap;
    }
    private String[] freqArray(PriorityQueue<Map.Entry<String, Integer>> minHeap) {
        String[] result = new String[minHeap.size()];
        for (int i = minHeap.size() - 1; i >= 0; i--) {
            result[i] = minHeap.poll().getKey();
        }
        return result;
    }
}
```

## [Missing Number I](https://app.laicode.io/app/problem/68?plan=3)

>Given an integer array of size N - 1, containing all the numbers from 1 to N except one, find the missing number.
>
>**Assumptions**
>
>- The given array is not null, and N >= 1
>
>**Examples**
>
>- A = {2, 1, 4}, the missing number is 3
>- A = {1, 2, 3}, the missing number is 4 找不到的时候返回末尾
>- A = {}, the missing number is 1
>
>

==思路==

- 使用HashSet存放所有的值
- 从大到小遍历set
- space = O（n） 开了hashset, time = O(n) 每个元素要放入

```java
public class Solution {
  public int missing(int[] array) {
    // Write your solution here
    int n = array.length + 1;
    Set<Integer> set = new HashSet<>();
    for (int num : array) {
      set.add(num);
    }
    for (int i = 1; i < n; i++) {
      if (!set.contains(i)) {
        return i;
      }
    }
    return n;
  }
}

```

- 整体求targetSum和，long类型防止溢出
- 必须用增强for loop 实现求acutalSum和,因为不知道起始求和值

```java
public class Solution {
    public int missing(int[] array) {
        int n = array.length + 1;
        long targetSum = (n + 0L) * (n + 1) / 2;
        long actualSum = 0L;
        for (int num : array) {
            actualSum += num;
        }
        return (int)(targetSum - acutalSum);
    }
}
```



## [Common Numbers Of Two Sorted Arrays(Array version)](https://app.laicode.io/app/problem/652?plan=3)

>Find all numbers that appear in both of two sorted arrays (the two arrays are all sorted in <u>ascending</u> order).
>
>**Assumptions**
>
>- In each of the two sorted arrays, there could be ==duplicate== numbers.
>- Both two arrays are not null.
>
>**Examples**
>
>- A = {1, 1, 2, 2, 3}, B = {1, 1, 2, 5, 6}, common numbers are [1, 1, 2]

==思路==

1. 不是升序的话将A中的元素放入hashSet， 

2. 遍历if hashset.contains(b), output(b)
3. space = O(m), Time = O(m + n) 

**升序**解法2

谁小移谁，Space = O(1), Time = O(m + n)

```java
public class Solution {
    public List<Integer> common(int[] a, int[] b) {
        List<Integer> common = new ArrayList<>();
        int i = 0;
        int j = 0;
        while (i < a.length && j < b.length) {
            if (a[i] == b[j]) {
                common.add(a[i]);
          		i++;
                j++;
            } else if (a[i] < b[j]) {
                i++;
            } else {
                j++;
            }
        }
        return common;
    }
}
```



## [Remove Certain Characters](https://app.laicode.io/app/problem/395?plan=3)

>Remove given characters in input string, the relative order of other characters should be remained. Return the new string after deletion.
>
>**Assumptions**
>
>- The given input string is not null.
>- The characters to be removed is given by another string, it is guaranteed to be not null.
>
>**Examples**
>
>- input = "abcd", t = "ab", delete all instances of 'a' and 'b', the result is "cd".

**相向而行物理意义：**I的左边不包含pivot一定小于pivot， j的右边不包含j的位置大于等于pivot，I,j 这个闭区间里面是没有定义的

**同行而行的物理意义：**I,j从一个方向往后走，一起往右边加，加的顺序不一样，速度也不一向，一个移动得快一个移动地慢。

**fast的左边不包含fast的位置**，是那些已经处理过的，fast的右边不包含j的位置是还没有处理的，fast指向的那个元素就是正在被处理的。

**slow的物理意义**：（要和fast对应着说）fast到什么地方，slow到什么地方？

所有在slow左边的不包含slow的字母，都是已经被处理过的并且应该要保留下来的。 

==思路==

1. 要删除的target放入Set
2. 快慢指针

​       slow = 0; 

​		fast遍历，if(!set.contains(array[fast])) {

​							array[slow++] = array[fast];

​							}

```java
public class Solution {
    public String remove(String input, String t) {
        char[] array = input.toCharArray();
        Set<Character> set = buildSet(t);
        int slow = 0;
        for (int fast = 0; fast < array.length; fast++) {
            if (!set.contains(array[fast])) {
                array[slow++] = array[fast];
            }
        }
        return new String(array, 0, slow);
    }
    private Set<Character> buildSet(String t) {
        Set<Character> set = new HashSet<>();
        for(int i = 0; i < t.length(); i++) {
            set.add(t.charAt(i));
        }
        return set;
    }
}
```



## [Remove Spaces](https://app.laicode.io/app/problem/281?plan=3)

>Given a string, remove all leading/trailing/duplicated empty spaces.
>
>**Assumptions:**
>
>- The given string is not null.
>
>**Examples:**
>
>- “  a” --> “a”
>- “  I   love MTV ” --> “I love MTV”

**fast的左边不包含fast的位置**，是那些已经处理过的，fast的右边不包含j的位置是还没有处理的，fast指向的那个元素就是正在被处理的。

**slow的物理意义**：（要和fast对应着说）fast到什么地方，slow到什么地方？

所有在slow左边的不包含slow的字母，都是已经被处理过的并且应该要保留下来的。 

Initialize: slow = 0,fast = 0

For each step: 

case1: letter, keep

case2: 前面是字母的空格，keep

case3: ignore: a[fast] = '  ' && (fast == 0 || a[fast - 1] = ' ')

Termination: fast == a.length()

b _ _ _ d               

​      s             

​            f

b _ `d `_ d               

​          s             

​                f

Post-processing: 

if(slow > 0 && a[slow - 1] == '  ') {slow--};

```java
public class Solution {
  public String removeSpaces(String input) {
    // Write your solution here
    if (input == null) {
      return input;
    }
    char[] array = input.toCharArray();
    int slow = 0;
    for (int fast = 0; fast < array.length; fast++) {
      if (array[fast] == ' ' && (fast == 0 || array[fast - 1] == ' ')) {
        continue;
      }
      array[slow++] = array[fast];
    }
    if (slow > 0 && array[slow - 1] == ' ') {
      slow--;
    }
    return new String(array, 0, slow);
  }
}
```



## [Remove Adjacent Repeated Characters I](https://app.laicode.io/app/problem/79?plan=3)

>Remove adjacent, repeated characters in a given string, leaving only one character for each group of such characters.
>
>**Assumptions**
>
>- Try to do it in place.
>
>**Examples**
>
>- “aaaabbbc” is transferred to “abc”
>
>**Corner Cases**
>
>- If the given string is null, returning null or an empty string are both valid.

**fast的左边不包含fast的位置**，是那些已经处理过的，fast的右边不包含j的位置是还没有处理的，fast指向的那个元素就是正在被处理的。

**slow的物理意义**：（要和fast对应着说）fast到什么地方，slow到什么地方？

所有在slow左边的不包含slow的字母，都是已经被处理过的并且应该要保留下来的。 

aabbbbc

  s

  f

Initialize: slow = 1, fast = 1

For each step: 

case1: a[fast] != a[slow- 1], a[slow++] = array[fast]

case2: ignore 

```java
public class Solution {
    public String deDup(String input) {
        if (input == null) {
            return input;
        }
        char[] array = input.toCharArray();
        int slow = 0;
        for (int fast = 0; fast < array.length; i++) {
            if (fast == 0 || array[fast] != array[slow - 1]) {
                array[slow++] = array[fast];
            }
        }
        return new String(array, 0, slow);
    }
}
```





## [Remove Adjacent Repeated Characters IV](https://app.laicode.io/app/problem/82?plan=3)

>消消乐
>
>Repeatedly remove all adjacent, repeated characters in a given string from left to right.
>
>No adjacent characters should be identified in the final string.
>
>**Examples**
>
>- "abbbaaccz" → "aaaccz" → "ccz" → "z"
>- "aabccdc" → "bccdc" → "bdc"

**fast的左边不包含fast的位置**，是那些已经处理过的，fast的右边不包含j的位置是还没有处理的，fast指向的那个元素就是正在被处理的。

**slow的物理意义**：所有在slow左边的不包含slow的字母，都是已经被处理过的并且应该要保留下来的。 

a b b b b a z w

   f

s

   aa 输入aa输出为空

s

​         f

Initialize: fast = 1, slow = 0

For each step: 

case 1: a[fast] != a[slow], then a[slow] = a[fast], slow++, fast循环增加

case2:  a[fast] == a[slow]相同，slow--, while array[fast] == array[fast + 1]，keep fast++, until a[fast] != a[slow] 

```java
public class Solution {
    public String deDup(String input) {
        if (input.length() <= 1) {
            return input;
        }
        char[] array = input.toCharArray();
        int slow = 0;
        for (int fast = 1; fast < array.length; fast++) {
            if (slow == -1 || array[fast] != array[slow]) { //slow = -1表示stack为空,后面需要归位
                slow++;//不相同的时候slow大胆往后走一步，然后将a[fast]赋值给a[slow]
                array[slow] = array[fast];
            } else { //相同就需要减掉slow--
                slow--;
                while(fast < array.length - 1 && array[fast] == array[fast + 1]) {//fast < array.length - 1最多遍历到倒数第二个元素
                    fast++;
                }
            }
        }
        return new String(array, 0, slow + 1);
    }
}
```



## [Determine If One String Is Another's Substring](https://app.laicode.io/app/problem/85?plan=3)

>Determine if a small string is a substring of another large string.
>
>Return the index of the first occurrence of the small string in the large string.
>
>Return -1 if the small string is not a substring of the large string.
>
>**Assumptions**
>
>- Both large and small are not null
>- If small is empty string, return 0
>
>**Examples**
>
>- “ab” is a substring of “bcabc”, return 2
>- “bcd” is not a substring of “bcabc”, return -1
>- "" is substring of "abc", return 0

思路： 滑动窗口解决 Time = O(n^2)



```java
public class Solution {
    public int strstr(String s1, String s2) {
        if (s1 == null || s2 == null || s1.length() < s2.length()) {
            return -1;
        }
        if (s2.length() == 0) {
            return 0;
        }
        //i s1从0往后走，j作为一个offs
        for (int i = 0; i <= s1.length() - s2.length(); i++) {
            int j = 0;
            while (j < s2.length() && s1.charAt(i + j) == s2.charAt(j)) {
                j++;
            }
            if (j == s2.length()) {
                return i;
            }
        }
        return -1;
    }
}
```

# 哈希表

#### [242. 有效的字母异位词](https://leetcode-cn.com/problems/valid-anagram/)

> 给定两个字符串 `*s*` 和 `*t*` ，编写一个函数来判断 `*t*` 是否是 `*s*` 的字母异位词。
>
> ![image-20220407150954592](8 HashTable and String I.assets/image-20220407150954592.png)

```java
class Solution {
    public boolean isAnagram(String s, String t) {
        int[] record = new int[26];
        for (char c : s.toCharArray()) {
            record[c - 'a'] += 1;
        }
        for (char c: t.toCharArray()) {
            record[c - 'a'] -= 1;
        }
        for (int i : record) {
            if (i != 0) {
                return false;
            }
        }
        return true;
    }
}
```

#### [349. 两个数组的交集](https://leetcode-cn.com/problems/intersection-of-two-arrays/)

>给定两个数组，编写一个函数来计算它们的交集。

```java
class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        if (nums1 == null || nums1.length == 0 || nums2 == null || nums2.length == 0) {
            return new int[0];
        }
        Set<Integer> set1 = new HashSet<>();
        Set<Integer> resSet = new HashSet<>();
        //遍历数组1
        for (int i : nums1) {
            set1.add(i);
        }
        //遍历数组2的过程中判断哈希表中是否存在该元素
        for (int i : nums2) {
            if (set1.contains(i)) {
                resSet.add(i);
            }
        }
        int[] resArr = new int[resSet.size()];
        int i = 0;
//       for (int num : resSet) {
//            resArr[i++] = num;
//        }
        Iterator<Integer> iter =  resSet.iterator();
        while (iter.hasNext()) {
            Integer p = iter.next();
            resArr[i++] = p;
        }
        return resArr;
    }
}
```

#### [202. 快乐数](https://leetcode-cn.com/problems/happy-number/)

> 编写一个算法来判断一个数 `n` 是不是快乐数。
>
> 「快乐数」定义为：
>
> 对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
>然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
> 如果 **可以变为  1，那么这个数就是快乐数。**
> 如果 n 是快乐数就返回 true ；不是，则返回 false 。
> 
> ![image-20210822070530246](8 HashTable and String I.assets/image-20210822070530246.png)

判断链表有没有环

```java
class Solution {
    public boolean isHappy(int n) {
        Set<Integer> record = new HashSet<>();
        while (n != 1 && !record.contains(n)) {
            record.add(n);
            n = getNextNumber(n);
        }
        return n == 1;
    }
    private int getNextNumber(int n) {
        int res = 0;
        while (n > 0) {
            int temp = n % 10; //个位
            res += temp * temp;
            n = n / 10; //十位or理解为去掉个位后的数
        }
        return res;
    }
}
```

```java
class Solution {
    public boolean isHappy(int n) {
        int slow = n;
        int fast = getNextNumber(n);
        while (fast != 1 && slow != fast) {
           slow = getNextNumber(slow);
           fast = getNextNumber(getNextNumber(fast));
        }
        return fast == 1;
    }
    private int getNextNumber(int n) {
        int res = 0;
        while (n > 0) {
            int temp = n % 10;//个位
            res += temp * temp;
            n = n / 10;//十位
        }
        return res;
    }
}
```

#### [剑指 Offer 49. 丑数](https://leetcode-cn.com/problems/chou-shu-lcof/)

![image-20220407151553997](8 HashTable and String I.assets/image-20220407151553997.png)

![image-20220407155849158](8 HashTable and String I.assets/image-20220407155849158.png)

```java
//设动态规划列表  ，dp[i] 代表第 i + 1i+1 个丑数；
        public int nthUglyNumber(int n) { 
            int a = 0, b = 0, c = 0; //a b c 表示维护的num2 num3 num5的index位置
            int[] dp = new int[n];
            dp[0] = 1;
            for(int i = 1; i < n; i++) {
                int n2 = dp[a] * 2, n3 = dp[b] * 3, n5 = dp[c] * 5; //维护三个array
                dp[i] = Math.min(Math.min(n2, n3), n5); //这里取最小值
                if(dp[i] == n2) a++;
                if(dp[i] == n3) b++; //如果最小值重复了 那就都要往后走一步
                if(dp[i] == n5) c++; 
            }
            return dp[n - 1];
        }

```





#### [1. 两数之和](https://leetcode-cn.com/problems/two-sum/)

>给定一个整数数组 `nums` 和一个整数目标值 `target`，请你在该数组中找出 **和为目标值** *`target`* 的那 **两个** 整数，并返回它们的数组下标。
>
>```
>输入：nums = [2,7,11,15], target = 9
>输出：[0,1]
>解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
>```

两数之和这道题目，不仅要判断y是否存在而且还要记录y的下表位置，因为要返回x 和 y的下表。所以set 也不能用。

![image-20210822111241917](8 HashTable and String I.assets/image-20210822111241917.png)

```java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        if (nums == null || nums.length < 2) {
            return new int[] {-1, -1};
        }
        int[] res = new int[] {-1, -1};
        HashMap<Integer, Integer> map = new HashMap<>(); //key是数值，value是数组下标
        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(target - nums[i])) {//可以 O(1) 地寻找target - nums[i]，找到了就存入
                res[0] = map.get(target - nums[i]); //根据值取出下标
                res[1] = i;
                break;
            }
            map.put(nums[i], i);
        }
        return res;
    }
}
```

#### [454. 四数相加 II](https://leetcode-cn.com/problems/4sum-ii/) - kv分两半

![image-20211212153639339](8%20HashTable%20and%20String%20I.assets/image-20211212153639339.png)

- HashMap存两个数组之和，如AB。然后计算两个数组之和，如 CD。时间复杂度为：`O(n^2)+O(n^2)`，得到 `O(n^2)`

  我们以存 AB 两数组之和为例。首先求出 A 和 B 任意两数之和 sumAB，以 sumAB 为 key，sumAB 出现的次数为 value，存入 hashmap 中。

  然后计算 C 和 D 中任意两数之和的相反数 sumCD，在 hashmap 中查找是否存在 key 为 sumCD。

```java
class Solution {
    public int fourSumCount(int[] nums1, int[] nums2, int[] nums3, int[] nums4) {
        Map<Integer, Integer> map = new HashMap<>(); // sum freq 
        int res = 0;
        for (int i : nums1) {//统计两个数组中的元素之和,同时统计出现的次数, 放入map
            for (int j : nums2) {
                int sum = i + j;
                Integer freq = map.get(sum);
                if (freq == null) {
                    map.put(sum, 1);
                } else {
                    map.put(sum, freq + 1);
                }
            }
        }

        for (int i : nums3) { //统计剩余的两个元素和,在map中找是否存在相加为0情况,同时记录次数
            for (int j : nums4) {
                int sum = i + j;
                if (map.containsKey(0 - sum)) {
                    res += map.get(0 - sum);
                }
            }
        }
        return res;
    }
}
```

#### [383. 赎金信](https://leetcode-cn.com/problems/ransom-note/) - 数组哈希

>![image-20211212163950457](8%20HashTable%20and%20String%20I.assets/image-20211212163950457.png)
>

```java
class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        int[] arr = new int[26];
        int temp;
        //记录杂志字符串出现的次数
        for (int i = 0; i < magazine.length(); i++) {
            temp = magazine.charAt(i) - 'a';
            arr[temp]++;
        }
        for (int i = 0; i < ransomNote.length(); i++) {
            temp = ransomNote.charAt(i) - 'a';
            if (arr[temp] > 0) { //满足大于0的时候 一直减小
                arr[temp]--;
            } else {
                return false;
            }
        }
        return true;
    }
}
```

#### [15. 三数之和](https://leetcode-cn.com/problems/3sum/)  - 双指针

>给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且**不重复**的三元组。
>
>```
>输入：nums = [-1,0,1,2,-1,-4]
>输出：[[-1,-1,2],[-1,0,1]]
>```

**这道题目使用双指针法 要比哈希法高效一些**，首先将数组排序，然后有一层for循环，i从下表0的地方开始，同时定一个下表left 定义在i+1的位置上，定义下表right 在数 组结尾的位置上。

![image-20211212224312252](8%20HashTable%20and%20String%20I.assets/image-20211212224312252.png)

这里相当于  a = nums[i] b = nums[left]  c = nums[right]。如果nums[i] + nums[left] + nums[right] > 0  就说明此时三数之和大了，因为数组是排序后了，所以right下表就应该向左移动，这样才能让三数之和小一些。如果 nums[i] + nums[left] + nums[right] < 0 说明 此时 三数之和小了，left 就向右移动，才能让三数之和大一些，直到left与right相遇为止。

```java
 class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        if (nums.length == 0) {
            return res;
        }
        Arrays.sort(nums); //一定要排序
        for (int i = 0; i < nums.length; i++) {
            if (i > 0 && nums[i - 1] == nums[i]) {
                continue;
            }
            int left = i + 1;
            int right = nums.length - 1;
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                if (sum > 0) {
                    right--;
                } else if (sum < 0) {
                    left++;
                } else {
                    res.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    while(right > left && nums[right] == nums[right - 1]) right--;
                    while (right > left && nums[left] == nums[left + 1]) left++;
                    left++;
                    right--;
                }
            }
        }
        return res;
    }
}
```

#### [18. 四数之和](https://leetcode-cn.com/problems/4sum/)

>给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] ：
>
>```
>示例 1：
>输入：nums = [1,0,-1,0,-2,2], target = 0
>输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
>```

四数之和的双指针解法是两层for循环nums[k] + nums[i]为确定值，依然是循环内有left和right下表作为双指针，找出nums[k] + nums[i] + nums[left] + nums[right] == target的情况，三数之和的时间复杂度是O(n^2), 四数之和的时间复杂度是O(n^3). 

<img src="8%20HashTable%20and%20String%20I.assets/image-20211215200837446.png" alt="image-20211215200837446" style="zoom:25%;" />

```java
class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        List<List<Integer>> res = new ArrayList<>();
        if (nums.length == 0) {
            return res;
        }
        Arrays.sort(nums);
        for (int i = 0; i < nums.length; i++) {
            if (i > 0 && nums[i - 1] == nums[i]) {
                continue;
            }
            for (int j = i + 1; j < nums.length; j++) {
                if (j > i + 1 && nums[j - 1] == nums[j]) {
                    continue;
                }
                int left = j + 1;
                int right = nums.length - 1;
                while (left < right) {
                    int sum = nums[i] + nums[j] + nums[left] + nums[right];
                    if (sum > target) {
                        right--;
                    } else if (sum < target) {
                        left++;
                    } else {
                        res.add(Arrays.asList(nums[i], nums[j], nums[left], nums[right]));
                        while (right > left && nums[right] == nums[right - 1]) right--;
                        while (right > left && nums[left] == nums[left + 1]) left++;

                        left++;
                        right--;
                    }
                }
            }
        }
        return res;
    }
}
```

## 字符串

#### [344. 反转字符串](https://leetcode-cn.com/problems/reverse-string/)

>编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。
>
>不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
>
>```
>输入：["h","e","l","l","o"]
>输出：["o","l","l","e","h"]
>```

```java
class Solution {
    public void reverseString(char[] s) {
        int left = 0;
        int right = s.length - 1;
        while (left <= right) {
            char temp = s[left];
            s[left] = s[right];
            s[right] = temp;
            left++;
            right--;
        }
    }
}
```

#### [541. 反转字符串 II](https://leetcode-cn.com/problems/reverse-string-ii/)  k次累加

>给定一个字符串 s 和一个整数 k，从字符串开头算起，每 2k 个字符反转前 k 个字符。
>
>如果剩余字符少于 k 个，则将剩余字符全部反转。
>如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。
>
>```
>输入：s = "abcdefg", k = 2
>输出："bacdfeg"
>```

遍历字符串的过程中，只要让 i += (2 * k)，i 每次移动 2 * k 就可以了，然后判断是否需要有反转的区间。

**当需要固定规律一段一段去处理字符串的时候，要想想在for循环的表达式上做做文章。**

```java
class Solution {
    public String reverseStr(String s, int k) {
        char[] array = s.toCharArray();
        for (int i = 0; i < array.length; i+= 2 * k) {
            int start = i;
            int end = Math.min(array.length - 1, start + k - 1);
            while (start < end) {
                char temp = array[start];
                array[start] = array[end];
                array[end] = temp;
                start++;
                end--;
            }
        }
        return new String(array);
    }
}
```

#### [剑指 Offer 05. 替换空格](https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof/)

> 请实现一个函数，把字符串 `s` 中的每个空格替换成"%20"。
>
> ```
> 输入：s = "We are happy."
> 输出："We%20are%20happy."
> ```

**很多数组填充类的问题，都可以先预先给数组扩容带填充后的大小，然后在从后向前进行操作。**

1. 不用申请新数组。
2. 从后向前填充元素，避免了从前先后填充元素要来的 每次添加元素都要将添加元素之后的所有元素向后移动。

```java
public static String replaceSpace(StringBuffer str) {
    if (str == null) {
        return null;
    }
    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < str.length(); i++) {
        if (" ".equals(String.valueOf(str.charAt(i)))) {
            sb.append("%20");
        } else {
            sb.append(str.charAt(i));
        }
    }
    return sb.toString();
}
```

#### [151. 翻转字符串里的单词](https://leetcode-cn.com/problems/reverse-words-in-a-string/)

>```
>示例 3：
>输入: "a good  example"
>输出: "example good a"
>解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
>```

```java
class Solution {
    public String reverseWords(String s) {
        if(s == null || s.length() == 0) {
            return s;
        }
        s = removeSpace(s);
        char[] array = s.toCharArray();
        reverse(array, 0, array.length - 1);
        int start = 0;
        for (int i = 0; i < array.length; i++) {
            if (array[i] != ' ' && (i == 0 || array[i - 1] == ' ')) {
                start = i;
            } 
            if (array[i] != ' ' && (i == array.length - 1 || array[i + 1] == ' ')) {
                reverse(array, start, i);
            }
        }
        return new String(array);
    }

    private void reverse(char[] array, int left, int right) {
        while (left <= right) {
            char c = array[left];
            array[left] = array[right];
            array[right] = c;
            left++;
            right--;
        }
    }
    private String removeSpace(String s) {
        int start = 0;
        int end = s.length() - 1;
        while (s.charAt(start) == ' ') start++;
        while(s.charAt(end) == ' ') end--;
        StringBuilder sb = new StringBuilder();
        while (start <= end) {
            char c = s.charAt(start);
            if (c != ' ' || sb.charAt(sb.length() - 1) != ' ') {
                sb.append(c);
            } 
            start++;
        }
        return sb.toString();
    }
}
```

#### [剑指 Offer 58 - II. 左旋转字符串](https://leetcode-cn.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/)

>字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。
>
>```
>示例 1：
>输入: s = "abcdefg", k = 2
>输出: "cdefgab"
>示例 2：
>输入: s = "lrloseumgh", k = 6
>输出: "umghlrlose"
>```

1. 反转区间为前n的子串
2. 反转区间为n到末尾的子串
3. 反转整个字符串

```java
class Solution {
    public String reverseLeftWords(String s, int n) {
        char[] array = s.toCharArray();
        reverse(array, 0, n - 1);
        reverse(array, n, array.length - 1);
        reverse(array, 0, array.length - 1);
        return new String(array);
    }
    private void reverse(char[] array, int left, int right) {
        while (left <= right) {
            char temp = array[left];
            array[left] = array[right];
            array[right] = temp;
            left++;
            right--;
        }
    }
}
```

#### KMP

#### [49. 字母异位词分组](https://leetcode-cn.com/problems/group-anagrams/)

![image-20220116214618765](8%20HashTable%20and%20String%20I.assets/image-20220116214618765.png)

```java
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> res = new ArrayList<>();
        Map<String, Integer> map = new HashMap<>();
        int count = 0; //从零开始记录每个位置存放的str
        for(String str : strs) {
            char[] array = str.toCharArray();
            Arrays.sort(array);
            String nStr = new String(array);
            if (!map.containsKey(nStr)) {
                res.add(new ArrayList<>());
                map.put(nStr, count);
                count++;
            }
            res.get(map.get(nStr)).add(str);//先找到存放的位置然后加入原来的字符串
        }
        return res;
    }
}
```

#### [56. 合并区间](https://leetcode-cn.com/problems/merge-intervals/)

![image-20220116222812714](8%20HashTable%20and%20String%20I.assets/image-20220116222812714.png)

![image-20220116224238683](8%20HashTable%20and%20String%20I.assets/image-20220116224238683.png)

```java
class Solution {
    public int[][] merge(int[][] intervals) {
        //1 按照区间左边排列
        Arrays.sort(intervals, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                if(o1[0] == o2[0]) {
                    return 0;
                }
                return o1[0] > o2[0] ? 1 : -1;//升序排列
            }
        });
        ArrayList<int[]> outputs = new ArrayList<>();
        for (int i = 0; i < intervals.length; i++) {
            int[] curInterval = intervals[i];
            if (outputs.isEmpty()) {
                outputs.add(curInterval);
            } else {
                int[] outputLastInterval = outputs.get(outputs.size() - 1);
                int outputLastIntervalRight = outputLastInterval[1]; //已存右边界
                int currLeft = curInterval[0];
                if (outputLastIntervalRight < currLeft) {
                    outputs.add(curInterval);
                } else {
                    int currRight = curInterval[1];
                    outputLastInterval[1] = Math.max(outputLastIntervalRight, currRight);
                }
            }
        }
        return outputs.toArray(new int[outputs.size()][]);
    }
}
```

#### [76. 最小覆盖子串](https://leetcode-cn.com/problems/minimum-window-substring/)

![image-20220118075958385](8%20HashTable%20and%20String%20I.assets/image-20220118075958385.png)

![image-20220118080140890](8%20HashTable%20and%20String%20I.assets/image-20220118080140890.png)

```java
class Solution {
    public String minWindow(String s, String t) {
        // 使用哈希表进行判断是否包含
        HashMap<Character, Integer> need = new HashMap<>();
        HashMap<Character, Integer> window = new HashMap<>();

        // 将字符串t的元素存放在哈希表need中
        for(int i = 0; i < t.length(); i++){
            need.put(t.charAt(i), need.getOrDefault(t.charAt(i), 0) + 1);
        }

        int valid = 0, r = 0, l = 0;
        int start = 0, len = Integer.MAX_VALUE;
        // r为右指针、l为左指针
        while(r < s.length()){
            // 将字符串s的元素存放在哈希表window中
            char addChar = s.charAt(r);
            window.put(addChar, window.getOrDefault(addChar, 0) + 1);
            r++;

            // 如果need包含addChar并且个数也一致、表示已经满足一个字符了
            if(need.containsKey(addChar) && window.get(addChar).equals(need.get(addChar))){
                valid++;
            }
            // 直到valid等于need.size()表示此部分已经包含t、开始考虑进行缩窗口
            while(valid == need.size()){
                // 每次更新保留最小的字符串长度
                if(r - l < len){
                    len = r - l;
                    start = l;
                }
                // 获取left侧的元素
                char removeChar = s.charAt(l);
                // 满足条件说明删错了、需要valid--
                if(need.containsKey(removeChar) && window.get(removeChar).equals(need.get(removeChar))){
                    valid--;
                }
                window.put(removeChar, window.get(removeChar) - 1);
                l++;
            }
        }
        // 判断len的值没有变说明根本涉及不到缩窗口的过程。
        // 也就是s不包含t的所有字符串。典型案例 s: "a", t: "aa"
        return len == Integer.MAX_VALUE ? "" : s.substring(start, start + len);
    }
}
```

#### [169. 多数元素](https://leetcode-cn.com/problems/majority-element/)

![image-20220120115145718](8%20HashTable%20and%20String%20I.assets/image-20220120115145718.png)

方法一 使用hashset记录个数打擂台

```java
class Solution {
    public int majorityElement(int[] nums) {
        Map<Integer, Integer> map = countMap(nums);
        Map.Entry<Integer, Integer> major = null;
        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            if (major == null || entry.getValue() > major.getValue()) {
                major = entry;
            }
        }
        return major.getKey();
    }
    private Map<Integer, Integer> countMap(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        for(int num : nums) {
            Integer a = map.get(num);
            if (a == null) {
                map.put(num, 1);
            } else {
                map.put(num, a + 1);
            }
        }
        return map;
    }
}
```

如果将数组 nums 中的所有元素按照单调递增或单调递减的顺序排序，那么下标为n/2的元素（下标从 0 开始）一定是众数。

```java
class Solution {
    public int majorityElement(int[] nums) {
        Arrays.sort(nums);
        return nums[nums.length / 2];
    }
}
```

#### [448. 找到所有数组中消失的数字](https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array/)

![image-20220202231632633](8%20HashTable%20and%20String%20I.assets/image-20220202231632633.png)

```java
class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        Set<Integer> set = new HashSet<>();
        List<Integer> list = new ArrayList<>();
        for (int i : nums) {
            set.add(i);
        }
        for (int i = 1; i <= nums.length; i++) {
            if (!set.contains(i)) {
                list.add(i);
            }
        }
        return list;
    }
}
```

## 滑动窗口

![image-20220203223637498](8%20HashTable%20and%20String%20I.assets/image-20220203223637498.png)



https://www.bilibili.com/video/BV1PU4y147tP?from=search&seid=4277159951594723532&spm_id_from=333.337.0.0

![image-20220203224646089](8%20HashTable%20and%20String%20I.assets/image-20220203224646089.png)
![image-20220203225024953](8%20HashTable%20and%20String%20I.assets/image-20220203225024953.png)

#### [3. 无重复字符的最长子串](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/)

![image-20220203230115235](8%20HashTable%20and%20String%20I.assets/image-20220203230115235.png)

```java
class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> set = new HashSet<>();
        int left = 0, res = 0;
        for (int i = 0; i < s.length(); i++) {// i 是右指针
            char c = s.charAt(i);
            while (!set.add(c)) { // 1 进：当前遍历的字符进入窗口
                set.remove(s.charAt(left++)); // 2 出 不符合条件时left持续出窗口
            }
            res = Math.max(res, i - left + 1); // 3 计算
        } 
        return res;
    }
}
```

方法二 使用hashmap

```java
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int left = 0;
        int res = 0;
        Map<Character, Integer> map = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (map.containsKey(c)) {
                // left = first valid position without cur
                left = Math.max(map.get(c), left); //将左端点直接移到某个出问题节点的下一个位置
            }
            map.put(c, i + 1);//记录当前位置的下一个位置 
            res = Math.max(res, i - left + 1);
        }
        return res;
    }
}
```

#### [159. 至多包含两个不同字符的最长子串](https://leetcode-cn.com/problems/longest-substring-with-at-most-two-distinct-characters/)

#### [340. 至多包含 K 个不同字符的最长子串](https://leetcode-cn.com/problems/longest-substring-with-at-most-k-distinct-characters/)

![image-20220205083258172](8%20HashTable%20and%20String%20I.assets/image-20220205083258172.png) 

```java
class Solution {
    public int lengthOfLongestSubstringTwoDistinct(String s) {
        Map<Character, Integer> map = new HashMap<>();
        int left = 0, res = 0;
        for (int i = 0; i < s.length(); i++) {
            // 1 遍历当前cur
            char cur = s.charAt(i);
            map.put(cur, map.getOrDefault(cur, 0) + 1); //2 记录出现的频率
            while (map.size() > 2) { // 说明出现了三个distinct character
                char c = s.charAt(left);
                map.put(c, map.get(c) - 1); // 开始减少左边的元素频率 然后left++其实可以确保left后面有这个元素的
                if (map.get(c) == 0) { //通过上一行代码减一 说明这个元素只出现了一次可以移除
                    map.remove(c);
                }
                left++;
            }
            res = Math.max(res, i - left + 1);
        }
        return res;
    }
}
```

#### [76. 最小覆盖子串](https://leetcode-cn.com/problems/minimum-window-substring/)

![image-20220207092529937](8%20HashTable%20and%20String%20I.assets/image-20220207092529937.png)

```java
class Solution {
    public String minWindow(String s, String t) {
        Map<Character, Integer> map = new HashMap<>();
        for(char c : t.toCharArray()) { //存放target的string
            map.put(c, map.getOrDefault(c, 0) + 1);
        }
        int left = 0, minStart = 0, minLen = Integer.MAX_VALUE, count = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (map.containsKey(c)) { // 如果有这个character 先更新count
                if (map.get(c) > 0) { //窗口内有绝对是小于零的 如果map中取元素大于零 说明这个元素还没有被窗口遍历到
                    count++;
                }
                map.put(c, map.get(c) - 1); //窗口里已经有了 就从map里面删除一个
            }
            while(count == t.length()) {
                if (i - left + 1 < minLen) {
                    minLen = i - left + 1;
                    minStart = left;
                }
                char leftChar = s.charAt(left);
                if (map.containsKey(leftChar)) {
                    map.put(leftChar, map.get(leftChar) + 1); // left要从滑动窗口删除 需要恢复map
                    if (map.get(leftChar) > 0) { //如果左边窗口元素是目标元素 那么目标就要减少
                        count--;
                    }
                }
                left++;
            }
        }
        if (minLen == Integer.MAX_VALUE) {
            return "";
        }
        return s.substring(minStart, minStart + minLen);
    }
}
```













#### [438. 找到字符串中所有字母异位词](https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/)

![image-20220203220642281](8%20HashTable%20and%20String%20I.assets/image-20220203220642281.png)

```java
public class Solution {
  public List<Integer> allAnagrams(String sh, String lo) {
    // Write your solution here  sh用于匹配
        List<Integer> result = new ArrayList<Integer>();
        if (lo.length() == 0) {
            return result;
        }
        //when s is longer that l, there is no way any of the substring of l
        //could be an anagram of s (s是同构异形)
        if (sh.length() > lo.length()) {
            return result;
        }
        //This map records for each of the distinct characters in s
        //how many characters are needed
        //eg. s = "abbc", map = {'a': 1, 'b':2,'c':1}
        //when we get an instance of 'a' in l, we let count of 'a' decremented by 1
        //and only when the count is from 1 to 0, we have 'a' totally matched
        Map<Character, Integer> map = countMap(sh);
        //record how many distinct characters have been matched
        //only when all the distinct characters are matched,
        //match == map.size(), we find an anagram
        int match = 0;
        // we have a sliding window of size s.length(), and since the size is fixed
        //we only need to record the end index of the sliding window
        //when move the sliding window by one step from left to right, what we need to change is
        //1. remove the leftmost character at the previous sliding window
        //2. add the rightmost character at the current sliding window
        for (int i = 0; i < lo.length(); i++) {
            //handle the new added character(rightmost) at the current sliding window
            char tmp = lo.charAt(i);
            Integer count = map.get(tmp);
            if (count != null) {
                //the number of needed count should be --
                // and only when the count is from 1 to 0, we find an additional
                //match of distinct character
                map.put(tmp, count - 1);
                if (count == 1) {
                    match++;
                }
            }
            //handle the leftmost character at the previous sliding window
            if (i >= sh.length()) {
                tmp = lo.charAt(i - sh.length());
                count = map.get(tmp);
                if (count != null) {
                    // the number of needed count should be ++
                    // and only when the count if from 0 to 1, we are short for one match of distinct character
                    map.put(tmp, count + 1);
                    if (count == 0) {
                        match--;
                    }
                }
            }
            //for the current sliding window, if all the distinct characters are matched(the count are all zero)
            if (match == map.size()) {
                result.add(i - sh.length() + 1);
            }
        }
        return result;
  }
   private Map<Character, Integer> countMap(String s) {
        Map<Character, Integer> map = new HashMap<Character, Integer>();
        for (char ch : s.toCharArray()) {
            Integer count = map.get(ch);
            if (count == null) {
                map.put(ch, 1);
            } else {
                map.put(ch, count + 1);
            }
        }
        return map;
    }
}
```

#### [554. 砖墙](https://leetcode-cn.com/problems/brick-wall/)

![image-20220330111410667](8 HashTable and String I.assets/image-20220330111410667.png) 使用hashmap,记录0到前长度作为key, 然后value是这个key出现的次数，如果出现次数最大，那就是要穿过的地方，那么就是要穿过的地方就越小。

```java
class Solution {
    public int leastBricks(List<List<Integer>> wall) {
        //position = sum to i; value = count
        HashMap<Integer, Integer> map = new HashMap<>();
        int sum = 0;
        for (int i = 0; i < wall.size(); i++) {
            int pos = 0;
            for (int j = 0; j < wall.get(i).size(); j++) {
                pos += wall.get(i).get(j);
                map.put(pos, map.getOrDefault(pos, 0) + 1);
                if (i == 0) { //如果只有一列的情况
                    sum += wall.get(i).get(j);
                }
            }
        }
        int res = Integer.MAX_VALUE;
        for (Integer pos : map.keySet()) {
            if (sum == pos) // 这里判断如果只有一列，那么求得的pos 一定就是sum直接返回wall.size()
                continue;
            res = Math.min(res, wall.size() - map.get(pos));
            //只有map.get(pos)能够取到最大值（即我避免了切割相同砖块最多的那一组），那么res就是最小值，
        }
        return res == Integer.MAX_VALUE ? wall.size() : res; //如果只有一列那就返回墙的大小
    }
}
```

#### [36. 有效的数独](https://leetcode-cn.com/problems/valid-sudoku/)

![image-20220330181516080](8 HashTable and String I.assets/image-20220330181516080.png)

```java
class Solution {
    public boolean isValidSudoku(char[][] board) {
        for (int x = 0; x < 9; x++) {
            for (int y = 0; y < 9; y++) {
                if (board[x][y] != '.') {
                    for (int j = 0; j < 9; j++) {
                        if (j != y) {
                            if (board[x][j] == board[x][y]) {
                                return false;
                            }
                        }
                    }
                    for (int i = 0; i < 9; i++) {
                        if (i != x) {
                            if (board[i][y] == board[x][y]) {
                                return false;
                            }
                        }
                    }
                    int sx = x / 3 * 3;
                    int sy = y / 3 * 3;
                    for (int i = 0; i < 3; i++) {
                        for (int j = 0; j < 3; j++) {
                            if (sx + i != x && sy + j != y && board[sx + i][sy + j] == board[x][y]) {
                                return false;
                            }
                        }
                    }
                }
            }
        }
        return true;
    }
}
```
