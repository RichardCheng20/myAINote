v ^ ~ (ex) (all) => 

# T/F

![image-20211026214949869](w6%20The%20First-Order%20Logic.assets/image-20211026214949869.png)

 Successor-state axioms solve the representational frame problem. 

![image-20211026220929365](w6%20The%20First-Order%20Logic.assets/image-20211026220929365.png)

![image-20211027001507758](w6%20The%20First-Order%20Logic.assets/image-20211027001507758.png)

![image-20211027122231046](w6%20The%20First-Order%20Logic.assets/image-20211027122231046.png)

a. Entailment must be checked in the real worlds.      

b. Inheritance  and Generalized modus ponens  are sound 

closed world assumption helps to address this problem:  Frame problem  

 b. Entailment can be checked by truth tables because truth tables divide all possible worlds into groups. 

 d. The best inference procedures should be sound and complete.     

 e. A conclusion derived from a sound inference procedure is consistent with entailment. 

 a. The first-order logic **cannot represent propositions** while propositional logic can 

e. Propositional logic can represent relationships between objects 

For **every sentence** in First-Order Logic and Propositional Logic, there exists an inferentially equivalent conjunctive normal form (CNF) sentence.

 Resolution is a sound and complete inference procedure for both Propositional Logic and First-Order Logic that amounts to proof by contradiction.

6. Every first-order knowledge base can be propositionalized.

7. Totally ordered plans are created by a search through the **space** of **plans** rather than through the state space.

8. Prolog has traded soundness for efficiency by:  Having no Occurs-Check, use backchaining, incomplete, not sound 

9.   Cyc is an example application of a knowledge engineering.

10. backward chaining: not complete due to infinite loops. When a loop is detected, suspend the loop branch and try other branches until getting this subgoal or no solution.

    Entailment is semidecidable: Algorithms exist that return YES to every entailed sentence, but no algorithm exists that also returns NO to every nonentailed sentence

# propositional Logic 10' 没有quantifier

1.  It is raining **if and only** if Lion is sick  

   R **<=>** S

2.  Lion either likes to eat or sleep 

   (E ^ ~S) v (~E ^ S)

   











# Frist-Order logic 20' 

就是根据英语写成fo, 送分

##  Logic Translation

1. **No** fish can walk 

~(ex x) Fish(x) => Walk 

2.  Sarah owns **exactly two** red cars. 

**(Ex)**x **(ex)** y Car(x) ^ Car(y) ^ Red(x) ^ Red(y) ^ Owns(Sarah, x) ^ Owns(Sarah, y) ^ **~(x = y)** ^ **(all) z** Car(z) ^ Red(z) ^ Owns(Sarah, z) => (z = x V z = y)

3.  **Some** people always complain.

**(ex) x** (all) t  Person(x) ^ Time(t) => Complain(x,t)

4. Students who attended all lectures find this test easy. 

(all) x (all) y Stuendent(x) ^ Lecture(y) ^ Attends(x, y) => FindsEasy(x, ThisTest)

5. Everyone who watches all the people is watched by someone. 

(all) x (all) y Person(x) ^ Person(y) ^ Watches(x, y) => (ex) z Person(z) ^ Watches(z, x)

6. Everyone who owns **a dog or a cat** is sweet. 

(all) x **(ex) y,z** Cat(y) ^ Dog(z) ^ (Owns(x, y) V Owns(x, z)) => Sweet(x)

7. Not all dogs are both sweet and cute. 

   '~(	(all) x Dog(x) => Sweet(x) ^ Cute(x)	)'

8. A person who loves all cats owns **at least 3 cats**. 当成刚好存在三只处理

(ex) x (all) y Cat(y) ^ Loves(x, y) => (ex) a, b, c Cat(a) ^ Cat(b) ^ Cat(c) ^ ~ (a = b = c) ^ Owns(x, a) ^ Owns(x, b) ^ Owns(x, c)

9. There is exactly one cook who assigns work to all other cooks

