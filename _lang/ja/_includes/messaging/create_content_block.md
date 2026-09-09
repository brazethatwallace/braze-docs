{% if include.location == "dnd" %}

1. **コンテンツ** > **Content Block** に移動します。<i class="fas fa-plus"></i> **Content Blockを作成** を選択し、**ドラッグ＆ドロップContent Block** を選択します。
2. [エディターブロック]({{site.baseurl}}/user_guide/channels/email/drag_and_drop/dnd_editor_blocks)をドラッグ＆ドロップして、ドラッグ＆ドロップコンテンツブロックを構築します。
3. **Rows** タブからフォーマットブロックをエディターにドラッグ＆ドロップして、コンテンツブロックのレイアウトを作成します。<br><br> ![ドラッグ＆ドロップコンテンツブロックコンポーザー。]({% image_buster /assets/img_archive/dnd_content_block_composer.png %})<br><br>
4. 必要に応じてドラッグ＆ドロップContent Blocksを追加し、メールキャンペーンを構築します。
5. コンテンツブロックの作成が完了したら、**完了** を選択します。
6. コンテンツブロックに名前を付けます。この名前は、**Content BlockのLiquidタグ**の一部として自動入力されます。
7. (オプション) 説明を追加します。
8. **プレビュー**タブを選択して、コンテンツブロックの表示を確認します。必要に応じて**プレビューリンクをコピー**を選択すると、ランダムなユーザーに対してメールがどのように表示されるかを示す共有可能なプレビューリンクを生成してコピーできます。リンクは7日間有効で、それ以降は再生成が必要です。<br><br> ![ドラッグ＆ドロップコンテンツブロックコンポーザーのプレビュータブ。]({% image_buster /assets/img_archive/dnd_content_block_preview_link.png %})<br><br>
9. **Content Blockを起動** を選択します。

{% elsif include.location == "html" %}

1. **コンテンツ** > **Content Block** に移動します。<i class="fas fa-plus"></i> **Content Blockを作成** を選択し、**HTMLコードエディター** を選択します。
2. **HTML** タブでHTMLを入力するか、**Classic** タブでコンテンツブロックを構築します。<br><br> ![HTMLコードエディターコンポーザー。]({% image_buster /assets/img_archive/html_content_block_composer.png %})<br><br>
3. コンテンツブロックの作成が完了したら、**完了** を選択します。
4. コンテンツブロックの名前を入力します。この名前は、**Content BlockのLiquidタグ**の一部として自動入力されます。
5. (オプション) 説明を追加します。
6. **プレビュー**タブを選択して、コンテンツブロックの表示を確認します。必要に応じて**プレビューリンクをコピー**を選択すると、ランダムなユーザーに対してメールがどのように表示されるかを示す共有可能なプレビューリンクを生成してコピーできます。リンクは7日間有効で、それ以降は再生成が必要です。<br><br> ![HTMLコードエディターコンポーザーのプレビュータブ。]({% image_buster /assets/img_archive/content_block_html_preview_link.png %})<br><br>
7. **Content Blockを起動** を選択します。

{% endif %}