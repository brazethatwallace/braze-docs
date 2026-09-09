---
nav_title: リンクテンプレート
article_title: リンクテンプレート
page_order: 4
description: "この記事では、メールでさまざまなタイプのリンクテンプレートを作成する方法について説明します。"
tool:
  - Templates
channel:
  - email

---

# リンクテンプレート {#link-templates}

> リンクテンプレートを使用すると、パラメーターの追加やURLの前置によって、メールキャンペーン用のダイナミックで再利用可能なリンクを作成できます。これにより、キャンペーンやメッセージ全体でURLの一貫性を確保できます。

{% alert note %}
リンクテンプレートはオプション機能です。**テンプレート**セクションに**メールリンクテンプレート**が表示されない場合は、アカウントマネージャーに連絡して機能を有効にしてください。
{% endalert %}

## 仕組み {#how-it-works}

リンクテンプレートは、主に以下のユースケースで使用されます。

- 特定のメールメッセージ内のすべてのリンクに Google Analytics のクエリパラメーターを追加する
- 特定のメールメッセージ内のすべてのリンクの先頭に URL を追加する

例えば、新製品の発売に向けたプロモーションメールキャンペーンを実施しているとします。リンクテンプレートを使用して、ユーザーを製品ページに誘導し、ユーザーの名前や特定のプロモーションコードを含むリンクをパーソナライズすることができます。これにより、リンクをクリックしたユーザーの数や購入に至ったユーザーの数を追跡できます。このようにして、リンク全体の一貫性を保ち、分析をより効果的に追跡できます。

## リンクテンプレートの作成 {#creating-a-link-template}

さまざまなニーズに対応するために、リンクテンプレートを無制限に作成できます。リンクテンプレートを作成するには、次の手順に従ってください。

1. **コンテンツ** > **メールリンク**に移動します。
2. **メールリンクテンプレートを作成**を選択します。
3. リンクテンプレートに名前を付けます。
4. （オプション）説明、チーム、またはタグを追加して、リンクテンプレートに関する詳細を付与します。
5. （オプション）トグルを選択すると、メールキャンペーンやキャンバスのリンクにリンクテンプレートが自動的に追加されます。これは、新規または既存のメールに新しいリンクを追加する際に適用されます。

作成できるリンクテンプレートには2種類あります。

- [URLの前に挿入するリンクテンプレート](#prepend-link-template)
- [URLの後に挿入するリンクテンプレート](#append-link-template)

リンクテンプレートと[Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)を使用する場合、一貫したレンダリングを確保するために、Liquidはbodyタグ内にのみ追加する必要があります。

### プリペンド：URLの前に挿入するリンクテンプレートの作成 {#prepend-link-template}

メールメッセージ内のリンクの前に文字列やURLを追加するには、次の手順に従ってください。

1. 新しいリンクテンプレートを作成します。
2. **Template Position**を**Before URL**に設定します。
3. URLの前に常に追加される文字列を入力します。

**Template preview**には、リンクテンプレートがURLの前にどのように挿入されるかの例が表示されます。

![URLの前にリンクテンプレートを挿入するプロセスの「Template Position」、「Prepend URL」、「Template Preview」フィールド。]({% image_buster /assets/img_archive/link_template_preappend.png %}){: style="max-width:90%;"}

### アペンド：URLの後に挿入するリンクテンプレートの作成 {#append-link-template}

メールメッセージ内のURLの後にクエリパラメータを追加する場合は、次の手順に従ってください。

1. 新しいリンクテンプレートを作成します。
2. **Template Position**を**After URL**に設定します。
3. 各URLの末尾にクエリパラメータ（`value=example`）を入力します。URLの末尾に複数のパラメータを追加できます。

![URLの後にリンクテンプレートを挿入するプロセスの「Template Position」、「Query Parameters」、「Template Preview」フィールド。]({% image_buster /assets/img_archive/link_template_postappend.png %}){: style="max-width:90%;"}

#### `utm_campaign`のLiquidタグ {#liquid-tags-for-utm_campaign}

`utm_campaign`のLiquidタグは、キャンペーンとキャンバスで異なります。

キャンペーンでは、以下を使用します。

{% raw %}
- `{{campaign.${name}}}` でキャンペーン名を取得
- `{{campaign.${message_name}}}` でメッセージバリアント名を取得
{% endraw %}

キャンバスでは、以下を使用します。

{% raw %}
- `{{canvas.${name}}}` でキャンバス名を取得
- `{{campaign.${name}}}` でキャンバスステップ名を取得（メッセージステップのみ）
{% endraw %}

Liquid、REST API、Currentsにおけるこれらの属性の詳細な比較については、[ソース間のキャンペーンとキャンバスの属性]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/campaign_and_canvas_attributes_across_sources)を参照してください。URLエンコードのガイダンスについては、[URL内のキャンペーン名]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags#campaign-names-in-urls)を参照してください。

## メールキャンペーンでのリンクテンプレートの使用 {#using-link-templates-in-email-campaigns}

リンクテンプレートを設定した後、メールに適用できます。

HTML エディターまたはドラッグ＆ドロップエディターでリンクテンプレートを適用するには、以下のステップに従ってください。

{% alert note %}
メールリンクテンプレートまたは[リンクエイリアス]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_aliasing)がワークスペースで有効になっている場合、更新された HTML エディターおよびドラッグ＆ドロップエディターで**リンク管理**タブにアクセスできます。
{% endalert %}