10. Every student takes at least two courses in each semester.

    `(all) x, z (( Student(x) ^ Semester(z)	)=> (ex)y,t (Course(y)^Takes(x,y,z)^Course(t)^Takes(x,t,z) ^ y = t)	)`

11. 

![image-20211027084054169](w6%20The%20First-Order%20Logic.assets/image-20211027084054169.png)



 ![image-20211026231954238](w6%20The%20First-Order%20Logic.assets/image-20211026231954238.png)

10. People do not complain about anyone when they wait for their lover.

(all) x (all) y Waits(x, Lover(x)) => ~Complain(x, y) 

11.  Everyone is happy to be their lover’s lover.

(all) x x = Lover(Lover(x)) => Happy(x)

![image-20211027120919308](w6%20The%20First-Order%20Logic.assets/image-20211027120919308.png)

#  Convert to CNF 

![image-20211026201936753](w6%20The%20First-Order%20Logic.assets/image-20211026201936753.png)

![image-20211026223527129](w6%20The%20First-Order%20Logic.assets/image-20211026223527129.png)



![image-20211027085601380](w6%20The%20First-Order%20Logic.assets/image-20211027085601380.png)

![image-20211027085641605](w6%20The%20First-Order%20Logic.assets/image-20211027085641605.png)

![image-20211027095906318](w6%20The%20First-Order%20Logic.assets/image-20211027095906318.png)

# Inference 30' 

## 使用resolution证明

### Propositional inference

p logic 没有quantifiers, FOL talks about rules, it is involved with objects, relations, properties, functions. 

![image-20211026201634022](w6%20The%20First-Order%20Logic.assets/image-20211026201634022.png)

![image-20211026232428425](w6%20The%20First-Order%20Logic.assets/image-20211026232428425.png)

![image-20211027000129441](w6%20The%20First-Order%20Logic.assets/image-20211027000129441.png)



![image-20211027090302143](w6%20The%20First-Order%20Logic.assets/image-20211027090302143.png)



1. 公式

![image-20211026231431119](w6%20The%20First-Order%20Logic.assets/image-20211026231431119.png)

![image-20211026231500878](w6%20The%20First-Order%20Logic.assets/image-20211026231500878.png)

![image-20211026231622642](w6%20The%20First-Order%20Logic.assets/image-20211026231622642.png)



### Prove resolution algorithm that: John likes peanuts 

![image-20211026214322514](w6%20The%20First-Order%20Logic.assets/image-20211026214322514.png)

先转化为CNF ,然后否定结论, 通过结论和之前的kb进行resolution, 注意**有替换**, 两者结合出现替换

![image-20211026214738180](w6%20The%20First-Order%20Logic.assets/image-20211026214738180.png)



## Caesar

![image-20211027104958183](w6%20The%20First-Order%20Logic.assets/image-20211027104958183.png)

![image-20211027105112982](w6%20The%20First-Order%20Logic.assets/image-20211027105112982.png)





# Planning 20'

Action 

Precondition 

Effect 

![image-20211026224226958](w6%20The%20First-Order%20Logic.assets/image-20211026224226958.png)

![image-20211026224320739](w6%20The%20First-Order%20Logic.assets/image-20211026224320739.png)



![image-20211026224452320](w6%20The%20First-Order%20Logic.assets/image-20211026224452320.png)

![image-20211026224621466](w6%20The%20First-Order%20Logic.assets/image-20211026224621466.png)



## 马

![image-20211026233633514](w6%20The%20First-Order%20Logic.assets/image-20211026233633514.png)

![image-20211026233653446](w6%20The%20First-Order%20Logic.assets/image-20211026233653446.png)

![image-20211026233820228](w6%20The%20First-Order%20Logic.assets/image-20211026233820228.png)

## 颜料

![image-20211027091018466](w6%20The%20First-Order%20Logic.assets/image-20211027091018466.png)

## Block

![image-20211027101907151](w6%20The%20First-Order%20Logic.assets/image-20211027101907151.png)

![image-20211027101955678](w6%20The%20First-Order%20Logic.assets/image-20211027101955678.png)



![image-20211027124227943](w6%20The%20First-Order%20Logic.assets/image-20211027124227943.png)

