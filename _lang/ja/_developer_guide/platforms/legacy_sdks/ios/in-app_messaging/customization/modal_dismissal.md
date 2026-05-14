---
nav_title: モーダルを閉じる
article_title: iOS のアプリ内メッセージモーダルを閉じる
platform: iOS
page_order: 29
description: "この参考記事では、iOS アプリケーションのアプリ内メッセージングのモーダルを閉じることについて説明します。"
channel:
  - in-app messages
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 外側のタップでモーダルを閉じる {#dismiss-modal-on-outside-tap}

デフォルト値は `NO` です。ユーザーがアプリ内メッセージの外側をタップしたときに、モーダルタイプのアプリ内メッセージが閉じられるかどうかを決定します。

外側タップによる閉じる操作を有効にするには、`Braze` という名前のディクショナリを `Info.plist` ファイルに追加します。次のコードスニペットに示すように、`Braze` ディクショナリ内にブール値サブエントリ `DismissModalOnOutsideTap` を追加し、値を `YES` に設定します。なお、Braze iOS SDK v4.0.2 より前のバージョンでは、`Braze` の代わりにディクショナリキー `Appboy` を使用する必要があります。

```
<key>Braze</key>
<dict>
  <key>DismissModalOnOutsideTap</key>
  <boolean>YES</boolean>
</dict>
```

また、`appboyOptions` で `ABKEnableDismissModalOnOutsideTapKey` を `YES` に設定して、実行時に機能を有効にすることもできます。

| `DismissModalOnOutsideTap` | 説明 |
|----------|-------------|
| `YES`       | モーダルアプリ内メッセージは、外側タップで閉じられます。     |
| `NO`        | デフォルトでは、モーダルアプリ内メッセージは外側タップでは閉じられません。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="外側のタップでモーダルを閉じる" }