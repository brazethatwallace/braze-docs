{% tabs %}
{% tab Abandoned browse %}

### Abgebrochenes Stöbern {#abandoned-browse}

Verwenden Sie das Template **Abandoned browse**, um Nutzer:innen anzusprechen, die sich Produkte angesehen, aber weder in den Warenkorb gelegt noch eine Bestellung aufgegeben haben.

![Ein angewandtes „Abandoned Browse“ Canvas-Template mit erweiterten „Entry Rules“.]({% image_buster /assets/img_archive/abandoned_browse.png %})

#### Einrichtung {#setup}

Wählen Sie auf der Canvas-Seite **Use a Canvas Template** > **Braze templates** und wenden Sie dann das Template **Abandoned browse** an.

##### Standardeinstellungen {#default-settings}

Die folgenden Einstellungen sind in Ihrem Canvas vorkonfiguriert:
- Grundlagen
    - Canvas-Name: **Abandoned browse**
    - Konversions-Event: `ecommerce.order placed`
        - Conversion-Frist: 3 Tage
- Entry-Zeitplan
    - Aktionsbasiert, wenn ein:e Nutzer:in das Event `ecommerce.product_viewed` ausführt
    - Startzeit ist der Zeitpunkt, an dem Sie das Canvas-Template erstellen<br><br>![„Action Based Options“ für das Canvas.]({% image_buster /assets/img/ecommerce/abandoned_browse_entry.png %})<br><br>
- Zielgruppe
    - Entry-Zielgruppe
        - E-Mail **ist nicht leer**
        - Sie können die Kriterien für die Entry-Zielgruppe auch an Ihre geschäftlichen Anforderungen anpassen
    - Eingangskontrollen
        - Nutzer:innen können diesen Canvas erneut betreten, nachdem die gesamte Dauer des Canvas abgelaufen ist
    - Ausstiegskriterien
        - Führt `ecommerce.cart_updated`, `ecommerce.checkout_started` oder `ecommerce.order_placed` aus<br><br>![Eingangskontrollen und Ausstiegskriterien für das Canvas.]({% image_buster /assets/img/ecommerce/abandoned_browse_entry_exit.png %})<br><br>
- Sendeeinstellungen
    - Nutzer:innen, die abonniert oder per Opt-in angemeldet sind
- Verzögerungsschritt
    - 1 Stunde Verzögerung
