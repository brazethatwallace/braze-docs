---
nav_title: Shopify upgraden (angepasst)
article_title: "Ihre angepasste Shopify-Integration upgraden"
description: "Erfahren Sie, wie Sie Ihre angepasste Shopify-Integration für Braze upgraden."
page_type: partner
search_tag: Partner
permalink: "/shopify_custom_upgrade/"
hidden: true
---

# Ihre Shopify-Integration upgraden (angepasst) {#upgrading-your-shopify-integration-custom}

> Erfahren Sie, wie Sie Ihre Shopify-Integration über den angepassten Pfad für Braze upgraden. Im Rahmen unseres Engagements, Ihnen die bestmögliche Erfahrung zu bieten, verlangen wir, dass alle Shopify-Integrationen bis zum 28. August 2025 auf die neueste Version [upgraden]({{site.baseurl}}/shopify). Dieses Upgrade or upgraden ist unerlässlich, da wesentliche Änderungen in der Shopify-Technologie die Funktionsweise unserer Integration beeinflussen werden.

## Wer ist berechtigt? {#whos-eligible}

Dieser Upgrade or upgraden-Pfad ist für Marken mit einem Shopify-Headless- oder Shopify-Hydrogen-Shop vorgesehen.

{% multi_lang_include partners/shopify_alerts.md alert='breaking' %}

## Upgrade or upgraden-Anforderungen {#upgrade-requirements}

Bevor Sie beginnen, prüfen Sie die folgenden Punkte:

| Anforderung           | Beschreibung |
|-----------------------|-------------|
| **Wichtige Änderungen**  | Stellen Sie sicher, dass Sie alle wichtigen Änderungen vom Legacy-Konnektor zum neuen Konnektor unter [Shopify-Upgrade or upgraden – Übersicht]({{site.baseurl}}/shopify_upgrade_overview#subscriber-collection) geprüft haben. |
| **Upgrade or upgraden-Voraussetzungen** | Stellen Sie sicher, dass Sie alle erforderlichen [Upgrade or upgraden-Voraussetzungen]({{site.baseurl}}/shopify_upgrade_overview#upgrade-prerequisites) mit Ihren Engineering- und Marketing-Teams abgeschlossen haben. Um Ihren Headless-Shopify-Shop mit Braze zu Update or aktualisieren or aktualisieren, müssen Sie zwei wichtige Schritte durchführen:<br><br>- Das Braze Web SDK or Software-Development-Kit initialisieren und laden, um Onsite-Tracking zu aktivieren<br>- Ihren bestehenden Shop über das produktinterne Upgrade or upgraden-Erlebnis Update or aktualisieren or aktualisieren |
| **Breaking Changes**  | Prüfen und beheben Sie alle in Braze markierten Breaking Changes. Eine vollständige Anleitung finden Sie unter [Breaking Changes beheben](#fixing-breaking-changes-fixing-breaking-changes). |
{: .reset-td-br-1 .reset-td-br-2  role="presentation"}

## Breaking Changes beheben {#fixing-breaking-changes}

Gehen Sie in Braze zu **Partnerintegrationen** > **Shopify** und wählen Sie dann **Upgrade or upgraden starten**.

![Panel mit einer Option zum Starten des Upgrades.]({% image_buster /assets/unlisted_docs/img/shopify/start_shopify_custom_upgrade.png %}){: style="max-width:35%;"}

Alle betroffenen Canvase, Campaigns und Segmente, die Shopify-Daten verwenden, werden markiert.

![Ein Modal zur Überprüfung der von Breaking Changes betroffenen Elemente.]({% image_buster /assets/unlisted_docs/img/shopify/review_breaking_changes.png %})

Für die meisten Events empfehlen wir, die neuen erforderlichen Shopify-Events und -Attribute mit einem „ODER“-Operator einzubeziehen, um ein reibungsloses Upgrade or upgraden aktiver Nachrichten zu ermöglichen. Für spezifischere Fälle beachten Sie Folgendes:

{% tabs local %}
{% tab Warenkorb-Abbruch %}
Für Warenkorb-Abbruch-Nachrichten müssen Sie die neuen Warenkorb-Abbruch-Canvas-Templates verwenden, die Folgendes enthalten:

{% multi_lang_include partners/shopify/abandoned_cart_template_features.md %}
{% endtab %}

{% tab Checkout-Abbruch %}
Für Checkout-Abbruch-Nachrichten müssen Sie das neue Checkout-Abbruch-Canvas-Template verwenden, das Folgendes enthält:

{% multi_lang_include partners/shopify/abandoned_checkout_template_features.md %}

Eine vollständige Liste der neuen E-Commerce-Canvas-Templates und vordefinierten HTML-Blöcke für die Produktpersonalisierung, die über die Integration verfügbar sind, finden Sie unter [Ihre Canvas-User-Journeys erstellen]({{site.baseurl}}using_shopify_with_braze#create-your-canvas-user-journeys).

{% alert important %}
Wenn Sie aktive Nachrichten, die eingestellte Events in der Shopify-Integration verwenden, nicht berücksichtigen, werden betroffene Nachrichten nicht mehr an Ihre Kund:innen gesendet.
{% endalert %}

Weitere Informationen finden Sie unter [Unterstützte Shopify-Events]({{site.baseurl}}/shopify_upgrade_overview#supported-shopify-events).
{% endtab %}

{% tab Abonnent:innenlisten %}
Wenn Sie E-Mail- oder Kurzmitteilungsdienst or SMS-Abonnent:innen von Shopify über die Integration erfassen, bestätigen Sie, dass Ihre aktiven Nachrichten die entsprechenden Abonnent:innenlisten für Ihren Shopify-Shop enthalten.

Wenn das Upgrade or upgraden abgeschlossen ist, werden neue Standard-Abo-Gruppen für Ihre Integration erstellt, die Sie als Teil Ihres aktiven Messagings nutzen müssen. Weitere Informationen zu den Änderungen finden Sie unter [Abonnent:innenerfassung]({{site.baseurl}}/shopify_upgrade_overview#subscriber-collection).
{% endtab %}
{% endtabs %}

## Upgrade or upgraden von Shopify {#upgrading-shopify}

{% alert important %}
Es ist wichtig, dass Sie alle [Breaking Changes beheben](#fixing-breaking-changes), bevor Sie mit dem Upgrade or upgraden beginnen.
{% endalert %}

### Schritt 1: Braze Web SDK or Software-Development-Kit initialisieren und laden, um Onsite-Tracking zu aktivieren {#step-1}

Falls noch nicht geschehen, initialisieren und laden Sie das Braze Web SDK or Software-Development-Kit, um Onsite-Tracking zu aktivieren. Eine vollständige Anleitung finden Sie unter [Shopify – benutzerdefinierte Integration einrichten]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration#step-1):
- Eine Braze-Web-App erstellen
- Subdomain und Umgebungsvariablen hinzufügen
- Onsite-Tracking aktivieren
- Ein Shopify-Konto-Anmeldeereignis hinzufügen
- Tracking für „Produkt angesehen“- und „Warenkorb-Aktualisierung“-Ereignisse hinzufügen

### Schritt 2: Upgrade or upgraden starten {#step-2-start-the-upgrade}

Gehen Sie in Braze zu **Partnerintegrationen** > **Shopify** und wählen Sie **Upgrade or upgraden starten**.

![Panel mit einer Option zum Starten des Upgrades.]({% image_buster /assets/unlisted_docs/img/shopify/start_shopify_custom_upgrade.png %}){: style="max-width:35%;"}

Stimmen Sie den Upgrade or upgraden-Richtlinien zu, indem Sie das Kontrollkästchen aktivieren, und wählen Sie dann **Upgrade or upgraden starten**.

![Modal zur Bestätigung, dass Sie verstanden haben, dass das Upgrade or upgraden Breaking Changes verursachen kann.]({% image_buster /assets/unlisted_docs/img/shopify/confirm_upgrade.png %}){: style="max-width:50%;"}

Bestätigen Sie mit Ihren Entwickler:innen, dass Sie Schritt 1 des benutzerdefinierten Upgrade or upgraden-Pfads abgeschlossen haben, indem Sie das Kontrollkästchen aktivieren, und wählen Sie dann **Bestätigen**.

![Modal mit einem Kontrollkästchen zur Bestätigung, dass Sie die Schritte eins bis fünf abgeschlossen haben.]({% image_buster /assets/unlisted_docs/img/shopify/confirm_completed_steps.png %}){: style="max-width:50%;"}

{% alert important %}
Damit die Integration korrekt funktioniert, stellen Sie sicher, dass Sie [Schritt 1](#step-1) des benutzerdefinierten Upgrades abgeschlossen haben. Wenn Sie diesen Schritt überspringen, funktioniert die Integration möglicherweise nicht ordnungsgemäß.
{% endalert %}

### Schritt 3: Die Braze-App erneut autorisieren {#step-3-reauthorize-the-braze-app}

Um die Braze-App erneut zu autorisieren, wählen Sie **Zu Shopify wechseln**.

![Panel mit einer Option, um zu Shopify zu wechseln.]({% image_buster /assets/unlisted_docs/img/shopify/custom_go_to_shopify.png %}){: style="max-width:35%"}

Folgen Sie auf der Shopify-Website den Anweisungen, um Ihre Braze-App erneut zu autorisieren. Dadurch erhält Braze Zugriff auf Ihre Shopify-Daten.

{% alert important %}
Der Prozess der erneuten Autorisierung kann einige Minuten dauern. Er wird jedoch automatisch auf Ihrer Shopify-Seite aktualisiert, sobald er abgeschlossen ist.
{% endalert %}

![Shopify-Upgrade or upgraden-Panel mit einem Ladesymbol neben „Braze-App erneut autorisieren“.]({% image_buster /assets/unlisted_docs/img/shopify/reauthorize_app_loading.png %}){: style="max-width:35%;"}

### Schritt 4: Einen externen ID-Typ wählen {#step-4-choose-an-external-id-type}

Der von Ihnen gewählte externe ID-Typ wird neuen Shopify-Kundenprofilen zugewiesen, wenn ein Shopify-Konto erstellt oder eine Bestellung aufgegeben wird. Er wird auch verwendet, um bestehende Nutzerprofile zu Update or aktualisieren or aktualisieren, wenn diese bereits einen Shopify-Kunden-ID-Alias haben, aber keine externe ID in Braze zugewiesen bekommen haben.

Um Ihren externen ID-Typ zu wählen, kehren Sie zu Braze zurück und wählen Sie **Externe ID bestätigen**.

![Shopify-Upgrade or upgraden-Panel mit einem Button zur Bestätigung der externen ID.]({% image_buster /assets/unlisted_docs/img/shopify/custom_confirm_external_id.png %}){: style="max-width:35%;"}

Wählen Sie die externe ID, die Sie für die Shopify-Integration Ihres Workspace verwenden möchten. Wenn Sie fertig sind, wählen Sie **Externe ID festlegen**.

![Modal mit einem Dropdown zur Auswahl der externen ID.]({% image_buster /assets/unlisted_docs/img/shopify/external_id_custom.png %}){: style="max-width:50%;"}

{% alert important %}
Standardmäßig konvertiert Braze E-Mails von Shopify automatisch in Kleinbuchstaben, bevor sie als externe ID verwendet werden. Wenn Sie E-Mail oder gehashte E-Mail als externe ID verwenden, stellen Sie sicher, dass Ihre E-Mail-Adressen ebenfalls in Kleinbuchstaben konvertiert werden, bevor Sie sie als externe ID zuweisen oder bevor Sie sie aus anderen Datenquellen hashen. Dies hilft, Diskrepanzen bei externen IDs zu vermeiden und die Erstellung doppelter Nutzerprofile in Braze zu verhindern.
{% endalert %}

Wenn Sie einen benutzerdefinierten externen ID-Typ gewählt haben, fahren Sie mit den Schritten 4.1–4.3 fort. Andernfalls fahren Sie mit Schritt 5 fort.

#### Schritt 4.1: Das Metafeld `braze.external_id` erstellen {#step-41-create-the-brazeexternal_id-metafield}

{% multi_lang_include partners/shopify/customer_metafield_definition_steps.md %}

Nachdem das Metafeld erstellt wurde, befüllen Sie es für Ihre Kund:innen. Wir empfehlen die folgenden Ansätze:

- **Auf Webhooks zur Kundenerstellung hören:** Richten Sie einen Webhook ein, der auf [`customer/create`-Ereignisse](https://help.shopify.com/en/manual/fulfillment/setup/notifications/webhooks) lauscht. So können Sie das Metafeld schreiben, wenn ein:e neue:r Kund:in erstellt wird.
- **Bestehende Kund:innen nachträglich befüllen:** Verwenden Sie die [Admin API](https://shopify.dev/docs/api/admin-graphql) oder die [Customer API](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer), um das Metafeld für zuvor erstellte Kund:innen nachträglich zu befüllen.

#### Schritt 4.2: Einen Endpunkt zum Abrufen Ihrer externen ID erstellen {#step-42-create-an-endpoint-to-retrieve-your-external-id}

Sie müssen einen öffentlichen Endpunkt erstellen, den Braze aufrufen kann, um die externe ID abzurufen. Dies ist für Szenarien erforderlich, in denen Shopify das Metafeld `braze.external_id` nicht bereitstellen kann.

##### Endpunkt-Spezifikationen {#endpoint-specifications}

**Methode:** `GET`

| Parameter | Beschreibung |
| --- | --- |
| `shopify_customer_id` | Die Shopify-Kunden-ID. |
| `email_address` | Die E-Mail-Adresse der angemeldeten Nutzer:in. |
| `shopify_storefront` | Die Storefront für die Anfrage. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

##### Beispiel-Endpunkt {#example-endpoint}

```
GET
https://mystore.com/custom_id?shopify_customer_id=1234&email_address=bob@example.com&shopify_storefront=dev-store.myshopify.com
```

##### Erwartete Antwort {#expected-response}

Braze erwartet einen `200`-Statuscode. Jeder andere Code wird als Fehler betrachtet.

{% raw %}
```json
{ "external_id": "my_external_id" }
```
{% endraw %}

{% alert important %}
Es ist wichtig zu überprüfen, dass `shopify_customer_id` und `email_address` mit den Kundenwerten in Shopify übereinstimmen. Sie können die [Admin API](https://shopify.dev/docs/api/admin-graphql) oder die [Customer API](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer) verwenden, um diese Parameter zu validieren und das Metafeld `braze.external_id` abzurufen.
{% endalert %}

#### Schritt 4.3: Ihre externe ID eingeben {#step-43-input-your-external-id}

Wiederholen Sie [Schritt 4](#step-4-choose-an-external-id-type) und geben Sie Ihre Endpunkt-URL ein, nachdem Sie „benutzerdefinierte externe ID“ als Ihren Braze-externen-ID-Typ ausgewählt haben.

##### Hinweise {#considerations}

{% multi_lang_include partners/shopify/external_id_generation_notes.md %}

### Schritt 5: Das Braze-App-Embed aktivieren {#step-5-enable-the-braze-app-embed}

Um das Braze-App-Embed im Theme Ihres Shops zu aktivieren, kehren Sie zu Braze zurück und wählen Sie „Zu Shopify wechseln“.

![Shopify-Upgrade or upgraden-Panel mit einem Button zum Aktivieren des Braze-App-Embeds.]({% image_buster /assets/unlisted_docs/img/shopify/custom_enable_app_embed.png %}){: style="max-width:35%;"}

Aktivieren Sie auf der Shopify-Website das Braze-App-Embed und speichern Sie Ihre Änderungen.

![Ein Beispiel für ein App-Embed.]({% image_buster /assets/unlisted_docs/img/shopify/app_embed.png %})

### Schritt 6: Upgrade or upgraden überprüfen {#step-6-verify-the-upgrade}

Zurück in Braze werden Sie benachrichtigt, wenn die Installation Ihrer Shopify-Integration abgeschlossen ist.

![Shopify-Integrationsseite mit einem Erfolgsbanner.]({% image_buster /assets/unlisted_docs/img/shopify/success_integration.png %})

Um zu überprüfen, ob Ihr neuer Shopify-Konnektor aktiv ist, testen Sie Folgendes:

{% multi_lang_include partners/shopify/upgrade_validation_checklist.md %}

Wenn Sie Fragen haben, [kontaktieren Sie den Support]({{site.baseurl}}/user_guide/administer/personal/braze_support).