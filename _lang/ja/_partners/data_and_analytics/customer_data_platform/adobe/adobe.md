---
nav_title: Adobe
article_title: Adobe
description: "このページでは、Brazeと Adobe のパートナーシップについて説明します。Adobe は顧客データプラットフォームであり、ブランドはリアルタイムで Adobe データ（カスタム属性とセグメント）をBrazeに接続してマッピングできます。その後、ブランドはこのデータに基づいて行動し、パーソナライズされたターゲットを絞った体験をユーザーに提供できます。"
page_type: partner
page_order: 1
search_tag: Partner

---

# Adobe

> Adobe Experience Platformに基づいて構築されたAdobe のリアルタイム顧客データプラットフォームは、複数のエンタープライズソースからの既知の匿名データをまとめて顧客プロファイルを作成します。その後、これらのプロファイルを使用して、パーソナライズされたエクスペリエンスをすべてのチャネルおよびデバイスでリアルタイムに提供できます。

BrazeとAdobe CDPの統合により、ブランドのAdobe データ（カスタム属性とセグメント）がリアルタイムでBrazeに接続され、マッピングされます。その後、このデータに基づいて行動し、ユーザーにパーソナライズされたターゲットを絞った体験を提供できます。Adobeでは、統合は直感的です。Adobeの任意の[ID](https://experienceleague.adobe.com/docs/experience-platform/identity/namespaces.html?lang=en)をBrazeのexternal IDにマッピングし、Brazeプラットフォームに送信するだけです。送信されたすべてのデータは、Brazeで新しい `AdobeExperiencePlatformセグメント` 属性を通じてアクセスできます。

{% alert important %}
Adobe Experience Platform統合では、現在、ダイナミックなオーディエンスメンバーシップはサポートされていません。つまり、ユーザープロファイルには値を追加できますが、削除することはできません。
{% endalert %}

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| Adobe アカウント | このパートナーシップを活用するには、[Adobe アカウント](https://account.adobe.com/)が必要です。 |
| Braze REST APIキー | `users.track` 権限を持つBraze REST APIキー。<br><br> これは、Brazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| Brazeインスタンス | Brazeインスタンスは、Brazeオンボーディングマネージャーから取得するか、[API概要ページ]({{site.baseurl}}/api/basics/#endpoints)で確認できます。 |
| Braze RESTエンドポイント | RESTエンドポイントのURL。エンドポイントはインスタンスの[Braze URL]({{site.baseurl}}/api/basics/#endpoints)に応じて異なります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

{% alert important %}
追加のカスタム属性を送信すると、データポイント使用量が増加します。この潜在的なデータポイントの増加をよりよく理解するために、カスタマーサクセスマネージャーにご相談ください。
{% endalert %}

## 統合 {#integration}

### ステップ 1: Braze送信先を設定する {#step-1-configure-braze-destination}

Adobeの**Settings**ページで、**Collections**の下にある**Destinations**を選択します。そこから**Braze**タイルを見つけ、**Configure**を選択します。

![]({% image_buster /assets/img/adobe/braze-destination-configure.png %})

{% alert note %}
Brazeとの接続がすでに存在する場合は、送信先カードに**Activate**ボタンが表示されます。ActivateとConfigureの違いの詳細については、Adobe送信先ワークスペースの[ドキュメント](https://experienceleague.adobe.com/docs/experience-platform/rtcdp/destinations/destinations-interface/destinations-workspace.html?lang=en#catalog)のカタログセクションを参照してください。
{% endalert %}

### ステップ 2: Brazeトークンを提供する {#step-2-provide-braze-token}

**Account**ステップで、Braze APIキーを入力し、**Connect to destination**を選択します。

![]({% image_buster /assets/img/adobe/braze-destination-account.png %}){: style="max-width:60%"}

### ステップ 3: 認証 {#step-3-authentication}

次に、**Authentication**ステップで、Braze接続の詳細を入力します。
- **Name**: 今後この送信先を認識するために使用する名前を入力します。
- **Destination**: この送信先を特定するのに役立つ説明を入力します。
- **Endpoint instance**: Brazeエンドポイントインスタンスを入力します。
- **Marketing use case**: マーケティングユースケースは、データを送信先にエクスポートする目的を示します。Adobe定義のマーケティングユースケースから選択するか、独自のマーケティングユースケースを作成できます。Adobeマーケティングユースケースの詳細については、[Adobe Experience Platformのデータガバナンス](https://experienceleague.adobe.com/docs/experience-platform/rtcdp/privacy/data-governance-overview.html?lang=en#destinations)を参照してください。

![]({% image_buster /assets/img/adobe/braze-destination-authentication.png %}){: style="max-width:60%;"}

### ステップ 4: 送信先を作成する {#step-4-create-destination}
**Create destination**を選択します。送信先が作成されました。**Save & Exit**を選択して後でセグメントを有効にするか、**Next**を選択してワークフローを続行し、有効にするセグメントを選択できます。

### ステップ 5: セグメントを有効にする {#step-5-activate-segments}
Adobe Real-Time CDPのデータを有効にするには、セグメントをBraze送信先にマッピングします。

以下のリストでは、セグメントを有効にするために必要な一般的なステップを示します。Adobeのセグメントとセグメント有効化ワークフローの詳細なガイダンスについては、[Adobe](https://experienceleague.adobe.com/docs/experience-platform/destinations/ui/activate-destinations.html?lang=en#prerequisites)を参照してください。

1. Braze送信先を選択してアクティブ化します。
2. 該当するセグメントを選択します。
4. エクスポートする各セグメントのスケジュールとファイル名を設定します。
5. Brazeに送信する属性を選択します。
6. アクティベーションを確認します。

### ステップ 6: フィールドマッピング {#step-6-field-mapping}

Adobe Experience PlatformからBrazeにオーディエンスデータを正しく送信するには、フィールドマッピングステップを完了する必要があります。マッピングにより、Adobe Experienceデータモデルのフィールドと対応するBrazeプラットフォームのフィールドの間にリンクが作成されます。

1. マッピングステップで**Add new mapping**を選択します。<br>![]({% image_buster /assets/img/adobe/braze-destination-mapping.png %}){: style="max-width:50%;"}<br><br>
2. ソースフィールドセクションで、空のフィールドの横にある矢印ボタンを選択して、ソースフィールド選択ウィンドウを開きます。<br>![]({% image_buster /assets/img/adobe/braze-destination-mapping-source.png %})<br><br>
3. ウィンドウで、Braze属性にマッピングするAdobe属性を選択します。<br>![]({% image_buster /assets/img/adobe/braze-destination-mapping-attributes.png %}){: style="max-width:70%;"}<br><br>次に、IDネームスペースを選択します。このオプションは、プラットフォームIDネームスペースをBrazeネームスペースにマッピングするために使用されます。<br>![]({% image_buster /assets/img/adobe/braze-destination-mapping-namespaces.png %}){: style="max-width:80%;"}<br>ソースフィールドを選択し、**Select**を選択します。<br><br>
4. ターゲットフィールドセクションで、フィールドの横にあるマッピングアイコンを選択します。<br>![]({% image_buster /assets/img/adobe/braze-destination-mapping-target.png %}){: style="max-width:90%;"}<br><br>
5. ターゲットフィールド選択ウィンドウでは、ターゲットフィールドの3つのカテゴリから選択できます。<br><br>• **Select identity namespace**: PlatformのIDネームスペースをBrazeのIDネームスペースにマッピングするには、このオプションを使用します。<br>• **Select custom attributes**: Adobe XDM属性を、Brazeアカウントで定義したカスタムBraze属性にマッピングするには、このオプションを使用します。<br><br>![]({% image_buster /assets/img/adobe/braze-destination-mapping-target-fields.png %}){: style="max-width:60%;"}<br><br>**このオプションを使用して、既存のXDM属性の名前をBrazeで変更することもできます。** たとえば、XDM属性 `lastname` をBrazeのカスタム属性 `Last_Name` にマッピングすると、Brazeに `Last_Name` 属性がまだ存在しない場合はこの属性が作成され、XDM属性 `lastname` がそれにマッピングされます。<br><br>ターゲットフィールドを選択し、**Select**を選択します。<br><br>
6. フィールドマッピングがリストに表示されます。<br>![]({% image_buster /assets/img/adobe/braze-destination-mapping-complete.png %})<br><br>
7. マッピングをさらに追加するには、必要に応じてステップ1〜6を繰り返します。

## ユースケース {#use-case}

たとえば、XDMプロファイルスキーマとBrazeインスタンスに次の属性とIDが含まれているとします。

|     | XDMプロファイルスキーマ | Brazeインスタンス |
| --- | ------------------ | -------------- |
| 属性 | - `person.name.firstname`<br>- `person.name.lastname`<br>- `mobilePhone.number`| - `FirstName`<br>- `LastName`<br>- `PhoneNumber`|
| ID | - `Email`<br>- Google広告ID (`GAID`)<br>- Apple ID For Advertisers (`IDFA`) | - `external_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Use case" }

正しいマッピングは次のようになります。

![送信先マッピング: IdentityMap:IDFAをIdentityMap:external_idにマッピング、IdentityMap:GAIDをIdentityMap:external_idにマッピング、IdentityMap:EmailをIdentityMap:external_idにマッピング、xdm:mobilePhone.numberをCustomAttribute:PhoneNumberにマッピング、xdm:person.name.lastNameをCustomAttribute:LastNameにマッピング、xdm:person.name.firstNameをCustomAttribute:FirstNameにマッピング]({% image_buster /assets/img/adobe/braze-destination-mapping-example.png %})

## エクスポートされたデータ {#exported-data}
データが正常にBrazeにエクスポートされたかどうかを確認するには、Brazeアカウントをチェックします。Adobe Experience Platformのセグメントは、`AdobeExperiencePlatformセグメント` 属性でBrazeにエクスポートされます。

## データの使用とガバナンス {#data-usage-and-governance}
データの処理時に、Adobe Experience Platformのすべての送信先はデータ使用ポリシーに準拠します。Adobe Experience Platformによるデータガバナンスの実施方法の詳細については、[Real-Time CDPのデータガバナンス](https://experienceleague.adobe.com/docs/experience-platform/rtcdp/privacy/data-governance-overview.html?lang=en)を参照してください。