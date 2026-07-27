---
nav_title: Shopify Standard-Integration einrichten
article_title: Shopify Standard-Integration einrichten
description: "In diesem Referenzartikel erfahren Sie, wie Sie die Standard-Shopify-Integration einrichten."
page_type: partner
search_tag: Partner
alias: /shopify_standard_integration/
page_order: 1
---

# Shopify Standard-Integration einrichten {#shopify-standard-integration-setup}

> Auf dieser Seite erfahren Sie, wie Sie Braze mithilfe unserer Standardintegration für Nutzer:innen mit einem Shopify-Onlineshop in Shopify integrieren können. Wenn Sie eine Shopify-Headless-Website verwenden oder weitere angepasste Lösungen implementieren möchten, lesen Sie bitte den Abschnitt [Einrichtung der angepassten Integration in Shopify]({{site.baseurl}}/shopify_custom_integration).

## 1. Schritt: Verbinden Sie Ihren Shopify-Shop {#step-1-connect-your-shopify-store}

1. Gehen Sie in Braze zu **Partnerintegrationen** > **Technologie-Partner** und suchen Sie dann nach „Shopify“.
2. Wählen Sie auf der Shopify-Partnerseite **Begin setup**, um die Integration zu starten.<br><br>![Shopify-Integrationsseite mit Button, um mit der Einrichtung zu beginnen.]({% image_buster /assets/img/shopify/begin_setup.png %})<br><br>
3. Installieren Sie im Shopify App Store die Braze-Anwendung.<br><br>![Die Braze-App-Store-Seite mit einem Button zur Installation der Anwendung.]({% image_buster /assets/img/shopify/shopify_log_in.png %}){: style="max-width:70%;"}

{% alert note %}
Wenn Ihr Shopify-Konto mit mehr als einem Shop verbunden ist, können Sie den Shop, bei dem Sie angemeldet sind, ändern, indem Sie das Shop-Symbol in der Kopfzeile auswählen und **Switch stores** wählen.
{% endalert %}

{: start="4"}
4. Nach der Installation der Braze-App werden Sie zu Braze weitergeleitet, um den Workspace zu bestätigen, den Sie mit Shopify verbinden möchten. Ein Shopify-Shop kann nur mit einem Workspace verbunden werden. Wenn Sie wechseln müssen, wählen Sie den richtigen Workspace aus.<br><br>![Ein Fenster, das Sie auffordert zu bestätigen, dass Sie sich im richtigen Workspace befinden.]({% image_buster /assets/img/shopify/confirm_workspace1.png %}){: style="max-width:70%;"}

{: start="5"}
5. Wählen Sie **Begin setup**.<br><br>![„Integrationseinstellungen“ mit einem Feld zur Eingabe der Domain und einem Button zum Starten der Einrichtung.]({% image_buster /assets/img/shopify/choose_account.png %})

## 2. Schritt: Braze Web SDKs aktivieren {#step-2-enable-braze-web-sdks}

Für Shopify-Onlineshops können Sie das Standard-Setup auswählen, um das Braze Web SDK und das JavaScript SDK automatisch zu implementieren.

![Schritt „Web SDK aktivieren“ mit Optionen zur Implementierung über eine Standardeinrichtung oder eine angepasste Einrichtung.]({% image_buster /assets/img/shopify/sdk_setup.png %})

Nachdem Sie den Standard-Onboarding-Pfad ausgewählt haben, müssen Sie aus einer der folgenden Optionen auswählen, wann Braze die SDKs initialisieren und laden soll:
- Beim Seitenbesuch, z. B. zu Beginn der Sitzung
    - Tracking von identifizierten und anonymen Nutzer:innen
- Bei der Kontoanmeldung, z. B. beim Account-Login
    - Nur identifizierte Nutzer:innen tracken
    - Startet das Tracking von Daten, wenn sich Besucher:innen der Website registrieren oder bei ihren Konten anmelden

## 3. Schritt: Konfigurieren Sie Ihre Shopify-Daten {#step-3-configure-your-shopify-data}

### Standard-Dateneinrichtung {#standard-data-setup}

{% multi_lang_include alerts/important_alerts.md alert='Shopify cart token alias' %}

Jetzt wählen Sie die Shopify-Daten aus, die Sie tracken möchten.

