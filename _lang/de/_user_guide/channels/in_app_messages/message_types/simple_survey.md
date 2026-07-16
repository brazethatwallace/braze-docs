---
nav_title: "Einfache Umfrage"
article_title: Einfache Umfrage als In-App-Nachricht
page_order: 6
page_type: reference
description: "Dieser Referenzartikel beschreibt, wie Sie Nutzerattribute, Insights und Präferenzen erfassen können, um Ihre Campaign-Strategie mithilfe von In-App-Nachrichten-Umfragen zu unterstützen."
channel:
  - in-app messages
tool:
  - Templates
---

# Einfache Umfrage {#simple-survey}

> Verwenden Sie das In-App-Nachrichten-Template **Simple Survey**, um Nutzerattribute, Insights und Präferenzen zu erfassen, die Ihre Campaign-Strategie unterstützen.

Dieser Nachrichtentyp ist im [traditionellen Editor]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional) verfügbar.

Häufige Anwendungsfälle für Umfragen sind z. B. die Frage, wie Nutzer:innen Ihre App nutzen möchten, mehr über ihre persönlichen Präferenzen zu erfahren oder ihre Zufriedenheit mit einem bestimmten Feature abzufragen.

![Drei einfache Umfragenachrichten: Benachrichtigungspräferenzen, Ernährungspräferenzen und eine Kundenzufriedenheitsumfrage. Die ausgewählten Optionen in den Umfragen entsprechen angepassten Attributen, die für die jeweiligen Nutzer:innen protokolliert werden.]({% image_buster /assets/img/iam/iam-survey.png %})

## SDK-Anforderungen {#supported-sdk-versions}

Diese In-App-Nachricht wird nur an Geräte ausgeliefert, die [Flex CSS](https://caniuse.com/flexbox) unterstützen, und erfordert mindestens die folgenden [SDK-Versionen]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/new_features#filtering-by-most-recent-app-versions).

{% sdk_min_versions ios:3.23.0 android:8.0.0 web:2.5.0 %}

{% alert note %}
Um HTML-In-App-Nachrichten über das Web-SDK zu aktivieren, müssen Sie die Initialisierungsoption `allowUserSuppliedJavascript` an Braze übergeben.
{% endalert %}

## Eine Umfrage erstellen {#create}

Wenn Sie eine [In-App-Nachricht]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional) erstellen, wählen Sie **Simple Survey** als **Nachrichtentyp** aus.

