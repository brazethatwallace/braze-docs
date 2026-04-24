---
nav_title: カスタムコードとJavaScriptブリッジ
article_title: バナー用カスタムコードとJavaScriptブリッジ
page_order: 2
page_type: reference
description: "バナーでカスタムHTMLを使用する方法と、JavaScriptブリッジを使用してクリックを記録しBrazeアクションをトリガーする方法について説明します。"
channel:
  - banners
---

# バナー用カスタムコードとJavaScriptブリッジ

> バナーコンポーザーで**カスタムコード**エディターブロックを使用する場合、クリックを記録するにはカスタムHTML内から`brazeBridge.logClick()`を呼び出す必要があります。バナーはHTMLアプリ内メッセージと同じJavaScriptブリッジを使用するため、同じメソッドとパターンが適用されます。

バナーデザインでカスタムHTMLを使用する場合、Braze SDKはカスタムコード内の要素にクリックリスナーを自動的にアタッチできません。キャンペーン分析で追跡したいクリック可能な要素（リンク、ボタンなど）に対して、明示的に`brazeBridge.logClick()`を呼び出す必要があります。

例えば、カスタムHTML内のボタンをユーザーがタップしたときにクリックを記録するには、次のようにします。

```html
<button onclick="brazeBridge.logClick()">
  Click me
</button>
```

利用可能なすべてのメソッドやクリックトラッキングオプションを含むJavaScriptブリッジの完全なリファレンスについては、以下のセクションを参照してください。

## JavaScriptブリッジ {#javascript-bridge}

{% include javascript_bridge/reference.md %}