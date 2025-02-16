- ポケポケのRAGを作ってみる
- まずはRAGに入れるためのデータベースを作成する
https://note.com/plan_sssss/n/n01fabe8eb739
- layerを入れるにはpythonはいかに

- excelfileへの書き込みはLambda関数だとできないらしく、いったんメモリを作成する必要があるらしい
```
このエラーメッセージは、'pokemon.xlsx' ファイルを書き込もうとしたときに発生しています。エラーの原因は、書き込み先のファイルシステムが読み取り専用であるためです。

Lambda関数のデフォルト環境では、読み取り専用のファイルシステムが使用されるため、直接ファイルに書き込むことができません。この問題を解決するには、ファイルを書き込む代わりに、メモリ内でExcelファイルを作成し、その内容をS3バケットなどにアップロードする方法を使用できます。
```

- Bedrock作成資料
https://zenn.dev/ncdc/articles/41bf6e7735ec9f

https://qiita.com/cyberBOSE/items/cc0a7434b4b7b27ce6de