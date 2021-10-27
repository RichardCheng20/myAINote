# Knowledge and Reasoning

Knowledge representation(现实问题转换到电脑) 

Logic(agent大脑中的语言) and representation

Propositional (Boolean) logic 

Normal forms 

Inference in propositional logic 

Wumpus world example

----

<img src="../w5%20Knowledge,%20Reasoning%20Propositional%20Logic.assets/image-20211012175244368.png" alt="image-20211012175244368" style="zoom:50%;" />

**Wumpus World Example**

- Deterministic?Yes – **outcome exactly specified**
- Accessible? No – only local perception
- Static?Yes – Wumpus and pits do not move
- Discrete? Yes
- Episodic? (Yes) – because static

<img src="../w5%20Knowledge,%20Reasoning%20Propositional%20Logic.assets/image-20211012181101189.png" alt="image-20211012181101189" style="zoom:50%;" />

 反正就是走一步 然后在那一步左上角写下是否检测到东西

-----

### Logic in General

![image-20211012182154537](../w5%20Knowledge,%20Reasoning%20Propositional%20Logic.assets/image-20211012182154537.png)

### Types of Logic

![image-20211012182359220](../w5%20Knowledge,%20Reasoning%20Propositional%20Logic.assets/image-20211012182359220.png)

## Key Concepts of Logic

 • Syntax • Semantics • Entailment • Inference • Soundness • Completeness • Inference Rules • Normal Forms • Truth Tables • Reasoning

<img src="../w5%20Knowledge,%20Reasoning%20Propositional%20Logic.assets/image-20211012182544392.png" alt="image-20211012182544392" style="zoom:25%;" />



## Entailment |= 包含

KB (“mind”) and Models (“real worlds”)

<img src="../w5%20Knowledge,%20Reasoning%20Propositional%20Logic.assets/image-20211012182819447.png" alt="image-20211012182819447" style="zoom:50%;" />



<img src="../w5%20Knowledge,%20Reasoning%20Propositional%20Logic.assets/image-20211012183306568.png" alt="image-20211012183306568" style="zoom:50%;" />

![image-20211012184241526](../w5%20Knowledge,%20Reasoning%20Propositional%20Logic.assets/image-20211012184241526.png)

KB: G和R都wi,  alpha: G或者R win 

### Inference

![image-20211012185822135](../w5%20Knowledge,%20Reasoning%20Propositional%20Logic.assets/image-20211012185822135.png)

<img src="../w5%20Knowledge,%20Reasoning%20Propositional%20Logic.assets/image-20211012190133485.png" alt="image-20211012190133485" style="zoom:50%;" />

## Propositional Logic: Syntax

![image-20211012190404995](../w5%20Knowledge,%20Reasoning%20Propositional%20Logic.assets/image-20211012190404995.png)

## Propositional Logic: Semantics   (must be checked in real worlds)

![image-20211012190955805](../w5%20Knowledge,%20Reasoning%20Propositional%20Logic.assets/image-20211012190955805.png)

### Truth Tables 

![image-20211012202018656](../w5%20Knowledge,%20Reasoning%20Propositional%20Logic.assets/image-20211012202018656.png)

![image-20211012213747555](../w5%20Knowledge,%20Reasoning%20Propositional%20Logic.assets/image-20211012213747555.png)

------------

### **Tautologies** 一直都是true

<img src="../w5%20Knowledge,%20Reasoning%20Propositional%20Logic.assets/image-20211013084536664.png" alt="image-20211013084536664" style="zoom:50%;" />

### Validity and Satisfiabilit

![image-20211013085920799](../w5%20Knowledge,%20Reasoning%20Propositional%20Logic.assets/image-20211013085920799.png)



### Inference Rules

![image-20211013091106994](../w5%20Knowledge,%20Reasoning%20Propositional%20Logic.assets/image-20211013091106994.png)

![image-20211013091250629](../w5%20Knowledge,%20Reasoning%20Propositional%20Logic.assets/image-20211013091250629.png)

