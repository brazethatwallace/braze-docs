---
nav_title: Fehlerbehebung
article_title: Fehlerbehebung für HTML-E-Mails
page_order: 9
description: "Diagnostizieren Sie Probleme mit dem Rendering und dem Editor von HTML-E-Mails mithilfe eines Symptomindex und standardisierter Schritte zur Fehlerbehebung."
channel: email
---

# Fehlerbehebung für HTML-E-Mails {#troubleshoot-html-emails}

> Verwenden Sie diese Seite, um häufige Probleme mit dem HTML-E-Mail-Editor und dem Testversand zu beheben. Informationen zu Inbox Vision und Zustellbarkeit finden Sie unter [Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision) und [E-Mail-Einrichtung]({{site.baseurl}}/user_guide/channels/email/email_setup).

## Hier starten: Symptom zuordnen {#start-here-match-your-symptom}

Ordnen Sie Ihr Symptom in der Tabelle zu, um zum entsprechenden Abschnitt zu navigieren.

| Symptom | Gehe zu |
| --- | --- |
| Test-E-Mail-HTML sieht falsch aus | [HTML wird in Test-E-Mails nicht korrekt dargestellt](#html-renders-incorrectly-in-test-emails) |
| Editor verhält sich in Chrome ungewöhnlich | [Erweiterungskonflikte](#extension-conflicts) |
| E-Mail sieht in verschiedenen Clients unterschiedlich aus | [E-Mail-Rendering](#email-rendering) |
| Inbox-Vision-Vorschau stimmt nicht mit gesendeter E-Mail überein | [CSS-Inlining](#css-inlining) |
| Weißer Raum oder Linien nach Bildern in Test-E-Mails | [Weißer Raum unter Bildern](#white-space-under-images) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="HTML-E-Mail-Symptom" }

## Standardmäßiger Untersuchungspfad {#standard-investigation-path}

Verwenden Sie diesen Workflow, wenn das Rendering oder das Verhalten des Editors bei HTML-E-Mails nicht Ihren Erwartungen entspricht. Beginnen Sie bei Schritt 1.

1. Validieren Sie Ihr HTML-Markup im Editor oder einem externen Validator.
2. Senden Sie eine [Test-E-Mail]({{site.baseurl}}/developer_guide/platform_wide/sending_test_messages#sending-a-test-push-notification-or-in-app-messages-a-classmargin-fix-namepush-inapp-testa) und notieren Sie, welche E-Mail-Clients oder Browser das Problem zeigen.
3. Nutzen Sie die Vorschau mit [Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision#inbox-vision), um das Rendering über verschiedene Clients hinweg zu vergleichen.
4. Schließen Sie [Erweiterungskonflikte](#extension-conflicts) aus, wenn sich der Editor selbst ungewöhnlich verhält.
5. Wenn das Problem weiterhin besteht, eröffnen Sie ein [Support-Ticket]({{site.baseurl}}/braze_support) mit Screenshots aus Inbox Vision und den betroffenen Clients.

## HTML wird in Test-E-Mails nicht korrekt dargestellt {#html-renders-incorrectly-in-test-emails}

**Symptom:** Eine [Test-E-Mail]({{site.baseurl}}/developer_guide/platform_wide/sending_test_messages#sending-a-test-push-notification-or-in-app-messages-a-classmargin-fix-namepush-inapp-testa) entspricht nicht dem, was Sie im Editor erwarten.

Überprüfen Sie zunächst Ihr HTML-Setup und sehen Sie sich dann [Erweiterungskonflikte](#extension-conflicts), [E-Mail-Rendering](#email-rendering), [CSS-Inlining](#css-inlining) und [Weißer Raum unter Bildern](#white-space-under-images) an.

### Erweiterungskonflikte {#extension-conflicts}

Bestimmte Browser-Erweiterungen können Probleme mit dem E-Mail-Editor verursachen. Ein Beispiel ist [Grammarly](https://chrome.google.com/webstore/detail/grammarly-for-chrome/kbfnbcaeplbcioakkpcpgfkobkghlhen?hl=en) in Verbindung mit Google Chrome. Wenn Sie eine dieser Erweiterungen verwenden, sollten Sie entweder:

- Braze-E-Mails in einem Browser bearbeiten, in dem Grammarly nicht als Browser-Erweiterung installiert ist
- Ihren Braze Account Manager kontaktieren und darum bitten, Ihre E-Mail-Editoren auf reines HTML oder Nur-Text umzustellen.

Die Nur-Text-Ansicht entfernt Ihren `WYSIWYG`-Editor (What You See Is What You Get), daher sollten Sie zunächst sicherstellen, dass alle Team-Mitglieder mit HTML vertraut sind, bevor Sie diese Änderung anfordern.

### E-Mail-Rendering {#email-rendering}

E-Mails werden je nach Browser und E-Mail-Client unterschiedlich dargestellt. Notieren Sie sich daher, bei welchen Browsern und E-Mail-Clients Probleme auftreten.

- Nutzen Sie die Vorschau Ihrer E-Mails mit [Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision#inbox-vision), um zu sehen, wie Ihre E-Mails in verschiedenen Browsern und E-Mail-Clients aussehen.
- Nachdem Sie festgestellt haben, welche Browser oder E-Mail-Clients Probleme verursachen, informieren Sie Ihr Entwickler:innen-Team, damit es das HTML anpassen und Änderungen für diese Browser oder E-Mail-Clients vornehmen kann.

### CSS-Inlining {#css-inlining}

Es kann vorkommen, dass die Vorschauen in Inbox Vision nicht mit dem übereinstimmen, was mit Braze versendet wird. Dies kann durch Unterschiede beim CSS-Inlining verursacht werden, das von Braze und anderen Tools durchgeführt wird. Wenn Sie vermuten, dass dies der Fall ist, deaktivieren Sie das CSS-Inlining.

### Weißer Raum unter Bildern {#white-space-under-images}

**Symptom:** Weißer Raum oder Linien erscheinen nach Bildern in Test-E-Mails.

Wenn Sie in Ihren Test-E-Mails weißen Raum oder Linien nach Bildern bemerken, liegt dies in der Regel daran, wie E-Mail-Clients Inline-Elemente rendern. Bilder sind standardmäßig Inline-Elemente und werden an der Grundlinie ausgerichtet, sodass Browser Unterlängen berücksichtigen können (der Teil von Buchstaben wie „g“ oder „y“, der unter die Grundlinie reicht). Dadurch entsteht ein kleiner Abstand, der als weißer Raum erscheint.

Um dies zu beheben, fügen Sie `display: block;` zu Ihrem Bild-CSS hinzu:

```html
<style>
  img {
    display: block;
  }
</style>
```

Alternativ können Sie den Stil direkt auf bestimmte Bilder anwenden:

```html
<img src="https://example.com/image.jpg" style="display: block;" alt="Image description" />
```
