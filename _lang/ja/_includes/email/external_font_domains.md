### 外部フォントドメイン {#external-font-domains}

カスタム{{ include.page_type }}ページを作成する際、Brazeはクロスサイトスクリプティング（XSS）攻撃を防ぐためにHTML入力をサニタイズします。このセキュリティ対策の一環として、フォントURLを含む外部リソースURLは、以下の許可されたドメインからのものでない限り削除されます。

- `assets.appboycdn.com`
- `braze-images.com`
- `cdn.braze.com`
- `cdn.braze.eu`
- `fonts.googleapis.com`
- `fonts.gstatic.com`

{{ include.page_type }}ページでカスタムフォントを使用する必要がある場合は、これらのドメインのいずれかからフォントを参照するか、代わりに[Webセーフフォント](https://www.w3schools.com/cssref/css_websafe_fonts.php)を使用してください。

メールリスト管理のベストプラクティスについては、[メール購読]({{site.baseurl}}/user_guide/channels/email/subscriptions)を参照してください。