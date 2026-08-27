---
nav_title: メッセージングのテスト
article_title: テストメッセージを送信する
page_order: 11.5
tool:
  - Campaigns
  - Canvas
page_type: reference
description: "このリファレンス記事では、さまざまなBrazeチャネルでテストメッセージを送信する方法と、カスタムイベントプロパティやユーザー属性を組み込む方法について説明します。"
---

# テストメッセージの送信 {#send-test-messages}

> メッセージングキャンペーンをユーザーに送信する前に、正しく表示され、意図した通りに動作することを確認するためにテストを行うことをお勧めします。Brazeダッシュボードのツールを使用して、選択したデバイスやチームメンバーにテストメッセージを作成して送信できます。

{% alert important %}
テスト後はキャンペーンの下書きを保存して、キャンペーンが削除されないようにしてください。下書きとして保存せずにテストメッセージを送信することも可能です。
{% endalert %}

## ステップ 1: テストユーザーを特定する {#step-1-identify-your-test-users}

メッセージングキャンペーンをテストする前に、テストユーザーを特定することが重要です。テストユーザーには、既存のユーザーIDやメールアドレスを使用することも、メッセージングキャンペーンのテスト専用に新しいユーザーを作成することもできます。

### オプション：コンテンツテストグループを作成する {#optional-create-a-content-test-group}

テストユーザーを整理する便利な方法は、[コンテンツテストグループ]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups)を作成することです。これは、キャンペーンからテストメッセージを受信するユーザーのグループです。キャンペーンの**テスト受信者**の下にある**コンテンツテストグループを追加**フィールドにこのテストグループを追加すれば、個々のテストユーザーを作成・追加することなくテストを開始できます。

## ステップ 2: チャネル別のテストメッセージを送信する {#step-2-send-channel-specific-test-messages}

テストメッセージの送信手順については、該当するチャネルの以下のセクションを参照してください。

{% tabs local %}
{% tab バナー %}

{% alert important %}
Brazeでバナーメッセージをテストする前に、Brazeでバナーキャンペーンを作成する必要があります。また、テストしたいプレースメントがすでに[アプリまたはWebサイトに配置されている]({{site.baseurl}}/developer_guide/banners/placements)ことを確認してください。
{% endalert %}

バナーメッセージを作成した後、バナーをプレビューするか、テストメッセージを送信できます。

1. バナーメッセージの下書きを作成します。
2. **プレビュー**を選択して、バナーをプレビューするか、テストメッセージを送信します。
3. テストメッセージを送信するには、コンテンツテストグループまたは1人以上の個別ユーザーを**テスト受信者**として追加し、**テスト送信**を選択します。

テストメッセージはデバイス上で最大5分間表示できます。

![バナーコンポーザーのプレビュータブ。]({% image_buster /assets/img/banners/preview_banner.png %})

{% alert note %}
ハードウェアの違いにより、プレビューがユーザーのデバイスでの最終的なレンダリングと同一でない場合があることに留意してください。
{% endalert %}

### テストチェックリスト {#test-checklist}

- バナーキャンペーンはプレースメントに割り当てられていますか？
- 画像やメディアは、ターゲットデバイスタイプと画面サイズで期待通りに表示・動作しますか？
- リンクやボタンは、ユーザーを正しい場所に誘導しますか？
- Liquidは期待通りに機能しますか？Liquidが情報を返さない場合に備えて、デフォルトの属性値を設定していますか？
- コピーは明確で簡潔、かつ正確ですか？

{% endtab %}
{% tab Content Card %}

{% alert important %}
[コンテンツテストグループ]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#content-test-groups)または個別ユーザーにテストを送信するには、送信前にテストデバイスでプッシュが有効になっており、テストユーザーに有効なプッシュトークンが登録されている必要があります。iOSユーザーの場合、テストContent Cardを表示するには、Brazeから送信されたプッシュ通知をタップする必要があります。この動作はテストContent Cardにのみ適用されます。
{% endalert %}

テストContent Cardはプッシュ通知を介して配信されます。カードはプッシュペイロードにパッケージ化され、プッシュが受信されるとSDKがそれを抽出してローカルにキャッシュします。

このプロセスは通常のカード配信システムをバイパスするため、Content Cardのテストであってもプッシュが有効になっている必要があります。

テストContent Cardは送信後約5分で期限切れになります。

Content Cardを作成した後、テストContent Cardをアプリに送信して、リアルタイムでどのように表示されるかを確認できます。

