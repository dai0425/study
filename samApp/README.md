# 備忘録

- ポリシーの設定は完璧だが、アクセス権限エラーが起きる
https://qiita.com/fumi19/items/d6896fd1330227380ca0

- 使用するimageIdに応じてbodyの中身が異なる
https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html
https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-titan-text.html

- lambdaで返却する文字列が勝手にエスケープされる
ensure_ascii=Falseをすれば、そのままの文字列でいけた

- corsエラーがつづいたが、ヘッダーに
"Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "OPTIONS,POST,GET",
    を付けたら通った、→"Access-Control-Allow-Origin": "*",だけではだめ←追記　そのあと＊だけでも通ったため、キャッシュが影響してそう