# テーブルの作成
以下のコマンドをターミナルで実行すると `db.Model` を継承したクラスがテーブルとして、データベース内に作成される。

```shell script
$ python
>> from app import db
>> db.create_all()
```

# データの追加
上記に続いて、次のコマンドでデータを追加できる。

```shell script
# create new_data
>> db.session.add(new_data)
>> db.session.commit()
```