1. Content Cardの下書きを作成します。
2. **テスト**タブを選択し、このテストメッセージを受信するコンテンツテストグループまたは個別ユーザーを少なくとも1つ選択します。
3. **テスト送信**を選択して、Content Cardをアプリに送信します。

![テストContent Card]({% image_buster /assets/img/contentcard_test.png %})

### プレビュー {#preview}

**プレビュー**タブでカードを作成しながらプレビューできます。これにより、ユーザーの視点から最終的なメッセージがどのように表示されるかを視覚化できます。

{% alert note %}
コンポーザーの**プレビュー**タブでは、メッセージの表示がユーザーのデバイスでの実際のレンダリングと同一でない場合があります。メディア、コピー、パーソナライゼーション、カスタム属性が正しく生成されることを確認するために、常にデバイスにテストメッセージを送信することをお勧めします。
{% endalert %}

### テストチェックリスト

- テストユーザーは有効なプッシュトークンでプッシュにオプトインしていますか？
- 画像やメディアは期待通りに表示・動作しますか？
- Liquidは期待通りに機能しますか？Liquidが情報を返さない場合に備えて、[デフォルトの属性値]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic#accounting-for-null-nil-and-blank-attribute-values)を設定していますか？
- コピーは明確で簡潔、かつ正確ですか？
- リンクはユーザーを正しい場所に誘導しますか？
- テストユーザーは有効なプッシュトークンでプッシュにオプトインしていますか？

### 壊れた画像のトラブルシューティング {#troubleshooting-broken-images}

Content Cardの画像がレンダリングされない、または壊れて表示される場合：

- **URLが正しくURLエンコードされていることを確認する：** URL内の特殊文字（スペースやクエリパラメーターなど）は適切にエンコードする必要があります。そうでない場合、画像リクエストが失敗します。
- **コンテンツセキュリティポリシーを確認する：** 組織にコンテンツセキュリティポリシー（CSP）または内部ITセキュリティルールがある場合、ポリシーが画像ドメインをブロックしている可能性があります。画像URLのドメインがCSPで許可されていることを確認してください。
- **HTTPSを使用する：** 画像URLはブラウザやアプリでの混合コンテンツブロッキングを避けるために、`http://`ではなく`https://`を使用する必要があります。
- **ブラウザでURLを直接開く：** 画像がブラウザで読み込まれない場合、問題はBrazeではなく画像URLまたはホスティングにあります。

### デバッグ {#debug}

Content Cardが送信された後、Developer Consoleの[イベントユーザーログ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log)から問題を分析またはデバッグできます。

一般的なユースケースは、ユーザーが特定のContent Cardを表示できない理由をデバッグすることです。そのためには、**イベントユーザーログ**でセッション開始時にSDKに配信されたContent Card（インプレッション前）を確認し、特定のキャンペーンまで追跡できます。

1. **設定** > **イベントユーザーログ**に移動します。
2. テストユーザーのSDKリクエストを見つけて展開します。
3. **Raw Data**をクリックします。
4. セッションの`id`を見つけます。以下は例の抜粋です：

    ```json
    [
      {
        "session_id": "D1B051E6-469B-47E2-B830-5A728D1D4AC5",
        "data": {
          "ids": [
            "NDg2MTY5MmUtNmZjZS00MjE1LWJkMDUtMzI1NGZiOWU5MDU3"
          ]
        },
        "name": "cci",
        "time": 1636106490.155
      }
    ]
    ```

{: start="5"}
5. [Base64 Decode and Encode](https://www.base64decode.org/)などのデコードツールを使用して、`id`をBase64形式からデコードし、関連する`campaign_id`を見つけます。この例では、以下の結果になります：

    ```
    4861692e-6fce-4215-bd05-3254fb9e9057_$_cc=c3b25740-f113-c047-4b1d-d296f280af4f&mv=6185005b9d9bee79387cce45&pi=cmp
    ```

    ここで`4861692e-6fce-4215-bd05-3254fb9e9057`が`campaign_id`です。<br><br>

6. **キャンペーン**ページに移動し、`campaign_id`を検索します。

![キャンペーンページでのcampaign_id検索]({% image_buster /assets/img_archive/cc_debug.png %}){: style="max-width:80%;"}

ここから、メッセージの設定とコンテンツを確認して、ユーザーが特定のContent Cardを表示できない理由を詳しく調査できます。

{% endtab %}
{% tab メール %}

1. メールメッセージの下書きを作成します。
2. **プレビューとテスト**を選択します。
3. **テスト送信**タブを選択し、**個別ユーザーを追加**フィールドにメールアドレスまたはユーザーIDを追加します。
4. **テスト送信**を選択して、下書きしたメールを受信トレイに送信します。

![テストメール]({% image_buster /assets/img_archive/testemail.png %}){: style="max-width:40%;" }

メールに[ユーザー設定センター]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center)のリンクが含まれている場合、テスト送信では機能するリンクが生成されず、設定を保存することもできません。ユーザー設定センターをテストするには、代わりにテストユーザーまたは小規模な内部セグメントにメッセージを送信してください。詳細については、[ユーザー設定センターのテスト]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center#testing-preference-centers)を参照してください。

