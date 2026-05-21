---
nav_title: Bluedot
article_title: Bluedot
alias: /partners/bluedot/
description: "この参考記事では、BrazeとロケーションプラットフォームであるBluedotのパートナーシップについて概説し、アプリに正確でわかりやすいジオフェンシングプラットフォームを提供します。"
page_type: partner
search_tag: Partner

---

# Bluedot

> [Bluedot](https://bluedot.io/)は、アプリのための正確でシンプルなジオフェンシングプラットフォームを提供するロケーションプラットフォームです。BluedotのSDKを使用して、よりスマートなメッセージを発信し、モバイル注文のチェックインを自動化し、ワークフローを最適化し、摩擦のない体験を生み出しましょう。

_この統合はBluedotによって管理されています。_

## 統合について {#about-the-integration}

BrazeとBluedotの統合により、Bluedotのジオフェンスロケーションサービスを利用してユーザーイベントを作成し、ジャーニーやキャンペーンの構築、顧客の行動や関心の分析に活用できます。ユーザーがデバイス上で発生させたイベント（入場/退場）は、すべての関連情報とともに即座にBrazeに送信されます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
|---|---|
| Bluedotアカウント | この統合を活用するには、Bluedotアカウントが必要です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## ユースケース {#use-cases}

Bluedotによって提供されるカスタムイベントのロケーション情報は、キャンペーンで次のような一般的なユースケースを実現するために使用できます。
- [`QSR`](https://bluedot.io/solutions/quick-service-restaurants/)（クイックサービスレストラン）
- [`Click and Collect`](https://bluedot.io/solutions/click-and-collect/)
- [`Drive-Thru`](https://bluedot.io/solutions/qsr-drive-thru/)

## 統合 {#integration}

### ステップ1：Bluedotプロジェクトを作成する {#step-1-create-a-bluedot-project}
Bluedotアカウントを設定し、[Bluedot キャンバスダッシュボード](https://docs.bluedot.io/canvas/)にログインします。新しいプロジェクトの作成方法については、[Bluedotのドキュメント](https://docs.bluedot.io/canvas/creating-a-new-project/)を参照してください。

### ステップ2：SDKを統合する {#step-2-integrate-the-sdks}
[BluedotとBrazeの統合](https://docs.bluedot.io/integrations/braze-integration/)に関するドキュメントに記載されている手順を使用して、Bluedot Point SDKとBraze SDKをアプリに統合します。

### ステップ3：Bluedot SDKを認証する {#step-3-authenticate-the-bluedot-sdk}
ステップ1で作成した`projectId`を使用してBluedot Point SDKを認証します。

### ステップ4：BrazeでBluedotイベントを使用する {#step-4-use-bluedot-events-in-braze}

#### メッセージのトリガー {#triggering-messages}

Bluedot SDKによって生成されたロケーションイベントをもとにアクションを実行するプッシュキャンペーンまたはキャンバスを設定できます。この統合ルートは、ユーザーが会場や関心のあるロケーションに入った直後のリアルタイムメッセージングや、ユーザーがその場を離れた後の遅延フォローアップコミュニケーションに最適です。

Brazeでアクションベースのキャンペーンを設定し、設定したロケーションに基づいてメッセージを送信します。トリガーには、以下のスクリーンショットに示すように、`bluedot_entry`または`bluedot_exit`のカスタムイベントを使用します。

![配信ステップでのアクションベースのキャンペーン。ここでは、ユーザーがカスタムの`bluedot_entry`または`bluedot_exit`イベントを実行した場合にキャンペーンを送信する2つのスケジュールオプションがあります。]({%image_buster /assets/img_archive/キャンペーン-Delivery-BD.png %}){: style="max-width:80%"}

#### ユーザーのターゲット設定 {#targeting-users}

ワークスペースのターゲットとして**すべてのユーザー**を選択してください。
![アクションベースのキャンペーンのターゲットユーザーステップで、目的のセグメントとして「すべてのユーザー」を選択することを推奨しています。]({%image_buster /assets/img_archive/キャンペーン-Target_users-BD.png %}){: style="max-width:80%"}