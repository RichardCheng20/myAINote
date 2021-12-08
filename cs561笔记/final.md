# 1 TF 

![image-20211206141023902](final.assets/image-20211206141023902.png)

![image-20211206141112361](final.assets/image-20211206141112361.png)



![image-20211206190755468](final.assets/image-20211206190755468.png)

![image-20211206190945067](final.assets/image-20211206190945067.png)



![image-20211206191417480](final.assets/image-20211206191417480.png)

![image-20211206191841219](final.assets/image-20211206191841219.png)

![image-20211206194101067](final.assets/image-20211206194101067.png)

![image-20211206194215003](final.assets/image-20211206194215003.png)

![image-20211206195304202](final.assets/image-20211206195304202.png)



![image-20211206195542895](final.assets/image-20211206195542895.png)

![image-20211206195721427](final.assets/image-20211206195721427.png)

![image-20211206202416783](final.assets/image-20211206202416783.png)

![image-20211206202941655](final.assets/image-20211206202941655.png)

![image-20211206203152316](final.assets/image-20211206203152316.png)

![image-20211207103736832](final.assets/image-20211207103736832.png)

Markov blanket of node: D's parents, D's children, D's children's other parents;

Genetic Algorithms can be used to determine the number of hiddent units that combines network's performance and complexity and applyingh mutations to network. 

![image-20211207113145178](final.assets/image-20211207113145178.png)

machine learing: unknown environments, adaptability, lazy, autonomous

Ockham's razor: Bias for simplest hypothesis, finds smallest tree first/fewer hidden units 

Smaller trees allow for more generalization of the concept 

larger trees allow for overfitting to the training data 





# 2 Decision Tree Learning 

## 20 spring 

![image-20211206102624300](final.assets/image-20211206102624300.png)





**Entropy of the decision** = I(electricity consumption) = I(1/2, 1/2) = -1/2log(1/2) - 1/2log(1/2) = 1

**Entropy remaining(remainder)**  分裂之后

  High use

​      / 	\ 

(2l, 2h) (2l, 2h)

R(high use) = 1/2I(1/2, 1/2) +  1/2I(1/2, 1/2) = 1

同理求得R(locaion) = 0.8, R(type) = 0.8

**Information Gain:** 

IG(high) = 1 - 1 = 0; IG(location) = 1 - 0.8 = 0.2 ; IG(type) = 1 - 0.2 = 0.2 

High use of applications can't be chosen to split the dataset because informaion gain is loweset compare to the other 2 attributes

<img src="final.assets/image-20211206175433279.png" alt="image-20211206175433279" style="zoom:50%;" />



![image-20211207112316606](final.assets/image-20211207112316606.png)

# 3 Neural Network 

## 20 spring 



<img src="final.assets/image-20211206104016283.png" alt="image-20211206104016283" style="zoom:50%;" />



1.1 A = 1, B = 0, C = 0

1.2 error = |expected - observed| = |1 - 0| = 1  

 	AC_new = weight_old + alpha * output * error = -0.1 + alpha * 1 * 1 = 1 - 0.1 = 0.9; BC_new = 0 

# 4 Bayesian Network 父子关系

## 20 spring 

<img src="final.assets/image-20211206105337240.png" alt="image-20211206105337240" style="zoom:50%;" />



4a. Find P(B = good, F = not empty, G = empty, S = no) = P(B = good)P(F=not empty)P(G = empty|B = good, F=not empty) P(S=no|B = good, F=not empty)

4b. Use **enumeration** P(S|B = bad) = [P(S = yes|B = bad), P(S = no| B = bad)] 引入fule

P(S = yes|B = bad) = P(S = yes, B = bad) / P(B = bad) = [P(B = bad)P(Fule = empty)P(S = yes| B = bad, F = empty) + P(B = bad)P(Fule = ~empty)P(S = yes| B = bad, F = ~empty)] / P (B = bad) 

![image-20211207120114860](final.assets/image-20211207120114860.png)



![image-20211207161015811](final.assets/image-20211207161015811.png)

# 5 Probability Theory 

<img src="final.assets/image-20211206112000309.png" alt="image-20211206112000309" style="zoom:50%;" />

<img src="final.assets/image-20211206112024220.png" alt="image-20211206112024220" style="zoom:50%;" />

<img src="final.assets/image-20211206112048518.png" alt="image-20211206112048518" style="zoom:50%;" />



![image-20211206205054350](final.assets/image-20211206205054350.png)

# 6 Naive Bayes 

## 20 Spring 

<img src="final.assets/image-20211206112429282.png" alt="image-20211206112429282" style="zoom:50%;" />

<img src="final.assets/image-20211206112624126.png" alt="image-20211206112624126" style="zoom:50%;" />

# 7 MDP 

![image-20211206173833219](final.assets/image-20211206173833219.png)

![image-20211206174056660](final.assets/image-20211206174056660.png)

![image-20211206174451488](final.assets/image-20211206174451488.png)

![image-20211206175113183](final.assets/image-20211206175113183.png)

## 2 work 

![image-20211206222524244](final.assets/image-20211206222524244.png)

![image-20211206224838909](final.assets/image-20211206224838909.png)

## 3 Treasure Hunting 

![image-20211207090906137](final.assets/image-20211207090906137.png)

![image-20211207091115374](final.assets/image-20211207091115374.png)

![image-20211207092609407](final.assets/image-20211207092609407.png)

## 4 trainsition reward 

![image-20211207120756130](final.assets/image-20211207120756130.png)

![image-20211207145715989](final.assets/image-20211207145715989.png)

## 5 Q TD

![image-20211207151140839](final.assets/image-20211207151140839.png)

![image-20211207151202430](final.assets/image-20211207151202430.png)





---

![image-20211207171423937](final.assets/image-20211207171423937.png)

p 152 
