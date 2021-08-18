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

```java
PriorityQueue<Map.Entry<String, Integer>> minHeap = new PriorityQueue<>(k, new Comparator<Map.Entry<String, Integer>>() {
           @Override
           public int compare(Map.Entry<String, Integer> e1, Map.Entry<String, Integer> e2) {
               return e1.getValue().compareTo(e2.getValue());
           }
        });
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

```
 //we need to find in total what is the number
        int count = 0;
        while (ti < t.length() && t.charAt(ti) >= '0' && t.charAt(ti) <= '9') {
            count = count * 10 + (t.charAt(ti) - '0');
            ti++;
        }
```

最小值定义： 

 int[] max = new int[]{Integer.MIN_VALUE}; //这样就可以使用interger表示里面的int最小了

