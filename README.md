# SQL command

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