メールキャンペーンに大きな画像が含まれており、Outlookで期待通りに表示されない場合は、CSSやHTMLでのみスケーリングするのではなく、画像編集ツールやリサイズツールを使用して画像の実際のファイルサイズを縮小することを検討してください。

{% endtab %}
{% tab アプリ内メッセージ %}

{% alert warning %}
[コンテンツテストグループ]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#content-test-groups)または個別ユーザーにテストを送信するには、送信前にテストデバイスでプッシュが有効になっている必要があります。たとえば、テストメッセージが表示される前に通知をタップするために、iOSデバイスでプッシュが有効になっている必要があります。{% endalert %}

アプリ内およびテストデバイスでプッシュ通知が設定されている場合、テストのアプリ内メッセージをアプリに送信して、リアルタイムでどのように表示されるかを確認できます。

1. アプリ内メッセージの下書きを作成します。
2. **テスト**タブを選択し、**個別ユーザーを追加**フィールドにメールアドレスまたはユーザーIDを追加します。
3. **テスト送信**を選択して、プッシュメッセージをデバイスに送信します。

テストのプッシュメッセージがデバイス画面の上部に表示されます。

![テストアプリ内メッセージ]({% image_buster /assets/img_archive/test-in-app.png %})

{% alert important %}
テスト送信では、各受信者に複数のアプリ内メッセージが送信される場合があります。
{% endalert %}

プッシュメッセージを直接クリックして開くと、アプリに移動し、アプリ内メッセージのテストを確認できます。このアプリ内メッセージのテスト機能は、ユーザーがテストプッシュ通知をクリックしてアプリ内メッセージをトリガーすることに依存しています。そのため、テストプッシュ通知が正常に配信されるには、ユーザーが該当するアプリでプッシュ通知を受信する資格がある必要があります。

### プレビュー

**プレビュー**タブで作成中のアプリ内メッセージをプレビューできます。これにより、ユーザーの視点から最終的なメッセージがどのように表示されるかを視覚化できます。ランダムなユーザー、特定のユーザー、またはカスタマイズされたユーザーとしてメッセージをプレビューできます。モバイルデバイスまたはタブレット向けのメッセージもプレビューできます。

![アプリ内メッセージの作成時のコンポーズタブで、メッセージがどのように表示されるかのプレビューを表示しています。ユーザーが選択されていないため、本文セクションに追加されたLiquidはそのまま表示されます。]({% image_buster /assets/img/in-app-message-preview.png %})

Brazeには3世代のアプリ内メッセージがあります。サポートする世代に基づいて、メッセージを送信するデバイスを細かく調整できます。

![アプリ内メッセージのプレビュー時の世代切り替え。]({% image_buster /assets/img/iam-generations.gif %}){: height="50%" width="50%"}

{% alert warning %}
**プレビュー**では、メッセージの表示がユーザーのデバイスでの実際のレンダリングと同一でない場合があります。メディア、コピー、パーソナライゼーション、カスタム属性が正しく生成されることを確認するために、常にデバイスにテストメッセージを送信することをお勧めします。
{% endalert %}

### テストチェックリスト

- 画像やメディアは期待通りに表示・動作しますか？
- Liquidは期待通りに機能しますか？Liquidが情報を返さない場合に備えて、[デフォルトの属性値]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic#accounting-for-null-nil-and-blank-attribute-values)を設定していますか？
- コピーは明確で簡潔、かつ正確ですか？
- ボタンはユーザーを正しい場所に誘導しますか？

### アクセシビリティスキャナー {#accessibility-scanner}

