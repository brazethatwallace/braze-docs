{% tab swift %}
各アプリ内メッセージタイプは、コンテンツ、画像、アイコン、クリックアクション、分析、表示、配信にわたって高度にカスタマイズできます。これらは`Braze.InAppMessage`の列挙型であり、すべてのアプリ内メッセージの基本的な振る舞いと特性を定義します。アプリ内メッセージのプロパティと使用法の完全な一覧については、[`InAppMessage`クラス](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage)を参照してください。

以下は、Brazeで使用可能なアプリ内メッセージタイプと、エンドユーザーにどのように表示されるかを示しています。

{% subtabs %}
{% subtab Slideup %}

[`Slideup`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/slideup-swift.struct)アプリ内メッセージは、画面の上部または下部から「スライドアップ」または「スライドダウン」することからこの名前が付けられています。画面の一部分だけを覆い、効果的で邪魔にならないメッセージング機能を提供します。

![スマートフォン画面の下部と上部に表示されるスライドアップアプリ内メッセージ。]({% image_buster /assets/img/slideup-spec.png %}){: style="max-width:35%;border:none;"}


{% endsubtab %}
{% subtab Modal %}

[`Modal`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/modal-swift.struct)アプリ内メッセージは画面中央に表示され、半透明のパネルに囲まれます。より重要なメッセージングに有用で、最大2つの分析対応ボタンを装備できます。

![スマートフォン画面の中央に表示されるモーダルアプリ内メッセージ。]({% image_buster /assets/img/modal-header-text.png %}){: style="max-width:35%;border:none;"}

{% endsubtab %}
{% subtab Modal Image %}

[`Modal Image`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/modalimage-swift.struct)アプリ内メッセージは画面中央に表示され、半透明のパネルに囲まれます。これらのメッセージは、ヘッダーやメッセージテキストがないことを除けば、`Modal`タイプに似ています。より重要なメッセージングに有用で、最大2つの分析対応ボタンを装備できます。

![スマートフォン画面の中央に表示されるモーダル画像アプリ内メッセージ。]({% image_buster /assets/img/modal-full-image.png %}){: style="max-width:35%;border:none;"}

{% endsubtab %}
{% subtab Fullscreen %}

[`Full`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/full-swift.struct)アプリ内メッセージは、ユーザーコミュニケーションの内容とインパクトを最大化するのに有効です。`Full`アプリ内メッセージの上半分には画像が含まれ、下半分にはテキストと最大2つの分析対応ボタンが表示されます。

![スマートフォン画面全体に表示されるフルスクリーンアプリ内メッセージ。]({% image_buster /assets/img/full-screen-header-text.png %}){: style="max-width:35%;border:none;"}

{% endsubtab %}
{% subtab Full Screen Image %}

[`Full Image`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/fullimage-swift.struct)アプリ内メッセージは、ヘッダーやメッセージテキストがないことを除けば、`Full`アプリ内メッセージと似ています。このメッセージタイプは、ユーザーコミュニケーションの内容とインパクトを最大化するのに有効です。`Full Image`アプリ内メッセージには画面全体に広がる画像が含まれ、オプションで最大2つの分析対応ボタンを表示できます。

![スマートフォン画面全体に表示されるフルスクリーン画像アプリ内メッセージ。]({% image_buster /assets/img/full-screen-image.png %}){: style="max-width:35%;border:none;"}

{% endsubtab %}
{% subtab Custom HTML %}

[`HTML`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/html-swift.struct)アプリ内メッセージは、完全にカスタマイズされたユーザーコンテンツを作成するのに便利です。ユーザー定義のHTMLフルアプリ内メッセージコンテンツは`WKWebView`に表示され、必要に応じて画像やフォントなどの他のリッチコンテンツを含めることができます。これにより、メッセージの外観と機能を完全にコントロールできます。<br><br>iOSアプリ内メッセージは、HTML内からBraze Web SDKのメソッドを呼び出すためのJavaScript `brazeBridge`インターフェイスをサポートしています。詳細については、[ベストプラクティス]({{site.baseurl}}/user_guide/channels/in_app_messages/best_practices)を参照してください。

次の例は、ページ分割されたHTMLフルアプリ内メッセージを示しています。

![コンテンツのカルーセルとインタラクティブボタンを備えたHTMLアプリ内メッセージ。]({% image_buster /assets/img_archive/ios-html-full-iam.gif %})

現在、iOSとAndroidプラットフォームでは、iFrame内でのカスタムHTMLアプリ内メッセージの表示はサポートしていません。

{% endsubtab %}
{% subtab Control %}

[`Control`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/control-swift.struct)アプリ内メッセージにはUIコンポーネントは含まれず、主に分析目的で使用されます。このタイプは、コントロールグループに送信されたアプリ内メッセージの受信を確認するために使用されます。

バリアントの自動最適化とコントロールグループについては、[BrazeAI<sup>TM</sup>で最適化する]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection)を参照してください。

{% endsubtab %}
{% endsubtabs %}
{% endtab %}