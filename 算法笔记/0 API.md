# 必须记忆的Interface

## LinkedList

`get(int index)`

`set(int index, E e)`

`add(int index, E e), add(E e)`

`remove(int index)`

`size()`

`isEmpty()`

>addLast()
>
>getLast()
>
>removeLast()
>
>addFirst()
>
>getFirst()
>
>removeFirst()

Iterator

==实现==： LinkedList<Student>  st = new LinkedList<>();

ArrayList

> 嵌套List<List<Integer>> st = new LinkedList<>();
>
> st.add(new ArrayList<>());



## ArrayList

`get(int index)`

`set(int index, E e)`

`add()`

`remove()`

`size()`



## Queue & Deque & Stack

**Queue** 

`offer()`

`poll()`

`peek()`

`isEmpty()`

`size()`

**Deque**

`offerFirst(),offerLast()`

`pollFirst(),pollLast()`

`peekFirst(),peekLast()`

`isEmpty()`

`size()`

==implementation==: LinkedList, ArrayDeque

Queue<Integer> queue = new LinkedList<>();

**stack**

`pop()`

`peek()`

`push()`

`empty()`



## PriorityQueue

`offer()`

`poll()`

`peek()`

`isEmpty()`

`size()`

PriorityQueue<Integer> minHeap = new PriorityQueue<Integer>();

使用匿名类，实现comparator接口，重写compare方法

```java
PriorityQueue<Map.Entry<String, Integer>> minHeap = new PriorityQueue<>(k, new Comparator<Map.Entry<String, Integer>>() {
           @Override
           public int compare(Map.Entry<String, Integer> e1, Map.Entry<String, Integer> e2) { //Map.Entry<String, Integer>类型 e1 - e2这种按顺序是从小到大, minheap
               return e1.getValue().compareTo(e2.getValue());
           }
        });

/// 注意实现compare方法
//反序
PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
//自己实现的话
class MyInteger {
    public int value;
    public MyInteger(int value) {
        this.value = value;
    }
    static class Mycomparator implements Comparator<MyInteger> {
        @Override
        public int compare(MyInteger o1, MyInteger o2) {
            if (o1.value == o2.value) {
                return 0;
            }
            return o1.value > o2.value ? -1 : 1; //大的优先，即maxheap 
        }
    }
}

```

## Map

- **Map Interface**

`put(key, value)`

`get(key)`

`containsKey(key)`

`remove(key)`

`size()`

`isEmpty()`

Set<Map.Entry<Key, Vlue>> entrySet()

Set<KeyType> keySet()

`freqMap.entrySet()`

freqMap.`keySet()`是map的集合,可以遍历

```java
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
```

- **Map.Entry<Key, Value>**  iterface

**Map都有entrySet()** 

Map.==Entry==<String, Integer> entry

entry.==getKey()== + ":" + entry.==getValue()==

```
for(Map.Entry<String, Integer> entry : scores.entrySet()) {
	System.out.println(entry.getKey() + ":" + entry.getValue());
}
```

遍历Map.Entry

```java
Iterator<Map.Entry<String, Integer>> iter = M.entrySet();
while (iter.hasNext) {
	Map.Entry<String, Integer> curr = iter.next();
	System.out.println(curr.getKey() + " " cur.getValue());
}
```

计算频率

```
Integer oldValue = scores.get(word);
	if (oldValue == null) {
		scores.put(word, 1);
	} else {
		scores.put(word, oldValue + 1);
	}
```

遍历set

```
Set<Point> mySet
Iterator<Point> iter = mySet.iterator();
while (iter.hasNext()) {
	Point p = iter.n
}
```

## Collection 

ArrayList, LinkedList, TreeSet, HashSet实现了这个接口

`contains()`

`size()`

`add()`

`remove()`

`isEmpty()`

`iterator()`

set有以上方法





 private final static HashSet<Character> vowels = new HashSet<>(`Arrays.asList`('a', 'e,', 'i', 'o', 'u',

  'A','E', 'I', 'O', 'U'));

##  矩阵数学

 int large = (int)Math.`sqrt(c);`

```
//定义一个整型数组:3行4列
int a[][] = new int[3][4];
//获取行数---3行，将每一行的一维数组看作元素
int lenY = a.length;
//获取列数---4列，将二维数组的第一行的列数统计出来
int lenX = a[0].length;
```

字符串转换为数字： 

```java
private int stoi(String s) {
    return Integer.valueOf(s);
}
```

```java
 //we need to find in total what is the number
        int count = 0;
        while (ti < t.length() && t.charAt(ti) >= '0' && t.charAt(ti) <= '9') {
            count = count * 10 + (t.charAt(ti) - '0');
            ti++;
        }
```

最小值定义： 

 int[] max = new int[]{Integer.MIN_VALUE}; //这样就可以使用interger表示里面的int最小了

顺时针打印矩阵 这里可以是非方阵。一般切割上下。然后剩下右边左边。

```java
import java.util.ArrayList;
public class Solution {
    public ArrayList<Integer> printMatrix(int [][] matrix) {
        ArrayList<Integer> res = new ArrayList<>();
        int rows = matrix.length;//行数
        int cols = matrix[0].length;//列
        if (rows == 0) {
            return res;
        }
        int left = 0;
        int right = cols - 1;
        int up = 0; 
        int down = rows - 1;
        while (left < right && up < down) {
            for (int i = left; i <= right; i++) {
                res.add(matrix[up][i]);
            }
            for (int i = up + 1; i <= down - 1; i++) {
                res.add(matrix[i][right]);
            }
            for (int i = right; i >= left; i--) {
                res.add(matrix[down][i]);
            }
            for (int i = down - 1; i >= up + 1; i--) {
                res.add(matrix[i][left]);
            }
            left++;
            right--;
            up++;
            down--;
        }
        if (left > right || up > down) {
            return res;
        }
        if (left == right) {
            for (int i = up; i <= down; i++) {
                res.add(matrix[i][left]);
            }
        } else {
            for (int i = left; i <= right; i++) {
                res.add(matrix[up][i]);
            }
        }
        return res;
    }
}
```

