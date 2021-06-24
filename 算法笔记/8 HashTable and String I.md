# HashTable and String I

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
        if (input == null) {
            return input;
        }
        Char[] array = input.toCharArray();
        int slow = 0;
        for (int fast = 0; fast < array.length; fast++) {
            if (array[fast] = ' ' &&(fast == 0 || array[fast-1]) = ' ') {
                continue;
            }
            array[slow++] = array[fast];
        }
        if (slow > 0 && array[slow - 1] == ' ')
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

