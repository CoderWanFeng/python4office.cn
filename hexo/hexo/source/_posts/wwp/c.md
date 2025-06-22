# c

# C++1.数据类型

## 1.第一个代码分析

![image-20250601143132639](file:///D:/blog/linux.assets/image-20250601143132639.png?lastModify=1750474500)

## 1.数据类型

**定义一个变量或者常量 其实就是开辟了一块不同大小的空间，根据定义的格式来决定空间的大小，然后给这个空间起一个名字，然后在空间里存一个值，如果值的大小超过了空间的大小，就会造成数据的丢失。输出的时候，可以自己定义输出个格式，就是把空间的值给拿出来，然后按照要求来输出，输出的格式跟空间的格式没有关系，因为空间的格式只是为了决定这个空间的大小。**

|类型|大小 (字节)|范围/精度|
| ----| -----------| -------------------------------------------------------|
|​`bool`​|1|true 或 false|
|​`char`​|1|-128 到 127 或 0 到 255|
|​`signed char`​|1|-128 到 127|
|​`unsigned char`​|1|0 到 255|
|​`short`​|2|-32,768 到 32,767|
|​`unsigned short`​|2|0 到 65,535|
|​`int`​|4|-2,147,483,648 到 2,147,483,647|
|​`unsigned int`​|4|0 到 4,294,967,295|
|​`long`​|4 或 8|平台相关|
|​`unsigned long`​|4 或 8|平台相关|
|​`long long`​|8|-9,223,372,036,854,775,808 到 9,223,372,036,854,775,807|
|​`unsigned long long`​|8|0 到 18,446,744,073,709,551,615|
|​`float`​|4|约 7 位十进制数字精度|
|​`double`​|8|约 15 位十进制数字精度|
|​`long double`​|8, 12 或 16|平台相关，更高精度|

1 字节 (Byte, B) \= 8 位 (bit)1 KB (Kilobyte) \= 1024 B1 MB (Megabyte) \= 1024 KB1 GB (Gigabyte) \= 1024 MB1 TB (Terabyte) \= 1024 GB

### **1 变量和常量**

#### 1.1 关键字

![image-20250601144123446](file:///D:/blog/linux.assets/image-20250601144123446.png?lastModify=1750474500)

#### 1.2 变量

![image-20250601144914872](file:///D:/blog/linux.assets/image-20250601144914872.png?lastModify=1750474500)

### 2.整形和变量的定义和输出

![image-20250601150416007](file:///D:/blog/linux.assets/image-20250601150416007.png?lastModify=1750474500)

### 3.整形的输入

![image-20250601151424446](file:///D:/blog/linux.assets/image-20250601151424446.png?lastModify=1750474500)

scanf 是不安全的，如果不按照要求格式输入就会造成溢出，但是也会接受，但是数据就会丢失部分，所以有可能报错

### 4. short int long longlong

![image-20250601151707319](file:///D:/blog/linux.assets/image-20250601151707319.png?lastModify=1750474500)

### 输出![image-20250601152124130](file:///D:/blog/linux.assets/image-20250601152124130.png?lastModify=1750474500)

![image-20250601170321874](file:///D:/blog/linux.assets/image-20250601170321874.png?lastModify=1750474500)

![image-20250602145328688](file:///D:/blog/linux.assets/image-20250602145328688.png?lastModify=1750474500)

![image-20250602150202248](file:///D:/blog/linux.assets/image-20250602150202248.png?lastModify=1750474500)

### 输入

![image-20250602151022130](file:///D:/blog/linux.assets/image-20250602151022130.png?lastModify=1750474500)

### 5.字符型

**chor 存储是以 ascii 码形式存储**

## 2.关键字 sizeof

![image-20250601152348590](file:///D:/blog/linux.assets/image-20250601152348590.png?lastModify=1750474500)

## 3.转义字符

![image-20250601162545782](file:///D:/blog/linux.assets/image-20250601162545782.png?lastModify=1750474500)

## 4.浮点数

![image-20250601163125470](file:///D:/blog/linux.assets/image-20250601163125470.png?lastModify=1750474500)

单精度 4 个字节 双精度 8 个字节

## 5.类型限定符

![image-20250601164757664](file:///D:/blog/linux.assets/image-20250601164757664.png?lastModify=1750474500)

![image-20250601164807966](file:///D:/blog/linux.assets/image-20250601164807966.png?lastModify=1750474500)

‍

‍

# 2.运算符

## 1.算数运算符

![image-20250602160012552](file:///D:/blog/linux.assets/image-20250602160012552.png?lastModify=1750474500)

## 2.逻辑运算符

![image-20250602162200431](file:///D:/blog/linux.assets/image-20250602162200431.png?lastModify=1750474500)

## 3.运算符优先级

![image-20250602162250281](file:///D:/blog/linux.assets/image-20250602162250281.png?lastModify=1750474500)

**多个运算符的时候建议用（）括起来，可读性更高 逻辑更清晰**

## 4. 类型转换

![image-20250602163607051](file:///D:/blog/linux.assets/image-20250602163607051.png?lastModify=1750474500)

## 5.条件判断 if

![image-20250602164446914](file:///D:/blog/linux.assets/image-20250602164446914.png?lastModify=1750474500)

## 6.三目运算符

![image-20250602171830597](file:///D:/blog/linux.assets/image-20250602171830597.png?lastModify=1750474500)

**满足下 x&gt;y 返回 x 否则返回 y**

![image-20250602172136806](file:///D:/blog/linux.assets/image-20250602172136806.png?lastModify=1750474500)

**嵌套**

## 7.switch

![image-20250603152010680](file:///D:/blog/linux.assets/image-20250603152010680.png?lastModify=1750474500)

## 8.while

![image-20250603153457884](file:///D:/blog/linux.assets/image-20250603153457884.png?lastModify=1750474500)

## 9. do while

![image-20250603153520959](file:///D:/blog/linux.assets/image-20250603153520959.png?lastModify=1750474500)

## 10.for 循环

![image-20250603154118627](file:///D:/blog/linux.assets/image-20250603154118627.png?lastModify=1750474500)

## 11.跳转语句

### 1.continue

![image-20250603155245354](file:///D:/blog/linux.assets/image-20250603155245354.png?lastModify=1750474500)

### 2.break

![image-20250603155757321](file:///D:/blog/linux.assets/image-20250603155757321.png?lastModify=1750474500)

**break 只跳出离它最近的一层循环；break 只能在 switch 和循环中使用**

### 3.goto

![image-20250603160627774](file:///D:/blog/linux.assets/image-20250603160627774.png?lastModify=1750474500)

## 12.数组

![image-20250603160909416](file:///D:/blog/linux.assets/image-20250603160909416.png?lastModify=1750474500)

![image-20250603165105360](file:///D:/blog/linux.assets/image-20250603165105360.png?lastModify=1750474500)

### 12.1 一维数组的初始化

![image-20250603164806179](file:///D:/blog/linux.assets/image-20250603164806179.png?lastModify=1750474500)

![image-20250603165455416](file:///D:/blog/linux.assets/image-20250603165455416.png?lastModify=1750474500)

### 12.2 二维数组初始化

![image-20250605153520573](file:///D:/blog/linux.assets/image-20250605153520573.png?lastModify=1750474500)

![image-20250605154013773](file:///D:/blog/linux.assets/image-20250605154013773.png?lastModify=1750474500)

![image-20250605154237885](file:///D:/blog/linux.assets/image-20250605154237885.png?lastModify=1750474500)

### 12.3 字符数组和字符串的区别

![image-20250605155418249](file:///D:/blog/linux.assets/image-20250605155418249.png?lastModify=1750474500)

## 13.字符串的输入输出

![image-20250605163734741](file:///D:/blog/linux.assets/image-20250605163734741.png?lastModify=1750474500)

![image-20250605165115974](file:///D:/blog/linux.assets/image-20250605165115974.png?lastModify=1750474500)

**fgets 可以指定接受到数据的大小，并且会接收换行的转义字符，如果打印的话 还会进行换行，并别\n 会占一个元素，而且指定接收大小的时候，会少接收一位，因为要自动补一个’\0‘，作为字符串的结束**

**前两个不安全，超出范围会报错，fgets 超出范围不会报错，但是只会接收规定范围的数据，超出的不接收。**

![image-20250605171408119](file:///D:/blog/linux.assets/image-20250605171408119.png?lastModify=1750474500)

![image-20250605171735616](file:///D:/blog/linux.assets/image-20250605171735616.png?lastModify=1750474500)

### 13.1 字符串的拼接

![image-20250605172523145](file:///D:/blog/linux.assets/image-20250605172523145.png?lastModify=1750474500)

## 14.函数

### 14.1 函数的构造

![image-20250607183350599](file:///D:/blog/linux.assets/image-20250607183350599.png?lastModify=1750474500)

### 14.2 函数声明 和 exit 函数

![image-20250607190513945](file:///D:/blog/linux.assets/image-20250607190513945.png?lastModify=1750474500)

### 14.3 分文件编程

![image-20250607191145451](file:///D:/blog/linux.assets/image-20250607191145451.png?lastModify=1750474500)

### 14.4 防止头文件重复包涵

![image-20250607191405264](file:///D:/blog/linux.assets/image-20250607191405264.png?lastModify=1750474500)

![image-20250607191818393](file:///D:/blog/linux.assets/image-20250607191818393.png?lastModify=1750474500)

## 15.指针

![image-20250619161037987](file:///D:/blog/linux.assets/image-20250619161037987.png?lastModify=1750474500)

### 15.1 含义

**指针本质就是指的是内存地址；**

**指针变量指的是存储内存地址的变量；**

### 15.2 p 和 **p*

![image-20250608163729285](linux.assets/image-20250608163729285.png

![image-20250608163812832](file:///D:/blog/linux.assets/image-20250608163812832.png?lastModify=1750474500)

### 15.3 万能指针

![image-20250608165834305](file:///D:/blog/linux.assets/image-20250608165834305.png?lastModify=1750474500)

### 15.4 const 修饰的指针

![image-20250608171735057](file:///D:/blog/linux.assets/image-20250608171735057.png?lastModify=1750474500)

**前后都有 const 两个都不能改 p**  ***** p **都不能改**

### 15.5 指针操作数组

![image-20250608175658331](file:///D:/blog/linux.assets/image-20250608175658331.png?lastModify=1750474500)

## 16.字符串处理函数

### 16.1 复制

![image-20250610152014687](file:///D:/blog/linux.assets/image-20250610152014687.png?lastModify=1750474500)

**注意：会覆盖原来的内容**

![image-20250610152142382](file:///D:/blog/linux.assets/image-20250610152142382.png?lastModify=1750474500)

### 16.2 拼接

![image-20250610152829546](file:///D:/blog/linux.assets/image-20250610152829546.png?lastModify=1750474500)

![image-20250610152844623](file:///D:/blog/linux.assets/image-20250610152844623.png?lastModify=1750474500)

### 16.3 比大小

![image-20250610153949553](file:///D:/blog/linux.assets/image-20250610153949553.png?lastModify=1750474500)

![image-20250610154135873](file:///D:/blog/linux.assets/image-20250610154135873.png?lastModify=1750474500)

### 16.4 按指定格式输出输入

![image-20250610154447824](file:///D:/blog/linux.assets/image-20250610154447824.png?lastModify=1750474500)

![image-20250610154600822](file:///D:/blog/linux.assets/image-20250610154600822.png?lastModify=1750474500)

### 16.5 寻找

![image-20250610155410056](file:///D:/blog/linux.assets/image-20250610155410056.png?lastModify=1750474500)

![image-20250610155443734](file:///D:/blog/linux.assets/image-20250610155443734.png?lastModify=1750474500)

### 16.6 分割

![image-20250610160145787](file:///D:/blog/linux.assets/image-20250610160145787.png?lastModify=1750474500)

**while 循环里 第一次分割需要传首地址，后面传 NULL 就可以**

### 16.7 转型

![image-20250610160430531](file:///D:/blog/linux.assets/image-20250610160430531.png?lastModify=1750474500)

![image-20250610163507232](file:///D:/blog/linux.assets/image-20250610163507232.png?lastModify=1750474500)

![image-20250610163546908](file:///D:/blog/linux.assets/image-20250610163546908.png?lastModify=1750474500)

![image-20250610163529270](file:///D:/blog/linux.assets/image-20250610163529270.png?lastModify=1750474500)

![image-20250610163421125](file:///D:/blog/linux.assets/image-20250610163421125.png?lastModify=1750474500)

## 17.静态变量 static 和全局变量

![image-20250611100512543](file:///D:/blog/linux.assets/image-20250611100512543.png?lastModify=1750474500)

### 17.1 全局变量

![image-20250611101715496](file:///D:/blog/linux.assets/image-20250611101715496.png?lastModify=1750474500)

![image-20250611101727604](file:///D:/blog/linux.assets/image-20250611101727604.png?lastModify=1750474500)

### 17.2 全局函数和静态函数

**和变量是一样的**

![image-20250611103639674](file:///D:/blog/linux.assets/image-20250611103639674.png?lastModify=1750474500)

## 18 内存布局

![image-20250611110124223](file:///D:/blog/linux.assets/image-20250611110124223.png?lastModify=1750474500)

**eg：**

![image-20250611110425778](file:///D:/blog/linux.assets/image-20250611110425778.png?lastModify=1750474500)

![image-20250611110450114](file:///D:/blog/linux.assets/image-20250611110450114.png?lastModify=1750474500)

![image-20250611111130896](file:///D:/blog/linux.assets/image-20250611111130896.png?lastModify=1750474500)

### 18.1 内存操作函数

![image-20250611113715352](file:///D:/blog/linux.assets/image-20250611113715352.png?lastModify=1750474500)

![image-20250611113809665](file:///D:/blog/linux.assets/image-20250611113809665.png?lastModify=1750474500)

**现在版本这个重叠问题已经解决**

![image-20250611113849132](file:///D:/blog/linux.assets/image-20250611113849132.png?lastModify=1750474500)

**memmove 就是用来解决 memcpy 的重叠问题的，现在一般不用了**

![image-20250611113941892](file:///D:/blog/linux.assets/image-20250611113941892.png?lastModify=1750474500)

## 19 结构体

![image-20250612144712200](file:///D:/blog/linux.assets/image-20250612144712200.png?lastModify=1750474500)

## 19.1 结构体成员的使用

![image-20250612150229833](file:///D:/blog/linux.assets/image-20250612150229833.png?lastModify=1750474500)

![image-20250612155040765](file:///D:/blog/linux.assets/image-20250612155040765.png?lastModify=1750474500)

**字符串赋值的时候 如果是初始化结构体时可以直接赋值，以外赋值或者修改都要从 strcpy**

eg：

```
struct Person {
    char name[50];
    int age;
};

int main() {
    struct Person p = {"张三", 25};  // 仅限初始化时使用= 
    return 0;
}
```

```
#include <string.h>

struct Person {
    char name[50];
    int age;
};

int main() {
    struct Person p;
    strcpy(p.name, "张三");  // 正确：将字符串复制到数组中
    p.age = 25;
    return 0;
}
```

### 19.2 结构体和指针

![image-20250614143928805](file:///D:/blog/linux.assets/image-20250614143928805.png?lastModify=1750474500)

![image-20250614144139971](file:///D:/blog/linux.assets/image-20250614144139971.png?lastModify=1750474500)

![image-20250614144430281](file:///D:/blog/linux.assets/image-20250614144430281.png?lastModify=1750474500)

![image-20250614150723465](file:///D:/blog/linux.assets/image-20250614150723465.png?lastModify=1750474500)

## 20.共用体 联合体

![image-20250614151756694](file:///D:/blog/linux.assets/image-20250614151756694.png?lastModify=1750474500)

![image-20250614151813150](file:///D:/blog/linux.assets/image-20250614151813150.png?lastModify=1750474500)

![image-20250614151823223](file:///D:/blog/linux.assets/image-20250614151823223.png?lastModify=1750474500)

***补充***![image-20250614152501780](file:///D:/blog/linux.assets/image-20250614152501780.png?lastModify=1750474500)

## 21.枚举

![image-20250614153031630](file:///D:/blog/linux.assets/image-20250614153031630.png?lastModify=1750474500)

![image-20250614153104163](file:///D:/blog/linux.assets/image-20250614153104163.png?lastModify=1750474500)

## 22.typedef

![image-20250614155424146](file:///D:/blog/linux.assets/image-20250614155424146.png?lastModify=1750474500)

‍

‍

# 23.文件操作

***perror***​**函数是一个用于错误处理的库函数，它的作用是将上一个函数发生错误的原因输出到标准错误输出（stderr）。**

## 1. 概述

![image-20250614160856318](file:///D:/blog/linux.assets/image-20250614160856318.png?lastModify=1750474500)

## 2. 文件的打开

![image-20250614161545244](file:///D:/blog/linux.assets/image-20250614161545244.png?lastModify=1750474500)

![image-20250614161722112](file:///D:/blog/linux.assets/image-20250614161722112.png?lastModify=1750474500)

![image-20250614161917148](file:///D:/blog/linux.assets/image-20250614161917148.png?lastModify=1750474500)

![image-20250614163026569](file:///D:/blog/linux.assets/image-20250614163026569.png?lastModify=1750474500)

## 3.文件关闭

![image-20250614163258804](file:///D:/blog/linux.assets/image-20250614163258804.png?lastModify=1750474500)

## 4.按照字符读写文件

![image-20250614164110773](file:///D:/blog/linux.assets/image-20250614164110773.png?lastModify=1750474500)

![image-20250614164313686](file:///D:/blog/linux.assets/image-20250614164313686.png?lastModify=1750474500)

**以字节的方式读文件**

![image-20250615092930541](file:///D:/blog/linux.assets/image-20250615092930541.png?lastModify=1750474500)

![image-20250615093005824](file:///D:/blog/linux.assets/image-20250615093005824.png?lastModify=1750474500)

## 5.按照行来读写文件

![image-20250615094612016](file:///D:/blog/linux.assets/image-20250615094612016.png?lastModify=1750474500)

**fgets**

![image-20250615095231061](file:///D:/blog/linux.assets/image-20250615095231061.png?lastModify=1750474500)

**memset 是为了把 buf 里面的数据清空，防止后面写进去后读操作时读取到旧的数据.**

## 训练

```
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

int main()
{
    FILE* fp = NULL;
    fp = fopen("a.txt", "w");
    if (fp == NULL)
    {
        perror("fopen");
        return -1;
    }
    srand(time(NULL));
    int n = rand() % 10;
    char buf[100] = { 0 };
    char opt[4] = { '+','-','*','/' };
    int a, b;
    char ch;
    for (int i = 0; i < n; i++)
    {
        a = rand() % 10;
        b = rand() % 10;
        ch =opt[ rand() % 4];
        sprintf(buf, "%d%c%d=\n", a, ch, b);
        puts(buf);
        fputs(buf, fp);
    }
fclose(fp);
return 0;
```

}

## 6.按照格式化 读写文件

![image-20250615193317581](file:///D:/blog/linux.assets/image-20250615193317581.png?lastModify=1750474500)

**读文件**

![image-20250615193330756](file:///D:/blog/linux.assets/image-20250615193330756.png?lastModify=1750474500)

**读取的时候，需要用变量来接收**

![image-20250615194542696](file:///D:/blog/linux.assets/image-20250615194542696.png?lastModify=1750474500)

## 7.按照块读写文件

![image-20250616104329562](file:///D:/blog/linux.assets/image-20250616104329562.png?lastModify=1750474500)

![image-20250616104455168](file:///D:/blog/linux.assets/image-20250616104455168.png?lastModify=1750474500)

## 8.文件的随机读写

![image-20250616110448520](file:///D:/blog/linux.assets/image-20250616110448520.png?lastModify=1750474500)

![image-20250616111638152](file:///D:/blog/linux.assets/image-20250616111638152.png?lastModify=1750474500)

## 9.获取文件信息

![image-20250616112629887](file:///D:/blog/linux.assets/image-20250616112629887.png?lastModify=1750474500)

![image-20250616112703272](file:///D:/blog/linux.assets/image-20250616112703272.png?lastModify=1750474500)

**将文件的信息保存在一个结构体内**

![image-20250616112757703](file:///D:/blog/linux.assets/image-20250616112757703.png?lastModify=1750474500)

## 10.删除文件和更改文件名字

![image-20250616114405429](file:///D:/blog/linux.assets/image-20250616114405429.png?lastModify=1750474500)

‍

‍

# c 高级

## void

![image-20250619142734363](file:///D:/blog/linux.assets/image-20250619142734363.png?lastModify=1750474500)

## sizeof

![image-20250619143317228](file:///D:/blog/linux.assets/image-20250619143317228.png?lastModify=1750474500)

![image-20250619143638100](file:///D:/blog/linux.assets/image-20250619143638100.png?lastModify=1750474500)

![image-20250619143929079](file:///D:/blog/linux.assets/image-20250619143929079.png?lastModify=1750474500)

## 指针 堆栈

![image-20250619150208022](file:///D:/blog/linux.assets/image-20250619150208022.png?lastModify=1750474500)

![image-20250619152753799](file:///D:/blog/linux.assets/image-20250619152753799.png?lastModify=1750474500)

## const 修饰常量

![image-20250619164123083](file:///D:/blog/linux.assets/image-20250619164123083.png?lastModify=1750474500)

**const 修饰的全局常量 直接和间接修改都不能保护，因为是在常量区中**

**const 修饰的局部变量，不能直接修改  间接可以修改，因为实在栈中，不受保护，是一个伪常量**

## 字符常量

![image-20250619164456792](file:///D:/blog/linux.assets/image-20250619164456792.png?lastModify=1750474500)

![image-20250619164713787](file:///D:/blog/linux.assets/image-20250619164713787.png?lastModify=1750474500)

## 宏

![image-20250620110205470](file:///D:/blog/linux.assets/image-20250620110205470.png?lastModify=1750474500)

![image-20250620110402152](file:///D:/blog/linux.assets/image-20250620110402152.png?lastModify=1750474500)

![image-20250620111331226](file:///D:/blog/linux.assets/image-20250620111331226.png?lastModify=1750474500)

![image-20250620111653585](file:///D:/blog/linux.assets/image-20250620111653585.png?lastModify=1750474500)

![image-20250620111958460](file:///D:/blog/linux.assets/image-20250620111958460.png?lastModify=1750474500)

## 指针

![image-20250620112406382](file:///D:/blog/linux.assets/image-20250620112406382.png?lastModify=1750474500)![image-20250620112449791](file:///D:/blog/linux.assets/image-20250620112449791.png?lastModify=1750474500)

![image-20250620112613418](file:///D:/blog/linux.assets/image-20250620112613418.png?lastModify=1750474500)

![image-20250620112721371](file:///D:/blog/linux.assets/image-20250620112721371.png?lastModify=1750474500)

![image-20250620140442749](file:///D:/blog/linux.assets/image-20250620140442749.png?lastModify=1750474500)

## 字符串指针强化

![image](assets/image-20250621143736-0droe0s.png)

**或者设置数组的元素个数多一点，会自动加一个    ‘\0’**

![image](assets/image-20250621143930-0fjryb0.png)

答案  6   5

**strlen 统计的时候不算上‘\0’**

![image](assets/image-20250621144035-2xwyioh.png)

strof 统计的是整个数组的长度

答案  100    5

![image](assets/image-20250621162937-hlh6qat.png)

‍

![image](assets/image-20250621163345-d7v3lbd.png)

### 字符串函数

**赋值的操作 注释是例子 把 while 里 a=0 改成 1 运行两次看结果来理解这个操作**

![image](assets/image-20250621164112-y7c9xer.png)

### **用指针方式实现反转**

![image](assets/image-20250621172825-6q0crgn.png)

### 格式化 sprintf

![image](assets/image-20250621173422-ncowhh0.png)

![image](assets/image-20250621173601-kvf2juc.png)

![image](assets/image-20250621173626-clsnc5f.png)

![image](assets/image-20250621173749-wjzp4tg.png)

### 堆

![image](assets/image-20250621175728-rc5xlbb.png)

**和 malloc 唯一的区别会自动把内容内容初始化为 0；**

![image](assets/image-20250621180030-fyhvsnm.png)

**realloc 是重新分配空间是用的**

‍

‍

### 格式化 sscanf

![image](assets/image-20250621181736-2gseknz.png)

忽略某种类型的字符 遇到空格和 \t 和第一个非该字符 会结束忽略   **注：**​**<u>非</u>**​**常不好用**

‍

‍

‍

![image](assets/image-20250621181926-tdvtktv.png)

![image](assets/image-20250621182033-sim1rut.png)

**这个也不好用，匹配到第一个非范围内的字符就会停止 可以搭配忽略来用**   ![image](assets/image-20250621182234-55rpy9l.png)

‍

‍

![image](assets/image-20250621182343-0rj7m8k.png)

‍

‍

‍

‍

![image](assets/image-20250621182506-9u630jr.png) ![image](assets/image-20250621182613-qrqmyqo.png)

**匹配到第一个设定的字符就停止**

‍

‍

### 容易出错的点

![image](assets/image-20250622105224-1k1c1gf.png)

**指针偏移后 在释放指针 不会把前面的空间释放了 会报错**

**这种可以定义一个临时指针指向原指针，代替原指针进行操作，最后释放原指针就行了**

‍

‍

![image](assets/image-20250622105403-syemb39.png)

**将局部变量返回并调用，会乱码，因为局部变量在函数结束时就释放掉了**

‍

‍

### const

![image](assets/image-20250622113019-uwg2n8f.png)
