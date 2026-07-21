---
nav_title: Decisioning Studio Go
article_title: BrazeAI Decisioning Studio Go
page_order: 5.5
description: "BrazeAI Decisioning Studio<sup>TM</sup> GoをBrazeに設定・統合する方法を学びます。"
---

# BrazeAI Decisioning Studio™ Go

> BrazeAI Decisioning Studio™ GoをBrazeに設定・統合する方法について説明します。

## Decisioning Studio Goについて {#about-decisioning-studio-go}

Decisioning Studio Goは、定期的なメールプログラム向けのAI意思決定エージェントです。オーディエンス全体に対して1つの最適な件名、送信時間、または画像を選ぶのではなく、エージェントが各受信者の過去のエンゲージメントに基づいて最適な組み合わせを選択します。

エージェントが選択できるバリアントを定義します。件名、CTA、画像、送信曜日、送信時間などです。セグメント内の各ユーザーに対して、設定した制約とスケジュールの範囲内で、エンゲージメントを促進する可能性が最も高いオプションをエージェントが選択します。

これは、キャンペーンレベルのABテストや[インテリジェントセレクション]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection)とは異なります。これらはオーディエンス全体に対して単一のバリアントを最適化するものです。Decisioning Studio Goは、プログラム内のすべての送信において、個人レベルでパーソナライズを行います。

### 仕組み {#how-it-works}

エージェントはBrazeセグメントを2つのグループに分割します。AI最適化されたメールコンテンツを受け取るDecisioning Studioグループと、同じオプションのランダムな組み合わせを受け取るランダムコントロールグループ（最低5%）です。ランダムコントロールにより、エージェントのリフトを継続的に同条件で測定できます。パーソナライズされた体験が、パーソナライゼーションなしで送信された同じコンテンツと比較してどのようなパフォーマンスを示すかを常に確認できます。

Decisioning Studioグループの各ユーザーに対して、エージェントは提供されたオプションの中から選択します。どのクリエイティブを送信するか（その中の特定の件名、CTA、画像を含む）、いつ送信するか（曜日と時間帯、クワイエットアワーとユーザーのローカルタイムゾーンを考慮）です。[Decisioning Studio Goエージェントを設定する]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/setup)で、これらの各項目について詳しく説明しています。

ユーザーがエンゲージする（またはしない）につれて、エージェントは学習します。レポートでは、エージェントがまだトレーニング期間中なのか、積極的にパーソナライズを行っているのかが示されるため、エージェントがどの段階にあるかを常に把握できます。

### 設定する内容 {#what-you-configure}

| 設定 | 説明 |
|---|---|
| **オーディエンス** | エントリオーディエンスとして単一のBrazeセグメントを指定します。エージェントがセグメントを意思決定グループとランダムコントロールグループに自動的に分割します。 |
| **スケジュール** | 送信頻度（例：週3回の単一選択）、許可する曜日、ユーザーのローカルタイムゾーンでのクワイエットアワー、エージェントレベルのフリークエンシーキャップルールの遵守。 |
| **クリエイティブ** | Brazeコンポーザーで作成した1つ以上のベースクリエイティブ。各ベースクリエイティブ内で、件名、CTA、画像をLiquidタグを使用してパーソナライゼーションポイントとしてマークし、それぞれのバリアントリストを提供できます。エージェントが各受信者に使用するベースクリエイティブとバリアントを決定します。 |
| **制約** | 定義したウィンドウ内で、同じベースクリエイティブまたは同じ件名をユーザーに複数回送信することを防ぐ制限。 |
| **確認と起動** | 起動前に対処すべき警告を表示する最終検証画面。エージェントは**下書き**から**ライブ**に移行し、送信を開始します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Decisioning Studio Goの設定" }

### Decisioning Studio Goを使用するタイミング {#when-to-use-decisioning-studio-go}

最も適しているのは、安定したオーディエンスとクリック可能なコンテンツを持つ定期的なメールプログラムです。例えば、常時稼働のカレンダー（報酬、コンテンツドロップ、ライフサイクルナッジ）、エバーグリーンプログラム（ウィンバック、リエンゲージメント）、複数メールのプロモーションなどです。これらは、エージェントが有意義に学習するのに十分なボリュームとバリエーションを提供します。

プログラムタイプ別の詳細な適合ガイダンスについては、[Decisioning Studio Goの例]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/examples)を参照してください。

### Decisioning StudioスイートにおけるDecisioning Studio Goの位置づけ {#where-decisioning-studio-go-sits-in-the-decisioning-studio-suite}

Decisioning Studio Goは、BrazeAI Decisioning Studioのエントリティアです。完全なDecisioning Studio Proの実装にかかるセットアップの負担なしに、1対1のメールパーソナライゼーションを実現したいマーケター向けに設計されています。

Decisioning Studio Proでは以下が追加されます：
- あらゆるビジネス指標（クリックだけでなく）に対する最適化
- あらゆるファーストパーティデータソースへの接続
- マルチチャネルの意思決定
- 拡張されたオーケストレーションパターン
- Braze AI意思決定サービスチームによる専任サポート

## 次のステップ {#next-steps}

- [Decisioning Studio Goエージェントを設定する]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/setup)—オーディエンス、スケジュール、クリエイティブ、制約を設定します
- [Decisioning Studio Goの例を確認する]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/examples)—プログラムが適しているか確認します
- よくある質問については[FAQ]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/faq)を参照してください