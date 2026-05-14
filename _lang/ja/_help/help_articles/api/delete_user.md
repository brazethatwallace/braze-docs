---
nav_title: API を使用したユーザーの削除
article_title: API を使用したユーザーの削除
page_order: 0

page_type: reference
description: "このヘルプ記事では、Braze REST APIを使用してユーザープロファイルを削除した場合の影響について説明します。"
tool: Dashboard
platform: API
---

# APIを使用したユーザーの削除 {#remove-users-via-api}

[Braze REST APIを使用してユーザーを削除]({{site.baseurl}}/api/endpoints/user_data/#user-delete-endpoint/)すると、以下のデータが削除（null化）されます。
- ユーザーが持っていたすべての属性
- メールアドレス
- 電話番号
- 外部ユーザー ID
- 性別
- 国
- 言語

[Braze REST APIを使用してユーザーを削除]({{site.baseurl}}/api/endpoints/user_data/#user-delete-endpoint/)すると、以下の事象が発生します。
- ユーザープロファイルが削除（null化）されます。
- [生涯ユーザー数]({{site.baseurl}}/user_guide/data_and_analytics/analytics/understanding_your_app_usage_data/#lifetime-users)が更新され、新たに削除されたユーザーが反映されます。
- 削除されたユーザーは、集計コンバージョン率に引き続きカウントされます。削除されたユーザーのカスタムイベント数と購入数は更新されません。

## メールアドレスを共有する複数のプロファイル {#multiple-profiles-with-a-shared-email-address}

同じメールアドレスを共有する複数のユーザープロファイルを統合する場合を考えてみましょう。

これらのユーザープロファイルを統合するには、以下の手順を実行します。

 1. 重複するメールアドレスを持つユーザーを特定します。
 2. 単一プロファイルのすべての属性をエクスポートします。
 3. それらの属性をAPIまたはCSVを使用してユーザープロファイルにインポートします。
 4. APIを使用してユーザーを削除します。これにより、重複ユーザーと上記のデータが削除されます。

_最終更新日：2023年9月13日_