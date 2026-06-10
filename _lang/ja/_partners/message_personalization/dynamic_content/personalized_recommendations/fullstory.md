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

## この統合について {#about-this-integration}

BrazeでFullstoryのインサイトを活用して、ユーザーのWebサイトやアプリ体験の一瞬一瞬を捉えた画像を構築し、文脈に応じたメッセージングを配信できます。FullstoryのセッションサマリーAPIにより、ユーザーの閲覧行動に関する詳細なメタデータをキャプチャしてBrazeメッセージングで使用できます。これは、Canvasのような複数ステップのメッセージングジャーニーで活用する際に特に威力を発揮します。

Fullstoryのセッションサマリーデータのリアルタイムの価値は、コネクテッドコンテンツを通じて最大限に活用されます。コネクテッドコンテンツをCanvasコンテキストステップで使用することで、ユーザーのCanvasジャーニーを通じてFullstoryのデータを保存し、その後のCanvasステップで使用できます。これにより、カスタムイベントや属性を通じてBrazeユーザープロファイルにこのデータを書き込む必要もなくなります。

以下の例では、エージェントAI Canvasステップでcanvasコンテキストデータを活用し、ユーザーに放棄カートを取り戻すよう促す最適なメッセージを生成しています。ただし、データを活用してメッセージを直接パーソナライズしたり、オーディエンスパスでユーザーのジャーニーを決定したり、後続のメッセージングステップで使用するコピーやアセットを決定したりすることもできます。

## 前提条件 {#prerequisites}

始める前に、以下のものが必要です。

| 必要条件 | 説明 |
|-----------------------|-----------------|
| FullstoryセッションAPI認証トークン | 以下のステップ1を参照してください。 |
| Brazeコネクテッドコンテンツ認証トークンが有効であること | 早期アクセスについては、下記の注記を参照してください。 |
| Braze Canvasコンテキストステップ | 早期アクセスについては、下記の注記を参照してください。 |
| Braze AIエージェントステップが有効であること | 早期アクセスについては、下記の注記を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

{% alert important %}
Brazeエージェント、Canvasコンテキスト、およびコネクテッドコンテンツ認証トークンはすべて早期アクセス段階です。このソリューションの活用に興味がある場合は、Brazeのカスタマーサクセスマネージャーにこれらのツールの有効化についてご相談ください。
{% endalert %}

## Fullstoryの統合 {#integrate-fullstory}

### ステップ1: セッションサマリーAPIイネーブルメントのためにFullstoryを設定する {#step-1}

#### ステップ1.1: セッションサマリーAPIエンドポイントの認証トークンを取得する {#step-11-retrieve-the-authentication-token-for-the-session-summary-api-endpoint}

