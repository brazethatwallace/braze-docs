---
nav_title: カスタムコードとJavaScriptブリッジ
article_title: バナー用のカスタムコードとJavaScriptブリッジ
page_order: 2
page_type: reference
description: "バナーでのカスタムHTMLの使用方法と、JavaScriptブリッジを使ってクリックを記録し、Brazeアクションをトリガーする方法を学ぶ。"
channel:
  - banners
---

# バナー用のカスタムコードとJavaScriptブリッジ {#custom-code-and-javascript-bridge-for-banners}

> バナーコンポーザーで**カスタムコード**エディターブロックを使用する場合、クリックを記録するにはカスタムHTML内から`brazeBridge.logClick()`を呼び出す必要があります。バナーはHTMLアプリ内メッセージと同じJavaScriptブリッジを使用するため、同じメソッドとパターンが適用されます。

バナーデザインでカスタムHTMLを使用する場合、Braze SDKはカスタムコード内の要素にクリックリスナーを自動的にアタッチできません。キャンペーン分析でトラッキングしたいクリック可能な要素（リンク、ボタンなど）については、明示的に`brazeBridge.logClick()`を呼び出す必要があります。

例えば、カスタムHTML内のボタンをユーザーがタップした際にクリックを記録するには、次のようにします。

```html
<button onclick="brazeBridge.logClick()">
  Click me
</button>
```

利用可能なすべてのメソッドやクリックトラッキングオプションを含む完全なJavaScriptブリッジリファレンスについては、以下のセクションを参照してください。

## JavaScriptブリッジ {#javascript-bridge}

{% include javascript_bridge/reference.md %}