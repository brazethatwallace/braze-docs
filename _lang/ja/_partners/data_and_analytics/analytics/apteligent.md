---
nav_title: Apteligent
article_title: Apteligent
alias: /partners/apteligent/
description: "このリファレンス記事では、BrazeとApteligentのパートナーシップについて説明します。Apteligentは、詳細なクラッシュレポートを作成するモバイルアプリケーションであり、重要なデータを既存のBrazeソリューションに記録できるようにします。"
page_type: partner
search_tag: Partner

---

# Apteligent

> [Apteligent](https://www.vmware.com/products/workspace-one/intelligence-consumer-apps.html)は、開発者と製品マネージャーにツールとインサイトを提供するモバイルアプリケーションパフォーマンスプラットフォームです。

_この統合はApteligentによって管理されています。_

## 統合について {#about-the-integration}

BrazeとApteligentの統合は、詳細なiOSクラッシュレポートを提供し、重要なデータを既存のBrazeソリューションに記録するだけでなく、アプリケーションのクラッシュを経験したユーザーをセグメント化し、理解し、エンゲージすることを可能にします。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
|---|---|
| TestDriveアカウント | このパートナーシップを活用するには、TestDriveアカウントが必要です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

{% alert warning %}
この統合は現在iOSでのみサポートされています。
{% endalert %}

## 統合 {#apteligent-ios-integration}

### ステップ 1:オブザーバーを登録する {#step-1-register-an-observer}

最初にオブザーバーを登録する必要があります。Apteligentを初期化する前に、この登録が完了していることを確認してください。

```objc
[[NSNotificationCenter defaultCenter] addObserver:self
                                         selector:@selector(crashDidOccur:)
                                             name:@"CRCrashNotification"
                                           object:nil];
```

### ステップ 2:カスタムクラッシュ分析を記録する {#step-2-log-custom-crash-analytics}

Apteligent SDKは、クラッシュが発生した後にユーザーがアプリケーションを読み込むと通知を発行します。通知には、クラッシュの名前、理由、発生日が含まれます。

通知を受け取ったら、カスタムクラッシュイベントをログに記録し、Apteligentのクラッシュレポート分析を使用してユーザー属性を更新します。

`````````objc
- (void)crashDidOccur:(NSNotification*)notification {
  NSDictionary *crashInfo = notification.userInfo;
  [[Appboy sharedInstance] logCustomEvent:@"ApteligentCrashEvent" withProperties:crashInfo];
  [[Appboy sharedInstance].user setCustomAttributeWithKey:@"lastCrashName" andStringValue:crashInfo[@"crashName"]];
  [[Appboy sharedInstance].user setCustomAttributeWithKey:@"lastCrashReason" andStringValue:crashInfo[@"crashReason"]];
  [[Appboy sharedInstance].user setCustomAttributeWithKey:@"lastCrashDate" andDateValue:crashInfo[@"crashDate"]];
}
```

完了すれば、Apteligentプラットフォームにあるクラッシュ情報を使って、Brazeのセグメンテーションとエンゲージメント分析の力を活用できるようになります。