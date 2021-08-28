# 4 Queue & Stack
## Sort With 2 Stacks
Given an array that is initially stored in one stack, sort it with one additional stacks (total 2 stacks).

After sorting the original stack should contain the sorted integers and from top to bottom the integers are sorted in ascending order.

Assumptions:

The given stack is not null.
There can be duplicated numbers in the give stack.
Requirements:

No additional memory, time complexity = O(n ^ 2).

- 初始input stack 用来存没有sort好的元素
- buffer用来左半边用来装sort好的,右半边倒回去给input继续找
- 关键: 1.1 先将input里的元素倒到buffer里 然后找到里面的curmin,并且记录一个count
		   1.2 将大于curmin的元素放回到input, 小于的就保存到buffer里
		   2 将buffer

注意我这里实现用得是Deque然后一直用得offerFirst所以是个左开右闭的stack

```java
public class Solution {
	public void sort(LinkedList<Integer> s1) {
		LinkedList<Integer> s2 = new LinkedList<Integer>();
		sort(s1, s2);
	}
	private void sort(Deque<Integer> input, Deque<Integer> buffer) {
		while (!input.isEmpty()) {	//确保所有的input都查看过
			int curMin = Integer.MAX_VALUE;
			int count = 0;
			//step 1.1 把input里的值都遍历一遍放到buffer然后找到curmin
			while (!input.isEmpty()) {
				int cur = input.pollFirst();
				if (cur < curMin) {
					curMin = cur;
					count = 1;
				} else if (cur == curMin) {
					count++;
				}
				buffer.offerFirst(cur);
			}
			//1.2 buffer里不是curMin的放回input
			while (!buffer.isEmpty() && buffer.peekFirst() >= curMin) {
				int tmp = buffer.pollFirst();
				if (tmp != curMin) {
					input.offerFirst(tmp);
				}
			}
			// 1.3 将curmin放到buffer里
			while (count-- > 0) {
				buffer.offerFirst(curMin);
			}
		}
		// step 2 将buffer里的值统统放回input 确保升序
		while (!bufer.isEmpty()) {
			input.offerFirst(buffer.pollFirst());
		}
	}
}
```
## Queue By Two Stacks
Java: Implement a queue by using two stacks. The queue should provide size(), isEmpty(), offer(), poll() and peek() operations. When the queue is empty, poll() and peek() should return null.

Assumptions

The elements in the queue are all Integers.
size() should return the number of elements buffered in the queue.
isEmpty() should return true if there is no element buffered in the queue, false otherwise.

- 一个stack用来push存 一个stack用来poll(当它不为空时) 
- 关键写出move(),只要out为空就一股脑移动到in里面去
- time = 0(1) amotized, space = O(n)
```java
public class Solution {
	private LinkedList<Integer> in;
	private LinkedList<Integer> out;
  public Solution() {
    in = new LinkedList<Integer>();
    out = new LinkedList<Integer>();
  }
  //in 
  //out 
  public Integer poll() {
    move();
    return out.isEmpty() ? null : out.pollFirst();
  }
  
  public void offer(int element) {
    in.offerFirst(element);
  }
  
  public Integer peek() {
    move();
    return out.isEmpty() ? null : out.peekFirst();
  }
  
  public int size() {
    return in.size() + out.size();
  }
  
  public boolean isEmpty() {
    return in.isEmpty() && out.isEmpty();//&& 都为空的时候才是空了
  }

  private void move() {
  	if (out.isEmpty()) {
  		while(!in.isEmpty()) {
  			out.offerFirst(in.pollFirst());
  		}
  	}
  }
}
```

## Stack With min()
Enhance the stack implementation to support min() operation. min() should return the current minimum value in the stack. If the stack is empty, min() should return -1.

push(int element) - push the element to top
pop() - return the top element and remove it, if the stack is empty, return -1
top() - return the top element without remove it, if the stack is empty, return -1
min() - return the current min value in the stack.

- 要实现找stack里面的最小值
- stack1 存放input元素
- stack2(minStack) 存放stack1里最小值so far , min取它peekFirst
- 

