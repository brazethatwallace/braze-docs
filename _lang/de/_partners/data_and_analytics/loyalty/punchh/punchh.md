---
nav_title: Punchh
article_title: Punchh
page_order: 1
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Punchh, einer Plattform für Kundenbindung und Engagement, die es Ihnen ermöglicht, Daten zwischen den beiden Plattformen zu synchronisieren. In Braze veröffentlichte Daten stehen für die Segmentierung zur Verfügung und können über in Braze eingerichtete Webhook-Templates Nutzerdaten zurück in Punchh synchronisieren."
page_type: partner
search_tag: Partner

---

# Punchh

> [Punchh](https://punchh.com/) ist eine branchenführende Plattform für Kundenbindung und Engagement, die es Marken ermöglicht, Omnichannel-Kundenbindungs-Programme sowohl im Shop als auch digital anzubieten.

_Diese Integration wird von Punchh gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Braze und Punchh ermöglicht es Ihnen, Daten für Geschenk- und Treuezwecke über die beiden Plattformen hinweg zu synchronisieren. In Braze veröffentlichte Daten stehen für die Segmentierung zur Verfügung und können Nutzerdaten über Braze-Webhooks zurück in Punchh synchronisieren.

## Was sind die Vorteile? {#what-are-the-benefits}

- Nehmen Sie Loyalitätsdaten von Punchh in Realtime in Braze auf.
- Nutzen Sie leistungsstarke Zielgruppendaten von Braze, um aussagekräftige und dynamische kanalübergreifende Erlebnisse (App, Mobilgerät, Internet, E-Mail und SMS) bereitzustellen.
  - Haben die Kund:innen ihre E-Mails geöffnet? Haben die Kund:innen die App in der Nähe eines Shops geöffnet?
- Standardisieren Sie das Erscheinungsbild von Transaktions-E-Mails, die über Braze versendet werden.
- Erstellen Sie Journeys, die A/B-Tests und eine Optimierung im laufenden Betrieb ermöglichen.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
|---|---|
| Punchh-Konto | Sie benötigen ein aktives Punchh-Konto, um die Vorteile dieser Partnerschaft zu nutzen. |
| Braze REST-API-Schlüssel | Ein Braze REST-API-Schlüssel mit `users.track`-Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST-Endpunkt | [Ihre URL für den REST-Endpunkt]({{site.baseurl}}/api/basics#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Was sollte ich sonst noch wissen? {#what-else-should-i-know}

### Vor der Integration {#before-integrating}

- Wenn Sie die Braze-Integration nutzen, sind zwei Kampagnen erforderlich – eine in Punchh und eine zweite in Braze. Wenn Sie beispielsweise eine Kampagne mit einem angehängten Angebot versenden, wird die Geschenkkampagne in Punchh konfiguriert, und die Benachrichtigung kann von Braze aus gesendet werden.
- Gäste sollten bereits in Punchh und Braze vorhanden sein. Punchh filtert alle Kund:innen heraus, die nicht bereits Treuegäste sind.

### Wichtige Hinweise {#important-things-to-note}

- Punchh bietet die Möglichkeit, das Senden von Standard-Nutzerattributen an Braze zu deaktivieren, sodass der Kund:in keine Mehrkosten für Datenpunkte entstehen. Dies wird bei der Einrichtung des Adapters konfiguriert.
- Wenn Sie angepasste Segmente für wiederkehrende Kampagnen verwenden, muss der Kampagnenname anstelle der Kampagnen-ID verwendet werden, da sich die IDs bei jedem Kampagnendurchlauf ändern.
- Zu den Kommunikationskanälen, die innerhalb jeder Punchh-Geschenkkampagne zur Verfügung stehen, gehören Rich Messages, Push-Benachrichtigungen, SMS und E-Mail.
- Nachdem Nutzer:innen von Braze an ein angepasstes Punchh-Segment gesendet wurden, können sie nicht mehr entfernt werden. Einem bestehenden angepassten Segment können nur neue Gäste hinzugefügt werden. Wenn Gäste aus einem bestehenden angepassten Punchh-Segment entfernt werden sollen, muss in Braze eine neue Webhook-Kampagne erstellt werden, um Nutzer:innen an ein neues angepasstes Punchh-Segment zu senden.

## Integration

Punchh bietet verschiedene Endpunkte an, die Braze-Kund:innen zur Verfügung stehen, um der Punchh-Plattform über die folgenden Punchh-API-Endpunkte externe IDs hinzuzufügen. Nachdem die externen IDs hinzugefügt wurden, erstellen Sie einen Adapter in Punchh, geben Ihre Braze-Zugangsdaten an und wählen die Ereignisse aus, die Sie synchronisieren möchten. Anschließend können Sie die Punchh-Segment-ID verwenden, um einen Punchh-Webhook zu erstellen, der die Kundensynchronisierung in einer Canvas Journey triggert.

Beachten Sie, dass die Punchh `user_id` und die Braze `external_id` in beiden Plattformen verfügbar sein müssen, damit die Integration korrekt synchronisiert werden kann.
- Ereignisse, die von Punchh an Braze gesendet werden, enthalten die Braze `external_id` als Bezeichner. Wenn Punchh so konfiguriert ist, dass die `external_source_id` verwendet wird, wird dieser Wert als Braze `external_id` gesetzt. Andernfalls wird bei der Integration standardmäßig die Punchh `user_id` als Braze `external_id` gesetzt.
- Um Webhooks von Braze an Punchh zu senden, muss die Punchh `user_id` im Braze-Nutzerprofil verfügbar sein. Wenn die Punchh `user_id` nicht als Braze `external_id` verwendet wird, sollte sie als angepasstes Attribut „punchh_user_id“ festgelegt werden.

### 1. Schritt: Einrichten von externen ID-Ingestion-Endpunkten (optional) {#step-1-set-up-external-id-ingestion-endpoints-optional}

Externe IDs von Braze können über die folgenden Endpunkte für neue und bestehende Punchh-Nutzer:innen hinzugefügt werden.

{% alert important %}
Die Werte in den Feldern `external_source` und `external_source_id` müssen für Punchh eindeutig sein und dürfen nicht mit bestehenden Profilen verknüpft sein.
{% endalert %}

1. Neue Punchh-Nutzer:innen<br>
Erstellen Sie neue Nutzer:innen in Punchh mit einem Punchh-Registrierungsendpunkt unter Verwendung der Felder `external_source` und `external_source_id`. Punchh ermöglicht die Übermittlung externer Bezeichner mit einem Nutzerprofil über einen der folgenden Registrierungsendpunkte:
- [Mobile Signup API](https://developers.punchh.com/docs/dev-portal-mobile/2e67abf6f8e12-sign-up-register)
- [SSO Signup API](https://developers.punchh.com/docs/dev-portal-online-ordering/58f18dfdd2a3d-signup-with-email-and-password)<br><br>
2. Bestehende Punchh-Nutzer:innen <br>
Aktualisieren Sie die `external_source_id` für bestehende Punchh-Nutzer:innen. Punchh ermöglicht das Hinzufügen externer Bezeichner zu einem Profil über einen Nutzer-API-Update-Endpunkt:
- [Mobile User Update](https://developers.punchh.com/docs/dev-portal-mobile/c9b928e35a6f3-update-user-profile)
- [SSO User Update](https://developers.punchh.com/docs/dev-portal-online-ordering/eef4eef6c97a0-update-user-information)
- [Dashboard User Update](https://developers.punchh.com/docs/dev-portal-platform-functions/6351feaf591aa-update-a-user)
<br><br>
{% tabs local %}
{% tab Beispiel für die Nutzerregistrierungs-API %}
Dieses Beispiel ermöglicht es Ihnen, bei der Registrierung externe Bezeichner mit einem Nutzerprofil zu senden. Dies geschieht, indem Sie `external_source` als "customer_id" und `external_source_id` als "111111111111111111" als String-Datentyp senden.

```bash
curl --location --request POST 'https://server_name_goes_here.punchh.com/api2/mobile/users' \
--header 'Content-Type: application/json' \
--header 'x-pch-digest: SIGNATURE' \
--header 'Accept-Timezone: Etc/UTC' \
--header 'Accept: application/json' \
--header 'Accept-Language: en' \
--data-raw '{
    "client":"CLIENT",
    "user" : {
      "email": "test@example.com",
      "password": "PASSWORD",
      "first_name":"FIRST_NAME",
      "last_name":"LAST_NAME",
      "terms_and_conditions":"true",
      "anniversary":"2014-02-02",
      "zip_code":"94497",
      "birthday":"2004-02-02",
      "external_source":"customer_id",
      "external_source_id":"111111111111111111"
      }
}'
```
{% endtab %}
{% tab Beispiel für die Nutzeraktualisierungs-API %}
Dieses Beispiel ermöglicht es Ihnen, externe Bezeichner mit einem Nutzerprofil zu aktualisieren. Dies geschieht, indem Sie `external_source` als "customer_id" und `external_source_id` als "111111111111111111" als String-Datentyp senden.

```bash
curl --location --request PUT 'https://server_name_goes_here.punchh.com/api2/mobile/users' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Accept-Language: en' \
--header 'x-pch-digest: SIGNATURE' \
--header 'Authorization: Bearer ACCESS_TOKEN' \
--data-raw '{
    "client":"CLIENT",
    "user": {
        "external_source":"customer_id",
        "external_source_id":"111111111111111111"
    }
}'
```
{% endtab %}
{% endtabs %}

{% alert note %}
**Plattform-Konfiguration:** Um externe Bezeichner in Punchh zu aktivieren, navigieren Sie im Punchh-Dashboard zu **Cockpit** > **Dashboard** > **External User Identifier**.
{% endalert %}

### 2. Schritt: Braze-Adapter-Einrichtung in Punchh {#step-2-braze-adapter-setup-in-punchh}

#### Verfügbare zu synchronisierende Ereignisse {#available-events-to-sync}

1. **Gast:** Ausgelöst bei jeder Registrierung, Aktualisierung des Gastprofils, Deaktivierung oder Löschung
2. **Loyalitäts-Check-in:** Ausgelöst bei Treuetransaktionen oder durch Scannen des Barcodes auf dem Kassenbon
3. **Geschenk-Check-in:** Ausgelöst durch Punkte, die aus einer Kampagne verschenkt werden
4. **Einlösung:** Ausgelöst bei jeder Prämieneinlösung mit Ausnahme von Punchh-Coupons, da diese separat als Coupon-Ereignisse gesendet werden, einschließlich Ausgabe und Einlösung
5. **Rewards:** Ausgelöst durch geschenkte Rewards aus Kampagnen, Aktivität, Konversion von Punkten in Rewards oder Admin-Geschenke
6. **Transaktionsbenachrichtigungen:** Ausgelöst bei Transaktionsaktivitäten einer Nutzer:in innerhalb des Punchh-Systems (z. B. Punkteverfall)
7. **Marketing-Benachrichtigungen:** Ausgelöst auf der Grundlage verschiedener Kampagnen-Setups in Punchh für ein zugehöriges Segment von Nutzer:innen

{% alert note %}
In der Punchh-Dokumentation finden Sie Beispiel-Payloads für diese verfügbaren Ereignisse.
{% endalert %}

Arbeiten Sie mit Ihrem Punchh Implementation Manager zusammen, um diesen Adapter einzurichten.

Um die Integration von Braze und Punchh einzurichten, gehen Sie wie folgt vor:

1. Navigieren Sie im Punchh-Dashboard zu **Cockpit** > **Dashboard** > **Major Features** > **Enable Webhook Management** und schalten Sie **Enable Webhook Management** ein.<br><br>
2. Aktivieren Sie als Nächstes die Adapter, indem Sie zu **Settings** > **Webhooks Manager** > **Configurations** > **Show Adapters Tab** navigieren und **Show Adapters Tab** einschalten.<br><br>
3. Navigieren Sie zum **Webhooks Manager** unter dem Tab **Settings**, wählen Sie den Tab **Adapters** und klicken Sie auf **Create Adapter**. <br><br>![Punchh Webhooks Manager – Tab „Adapters“ mit ausgewähltem „Create Adapter“.]({% image_buster /assets/img/punchh/punchh1.png %})<br><br>
4. Geben Sie den Adapternamen, die Beschreibung und die Admin-E-Mail ein. Wählen Sie **Braze** als Ihren Adapter und geben Sie Ihren Braze REST-API-Endpunkt und Braze-API-Schlüssel an.<br><br>
5. Wählen Sie dann die verfügbaren Ereignisse aus, die Sie aktivieren möchten. Eine Liste dieser Ereignisse finden Sie unter [Verfügbare zu synchronisierende Ereignisse](#available-events-to-sync).<br><br>![Punchh-Adaptereinstellungen mit auswählbaren Ereignissen für die Braze-Synchronisierung.]({% image_buster /assets/img/punchh/punchh3.png %})<br><br>
6. Klicken Sie auf **Submit**, um den Webhook zu aktivieren.

## Punchh-Webhook in Braze erstellen {#create-punchh-webhook-in-braze}

Braze kann Nutzer:innen über Webhooks unter Verwendung von angepassten Punchh-Segmenten zu einem Punchh-Segment hinzufügen.

1. Erstellen Sie ein angepasstes Segment in Punchh und notieren Sie die `custom_segment_id`, die in der URL des Punchh-Segment-Dashboards angezeigt wird (siehe folgendes Beispiel). Es können sowohl der klassische als auch der Beta-Segment-Builder verwendet werden. Es wird jedoch empfohlen, die Beta-Version zu verwenden, da die klassische Version irgendwann eingestellt wird.<br><br>Navigieren Sie in der Punchh-Plattform zu **Guest** > **Segment** > **Custom List** > **New Custom List**.<br><br>![Punchh-Dashboard für angepasste Segmente mit der angepassten Segment-ID in der URL.]({% image_buster /assets/img/punchh/update1.png %})<br><br>

2. Erstellen Sie eine Webhook-Kampagne in Braze, indem Sie den Punchh-Endpunkt zum Hinzufügen einer Nutzer:in zu einem angepassten Segment als Webhook-URL verwenden. Hier können Sie die `custom_segment_id` aus der URL und die `user_id` als Schlüssel-Wert-Paare angeben.<br><br>![Braze-Webhook-Composer mit Punchh-Endpunkt und Schlüssel-Wert-Payload-Feldern.]({% image_buster /assets/img/punchh/punchh4.png %})<br><br>

3. Dieser Webhook kann als einzelne Kampagne oder als Schritt innerhalb eines Canvas eingerichtet werden. Wenn der Webhook, der Nutzer:innen zu diesem speziellen Punchh-Segment hinzufügt, in mehreren Campaigns oder Canvases verwendet werden soll, kann er alternativ als [Template]({{site.baseurl}}/user_guide/messaging/templates/webhook_templates) eingerichtet werden.<br><br>
Der Schlüssel `user_id` innerhalb des Webhooks bildet die Punchh-Nutzer-ID ab. Dieser Bezeichner muss zu allen in Braze erstellten Webhooks hinzugefügt werden, um Nutzer:innen einem angepassten Punchh-Segment hinzuzufügen. Das angepasste Attribut `punch_user_id` kann mithilfe von [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid#pre-formatted-variables) dynamisch als Wert für den Schlüssel `user_id` eingefügt werden. Sie können die angepasste Attributvariable `punchh_user_id` einfügen, indem Sie das blaue „Plus“-Symbol in der Symbolleiste des Template-Textfelds verwenden.<br><br>![Braze-Webhook-Payload-Feld mit eingefügter Punchh-Nutzer-ID-Liquid-Variable.]({% image_buster /assets/img/punchh/update3.png %}){: style="max-width:65%;"}<br><br>![Braze-Personalisierungsauswahl mit dem angepassten Attribut „punchh_user_id“.]({% image_buster /assets/img/punchh/update4.png %}){: style="max-width:65%;"}<br><br>

4. Nachdem der Webhook gespeichert wurde, kann er zur Synchronisierung von Nutzer:innen verwendet werden. Wenn diese Braze-Webhook-Kampagne gestartet wird, werden beispielsweise 136 Gäste dem angepassten Punchh-Segment hinzugefügt.<br><br>![Ein Beispiel für die Synchronisierung von Nutzer:innen mit dem gespeicherten Webhook aufgrund der Integration von Braze und Punchh.]({% image_buster /assets/img/punchh/punchh6.png %})

Weitere Informationen darüber, wie Webhooks bei Braze verwendet werden, finden Sie unter [Einen Webhook erstellen]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook).

## Anwendungsfälle für Kampagnen {#use-case-campaigns}

### Kampagnen- und Canvas-Konfiguration {#campaign-and-canvas-configuration}

#### Triggern {#triggering}

Anwendungsfälle für Braze-Messaging, das durch an Braze gesendete Punchh-Ereignisse ausgelöst wird, wie z. B. Reward-Ereignisse oder Gast-Ereignisse, können als [aktionsbasierte Campaigns]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery#action-based-delivery) oder Canvases erstellt werden, die durch das entsprechende Punchh-Ereignis getriggert werden.

Wenn Sie einen Trigger hinzufügen, wird die Liste der in Braze erstellten Ereignisse angezeigt. Wählen Sie das Ereignis, das Ihre Campaign oder Ihr Canvas triggern soll, damit es an die Nutzer:in gesendet wird, die das Ereignis protokolliert hat.

![Braze-Trigger-Konfiguration mit einem ausgewählten Punchh-Ereignis für eine aktionsbasierte Campaign.]({% image_buster /assets/img/punchh/update5.png %})

Sie können Eigenschaftsfilter hinzufügen, um das auslösende Ereignis weiter zu filtern. Beispielsweise sollte die Nachricht nur dann ausgelöst werden, wenn eine Kund:in das Ereignis „checkins_gift“ triggert, bei dem die genehmigte Eigenschaft `true` lautet. Dies ist ein optionales Feature, das möglicherweise nicht auf alle Anwendungsfälle anwendbar ist.

#### Segmentierung {#segmentation}

In vielen Fällen können Braze Campaigns und Canvases, die durch Punchh-Ereignisse ausgelöst werden, auf die Zielgruppe „Alle Nutzer:innen“ eingestellt werden, da die Segmentierung der Nutzer:innen, die diese Ereignisse triggern, in Punchh festgelegt wird. Kund:innen, die jedoch die Zielgruppe der Nutzer:innen, die das durch das Ereignis ausgelöste Braze-Messaging erhalten, weiter verfeinern möchten, können dies tun, indem sie zusätzliche Filter und Segmente im Abschnitt **Target Audiences** des Kampagnen-Composers oder der **Entry Audience** des Canvas-Composers hinzufügen.

### Anwendungsfälle {#use-cases}

{% tabs local %}
{% tab Registrierung %}
#### Registrierungskampagne {#sign-up-campaign}

Wenn Sie die Braze-Konfiguration für eine Registrierungskampagne mit angehängtem Angebot verwenden, muss eine Registrierungs-Geschenkkampagne in Punchh und eine Willkommensnachricht in Braze konfiguriert werden.

Punchh empfiehlt, der Registrierungskampagne eine Ausführungsverzögerung hinzuzufügen, damit Braze die Willkommensnachricht zuerst auf Grundlage des Gast-Ereignisses triggern kann. Wenn Sie eine Folgenachricht senden möchten, die die Nutzer:in darüber informiert, dass ein Geschenk erhalten wurde, können Sie dies auf Grundlage des Reward-Ereignisses triggern.

Im Falle einer Registrierungskampagne können alle Registrierten für das Segment verwendet werden; daher ist ein angepasstes Braze-Segment nicht erforderlich.

Punchh-Konfigurationen erforderlich:
- Kampagne: Registrierung
- Segment: Alle Registrierten
- Reward: Wahl der Kund:in
Erforderliche Ereignisse:
- Reward-Ereignis
- Gast-Ereignis
Überlegungen:
- Ausführungsverzögerung – es wird empfohlen, eine 5–10-minütige Verzögerung hinzuzufügen

![In Punchh wird ein Nutzer:innen-Segment eingerichtet, und Gäste melden sich für ein Kundenbindungs-Programm an. Danach wird das Gast-Ereignis, falls ausgelöst, und die Braze-Messaging-Kampagne getriggert. Anschließend wird die Punchh-Registrierungs-Geschenkkampagne nach 10 Minuten getriggert, wodurch das Reward-Ereignis und die optionale Folgenachricht ausgelöst werden.]({% image_buster /assets/img/punchh/usecase3.png %})
{% endtab %}

{% tab Braze-Willkommen %}
#### Braze-Willkommenskampagne {#braze-welcome-campaign}

Wenn sich neue Nutzer:innen anmelden, sendet Punchh ein Gast-Ereignis an Braze, das die Nutzer:in anlegt und ein angepasstes Attribut `signup_channel` sendet, mit dem Sie die Braze-Willkommenskampagne triggern können.

Um die Braze-Willkommenskampagne einzurichten, gehen Sie folgendermaßen vor:

1. Erstellen Sie in Braze eine aktionsbasierte Campaign.
2. Wählen Sie als Trigger **Change Custom Attribute Value** und setzen Sie das angepasste Attribut `signup_channel` auf **Any new value**.
3. Fahren Sie mit der Erstellung Ihrer Campaign fort und senden Sie sie ab, wenn Sie bereit sind!

{% endtab %}
{% tab Massenangebot %}
#### Massenangebotskampagne {#mass-offer-campaign}

Wenn Sie eine Massenangebotskampagne für Geschenke verwenden, muss eine Massenangebotskampagne in Punchh und eine Messaging-Kampagne in Braze konfiguriert werden.

Wenn Sie ein Braze-Segment für Ihre Kampagne verwenden oder vor dem Beschenken von Gästen auf der Punchh-Plattform eine Mitteilung von Braze senden möchten, ist ein [angepasstes Punchh-Segment]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/punchh#step-3-create-punchh-webhook-in-braze) für die Punchh-Geschenkkampagne erforderlich.

Die Erstellung eines Segments von Nutzer:innen, die dieses Angebot erhalten sollen, ist in Braze nur dann empfehlenswert, wenn Sie Attribute verwenden, die in Punchh nicht verfügbar sind. Andernfalls kann die Punchh-Segmentierung verwendet werden, und die Braze-Messaging-Kampagne wird als aktionsbasierte Campaign erstellt, die durch die Nutzer:innen ausgelöst wird, die ihre Belohnung erhalten (das von Punchh ausgelöste Reward-Ereignis).

Punchh-Konfigurationen erforderlich:
- Kampagne: Massenangebot
- Segment: Angepasste Liste oder Wahl der Kund:in
- Reward: Wahl der Kund:in

**Mit Punchh für Segmentierung und Geschenke und Braze für Messaging:**<br>
Beispiel: Eine 2-$-Rabattprämie wird an ein innerhalb von Punchh konfigurierbares Segment gesendet, wobei das Messaging über Braze erfolgt.<br>
![In Punchh kann ein Nutzer:innen-Segment konfiguriert werden, und Nutzer:innen erhalten über eine Punchh-Massenangebotskampagne ein Geschenk. Anschließend wird ein Reward-Ereignis ausgelöst, und dann wird die Braze-Messaging-Kampagne getriggert.]({% image_buster /assets/img/punchh/usecase6.png %}){: style="max-width:80%;"}

**Mit Braze-Segmentierung und -Messaging und Punchh für Geschenke:**<br>
Beispiel: Eine 2-$-Rabattprämie und Messaging an ein Segment mit Attributen, die in Punchh nicht verfügbar sind.<br>
![In Braze kann ein Nutzer:innen-Segment konfiguriert werden, und dann kann eine Nachricht von einem Braze-Segment gesendet werden. Anschließend werden die Nutzer:innen über einen Braze-Webhook mit Segment- und Nutzer-ID an das angepasste Punchh-Segment gesendet. Danach erhalten die Nutzer:innen ein Geschenk durch eine Punchh-Massenangebotskampagne mit einem angepassten Segment. Danach wird das Reward-Ereignis getriggert.]({% image_buster /assets/img/punchh/usecase5.png %}){: style="max-width:80%;"}

**Mit Braze-Segmentierung und Punchh für Geschenke oder Messaging oder beides:**<br>
Beispiel: Eine 2-$-Rabattprämie wird an ein Segment gesendet, dessen Attribute in Punchh nicht verfügbar sind, aber es ist kein Messaging erforderlich, oder das Messaging kann über Punchh gesendet werden (beachten Sie, dass alle Gäste in Punchh vorhanden sein müssen).<br>
![Ein Nutzer:innen-Segment kann in Braze konfiguriert werden, und die Nutzer:innen werden über einen Braze-Webhook mit Segment- und Nutzer-ID an das angepasste Punchh-Segment gesendet. Danach erhalten die Nutzer:innen ein Geschenk durch eine Punchh-Massenangebotskampagne mit einem angepassten Segment. Danach wird das Reward-Ereignis getriggert.]({% image_buster /assets/img/punchh/usecase4.png %})

{% endtab %}
{% tab Wiederkehrendes Massenangebot %}
#### Wiederkehrende Massenangebotskampagne {#recurring-mass-offer-campaign}

Wenn Sie eine wiederkehrende Massenangebotskampagne für Geschenke verwenden, muss eine Massenangebotskampagne in Punchh konfiguriert und eine Messaging-Kampagne in Braze eingerichtet werden. Ein angepasstes Punchh-Segment ist erforderlich, wenn die Kund:in die Braze-Segmentierung nutzen möchte (nur empfohlen, wenn Attribute verwendet werden, die in Punchh nicht verfügbar sind). Andernfalls kann die Punchh-Segmentierung verwendet werden, und die Braze-Messaging-Kampagne wird auf Grundlage des Reward-Ereignisses getriggert.

Punchh-Konfigurationen erforderlich:
- Kampagne: Wiederkehrendes Massenangebot
- Segment: Angepasste Liste oder Wahl der Kund:in
- Reward: Wahl der Kund:in
Überlegungen:
- Kampagnen-IDs und Kampagnennamen werden als Ereigniseigenschaften an Braze gesendet. Wenn Sie in Braze einen Punchh-Kampagnenbezeichner verwenden möchten, um die Zielgruppe, die die Kampagne erhält, weiter zu filtern, müssen Sie den Kampagnennamen verwenden, da sich die Kampagnen-IDs täglich ändern.

{% endtab %}
{% tab Post-Check-in-Angebot mit Benachrichtigung %}
#### Post-Check-in-Angebotskampagne mit Benachrichtigung {#post-check-in-offer-campaign-with-notification}

Wenn Sie eine Post-Check-in-Angebotskampagne nutzen, sendet Braze die Benachrichtigung über das Geschenk, und wenn der Gast eincheckt, erhält er ein Geschenk aus der Punchh-Post-Check-in-Kampagne. Daher muss eine Post-Check-in-Angebotskampagne in Punchh und eine Messaging-Kampagne in Braze konfiguriert werden (wenn die Kund:innen über die Kampagne informiert werden sollen).

Punchh-Konfigurationen erforderlich:
- Kampagne: Post-Check-in-Angebot
- Segment: Angepasste Liste
- Reward: Wahl der Kund:in

Beispiel: Eine E-Mail, die Gäste darauf hinweist, dieses Wochenende vorbeizukommen, um doppelte Punkte zu erhalten – an ein Segment mit Attributen, die in Punchh nicht verfügbar sind. Punchh schenkt diesem Segment Punkte nach einem qualifizierten Check-in und optionalem Messaging von Braze.

![Ein Nutzer:innen-Segment wird in Braze konfiguriert, und Nachrichten werden von der Braze-Post-Check-in-Kampagne gesendet. Anschließend werden die qualifizierten Nutzer:innen über einen Braze-Webhook mit Segment- und Nutzer-ID an das angepasste Punchh-Segment gesendet. Schließlich checkt die qualifizierte Nutzer:in im angepassten Segment ein und erhält das Geschenk und die optionale Nachricht durch die Post-Check-in-Kampagne.]({% image_buster /assets/img/punchh/update7.png %})

{% endtab %}
{% tab Post-Check-in-Angebot ohne Benachrichtigung %}
#### Post-Check-in-Angebotskampagne ohne Benachrichtigung {#post-check-in-offer-campaign-without-notification}

Wenn Sie eine Post-Check-in-Angebotskampagne verwenden, bei der die Kund:innen nicht zuerst benachrichtigt werden, wird die Kampagne ein Geschenk machen (optionales Messaging) und eine Benachrichtigung innerhalb von Braze triggern. Daher muss eine Post-Check-in-Angebotskampagne in Punchh konfiguriert werden; eine angepasste Liste ist jedoch nicht erforderlich. Stattdessen können Sie das gewünschte Segment innerhalb von Punchh auswählen.

Punchh-Konfigurationen erforderlich:
- Kampagne: Post-Check-in-Angebot
- Segment: Wahl der Kund:in
- Reward: Wahl der Kund:in

Beispiel: Eine Überraschungs- und Freude-Kampagne von Braze wird an ein in Punchh verfügbares Segment gesendet, das sich bei den Gästen für ihren Besuch bedankt und sie mit 2 $ Rabatt auf ihren nächsten Besuch belohnt.

![Innerhalb von Punchh kann ein Segment für qualifizierte Nutzer:innen konfiguriert werden. Eine qualifizierte Nutzer:in checkt ein und erhält über eine Punchh-Post-Check-in-Kampagne ein Geschenk. Danach wird ein Reward-Ereignis getriggert und die Rückrufnachricht gesendet, die die Gäste über die von Braze gesendete Belohnung informiert.]({% image_buster /assets/img/punchh/usecase2.png %})

{% endtab %}
{% tab Jubiläum %}
#### Jubiläumskampagne {#anniversary-campaign}

Wenn Sie eine Jubiläumskampagne nutzen, erhalten Nutzer:innen zunächst ein Geschenk zu ihrem Jubiläum aus der Punchh-Kampagne. Dieses Geschenk (Reward-Ereignis) triggert die Messaging-Kampagne innerhalb von Braze, die die Nutzer:in über das Geschenk informiert. Eine angepasste Liste ist daher nicht erforderlich. Stattdessen können Sie das Segment und die Jubiläumseinstellungen in Punchh auswählen.

Punchh-Konfigurationen erforderlich:
- Kampagne: Jubiläumskampagne
- Segment: Wahl der Kund:in
- Reward: Wahl der Kund:in
Überlegungen:
- Monat der Registrierung als Geschenk
- Gültigkeitsdauer (Wie lange ist die Geburtstagsbelohnung gültig?)
- Wiederkehrende Kampagnen, Zeitplan erforderlich

![Ein optionales Segment kann innerhalb von Punchh erstellt werden, und eine qualifizierte Nutzer:in erhält eine Belohnung durch eine Punchh-Jubiläumskampagne. Danach wird ein Reward-Ereignis getriggert und die Rückrufnachricht gesendet, die die Gäste über die von Braze gesendete Belohnung informiert.]({% image_buster /assets/img/punchh/usecase1.png %})

{% endtab %}
{% tab Rückruf %}
#### Rückrufkampagne {#recall-campaign}

Beim Targeting von Nutzer:innen auf Basis von Inaktivität kann eine Rückrufkampagne verwendet werden. Die Kund:in kann das Segment und die Kampagne innerhalb von Punchh erstellen, aber Braze für das Messaging nutzen.

Wenn Sie eine in Braze erstellte Segmentierung verwenden möchten, können Sie ein [angepasstes Punchh-Segment]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/punchh#step-3-create-punchh-webhook-in-braze) auf Basis von Inaktivität an eine wiederkehrende Massenangebotskampagne anhängen.

Punchh-Konfigurationen erforderlich:
- Kampagne: Rückrufkampagne
- Segment: Wahl der Kund:in
- Reward: Wahl der Kund:in
Überlegungen:
- Kampagne läuft nach einem Zeitplan

![Ein optionales Segment kann innerhalb von Punchh erstellt werden, und eine qualifizierte Nutzer:in erhält eine Belohnung durch eine Punchh-Rückrufkampagne. Danach wird ein Reward-Ereignis getriggert, und die Rückrufnachricht wird gesendet, um die Gäste über die von Braze gesendete Belohnung zu informieren.]({% image_buster /assets/img/punchh/usecase.png %})

{% endtab %}
{% endtabs %}