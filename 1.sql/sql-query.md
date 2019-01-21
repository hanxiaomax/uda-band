# SQL 基础


## 数据库与 ERD 表示法
在 Parch & Posey 数据库中，共有五个表（基本上是 5 个电子表格）:

1. web_events
2. accounts
3. orders
4. sales_reps
5. region

["crow's foot" 表示法](https://www.vertabelo.com/blog/technical-articles/crow-s-foot-notation)

## SQL 是什么？

1. SQL 与电子表格
2. SQL 与 NoSQL
3. 为什么需要数据库
  - 只有输入了需要输入的数据，以及只有某些用户能够将数据输入数据库，才能保证数据的完整性。
  - 可以快速访问数据 - SQL 可使我们从数据库中快速获取结果。 可以优化代码，快速获取结果。 
  - 可以很容易共享数据 - 多个人可以访问存储在数据库中的数据，所有访问数据库的用户获得的数据都是一样。
  
## SQL 基础语句

### SQL 基础语法与规范

[SQL样式指南 · SQL Style Guide](https://www.sqlstyle.guide/zh/)

1. 大写
2. 表和变量名中不需要空格
3. 在查询中使用空格
4. SQL 不区分大小写


### SQL 学习资源

SQL 的目的是为了查询结果，向着越来越精确的方向发展。精确包含两个含义：

1.结果集中的元素由多变少，过滤掉不需要的内容
2.结果集的混乱程度由高变低，使得规律更容易观察


### 1. 创建和删除
`CREATE TABLE` 是一个在数据库中创建新表的语句。  
`DROP TABLE` 是删除数据库中表的语句。

### 2. 查询
`SELECT FROM` 读取并显示数据。我们将这称为查询。 


`SELECT`用于选择返回哪些列，`FROM`表示从哪个表中查询。（列必须属于该表）

order 表含有如下列
```
id	
account_id	
occurred_at	
standard_qty
gloss_qty
poster_qty
total	
standard_amt_usd	
gloss_amt_usd
poster_amt_usd	
total_amt_usd
```

#### 2.1 从 order 表中，提取全部的列（*表示全部的列）

```sql
SELECT * 
FROM orders;
```
也可以写作下面的形式

```sql
SELECT * FROM orders;
```
这两种形式的不同，体现在人类的感官上，对计算机是没有差别的，适当的换行有助于理清逻辑，毕竟“程序是给人看的，顺便给计算机执行”

```
id	account_id	occurred_at	standard_qty	gloss_qty	poster_qty	total	standard_amt_usd	gloss_amt_usd	poster_amt_usd	total_amt_usd
1	1001	2015-10-06T17:31:14.000Z	123	22	24	169	613.77	164.78	194.88	973.43
2	1001	2015-11-05T03:34:33.000Z	190	41	57	288	948.10	307.09	462.84	1718.03
3	1001	2015-12-04T04:21:55.000Z	85	47	0	132	424.15	352.03	0.00	776.18
```

#### 2.2 从 order 表中选取特定的列(id, account_id, occurred_at)

```sql
SELECT id, account_id, occurred_at
  FROM orders
```
```
结果
Output 3 results
id	account_id	occurred_at
1	1001	2015-10-06T17:31:14.000Z
2	1001	2015-11-05T03:34:33.000Z
3	1001	2015-12-04T04:21:55.000Z
```

### 3. 过滤和排序
对于 SQL 来讲，查询语句固然重要，但是往往不是最终的结果，因为单纯的查询，其结果是一个“混沌巨兽”——结果集非常大，且杂乱。通过 SELECT 语句，我们可以做最基本的过滤，比如不使用`*`符合，而选择我们感兴趣的列，例如`SELECT id, account_id, occurred_at`。

#### 3.1 `LIMIT` 

`LIMIT` 命令始终是查询的最后一部分，写在语句的最后。`LIMIT` 允许我们限制出打印的条目个数

```sql
SELECT occurred_at, account_id, channel
FROM web_events
LIMIT 15;
```


#### 3.2 `ORDER BY`

对筛选的的结果再次进行排序，进一步让结果有序。
可以在 ORDER BY 语句中的列之后添加 DESC，然后按降序排序，因为默认是按升序排序的

```sql
SELECT id, occurred_at, total_amt_usd
FROM orders
ORDER BY occurred_at
LIMIT 10;
```
基于 `occurred_at`（发生时间）进行排序

```sql
SELECT id, account_id, total_amt_usd
FROM orders
ORDER BY total_amt_usd DESC 
LIMIT 5;
```

基于 `total_amt_usd`降序排序

此外，我们还可以对多个列同时排序：

```sql
SELECT *
FROM orders
ORDER BY occurred_at DESC, total_amt_usd 
LIMIT 5;
```


#### 3.3 `WHERE`
WHERE 可以帮助我们创建当前查询的子集以缩小结果范围，通常配合比较符号和单引号来使用

WHERE 语句中使用的常用符号包括：  
`>`（大于）
`<`（小于）
`>=`（大于或等于）
`<=`（小于或等于）
`=`（等于）
`!=`（不等于）

```sql
SELECT *
FROM orders
WHERE gloss_amt_usd >= 1000
LIMIT 5;
```
从 orders 表中选择所有列，并筛选 gloss_amt_usd 值大于1000的5个结果

```sql
SELECT *
FROM citys_data
WHERE city = 'ShangHai'
```

从 citys_data 表中选择所有列，并筛选城市名为 'ShangHai' 的结果。注意字符串应该使用**单引号**

### 4 逻辑运算符

#### 4.1 `LIKE`

LIKE 运算符对于处理文本非常有用。我们将在 WHERE 子句中使用 LIKE。 LIKE 运算符经常与 ％ 一起使用。% 是通配符，除此之外还有其他的通配符，关于通配符可以查看这个[链接](http://www.w3school.com.cn/sql/sql_wildcards.asp)

```sql
SELECT name
FROM accounts
WHERE name LIKE 'C%';
```

#### 4.2 `IN`

IN 运算符对于数字和文本列都很有用。这个运算符可使我们使用 =，但对于特定列的多个项目。 可以检查我们要提取数据的一个、两个或多个列值，但这些都在同一个查询中。 在后面的概念中，我们将介绍 OR 运算符，也可以使用这个运算符执行这些任务，但使用 In 运算符编写的查询更清楚一些。

```sql
SELECT name, primary_poc, sales_rep_id
FROM accounts
WHERE name IN ('Walmart', 'Target', 'Nordstrom');
```

```sql
SELECT *
FROM web_events
WHERE channel IN ('organic', 'adwords');
```

### 5.算数运算符

```sql
SELECT id, account_id, standard_amt_usd/standard_qty AS unit_price
FROM orders
LIMIT 10;
```

其中 `unit_price` 是**派生列**，也就是根据一些列，经由算数运算符计算得到的新的一列，它会生成在新的表中。

原表：
```
id	account_id	occurred_at	standard_qty	gloss_qty	poster_qty	total	standard_amt_usd	gloss_amt_usd	poster_amt_usd	total_amt_usd
1	1001	2015-10-06T17:31:14.000Z	123	22	24	169	613.77	164.78	194.88	973.43
2	1001	2015-11-05T03:34:33.000Z	190	41	57	288	948.10	307.09	462.84	1718.03
3	1001	2015-12-04T04:21:55.000Z	85	47	0	132	424.15	352.03	0.00	776.18
```

结果（`unit_price`是派生列，通过`standard_amt_usd/standard_qty`得到）

```
id	account_id	unit_price
1	1001	4.9900000000000000
2	1001	4.9900000000000000
3	1001	4.9900000000000000
```

## 小结

|语句|作用|样例|文档|
|:--:|:--|:--|:--:|
|SELECT FROM|||[链接]()|
|LIMIT|||[链接]()|
|ORDER BY|||[链接]()|
|WHERE|||[链接](http://www.w3school.com.cn/sql/sql_where.asp)|
|LIKE|可用于进行类似于使用 WHERE 和 = 的运算，但是这用于你可能 不 知道自己想准确查找哪些内容的情况||[链接](http://www.w3school.com.cn/sql/sql_like.asp)|
|IN|用于执行类似于使用 WHERE 和 = 的运算，但用于多个条件的情况||[链接](http://www.w3school.com.cn/sql/sql_in.asp)|
|NOT|这与 IN 和 LIKE 一起使用，用于选择 NOT LIKE 或 NOT IN 某个条件的所有行||[链接]()|
|AND & BETWEEN|可用于组合所有组合条件必须为真的运算||[链接]()|
|OR|可用于组合至少一个组合条件必须为真的运算||[链接]()|


