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