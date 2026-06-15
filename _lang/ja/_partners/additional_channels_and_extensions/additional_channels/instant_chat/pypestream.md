---
nav_title: Pypestream
article_title: Pypestream
description: "この参考記事では、ブランドとのデジタルエンゲージメントを強化できるフルスタックの会話型AIプラットフォームであるBrazeとPypestreamのパートナーシップについて説明します。"
alias: /partners/pypestream/
page_type: partner
search_tag: Partner

---

# Pypestream

> [Pypestream](https://www.pypestream.com) はフルスタックの会話型AIプラットフォームであり、特許取得済みのオールインワン型クラウドメッセージングを提供し、ブランドを「常時稼働」状態のデジタルエンティティに変換します。Pypestreamにより、ブランドは没入型のユーザーエクスペリエンス、高度なNLU機能、バックエンドシステムへのリアルタイム統合を活用しながら、すべての顧客と大規模なオムニチャネルの会話を行えるようになります。

_この統合はPypestreamによって管理されています。_

## 統合について {#about-the-integration}

BrazeとPypestreamの統合により、最初のアウトリーチから会話エクスペリエンスへのルーティング、インテリジェントなリターゲティングによるオムニチャネルのフォローアップまで、エンドツーエンドのカスタマーライフサイクルをシームレスにオーケストレーションできます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
|---|---|
| Pypestreamアカウント | このパートナーシップを活用するには、[Pypestreamアカウント](https://www.pypestream.com/contact-us/)が必要です。<br><br>サブスクライブ後、Pypestreamチームが、Brazeと統合する会話型AIソリューションの構築を開始するための専用環境の設定を支援します。 |
| Braze REST APIキー | `users.track` 権限を持つBraze REST APIキー。<br><br>これは、Brazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| Braze RESTエンドポイント | RESTエンドポイントのURL。エンドポイントはインスタンスの[Braze URL]({{site.baseurl}}/api/basics/)に応じて異なります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## ユースケース {#use-cases}

BrazeとPypestreamの連携により、キャンバスで以下のような一般的なユースケースを実現できます。
* **インテリジェントなリターゲティング**：Pypestreamで収集されたリッチなデータポイントをすべて活用して、ユーザーがブランドとの会話エンゲージメントを終えた後にBraze キャンバスでリターゲティングします。
* **ダイナミックターゲティング**：特定のコホートやセグメントに基づいて既存顧客や見込み顧客にコンタクトし、Pypestreamを介してカスタマイズされた会話エクスペリエンスを提供します。
* **文脈に応じた顧客インサイト**：エンドユーザー（既存の顧客または見込み客）がWebサイトでやり取りをした後、Pypestream Event Listenerから取り込んだWebページタグとBrazeに保存されている顧客データを組み合わせることで、完全にパーソナライズされ、コンテキストに即した会話型インタラクションを提供できます。

## 統合 {#integration}

Pypestreamはサーバーレスの統合レイヤーを活用し、さまざまなプラットフォームへのカスタム統合を行います。このレイヤーは、構築される会話フローのデータ要件をサポートするために、サービスやシステムとのインターフェースに使用されます。これらの統合はアクションノード統合と呼ばれ、通常Pythonで記述され、Pypestreamプラットフォームを使用してデプロイされます。アクションノードがインスタンス化されると、Braze APIのどのエンドポイントにも柔軟に統合でき、結果をさまざまな方法で評価できるようになります。

{% alert note %}
Pypestreamアクションノードの概要と設定手順については、この[Pypestreamの記事](https://pypestream.atlassian.net/servicedesk/customer/kb/view/669352070)を参照してください。このドキュメントにアクセスするには、Pypestreamの顧客である必要があります。
{% endalert %}

### ステップ1:エンドポイントの設定を行う {#step-1-set-endpoint-configurations}

Braze RESTエンドポイントURLやBraze APIキーなどの主要な設定値は、ソリューションの`app.py`ファイルで設定する必要があります。

```
import os

NAME = '{ CUSTOMER NAME }'
BOTS = []
CSV_BOTS = ['{ SOLUTION NAME }']
PATH = os.path.dirname(__file__)

PARAMS = {
    'sandbox': {
        #Braze
        'braze_url': '{ BRAZE ENDPOINT URL }',
        'braze_api_key': '{ BRAZE API KEY }',
        'braze_user_track': 'users/track'
    },
    'prod': {

        #Braze
        'braze_url': '{ BRAZE ENDPOINT URL }',
        'braze_api_key': '{ BRAZE API KEY }',
        'braze_user_track': 'users/track'
    },
}
```

### ステップ2:アクションノードテンプレートを開発する {#step-2-develop-action-node-template}

アクションノードは、前のステップで設定されたそれぞれのBrazeエンドポイントを使用して、ソリューションがデプロイされた環境を活用します。このステップでは、特定のBrazeエンドポイントを統合するためのアクションノードを開発します。統合を開発する際のガイドとして、以下のテンプレートを使用してください。

```
# -*- coding: utf-8 -*-
r'''
    ______  ______  _____________________  _________    __  ___
   / __ \ \/ / __ \/ ____/ ___/_  __/ __ \/ ____/   |  /  |/  /
  / /_/ /\  / /_/ / __/  \__ \ / / / /_/ / __/ / /| | / /|_/ /
 / ____/ / / ____/ /___ ___/ // / / _, _/ /___/ ___ |/ /  / /
/_/     /_/_/   /_____//____//_/ /_/ |_/_____/_/  |_/_/  /_/
Action Node Script for Braze Integration

Parameters
----------
POST Request to the User Track Braze Endpoint (users/track)

{
  "api_base_url": "{env.braze_url}",
  "req_endpoint_path": "users/track",
  "req_method": "POST",
  "req_headers": {
    "Authorization": "{YOUR-REST-API-KEY}"
    "Content-Type": "application/json"
  },
  "req_body": {
        "api_key": "{env.braze_api_key}",
        "attributes": [{
                "external_id": "{HOLDER_EMAIL}",
                ...
        }],
        "events": [
            ...
        ]
}

Returns
-------
Creates and/or Updates User Details within Braze dashboard

'''
import requests
from .. import app

class BrazeExample:
    def execute(self, log, payload=None, context=None):
        try:
            # initialize payload variables
            app_params = app.PARAMS[context['env']]
            req_params = {
                "attributes": [{
                    "external_id": "{ USER_ID }",
                    # include add'tl user details in this section
                    # refer to the Braze API Documentation for User Track REST API Endpoint for more details
                }],
                "events": [],
                "partner" : 'pypestream'
            }
            req_url = '{}/{}'.format(
                app_params['braze_url'],
                app_params['braze_user_track']
            )
            req_headers = {
                "Authorization": app_params['braze_api_key']
                "Content-Type": "application/json"
            }

            resp = requests.post(req_url,
                                params=req_params,
                                headers=req_headers)

            log('BrazeExample API response: {}'.format(resp.text))

            if resp.status_code == 400:
                return {'success': 'error'}

            return {'success': 'true'}

        except Exception as err:
            log('BrazeExample Exception error: {}'.format(err))

        return {'success': 'error'}
```
### ステップ3:ソリューションデザインを更新する {#step-3-update-the-solution-designs}

Braze REST APIと統合する最後のステップでは、前のステップで開発したアクションノードを使用するように、Pypestreamの[Design Studio](https://platform.pypestream.com/design-studio/)内でフローを設定します。

{% alert note %}
Design Studioでモードを設定する方法の概要については、この[Pypestreamの記事](https://pypestream.atlassian.net/servicedesk/customer/kb/view/669352070)を参照してください。このドキュメントにアクセスするには、Pypestreamの顧客である必要があります。
{% endalert %}

## 統合のユースケース {#integration-use-case}

前提条件が満たされ、アクションノード構造が作成されると、開発者はBraze APIエンドポイントとのインタラクションを行うためのブランクのキャンバスを使用できます。この例では、アクションノードをBrazeの[`/user/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)に統合するために必要な手順を示します。具体的には、Pypestreamの会話フローに入る特定のユーザーを追跡するためにユーザープロファイルを作成します。

### ステップ1:会話の中でユーザーからデータを収集する {#step-1-collect-data-from-the-user-in-conversation}

ユーザーがPypestreamセッションに入ると、収集されるデータの詳細は、その時点でのユースケースに完全に依存します。Brazeでユーザープロファイルを作成するには、目的のエンドポイントに必要なフィールドを会話で収集する必要があります。

たとえば、ソリューションがBrazeの`/user/track`エンドポイントの会話中にユーザーから次の情報を収集するとします。

* 名
* 姓
* メールアドレス
* 生年月日
* 居住地の市区町村
* オペレーティングシステム

このデータをBrazeプラットフォームに送信して、このユーザーのエンゲージメントを追跡し、将来的にリターゲティングすることが可能になります。一般的なアプリケーションについては、[ユースケースリスト](#use-cases)をご覧ください。

### ステップ2:アクションノード構造にデータを入力する {#step-2-populate-data-in-the-action-node-structure}

アクションノードを開発するための同じ構造を活用して、ユーザーから収集したデータをアクションノードに入力し、`/user/track`エンドポイントを経由してBrazeに送信できます。

```
# -*- coding: utf-8 -*-
r'''
    ______  ______  _____________________  _________    __  ___
   / __ \ \/ / __ \/ ____/ ___/_  __/ __ \/ ____/   |  /  |/  /
  / /_/ /\  / /_/ / __/  \__ \ / / / /_/ / __/ / /| | / /|_/ /
 / ____/ / / ____/ /___ ___/ // / / _, _/ /___/ ___ |/ /  / /
/_/     /_/_/   /_____//____//_/ /_/ |_/_____/_/  |_/_/  /_/
Action Node Script for Braze Integration

Parameters
----------
POST Request to the User Track Braze Endpoint (users/track)

{
  "api_base_url": "{env.braze_url}",
  "req_endpoint_path": "users/track",
  "req_method": "POST",
  "req_headers": {
    "Content-Type": "application/json"
  },
  "req_body": {
        "api_key": "{env.braze_api_key}",
        "attributes": [{
                "external_id": "{HOLDER_EMAIL}",
                ...
        }],
        "events": [
            ...
        ],
        "partner" : 'pypestream'
}

Returns
-------
Creates and/or Updates User Details within Braze dashboard

'''
import requests
from .. import app

class BrazeExample:
    def execute(self, log, payload=None, context=None):
        try:
            # initialize payload variables
            app_params = app.PARAMS[context['env']]
            req_params = {
                "attributes": [{
                    "external_id": "{ USER_ID }",
                    "first_name": "{ FIRST_NAME }",
                    "last_name": "{ LAST_NAME }",
                    "email": "{ EMAIL_ADDRESS }",
                    "dob": "{ DATE_OF_BIRTH }",
                    "home_city": "{ CITY_OF_RESIDENCE }",
                    "operating_system": "{ OPERATING_SYSTEM }" #custom attributes can be added here as well
                    # include add'tl user details in this section
                    # refer to the Braze API Documentation for User Track REST API Endpoint for more details
                }],
                "events": [{
                    "external_id": "{ USER_ID }",
                    "name": "{ NAME_OF_EVENT }",
                    "time": "{ EVENT_TIME }"
                }],
                "partner" : 'pypestream'
            }
            req_url = '{}/{}'.format(
                app_params['braze_url'],
                app_params['braze_user_track']
            )
            req_headers = {
                "Authorization": app_params['braze_api_key']
                "Content-Type": "application/json"
            }

            resp = requests.post(req_url,
                                params=req_params,
                                headers=req_headers)

            log('BrazeExample API response: {}'.format(resp.text))

            if resp.status_code == 400:
                return {'success': 'error'}

            return {'success': 'true'}

        except Exception as err:
            log('BrazeExample Exception error: {}'.format(err))

        return {'success': 'error'}
```

### ステップ3:アクションノードの成功/失敗時にリダイレクトするようにソリューションフローを更新する {#step-3-update-solution-flows-to-redirect-upon-successfailure-of-action-node}

最後に、各ソリューションの設計では、アクションノードAPI呼び出しが成功したかどうかに基づいて、ユーザーをノードにルーティングできます。アクションノードがエラーメッセージを受信した場合、エンドユーザーを慎重に処理する必要があります。