```java
public class Solution {
	private Deque<Integer> stack;
	private Deque<Integer> minStack;

	public Solution() {
		stack = new LinkedList<Integer>();
		minStack = new LinkedList<Integer>();
	}
	
	public int min() {
		if (minStack.isEmpty()) {
			return -1;
		}
		return minStack.peekFirst();
	}
	
	public void push(int value) { //对于比较小的元素,minStack里面也要存
		stack.offerFirst(value);
		if (minStack.isEmpty() || value <= minStack.peekFirst()) {
			minStack.offerFirst(value);
		}
	}

	public int pop() {
		if (stack.isEmpty()) {
			return -1;
		}
		Integer result = stack.pollFirst();
		if (minStack.peekFirst().equals(result)) {
			minStack.pollFirst();
		}
		return result;
	}

	public int top() {
		if (stack.isEmpty()) {
			return -1;
		}
		return stack.peekFirst();
	}
}
```

## Stack by Queue(s)
Implement a stack containing integers using queue(s). The stack should provide push(x), pop(), top() and isEmpty() operations.

In java: if the stack is empty, then top() and pop() will return null.

In Python: if the stack is empty, then top() and pop() will return None.

In C++:  if the stack is empty, then top() and pop() will return nullptr.

```java
class Solution {
    private Queue<Integer> q1;
    private Queue<Integer> q2;
    /** Initialize your data structure here. */
    public Solution() {
       q1 = new ArrayDeque<>();
       q2 = new ArrayDeque<>();
    }

    /** Push element x onto stack. */
    public void push(int x) {
        q1.offer(x);
    }

    /** Removes the element on top of the stack and returns that element. */
    public Integer pop() {
        Integer prev = q1.poll();
        Integer cur = q1.poll();
        while (cur != null) {
          q2.offer(prev);
          prev = cur;
          cur = q1.poll();
        }
        Queue<Integer> tmp = q1;
        q1 = q2;
        q2 = tmp;
        return prev;
    }

    /** Get the top element. */
    public Integer top() {
        Integer ret = pop();
        if (ret != null) {
          q1.offer(ret);
        }
        return ret;
    }

    /** Returns whether the stack is empty. */
    public boolean isEmpty() {
       return top() == null;
    }
}
```

## Deque By Three Stacks
Java: Implement a deque by using three stacks. The queue should provide size(), isEmpty(), offerFirst(), offerLast(), pollFirst(), pollLast(), peekFirst() and peekLast() operations. When the queue is empty, pollFirst(), pollLast(), peekFirst() and peek() should return null.

// ipad详解

```java
public class Solution { 
	private Deque<Integer> left;
	private Deque<Integer> right;
	private Deque<Integer> buffer;
	
	public Solution() {
		left = new ArrayDeque<>();
		right = new ArrayDeque<>();
		buffer = new ArrayDeque<>();
	}

	public void offerFirst(int element) {
		left.offerFirst(element);
	}

	public void offerLast(int element) {
		right.offerFirst(element);
	}

	public Integer pollFirst() {
		move(right, left);
		return left.isEmpty() ? null : left.pollFirst();
	}

	public Integer pollLast() {
		move(left, right);
		return right.isEmpty() ? null : right.pollFirst();
	}

	public Integer peekFirst() {
		move(right, left);
		return left.isEmpty() ? null : left.peekFirst();
	}

  public Integer peekLast() {
		move(left, right);
		return right.isEmpty() ? null : right.peekFirst();
	}

	public int size() {
		return left.size() + right.size();
	}
	
	public boolean isEmpty() {
		return left.isEmpty() && right.isEmpty();
	}
  	
	private void move(Deque<Integer> src, Deque<Integer> dest) {
		if (!dest.isEmpty()) {
			return;
		}
		int halfSize = src.size() / 2;
		for (int i = 0; i < halfSize; i++) {
			buffer.offerFirst(src.pollFirst());
		}
		while (!src.isEmpty()) {
			dest.offerFirst(src.pollFirst());
		}
		while (!buffer.isEmpty()) {
			src.offerFirst(buffer.pollFirst());
		}
	}
}
```

# 理论

队列是先进先出

![image-20210828085947370](4 Queue & Stack.assets/image-20210828085947370.png)

栈是先进后出

![image-20210828090007132](4 Queue & Stack.assets/image-20210828090007132.png)

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