アクセシビリティのベストプラクティスをサポートするために、Brazeは従来のHTMLエディターを使用して作成されたアプリ内メッセージのコンテンツをアクセシビリティ基準に照らして自動的にスキャンします。このスキャナーは、Webコンテンツアクセシビリティガイドライン（[WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)）の基準を満たしていない可能性のあるコンテンツを特定するのに役立ちます。WCAGは、World Wide Web Consortium（W3C）が策定した、障害を持つ人々にとってWebコンテンツをよりアクセスしやすくするための国際的に認められた技術標準です。

![アクセシビリティスキャン結果]({% image_buster /assets/img/Accessibilty_Scanner_IAM.png %})

{% alert note %}
アプリ内メッセージのアクセシビリティスキャナーは、カスタムHTMLで構築されたメッセージに対してのみ実行されます。
{% endalert %}

#### 仕組み {#how-it-works}

スキャナーはカスタムHTMLメッセージに対して自動的に実行され、HTMLメッセージ全体を[WCAG 2.1 AAルールセット](https://www.w3.org/WAI/WCAG22/quickref/?versions=2.1&currentsidebar=%23col_customize&levels=aaa)に照らして評価します。フラグが立てられた各問題について、以下が表示されます：

- 関連する特定のHTML要素
- アクセシビリティの問題の説明
- 追加のコンテキストまたは修正ガイダンスへのリンク

#### 自動アクセシビリティテストについて {#understanding-automated-accessibility-testing}

{% multi_lang_include accessibility/automated_testing.md %}

{% endtab %}
{% tab LINE %}

1. LINEメッセージを作成します。
2. **テスト**タブを選択し、このテストメッセージを受信するコンテンツテストグループまたは個別ユーザーを少なくとも1つ選択します。
3. **テスト送信**を選択してメッセージを送信します。

![テストLINEメッセージ。]({% image_buster /assets/img/line/test_preview.png %})

{% endtab %}
{% tab プッシュ %}

#### モバイルプッシュ {#mobile-push}

1. モバイルプッシュの下書きを作成します。
2. **テスト**タブを選択し、**個別ユーザーを追加**フィールドにメールアドレスまたはユーザーIDを追加します。
3. **テスト送信**を選択して、下書きしたメッセージをデバイスに送信します。

![テストプッシュ]({% image_buster /assets/img_archive/testpush.png %})

選択したユーザーに一致するプッシュトークンがないというエラーが表示された場合、テストユーザーが選択したプラットフォームの有効なプッシュトークンを持っていません。ユーザーはアプリでセッションを開始し、そのデバイスでプッシュを有効にしている必要があります。詳細については、[プッシュの有効化とプッシュの購読]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states)を参照してください。

#### Webプッシュ {#web-push}

1. Webプッシュを作成します。
2. **テスト**タブを選択します。
3. **自分にテスト送信**を選択します。
4. **テスト送信**を選択して、WebプッシュをWebブラウザに送信します。

![テストWebプッシュ]({% image_buster /assets/img_archive/testwebpush.png %})

Brazeダッシュボードからのプッシュメッセージをすでに許可している場合、メッセージは画面の隅に表示されます。許可していない場合は、プロンプトが表示されたら**許可**を選択すると、メッセージが表示されます。

選択したユーザーにWebプッシュの一致するプッシュトークンがないというエラーが表示された場合、テストユーザーが選択したプラットフォームの有効なプッシュトークンを登録していることを確認してください。プッシュトークンを受信するには、ユーザーがデバイス上のアプリのプッシュ通知を受信するように設定されている必要があります。詳細については、[プッシュの有効化とプッシュの購読]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states)を参照してください。

{% endtab %}
{% tab SMS/MMSおよびRCS %}

SMS、MMS、またはRCSメッセージを作成した後、テストメッセージを携帯電話に送信して、リアルタイムでどのように表示されるかを確認できます。受信者はテスト送信時に選択したSMS購読グループに属し、有効な電話番号を持ち、**地理的権限**で少なくとも1つの国が選択されている必要があります。詳細については、[SMS FAQ]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/faqs#does-a-user-need-to-be-part-of-an-sms-subscription-group-to-receive-sms-test-messages)を参照してください。

1. SMS、MMS、またはRCSメッセージの下書きを作成します。
2. **テスト**タブを選択し、このテストメッセージを受信するコンテンツテストグループまたは個別ユーザーを少なくとも1つ選択します。
3. **テスト送信**を選択してテストメッセージを送信します。

![テストContent Card]({% image_buster /assets/img/sms_test.png %})

{% endtab %}
{% tab Webhook %}