Dieses Umfrage-Template wird sowohl für mobile Apps als auch für Webbrowser unterstützt. Stellen Sie sicher, dass Ihre SDKs die für dieses Feature erforderlichen [Mindest-SDK-Versionen](#supported-sdk-versions) erfüllen.

### Schritt 1: Umfragefrage hinzufügen {#step-1-add-your-survey-question}

Um mit der Erstellung Ihrer Umfrage zu beginnen, fügen Sie Ihre Frage in das Feld **Header** der Umfrage ein. Bei Bedarf können Sie eine optionale **Body**-Nachricht hinzufügen, die unter Ihrer Umfragefrage angezeigt wird.

![Tab „Verfassen“ des einfachen Umfrage-Editors mit Feldern für einen Header, einen optionalen Body und einen optionalen Hilfetext.]({% image_buster /assets/img/iam/iam-survey2.png %}){: style="max-width:90%"}

{% alert tip %}
Diese Felder können sowohl Liquid als auch Emojis enthalten – lassen Sie Ihrer Kreativität freien Lauf!
{% endalert %}

### Schritt 2: Auswahlmöglichkeiten konfigurieren {#single-multiple-choice}

Sie können bis zu 12 Auswahlmöglichkeiten in einer Umfrage hinzufügen.

Wählen Sie entweder **Single-choice selection** oder **Multiple-choice selection**. Der **Hilfetext** wird automatisch aktualisiert, wenn Sie zwischen den beiden Optionen wechseln, um Nutzer:innen darüber zu informieren, wie viele Auswahlmöglichkeiten sie auswählen können.

Legen Sie dann fest, ob Sie [angepasste Attribute erfassen](#custom-attributes) oder [nur Antworten protokollieren](#no-attributes) möchten.

![Dropdown für Auswahlmöglichkeiten mit ausgewählter Option „Log attributes upon submission“.]({% image_buster /assets/img/iam/collect-attributes.png %}){: style="max-width:60%"}

#### Angepasste Attribute erfassen {#custom-attributes}

Wählen Sie **Log attributes upon submission**, um Attribute basierend auf der Antwort der Nutzer:innen zu erfassen. Sie können diese Option verwenden, um neue Segmente und Retargeting-Campaigns zu erstellen. Beispielsweise könnten Sie in einer [Zufriedenheitsumfrage](#user-satisfaction) eine Follow-up-E-Mail an alle Nutzer:innen senden, die nicht zufrieden waren.

Um jeder Auswahlmöglichkeit ein angepasstes Attribut hinzuzufügen, wählen Sie einen Namen für das angepasste Attribut aus dem Dropdown-Menü aus (oder erstellen Sie ein neues) und geben Sie dann den Wert ein, der gesetzt werden soll, wenn diese Auswahl abgesendet wird. Sie können auch ein neues angepasstes Attribut auf Ihrer [Einstellungsseite]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data) erstellen.

Der Datentyp Ihrer angepassten Attribute ist wichtig und hängt davon ab, wie Sie Ihre Umfrage eingerichtet haben.

- **Multiple-choice selection:** Der Datentyp des angepassten Attributs muss ein Array sein. Wenn das angepasste Attribut auf einen anderen Datentyp eingestellt ist, werden Antworten nicht protokolliert.
- **Single-choice selection:** Der Datentyp des angepassten Attributs muss ein String sein. Angepasste Attribute, die nicht vom Typ String sind, werden nicht im Dropdown angezeigt, und Antworten werden nicht protokolliert.

{% alert important %}
Wenn die Erfassung angepasster Attribute aktiviert ist, werden Auswahlmöglichkeiten, die denselben Namen für das angepasste Attribut verwenden, in einem Array zusammengefasst.
{% endalert %}

##### Beispiel {#example}

In einer [Umfrage zu Benachrichtigungspräferenzen](#notification-preferences) könnten Sie beispielsweise jede Auswahlmöglichkeit als boolesches (true/false) Attribut anlegen, damit Nutzer:innen auswählen können, welche Themen sie interessieren. Wenn eine Nutzer:in die Auswahl „Aktionen“ ankreuzt, wird ihr [Nutzerprofil]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle) mit dem angepassten Attribut `Promotions Topic` auf `true` aktualisiert. Wenn die Auswahl nicht angekreuzt wird, bleibt dasselbe Attribut unverändert.

Sie können dann den Filter `Custom Attribute` verwenden, um ein Segment für Nutzer:innen mit dem angepassten Attribut `Promotions Topic` `is` `true` zu erstellen, damit nur Nutzer:innen, die an Ihren Aktionen interessiert sind, die relevanten Campaigns erhalten.

#### Nur Antworten protokollieren {#no-attributes}

Alternativ können Sie **Log responses only (no attributes)** wählen. Wenn diese Option ausgewählt ist, werden Umfrageantworten als Button-Klicks protokolliert, aber angepasste Attribute werden nicht im Profil der Nutzer:innen gespeichert. Das bedeutet, dass Sie weiterhin die Klick-Metriken für jede Umfrageoption einsehen können (siehe [Analytics](#analytics)), aber diese Auswahl wird nicht in ihrem Nutzerprofil widergespiegelt.

Diese Klick-Metriken stehen nicht für Retargeting zur Verfügung.

### Schritt 4: Absendeverhalten festlegen {#step-4-choose-submission-behavior}

Sobald eine Nutzer:in ihre Antwort absendet, können Sie optional eine Bestätigungsseite anzeigen oder die Nachricht einfach schließen.

Eine Bestätigungsseite ist ein guter Ort, um Nutzer:innen für ihre Zeit zu danken oder zusätzliche Informationen bereitzustellen. Sie können den Call-to-Action auf dieser Seite anpassen, um Nutzer:innen zu einer anderen Seite Ihrer App oder Website zu leiten.

Bearbeiten Sie Ihren Button-Text und das Klickverhalten im Abschnitt **Submit Button** am unteren Rand des Tabs **Survey**:

![Klickverhalten eingestellt auf „Submit responses and display confirmation page“.]({% image_buster /assets/img/iam/confirmation-option.png %}){: style="max-width:60%"}

Wenn Sie eine Bestätigungsseite hinzufügen möchten, wechseln Sie zum Tab **Confirmation Page**, um Ihre Nachricht anzupassen:

![Tab „Confirmation Page“ des einfachen Umfrage-Editors. Die verfügbaren Felder sind Header, optionaler Body, Button-Text und Button-Klickverhalten.]({% image_buster /assets/img/iam/confirmation-page.png %}){: style="max-width:90%"}

Wenn Sie Nutzer:innen zu einer anderen Seite Ihrer App oder Website leiten möchten, ändern Sie das **Klickverhalten** des Buttons.

### Schritt 5: Nachricht gestalten (optional) {#styling}

Sie können die Schriftfarbe und die Akzentfarbe der Nachricht mit dem **Color Theme**-Picker anpassen.

![Tab „Verfassen“ des einfachen Umfrage-Editors mit erweitertem Color-Theme-Picker, nachdem eine Nutzer:in auf die Farbpalette geklickt hat.]({% image_buster /assets/img/iam/color-theme-picker.png %}){: style="max-width:80%"}

## Ergebnisse analysieren {#analytics}

Sobald Ihre Campaign gestartet wurde, können Sie die Ergebnisse in Echtzeit analysieren, um die Aufschlüsselung jeder ausgewählten Option zu sehen. Wenn Sie die [Erfassung angepasster Attribute](#custom-attributes) aktiviert haben, können Sie auch neue Segmente oder Follow-up-Campaigns für Nutzer:innen erstellen, die die Umfrage abgesendet haben.

{% alert note %}
Gelöschte Umfrageoptionen werden weiterhin in Analytics angezeigt, aber neuen Nutzer:innen nicht mehr als Auswahlmöglichkeit präsentiert.
{% endalert %}

Sie finden Ihre Umfrage-Performance-Metriken, indem Sie das Dropdown **Ergebnisse** für eine bestimmte Variante im Abschnitt **In-App Message Performance** der Analytics aufklappen. Hier ist eine Aufschlüsselung dessen, was Sie sehen werden:

- **Umfrage-Engagement** zeigt, wie Nutzer:innen insgesamt mit der Umfrage interagiert haben, einschließlich der Gesamtzahl der Absendungen, Ablehnungen und Klicks innerhalb des Nachrichtentexts.
- **Umfrageergebnisse** zeigen eine Aufschlüsselung, wie viele Nutzer:innen jede Antwortoption ausgewählt haben, zusammen mit dem prozentualen Anteil an den Gesamtabsendungen, den jede Auswahl repräsentiert.
- **Bestätigungsseiten-Metriken** (falls aktiviert) umfassen, wie viele Nutzer:innen den Bestätigungsbildschirm gesehen, seinen Button angeklickt oder ihn ohne Interaktion geschlossen haben.

Definitionen der Umfrage-Metriken finden Sie im [Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/analytics/metrics_glossary). Filtern Sie dort nach „In-App Message“.

Sehen Sie sich den [In-App-Nachrichten-Bericht]({{site.baseurl}}/user_guide/channels/in_app_messages/reporting) für eine Aufschlüsselung Ihrer Campaign-Metriken an.

### Currents {#currents}

Ausgewählte Optionen fließen automatisch in Currents ein, unter dem Feld `button_id` der [**In-App Message Click Events**]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#in-app-message-click-events). Jede Auswahl wird mit ihrem universell eindeutigen Bezeichner (UUID) gesendet.

## Anwendungsfälle {#use-cases}

{% tabs %}
{% tab Kundenzufriedenheit %}

### Kundenzufriedenheit {#user-satisfaction}

**Ziel:** Kundenzufriedenheit messen und Rückgewinnungs-Campaigns an Nutzer:innen senden, die niedrige Bewertungen abgegeben haben.

Um dies einzurichten, verwenden Sie eine Einfachauswahl-Umfrage mit fünf Optionen von „😡 Sehr unzufrieden“ bis „😍 Sehr zufrieden“. Jede Auswahl ist dem angepassten Attribut `customer_satisfaction` zugeordnet, mit einem numerischen Wert von 1 bis 5 – wobei 1 die geringste Zufriedenheit und 5 die höchste Zufriedenheit angibt. Beachten Sie, dass diese numerischen Werte als Strings gespeichert werden, da für die Einfachauswahl angepasste String-Attribute erforderlich sind.

| Auswahl | Attribut | Wert |
|---------|----------|------|
| 😡 Sehr unzufrieden | `customer_satisfaction` | 1 |
| 😟 Unzufrieden | `customer_satisfaction` | 2 |
| 🙂 Weder zufrieden noch unzufrieden | `customer_satisfaction` | 3 |
| 😊 Zufrieden | `customer_satisfaction` | 4 |
| 😍 Sehr zufrieden | `customer_satisfaction` | 5 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Kundenzufriedenheit" }

Wenn eine Nutzer:in die Umfrage absendet, wird der ausgewählte Wert als angepasstes Attribut protokolliert. Sie können dann Follow-up-Campaigns mithilfe von Zielgruppenfiltern erstellen. Senden Sie beispielsweise Rückgewinnungsnachrichten an Nutzer:innen, deren Attribut `customer_satisfaction` den Wert „1“ oder „2“ hat.

{% endtab %}
{% tab Benachrichtigungspräferenzen %}

### Benachrichtigungspräferenzen {#notification-preferences}

**Ziel:** Nutzer:innen die Möglichkeit geben, sich für bestimmte Arten von Benachrichtigungen anzumelden.

Um dies einzurichten, verwenden Sie eine Mehrfachauswahl-Umfrage, bei der jede Auswahl ein Benachrichtigungsthema darstellt. Anstatt dasselbe Attribut mit verschiedenen Werten zuzuweisen, wird jede Auswahl einem eigenen booleschen Attribut zugeordnet, das das Interesse der Nutzer:innen an diesem Thema widerspiegelt. Wenn eine Nutzer:in eine Auswahl trifft, wird das entsprechende Attribut auf `true` gesetzt. Wenn die Auswahl nicht getroffen wird, bleibt das Attribut unverändert.

| Auswahl | Attribut | Wert |
|---------|----------|------|
| Produkt-Updates | `wants_product_updates` | `true` |
| Aktionen | `wants_promotions` | `true` |
| Event-Einladungen | `wants_event_invites` | `true` |
| Umfragen und Feedback | `wants_surveys` | `true` |
| Tipps und Tutorials | `wants_tips` | `true` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Benachrichtigungspräferenzen" }

{% endtab %}
{% tab Kundenziele identifizieren %}

### Kundenziele identifizieren {#identify-customer-goals}

**Ziel:** Die wichtigsten Gründe identifizieren, warum Nutzer:innen Ihre App besuchen.

Um dies einzurichten, verwenden Sie eine Einfachauswahl-Umfrage, bei der jede Option ein häufiges Ziel oder eine Absicht darstellt. Jede Auswahl ist dem angepassten Attribut `product_goal` zugeordnet, mit einem Wert, der der ausgewählten Absicht der Nutzer:innen entspricht.

| Auswahl | Attribut | Wert |
|---------|----------|------|
| Status prüfen | `product_goal` | `status` |
| Mein Konto upgraden | `product_goal` | `upgrade` |
| Einen Termin vereinbaren | `product_goal` | `schedule` |
| Kundensupport | `product_goal` | `support` |
| Nur stöbern | `product_goal` | `browse` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Kundenziele identifizieren" }

Wenn eine Nutzer:in die Umfrage absendet, wird der ausgewählte Wert als angepasstes Attribut in ihrem Profil protokolliert. Sie können diese Daten dann nutzen, um zukünftige Erlebnisse zu personalisieren oder Nutzer:innen basierend auf ihrem primären Ziel zu segmentieren.

{% endtab %}
{% tab Konversionsraten verbessern %}

### Konversionsraten verbessern {#improve-conversion-rates}

**Ziel:** Verstehen, warum Kund:innen nicht upgraden oder kaufen.

Um dies einzurichten, verwenden Sie eine Einfachauswahl-Umfrage, bei der jede Option ein häufiges Hindernis für ein Upgrade darstellt. Jede Auswahl ist dem angepassten Attribut `upgrade_reason` zugeordnet, mit einem entsprechenden Wert, der die Auswahl der Nutzer:innen widerspiegelt.

| Auswahl | Attribut | Wert |
|---------|----------|------|
| Zu teuer | `upgrade_reason` | `expensive` |
| Nicht wertvoll genug | `upgrade_reason` | `value` |
| Schwer zu bedienen | `upgrade_reason` | `difficult` |
| Nutze einen Wettbewerber | `upgrade_reason` | `competitor` |
| Anderer Grund | `upgrade_reason` | `other` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Konversionsraten verbessern" }

Wenn eine Nutzer:in die Umfrage absendet, wird der ausgewählte Wert in ihrem Profil gespeichert. Sie können diese Nutzer:innen dann mit Campaigns ansprechen, die auf ihren spezifischen Einwand zugeschnitten sind, wie z. B. Rabattangebote oder Verbesserungen der Benutzerfreundlichkeit.

{% endtab %}
{% tab Lieblings-Features %}

### Lieblings-Features {#favorite-features}

**Ziel:** Verstehen, welche Features Kund:innen gerne nutzen.

Um dies einzurichten, verwenden Sie eine Mehrfachauswahl-Umfrage, bei der jede Option ein Feature Ihrer App darstellt. Jede Auswahl ist dem angepassten Attribut `favorite_features` zugeordnet, und wenn die Nutzer:in die Umfrage absendet, wird das Attribut auf ein Array der ausgewählten Werte gesetzt.

| Auswahl | Attribut | Wert |
|---------|----------|------|
| Lesezeichen | `favorite_features` | `bookmarks` |
| Mobile App | `favorite_features` | `mobile` |
| Beiträge teilen | `favorite_features` | `sharing` |
| Kundensupport | `favorite_features` | `support` |
| Anpassung | `favorite_features` | `custom` |
| Preis / Wert | `favorite_features` | `value` |
| Community | `favorite_features` | `community` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Lieblings-Features" }

Da diese Umfrage die Mehrfachauswahl verwendet, wird das Profil der Nutzer:innen mit einer Liste aller ausgewählten Feature-Werte aktualisiert.

{% endtab %}
{% endtabs %}