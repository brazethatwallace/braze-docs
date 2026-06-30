---
nav_title: Fehlerbehebung
article_title: Fehlerbehebung
page_order: 9
description: "Dieser Hilfeartikel zeigt Ihnen, wie Sie Probleme mit HTML-E-Mails beheben können."
channel: email
---

# Fehlerbehebung {#troubleshooting}

> Dieser Artikel behandelt häufige Probleme mit HTML-E-Mails und deren Lösung, einschließlich Erweiterungskonflikten, Rendering-Unterschieden und CSS-Inlining.

## HTML wird in Test-E-Mails nicht korrekt dargestellt {#html-renders-incorrectly-in-test-emails}

Wenn Ihre [Test-E-Mail]({{site.baseurl}}/developer_guide/platform_wide/sending_test_messages#sending-a-test-push-notification-or-in-app-messages-a-classmargin-fix-namepush-inapp-testa) nicht richtig aussieht, empfehlen wir, zunächst Ihr HTML-Setup zu überprüfen. Anschließend können Sie nach folgenden Problemen suchen:
* [Erweiterungskonflikte](#check-conflicts)
* [E-Mail-Rendering](#check-rendering)
* [CSS-Inlining](#switch-css-inlining)

### Erweiterungskonflikte {#extension-conflicts}

Bestimmte Browser-Erweiterungen können Probleme mit unserem E-Mail-Editor verursachen. Ein Beispiel ist [Grammarly](https://chrome.google.com/webstore/detail/grammarly-for-chrome/kbfnbcaeplbcioakkpcpgfkobkghlhen?hl=en) in Verbindung mit Google Chrome. Wenn Sie eine dieser Erweiterungen verwenden, sollten Sie entweder:
- Braze-E-Mails in einem Browser bearbeiten, in dem Grammarly nicht als Browser-Erweiterung installiert ist
- Ihren Braze Account Manager kontaktieren und darum bitten, Ihre E-Mail-Editoren auf reines HTML oder Nur-Text umzustellen.

Die Nur-Text-Ansicht entfernt Ihren `WYSIWYG`-Editor (What You See Is What You Get), daher sollten Sie zunächst sicherstellen, dass alle Team-Mitglieder mit HTML vertraut sind, bevor Sie diese Änderung anfordern.

### E-Mail-Rendering {#email-rendering}

E-Mails werden je nach Browser und E-Mail-Client unterschiedlich dargestellt. Notieren Sie sich daher, bei welchen Browsern und E-Mail-Clients Probleme auftreten.

- Nutzen Sie die Vorschau Ihrer E-Mails mit [Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision#inbox-vision), um zu sehen, wie Ihre E-Mails in verschiedenen Browsern und E-Mail-Clients aussehen.
- Nachdem Sie festgestellt haben, welche Browser oder E-Mail-Clients Probleme verursachen, informieren Sie Ihr Entwickler:innen-Team, damit es das HTML anpassen und Änderungen für diese Browser oder E-Mail-Clients vornehmen kann.

### CSS-Inlining

Es kann vorkommen, dass die Vorschauen in Inbox Vision nicht mit dem übereinstimmen, was mit Braze versendet wird. Dies kann durch Unterschiede beim CSS-Inlining verursacht werden, das von Braze und anderen Tools durchgeführt wird. Wenn Sie vermuten, dass dies der Fall ist, deaktivieren Sie das CSS-Inlining.

Benötigen Sie weitere Hilfe? Eröffnen Sie ein [Support-Ticket]({{site.baseurl}}/braze_support).