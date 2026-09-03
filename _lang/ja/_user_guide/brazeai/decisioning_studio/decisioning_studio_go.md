---
nav_title: Decisioning Studio Go
article_title: BrazeAI Decisioning Studio Go
page_order: 5.5
description: "BrazeAI Decisioning Studio<sup>TM</sup> GoをBrazeに設定・統合する方法について説明します。"
---

# BrazeAI Decisioning Studio™ Go

> BrazeAI Decisioning Studio™ GoをBrazeに設定・統合する方法について説明します。

## Decisioning Studio Goについて {#about-decisioning-studio-go}

Decisioning Studio Goは、定期的なメールプログラム向けのAI意思決定エージェントです。オーディエンス全体に対して1つの勝者の件名、送信時間、または画像を選ぶ代わりに、エージェントが各受信者の過去のエンゲージメントに基づいて最適な組み合わせを選択します。

エージェントが選択できるバリアントを定義します。件名、CTA、画像、送信曜日、送信時間などです。セグメント内の各ユーザーに対して、設定した制約とスケジュールの範囲内で、エンゲージメントを促進する可能性が最も高いオプションをエージェントが選択します。

これは、[BrazeAI<sup>TM</sup>で最適化]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection)によるキャンペーンレベルのABテストとは異なります。ABテストはオーディエンス全体に対してバリアントを最適化しますが、Decisioning Studio Goはプログラム内のすべての送信で個人レベルのパーソナライゼーションを行います。

### 仕組み {#how-it-works}

エージェントはBrazeセグメントを2つのグループに分割します。AI最適化されたメールコンテンツを受信するDecisioning Studioグループと、同じオプションのランダムな組み合わせを受信するランダムコントロールグループ（最低5%）です。ランダムコントロールにより、エージェントのリフトを継続的に同等条件で測定できます。パーソナライズされた体験が、パーソナライゼーションなしで送信された同じコンテンツと比較してどのようなパフォーマンスを示しているか、常に確認できます。

Decisioning Studioグループの各ユーザーに対して、エージェントは提供されたオプションから選択します。どのクリエイティブを送信するか（特定の件名、CTA、画像を含む）、いつ送信するか（曜日と時間帯、クワイエットアワーとユーザーのローカルタイムゾーンを考慮）です。[Decisioning Studio Goエージェントを設定する]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/setup)で、それぞれの詳細について説明しています。

ユーザーがエンゲージする、またはしないことで、エージェントは学習します。レポートでは、エージェントがまだトレーニング期間中なのか、積極的にパーソナライズしているのかが示されるため、エージェントがどの段階にあるかを常に把握できます。

### 設定項目 {#what-you-configure}

| 設定項目 | 説明 |
|---|---|
| **オーディエンス** | エントリオーディエンスとして単一のBrazeセグメントを使用します。エージェントがセグメントを意思決定グループとランダムコントロールグループに自動的に分割します。 |
| **スケジュール** | 送信頻度（例：週3回の単一選択）、許可する曜日、ユーザーのローカルタイムゾーンでのクワイエットアワー、エージェントレベルのフリークエンシーキャップルールの遵守。 |
| **クリエイティブ** | Brazeコンポーザーで作成した1つ以上のベースクリエイティブ。各ベースクリエイティブ内で、件名、CTA、画像をLiquidタグを使用してパーソナライゼーションポイントとして指定し、それぞれのバリアントリストを提供できます。エージェントが各受信者に使用するベースクリエイティブとバリアントを決定します。 |
| **制約** | 定義したウィンドウ内で、同じベースクリエイティブまたは同じ件名をユーザーに複数回送信することを防ぐ制限です。 |
| **確認と起動** | 起動前に注意すべき警告を表示する最終確認画面です。エージェントは**下書き**から**アクティブ**に移行し、送信を開始します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Decisioning Studio Goの設定" }

### Decisioning Studio Goを使用するタイミング {#when-to-use-decisioning-studio-go}

最も適しているのは、安定したオーディエンスとクリック可能なコンテンツを持つ定期的なメールプログラムです。例えば、常時稼働のカレンダー（報酬、コンテンツドロップ、ライフサイクルナッジ）、エバーグリーンプログラム（ウィンバック、再エンゲージメント）、複数メールのプロモーションなどが該当します。これらはエージェントが有意義に学習するのに十分なボリュームとバリエーションを提供します。

プログラムタイプ別の詳細な適合度ガイダンスについては、[Decisioning Studio Goの例]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/examples)を参照してください。

### Decisioning Studioスイートにおける位置づけ {#where-decisioning-studio-go-sits-in-the-decisioning-studio-suite}

Decisioning Studio Goは、BrazeAI Decisioning Studioのエントリティアです。Decisioning Studio Proの本格的な実装のセットアップ負荷なしに、1対1のメールパーソナライゼーションを実現したいマーケター向けに設計されています。

Decisioning Studio Proでは以下が追加されます：
- あらゆるビジネス指標に対する最適化（クリックだけでなく）
- あらゆるファーストパーティデータソースへの接続
- マルチチャネルの意思決定
- 拡張されたオーケストレーションパターン
- Braze AI Decisioning Servicesチームによる専任サポート

## 次のステップ {#next-steps}

- [Decisioning Studio Goエージェントを設定する]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/setup)：オーディエンス、スケジュール、クリエイティブ、制約を設定します
- [Decisioning Studio Goの例を確認する]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/examples)：お客様のプログラムが適しているかどうかを確認できます
- よくある質問については[FAQ]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/faq)を参照してください