---
nav_title: Shopify upgraden
article_title: "Ihre Shopify-Integration upgraden"
description: "Erfahren Sie, wie Sie Ihre Shopify-Integration für Braze upgraden."
page_type: partner
search_tag: Partner
permalink: "/shopify_standard_upgrade/"
hidden: true
---

# Ihre Shopify-Integration upgraden (Standard) {#upgrading-your-shopify-integration-standard}

> Erfahren Sie, wie Sie Ihre Shopify-Integration über den Standardpfad für Braze upgraden. Im Rahmen unseres Engagements, Ihnen die bestmögliche Erfahrung zu bieten, verlangen wir, dass alle Shopify-Integrationen bis zum 28. August 2025 auf die neueste Version [upgraden]({{site.baseurl}}/shopify). Dieses Upgrade or upgraden ist unerlässlich, da wesentliche Änderungen in der Shopify-Technologie die Funktionsweise unserer Integration beeinflussen werden.

## Wer ist berechtigt? {#whos-eligible}

Dieser Upgrade or upgraden-Pfad ist für Marken mit einem Shopify-Onlineshop gedacht.

{% multi_lang_include partners/shopify_alerts.md alert='breaking' %}

## Upgrade or upgraden-Anforderungen {#upgrade-requirements}

Bevor Sie beginnen, überprüfen Sie Folgendes:

- **Kritische Änderungen:** Stellen Sie sicher, dass Sie alle wichtigen Änderungen vom alten Konnektor zum neuen Konnektor unter [Shopify-Upgrade or upgraden – Übersicht]({{site.baseurl}}/shopify_upgrade_overview#subscriber-collection) geprüft haben.
- **Upgrade or upgraden-Voraussetzungen:** Stellen Sie sicher, dass Sie alle erforderlichen [Upgrade or upgraden-Voraussetzungen]({{site.baseurl}}/shopify_upgrade_overview#upgrade-prerequisites) mit Ihren Engineering- und Marketing-Teams abgeschlossen haben.
- **Breaking Changes:** Überprüfen und beheben Sie alle in Braze gemeldeten Breaking Changes. Eine vollständige Anleitung finden Sie unter [Breaking Changes beheben](#fixing-breaking-changes-fixing-breaking-changes).

## Breaking Changes beheben {#fixing-breaking-changes}

Gehen Sie in Braze zu **Partnerintegrationen** > **Shopify** und wählen Sie dann **Upgrade or upgraden starten**.

![Panel mit einer Option zum Starten des Upgrades.]({% image_buster /assets/unlisted_docs/img/shopify/start_shopify_upgrade.png %}){: style="max-width:35%;"}

Alle betroffenen Canvase, Campaigns und Segmente, die Shopify-Daten verwenden, werden markiert.

![Ein Modal zur Überprüfung der von Breaking Changes betroffenen Elemente.]({% image_buster /assets/unlisted_docs/img/shopify/review_breaking_changes.png %})

Für die meisten Events empfehlen wir, die neuen erforderlichen Shopify-Events und -Attribute mit einem „ODER“-Operator einzubeziehen, um ein reibungsloses Upgrade or upgraden aktiver Nachrichten zu ermöglichen. Für spezifischere Fälle beachten Sie Folgendes:

{% tabs local %}
{% tab Warenkorb-Abbruch %}
Für Warenkorb-Abbruch-Nachrichten müssen Sie die neuen Canvas-Templates für Warenkorb-Abbruch verwenden, die Folgendes enthalten:

{% multi_lang_include partners/shopify/abandoned_cart_template_features.md %}
{% endtab %}

{% tab Checkout-Abbruch %}
Für Checkout-Abbruch-Nachrichten müssen Sie das neue Canvas-Template für Checkout-Abbruch verwenden, das Folgendes enthält:

{% multi_lang_include partners/shopify/abandoned_checkout_template_features.md %}

Eine vollständige Liste der neuen E-Commerce-Canvas-Templates und vordefinierten HTML-Blöcke für Produktpersonalisierung, die über die Integration verfügbar sind, finden Sie unter [Erstellen Sie Ihre Canvas-User-Journeys]({{site.baseurl}}using_shopify_with_braze#create-your-canvas-user-journeys).

{% alert important %}
Wenn Sie aktive Nachrichten, die eingestellte Events in der Shopify-Integration verwenden, nicht berücksichtigen, werden betroffene Nachrichten nicht mehr an Ihre Kund:innen gesendet.
{% endalert %}

Weitere Informationen finden Sie unter [Unterstützte Shopify-Events]({{site.baseurl}}/shopify_upgrade_overview#supported-shopify-events).
{% endtab %}

{% tab Abonnent:innenlisten %}
Wenn Sie E-Mail- oder Kurzmitteilungsdienst or SMS-Abonnent:innen über die Integration aus Shopify erfassen, bestätigen Sie, dass Ihre aktiven Nachrichten die entsprechenden Abonnent:innenlisten für Ihren Shopify-Shop enthalten.

Wenn das Upgrade or upgraden abgeschlossen ist, werden neue Standard-Abo-Gruppen für Ihre Integration erstellt, die Sie als Teil Ihres aktiven Messagings nutzen müssen. Weitere Informationen zu den Änderungen finden Sie unter [Abonnent:innenerfassung]({{site.baseurl}}/shopify_upgrade_overview#subscriber-collection).
{% endtab %}
{% endtabs %}

## Upgrade or upgraden von Shopify {#upgrading-shopify}

{% alert important %}
Es ist wichtig, dass Sie alle [Breaking Changes beheben](#fixing-breaking-changes), bevor Sie mit dem Upgrade or upgraden beginnen.
{% endalert %}

### Schritt 1: Das Upgrade or upgraden starten {#step-1-start-the-upgrade}

Gehen Sie in Braze zu **Partnerintegrationen** > **Shopify** und wählen Sie dann **Start Upgrade or upgraden** aus.

![Panel mit der Option, das Upgrade or upgraden zu starten.]({% image_buster /assets/unlisted_docs/img/shopify/start_shopify_upgrade.png %}){: style="max-width:35%;"}

Stimmen Sie den Geschäftsbedingungen zu, indem Sie das Kontrollkästchen aktivieren, und wählen Sie dann **Start the Upgrade or upgraden** aus.

![Modal zur Bestätigung, dass Sie verstehen, dass das Upgrade or upgraden Breaking Changes verursachen kann.]({% image_buster /assets/unlisted_docs/img/shopify/confirm_upgrade.png %})

### Schritt 2: Braze SDKs einrichten {#step-2-set-up-the-braze-sdks}

Die Standardintegration fügt die Braze SDKs automatisch zu Ihrer Shopify-Website hinzu. Wenn Sie die Braze SDKs bereits direkt integriert oder ein Drittanbieter-Tool dafür verwendet haben, koordinieren Sie sich mit Ihren Entwickler:innen, um die vorherige SDK or Software-Development-Kit-Implementierung während des Upgrades zu entfernen.

![Modal, das bestätigt, dass die neue Integration automatisch das Braze und JavaScript SDK or Software-Development-Kit in Ihrem Shop implementiert.]({% image_buster /assets/unlisted_docs/img/shopify/confirm_integration.png %}){: style="max-width:70%;"}

### Schritt 3: Die Braze-App erneut autorisieren {#step-3-reauthorize-the-braze-app}

Um die Braze-App erneut zu autorisieren, wählen Sie **Go to Shopify** aus.

![Shopify-Upgrade or upgraden-Panel mit einem Button, um zu Shopify zu wechseln und die Braze-App erneut zu autorisieren.]({% image_buster /assets/unlisted_docs/img/shopify/reauthorize_braze_app.png %}){: style="max-width:35%;"}

Folgen Sie auf der Shopify-Website den Anweisungen, um Ihre Braze-App erneut zu autorisieren. Dadurch kann Braze auf Ihre Shopify-Daten zugreifen.

{% alert note %}
Der erneute Autorisierungsprozess kann einige Minuten dauern, wird aber automatisch auf Ihrer Shopify-Seite aktualisiert, sobald er abgeschlossen ist.
{% endalert %}

![Die Seite „Integration Settings“ mit dem Status der Shopify-Ereignisse.]({% image_buster /assets/unlisted_docs/img/shopify/reauthorization_status.png %})

### Schritt 4: Einen externen ID-Typ auswählen {#step-4-choose-an-external-id-type}

Der von Ihnen gewählte externe ID-Typ wird neuen Shopify-Kundenprofilen zugewiesen, wenn entweder ein Shopify-Konto erstellt oder eine Bestellung aufgegeben wird. Er wird auch verwendet, um vorhandene Nutzerprofile zu Update or aktualisieren or aktualisieren, wenn diese bereits ein Shopify-Kunden-ID-Alias haben, aber noch keine externe ID in Braze zugewiesen bekommen haben.

Um Ihren externen ID-Typ auszuwählen, gehen Sie zurück zu Braze und wählen Sie dann **Confirm external ID** aus.

![Shopify-Upgrade or upgraden-Panel mit einem Button zur Bestätigung der externen ID.]({% image_buster /assets/unlisted_docs/img/shopify/confirm_external_id.png %}){: style="max-width:35%;"}

Wählen Sie die externe ID aus, die Sie für die Shopify-Integration Ihres Workspace verwenden möchten. Wenn Sie fertig sind, wählen Sie **Set external ID** aus.

![Modal mit einem Dropdown zur Auswahl der externen ID.]({% image_buster /assets/unlisted_docs/img/shopify/external_id_field.png %}){: style="max-width:70%;"}

{% alert important %}
Die Verwendung einer E-Mail-Adresse oder einer gehashten E-Mail-Adresse als Ihre externe Braze-ID kann das Identitätsmanagement über Ihre Datenquellen hinweg vereinfachen. Es ist jedoch wichtig, die potenziellen Risiken für die Privatsphäre der Nutzer:innen und die Datensicherheit zu berücksichtigen.<br><br>

- **Erratbare Informationen:** E-Mail-Adressen sind leicht zu erraten, was sie anfällig für Angriffe macht.
- **Missbrauchsrisiko:** Wenn eine böswillige Person ihren Webbrowser so manipuliert, dass die E-Mail-Adresse einer anderen Person als externe ID gesendet wird, könnte sie potenziell auf vertrauliche Nachrichten oder Kontoinformationen zugreifen.
{% endalert %}

Standardmäßig wandelt Braze E-Mails von Shopify automatisch in Kleinbuchstaben um, bevor sie als externe ID verwendet werden. Wenn Sie E-Mail oder gehashte E-Mail als Ihre externe ID verwenden, stellen Sie sicher, dass Ihre E-Mail-Adressen ebenfalls in Kleinbuchstaben umgewandelt werden, bevor Sie sie als externe ID zuweisen oder bevor Sie sie aus anderen Datenquellen hashen. Dies hilft, Abweichungen bei externen IDs zu vermeiden und das Erstellen doppelter Nutzerprofile in Braze zu verhindern.

Wenn Sie einen angepassten externen ID-Typ ausgewählt haben, fahren Sie mit den Schritten 4.1–4.3 fort. Andernfalls fahren Sie mit Schritt 5 fort.

#### Schritt 4.1: Das Metafeld `braze.external_id` erstellen {#step-41-create-the-brazeexternal_id-metafield}

{% multi_lang_include partners/shopify/customer_metafield_definition_steps.md %}

Nachdem das Metafeld erstellt wurde, befüllen Sie es für Ihre Kund:innen. Wir empfehlen die folgenden Ansätze:

- **Auf Webhooks zur Kundenerstellung lauschen:** Richten Sie einen Webhook ein, um auf [`customer/create`-Ereignisse](https://help.shopify.com/en/manual/fulfillment/setup/notifications/webhooks) zu lauschen. So können Sie das Metafeld schreiben, wenn eine neue Kundin oder ein neuer Kunde erstellt wird.
- **Bestehende Kund:innen nachträglich befüllen:** Verwenden Sie die [Admin-API](https://shopify.dev/docs/api/admin-graphql) oder die [Customer-API](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer), um das Metafeld für zuvor erstellte Kund:innen nachträglich zu befüllen.

#### Schritt 4.2: Einen Endpunkt zum Abrufen Ihrer externen ID erstellen {#step-42-create-an-endpoint-to-retrieve-your-external-id}

Sie müssen einen öffentlichen Endpunkt erstellen, den Braze aufrufen kann, um die externe ID abzurufen. Dies ist für Szenarien erforderlich, in denen Shopify das Metafeld `braze.external_id` nicht bereitstellen kann.

##### Endpunktspezifikationen {#endpoint-specifications}

**Methode:** `GET`

| Parameter | Beschreibung |
| --- | --- |
| `shopify_customer_id` | Die Shopify-Kunden-ID. |
| `email_address` | Die E-Mail-Adresse der angemeldeten Nutzerin oder des angemeldeten Nutzers. |
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
{
    "external_id": "my_external_id"
}
```
{% endraw %}

{% alert important %}
Es ist wichtig zu überprüfen, dass `shopify_customer_id` und `email_address` mit den Kundenwerten in Shopify übereinstimmen. Sie können die [Admin-API](https://shopify.dev/docs/api/admin-graphql) oder die [Customer-API](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer) verwenden, um diese Parameter zu validieren und das Metafeld `braze.external_id` abzurufen.
{% endalert %}

#### Schritt 4.3: Ihre externe ID eingeben {#step-43-input-your-external-id}

Wiederholen Sie [Schritt 4](#step-4-choose-an-external-id-type) und geben Sie Ihre Endpunkt-URL ein, nachdem Sie die angepasste externe ID als Ihren externen Braze-ID-Typ ausgewählt haben.

##### Überlegungen {#considerations}

{% multi_lang_include partners/shopify/external_id_generation_notes.md %}

### Schritt 5: Das Braze-App-Embed aktivieren {#step-5-enable-the-braze-app-embed}

Um das Braze-App-Embed im Theme Ihres Shops zu aktivieren, gehen Sie zurück zu Braze und wählen Sie dann **Go to Shopify** aus.

![Shopify-Upgrade or upgraden-Panel mit einem Button zum Aktivieren des Braze-App-Embeds.]({% image_buster /assets/unlisted_docs/img/shopify/enable_app_embed.png %}){: style="max-width:35%;"}

Aktivieren Sie auf der Shopify-Website das Braze-App-Embed und speichern Sie dann Ihre Änderungen.

![Ein Beispiel für ein App-Embed.]({% image_buster /assets/unlisted_docs/img/shopify/app_embed.png %})

### Schritt 6: Das Upgrade or upgraden überprüfen {#step-6-verify-the-upgrade}

Zurück in Braze werden Sie benachrichtigt, wenn die Installation Ihrer Shopify-Integration abgeschlossen ist.

![Shopify-Integrationsseite mit einem Erfolgsbanner.]({% image_buster /assets/unlisted_docs/img/shopify/success_integration.png %})

Um zu überprüfen, ob Ihr neuer Shopify-Konnektor aktiv ist, testen Sie Folgendes:

{% multi_lang_include partners/shopify/upgrade_validation_checklist.md %}

Wenn Sie Fragen haben, [kontaktieren Sie den Support]({{site.baseurl}}/user_guide/administer/personal/braze_support).