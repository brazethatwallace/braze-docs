---
nav_title: "Gmail-Tab „Aktionen“"
article_title: "Gmail-Tab „Aktionen“"
page_order: 8
description: "In diesem Referenzartikel erfahren Sie, wie Sie mit Braze die Gmail-Karte für Mobilgeräteaktionen aus Ihrer E-Mail-Campaign erstellen."
channel:
  - email
toc_headers: h2
---

# Gmail-Tab „Aktionen“ {#gmail-promotions-tab}

> Der [Gmail-Tab „Aktionen“ für Mobilgeräte](https://developers.google.com/gmail/promotab/) ermöglicht es Marketern, über Annotationen in einer „Karte“ mehr Informationen zu senden als nur die Betreffzeile oder den Preheader. Braze bietet ein integriertes Tool, mit dem Sie die Karte aus Ihrer E-Mail-Campaign erstellen können.

## Voraussetzungen {#prerequisites}

Leiten Sie zunächst Ihre Domains und Subdomains an das Outreach-Team für den Gmail-Tab „Aktionen“ unter <a href="mailto:p-promo-outreach@google.com">p-promo-outreach@google.com</a> weiter, um auf die Allowlist von Gmail gesetzt zu werden. So können Sie alle Features nutzen, die reichhaltige Bilder anzeigen, wie z. B. das Produktkarussell für den Gmail-Tab „Aktionen“.

## Karten in Braze erstellen {#build-the-card-with-braze}

Befolgen Sie diese Anleitung, um eine Gmail-Aktionskarte für eine E-Mail-Campaign zu erstellen. Beachten Sie, dass das Verlassen des Bereichs **Content** im Editor die Felder und Informationen auf dem Tab **Gmail Promotion** zurücksetzt. Schließen Sie die Einrichtung Ihrer Aktionskarte ab und kopieren Sie den generierten HTML-Code, damit Sie ihn nicht verlieren.

### 1. Schritt: E-Mail-Campaign erstellen {#step-1-create-an-email-campaign}

[Erstellen Sie zunächst Ihre E-Mail-Campaign]({{site.baseurl}}/user_guide/channels/email/html_editor) und wählen Sie den **HTML code editor** als Bearbeitungsumgebung aus.

### 2. Schritt: Details zur Gmail-Aktionskarte hinzufügen {#step-2-add-details-to-gmail-promotion-card}

Gehen Sie als Nächstes zum Bereich **Content** des HTML-Editors und wählen Sie den Tab **Gmail Promotion**. Füllen Sie die Felder unter **Basic Information** aus und wählen Sie dann **Generate HTML Code**. Dadurch wird das Skript für Ihre Gmail-Aktionskarte im Abschnitt **Copy and Paste HTML code into `<Head>`** generiert.

![Ein Beispiel für die Erstellung einer Karte.]({% image_buster /assets/img/create-gmail-promo.png %})

### 3. Schritt: Gmail-Aktionskarte anpassen {#step-3-customize-your-gmail-promotion-card}

Wählen Sie, ob Sie ein Rabattangebot, eine Deal-Karte, eine Aktionskarte oder alle Optionen für Ihre Gmail-Aktionskarte einbinden möchten.

{% tabs %}
{% tab Rabattangebot %}

Mit einem Rabattangebot können Sie die Gültigkeitsdaten für einen Rabatt festlegen.

1. Aktivieren Sie den Toggle **Discount Offer**.
2. Geben Sie unter **Offer** eine kurze Zusammenfassung des Rabatts ein. Ein Beispiel ist „20 % Rabatt“.
3. Fügen Sie unter **Code** den Aktionscode hinzu, den Nutzer:innen beim Checkout eingeben müssen.
4. Wählen Sie dann das Startdatum und die Startzeit für das Rabattangebot.
5. Legen Sie fest, ob das Rabattangebot zu einem bestimmten Zeitpunkt enden oder nie ablaufen soll.

![Optionen zur Angabe von Angebotswert, Code sowie Startdatum und -zeit für ein Rabattangebot.]({% image_buster /assets/img/gmail_promo_discount_details.png %}){: style="max-width:70%;"}

{% endtab %}
{% tab Deal-Karten %}

Verwenden Sie Deal-Karten, um wichtige Angebotsinformationen direkt am Anfang des E-Mail-Textes bereitzustellen. So können Empfänger:innen die Angebotsdetails schnell erfassen und handeln. Sie können Deal-Karten beispielsweise nutzen, um zeitlich begrenzte Angebote zu bewerben und den Aufwand für Nutzer:innen zu reduzieren, innerhalb von E-Mails nach Details zu suchen.

1. Aktivieren Sie den Toggle **Deal Card**.
2. Geben Sie unter **Offer** eine kurze Zusammenfassung des Rabatts ein. Ein Beispiel ist „20 % Rabatt auf alle Schuhe“.
3. (optional) Fügen Sie unter **Code** den Aktionscode hinzu, den Nutzer:innen beim Checkout eingeben müssen.
4. Geben Sie mindestens eine der folgenden URLs ein.
-  **Offer Page URL:** Die URL für die spezifische Angebots-Landing-Page. Dadurch wird ein Button „Jetzt einkaufen“ (oder ähnlich) erstellt. Wir empfehlen, diese URL für Ihre Deal-Karte anzugeben.
- **Merchant Homepage URL:** Die URL für Ihre Hauptseite. Verwenden Sie dieses Feld nur, wenn keine spezifische Angebotsseiten-URL verfügbar ist.
5. (optional) Fügen Sie ein Startdatum für das Angebot hinzu.
6. Legen Sie fest, ob das Angebot zu einem bestimmten Zeitpunkt enden oder nie ablaufen soll.

![Optionen zur Angabe von Angebotswert, Code sowie Startdatum und -zeit für eine Deal-Karte.]({% image_buster /assets/img/gmail_promo_deal_cards.png %}){: style="max-width:70%;"}

{% endtab %}
{% tab Aktionskarten %}

Aktionskarten in Ihrem Produktkarussell sind hilfreich, um Bilder zu Ihrem Angebot bereitzustellen. Sie können auch Variablen in Ihrem Produktkarussell anpassen und bis zu zehn Bildvorschauen einbinden, wobei jedes Bild eindeutig sein muss.

1. Aktivieren Sie den Toggle **Promotion Cards**.
2. Wählen Sie **Add promotion card**. Jedes Bild in Ihrem Produktkarussell muss eine eindeutige URL haben und dasselbe Seitenverhältnis verwenden (4:5, 1:1, 1.91:1).
3. Fügen Sie eine Bild-URL ein.
4. Fügen Sie unter **Target URL** den Link für Ihre Aktion hinzu.

{% alert tip %}
Wir empfehlen, Ihre Produktbilder in die Medienbibliothek hochzuladen und dann die URLs in die entsprechenden Felder zu kopieren. Es werden nur statische Bildformate (PNG und JPEG) akzeptiert. Einige Bildformate (GIF) werden zwar hochgeladen, aber nicht wie erwartet angezeigt.
{% endalert %}

{: start="5"}
5. Passen Sie Ihre Aktionskarte an, indem Sie eine Überschrift, Währung, Preis und Rabattwert hinzufügen.

| Anpassbare Eigenschaft | Beschreibung |
|---|---|
| Überschrift | (optional) Ein- oder zweisätzige Beschreibung der Aktion. Wird unter dem Vorschaubild angezeigt. |
| Währung | (optional) Die Währung des Preises. |
| Preis | Der Preis der Aktion. |
| Rabattwert | Der vom Originalpreis abgezogene Betrag. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="3. Schritt: Gmail-Aktionskarte anpassen" }