- Nachrichtenschritt
    - Überprüfen Sie das E-Mail-Template und den HTML-Block mit einem Liquid-Templating-Beispiel, um Produkte zu Ihrer Nachricht im vorgefertigten Template hinzuzufügen. Wenn Sie Ihr eigenes E-Mail-Template verwenden, können Sie auch [Liquid-Variablen](#message-personalization) referenzieren, wie im folgenden Abschnitt gezeigt.

#### Produktpersonalisierung für E-Mails bei abgebrochenem Stöbern {#abandoned-browse-product-personalization-for-emails}

Hier sehen Sie ein Beispiel, wie Sie einen HTML-Produktblock für Ihre E-Mail bei abgebrochenem Stöbern hinzufügen.

{% raw %}
```java
<table aria-label="Abandoned browse product personalization for emails" style="width:100%">
  <tr>
    <th><img src="{{context.${image_url}}}" width="200" height="200"><img></th>
    <th align="left">
      <ul style="list-style-type: none">
        <li>Item: {{context.${product_name}}}</li>
        <li>Price: ${{context.${price}}}</li>
      </ul>
    </th>
  </tr>
</table>
```
{% endraw %}

##### Produkt-URL {#product-url}

{% raw %}
```liquid
{{context.${product_url}}}
```
{% endraw %}

{% endtab %}
{% tab Abandoned cart %}

### Warenkorb-Abbruch {#abandoned-cart}

Verwenden Sie das Template **Abandoned cart**, um potenzielle entgangene Umsätze von Kund:innen abzufangen, die Produkte in ihren Warenkorb gelegt, aber weder zur Kasse gegangen sind noch eine Bestellung aufgegeben haben.

![Ein angewandtes „Abandoned Cart“ Canvas-Template mit erweiterten „Entry Rules“.]({% image_buster /assets/img_archive/abandoned_cart.png %})

#### Einrichtung

Wählen Sie auf der Canvas-Seite **Use a Canvas Template** > **Braze templates** und wenden Sie dann das Template **Abandoned cart** an.

##### Standardeinstellungen

Die folgenden Einstellungen sind in Ihrem Canvas vorkonfiguriert:
- Grundlagen
    - Canvas-Name: **Abandoned cart**
    - Konversions-Event: `ecommerce.order_placed`
        - Conversion-Frist: 3 Tage
- Entry-Zeitplan
    - Aktionsbasierter Trigger or triggern, wenn ein:e Nutzer:in das **Perform Cart Updated Event** auslöst (im Dropdown-Menü)
    - Startzeit ist der Zeitpunkt, an dem Sie das Canvas-Template erstellen<br><br>![„Action Based Options“ für das Canvas.]({% image_buster /assets/img/ecommerce/abandoned_cart_entry.png %})<br><br>
- Zielgruppe
    - Entry-Zielgruppe
        - Hat diese Apps **mehr als 0** Mal verwendet
        - E-Mail **ist nicht leer**
    - Eingangskontrollen
        - Nutzer:innen sind sofort wieder für den Canvas-Eingang berechtigt
    - Ausstiegskriterien
        - Führt `ecommerce.cart_updated`, `ecommerce.checkout_started` oder `ecommerce.order_placed` aus<br><br>![Eingangskontrollen und Ausstiegskriterien für das Canvas.]({% image_buster /assets/img/ecommerce/abandoned_cart_entry_exit.png %})<br><br>
- Sendeeinstellungen
    - Nutzer:innen, die abonniert oder per Opt-in angemeldet sind
- Verzögerungsschritt
     - 4 Stunden Verzögerung
- Nachrichtenschritt
    - Überprüfen Sie das E-Mail-Template und den HTML-Block mit einem Liquid-Templating-Beispiel, um Produkte zu Ihrer Nachricht im vorgefertigten Template hinzuzufügen. Wenn Sie Ihr eigenes E-Mail-Template verwenden, können Sie auch [Liquid-Variablen](#message-personalization) referenzieren, wie im folgenden Abschnitt gezeigt.

#### So funktioniert die Re-Entry-Logik bei Warenkorb-Abbrüchen {#how-abandoned-cart-re-entry-logic-works}

Wenn ein:e Nutzer:in den Checkout-Prozess startet, wird der Warenkorb als `checkout_started` markiert. Ab diesem Zeitpunkt berechtigen weitere Warenkorb-Updates mit derselben Warenkorb-ID die Nutzer:innen nicht mehr dazu, die Journey für Warenkorb-Abbrüche erneut zu betreten.

1. Wenn ein:e Nutzer:in einen Artikel in den Warenkorb legt, betritt er/sie den Canvas.
2. Bei jeder Hinzufügung oder Aktualisierung von Artikeln erfolgt ein erneuter Eintritt in den Canvas – so bleiben Warenkorb-Daten und Messaging stets aktuell.
3. Wenn der/die Nutzer:in den Checkout-Prozess startet, wird der Warenkorb mit `checkout_started` getaggt und er/sie verlässt den Canvas.
4. Zukünftige Warenkorb-Updates mit derselben Warenkorb-ID Trigger or triggern or triggern keinen erneuten Eintritt, da dieser Warenkorb bereits in die Checkout-Phase übergegangen ist.

Wenn Nutzer:innen zur Checkout-Journey übergehen, werden sie stattdessen vom [Canvas für abgebrochene Checkouts](#abandoned-checkout) angesprochen, der für Nutzer:innen konzipiert ist, die sich bereits weiter im Kaufprozess befinden.

#### Produktpersonalisierung für E-Mails bei Warenkorb-Abbruch {#abandoned-cart-checkout}

Journeys bei Warenkorb-Abbruch erfordern einen speziellen `shopping_cart` Liquid-Tag für die Produktpersonalisierung.

Hier sehen Sie ein Beispiel, wie Sie mit Ihrem `shopping_cart` Liquid-Tag einen HTML-Block hinzufügen, um Produkte in Ihre E-Mail aufzunehmen.

{% raw %}
```java
<table aria-label="Abandoned cart product personalization for emails #abandoned-cart-checkout" style="width:100%">
  {% shopping_cart {{context.${cart_id}}} %}
  {% for item in shopping_cart.products %}
  {% catalog_items <add_your_catalog_name> {{item.variant_id}} %}
  <tr>
    <th><img src="{{ items[0].variant_image_url }}" width="200" height="200"><img></th>
    <th align="left">
      <ul style="list-style-type: none">
        <li>Item: {{ item.product_name }}</li>
        <li>Price: ${{ item.price }}</li>
        <li>Quantity: ${{ item.quantity }}</li>
        <li>Variant ID: {{ item.variant_id }}</li>
        <li>Product URL:{{ item.product_url }}</li>
        <li>SKU: {{ item.metadata.sku }}</li>
      </ul>
    </th>
  </tr>
  {% endfor %}
</table>
```
{% endraw %}

{% alert note %}
Wenn Sie Shopify verwenden, fügen Sie Ihren Katalognamen hinzu, um die Varianten-Bild-URL abzurufen.
{% endalert %}

##### HTML-Warenkorb-URL {#html-cart-url}

Wenn Sie Nutzer:innen zurück zu ihrem Warenkorb leiten möchten, können Sie eine verschachtelte Event-Eigenschaft unter dem Metadaten-Objekt hinzufügen, zum Beispiel:

{% raw %}
```liquid
{{context.${metadata}.cart_url}}
```
{% endraw %}

Wenn Sie Shopify verwenden, erstellen Sie Ihre Warenkorb-URL mit diesem Liquid-Template:

{% raw %}
```liquid
{{context.${source}}}/checkouts/cn/{{context.${cart_id}}}
```
{% endraw %}

{% endtab %}
{% tab Abandoned checkout %}

### Abgebrochener Checkout {#abandoned-checkout}

Verwenden Sie das Template **Abandoned checkout**, um Kund:innen anzusprechen, die den Checkout-Prozess begonnen, aber vor der Bestellung abgebrochen haben.

![Ein angewandtes „Abandoned Checkout“ Canvas-Template mit erweiterten „Entry Rules“.]({% image_buster /assets/img_archive/abandoned_checkout.png %})

#### Einrichtung

Wählen Sie auf der Canvas-Seite **Use a Canvas Template** > **Braze templates** und wenden Sie dann das Template **Abandoned checkout** an.

##### Standardeinstellungen

Die folgenden Einstellungen sind in Ihrem Canvas vorkonfiguriert:

- Grundlagen
    - Canvas-Name: **Abandoned checkout**
    - Konversions-Event: `ecommerce.order_placed`
        - Conversion-Frist: 3 Tage
- Entry-Zeitplan
    - Aktionsbasierter Trigger or triggern, wenn ein:e Nutzer:in das Event `ecommerce.checkout_started` ausführt
    - Startzeit ist der Zeitpunkt, an dem Sie das Canvas-Template erstellen<br><br>![„Action Based Options“ für das Canvas.]({% image_buster /assets/img/ecommerce/abandoned_checkout_entry.png %})
- Zielgruppe
    - Entry-Zielgruppe
        - Hat diese Apps **mehr als 0** Mal verwendet
        - E-Mail **ist nicht leer**
    - Eingangskontrollen
        - Nutzer:innen sind sofort wieder für den Canvas-Eingang berechtigt
        - Ausstiegskriterien
            - Führt die Events `ecommerce.order_placed` aus<br><br>![Eingangskontrollen und Ausstiegskriterien für das Canvas.]({% image_buster /assets/img/ecommerce/abandoned_checkout_entry_exit.png %})<br><br>
- Sendeeinstellungen
    - Nutzer:innen, die abonniert oder per Opt-in angemeldet sind
- Verzögerungsschritt
    - 4 Stunden Verzögerung
- Nachrichtenschritt
    - Überprüfen Sie das E-Mail-Template und den HTML-Block mit einem Liquid-Templating-Beispiel, um Produkte zu Ihrer Nachricht im vorgefertigten Template hinzuzufügen. Wenn Sie Ihr eigenes E-Mail-Template verwenden, können Sie auch [Liquid-Variablen](#message-personalization) referenzieren, wie im folgenden Abschnitt gezeigt.

#### Personalisierung für E-Mails bei abgebrochenem Checkout {#abandoned-checkout-personalization-for-emails}

Journeys bei abgebrochenem Checkout erfordern einen speziellen `shopping_cart` Liquid-Tag für die Produktpersonalisierung.

Hier sehen Sie ein Beispiel, wie Sie mit Ihrem `shopping_cart` Liquid-Tag einen HTML-Block hinzufügen, um Produkte in Ihre E-Mail aufzunehmen.

{% raw %}
```java
<table aria-label="Abandoned checkout personalization for emails" style="width:100%">
  {% shopping_cart {{context.${cart_id}}} :abort_if_not_abandoned false %}
  {% for item in shopping_cart.products %}
  {% catalog_items <add_your_catalog_name> {{item.variant_id}} %}
  <tr>
    <th><img src="{{ items[0].variant_image_url }}" width="200" height="200"><img></th>
    <th align="left">
      <ul style="list-style-type: none">
        <li>Item: {{ item.product_name }}</li>
        <li>Price: ${{ item.price }}</li>
        <li>Quantity: ${{ item.quantity }}</li>
        <li>Variant ID: {{ item.variant_id }}</li>
        <li>Product URL:{{ item.product_url }}</li>
        <li>SKU: {{ item.metadata.sku }}</li>
      </ul>
    </th>
    {% endfor %}
</table>
```
{% endraw %}

##### `abort_if_not_abandoned` {#abort-if-not-abandoned}

Der Parameter `abort_if_not_abandoned` ist spezifisch für den Anwendungsfall des abgebrochenen Checkouts und wird ausschließlich mit dem `shopping_cart` Liquid-Tag in Verbindung mit dem Event `ecommerce.checkout_started` verwendet.

| Wert | Verhalten |
| ----- | -------- |
| `true` (Standard) | Die Nachricht wird abgebrochen, wenn der Warenkorb nicht verlassen wurde – das heißt, wenn der/die Nutzer:in die Bestellung inzwischen abgeschlossen hat. |
| `false` | Die Nachricht wird auch dann gesendet, wenn sich der Warenkorb nicht im abgebrochenen Zustand befindet. So kann die E-Mail Warenkorb-Details enthalten, unabhängig vom aktuellen Checkout-Status. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="abortifnotabandoned #abort-if-not-abandoned" }

Setzen Sie `abort_if_not_abandoned` auf `false`, wenn Sie die Checkout-Erinnerung unabhängig davon senden möchten, ob der Warenkorb zum Sendezeitpunkt noch als abgebrochen gilt. Wenn Sie den Parameter weglassen oder auf `true` setzen, bricht Braze die Nachricht für Nutzer:innen ab, die ihren Kauf bereits abgeschlossen haben.

##### Checkout-URL

{% raw %}
```liquid
{{context.${metadata}.checkout_url}}
```
{% endraw %}

{% endtab %}
{% tab Order confirmation and feedback survey %}

### Bestellbestätigung und Feedback-Umfrage {#order-confirmation-and-feedback-survey}

Verwenden Sie das Template **Order confirmation & feedback survey**, um erfolgreiche Bestellungen zu bestätigen und die Kundenzufriedenheit zu steigern.

![Ein angewandtes „Order confirmation“ Canvas-Template mit erweiterten „Entry Rules“.]({% image_buster /assets/img_archive/order_confirmation_feedback.png %})

#### Einrichtung

Wählen Sie auf der Canvas-Seite **Use a Canvas Template** > **Braze templates** und wenden Sie dann das Template **Order confirmation & feedback survey** an.

##### Standardeinstellungen

Die folgenden Einstellungen sind in Ihrem Canvas vorkonfiguriert:

- Grundlagen
    - Canvas-Name: **Order confirmation with feedback survey**
    - Konversions-Event: `ecommerce.session_start`
        - Conversion-Frist: 10 Tage
- Entry-Zeitplan
    - Aktionsbasierter Trigger or triggern, wenn ein:e Nutzer:in das Event `ecommerce.cart_updated` ausführt
    - Startzeit ist der Zeitpunkt, an dem Sie das Canvas-Template erstellen<br><br>![„Action Based Options“ für das Canvas.]({% image_buster /assets/img/ecommerce/feedback_entry.png %})<br><br>
- Zielgruppe
    - Entry-Zielgruppe
        - Hat diese Apps **mehr als 0** Mal verwendet
        - E-Mail **ist nicht leer**
    - Eingangskontrollen
        - Nutzer:innen sind sofort wieder für den Canvas-Eingang berechtigt
    - Ausstiegskriterien
        - Nicht zutreffend<br><br>![Zusätzliche Filter und Eingangskontrollen für das Canvas.]({% image_buster /assets/img/ecommerce/feedback_entry_exit.png %})<br><br>
- Sendeeinstellungen
    - Nutzer:innen, die abonniert oder per Opt-in angemeldet sind
- Nachrichtenschritt
    - Überprüfen Sie das E-Mail-Template und den HTML-Block mit einem Liquid-Templating-Beispiel, um Produkte zu Ihrer Nachricht im vorgefertigten Template hinzuzufügen. Wenn Sie Ihr eigenes E-Mail-Template verwenden, können Sie auch [Liquid-Variablen](#message-personalization) referenzieren, wie im folgenden Abschnitt gezeigt.

#### Personalisierung der Bestellbestätigung für E-Mails {#order-confirmation-personalization-for-emails}

Hier sehen Sie ein Beispiel, wie Sie einen HTML-Produktblock zu Ihrer Bestellbestätigung hinzufügen, nachdem eine Bestellung aufgegeben wurde.

{% raw %}
```json
<table aria-label="Order confirmation personalization for emails" style="width:100%">
  {% for item in {{context.${products}}} %}
  {% catalog_items <add_your_catalog_name> {{item.variant_id}} %}
  <tr>
    <th><img src="{{ items[0].variant_image_url }}" width="200" height="200" /></th>
    <th align="left">
      <ul style="list-style-type: none">
        <li>Item: {{item.product_name}}</li>
        <li>Price: {{item.price}}</li>
        <li>Quantity: {{item.quantity}}</li>
      </ul>
    </th>
  </tr>
  {% endfor %}
</table>
```
{% endraw %}

##### Auftragsstatus-URL {#order-status-url}

{% raw %}
```liquid
{{context.${metadata}.order_status_url}}
```
{% endraw %}

{% endtab %}
{% endtabs %}