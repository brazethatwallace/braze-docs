WhatsApp テンプレートを作成する前に、[WhatsApp のセットアップ]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/)を完了し、以下を準備する必要があります。
- Braze に接続済みのアクティブな WhatsApp Business アカウント（WABA）
- WABA 内に設定済みの適切なサブスクリプショングループ
- アップロード用のメディアアセット（画像または動画）
- 管理者以外のユーザーに対する Braze の権限
    - テンプレートビルダーで新規テンプレートを作成するユーザーの場合:
        - 「View WhatsApp Message Templates」
        - 「Edit WhatsApp Message Templates」
    - カルーセルテンプレートを使用してキャンペーンまたはキャンバスを作成するユーザーの場合:
        - 「View WhatsApp Message Templates」
- Liquid テンプレートの理解（オプション、ダイナミックなコンテンツ向け）

{% alert important %}
同じ WhatsApp Business アカウント（WABA）内のすべての電話番号とサブスクリプショングループはテンプレートを共有します。1つの WABA 内に複数のサブスクリプショングループがある場合、すべてのグループが同じカルーセルテンプレートにアクセスできます。ただし、異なる WABA 間ではテンプレートは共有されません。
{% endalert %}