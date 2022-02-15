还没做！！！ 

#### [136. 只出现一次的数字](https://leetcode-cn.com/problems/single-number/)

![image-20220119210809762](10%20Bi%20Representation%20&%20Operation.assets/image-20220119210809762.png)

```java
class Solution {
    public int singleNumber(int[] nums) {
        int single = 0;
        for (int num : nums) {
            single ^= num;
        }
        return single;
    }
}
```



#### [287. 寻找重复数](https://leetcode-cn.com/problems/find-the-duplicate-number/)

![image-20220124144711508](10%20Bi%20Representation%20&%20Operation.assets/image-20220124144711508.png)