![Abschnitt „Tracking von Shopify-Daten“ mit einem Kontrollkästchen zum Tracking von Verhaltens-Events und Nutzerattributen.]({% image_buster /assets/img/shopify/tracking_shopify_data.png %})

Die folgenden Events werden in der Standardintegration standardmäßig aktiviert.

| Von Braze empfohlene Events | Angepasste Shopify-Events | Angepasste Shopify-Attribute |
| --- | --- | --- |
| {::nomarkdown}<ul><li>Produkt angesehen</li><li>Warenkorb aktualisiert</li><li>Checkout gestartet</li><li>Bestellung aufgegeben</li></ul>{:/}  | {::nomarkdown}<ul><li>shopify_account_login</li><li>shopify_paid_order</li><li>shopify_order_canceled</li><li>shopify_order_refunded</li><li>shopify_order_fulfilled</li><li>shopify_order_partially_fulfilled</li></ul>{:/} | {::nomarkdown}<ul><li>shopify_tags</li><li>shopify_total_spent</li><li>shopify_order_count</li><li>shopify_last_order_id</li><li>shopify_last_order_name</li><li>shopify_zipcode</li><li>shopify_province</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2  .reset-td-br-3 aria-label="Standard-Dateneinrichtung" }

Weitere Informationen zu den Daten, die durch die Integration getrackt werden, finden Sie unter [Shopify-Daten-Features]({{site.baseurl}}/shopify_data_features).

{% multi_lang_include alerts/important_alerts.md alert='Shopify customer create' %}

### Historisches Backfill einrichten {#historical-backfill-setup}

Wählen Sie im Schritt **Track Shopify data** das Kontrollkästchen aus, um den anfänglichen historischen Datenimport als Teil Ihrer Integration einzuschließen.

Informationen zu den importierten Daten, zum Verhalten der Umsatzberichterstattung, zu Screenshots der Einrichtung und zur Vorgehensweise, wenn Sie Braze bereits mit aktiven Campaigns oder Canvases nutzen, finden Sie unter [Historisches Backfill]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features#historical-backfill).

### (Fortgeschritten) Angepasstes Daten-Tracking einrichten {#advanced-custom-data-tracking-setup}

Mit den Braze SDKs können Sie angepasste Events oder angepasste Attribute tracken, die über die Standard-Events für diese Integration hinausgehen. Angepasste Events erfassen einzigartige Interaktionen in Ihrem Shop, wie zum Beispiel:

<style>
#custom-data td {
    word-break: break-word;
    width: 50%;
}
</style>

<table aria-label="(Fortgeschritten) Angepasstes Daten-Tracking einrichten" style="width: 100%;">
  <caption>(Fortgeschritten) Angepasstes Daten-Tracking einrichten</caption>
  <thead>
    <tr>
      <th style="width: 50%;">Angepasste Events</th>
      <th style="width: 50%;">Angepasste Attribute</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <ul>
          <li>Einen angepassten Rabattcode verwenden</li>
          <li>Mit einer personalisierten Produktempfehlung interagieren</li>
          <li>Der Bestellung eine Geschenkbotschaft beifügen</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>Bevorzugte Marken oder Produkte</li>
          <li>Bevorzugte Einkaufskategorien</li>
          <li>Mitgliedschafts- oder Treuestatus</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

