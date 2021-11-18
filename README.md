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

## PlayGround 上でクエリを実行してみる
**すべての投稿を取得する**
```graphql
query AllPosts {
  listPosts {
    success
    errors
    posts {
      id
      title 
      description
      created_at
    }
  }
}
```

**指定した ID の投稿を取得する**
```graphql
query GetPost {
  getPost(id: "1") {
    post {
      id
      title
      description
    }
    success
    errors
  }
}
```

**新しい投稿を追加する**
```graphql
mutation CreateNewPost {
  createPost(
    title: "New Post", 
    description:"This is a new post !!") {
    post {
      id
      title
      description
      created_at
    }
    success
    errors
  }
}
```

**投稿を更新する**
```graphql
mutation UpdatePost {
  updatePost(
    id: "2",
    title: "New title !!",
    description: "This post was updated..."
  ) {
    post {
      id
      title
      description
    }
    success
    errors
  }
}
```

**投稿を削除する**
```graphql
mutation DeletePost{
  deletePost(id: "2") {
    post{
      id
      title
      description
    }
    success
    errors
  }
}
```