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

Ordnen Sie Ihr Symptom in der folgenden Tabelle zu, um zum entsprechenden Abschnitt zu navigieren.

| Symptom | Gehe zu |
| --- | --- |
| HTML der Test-E-Mail sieht falsch aus | [HTML wird in Test-E-Mails nicht korrekt dargestellt](#html-renders-incorrectly-in-test-emails) |
| Editor verhält sich in Chrome unerwartet | [Erweiterungskonflikte](#extension-conflicts) |
| E-Mail sieht in verschiedenen Clients unterschiedlich aus | [E-Mail-Rendering](#email-rendering) |
| E-Mail zeigt Liquid-Code oder fehlerhafte Links an | [Unausgeglichenes HTML in Liquid-Templates](#unbalanced-html-in-liquid-templates) |
| Inbox Vision-Vorschau stimmt nicht mit gesendeter E-Mail überein | [CSS-Inlining](#css-inlining) |
| Leerraum oder Linien nach Bildern in Test-E-Mails | [Leerraum unter Bildern](#white-space-under-images) |
| Klick-Analytics enthalten keine Abfrageparameter | [Einschränkungen bei Link-Klick-Analytics](#link-click-analytics-limitations) |
| Hochgestellte Zeichen verursachen inkonsistenten Zeilenabstand | [Probleme mit der Zeilenhöhe bei hochgestellten Zeichen](#superscript-line-height-issues) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="HTML-E-Mail-Symptom" }

## Standardmäßiger Untersuchungspfad {#standard-investigation-path}

Verwenden Sie diesen Workflow, wenn das Rendering von HTML-E-Mails oder das Verhalten des Editors nicht Ihren Erwartungen entspricht. Beginnen Sie bei Schritt 1.

1. Validieren Sie Ihr HTML-Markup im Editor oder einem externen Validator.
2. Senden Sie eine [Test-E-Mail]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages) und notieren Sie, bei welchen E-Mail-Clients oder Browsern das Problem auftritt.
3. Nutzen Sie die Vorschau mit [Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision), um das Rendering über verschiedene Clients hinweg zu vergleichen.
4. Schließen Sie [Konflikte mit Browser-Erweiterungen](#extension-conflicts) aus, wenn sich der Editor selbst unerwünscht verhält.
5. Wenn das Problem weiterhin besteht, erstellen Sie ein [Support-Ticket]({{site.baseurl}}/user_guide/administer/personal/braze_support) mit Screenshots aus Inbox Vision und den betroffenen Clients.

## HTML wird in Test-E-Mails nicht korrekt dargestellt {#html-renders-incorrectly-in-test-emails}

### Symptom {#symptom}

Eine [Test-E-Mail]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages) entspricht nicht dem, was Sie im Editor erwarten.

Überprüfen Sie zunächst Ihr HTML-Setup und sehen Sie sich dann [Erweiterungskonflikte](#extension-conflicts), [E-Mail-Rendering](#email-rendering), [CSS-Inlining](#css-inlining) und [Weißer Raum unter Bildern](#white-space-under-images) an.

### Erweiterungskonflikte {#extension-conflicts}

Bestimmte Browser-Erweiterungen können Probleme mit dem E-Mail-Editor verursachen. Ein Beispiel ist [Grammarly](https://chrome.google.com/webstore/detail/grammarly-for-chrome/kbfnbcaeplbcioakkpcpgfkobkghlhen?hl=en) in Verbindung mit Google Chrome. Wenn Sie eine dieser Erweiterungen verwenden, sollten Sie entweder:

- Braze-E-Mails in einem Browser bearbeiten, in dem Grammarly nicht als Browser-Erweiterung installiert ist
- Ihren Braze Account Manager:in kontaktieren und darum bitten, Ihre E-Mail-Editoren auf reines HTML oder Nur-Text umzustellen.

Die Nur-Text-Ansicht entfernt Ihren `WYSIWYG`-Editor (What You See Is What You Get), daher sollten Sie zunächst sicherstellen, dass alle Teammitglieder mit HTML vertraut sind, bevor Sie diese Änderung anfordern.

### E-Mail-Rendering {#email-rendering}

E-Mails werden je nach Browser und E-Mail-Client unterschiedlich dargestellt. Notieren Sie sich daher, bei welchen Browsern und E-Mail-Clients Probleme auftreten.

- Nutzen Sie die Vorschau Ihrer E-Mails mit [Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision), um zu sehen, wie Ihre E-Mails in verschiedenen Browsern und E-Mail-Clients aussehen.
- Nachdem Sie festgestellt haben, welche Browser oder E-Mail-Clients Probleme verursachen, informieren Sie Ihr Entwickler:innen-Team, damit es das HTML anpassen und Änderungen für diese Browser oder E-Mail-Clients vornehmen kann.
- Wenn das Problem speziell damit zusammenhängt, [wie Alternativtext angezeigt wird]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility#how-email-clients-display-alt-text), beachten Sie, dass dieses Verhalten vom E-Mail-Client der Empfänger:innen gesteuert wird, nicht von Braze.

### Unausgeglichenes HTML in Liquid-Templates {#unbalanced-html-in-liquid-templates}

#### Symptom

Einige Nutzer:innen erhalten eine veränderte Version der E-Mail, in der Liquid-Code in der Nachricht angezeigt wird, Links fehlerhaft sind oder Abstände falsch aussehen.

Braze verwendet einen internen HTML-Parser, um E-Mails vor dem Versand aufzubereiten. Dieser Parser unterstützt Features wie Preheader-Generierung, Tracking-Pixel-Platzierung, Link-Templating und Link Aliasing. Wenn HTML-Tags innerhalb der zugehörigen Liquid-Logikblöcke oder Content Blocks nicht ausgeglichen sind, kann der Parser das zugrunde liegende HTML auf unerwartete Weise verändern. Dies kann zu folgenden Problemen führen:

- Zeilenumbrüche aus dem Liquid-Rendering in einigen E-Mail-Clients
- Ungewöhnliche Abstände durch `<p>`-Tags, die dem E-Mail-Body hinzugefügt werden
- Inhalte des `<head>`-Tags werden in den Preheader verschoben
- Inkonsistentes Rendering auf verschiedenen mobilen Betriebssystemen
- AMP-spezifischer Code wird aus AMP-E-Mail-Bodys entfernt, was zu Validierungsfehlern führt
- Fehlerhafte Links bei Verwendung vieler verschiedener Query-Parameter oder Media Queries

#### HTML innerhalb von Liquid-Blöcken ausgleichen {#balance-html-within-liquid-blocks}

Stellen Sie sicher, dass alle HTML-Tags innerhalb des zugehörigen Liquid-Logikblocks oder Content-Blocks geöffnet und geschlossen werden. Dies verhindert, dass der interne Parser das HTML als ungültig interpretiert und es verändert.

#### Unausgeglichenes Beispiel {#unbalanced-example}

{% raw %}
```liquid
<img src={% if ${language} == 'en' %}"https://example.com/images/banner-en.png" style="width: 100%"{% elsif ${language} == 'de' %}"https://example.com/images/banner-de.png"{% else %}"https://example.com/images/banner-default.png" {% endif %} />
```
{% endraw %}

In diesem Beispiel beginnt das öffnende `<img`-Tag außerhalb eines Liquid-Blocks, und verschiedene Teile der Tag-Attribute sind über Liquid-Bedingungsanweisungen verteilt. Diese Struktur verwirrt den Parser, der nicht bestimmen kann, wo das Tag beginnt oder endet.

#### Ausgeglichenes Beispiel {#balanced-example}

{% raw %}
```liquid
{% if ${language} == 'en' %}
  <img src="https://example.com/images/banner-en.png" style="width: 100%;" />
{% elsif ${language} == 'de' %}
  <img src="https://example.com/images/banner-de.png" style="width: 100%;" />
{% else %}
  <img src="https://example.com/images/banner-default.png" style="width: 100%;" />
{% endif %}
```
{% endraw %}

In der ausgeglichenen Version enthält jeder Liquid-Zweig ein vollständiges, eigenständiges `<img>`-Tag. Dieser Ansatz stellt sicher, dass der Parser jeden Zweig korrekt verarbeitet.

#### Zusätzliche Korrekturen {#additional-fixes}

Wenn bei Ihnen Rendering-Probleme mit Media Queries oder vielen Query-Parametern auftreten, versuchen Sie, das CSS-Inlining in Ihren E-Mail-Einstellungen zu deaktivieren. Dies kann Konflikte zwischen dem HTML-Parser und komplexen CSS-Regeln beheben.

### CSS-Inlining {#css-inlining}

Es kann vorkommen, dass die Vorschauen in Inbox Vision nicht mit dem übereinstimmen, was mit Braze versendet wird. Dies kann durch Unterschiede beim CSS-Inlining verursacht werden, das von Braze und anderen Tools durchgeführt wird. Wenn Sie vermuten, dass dies der Fall ist, deaktivieren Sie das CSS-Inlining.

### Weißer Raum unter Bildern {#white-space-under-images}

#### Symptom

Weißer Raum oder Linien erscheinen nach Bildern in Test-E-Mails.

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

## Einschränkungen bei der Klick-Analytics für Links {#link-click-analytics-limitations}

### Symptom

Die Klick-Analytics für E-Mails mit vielen eindeutigen Abfrageparametern entsprechen nicht Ihren Erwartungen. Möglicherweise sehen Sie aggregierte Klickzahlen für deparametrisierte URLs nach den ersten 100 eindeutigen Links.

### Wie das Link-Klick-Tracking funktioniert {#how-link-click-tracking-works}

Braze verfolgt Klicks sowohl auf parametrisierte URLs (mit Abfrageparametern) als auch auf deparametrisierte Basis-URLs. Für die ersten 100 eindeutigen parametrisierten Links, die in einer E-Mail-Campaign oder einem Canvas angeklickt werden, erfasst und meldet Braze Daten für beide:

- Die vollständige parametrisierte URL (zum Beispiel `https://example.com?user_id=12345`)
- Die deparametrisierte Basis-URL (zum Beispiel `https://example.com`)

Nachdem die ersten 100 eindeutigen parametrisierten Links angeklickt wurden, erhöht Braze die Klickzahlen nur noch für die deparametrisierte Basis-URL. Das bedeutet:

- Klick-Analytics werden auf der Basis-Domain und dem Pfad aggregiert, anstatt auf einzelnen Abfrageparameter-Kombinationen
- Sie können weiterhin aussagekräftiges Engagement basierend auf Link-Pfaden verfolgen
- Das individuelle Klick-Tracking auf Nutzer:innenebene funktioniert weiterhin normal

Dieses Verhalten verhindert, dass Analytics durch Tausende eindeutiger Abfrageparameter-Kombinationen aufgebläht werden, während die allgemeinen Link-Engagement-Muster weiterhin erfasst werden.

### Was das für Ihre Campaigns bedeutet {#what-this-means-for-your-campaigns}

Wenn Sie auf eindeutige Abfrageparameter angewiesen sind, um nutzerspezifisches Verhalten in externen Plattformen zu verfolgen (zum Beispiel `https://example.com?user_id=USER_ID`), beachten Sie, dass die Klick-Analytics von Braze diese Parameter nur für die ersten 100 angeklickten eindeutigen Links beibehalten. Nach diesem Schwellenwert werden Klicks weiterhin in Ihren Analytics erfasst, aber der deparametrisierten URL zugeordnet.

Klickdaten auf Nutzer:innenebene bleiben über [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) oder das [Nachrichtenaktivitätsprotokoll]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) verfügbar, unabhängig davon, wie viele eindeutige parametrisierte Links angeklickt werden.

### Probleme mit der Zeilenhöhe bei hochgestelltem Text {#superscript-line-height-issues}

#### Symptom

Text mit hochgestellten Zeichen wird mit uneinheitlichem Zeilenabstand dargestellt, wobei Zeilen näher zusammen oder weiter auseinander erscheinen als beabsichtigt. Dies ist ein häufiges Darstellungsproblem in E-Mail-Clients und nicht spezifisch für Braze.

Die Verwendung von hochgestelltem Text in E-Mails kann zu unerwartetem Zeilenhöhenverhalten führen, da verschiedene E-Mail-Clients hochgestellten Text unterschiedlich behandeln.

#### Lösung {#resolution}

Verwenden Sie den HTML-Editor, um das Styling von hochgestelltem Text und umgebenden Elementen zu steuern.

Um die Zeilenhöhe explizit zu definieren, fügen Sie Inline-CSS hinzu, um die `line-height` für den Text festzulegen:

```html
<p style="line-height: 1.5;">Example text with superscript<sup style="line-height: inherit;">1</sup></p>
```

Um die vertikale Ausrichtung anzupassen, verwenden Sie die Eigenschaft `vertical-align`, um den hochgestellten Text auszurichten, ohne die Zeilenhöhe zu beeinträchtigen:

```html
<sup style="vertical-align: top; font-size: smaller;">1</sup>
```

Wenn hochgestellter Text weiterhin Probleme verursacht, verwenden Sie als Alternative zu `<sup>` ein `<span>` für mehr Kontrolle:

```html
<span style="font-size: smaller; vertical-align: top;">1</span>
```
