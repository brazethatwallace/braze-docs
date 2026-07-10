---
nav_title: "ラストタッチアトリビューション"
permalink: /last-touch_attribution_metrics/
hidden: true
---

# ラストタッチアトリビューション指標 {#last-touch-attribution-metrics}

> レポートビルダーのレポートにラストタッチアトリビューション指標を追加します。

{% alert note %}
ラストタッチアトリビューション指標は早期アクセス段階です。早期アクセスへの参加にご興味がある場合は、カスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

ラストタッチアトリビューション（LTA）は、コンバージョン前にユーザーが最後にインタラクションしたメッセージにコンバージョンの全クレジットを付与するコンバージョンアトリビューションモデルです。キャンペーンレベルのコンバージョンウィンドウとは異なり、LTAは各チャネルに対して業界標準のアトリビューションウィンドウを使用します。

| チャネル | アトリビューションウィンドウ |
| --- | --- |
| メール | 30日間 |
| SMS | 7日間 |
| WhatsApp | 7日間 |
| プッシュ | 7日間 |
| アプリ内メッセージ | 3日間 |
| Content Cards | 3日間 |
| Webhook | このモデルから除外 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
チャネルのアトリビューションウィンドウ外でコンバージョンが発生した場合、このモデルではカウントされません。
{% endalert %}

## メリット {#benefits}

ラストタッチアトリビューションは、標準的なコンバージョントラッキングに比べて主要な利点を提供します。

* コンバージョンを特定のタッチポイントに帰属させることができ、どのチャネル（キャンペーンやキャンバスだけでなく）が成果を生み出しているかを理解できるようになります。
* クレジットは最後にタッチされたメッセージにのみ付与されるため、各コンバージョンは1回だけカウントされ、共通のコンバージョンイベントやオーディエンスを持つキャンペーンやキャンバス間でのコンバージョンの重複が排除されます。

## レポートにラストタッチアトリビューション指標を追加する {#add-last-touch-attribution-metrics-to-your-report}

1. **Analytics**の**レポートビルダー**に移動します。
2. **レポートを作成** > **カスタムレポートを作成**を選択します。
3. **行**ドロップダウンで、レポートを作成する対象を選択します。
4. （オプション）**ドリルダウンを追加**を選択し、レポートをさらに詳しく掘り下げる領域を選択します。
5. **列**で**指標をカスタマイズ**を選択します。
6. **コンバージョン**で**Last Touch Attribution**を選択し、次に**すべて選択**を選択します。

{% alert note %}
収益および購入指標は利用できません。
{% endalert %}

![ラストタッチアトリビューション指標が表示された指標カスタマイズパネル。]({% image_buster /assets/unlisted_docs/img/report_builder_2/lta_report_builder.png %})

{: start="7" }
7. [レポートビルダー]({{site.baseurl}}/user_guide/analytics/reporting/report_builder)ページのステップ7〜9に従ってください。

{% alert note %}
{% multi_lang_include product_feedback_cta.md context="pain_point" channel="feature" feature="last-touch attribution metrics in Report Builder" %}
{% endalert %}