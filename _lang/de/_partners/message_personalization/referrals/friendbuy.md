---
nav_title: FriendBuy
article_title: FriendBuy
description: "Erfahren Sie, wie Sie Friendbuy in Braze integrieren können."
alias: /partners/friendbuy/
page_type: partner
search_tag: Partner

---

# Friendbuy

> Nutzen Sie die Integration zwischen [Friendbuy](https://www.friendbuy.com/) und Braze, um Ihre E-Mail- und SMS-Funktionen zu erweitern und gleichzeitig die Kommunikation Ihrer Empfehlungs- und Kundenbindungs-Programme mühelos zu automatisieren. Braze erstellt Kundenprofile für alle Opt-in-Telefonnummern, die über Friendbuy erfasst wurden.

_Diese Integration wird von Friendbuy gepflegt._

## Voraussetzungen {#prerequisites}

Bevor Sie beginnen, benötigen Sie Folgendes:

| Voraussetzung | Beschreibung |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Ein Friendbuy-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Friendbuy-Konto](https://retailer.friendbuy.io/). |
| Ein Braze-REST-API-Schlüssel | Ein Braze-REST-API-Schlüssel mit `users.track`-Berechtigungen. Dieser kann im Braze-Dashboard unter **Settings** > **API Keys** erstellt werden. |
| Ein Braze-REST-Endpunkt | [Ihre REST-Endpunkt-URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints), die von der URL Ihrer Braze-Instanz abhängt. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration von Friendbuy {#integrating-friendbuy}

Gehen Sie in [Friendbuy](https://retailer.friendbuy.io/) zu **Developer Center** > **Integrations** und wählen Sie dann auf der Braze-Integrationskarte **Add integration** aus.

![Die Braze-Integrationskarte in Friendbuy.]({% image_buster /assets/img/friendbuy/choosing_braze.png %}){: style="max-width:75%;"}

Geben Sie im Formular Ihren REST-Endpunkt und API-Schlüssel ein und wählen Sie dann **Install Integration** aus.

![Das Friendbuy-Integrationsformular.]({% image_buster /assets/img/friendbuy/install_form.png %}){: style="max-width:55%;"}

Gehen Sie zurück zu Ihrem [Friendbuy-Konto](https://retailer.friendbuy.io/) und aktualisieren Sie die Seite. Wenn Ihre Integration erfolgreich war, sehen Sie eine Nachricht ähnlich der folgenden:

![Integration installiert]({% image_buster /assets/img/friendbuy/install_success.png %}){: style="max-width:55%;"}

### Angepasste Attribute {#custom-attributes}

| Name des angepassten Attributs | Definition | Datentyp |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| **Friendbuy Referral Status** | Empfehlende Personen werden als *Advocate* und geworbene Personen als *Referred Friend* kategorisiert. | String |
| **Friendbuy Customer Name** | Der Name, den die Kund:in bei der Übermittlung ihrer Daten über ein Empfehlungs-Widget eingegeben hat. | String |
| **Friendbuy Referral Link** | Ein persönlicher Empfehlungslink (PURL), der für einen Advocate erstellt wurde. Zum Beispiel: https://fbuy.io/EzcW | String |
| **Friendbuy Date of Last Share** | Datum und Uhrzeit, zu der der Advocate zuletzt über einen beliebigen Kanal mit einer Freundin oder einem Freund geteilt hat. Wenn der Advocate noch nicht geteilt hat, ist die Eigenschaft nicht sichtbar. | Time |
| **Friendbuy Campaign ID** | Die Campaign-ID, die mit dem für einen Advocate generierten persönlichen Empfehlungslink verknüpft ist. | String |
| **Friendbuy Campaign Name** | Der Campaign-Name, der mit dem für einen Advocate generierten persönlichen Empfehlungslink verknüpft ist. | String |
| **Friendbuy Coupon Code** | Der neueste Empfehlungs-Gutscheincode, der an die Kund:in verteilt wurde. Hinweis: Es wird nur ein Code angezeigt. | String |
| **Friendbuy Coupon Value** | Der Währungswert des zuletzt an die Kund:in verteilten Gutscheincodes. | Zahl |
| **Friendbuy Coupon Status** | Der Status des zuletzt an die Kund:in verteilten Gutscheincodes. Hinweis: Der Status lautet „distributed“ oder „redeemed“. | String |
| **Friendbuy Coupon Currency** | Währungscode (USD, CAD usw.) oder Prozentsatz (%) in Verbindung mit dem zuletzt an die Kund:in verteilten Gutscheincode. | String |
| **Friendbuy Coupon Campaign ID** | Die Campaign-ID, die mit dem für eine Kund:in generierten Gutscheincode verknüpft ist. | String |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Angepasste Attribute" }

## Standardverhalten {#default-behavior}

Bevor Kundendaten an Braze gesendet werden können, müssen Kund:innen über das Empfehlungs-Widget ein Opt-in durchführen, indem sie eines oder mehrere der folgenden Kontrollkästchen aktivieren:

![Empfehlungs-Widget]({% image_buster /assets/img/friendbuy/referral_widget.png %})

{% alert note %}
Friendbuy verwendet den internationalen Standard (E.164), um echte Telefonnummern zu überprüfen. Ungültige Nummern, wie z. B. `555-555-5555`, werden nicht an Braze gesendet.
{% endalert %}

### Verhalten bei Kontrollkästchen {#checkbox-behavior}

| Kontrollkästchen ausgewählt | Verhalten |
|-------------------|-----------------------------------------------------------------|
| Nur E-Mail | Nur die E-Mail-Adresse der Kund:in wird an Braze gesendet. |
| Nur Telefon | Nur die Telefonnummer der Kund:in wird an Braze gesendet. |
| Keines | Es werden keine Kundendaten an Braze gesendet. |
| Beides | Die E-Mail-Adresse und die Telefonnummer der Kund:in werden an Braze gesendet. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Verhalten bei Kontrollkästchen" }