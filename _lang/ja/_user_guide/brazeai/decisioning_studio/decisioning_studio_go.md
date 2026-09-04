---
nav_title: Decisioning Studio Go
article_title: BrazeAI Decisioning Studio Go
page_order: 5.5
description: "BrazeAI Decisioning Studio<sup>TM</sup> GoをBrazeに設定・統合する方法について説明します。"
---

# BrazeAI Decisioning Studio™ Go

> BrazeAI Decisioning Studio™ GoをBrazeに設定・統合する方法について説明します。

## Decisioning Studio Goについて {#about-decisioning-studio-go}

Decisioning Studio Goは、定期的なメールプログラム向けのAI意思決定エージェントです。オーディエンス全体に対して1つの勝者となる件名、送信タイミング、または画像を選ぶ代わりに、エージェントが各受信者の過去のエンゲージメントに基づいて最適な組み合わせを選択します。

エージェントが選択できるバリアントを定義します。件名、CTA、画像、送信曜日、送信時間などです。セグメント内の各ユーザーに対して、設定した制約とスケジュールの範囲内で、エンゲージメントを促進する可能性が最も高いオプションをエージェントが選択します。

これは、オーディエンス向けにバリアントを最適化する[BrazeAI<sup>TM</sup>で最適化]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection)を使用したキャンペーンレベルのABテストとは異なります。Decisioning Studio Goは、プログラム内のすべての送信において個人レベルでパーソナライズを行います。

### 仕組み {#how-it-works}

エージェントはBrazeセグメントを2つのグループに分割します。AI最適化されたメールコンテンツを受信するDecisioning Studioグループと、同じオプションのランダムな組み合わせを受信するランダムコントロールグループ（最低5%）です。ランダムコントロールにより、エージェントのリフトを継続的かつ同条件で測定できます。パーソナライズされた体験が、パーソナライゼーションなしで送信された同じコンテンツと比較してどのようにパフォーマンスを発揮するかを常に確認できます。

Decisioning Studioグループの各ユーザーに対して、エージェントは提供されたオプションの中から選択します。どのクリエイティブを送信するか（その中の特定の件名、CTA、画像を含む）、いつ送信するか（曜日と時間帯、クワイエットアワーとユーザーのローカルタイムゾーンを考慮）です。[Decisioning Studio Goエージェントを設定する]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/setup)で、それぞれの詳細を説明しています。

ユーザーがエンゲージする（またはしない）につれて、エージェントは学習します。レポートでは、エージェントがまだトレーニング期間中なのか、積極的にパーソナライズしているのかが表示されるため、エージェントがどの段階にあるかを常に把握できます。

### 設定項目 {#what-you-configure}

| 設定 | 説明 |
|---|---|
| **オーディエンス** | エントリオーディエンスとなる単一のBrazeセグメントです。エージェントがセグメントをDecisioning Studioグループとランダムコントロールグループに自動的に分割します。 |
| **スケジュール** | 送信頻度（例：週3回の単一選択）、許可する曜日、ユーザーのローカルタイムゾーンにおけるクワイエットアワー、エージェントレベルのフリークエンシーキャップルールの遵守です。 |
| **クリエイティブ** | Brazeコンポーザーで作成した1つ以上のベースクリエイティブです。各ベースクリエイティブ内で、Liquidタグを使用して件名、CTA、画像をパーソナライゼーションポイントとしてマークし、それぞれのバリアントリストを提供できます。エージェントが各受信者に使用するベースクリエイティブとバリアントを決定します。 |
| **制約** | 定義したウィンドウ内で、同じベースクリエイティブまたは同じ件名をユーザーに2回以上送信することを防ぐ制限です。 |
| **確認と起動** | 起動前に対応すべき警告を表示する最終検証画面です。エージェントは**下書き**から**アクティブ**に移行し、送信を開始します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Decisioning Studio Goの設定" }

### Decisioning Studio Goを使用するタイミング {#when-to-use-decisioning-studio-go}

最も適しているのは、安定したオーディエンスとクリック可能なコンテンツを持つ定期的なメールプログラムです。例えば、常時配信カレンダー（報酬、コンテンツドロップ、ライフサイクルナッジ）、エバーグリーンプログラム（ウィンバック、再エンゲージメント）、複数メールのプロモーションなどです。これらにより、エージェントは意味のある学習に十分なボリュームと多様性を得られます。

プログラムタイプ別の詳細な適合ガイダンスについては、[Decisioning Studio Goの例]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/examples)を参照してください。

### Decisioning Studio suiteにおけるDecisioning Studio Goの位置づけ {#where-decisioning-studio-go-sits-in-the-decisioning-studio-suite}

Decisioning Studio Goは、BrazeAI Decisioning Studioのエントリティアです。Decisioning Studio Proの本格的な実装のセットアップ負荷なしに、1対1のメールパーソナライゼーションを実現したいマーケター向けに設計されています。

Decisioning Studio Proでは以下が追加されます：
- あらゆるビジネス指標に対する最適化（クリックだけではありません）
- あらゆるファーストパーティデータソースへの接続
- マルチチャネルの意思決定
- 拡張されたオーケストレーションパターン
- Braze AI Decisioning Servicesチームによる専任サポート

## 次のステップ {#next-steps}

{% article_tiles %}
- name: Decisioning Studio Goエージェントを設定する
  link: /docs/user_guide/brazeai/decisioning_studio/decisioning_studio_go/setup/
- name: Decisioning Studio Goの例を確認する
  link: /docs/user_guide/brazeai/decisioning_studio/decisioning_studio_go/examples/
- name: FAQ
  link: /docs/user_guide/brazeai/decisioning_studio/decisioning_studio_go/faq/
{% endarticle_tiles %}