Webhookを作成した後、テスト送信を行ってWebhookのレスポンスを確認できます。**テスト**タブを選択し、**テスト送信**を選択して、指定されたWebhook URLにテスト送信を行います。個別ユーザーを選択して、特定のユーザーとしてレスポンスをプレビューすることもできます。

{% endtab %}
{% tab WhatsApp %}

1. WhatsAppメッセージを作成します。
2. **テスト**タブを選択し、このテストメッセージを受信するコンテンツテストグループまたは個別ユーザーを少なくとも1つ選択します。
3. このメッセージに使用している購読グループに関連付けられた電話番号にWhatsAppメッセージを送信して、会話ウィンドウを開始します。関連付けられた電話番号は、**テスト**タブのアラートに記載されています。
4. **テスト送信**を選択してメッセージを送信します。

![テストWhatsAppメッセージ。]({% image_buster /assets/img/whatsapp/whatsapp_test.png %})

{% endtab %}
{% endtabs %}

## パーソナライズされたキャンペーンのテスト {#test-personalized-campaigns}

ユーザーデータを使用するキャンペーンやカスタムイベントプロパティを使用するキャンペーンをテストする場合、追加の手順や異なる手順が必要になります。

### ユーザー属性でパーソナライズされたキャンペーンのテスト {#testing-campaigns-personalized-with-user-attributes}

メッセージで[パーソナライゼーション]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/overview)を使用している場合、キャンペーンを適切にプレビューし、ユーザーデータがコンテンツに正しく反映されていることを確認するために、追加の手順が必要です。

テストメッセージを送信する際は、**Select Existing User**または**Custom User**としてプレビューするオプションを選択してください。

![パーソナライズされたメッセージのテスト]({% image_buster /assets/img_archive/personalized_testing.png %}){: style="max-width:70%;" }

#### 既存のユーザーを選択する {#selecting-an-existing-user}

既存のユーザーを選択する場合、検索フィールドに特定のユーザーIDまたはメールアドレスを入力します。次に、ダッシュボードプレビューを使用して、そのユーザーにメッセージがどのように表示されるかを確認し、そのユーザーが受け取る内容を反映したテストメッセージをデバイスに送信します。

![ユーザーを選択する]({% image_buster /assets/img_archive/personalized_testing_select.png %})

#### カスタムユーザーを選択する {#selecting-a-custom-user}

カスタムユーザーとしてプレビューする場合、ユーザーの名やカスタム属性など、パーソナライゼーションに使用できるさまざまなフィールドにテキストを入力します。同様に、自分のメールアドレスを入力してデバイスにテストを送信できます。

![カスタムユーザー]({% image_buster /assets/img_archive/personalized_testing_custom.png %})

#### 既存のユーザーをカスタマイズする {#customizing-an-existing-user}

メッセージ内のダイナミックコンテンツをテストするために、ランダムまたは既存のユーザーの個々のフィールドを編集できます。**Edit**を選択すると、選択したユーザーが編集可能なカスタムユーザーに変換されます。

![「Edit」ボタンがある「Preview as a User」タブ]({% image_buster /assets/img_archive/edit_user_preview.png %}){: style="max-width:50%;"}

### カスタムイベントプロパティでパーソナライズされたキャンペーンのテスト {#testing-campaigns-personalized-with-custom-event-properties}

[カスタムイベントプロパティ]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties)でパーソナライズされたキャンペーンのテストは、前述の他のタイプのキャンペーンのテストとは若干異なります。

{% tabs local %}
{% tab 手動でトリガー %}

#### 方法 1: キャンペーンを手動でトリガーする {#method-1-triggering-campaign-manually}

カスタムイベントプロパティを使用したキャンペーンをテストする堅牢な方法として、キャンペーンを自分でトリガーできます。

1. イベントプロパティを含むコピーを作成します。

![プロパティを含むテストメッセージの作成]({% image_buster /assets/img_archive/testeventproperties-compose.png %})

{: start="2"}
2. [アクションベース配信]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery)を使用して、イベントの発生時にキャンペーンを配信します。

{% alert note %}
iOSプッシュキャンペーンをテストする場合、iOSは現在開いているアプリにプッシュ通知を配信しないため、アプリを終了するための時間を確保するために遅延を1分に設定する必要があります。他のタイプのキャンペーンは即時配信に設定できます。
{% endalert %}

![テストメッセージの配信]({% image_buster /assets/img_archive/testeventproperties-delivery.png %})

