---
nav_title: データプライバシーとセキュリティ
article_title: BrazeAI Operatorのデータプライバシーとセキュリティ
page_order: 5
page_type: reference
description: "このリファレンス記事では、HIPAA準拠、データ保持、PII最小化、ガバナンスなど、BrazeAI Operatorがデータをどのように扱うかについて説明します。"
---

# BrazeAI Operatorのデータプライバシーとセキュリティ {#data-privacy-and-security-for-brazeai-operator}

> BrazeAI Operator<sup>TM</sup>はOpenAIと統合し、AIを活用したアシスタンスを提供します。この記事では、Operatorがデータをどのように扱うか、OpenAIとどのような情報が共有されるか、PII露出を最小限に抑えアクセスを制御する方法について説明します。

## Operatorがデータにアクセスする仕組み {#how-operator-accesses-data}

Operatorの顧客データへのアクセスは、厳密にイベント駆動型かつ呼び出しスコープに限定されており、永続的ではありません。Operatorが開いている間にユーザーメッセージやナビゲーションイベントが発生するたびに、OpenAIへの個別のHTTPリクエストがトリガーされます。常時接続や永続的なデータフィードはありません。

OpenAIはBrazeのデータストアやユーザーテーブル全体に直接アクセスすることはできません。LLMはアクティブなリクエストに関連付けられた特定のペイロードのみを受け取ります。

### 各リクエストに含まれるデータ {#what-data-is-included-in-each-request}

OpenAIに送信される各リクエストのペイロードには、以下が含まれる場合があります。

- **システムメタデータ:** Brazeが作成したシステムプロンプトとツールスキーマ（LLMが呼び出せるツールの定義）。
- **ダッシュボードユーザーメッセージ:** ダッシュボードユーザーが入力したテキスト。
- **ツール出力:** 名前、ID、関連データを含む検索結果。
- **スクレイピングされたページコンテンツ:** アクティブなダッシュボードページのコンテンツ（約4,000文字に切り詰められます）。
- **ページコンテキスト文字列:** アクティブなダッシュボードページからのコンテキスト文字列。

## データサブプロセッサー {#data-sub-processors}

### サブプロセッサーまたはサードパーティプロバイダーとしてのモデルプロバイダー {#model-providers-as-sub-processors-or-third-party-providers}

Brazeサービスを通じてBrazeが提供するLLMプロバイダーとの統合（「Braze提供LLM」）を使用する場合、当該Braze提供LLMのプロバイダーはBrazeのサブプロセッサーとして機能し、お客様とBraze間のデータ処理補遺（DPA）の条件に従います。BrazeAI Operator<sup>TM</sup>はOpenAIと統合しています。

### OpenAIでのデータの使用方法 {#how-data-is-used-with-openai}

OpenAIを活用するBrazeAI機能を通じてAI出力（「出力」）を生成するために、Brazeは特定の情報（「入力」）をOpenAIに送信します。入力は、お客様のプロンプト、ダッシュボードに表示されるコンテンツ、およびお客様のクエリに関連するワークスペースデータで構成されます。[OpenAIのAPIプラットフォームコミットメント](https://openai.com/enterprise-privacy/)に基づき、Brazeを通じてOpenAIのAPIに送信されたデータは、OpenAIモデルのトレーニングや改善には使用されません。お客様とBraze間において、出力はお客様の知的財産です。Brazeは当該出力に対する著作権の所有権を主張しません。Brazeは、出力を含むAI生成コンテンツに関して、いかなる種類の保証も行いません。

## HIPAAコンプライアンスとデータ保持 {#hipaa-compliance-and-data-retention}

### HIPAAコンプライアンス {#hipaa-compliance}

BrazeのUS-02クラスターを使用している場合、OperatorはBrazeのビジネスアソシエイト契約（BAA）の対象となり、HIPAA要件に従って個人健康情報（PHI）を機能に送信できます。他のBrazeクラスターでOperatorを使用する場合は、HIPAAの対象となるPHIを送信しないでください。

### PIIリダクション {#pii-redaction}

Operatorのリクエストパイプラインには、自動PIIリダクションレイヤーはありません。データは完全に生の状態で送信され、OpenAIへの送信前に匿名化されません。アクセスはアクティブなダッシュボードページまたはダッシュボードユーザーの入力にスコープされますが、送信前にコンテンツフィルタリングは適用されません。

### OpenAIのデータ保持 {#openai-data-retention}

Operatorを通じて送信されたデータをOpenAIが保持する期間は、クラスターによって異なります。

| クラスター | 保持期間 |
| --- | --- |
| US-02（HIPAA顧客） | ゼロデータリテンション（ZDR）。処理後、OpenAIによるデータの保存はありません。 |
| その他すべてのクラスター | 不正利用監視のため30日間。これはOpenAIが課す業界標準の保持期間です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="クラスター別のOpenAIデータ保持" }

