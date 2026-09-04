---
nav_title: Oracle Crowdtwist
article_title: Crowdtwist
description: "この記事では、特別に作成されたBrazeデータ変換テンプレートとCrowdtwistのデータプッシュオブジェクトを活用した、BrazeとOracle Crowdtwistのパートナーシップについて説明します。"
alias: /partners/crowdtwist/
page_type: partner
search_tag: Partner
---

# Oracle Crowdtwist

> [Oracle Crowdtwist](https://www.oracle.com/uk/cx/marketing/customer-loyalty/)は、ブランドがパーソナライズされた顧客体験を提供できるようにする、クラウドネイティブなカスタマーロイヤルティソリューションのリーディングカンパニーです。同社のソリューションは100以上のすぐに使えるエンゲージメントパスを提供し、マーケターがより完全な顧客ビューを構築するための迅速なTime-to-Valueを実現します。

Oracle Crowdtwistのデータプッシュ機能では、Crowdtwistのプラットフォームで更新が発生するたびに、ユーザーやイベントのメタデータを渡すことができます。

このガイドでは、Oracle Crowdtwistのユーザープロファイル、ユーザーアクティビティ、およびユーザーリデンプションのライブプッシュフィードをBraze環境に統合する方法について説明します。このドキュメントでは明示的にカバーされていませんが、さらに2つのデータプッシュタイプが利用可能であり、そのセットアップはこのガイドで概説する同じ原則に従います。

* [Live Pushユーザープロファイル](https://docs.oracle.com/en/cloud/saas/marketing/crowdtwist-develop/Developers/PushUserProfile-withTiersv2.html): 新規プロファイルの作成と既存プロファイルの更新を含みます。

* [Live Pushユーザーアクティビティ](https://docs.oracle.com/en/cloud/saas/marketing/crowdtwist-develop/Developers/LivePushUserActivity.html): ユーザーアクティビティの完了データを含みます。

* [Live Pushユーザーリデンプション](https://docs.oracle.com/en/cloud/saas/marketing/crowdtwist-develop/Developers/LivePushUserRedemption.html): ユーザー報酬の引き換えに関するデータを含みます。

Brazeデータ変換テンプレートを使用することで、Brazeに関係のないデータプッシュの要素をフィルターで除外し、Brazeで必要な値を割り当てて、利用可能な「送信先」で活用できるようにすることができます。

例えば、データプッシュを使用して、ユーザーがロイヤルティティアを変更したり報酬を引き換えたりした際に、関連するカスタムイベントやカスタム属性をBrazeに渡すことができます。また、ユーザーのポイント残高のように、メンバーのユーザープロファイルでデータが更新されると同時に、カスタム属性をBrazeに記録するために使用することもできます。

## 前提条件 {#prerequisites}


| 要件 | 説明 |
| --- | --- |
| Oracle Crowdtwistアカウント | このパートナーシップを利用するには、[Oracle Crowdtwistアカウント](https://www.oracle.com/uk/cx/marketing/customer-loyalty/)が必要です。 |
| Brazeデータ変換エンドポイント | この連携は、Brazeの[データ変換ツール]({{site.baseurl}}/user_guide/data/unification/data_transformation)に依存しています。データ変換を作成すると、Brazeはユニークなエンドポイントを生成します。このエンドポイントをCrowdtwistのData Pushの送信先として追加できます。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 統合 {#integration}

BrazeとOracle Crowdtwistは、ユーザープロファイル、ユーザーリデンプション、およびユーザーアクティビティイベントを活用する独自のデータ変換を開発する際に役立つ[データ変換テンプレート]({{site.baseurl}}/user_guide/data/unification/data_transformation/creating_a_transformation?redirected=1#step-2-create-a-transformation)を作成しました。

## ステップ1:Oracle CrowdTwistテンプレートからData Transformationを作成する {#step-1-create-data-transformation-from-oracle-crowdtwist-template}

**データ設定 > Data Transformation > トランスフォーメーションを作成 > テンプレートを使用** に移動し、お好みの「BRAZE <> CROWDTWIST」テンプレートを選択します。

4つのテンプレートが用意されています。ユーザープロファイル、ユーザーアクティビティ、ユーザーリデンプションイベントをそれぞれ変換するテンプレートが1つずつと、条件ロジックを使用してさまざまなData Pushイベントに適用するマスターテンプレートが1つです。

[Oracle CrowdTwistのData Pushドキュメント](https://docs.oracle.com/en/cloud/saas/marketing/crowdtwist-develop/Developers/DataPush.html)に示されているように、Data Pushオブジェクトにはそれぞれ異なるメタデータが含まれているため、適切なBrazeオブジェクトを作成するにはそれぞれ独自の変換コードが必要です。マスターテンプレートは、3種類のオブジェクトそれぞれを受け入れる単一のData Transformationを設定し、各オブジェクトの値を使用して適切な出力を作成する方法を示しています。

## ステップ2: テンプレートの更新とテスト {#step-2-update-and-test-template}

このセクションでは、注釈付きテンプレートを確認できます。これらのテンプレートの本文は、`/users/track` 送信先に適用するように設計されています。注釈は `//` で始まる行と緑色のテキストで示されており、変換コードの動作に影響を与えることなく削除できます。

この変換は JavaScript を使用しており、「brazecall」と呼ばれるオブジェクトを構築します。このオブジェクトは、Braze REST APIエンドポイントに送信されるリクエストボディを作成する場所です。これらの送信先へのリクエストに必要な構造のガイダンスについては、「送信先」セクションのリンクを参照してください。

{% alert note %}
各「キー」の「値」は `payload.` で始まっています。payload は、Oracle Crowdtwist から受信したデータオブジェクトを表します。JavaScript のドット記法を使用して、Braze オブジェクトの要素に入力するデータを選択します。例えば、`external_id: payload.thirdPartyId` と表示されている場合、Braze の external ID は Oracle Crowdtwist に保存されている `third_party_id` の値で設定されることを意味します。Oracle Crowdtwist から送信されるオブジェクトのスキーマや構成の詳細については、[Oracle のドキュメント](https://docs.oracle.com/en/cloud/saas/marketing/crowdtwist-develop/Developers/LivePushUserActivity.html)を参照してください。
{% endalert %}

{% alert important %}
 Oracle Crowdtwist から送信されるオブジェクトを使用して、Braze でユーザーを作成します。`update_existing_only` キーを値 `false` で含めることにより、属性またはイベントオブジェクトに Braze に存在しない識別子が含まれている場合、Braze はイベントまたは属性オブジェクトに含まれる属性を持つユーザープロファイルを作成します。Oracle Crowdtwist が Braze に既に存在するプロファイルのみを更新するようにしたい場合は、各属性またはイベントオブジェクトでこの属性を `true` に設定してください。
{% endalert %}

### データ変換テンプレート {#data-transformation-templates}
{% tabs %}
{% tab ユーザープロファイルイベントテンプレート %}
```javascript
let brazecall = {
 "attributes": [
   {
     //You must include an appropriate identifier for your attribute or event object from data available in Oracle Crowdtwist. This could be an external ID, Braze ID, user alias, phone, or email address for attribute or event objects.
     "external_id": payload.thirdPartyId,
     "email": payload.emailAddress,
   // **Important** To allow Oracle Crowdtwist events to create users in Braze, set the value of "_update_existing_only" to false. Otherwise, set this value to true in your event and attribute objects.
     "_update_existing_only": false,
     "crowdtwist_loyalty_points": payload.redeemablePoints,
 //In this example, the "tierInfo" object from Crowdtwist is transformed into a Braze Nested Custom Attribute. Use the "_merge_objects" value to avoid duplications in a data point efficient manner.
 //The "tierinfo_current_level" attribute is a flat Braze custom attribute, while the following "tierInfo" value is a nested object mirroring the Crowdtwist payload; the difference in capitalization is intentional.
     "tierinfo_current_level": payload.tierInfo.currentLevel,
     "_merge_objects" : true,
     "tierInfo" : {
       "resetDate": payload.tierInfo.resetDate,
       "dateReached":payload.tierInfo.dateReached,
        "scoreNeededToReach": payload.tierInfo.scoreNeededToReach,
        "nextLevel":{
        "minValue":payload.tierInfo.nextLevel.minValue,
        "maxValue":payload.tierInfo.nextLevel.maxValue,
        "title":payload.tierInfo.nextLevel.title
     }
     }
   }
 ]
,
//Below we show how to create both custom attributes and events from a single Crowdtwist User Profile object.
 "events": [
   {
     "external_id": payload.thirdPartyId,
     "email": payload.emailAddress,
     "name": "assignedByEvent",
//Below we can see how to write a timestamp in your object, which is a required value for some objects, like the Event Object.
     "time": new Date().toISOString(),
     "properties": {
       "assigned_by_event": payload.tierInfo.assignedByEvent,
       "date_assigned": payload.tierInfo.dateAssigned
     },
           "_update_existing_only": false
   }
 ]
};
// After the /users/track request is assigned to brazecall, return brazecall to create an output.
return brazecall;

```

{% endtab %}
{% tab ユーザーアクティビティイベントテンプレート %}
```javascript
let brazecall = {
"events": [
   {
     "external_id": payload.thirdPartyId,
     "_update_existing_only": false,
     "activityId": payload.activityId,
     "name": payload.activityName,
     "time": new Date().toISOString(),
     "properties": {
       "description": payload.description,
       "date_assigned": payload.dateAwarded
     }
   }
 ]
};
return brazecall;
```
{% endtab %}
{% tab リデンプションイベントテンプレート %}
```javascript
let brazecall = {
 "attributes": [
   {
   "external_id": payload.thirdPartyId,
   //A user redemption event may not have a third party id, in which case you can instead provide the opportunity to include a user alias.
   "user_alias": { "alias_name" : "crowdtwist_redemption_username", "alias_label" : payload.userName},
   "_update_existing_only": false,
   "redeemed_coupon": payload.couponCode,
   "total_points_redeemed": payload.totalPointsRedeemed
      }
]
}
return brazecall;

```
{%endtab%}
{% tab マスターテンプレート %}
```javascript
//The master template uses JavaScript's conditional operators to determine the output of the Data Transformation. This example shows how to apply JavaScript to your transformation to allow for a dynamic range of sources or inputs.

 // We open the transformation with a simple "if" function. We're checking if the value "payload.tierInfo" is present. "tierInfo" is a value that is always populated in the User Profile Live Push object, but is not present in the others.

if (payload.tierInfo) {
let brazecall = {
 "attributes": [
   {
     "external_id": payload.thirdPartyId,
     "email": payload.emailAddress,
     "_update_existing_only": false,
     "crowdtwist_loyalty_points": payload.redeemablePoints,
     "tierinfo_current_level": payload.tierInfo.currentLevel,
     "_merge_objects" : true,
     "tierInfo" : {
       "resetDate": payload.tierInfo.resetDate,
       "dateReached":payload.tierInfo.dateReached,
        "scoreNeededToReach": payload.tierInfo.scoreNeededToReach,
        "nextLevel":{
        "minValue":payload.tierInfo.nextLevel.minValue,
        "maxValue":payload.tierInfo.nextLevel.maxValue,
        "title":payload.tierInfo.nextLevel.title
     }
     }
   }
 ]
,
 "events": [
   {
     "external_id": payload.thirdPartyId,
     "email": payload.emailAddress,
     "name": "assignedByEvent",
     "time": new Date().toISOString(),
     "properties": {
       "assigned_by_event": payload.tierInfo.assignedByEvent,
       "date_assigned": payload.tierInfo.dateAssigned
     },
           "_update_existing_only": false
   }
 ]
};
return brazecall;
//Now we use an "else if" operator to change the "brazecall" body if the object is a User Activity event by checking if the unique key "activityId" has been populated.
} else if (payload.activityId) {
 let brazecall = {
"events": [
   {
     "external_id": payload.thirdPartyId,
     "_update_existing_only": false,
     "activityId": payload.activityId,
     "name": payload.activityName,
     "time": new Date().toISOString(),
     "properties": {
       "description": payload.description,
       "date_assigned": payload.dateAwarded
     }
   }
 ]
};
return brazecall;
//Finally, this conditional statement triggers if the Data Push object is a User Redemption event, based on whether a value populates in the key "rewardId".
} else if (payload.rewardId) {
 let brazecall = {
 "attributes": [
   {
   "external_id": payload.thirdPartyId,
   "_update_existing_only": false,
   "redeemed_coupon": payload.couponCode,
   "total_points_redeemed": payload.totalPointsRedeemed
      }
]
}
return brazecall;
} else {
 //Include this error message to help with troubleshooting in the log if a call fails. Replace the text in the parentheses with anything that might be clearer to your team based on your Data Transformation.
 throw new Error("No appropriate Identifiers found");
}

```
{% endtab %}
{% endtabs %}

### 送信先 {#destinations}

このガイドのテンプレートは「Track Users」送信先に配信するために作成されていますが、[Braze のデータ変換ガイド]({{site.baseurl}}/user_guide/data/data_transformation/creating_a_transformation#step-2-create-a-transformation)に記載されている任意のエンドポイントに送信するようにテンプレートを設計できます。関連する [REST APIドキュメント]({{site.baseurl}}/api/home)もサポートとしてご利用いただけます。

### テスト {#testing}

テンプレートを好みに合わせて修正した後、正しく動作することを検証する必要があります。変換エディターで**Validate**を選択して**Output**セクションにプレビューを生成し、選択した送信先に対してマッピングされたリクエストを Braze が受け入れることを確認します。

**Output**フィールドに表示されるオブジェクトに問題がなければ、**Activate**を選択して、データ変換エンドポイントがデータを受信できる状態にします。

データ変換の Webhook URL は変換詳細パネルに表示されます。これをコピーして、Oracle Crowdtwist の Integration Hub 内の設定に使用してください。

{% alert important %}
Braze データ変換エンドポイントには、1分あたり1000リクエストのレート制限があります。Braze でこのデータを利用可能にする速度を検討し、より高いデータ変換レート制限が必要な場合は Braze アカウントマネージャーにご相談ください。
{% endalert %}

データ変換は非常にダイナミックなツールであり、JavaScript の理解と REST APIドキュメントのガイダンスにより、このドキュメントで説明されている内容を超えた目的で設計できます。データ変換テンプレートへの複雑な変更に関するサポートやトラブルシューティングについては、カスタマーサクセスマネージャーに相談して、利用可能なガイダンスについてご確認ください。