---
nav_title: Canvasの複製
article_title: Canvasの複製
page_order: 3
alias: "/cloning_canvases/"
description: "このリファレンス記事では、オリジナルのCanvasエディターからキャンバスフローワークフローにCanvasを複製する方法について説明します。"
tool: Canvas
---

# Canvasをキャンバスフローに複製する {#clone-canvases-to-canvas-flow}

> オリジナルのエディターで作成した既存のCanvasがある場合、そのCanvasを複製してキャンバスフローにコピーを作成できます。現在のCanvasワークフローに切り替えることで、軽量な[Canvasコンポーネント]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components)、[永続的なエントリプロパティ]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#canvas-entry-properties)、および[起動後の編集]({{site.baseurl}}/post-launch_edits)にアクセスできるようになります。オリジナルのCanvasは変更も削除もされません。

{% alert important %}
オリジナルのCanvasエクスペリエンスを使用してCanvasを作成または複製することはできなくなりました。Brazeでは、オリジナルのCanvasエクスペリエンスを使用している顧客に、現在のCanvasエクスペリエンスであるキャンバスフローへの移行を推奨しています。
{% endalert %}

Canvasを複製するには、以下の手順に従ってください。

1. Canvasダッシュボードに移動します。
2. キャンバスフローワークフローでコピーを作成したいCanvasを特定します。**下書き**、**アクティブ**、または**停止済み**のステータスのCanvasを複製できます。
3. <i class="fas fa-ellipsis-vertical"></i> **More actions** をクリックし、**Clone to Canvas Flow** を選択します。

![説明されたプロセスのフロー図。]({% image_buster /assets/img_archive/clone_to_v2_workflow.png %}){: style="max-width:25%;"}

{: start="4"}
4. 新しいCanvasの名前を入力し、**Clone to Canvas Flow** をクリックします。

![コンテンツカードのモーダル配置の例。]({% image_buster /assets/img_archive/clone_to_v2_modal.png %}){: style="max-width:70%;"}

これで、Canvasの2つのバージョンが作成されました。オリジナルのCanvasとキャンバスフローバージョンです。オリジナルのCanvasは元のステータスのままで、複製されたCanvasは**下書き**ステータスになります。引き続きオリジナルのCanvasにアクセスできますが、Brazeではキャンバスフローワークフローを使用してCanvasの構築を続けることを推奨しています。

以前は、分岐を含む一部のCanvasは複製できませんでした。現在は、分岐を含むCanvasも複製できます。ただし、分岐を含むCanvasを複製すると、切断されたステップが発生する場合があります。これらの切断されたステップ（前のステップが接続されていないステップ）を解決して、Canvasジャーニーが正しくマッピングされていることを確認してください。

{% alert note %}
アクティブなCanvasを複製した場合、Brazeは引き続きオリジナルのCanvasを通じてユーザーにメッセージを送信します。両方のCanvasからユーザーに重複したメッセージが送信されるのを避けるため、複製する前にCanvasを停止することを推奨します。
{% endalert %}

![2つのCanvasが表示されたCanvasダッシュボード: V2 Copy of Canvas V1とCanvas V1。V2 Copy of Canvas V1には、キャンバスフローワークフローを使用していることを示すアイコンが表示されています。]({% image_buster /assets/img_archive/clone_to_v2_dashboard.png %})

キャンバスフローワークフローへのCanvasの複製が完了しました。この更新されたエクスペリエンスでCanvasの構築を続けましょう！

## おすすめ {#recommendations}

オリジナルのCanvasをキャンバスフローに複製した後、既存のユーザーがユーザージャーニーを継続できるようにするには、既存のCanvasにフィルターを追加して、新しいユーザーが新しいCanvasに入らないようにすることができます。

再エントリが無効の場合は、「Entered Canvas Variation」フィルターを追加します。再エントリが有効の場合は、ユーザーが同じCanvasに2回入らないようにするために、以下の方法を検討してください。
- 既存のCanvasにユニークなタグを追加するよう更新します。新しいCanvasには、「Last Received Message from Campaign or Canvas with Tag」フィルターを追加します。これにより、特定のエントリ日以降にユーザーがCanvasに2回入ることを防ぎます（オリジナルのCanvasから最後のメッセージが送信されてからの合計日数にコンバージョン時間枠を加えた期間）。
- **以下の方法ではデータポイントが記録されます。** オリジナルのCanvasを更新して、エントリ時にカスタム属性の日付タイムスタンプをトリガーするBraze間Webhookを含めます。この属性を使用して、指定された日付以降にユーザーが新しいCanvasに入ることを防ぐことができます（オリジナルのCanvasから最後のメッセージが送信されてからの合計日数にコンバージョン時間枠を加えた期間）。

APIトリガーのCanvasについては、新しいCanvasの起動準備が整った際に、これらのCanvasが新しいCanvas IDを使用するようエンジニアリングチームと調整してください。

オリジナルのCanvasエディターとキャンバスフローエクスペリエンスの違いについて詳しくは、[Canvas FAQ]({{site.baseurl}}/user_guide/messaging/canvas/faqs#what-are-the-main-differences-between-canvas-flow-and-the-original-canvas-editor)をご確認ください。