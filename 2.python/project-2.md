# 项目2-探索美国共享单车数据


## 软件设计文档（简略）

### 1. 需求描述
创建一个交互式程序，首先向用户提问，要求其输入需要查看的城市，然后是需要过滤的月份和星期几，输入all则表示不过滤。根据用户的输入，获取数据集中的数据并进行分析，并输出分析结果
### 2. 功能点分解
按照需求描述，我们首先思考能否将程序拆分成几个组成部分，如果我们将程序想象成一个流水线，它经历了如下几个阶段：用户输入，获取数据，数据分析，结果输出。

![](https://github.com/hanxiaomax/uda-band/blob/master/2.python/F275D712-040B-4796-8F03-6F45156310A6.jpeg)

同时，对于程序的输入，由于输入直接来自用户，因此具有很大的不确定性，用户的输入可能很随意，而我们的程序并不能处理所有的输入，因此需要确认，我们支持的输入，并对用户的输入进行校验，保证输入合法。因此这里可以分出一个或两个功能点：获取用户输入并校验

其次，我们需要将结果输出，输出的结果是经过数据分析后得出的结论。不同的分析点，输出结果不同，但总体上只要将结果使用描述性语句答应即可。这里我如们可以实现一个单独的输出函数，但是考虑到不同的分析，输出结果可能差异比较大，因此一个统一的输出模块未必可行，所以我们不单独实现一个大而全的输出模块，而是在数据分析的过程中，一边分析一边输出。

输入输出决定后，我们开始考虑程序的处理流程。

排除输入输出，程序的基本功能是对数据进行过滤并分析，数据过滤功能是所有分析之前都需要做的，而不同的分析点之间的关系是平等的：分析1，分析2，分析3，分析4之间的关系是平等独立的，而且可以按需要增加或减少，因此我们的功能点三是：根据用户输入的过滤条件，抽取数据，并利用该数据进行若干独立的数据分析，同时输出结果。这些独立的数据分析没有先后顺序的要求


### 3. 功能点1 获取用户输入并校验合法性
1. 输入  
要求用户输过滤条件
2. 处理  
- 用户输入
python 提供用户输入的接口`input()`函数
- 校验用户输入合法性  
考虑到用户输入的随意性，必须对其进行校验，我们首先需要知道哪些是合法的输入：
```python
CITYS =  ["chicago","new york city","washington" ]
MONTH = ["january","february","march","april","may","june","july","august","september","october","november","december",'all']
DAYSOFWEEK = ["monday" ,"tuesday" ,"wednesday", "thursday", "friday" ,"saturday" ,"sunday",'all']
```
  - 用户的输入要属于这些集合
  - 考虑大小写问题，这里需要将用户的输入和合法输入转成相同的大小写形式，这里可以参考[Python 字符串大小写转换](http://www.runoob.com/python3/python3-upper-lower.html)来进行转换，不一定非要转换成小写，但进行比较的两方要一致。
  
3. 输出  
合法的过滤条件。通过函数返回值返回。

### 4. 功能点2 根据过滤条件抽取数据并预处理

1. 输入  
经过校验的过滤条件 
2. 处理  
- 根据合法的过滤条件，加载数据（根据`city`）
  - 加载数据之后，我们需要对其的基本情况有所了解，可以使用以下这些函数
  ```
  df.head()
  df.columns
  df.describe()
  df.info()
  df['column_name'].value_counts()
  df['column_name'].unique()
  ```
- 对加载的数据进一步过滤，通过（根据`month`，`day`），如果用户输入的 `month`，`day` 为 all，则不进行这一步过滤
- 对过滤出的数据，进行预处理，这里考虑到我们后面要处理时间，但是加载的数据时间列为字符串，我们需要把它转换成时间，可以使用 pandas 提供的 `to_datetime`函数，这里我们求最喜欢开始的时间，因此只转换Start Time列即可。
```
----------------------------------------
chicago all all
   Unnamed: 0           Start Time             End Time  Trip Duration  \
0     1423854  2017-06-23 15:09:32  2017-06-23 15:14:53            321   
1      955915  2017-05-25 18:19:03  2017-05-25 18:45:53           1610   
2        9031  2017-01-04 08:27:49  2017-01-04 08:34:45            416   
3      304487  2017-03-06 13:49:38  2017-03-06 13:55:28            350   
4       45207  2017-01-17 14:53:07  2017-01-17 15:02:01            534   

                   Start Station                   End Station   User Type  \
0           Wood St & Hubbard St       Damen Ave & Chicago Ave  Subscriber   
1            Theater on the Lake  Sheffield Ave & Waveland Ave  Subscriber   
2             May St & Taylor St           Wood St & Taylor St  Subscriber   
3  Christiana Ave & Lawrence Ave  St. Louis Ave & Balmoral Ave  Subscriber   
4         Clark St & Randolph St  Desplaines St & Jackson Blvd  Subscriber   

   Gender  Birth Year  
0    Male      1992.0  
1  Female      1992.0  
2    Male      1981.0  
3    Male      1986.0  
4    Male      1975.0  
```

3. 输出
过滤并转换后的 dataframe 格式数据

### 5. 功能点3 数据分析

1. 输入
过滤并转换后的 dataframe 格式数据
2. 处理
根据题目要求，进行数据分析，每个待分析的问题，写一个独立的函数，负责分析并打印结果  
  - 时间数据 `time_stats`
  - 站点数据 `station_stats`
  - 行程数据 `trip_duration_stats`
  - 用户数据 `user_stats`


3. 输出
每个函数单独输出它的分析结果

### 6. 总体流程图 

![](https://github.com/hanxiaomax/uda-band/blob/master/2.python/3CF2B854-D453-4415-A893-58F5F4EE762A.jpeg)
