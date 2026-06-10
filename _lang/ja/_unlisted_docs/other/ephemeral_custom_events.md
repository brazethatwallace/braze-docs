---
nav_title: エフェメラルカスタムイベント
permalink: /ephemeral_custom_events/
hidden: true
page_type: reference
---

# エフェメラルカスタムイベント {#ephemeral-custom-events}

- エフェメラルカスタムイベントには、購入イベントやセッション開始・セッション終了（Brazeドキュメントに記載）は含まれません。
- Brazeは、SDK実装ごとに最大12のプレースメント/イベント名について、カスタムイベントをデータポイントとしてBrazeに送信・保存しません。
- エフェメラルイベントソリューションは、Brazeの本番用iOSおよびAndroid SDKに組み込まれており、Brazeがエフェメラルカスタムイベントソリューションを有効にしたプラットフォーム向けの将来のBraze本番用SDKにも組み込まれます。これにより、顧客はそのような本番用SDKを使用でき、将来の機能やバグ修正との同期が失われることはありません。また、顧客は他のカスタムプロセスを必要とせずに、将来のSDK更新を活用できます。
<!--
Keep this doc available on the docs site with the above permalink until 1/21/2026. This feature was built as a one-off page for a customer. Reach out to Rod Amies with questions, if needed.
-->