### モデルトレーニング {#model-training}

Brazeを通じてOpenAIのAPIに送信されたデータは、OpenAIモデルのトレーニングや改善には使用されません。これはBrazeとOpenAI間の契約およびOpenAIのAPIプラットフォームコミットメントによって規定されています。OpenAIはBrazeのサブプロセッサーとして機能し、すべての個人データはBrazeとそのクライアント間のDPAに従います。

### EUデータルーティング {#eu-data-routing}

EUデータルーティングは現在Operatorには実装されておらず、実装の予定もありません。

## PII露出を最小限に抑える {#minimize-pii-exposure}

Operatorを使用する際にPII露出を制限するために、いくつかの対策を講じることができます。

- Operatorを使用するすべてのユーザーに対して、**PII表示設定を無効にします**。ユーザーがPIIを表示できない場合、OperatorもPIIにアクセスできません。
- **ユーザープロファイルページでOperatorを開かないでください。**ページコンテンツはスクレイピングされ、OpenAIに送信される各リクエストに含まれます。
- **テスト時は、既存のユーザーを選択するのではなく、カスタムユーザープロファイルを使用してください。**これはOperatorのデフォルトの動作です。
- Operatorのプロンプトに**PIIを直接入力または貼り付けないでください**。
- Operatorがアクセスおよび実行できる内容を制御するために、**アクションの自動承認を無効にしてください**。
- Segmentの構築やLiquidの記述時に、**Operatorに属性のプレビュー値を表示するよう依頼しないでください**。

## ガバナンスとアクセス制御 {#governance-and-access-control}

### Operatorへのアクセスを制限する {#restrict-access-to-operator}

Operatorへのアクセスは、[きめ細かなユーザー権限]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/)を通じてワークスペースレベルで管理されます。管理者は個々のユーザーに対して**Use BrazeAI Operator**権限を付与または取り消すことができ、承認された担当者のみがツールを操作できるようにします。これらの特定の権限がない場合、Operatorインターフェイスは完全に非表示となり、バックエンドのエンドポイントもセキュリティで保護されたままになります。

### ヒューマンインザループモデル {#human-in-the-loop-model}

デフォルトでは、Operatorは変更をコミットする前に明示的な承認を必要とします。提案された変更は、確認のために[アクションカード]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions/)として表示されます。ユーザーが提案を拒否した場合、変更は行われません。ユーザーが提案を承認した場合、ダッシュボードは更新されますが、変更は保留状態のままであり、永続化するには手動で保存または起動する必要があります。

ユーザーはOperatorチャットパネルで**アクションの自動承認**を有効にできます。これにより、提案されたアクションは手動レビューなしで即座に実行されます。自動承認が有効な場合でも、画像の生成やワークスペースレベルの設定の変更など、安全性のために常に明示的な承認が必要なアクションがあります。

### ユーザー権限の継承 {#user-permission-inheritance}

Operatorは、ログインしているユーザーの権限プロファイルを完全に継承します。ユーザーが独立して実行する権限を持っていないデータの表示やアクション（Campaignの変更など）の実行は制限されます。

### チーム利用の監査 {#audit-team-usage}

Brazeの[セキュリティイベントレポート]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings/#security-event-report)をダウンロードして、チームの利用状況を監視します。「Requested BrazeAI Operator Response」イベントは包括的な監査証跡を提供し、Operatorに提供された正確な入力を確認できます。