[Fullstory APIキー](https://developer.fullstory.com/server/authentication/)を作成するには：

1. Fullstoryで、**Settings** > **API Keys**に移動します。
2. **Standard**権限レベルを選択します。
3. キー値は一度しか表示されないため、すぐにコピーしてください。

#### ステップ1.2: セッションサマリープロファイルIDを作成する {#step-12-create-a-session-summary-profile-id}

[Fullstoryのガイダンス](https://developer.fullstory.com/anywhere/activation/ai-session-summary-api/#step-1-creating-and-managing-summary-profiles)に従い、専用エンドポイントを使用してセッションサマリープロファイルを作成します。ここで、セッションサマリーのレスポンスがBrazeに提供するデータの種類を定義します。

このリクエストに対するレスポンスで、FullstoryはセッションプロファイルIDを提供します。このプロファイルIDは、以下のユースケースで使用されるコネクテッドコンテンツリクエストボディの重要な構成要素です。

### ステップ2: コネクテッドコンテンツのトークン認証を作成する {#step-2-create-the-connected-content-token-authentication}

1. Brazeで、**Settings** > **Workspace Settings** > **Connected Content** > **Add Credential** > **Token Authentication**に移動します。
2. 認証名を`fullstory`とします。
3. ヘッダーキー「Authorization」を追加します。前のステップでFullstoryが提供したヘッダー値を入力します。
4. **Allowed Domain**の下に、**api.fullstory.com**を入力します。

![認証情報の編集フィールドを示すBrazeのスクリーンショット]({% image_buster /assets/img/fullstory/1.png %}){: style="max-width:50%;"}

## ユースケース {#use-cases}

### ダイナミックなメッセージジャーニーを作成する {#create-dynamic-message-journeys}

Fullstoryの[Activation Streams](https://help.fullstory.com/hc/en-us/articles/360045134554-Streams)を使用すると、ユーザーとの重要なインタラクションの直後にBraze Canvasesをトリガーできます。この統合の威力は、システムがFullstoryからBrazeに自動的に渡す固有の`client_session_id`（{% raw %}`{{canvas_entry_properties.${client_session_id}}}`{% endraw %}でアクセス可能）にあります。このIDがキーとして機能し、Brazeはユーザーが体験した内容の完全なセッションサマリーを取得できます。

Canvasコンテキストステップとコネクテッドコンテンツを活用することで、このIDを使用してFullstoryにAPIリクエストを行い、セッションデータを取得し、ジャーニーの後半で使用するために変数として保存できます。

![BrazeのCanvasコンテキストステップ。コンテキスト変数「summary_result」が作成され、Fullstoryへのコネクテッドコンテンツコールでセッションサマリーが取得されている]({% image_buster /assets/img/fullstory/2.png %})

先に作成した認証トークンを使用して、以下のリクエスト構造でセッションサマリーデータを取得します。

{% raw %}
```bash
{% connected_content https://api.fullstory.com/v2/sessions/{{canvas_entry_properties.${client_session_id} | url_encode}}/summary?config_profile=[YOUR-FULLSTORY-PROFILE-ID] :auth_credentials fullstory :save summary_result %}
{{summary_result | as_json_string }}
```
{% endraw %}

{% alert note %}
レスポンスはLiquidタグ{% raw %}`{{context.${summary_result}.response}}`{% endraw %}として保存されます。このContextタグは、その後のCanvasステップで使用します。
{% endalert %}

この段階で、Canvasはコネクテッドコンテンツコールのレスポンスにアクセスでき、ユーザーセッションのメッセージペイロード全体が含まれています。

{% details セッションサマリーAPIからのペイロード例 %}

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

ユーザーのCanvasジャーニーの後半でコンテキストLiquidタグを使用して、上記のオブジェクトで利用可能なデータを活用できます。以下のステップでは、[エージェント]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/agent_step/)ステップでこのデータを使用する方法を示します。

{% alert note %}
予期しない動作を避けるために、コンテキストステップの後にオーディエンスパスステップを含めてください。このステップでは、Contextタグが空の場合（コネクテッドコンテンツコールが失敗したか、情報を返さなかったことを示す）にユーザーをコンテキストから外すことができます。

![Brazeのオーディエンスパスステップ]({% image_buster /assets/img/fullstory/3.png %})

{% endalert %}

### 適切なコピーを作成する {#produce-appropriate-copy}

FullstoryによってトリガーされたCanvasに[エージェントステップ]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)を作成し、上記で説明したコンテキストステップを含めることで、エージェントでFullstoryのセッションサマリーデータを参照できます。

この例では、このデータを使用してBrazeエージェントがコンテンツカードで使用する適切なメッセージコピーを生成し、ユーザーに放棄されたバスケットに戻るよう促すことができます。

![プロンプトが表示されたBrazeエージェントコンテキストクリエイターのスクリーンショット]({% image_buster /assets/img/fullstory/4.png %})

このステップで作成するコンテキストLiquidタグには、先に作成したAIエージェントステップで使用したコンテキストLiquidタグと同じ名前を使用してください。

ユースケースによって必要なプロンプトは異なります。効果的なエージェントプロンプトを作成するためのベストプラクティスについては、[指示の書き方]({{site.baseurl}}/user_guide/brazeai/agents/reference/#writing-instructions)を参照してください。

Canvasで、AIエージェントステップを選択し、ドロップダウンから**Session Context**エージェントを選択します。出力を変数として保存します。この場合は「message」で、Liquidタグ{% raw %}`{{context.${message}.message}}`{% endraw %}を使用してメッセージコピーに配置できます。

![プロンプトが表示されたBrazeエージェントコンテキストCanvasステップのスクリーンショット]({% image_buster /assets/img/fullstory/5.png %})

AIエージェントが作成したコピーを活用するメッセージステップを作成します。このステップではLiquidタグを使用します。

{% alert important %}
FullstoryのセッションサマリーAPIは、機密性の高い識別可能なユーザーデータを返す可能性があります。PII（個人を特定できる情報）を扱う際のコンプライアンスを確保するために、このユースケースを活用する前に、FullstoryのデータキャプチャルールがPIIを除外していることを確認してください。
{% endalert %}