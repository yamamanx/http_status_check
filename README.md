# http status check

- サイトのステータスをチェックして200以外ならSlackに通知します。
- AWS Lambdaでの稼働を想定しています。
- 設定など詳細はこちらの[ブログ](http://www.yamamanx.com/http_status_check/)に書きます。

1. Githubからコードをダウンロードして展開します。
1. 同じフォルダにrequestsをインストールします。
1. requestsもあわせてAWS Lambda関数をzipからアップロードで作成します。
1. Slackチームを作ります。もしくは既存のチームでIncoming Webhooksを設定してURLを取得します。
1. 環境変数を設定します。
1. トリガーをCloudWatch Eventで rate(5 minutes)として5分おきで実行します。

### 環境変数
* url_1 : 監視したいURL
* url_2 ~ 10 : 監視したいURLを10件まで登録出来ます。1だけでもOKです。
* SLACK_URL : SlackのIncoming Webhooks URLです。