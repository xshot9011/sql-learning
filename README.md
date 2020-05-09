# SQL command

## order

select ... case ... from ... where ... group by ... having ... order by ... limit ... 

## select

### normal 

```bash
SELECT [fields, ...]:AS [new field name] FROM [table];
```

note: only field that we want ^-^ better for db

### condition

```bash
SELECT [fields] FROM [table] WHERE [field][expression][value] :{AND, OR ..};
```

### sorting

```bash
SELECT [fields, ...] FROM [table] ORDER BY [fields] [DESC if more to less];
```

### limiting record

```bash
SELECT [fields, ...] FROM [table] LIMIT [number of record];
```

## insert

### crazy

```bash
INSERT INTO [table] VALUES (order field's value, ..)
```

note: all order fields > if dont have put NULL

### goods

```bash
INSERT INTO [table](fields, ..) VALUES (order field's value, ...)
```

note: only specific field

## update

```bash
UPDATE [table] SET [[field][expression][value], ...] WHERE [condition];
```

note: working complete without where condition becareful

## delete

note: becarefull

```bash
DELETE FROM [table] WHERE [condition]; 
```

note: working complete without where condition becareful

## aggregation funtion

### counting 

```bash
SELECT COUNT([field]) FROM [table] WHERE [condition]];
```

### average 

```bash
SELECT AVG([field]) FROM [table] WHERE [condition] ;
```

### sum

```bash
SELECT SUM([field]) FROM [table] WHERE [condition] ;
```

### max, min

```bash
SELECT [max, min]([field]) FROM [table] WHERE [condition] ;
```

### group by

note: combination between some fields and values

```bash
SELECT [fieds or others] FROM [table] GROUP BY [fields];
```

like you group the information depend on it's value on the specific column

### having

note: where count(filed) [<, >, =, ...] [value] is error
where cannot user with aggreate function

```bash
SELECT [...] FROM [table] GROUP BY [fields] HAVING [aggreate funtion or fields or as name][operation][value] ORDER BY [field];
```

ถ้าแปลเป็นไทยก็จัดกลุ่มโดยมีค่าในfields นี้เป็นหลัก โดยกลุ่มเหล่านั้นมีค่า ...ตามเงื่อนไข... เรียงโดย...

note: if statement has GROUPBY, HAVING always follow the it

## sql operator

### not 

put it after where state ment 
not x = value  === x != value

### in

```bash
SELECT [...] FROM [table] WHERE [field] in(value1, value2, ...);
```

note: not in 

### like 

```bash
SELECT [...] FROM [table] WHERE [field] like '[.0.]';
```

%c = everything end with 'c'
c% = everything start with 'c'

### between 

```bash
SELECT [...] FROM [table] WHERE [field] betwwen [value] and [value];
```

### is null

```bash
SELECT [...] FROM [table] WHERE [field] is NULL;
```

'' and NULL is dif, NULL is absolutely emtry

### and or

```bash
SELECT [...] FROM [table] WHERE [condition] [and, or] [condition];
```

## join

การเอาข้อมูล 2 ก้อนมารวมกัน

note: if name of fields are the same or similar or '1, you can use [table].[field] instead

ืnote: table สามารถเป็นอันเดียวกันได้ สิ่งที่สำคัญคืออะไรอยู่หลังพวงมาลัย ถุ้ยยย หลัง on อย่าลืมเปลี่ยนชื่อหลัง table ที่ 2 ไม่งั้นมันจะงงว่าเอา field นั้นมาจาก table ไหน

### inner join

the intersection between A and B

```bash
SELECT [fields]
FROM [table_a] INNER JOIN [table_b] ON [table_a].[field] = [table_b].[field]
ORDER BY [field];
```

### left (outer) join

เอาข้อมูล a มารวมกับข้อมูล b โดยข้อมูล a ต้องครบทุกตัว ข้อมูล b ถ้ารวมได้ก็จะรวม

```bash
SELECT [fields]
FROM [table_a] LEFT JOIN [table_b] ON [table_a].[field] = [table_b].[field]
ORDER BY [field];
```

### right (outer) join

เอาข้อมูล a มารวมกับข้อมูล b โดยข้อมูล b ต้องครบทุกตัว ข้อมูล a ถ้ารวมได้ก็จะรวม

```bash
SELECT [fields]
FROM [table_a] RIGHT JOIN [table_b] ON [table_a].[field] = [table_b].[field]
ORDER BY [field];
```

### full (outer) join

เอาข้อมูล a มารวมกับข้อมูล b โดยข้อมูล a, b ต้องครบทุกตัวถ้าสามารถรวมได้ก็จะรวม
ไม่ค่อยแนะนำ เพราะเรื่องข้อมูลขยะ

```bash
SELECT [fields]
FROM [table_a] FULL OUTER JOIN [table_b] ON [table_a].[field] = [table_b].[field]
ORDER BY [field];
```

## many condition

### case

```bash
SELECT [fields], 
CASE
WHEN [condtions] THEN [output value]
WHEN [conditions] THEN [output value]
ELSE [output value]
END AS [new_field_name]
FROM [table]
```

note: new_field_name will be the output value for each records mathcing condition

### sub queries

```bash
SELECT [fields], 
FROM [table],
WHERE [fields] IN (SELECT [field] FROM [TABLE] WHERE [condition])
/* or */
SELECT [field] = (SELECT [field] FROM [table] WHERE [condition]), [others fields]
FROM [table]
WHERE [condition]
```
