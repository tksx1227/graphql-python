# graphql-python
GraphQL x Python の勉強用リポジトリ

## データベースにテーブルを作成する
```shell script
$ python
>> from app import db
>> db.create_all()
```

SQLite のコンソールでテーブルを確認できる
```sqlite
SELECT name 
FROM   sqlite_master 
WHERE  type="table";
```

## サーバーにアクセスする
Flask サーバーを起動して `http://127.0.0.1:5000/graphql` にアクセスする
