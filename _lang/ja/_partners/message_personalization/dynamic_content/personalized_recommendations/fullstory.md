---
nav_title: Fullstory
article_title: Fullstory
description: "この参考記事では、BrazeとFullstoryのパートナーシップについて説明します。"
alias: /partners/fullstory/
page_type: partner
search_tag: Partner
---

# Fullstory

> [Fullstory](https://www.fullstory.com/)の行動データプラットフォームは、テクノロジーリーダーがより良い、より情報に基づいた意思決定を行えるよう支援します。デジタル行動データを分析スタックに注入することで、Fullstoryの特許取得済みテクノロジーは、質の高い行動データのパワーを大規模に引き出し、すべてのデジタル訪問をアクション可能なインサイトに変換します。

*この統合はFullstoryによって維持されています。*

## この連携について {#about-this-integration}

FullstoryのインサイトをBrazeで活用することで、ユーザーのWebサイトやアプリ体験をリアルタイムで把握し、文脈に応じたメッセージングを配信できます。FullstoryのSession Summary APIを使用すると、ユーザーの閲覧行動に関する詳細なメタデータを取得してBrazeのメッセージングに活用できます。これは、キャンバスのようなマルチステップメッセージングジャーニーで使用する場合に特に効果的です。

Fullstoryのセッションサマリーデータのリアルタイム価値は、Connected Contentを通じて最大限に活用できます。キャンバスのコンテキストステップでConnected Contentを使用すると、ユーザーのキャンバスジャーニー全体を通じてFullstoryのデータを保存し、後続のキャンバスステップで利用できます。これにより、カスタムイベントや属性を通じてBrazeのユーザープロファイルにデータを書き込む必要もなくなります。

以下の例では、キャンバスコンテキストデータをAgent AIキャンバスステップで活用し、放棄カートを再開するようユーザーに促す最適なメッセージを生成しています。ただし、このデータを活用してメッセージを直接パーソナライズしたり、オーディエンスパスでユーザーのジャーニーを決定したり、後続のメッセージングステップで使用するコピーやアセットを決定したりすることもできます。

## 前提条件 {#prerequisites}

始める前に、以下が必要です。

|要件     | 説明 |
|-----------------------|-----------------|
| Fullstory Session API認証トークン   | このガイドのステップ1を参照してください。 |
| Braze Connected Content認証トークンの有効化 | このセクションの早期アクセスに関する注記を参照してください。 |
| Brazeキャンバスコンテキストステップ | このセクションの早期アクセスに関する注記を参照してください。 |
| Braze AIエージェントステップの有効化 | このセクションの早期アクセスに関する注記を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## Fullstoryを統合する {#integrate-fullstory}

### ステップ1：Session Summary APIの有効化に向けてFullstoryを設定する {#step-1}

#### ステップ1.1：Session Summary APIエンドポイントの認証トークンを取得する {#step-11-retrieve-the-authentication-token-for-the-session-summary-api-endpoint}

[Fullstory APIキー](https://developer.fullstory.com/server/authentication/)を作成するには：

1. Fullstoryで、**設定** > **APIキー**に移動します。
2. **Standard**権限レベルを選択します。
3. キーの値は一度しか表示されないため、すぐにコピーしてください。

#### ステップ1.2：セッションサマリープロファイルIDを作成する {#step-12-create-a-session-summary-profile-id}

[Fullstoryのガイダンス](https://developer.fullstory.com/anywhere/activation/ai-session-summary-api/#step-1-creating-and-managing-summary-profiles)に従い、専用のエンドポイントを使用してセッションサマリープロファイルを作成します。ここで、セッションサマリーのレスポンスからBrazeにどのようなデータを提供するかを定義します。

このリクエストのレスポンスで、Fullstoryはセッションプロファイルを提供します。このプロファイルIDは、以下のユースケースで使用するConnected Contentリクエストボディの重要な構成要素です。

### ステップ2：Connected Contentのトークン認証を作成する {#step-2-create-the-connected-content-token-authentication}

1. Brazeで、**設定** > **ワークスペース設定** > **Connected Content** > **認証情報を追加** > **トークン認証**に移動します。
2. 認証名を`fullstory`にします。
3. ヘッダーキー「Authorization」を追加します。前のステップでFullstoryから提供されたヘッダー値を入力します。
4. **許可されたドメイン**に、**api.fullstory.com**と入力します。

![Brazeの認証情報の編集フィールドを示すスクリーンショット]({% image_buster /assets/img/fullstory/1.png %}){: style="max-width:50%;"}

## ユースケース {#use-cases}

### ダイナミックなメッセージジャーニーを作成する {#create-dynamic-message-journeys}

Fullstoryの[Activation Streams](https://help.fullstory.com/hc/en-us/articles/360045134554-Streams)を使用すると、主要なユーザーインタラクションの直後にBrazeキャンバスをトリガーできます。この連携の強みは、一意の`client_session_id`（{% raw %}`{{canvas_entry_properties.${client_session_id}}}`{% endraw %}でアクセス可能）にあり、FullstoryからBrazeへ自動的に渡されます。このIDはキーとして機能し、Brazeがユーザーの体験内容を正確に把握するための完全なセッションサマリーを取得できるようにします。

キャンバスのコンテキストステップとConnected Contentを活用することで、このIDを使ってFullstoryへAPIリクエストを送信し、セッションデータを取得して、ジャーニーの後続ステップで使用する変数として保存できます。

![Brazeキャンバスのコンテキストステップ。コンテキスト変数「summary_result」が作成され、Fullstoryへの Connected Content 呼び出しによってセッションサマリーを取得し、データが格納されている様子]({% image_buster /assets/img/fullstory/2.png %})

先ほど作成した認証トークンを使用して、以下のリクエスト構造でセッションサマリーデータを取得します。

{% raw %}
```bash
{% connected_content https://api.fullstory.com/v2/sessions/{{canvas_entry_properties.${client_session_id} | url_encode}}/summary?config_profile=[YOUR-FULLSTORY-PROFILE-ID] :auth_credentials fullstory :save summary_result %}
{{summary_result | as_json_string }}
```
{% endraw %}

{% alert note %}
レスポンスはLiquidタグ{% raw %}`{{context.${summary_result}.response}}`{% endraw %}として保存されます。このコンテキストタグを後続のキャンバスステップで使用してください。
{% endalert %}

この段階で、キャンバスはConnected Content呼び出しのレスポンスにアクセスでき、ユーザーのセッションに関するメッセージペイロード全体が含まれています。

{% details セッションサマリーAPIからのペイロードの例 %}

{% raw %}
```bash
{
    "response": {
        "primary_goal": "User attempted to update payment method.",
        "issues_encountered": [
            "Received 'invalid card number' error twice.",
            "Clicked 'Submit' button multiple times with apparent frustration (based on event patterns)."
        ],
        "final_action": "Navigated away from payment page to dashboard.",
        "reason_for_termination_suggestion": "Could not update payment method successfully.",
        "help_pages_visited": [
            "/help/payment-errors"
        ]
    },
    "response_schema": {
        "type": "OBJECT",
        "properties": {
            "primary_goal": {
                "type": "STRING",
                "description": "A summary of the user's main objective during the session."
            },
            "issues_encountered": {
                "type": "ARRAY",
                "description": "A list of problems or errors the user faced.",
                "items": {
                    "type": "STRING",
                    "description": "A description of a single issue."
                }
            },
            "final_action": {
                "type": "STRING",
                "description": "The last significant action the user took before the session ended."
            },
            "reason_for_termination_suggestion": {
                "type": "STRING",
                "description": "A suggested reason for why the user ended their session."
            },
            "help_pages_visited": {
                "type": "ARRAY",
                "description": "A list of URLs for help or documentation pages the user visited.",
                "items": {
                    "type": "STRING",
                    "description": "The URL of a help page."
                }
            }
        },
        "required": [
            "primary_goal",
            "issues_encountered",
            "final_action",
            "reason_for_termination_suggestion",
            "help_pages_visited"
        ]
    }
}
```
{% endraw %}
{% enddetails %}

上記のオブジェクトで利用可能なデータは、コンテキストLiquidタグを使って、ユーザーのキャンバスジャーニーの後続ステップで活用できます。以下のステップでは、このデータを[エージェント]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step)ステップで使用する方法を示します。

{% alert note %}
予期しない動作を避けるために、コンテキストステップの後にオーディエンスパスステップを追加してください。コンテキストタグが空の場合（Connected Content呼び出しが失敗したか、情報が返されなかったことを示します）、ユーザーをコンテキストからドロップアウトさせることができます。

![Brazeのオーディエンスパスステップ]({% image_buster /assets/img/fullstory/3.png %})

{% endalert %}

### 適切なコピーを生成する {#produce-appropriate-copy}

Fullstoryによってトリガーされるキャンバスに[エージェントステップ]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents)を作成し、このセクションで説明したコンテキストステップを含めることで、エージェント内でFullstoryのセッションサマリーデータを参照できます。

この例では、このデータを使用してBrazeエージェントがContent Cardで使用する適切なメッセージコピーを生成し、ユーザーに放棄カートへの復帰を促します。

![Brazeエージェントコンテキストクリエーターのスクリーンショット（プロンプト付き）]({% image_buster /assets/img/fullstory/4.png %})

このステップで作成するコンテキストLiquidタグには、先ほど作成したAIエージェントステップで使用するコンテキストLiquidタグと同じ名前を使用してください。

ユースケースに必要なプロンプトはケースによって異なります。効果的なエージェントプロンプトを作成するためのベストプラクティスについては、[インストラクションの作成]({{site.baseurl}}/user_guide/brazeai/agents/reference#writing-instructions)を参照してください。

キャンバスでAIエージェントステップを選択し、ドロップダウンから**Session Context**エージェントを選択します。出力を変数として保存します（この例では「message」）。Liquidタグ{% raw %}`{{context.${message}.message}}`{% endraw %}を使用してメッセージコピーに挿入できます。

![Brazeエージェントコンテキストキャンバスステップのスクリーンショット（プロンプト付き）]({% image_buster /assets/img/fullstory/5.png %})

AIエージェントが作成したコピーを活用するメッセージステップを作成します。このステップでLiquidタグを使用してください。

{% alert important %}
FullstoryのセッションサマリーAPIは、機密性のある個人識別可能なユーザーデータを返す場合があります。PII（個人識別情報）の取り扱いにおけるコンプライアンスを確保するため、このユースケースを活用する前に、Fullstoryのデータ取得ルールでPIIが除外されていることを確認してください。
{% endalert %}