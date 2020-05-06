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