- **更新された HTML エディター:**「**コンテンツ**」タブで「**リンク管理**」を選択し、「**リンクテンプレートを追加**」を選択してリンクテンプレートを選び、「**追加**」を選択します。
- **ドラッグ＆ドロップエディター:**「**コンテンツ**」タブで「**リンク管理**」を選択し、「**リンクテンプレートを追加**」を選択してリンクテンプレートを選び、「**追加**」を選択します。

![ドラッグ＆ドロップエディターのリンク管理タブとリンクテンプレートのリスト例。]({% image_buster /assets/img_archive/link_template_messagecomposer2.png %})

{% alert note %}
リンクテンプレートはプレーンテキストには適用されません。そのため、Currentsではリンクテンプレートのパラメーターを含まないクリックが表示されることがあります。これらのクリックはメールのプレーンテキストバージョンからのものである可能性があります。
{% endalert %}

**リンク管理**タブでリンクテンプレートを追加すると、各テンプレートはテーブルに追加の列として表示されます。メール内の既存のリンクにすでにリンクテンプレートが追加されている場合、新しく追加されたリンクにもデフォルトでリンクテンプレートが追加されます。

{% alert tip %}
メッセージにリンクを含める際は、URL が `http://` または `https://` で始まるようにしてください。
{% endalert %}

## リンクテンプレートの管理 {#managing-link-templates}

リンクテンプレートを[複製]({{site.baseurl}}/user_guide/messaging/templates/managing_templates)することもできます。テンプレートとクリエイティブコンテンツの作成と管理の詳細については、[テンプレートとメディア]({{site.baseurl}}/user_guide/messaging/templates)を参照してください。

{% alert important %}
テンプレートのアーカイブは、現在リンクテンプレートでは利用できません。
{% endalert %}

## トラブルシューティング {#troubleshooting}

### UTMパラメータが見つからない {#missing-utm-parameters}

リンクテンプレートは、標準的なHTMLコメント（`<!-- ... -->`）内のリンクには適用されません。Outlookの条件付きコメント（例：`<!--[if mso]>`）については、ワークスペースでリンクエイリアスが有効になっている場合にリンクテンプレートが適用されます。リンクエイリアスが有効になっていないワークスペースでは、条件付きコメントは引き続きスキップされます。

### UTMパラメータがブラウザには表示されるがリンクには含まれない {#utm-parameters-present-in-browser-but-missing-from-links}

これは、メール内のURLパスが意図した完全なパスと一致しない場合（例えば、Webサイトの完全なURLとは異なる短縮パスや別のパス）に発生することがあります。

- **確認すべきこと：**メール内の`href`に、ページへの完全なパスが含まれていること（リダイレクトに依存する部分的なパスだけではないこと）。
- **想定される動作：**メール内のパスが不完全または異なる場合、リンクテンプレートのUTMパラメータは、クリック時にそのリンクに適用されないことがあります。Webサイトが訪問者を正しいページにリダイレクトする場合でも同様です。

たとえば、完全なリンクが`https://www.somewebsite.com/women/designer/johnjane`であるのに、メールで`https://www.somewebsite.com/designer/johnjane`を使用している場合、UTMパラメータがメールリンクに追加されないのは想定される動作です。

### LiquidでレンダリングされたリンクにUTMパラメータが含まれない {#utm-parameters-missing-from-liquid-rendered-links}

リンクテンプレートを適用する際、Brazeは各URLを解析してパラメータの追加位置を決定します。LiquidタグがレンダリングするURLが有効なURIとして解析できない場合、リンクテンプレートはサイレントにスキップされます。Liquid出力が正しい形式のURLを生成しているか確認してください。特定のユーザーでメッセージをプレビューし、レンダリングされたURLが有効であることを確認してテストしてください。URLのパスやクエリ文字列にLiquid変数が含まれている場合は、出力に無効な文字やエンコードの不備が含まれていないことを確認してください。

### テスト送信でUTM値が表示されない {#utm-values-missing-in-test-sends}

リンクテンプレートをテスト送信する場合、{% raw %}`{{${user_id}}}`{% endraw %}はレンダリングされません。代わりに、キャンペーンを複製して内部ユーザーのメールまたは`external_id`をターゲットに設定し、キャンペーンを起動して、リンクテンプレートのすべてのUTMパラメータが正しく入力されていることを確認してください。

## よくある質問 {#frequently-asked-questions}

リンクテンプレートに関するよくある質問の回答については、[テンプレートFAQ]({{site.baseurl}}/user_guide/messaging/templates/email_templates/faq)ページをご覧ください。