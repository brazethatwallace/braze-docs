---
nav_title: ビーコンの統合
article_title: iOS 向けビーコン統合
platform: iOS
page_order: 4
description: "この記事では、Infillion Beacons for iOS を使用したカスタムイベントのログ記録について説明します。"

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# ビーコンの統合 {#beacon-integration}

ここでは、特定の種類のビーコンをBrazeと統合して、セグメンテーションとメッセージングを可能にする方法について説明します。

## Infillion ビーコン {#infillion-beacons}

Infillion ビーコンを設定してアプリに統合すると、カスタムイベント（アクセスの開始または終了、ビーコンの検知など）をログに記録できます。これらのイベントのプロパティ（場所の名前、滞在時間など）をログに記録することもできます。

ユーザーが場所に入ったときにカスタムイベントをログに記録するには、次のコードを `didBeginVisit` メソッドに入力します。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] logCustomEvent:@"Entered %@", visit.place.name];
[[Appboy sharedInstance] flushDataAndProcessRequestQueue];
```

{% endtab %}
{% tab swift %}

`````````swift
Appboy.sharedInstance()?.logCustomEvent("Entered %@", visit.place.name)
Appboy.sharedInstance()?.flushDataAndProcessRequestQueue()
```

{% endtab %}
{% endtabs %}

`flushDataAndProcessRequestQueue` は、アプリがバックグラウンドで実行されている場合でもイベントが必ずログに記録されることを確認します。これと同じプロセスを、ロケーションから離れる行動についても実装できます。これにより、ユーザーが新しい場所に入るたびにユニークなカスタムイベントが作成され、インクリメントされることに注意してください。50か所を超える場所を作成する予定の場合は、汎用的な「Place Entered」カスタムイベントを1つ作成し、イベントプロパティとして場所名を含めることをお勧めします。