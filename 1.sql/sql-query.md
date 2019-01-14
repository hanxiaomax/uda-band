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

#### 3.2 `WHERE`

#### 3.3 `ORDER BY`