Das Tracking angepasster Daten bietet tiefere Insights in das Nutzerverhalten und unterstützt eine zusätzliche Personalisierung. Um angepasste Events zu implementieren, müssen Sie [den Theme-Code Ihres Storefronts](https://help.shopify.com/en/manual/online-store/themes/theme-structure/extend/edit-theme-code) in der Datei `theme.liquid` bearbeiten. Möglicherweise benötigen Sie die Hilfe Ihrer Entwickler:innen.

Das folgende JavaScript-Snippet prüft zum Beispiel, ob die aktuelle Nutzer:in einen Newsletter abonniert hat, und protokolliert dies als angepasstes Event im Nutzerprofil in Braze:

```javascript
braze.logCustomEvent(
  “subscribed_to_newsletter”,
  {
    newsletterName: ‘News and Offers’,
    customerEmail: ‘customer_1@example.com’,
    sendOffers: true
  }
);

```

Das SDK muss auf dem Gerät der Nutzer:in initialisiert sein (auf Aktivitäten lauschen), um Events oder angepasste Attribute zu protokollieren. Mehr über die Protokollierung angepasster Daten erfahren Sie unter [User object](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html) und [logCustomEvent object](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent).

## 4. Schritt: Konfigurieren Sie die Nutzerverwaltung {#step-4}

Wählen Sie Ihren `external_id`-Typ aus der Dropdown-Liste aus.

![Abschnitt „Abonnent:innen sammeln“.]({% image_buster /assets/img/shopify/external_id_standard.png %})

{% alert important %}
Die Verwendung einer E-Mail-Adresse oder einer gehashten E-Mail-Adresse als externe Braze-ID kann die Identitätsverwaltung über Ihre Datenquellen hinweg vereinfachen. Es ist jedoch wichtig, die potenziellen Risiken für den Datenschutz und die Datensicherheit der Nutzer:innen zu berücksichtigen.<br><br>

- **Erratbare Informationen:** E-Mail-Adressen sind leicht zu erraten, was sie anfällig für Angriffe macht.
- **Missbrauchsrisiko:** Wenn eine böswillige Person ihren Webbrowser so manipuliert, dass die E-Mail-Adresse einer anderen Person als externe ID gesendet wird, kann sie möglicherweise auf sensible Nachrichten oder Kontoinformationen zugreifen.
{% endalert %}

Standardmäßig wandelt Braze E-Mails von Shopify automatisch in Kleinbuchstaben um, bevor sie als externe ID verwendet werden. Wenn Sie E-Mail oder gehashte E-Mail als externe ID verwenden, vergewissern Sie sich, dass Ihre E-Mail-Adressen ebenfalls in Kleinbuchstaben umgewandelt werden, bevor Sie sie als externe ID zuweisen oder bevor Sie sie aus anderen Datenquellen hashen. Dies hilft, Diskrepanzen bei externen IDs zu vermeiden und die Erstellung doppelter Nutzerprofile in Braze zu verhindern.

{% alert note %}
Die nächsten Schritte hängen davon ab, welche externe ID Sie ausgewählt haben:<br><br>
- **Wenn Sie einen angepassten externen ID-Typ ausgewählt haben:** Führen Sie die Schritte 4.1–4.3 aus, um Ihre angepasste externe ID-Konfiguration einzurichten.
- **Wenn Sie Shopify-Kund:innen-ID, E-Mail oder gehashte E-Mail ausgewählt haben:** Überspringen Sie die Schritte 4.1–4.3 und fahren Sie direkt mit Schritt 4.4 fort.
{% endalert %}

### Schritt 4.1: Erstellen Sie das Metafeld `braze.external_id` {#step-41-create-the-brazeexternal_id-metafield}

1. Gehen Sie in Ihrem Shopify-Admin-Panel zu **Settings** > **Metafields and metaobjects**.
2. Wählen Sie **Customers** > **Add definition**.
3. Geben Sie für **Name** `braze.external_id` ein.
4. Wählen Sie den automatisch generierten Namespace und Schlüssel (`custom.braze_external_id`) aus, um ihn zu bearbeiten und in `braze.external_id` zu ändern.
5. Wählen Sie unter **Type** den **ID Type** aus.

Nachdem Sie das Metafeld erstellt haben, füllen Sie es für Ihre Kund:innen aus. Wir empfehlen die folgenden Ansätze:

- **Auf Webhooks zur Kund:innen-Erstellung lauschen:** Richten Sie einen Webhook ein, um auf [`customer/create`-Events](https://help.shopify.com/en/manual/fulfillment/setup/notifications/webhooks) zu lauschen. Damit können Sie das Metafeld schreiben, wenn eine neue Kund:in angelegt wird.
- **Bestehende Kund:innen nachfüllen:** Verwenden Sie die [Admin API](https://shopify.dev/docs/api/admin-graphql) oder die [Customer API](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer), um das Metafeld für zuvor erstellte Kund:innen zu füllen.

#### Mögliche Race-Condition {#potential-race-condition}

Der Shopify-Webhook `customers/create` kann ausgelöst werden, bevor das Metafeld `braze.external_id` in das Nutzerprofil geschrieben wurde. In diesem Fall:

1. Wenn das Metafeld fehlt, ruft Braze den konfigurierten Endpunkt ([Schritt 4.2](#step-42-create-an-endpoint-to-retrieve-your-external-id)) auf, um die externe ID abzurufen.
2. Wenn auch dieser Aufruf fehlschlägt oder ein Timeout auftritt, erstellt Braze ein temporäres Nutzerprofil mit der Shopify-Kund:innen-ID als externe ID.
3. Bei jedem nachfolgenden Event, bei dem das Metafeld vorhanden ist (z. B. `customers/update` oder `orders/create` für ein `ecommerce.order_placed`-Event), erkennt Braze automatisch die Abweichung und führt das temporäre Profil mit der korrekten externen ID zusammen.

Das bedeutet, dass temporäre doppelte Profile möglich sind, sich aber automatisch korrigieren. Sie müssen keine manuellen Maßnahmen ergreifen, um diese Profile zusammenzuführen.

### Schritt 4.2: Erstellen Sie einen Endpunkt zum Abrufen Ihrer externen ID {#step-42-create-an-endpoint-to-retrieve-your-external-id}

Sie müssen einen öffentlichen Endpunkt erstellen, den Braze zum Abrufen der externen ID aufrufen kann. Dadurch kann Braze die ID in Szenarien abrufen, in denen Shopify das Metafeld `braze.external_id` nicht direkt bereitstellen kann.

#### Endpunkt-Spezifikationen {#endpoint-specifications}

**Methode:** GET

Braze sendet die folgenden Parameter an Ihren Endpunkt:

| Parameter | Erforderlich | Datentyp | Beschreibung |
|----------------------|----------|-----------|------------------------------------------------------------------|
| shopify_customer_id  | Ja      | String    | Die Shopify-Kund:innen-ID.                                         |
| shopify_storefront   | Ja      | String    | Der Storefront-Name für die Anfrage. Bsp.: `<storefront_name>.myshopify.com` |
| email_address        | Nein       | String    | Die E-Mail-Adresse der angemeldeten Nutzer:in. <br><br>Dieses Feld kann in bestimmten Webhook-Szenarien fehlen. Ihre Endpunkt-Logik sollte hier Nullwerte berücksichtigen (z. B. die E-Mail über die shopify_customer_id abrufen, wenn Ihre interne Logik dies erfordert). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Endpunkt-Spezifikationen" }

#### Beispiel-Endpunkt {#example-endpoint}

```http
GET https://mystore.com/custom_id?shopify_customer_id=1234&email_address=bob@example.com&shopify_storefront=dev-store.myshopify.com
```

#### Erwartete Antwort {#expected-response}
Braze erwartet einen `200`-Statuscode, der die externe ID als JSON zurückgibt:
```json
{
  "external_id": "my_external_id"
}
```

#### Validierung {#validation}
Es ist wichtig, dass Sie überprüfen, ob `shopify_customer_id` und `email_address` (falls vorhanden) mit den Kund:innen-Werten in Shopify übereinstimmen. Sie können die [Shopify Admin API](https://shopify.dev/docs/api/admin-graphql) oder die [Customer API](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer) verwenden, um diese Parameter zu validieren und das richtige `braze.external_id`-Metafeld abzurufen.

#### Fehlerverhalten und Zusammenführung {#failure-behavior-and-merging}
Jeder andere Statuscode als `200` wird als Fehler betrachtet.

{% multi_lang_include partners/shopify/external_id_merge_implications.md %}

### Schritt 4.3: Geben Sie Ihre externe ID ein {#step-43-input-your-external-id}

Wiederholen Sie [Schritt 4](#step-4) und geben Sie Ihre Endpunkt-URL ein, nachdem Sie die angepasste externe ID als Ihren externen Braze-ID-Typ ausgewählt haben.

#### Überlegungen {#considerations}

{% multi_lang_include partners/shopify/external_id_generation_notes.md %}

### Schritt 4.4: Sammeln Sie Ihre E-Mail- oder SMS-Opt-ins von Shopify (optional) {#step-44-collect-your-email-or-sms-opt-ins-from-shopify-optional}

Sie haben die Möglichkeit, Ihre Opt-ins für E-Mail- oder SMS-Marketing von Shopify zu sammeln.

Wenn Sie die Kanäle E-Mail oder SMS nutzen, können Sie Ihre Opt-in-Status für E-Mail- und SMS-Marketing mit Braze synchronisieren. Wenn Sie Opt-ins für das E-Mail-Marketing von Shopify synchronisieren, erstellt Braze automatisch eine E-Mail-Abo-Gruppe für alle Nutzer:innen, die mit diesem Shop verbunden sind. Sie müssen einen eindeutigen Namen für diese Abo-Gruppe erstellen.

![Abschnitt „Abonnent:innen sammeln“ mit der Option, Opt-ins für E-Mail- oder SMS-Marketing zu sammeln.]({% image_buster /assets/img/shopify/collect_email_subscribers.png %})

{% multi_lang_include partners/shopify/third_party_capture_form_note.md %}

## 5. Schritt: Produkte synchronisieren (optional) {#step-5-sync-products-optional}

Sie können alle Produkte aus Ihrem Shopify-Shop mit einem Braze-Katalog synchronisieren, um die Personalisierung von Nachrichten zu vertiefen. Automatische Updates erfolgen nahezu in Realtime, sodass Ihr Katalog stets aktuelle Produktdaten enthält. Mehr dazu erfahren Sie unter [Shopify-Produktsynchronisation]({{site.baseurl}}/partners/ecommerce/shopify/shopify_catalogs).

![Schritt 4 der Einrichtung mit „Shopify Variant ID“ als „Bezeichner für das Produkt im Katalog“.]({% image_buster /assets/img/shopify/sync_products_step1.png %}){: style="max-width:80%;"}

## 6. Schritt: Kanäle aktivieren (optional) {#step-6-activate-channels-optional}

Sie können In-App-Nachrichten ohne Entwickler:in aktivieren, indem Sie sie in Ihrem Setup konfigurieren.

![Einrichtungsschritt zur Aktivierung von Kanälen, wobei die verfügbare Option In-Browser-Messaging ist.]({% image_buster /assets/img/shopify/activate_channels_standard.png %})

{% alert note %}
Braze sammelt über In-Browser-Nachrichten Informationen über Besucher:innen, wie z. B. E-Mail-Adressen und Telefonnummern. Diese Informationen werden an Shopify gesendet. Diese Daten ermöglichen es Händlern, Besucher:innen ihres Shops zu erkennen und ein personalisiertes Einkaufserlebnis zu schaffen. Weitere Einzelheiten finden Sie unter [Visitor API](https://shopify.dev/docs/api/web-pixels-api/emitting-data#visitor-api).
{% endalert %}

### Unterstützung für zusätzliche SDK-Kanäle {#supporting-additional-sdk-channels}

Die Braze SDKs ermöglichen verschiedene Messaging-Kanäle, einschließlich Content Cards.

#### Content Cards und Feature-Flags {#content-cards-and-feature-flags}

Um Content Cards oder Feature-Flags hinzuzufügen, müssen Sie mit Ihren Entwickler:innen zusammenarbeiten, um den erforderlichen SDK-Code direkt in Ihre `theme.liquid`-Datei einzufügen. Eine ausführliche Anleitung finden Sie unter [Integration des Braze SDK]({{site.baseurl}}/developer_guide/sdk_integration).

#### Web-Push-Benachrichtigungen {#web-push-notifications}

Web-Push wird für die Shopify-Integration derzeit nicht unterstützt. {% multi_lang_include product_feedback_cta.md context="gap" feature="web push for the Shopify integration" %}

## 7. Schritt: Einrichtung abschließen {#step-7-finish-setup}

1. Nachdem Sie Ihre Einrichtung konfiguriert haben, wählen Sie **Finish Setup**.
2. Aktivieren Sie die Braze-App-Einbettung in Ihren Shopify-Themeneinstellungen. Wählen Sie **Open Shopify**, um zu Ihrem Shopify-Konto weitergeleitet zu werden und die App-Einbettung in den Themeneinstellungen Ihres Shops zu aktivieren.

![Ein Banner, das darauf hinweist, dass Sie die Braze-App-Einbettung in Shopify aktivieren müssen, und einen Button zum Öffnen von Shopify enthält.]({% image_buster /assets/img/shopify/open_shopify.png %})

{: start="3"}
3. Nachdem Sie die App-Einbettung aktiviert haben, ist Ihre Einrichtung abgeschlossen!
Bestätigen Sie, dass Sie Ihre Integrationseinstellungen, den Status der ersten Datensynchronisation und Ihre aktiven Shopify-Events einsehen können. <br><br>![Shopify-Partnerseite mit den Integrationseinstellungen.]({% image_buster /assets/img/shopify/install_complete.png %})