![image-20211027124339721](w6%20The%20First-Order%20Logic.assets/image-20211027124339721.png)

![image-20211027124657654](w6%20The%20First-Order%20Logic.assets/image-20211027124657654.png)

## 飞机地球

![image-20211027111850121](w6%20The%20First-Order%20Logic.assets/image-20211027111850121.png)



![image-20211027112552829](w6%20The%20First-Order%20Logic.assets/image-20211027112552829.png)



## 放AB到桶里

![image-20211027114302965](w6%20The%20First-Order%20Logic.assets/image-20211027114302965.png)



## 猴子

![image-20211027125326551](w6%20The%20First-Order%20Logic.assets/image-20211027125326551.png)

![image-20211027125549748](w6%20The%20First-Order%20Logic.assets/image-20211027125549748.png)

## Forward-Chaining

Example:

**"As per the law, it is a crime for an American to sell weapons to hostile nations. Country A, an enemy of America, has some missiles, and all the missiles were sold to it by Robert, who is an American citizen."**

Prove that **"Robert is criminal."**

![image-20211023164627272](w6%20The%20First-Order%20Logic.assets/image-20211023164627272.png)

Step1: 从下面已知的然后一个一个往上推, 这个过程中没有变量替换,直接可以通过 **American(Robert), Enemy(A, America), Owns(A, T1), and Missile(T1)**. do not have implications,往上 ![image-20211023170354390](w6%20The%20First-Order%20Logic.assets/image-20211023170354390.png)



Step2: Rule-(4) satisfy with the substitution {p/T1}, **so Sells (Robert, T1, A)** is added, which infers from the conjunction of Rule (2) and (3).Rule-(6) is satisfied with the substitution(p/A), so Hostile(A) is added and which infers from Rule-(7).

![image-20211023170613821](w6%20The%20First-Order%20Logic.assets/image-20211023170613821.png)

Step3: Rule-(1) is satisfied with the substitution **{p/Robert, q/T1, r/A}, so we can add Criminal(Robert)**

![image-20211023170723339](w6%20The%20First-Order%20Logic.assets/image-20211023170723339.png)



![image-20211027084657096](w6%20The%20First-Order%20Logic.assets/image-20211027084657096.png)



![image-20211027084713193](w6%20The%20First-Order%20Logic.assets/image-20211027084713193.png)

![image-20211027085341976](w6%20The%20First-Order%20Logic.assets/image-20211027085341976.png)

## Backward-Chaining proof:

In Backward chaining, we will **start with our goal predicate,** which is **Criminal(Robert)**, and then infer further rules.

Step1: At the first step, we will **take the goal fact.** And from the goal fact, we will infer other facts, and at last, we will prove those facts true. 
![image-20211023170854706](w6%20The%20First-Order%20Logic.assets/image-20211023170854706.png)

**Step-2:** infer other facts form goal fact which satisfies the rules.从结论往前推, 结论里的实例代替变量

![image-20211023171022086](w6%20The%20First-Order%20Logic.assets/image-20211023171022086.png)

**Step-3:**t At step-3, we will extract further fact Missile(q) 

![image-20211023171224837](w6%20The%20First-Order%20Logic.assets/image-20211023171224837.png)

Step4:  substitution of A in place of r

![image-20211023171407722](w6%20The%20First-Order%20Logic.assets/image-20211023171407722.png)

**Step-5:**infer the fact **Enemy(A, America)** from **Hostile(A)** which satisfies Rule- 6. 

![image-20211023171507291](w6%20The%20First-Order%20Logic.assets/image-20211023171507291.png)

- Forward chaining can be used for tasks such as **planning, design process monitoring, diagnosis, and classification**, whereas backward chaining can be used for **classification and diagnosis tasks**.

![image-20211027100341968](w6%20The%20First-Order%20Logic.assets/image-20211027100341968.png)

 

![image-20211027113802852](w6%20The%20First-Order%20Logic.assets/image-20211027113802852.png)

##  

![image-20211027130505660](w6%20The%20First-Order%20Logic.assets/image-20211027130505660.png)