![Ein Beispiel für ein Produktkarussell eines Unternehmens namens Motto mit der E-Mail-Überschrift „Unsere meistverkauften Socken sind im Angebot“, mit drei Bildern von Socken und ihren reduzierten Preisen.]({% image_buster /assets/img_archive/product_carousel.png %}){: style="max-width:40%;"}

{% endtab %}
{% endtabs %}

### 4. Schritt: HTML-Code generieren und einfügen {#step-4-generate-and-paste-html-code}

Nachdem Sie Ihre Gmail-Aktionskarte erstellt haben, wählen Sie **Generate HTML code**. Kopieren Sie das Skript und fügen Sie es in das `<head>`-Element des HTML-Codes Ihrer E-Mail ein.

{% alert tip %}
Für den Drag-and-Drop-Editor kopieren Sie den generierten HTML-Code und fügen ihn in den Abschnitt [Custom Head Tags]({{site.baseurl}}/user_guide/channels/email/drag_and_drop#custom-head-tags) unter **Sending Settings** ein.
{% endalert %}

{% alert warning %}
Das Aktionsskript wird nur angezeigt, wenn Ihre E-Mail im Gmail-Tab „Aktionen“ landet. Derzeit verwendet Gmail Algorithmen, um zu bestimmen, wo Ihre E-Mail landet. Wenn jedoch ein:e Nutzer:in Ihre E-Mail jemals als Aktion markiert, wird der Gmail-Algorithmus ignoriert und Ihre E-Mail landet künftig automatisch im Tab „Aktionen“.
{% endalert %}

### 5. Schritt: Mit dem Gmail-Vorschau-Tool testen {#step-5-test-using-gmails-preview-tool}

Um Annotationen für Sendungen mit geringem Volumen zu testen, müssen Sie zunächst das [Vorschau-Tool](https://developers.google.com/workspace/gmail/promotab/preview) von Gmail verwenden, um die Annotationen zu validieren. Wenn Sie diesen Schritt überspringen, werden das Produktkarussell und die Einzelbildvorschau nur bei höheren Sendevolumen ausgelöst.

## Gmail-Karten messen {#measure-gmail-cards}

Gmail liefert keine Analytics zu diesen Karten, und E-Mail-Anbieter (ESPs) wie Braze können kein eigenes Link-Tracking in Links im Header-Bereich (einschließlich Aktionskarten und Produktkarussells) einfügen. Sie können jedoch während der Einrichtung UTM-Parameter oder eindeutige Codes an die URLs anhängen. Diese Parameter ermöglichen es Ihnen, das Engagement über Ihre eigene Website-Analytics oder Ihr Conversion-Tracking zu verfolgen, da das Tracking Teil der URL selbst ist – und nicht vom E-Mail-Anbieter or ESP eingefügt wird. E-Mail-Anbieter or ESP-seitiges Klick-Tracking ist für diese Links nicht verfügbar.

### Bilder einbinden {#incorporate-images}

Gmail hat bessere Ergebnisse mit aussagekräftigen Bildern erzielt, die zum E-Mail-Inhalt passen. Gmail empfiehlt nicht, ein reines Textdesign zu verwenden, da dieser Bereich dafür konzipiert wurde, visuelle Sprache – die für E-Mail-Marketing entscheidend ist – in die Vorschau zu bringen. Verwenden Sie keine Bilder mit abgeschnittenem Text und wiederholen Sie keine Bilder in mehreren Campaigns.

### Angebote beschreiben {#describe-offers}

Gmail empfiehlt nicht, Sätze oder Phrasen wie „Kaufen Sie 1 und erhalten Sie 1 gratis oder Rabatte auf alle Shorts und Shirts“ zu verwenden, da diese abgeschnitten werden können, nicht mehr ins Auge fallen und mit der Betreffzeile konkurrieren. Dieser Bereich sollte nur dazu genutzt werden, Ihre Kund:innen mit Ihrem Messaging anzusprechen. Vermeiden Sie daher Formulierungen wie „Öffnen Sie diese E-Mail jetzt“ oder „Klicken Sie hier für Angebote“. Es ist am besten, Ihre Betreffzeile nicht zu wiederholen.

## Best Practices {#best-practices}

Befolgen Sie generell die [Best Practices für den Gmail-Tab „Aktionen“](https://developers.google.com/gmail/promotab/best-practices).

Berücksichtigen Sie beim Erstellen Ihrer Karte die folgenden Fragen:

- Ist das Annotationsskript gültig? [Vorschau mit Google anzeigen](https://developers.google.com/workspace/gmail/promotab/preview).
- Zeigt **Show original** in Gmail das Skript in der Rohnachricht an?
- Landet die E-Mail unter **Promotions**? Karten werden nur dort angezeigt.
- Haben Sie Desktop und Mobilgerät getestet?

{% alert tip %}
Obwohl Liquid im Skript unterstützt wird, empfehlen wir gründliches Testen, um Fehler zu vermeiden.
{% endalert %}

### Annotation in der Vorschau anzeigen {#preview-your-annotation}

Verwenden Sie das [Vorschau-Tool](https://developers.google.com/workspace/gmail/promotab/preview), um Ihre Annotation in der Vorschau anzuzeigen. Beachten Sie, dass das Senden einer Test-E-Mail an sich selbst für Annotationen nicht funktioniert, da Ihre Annotation nur gerendert wird, wenn die E-Mail an eine signifikante Anzahl von Empfänger:innen gesendet werden muss. Stellen Sie sicher, dass Sie die finale E-Mail (mit ihren Bild-URLs) an mindestens 100 Gmail-Empfänger:innen senden.

Verwenden Sie nicht Google Workspace, um E-Mails mit Annotationen zu senden. Verwenden Sie nur auf der Allowlist stehende E-Mail-Domains, um Annotationen an eine große Gruppe von Empfänger:innen zu senden.

### Bildrichtlinien einhalten {#adhere-to-image-guidelines}

Stellen Sie sicher, dass Ihre Bilder diesen Richtlinien entsprechen:
- Verwenden Sie hochwertige Bilder mit hoher Auflösung.
- Alle annotierten Bilder verwenden dasselbe Seitenverhältnis. Unterstützte Seitenverhältnisse sind: 4:5, 1:1, 1.91:1.
- Verwenden Sie korrekte Bildgrößen. Das Minimum beträgt 256x256; das Maximum beträgt 4096x4096 Pixel.

Gmail empfiehlt, Folgendes zu vermeiden:
- Übermäßige Verwendung von Text in Ihren Bildern
- Verwendung von Bildern, die nur Icons sind
- Verwendung von Bildern mit runden Masken
- Verwendung personalisierter Bild-URLs

### Bei DMARC Registrierung or registrieren {#register-with-dmarc}

Damit Ihre Annotationen korrekt gerendert werden, bestätigen Sie, dass die eingereichten Domains bei DMARC registriert sind und alle Richtlinien aktiviert sind.

## Häufig gestellte Fragen {#frequently-asked-questions}

### Wie füge ich ein Absenderlogo hinzu? {#how-do-i-add-a-sender-logo}

Verwenden Sie [Google Annotations](https://developers.google.com/workspace/gmail/promotab/overview), um Ihr Logo und Ihre Aktionskarte in der Gmail-App hinzuzufügen. Das Rendering wird von Gmail gesteuert, nicht von Braze.

### Warum zeigt meine Werbenachricht die Aktionskarte oder das Produktkarussell nicht im Posteingang der Endnutzer:innen an? {#why-is-my-promotional-message-not-displaying-the-promotion-card-or-product-carousel-in-the-end-users-inbox}

Es gibt viele Faktoren, die bestimmen, ob das Produktkarussell im Gmail-Tab „Aktionen“ angezeigt wird.

Alle Bilder in der Annotation müssen weiterhin einen Qualitätsfilter bestehen. Damit das Produktkarussell angezeigt wird, müssen alle Bilder in der Annotation das empfohlene Seitenverhältnis haben und hochwertige, hochauflösende Nahaufnahmen von Produkten sein. Die Bilder sollten wenig bis keinen Text enthalten. Der Qualitätsfilter filtert auch unangemessene Inhalte, sodass die Bilder familien-, nutzer:innen- und kinderfreundlich sein müssen.

Darüber hinaus hat Gmail eine Dichtebegrenzung dafür, wie viele Produktkarussells im Gmail-Tab „Aktionen“ einer Nutzerin oder eines Nutzers angezeigt werden. Wenn beispielsweise ein:e Nutzer:in viele Marken abonniert hat, die Produktkarussells in ihren Aktions-E-Mails verwenden, begrenzt Gmail irgendwann die Anzahl der angezeigten Produktkarussells.

Aufgrund der Datenschutz- und Sicherheitsvorschriften von Google müssen E-Mails mit Annotationen breit versendet werden, damit die Annotation funktioniert. Es wird empfohlen, eine Campaign zu starten und sie an mindestens 100 Empfänger:innen zu senden, damit Googles System sie als „Massenversand“ erkennt. Bild-URLs dürfen nicht zwischen Empfänger:innen variieren.

### Wie werden Klicks auf eine Aktionskarte oder ein Produktkarussell getrackt? {#how-are-clicks-on-a-promotion-card-or-product-carousel-tracked}

Braze oder andere ESPs können kein Link-Tracking in Links im Header-Bereich einfügen. Das bedeutet, dass Klicks auf eine Aktionskarte oder ein Produktkarussell nicht getrackt werden können.

### Gibt es eine Möglichkeit zu sehen, wie viele Nutzer:innen ein Produktkarussell erhalten haben? {#is-there-a-way-to-see-how-many-users-received-a-product-carousel}

Gmail bestimmt, wann und wem die Karte angezeigt wird, sodass es keine Garantie gibt, dass jede:r Empfänger:in das Produktkarussell sieht.

### Warum sehe ich keine Annotationen in meinem Gmail-Tab „Aktionen“? {#why-dont-i-see-annotations-in-my-gmail-promotions-tab}

Annotationen werden für Google Workspace nicht unterstützt. Um Annotationen in der Vorschau anzuzeigen, können Sie eine persönliche E-Mail-Adresse bei Gmail erstellen.

Beachten Sie, dass Annotationen nicht im Tab **Allgemein** oder in einem anderen Tab in der mobilen Gmail-App gerendert werden. Annotationen werden nicht angezeigt, nachdem ein:e Nutzer:in eine E-Mail geöffnet hat oder wenn Sie den Annotationstyp `DiscountOffer` verwenden und das Datum und die Uhrzeit bereits abgelaufen sind.

{% alert tip %}
Weitere Informationen zur Fehlerbehebung finden Sie in [Googles Leitfaden zur Fehlerbehebung für E-Mail-Aktionen](https://developers.google.com/workspace/gmail/promotab/troubleshooting).
{% endalert %}