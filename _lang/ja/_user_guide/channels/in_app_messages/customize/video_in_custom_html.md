---
nav_title: "カスタムHTMLでの動画"
article_title: "カスタムHTMLでの動画"
page_order: 4
page_type: reference
description: "この記事では、HTMLアプリ内メッセージに動画を埋め込む方法について説明します。"
channel:
  - in-app messages
---

# カスタムHTMLアプリ内メッセージでの動画 {#video}

> この記事は、[従来のエディター]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/)の[カスタムHTMLメッセージ]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html/)に適用されます。

## 動画の埋め込み {#embed-videos}

HTMLアプリ内メッセージで動画を再生するには、以下の `<video>` 要素をHTMLに含め、動画名をファイル名（またはリモートアセットのURL）に置き換えてください。その他の `<video>` オプションについては、[MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video)を参照してください。

```html
<video class="video" autoplay muted playsinline controls>
  <source src="https://video-provider.com/YOUR_VIDEO_FILE.mp4" type="video/mp4">
  <source src="https://video-provider.com/YOUR_VIDEO_FILE.ogg" type="video/ogg">
  Your device does not support playing this video.
</video>
```

ローカルの動画アセットを使用する場合は、キャンペーンにアセットをアップロードする際にこのファイルを含めてください。

{% alert note %}
動画コンテンツは、デバイスのネットワーク速度が十分な場合にのみ利用可能です。ただし、動画がデバイスのローカルから提供される場合は除きます。
{% endalert %}

## Androidに関する考慮事項 {#android-considerations}

Androidでは、HTMLアプリ内メッセージに動画やその他のHTML5コンテンツを埋め込むために、アプリ内メッセージが表示されるActivityでハードウェアアクセラレーションを有効にする必要があります。詳細については、[Android開発者ガイド]({{site.baseurl}}/developer_guide/in_app_messages/html_messages/#android_embedding-youtube-content)を参照してください。

**自動再生**: ハードウェアアクセラレーションが有効であっても、Android WebViewではメディア再生を開始するためにユーザージェスチャーが必要になる場合があります。自動再生が必要な場合は、HTMLアプリ内メッセージのレンダリングに使用されるWebViewで[`WebSettings.setMediaPlaybackRequiresUserGesture(false)`](https://developer.android.com/reference/android/webkit/WebSettings#setMediaPlaybackRequiresUserGesture(boolean))を設定して、ユーザージェスチャー要件を無効にしてください。これにはHTMLアプリ内メッセージの表示方法に対するSDKレベルのカスタマイズが必要です。セットアップガイダンスについては、[Braze SDKのアプリ内メッセージをカスタマイズする]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=android)を参照してください。

## iOSに関する考慮事項 {#ios-considerations}

iOSデバイスをサポートするには:

- フルスクリーン再生はサポートされていないため、`playsinline` 属性を含める必要があります。
- **iOSでは自動再生が保証されません**。iOSの再生動作は `WKWebView` とOSレベルのメディアポリシーに依存しており、`autoplay` と `muted` が設定されていてもユーザージェスチャーが必要になる場合があります。ターゲットのiOSバージョンとデバイスでHTMLアプリ内メッセージをテストしてください。

自動再生が必要で、テストによりデフォルトでは動作しないことが判明した場合は、HTMLアプリ内メッセージで使用される `WKWebViewConfiguration` をカスタマイズして、メディア再生のユーザーアクション要件を調整できます。たとえば、`mediaTypesRequiringUserActionForPlayback` プロパティを設定します。これにはSDKレベルのカスタマイズが必要です。Swiftリソースについては、[Braze SDKのアプリ内メッセージをカスタマイズする]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=swift)および[SwiftのWebViewにBraze JavaScriptインターフェイスを追加する]({{site.baseurl}}/developer_guide/in_app_messages/html_messages/?sdktab=swift)を参照してください。

## Webに関する考慮事項 {#web-considerations}

最新のブラウザのほとんどは、特定の条件下（一般的に動画がミュートされている場合）でのみ自動再生を許可しています。Webアプリ内メッセージで `autoplay` を使用する場合は、`muted` を含め、サポートするブラウザとデバイスでテストしてください。ブラウザのポリシーは異なり、場合によってはユーザージェスチャーが必要になることがあります。

Webアプリ内メッセージでYouTube動画を自動再生するには、URLパラメーター `&autoplay=1` を追加します。たとえば、以下の動画は自動再生され、ミュートされ（`&mute=1`）、コントロールが非表示になります（`&controls=0`）:

`````````html
<iframe class="video" src="https://www.youtube.com/embed/VPIPAc4oQqw?autoplay=1&mute=1&controls=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

## YouTube動画の表示方法 {#how-youtube-videos-display}

- YouTube埋め込みのアプリ内メッセージは、プラットフォームに応じて、アプリ内に直接表示されるか、アプリ内の別のタブに表示されます。
- YouTube埋め込みが表示されている場合、アプリ内メッセージのテキストが表示されないことがあります。

## トラブルシューティング {#troubleshooting}

アプリ内メッセージに動画が表示されない場合:

- URLが有効であることを確認してください。
- `type="video/mp4"` 宣言が欠落していないことを確認してください（YouTube以外の動画の場合）。
- 不足している閉じタグを追加し、タイプミスを修正してください。