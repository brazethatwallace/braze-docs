---
nav_title: Benutzerdefinierter Code und JavaScript-Bridge
article_title: Benutzerdefinierter Code und JavaScript-Bridge für Banner
page_order: 2
page_type: reference
description: "Erfahren Sie, wie Sie benutzerdefiniertes HTML in Bannern und die JavaScript-Bridge verwenden, um Klicks zu protokollieren und Braze-Aktionen auszulösen."
channel:
  - banners
---

# Benutzerdefinierter Code und JavaScript-Bridge für Banner

> Wenn Sie den Editor-Block **Custom Code** im Banner-Composer verwenden, müssen Sie `brazeBridge.logClick()` innerhalb Ihres benutzerdefinierten HTML aufrufen, um Klicks zu protokollieren. Banner verwenden dieselbe JavaScript-Bridge wie HTML-In-App-Nachrichten, sodass dieselben Methoden und Muster gelten.

Wenn Sie benutzerdefiniertes HTML in Ihrem Banner-Design verwenden, kann das Braze SDK nicht automatisch Klick-Listener an Elemente innerhalb Ihres benutzerdefinierten Codes anhängen. Sie müssen `brazeBridge.logClick()` explizit für alle klickbaren Elemente (Links, Buttons und Ähnliches) aufrufen, die Sie in den Kampagnen-Analytics tracken möchten.

Um beispielsweise einen Klick zu protokollieren, wenn ein:e Nutzer:in auf einen Button in Ihrem benutzerdefinierten HTML tippt:

```html
<button onclick="brazeBridge.logClick()">
  Click me
</button>
```

Die vollständige Referenz zur JavaScript-Bridge, einschließlich aller verfügbaren Methoden und Klick-Tracking-Optionen, finden Sie im folgenden Abschnitt.

## JavaScript-Bridge {#javascript-bridge}

{% include javascript_bridge/reference.md %}