{: start="3"}
3. テストフィルターを使用するか、自分のメールアドレスをターゲットにして、テスト用にユーザーをターゲットし、キャンペーンの作成を完了します。

![テストメッセージのターゲティング]({% image_buster /assets/img_archive/testeventproperties-target.png %})

{: start="4"}
4. アプリに移動してカスタムイベントを実行します。

キャンペーンがトリガーされ、イベントプロパティでカスタマイズされたメッセージが表示されます。

![テストメッセージの例]({% image_buster /assets/img_archive/testeventproperties-message2.png %})

{% endtab %}
{% tab テストメッセージ %}

#### 方法 2: 自分自身にテストメッセージを送信する {#method-2-sending-yourself-a-test-message}

カスタムユーザーIDを保存している場合は、カスタマイズされたテストメッセージを自分自身に送信してキャンペーンをテストすることもできます。

1. キャンペーンのコピーを作成します。
2. **Test**タブを選択し、**Customized User**を選択します。
3. ページの下部にカスタムイベントプロパティを追加し、上部のボックスにユーザーIDまたはメールアドレスを追加します。
4. **Send Test**を選択して、プロパティでパーソナライズされたメッセージを受信します。

![カスタマイズされたユーザーを使用したテスト]({% image_buster /assets/img_archive/testeventproperties-customuser.png %})

{% endtab %}
{% tab Liquid %}

#### 方法 3: Liquidを使用する {#method-3-using-liquid}

Liquidで値を手動で入力して、カスタムイベントプロパティをテストできます。

1. メッセージエディターで、カスタムイベントプロパティの値を入力します。
2. **Preview as a User**タブを選択して、正しいメッセージが表示されることを確認します。

{% endtab %}
{% endtabs %}

## 制限事項 {#limitations}

テストメッセージが、実際のユーザーに送信されるキャンペーンやキャンバスと同じように動作しない場合がいくつかあります。これらのケースでは、キャンペーンやキャンバスを限定されたテストユーザーに送信して、動作を検証することを検討してください。

- テストメッセージからBrazeの[ユーザー設定センター]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center)を表示すると、**Save Preferences**ボタンが無効になります。ユーザー設定センターのLiquidタグも有効なリンクに解決されない場合があります。これは想定された動作です。エンドツーエンドのテストを行うには、[ユーザー設定センターのテスト]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center#testing-preference-centers)を参照してください。
- アプリ内メッセージやContent Cardsのテストでは、ターゲットユーザーが対象デバイスのプッシュトークンを持っている必要があります。
- メール内の購読解除リンクをテストする場合は、テストユーザーのメールアドレスが該当するワークスペースに含まれていることを確認してください。
- `List-Unsubscribe`ヘッダーは、テストメッセージ機能で送信されるメールには含まれません。
- シードグループユーザーに送信されたメールは、ユーザープロファイルのキャンペーン受信リストを更新せず、ダッシュボード分析の送信数も増加しません。

## トラブルシューティング {#troubleshooting}

### アプリ内メッセージ {#in-app-messages}

アプリ内メッセージキャンペーンがプッシュキャンペーンによってトリガーされない場合は、アプリ内キャンペーンのセグメンテーションを確認し、ユーザーがプッシュメッセージを受信する**前に**ターゲットオーディエンスの条件を満たしていることを確認してください。

AndroidおよびiOSでのテスト送信では、**プッシュ許可をリクエスト**のクリック時動作を使用するアプリ内メッセージが一部のデバイスで表示されない場合があります。回避策として以下をご確認ください：
- **Android:** デバイスがAndroid 13以降で、Android SDKバージョン21.0.0以降である必要があります。また、アプリ内メッセージが表示されるデバイスにシステムレベルのプロンプトがすでに表示されている場合もあります。**今後表示しない**を選択した可能性があるため、再テストの前にアプリを再インストールして通知権限をリセットする必要がある場合があります。
- **iOS:** 開発者チームがアプリのプッシュ通知の実装を確認し、プッシュ許可をリクエストするコードを手動で削除することをお勧めします。詳細については、[プッシュプライマーアプリ内メッセージ]({{site.baseurl}}/user_guide/channels/push/best_practices)を参照してください。

アクションベースのアプリ内メッセージキャンペーンを配信するには、REST APIではなくBraze SDKを通じてカスタムイベントを記録する必要があります。これにより、ユーザーは対象となるアプリ内メッセージをデバイスに直接受信できます。ユーザーはセッション中にイベントを実行した場合にアプリ内メッセージを受信します。