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

Die Integration von Braze und Punchh ermöglicht es Ihnen, Daten für Geschenk- und Kundenbindungszwecke zwischen den beiden Plattformen zu synchronisieren. In Braze veröffentlichte Daten stehen für die Segmentierung zur Verfügung und können über Braze-Webhooks wieder in Punchh zurücksynchronisiert werden.

## Welche Vorteile bietet die Integration? {#what-are-the-benefits}

- Nehmen Sie Kundenbindungsdaten von Punchh in Braze in Echtzeit auf.
- Nutzen Sie leistungsstarke Zielgruppendaten aus Braze und kombinieren Sie diese, um bedeutungsvolle und dynamische kanalübergreifende Erlebnisse zu schaffen (App, Mobilgeräte, Internet, E-Mail und SMS).
  - Haben Kund:innen E-Mails geöffnet? Haben Kund:innen die App in der Nähe eines Shops geöffnet?
- Standardisieren Sie das Erscheinungsbild von Transaktions-E-Mails, die über Braze versendet werden.
- Erstellen Sie Journeys, die A/B-Tests und laufende Optimierung ermöglichen.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
|---|---|
| Punchh-Konto | Sie benötigen ein aktives Punchh-Konto, um diese Partnerschaft nutzen zu können. |
| Braze-REST-API-Schlüssel | Ein Braze-REST-API-Schlüssel mit `users.track`-Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze-REST-Endpunkt | [Ihre REST-Endpunkt-URL]({{site.baseurl}}/api/basics#endpoints). Ihr Endpunkt hängt von der Braze-URL Ihrer Instanz ab. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Was sollte ich sonst noch wissen? {#what-else-should-i-know}

### Vor der Integration {#before-integrating}

- Bei der Nutzung der Braze-Integration werden zwei Campaigns benötigt: eine in Punchh und eine zweite in Braze. Wenn Sie beispielsweise eine Campaign mit einem angehängten Angebot senden, wird die Geschenk-Campaign in Punchh konfiguriert und die Benachrichtigung kann über Braze gesendet werden.
- Gäste sollten bereits in Punchh und Braze vorhanden sein. Punchh filtert alle Kund:innen heraus, die nicht bereits Gäste im Kundenbindungs-Programm sind.

### Wichtige Hinweise {#important-things-to-note}

- Punchh bietet die Möglichkeit, das Senden von standardmäßigen Nutzerattributen an Braze zu deaktivieren, damit für den Kunden keine Mehrkosten bei Datenpunkten entstehen. Dies wird während der Adapter-Einrichtung konfiguriert.
- Wenn Sie benutzerdefinierte Segmente in wiederkehrenden Campaigns verwenden, muss der Campaign-Name anstelle der Campaign-ID verwendet werden, da sich die IDs bei jedem Durchlauf der Campaign ändern.
- Zu den verfügbaren Kommunikationskanälen innerhalb jeder Punchh-Geschenk-Campaign gehören Rich-Nachrichten, Push-Benachrichtigungen, SMS und E-Mail.
- Nachdem Nutzer:innen von Braze an ein benutzerdefiniertes Punchh-Segment gesendet wurden, können sie nicht mehr daraus entfernt werden. Es können nur neue Gäste zu einem bestehenden benutzerdefinierten Segment hinzugefügt werden. Wenn Gäste aus einem bestehenden benutzerdefinierten Punchh-Segment entfernt werden müssen, muss eine neue Webhook-Campaign in Braze erstellt werden, um Nutzer:innen an ein neues benutzerdefiniertes Punchh-Segment zu senden.

## Integration

Punchh bietet verschiedene Endpunkte an, die Braze-Kund:innen zur Verfügung stehen, um der Punchh-Plattform über die folgenden Punchh-API-Endpunkte externe IDs hinzuzufügen. Nachdem die externen IDs hinzugefügt wurden, erstellen Sie einen Adapter in Punchh, geben Ihre Braze-Zugangsdaten an und wählen die Ereignisse aus, die Sie synchronisieren möchten. Anschließend können Sie die Punchh-Segment-ID verwenden, um einen Punchh-Webhook zu erstellen, der die Kundensynchronisierung in einer Canvas Journey triggert.

Beachten Sie, dass die Punchh `user_id` und die Braze `external_id` in beiden Plattformen verfügbar sein müssen, damit die Integration korrekt synchronisiert werden kann.
- Ereignisse, die von Punchh an Braze gesendet werden, enthalten die Braze `external_id` als Bezeichner. Wenn Punchh so konfiguriert ist, dass die `external_source_id` verwendet wird, wird dieser Wert als Braze `external_id` gesetzt. Andernfalls wird bei der Integration standardmäßig die Punchh `user_id` als Braze `external_id` gesetzt.
- Um Webhooks von Braze an Punchh zu senden, muss die Punchh `user_id` im Braze-Kundenprofil verfügbar sein. Wenn die Punchh `user_id` nicht als Braze `external_id` verwendet wird, sollte sie als angepasstes Attribut „punchh_user_id“ festgelegt werden.

### 1. Schritt: Einrichten von externen ID-Ingestion-Endpunkten (optional) {#step-1-set-up-external-id-ingestion-endpoints-optional}

Externe IDs von Braze können über die folgenden Endpunkte für neue und bestehende Punchh-Nutzer:innen hinzugefügt werden.

{% alert important %}
Die Werte in den Feldern `external_source` und `external_source_id` müssen für Punchh eindeutig sein und dürfen nicht mit bestehenden Profilen verknüpft sein.
{% endalert %}

1. Neue Punchh-Nutzer:innen<br>
Erstellen Sie neue Nutzer:innen in Punchh mit einem Punchh-Registrierungsendpunkt unter Verwendung der Felder `external_source` und `external_source_id`. Punchh ermöglicht die Übermittlung externer Bezeichner mit einem Kundenprofil über einen der folgenden Registrierungsendpunkte:
- [Mobile Signup API](https://developers.punchh.com/docs/dev-portal-mobile/2e67abf6f8e12-sign-up-register)
- [Single Sign-on Signup API](https://developers.punchh.com/docs/dev-portal-online-ordering/58f18dfdd2a3d-signup-with-email-and-password)<br><br>
2. Bestehende Punchh-Nutzer:innen <br>
Aktualisieren Sie die `external_source_id` für bestehende Punchh-Nutzer:innen. Punchh ermöglicht das Hinzufügen externer Bezeichner zu einem Profil über einen Nutzer-API-Update-Endpunkt:
- [Mobile User Update](https://developers.punchh.com/docs/dev-portal-mobile/c9b928e35a6f3-update-user-profile)
- [Single Sign-on User Update](https://developers.punchh.com/docs/dev-portal-online-ordering/eef4eef6c97a0-update-user-information)
- [Dashboard User Update](https://developers.punchh.com/docs/dev-portal-platform-functions/6351feaf591aa-update-a-user)
<br><br>
{% tabs local %}
{% tab Beispiel für die Nutzerregistrierungs-API %}
Dieses Beispiel ermöglicht es Ihnen, bei der Registrierung externe Bezeichner mit einem Kundenprofil zu senden. Dies geschieht, indem Sie `external_source` als "customer_id" und `external_source_id` als "111111111111111111" als String-Datentyp senden.

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
Dieses Beispiel ermöglicht es Ihnen, externe Bezeichner mit einem Kundenprofil zu aktualisieren. Dies geschieht, indem Sie `external_source` als "customer_id" und `external_source_id` als "111111111111111111" als String-Datentyp senden.

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

Arbeiten Sie mit Ihrem Punchh Implementation Manager:in zusammen, um diesen Adapter einzurichten.

Um die Integration von Braze und Punchh einzurichten, gehen Sie wie folgt vor:

1. Navigieren Sie im Punchh-Dashboard zu **Cockpit** > **Dashboard** > **Major Features** > **Enable Webhook Management** und schalten Sie **Enable Webhook Management** ein.<br><br>
2. Aktivieren Sie als Nächstes die Adapter, indem Sie zu **Settings** > **Webhooks Manager:in** > **Configurations** > **Show Adapters Tab** navigieren und **Show Adapters Tab** einschalten.<br><br>
3. Navigieren Sie zum **Webhooks Manager** unter dem Tab **Settings**, wählen Sie den Tab **Adapters** und klicken Sie auf **Create Adapter**. <br><br>![Punchh Webhooks Manager – Tab „Adapters“ mit ausgewähltem „Create Adapter“.]({% image_buster /assets/img/punchh/punchh1.png %})<br><br>
4. Geben Sie den Adapternamen, die Beschreibung und die Admin-E-Mail ein. Wählen Sie **Braze** als Ihren Adapter und geben Sie Ihren Braze REST-API-Endpunkt und Braze-API-Schlüssel an.<br><br>
5. Wählen Sie dann die verfügbaren Ereignisse aus, die Sie aktivieren möchten. Eine Liste dieser Ereignisse finden Sie unter [Verfügbare zu synchronisierende Ereignisse](#available-events-to-sync).<br><br>![Punchh-Adaptereinstellungen mit auswählbaren Ereignissen für die Braze-Synchronisierung.]({% image_buster /assets/img/punchh/punchh3.png %})<br><br>
6. Klicken Sie auf **Submit**, um den Webhook zu aktivieren.

## Punchh-Webhook in Braze erstellen {#create-punchh-webhook-in-braze}

Braze kann Nutzer:innen über Webhooks, die Punchh Custom Segments nutzen, zu einem Punchh-Segment hinzufügen.

1. Erstellen Sie ein benutzerdefiniertes Segment in Punchh und notieren Sie die `custom_segment_id`, die in der URL des Punchh-Segment-Dashboards angezeigt wird, wie im folgenden Beispiel gezeigt. Sowohl der klassische als auch der Beta-Segment-Builder können verwendet werden. Der Beta-Builder wird jedoch empfohlen, da der klassische Builder irgendwann eingestellt wird.<br><br>Navigieren Sie in der Punchh-Plattform zu **Guest** > **Segment** > **Custom List** > **New Custom List**.<br><br>![Punchh-Dashboard für benutzerdefinierte Segmente mit der Custom-Segment-ID in der URL.]({% image_buster /assets/img/punchh/update1.png %})<br><br>

2. Erstellen Sie eine Webhook-Kampagne in Braze und verwenden Sie den Punchh-Endpunkt zum Hinzufügen einer Nutzer:in zu einem benutzerdefinierten Segment als Webhook-URL. Hier können Sie die `custom_segment_id` aus der URL und die `user_id` als Schlüssel-Wert-Paare angeben.<br><br>![Braze-Webhook-Composer mit Punchh-Endpunkt und Schlüssel-Wert-Payload-Feldern.]({% image_buster /assets/img/punchh/punchh4.png %})<br><br>

3. Dieser Webhook kann als einzelne Campaign oder als Schritt innerhalb eines Canvas eingerichtet werden. Alternativ kann der Webhook, der Nutzer:innen zu diesem bestimmten Punchh-Segment hinzufügt, als [Template]({{site.baseurl}}/user_guide/messaging/templates/webhook_templates) eingerichtet werden, wenn er in mehreren Campaigns oder Canvases verwendet wird.<br><br>
Der `user_id`-Schlüssel innerhalb des Webhooks wird der Punchh-Nutzer:innen-ID zugeordnet. Dieser Bezeichner muss zu allen in Braze erstellten Webhooks hinzugefügt werden, um Nutzer:innen zu einem benutzerdefinierten Punchh-Segment hinzuzufügen. Das angepasste Attribut `punch_user_id` kann mithilfe von [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid#pre-formatted-variables) dynamisch als Wert für den `user_id`-Schlüssel befüllt werden. Sie können die Variable des angepassten Attributs `punchh_user_id` über das blaue „Plus“-Symbol in der Symbolleiste des Template-Textfelds einfügen.<br><br>![Braze-Webhook-Payload-Feld mit eingefügter Punchh-Nutzer:innen-ID als Liquid-Variable.]({% image_buster /assets/img/punchh/update3.png %}){: style="max-width:65%;"}<br><br>![Braze-Personalisierungsauswahl mit dem angepassten Attribut „punchh_user_id“.]({% image_buster /assets/img/punchh/update4.png %}){: style="max-width:65%;"}<br><br>

4. Nachdem der Webhook gespeichert wurde, kann er zur Synchronisierung von Nutzer:innen verwendet werden. Beispielsweise würden 136 Gäste zum benutzerdefinierten Punchh-Segment hinzugefügt, wenn diese Braze-Webhook-Campaign gestartet wird.<br><br>![Ein Beispiel für die Synchronisierung von Nutzer:innen mit dem gespeicherten Webhook dank der Integration von Braze und Punchh.]({% image_buster /assets/img/punchh/punchh6.png %})

Weitere Informationen zur Verwendung von Webhooks in Braze finden Sie unter [Webhook erstellen]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook).

## Anwendungsfälle für Campaigns {#use-case-campaigns}

### Campaign- und Canvas-Konfiguration {#campaign-and-canvas-configuration}

#### Triggering

Anwendungsfälle für Braze-Nachrichten, die durch Punchh-Ereignisse ausgelöst werden, die an Braze gesendet werden, wie z. B. Reward-Ereignisse oder Gast-Ereignisse, können als [aktionsbasierte Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery) oder Canvases erstellt werden, die durch das entsprechende Punchh-Ereignis ausgelöst werden.

Durch das Hinzufügen eines Triggers wird die Liste der in Braze erstellten Ereignisse angezeigt. Wählen Sie das Ereignis aus, das Ihre Campaign oder Ihren Canvas auslösen soll, damit die Nachricht an die Nutzer:innen gesendet wird, die das Ereignis protokolliert haben.

![Braze-Trigger-Konfiguration mit einem ausgewählten Punchh-Ereignis für eine aktionsbasierte Campaign.]({% image_buster /assets/img/punchh/update5.png %})

Es können Eigenschaftsfilter hinzugefügt werden, um das auslösende Ereignis weiter einzugrenzen. Beispielsweise sollte die Nachricht nur ausgelöst werden, wenn eine Kund:in das Ereignis „checkins_gift“ auslöst und die Ereigniseigenschaft „approved“ den Wert `true` hat. Dies ist ein optionales Feature, das möglicherweise nicht für alle Anwendungsfälle relevant ist.

#### Segmentierung {#segmentation}

In vielen Fällen können Braze Campaigns und Canvases, die durch Punchh-Ereignisse ausgelöst werden, auf die Zielgruppe „Alle Nutzer:innen“ gesetzt werden, da die Segmentierung der Nutzer:innen, die diese Ereignisse auslösen, innerhalb von Punchh erfolgt. Kund:innen, die die Zielgruppe der Nutzer:innen, die das durch das Ereignis ausgelöste Braze-Messaging erhalten, weiter verfeinern möchten, können dies tun, indem sie zusätzliche Filter und Segmente im Bereich **Target Audiences** des Campaign-Composers oder in der **Entry Audience** des Canvas-Composers hinzufügen.

### Anwendungsfälle {#use-cases}

{% tabs local %}
{% tab Registrierung %}
#### Registrierungs-Campaign {#sign-up-campaign}

Wenn Sie die Braze-Konfiguration für eine Registrierungs-Campaign mit einem angehängten Angebot nutzen, muss eine Registrierungs-Gifting-Kampagne innerhalb von Punchh und eine Willkommensnachricht in Braze konfiguriert werden.

Punchh empfiehlt, eine Ausführungsverzögerung zur Registrierungs-Campaign hinzuzufügen, damit Braze zuerst die Willkommensnachricht basierend auf dem Gast-Ereignis auslösen kann. Wenn Sie eine Folgenachricht senden möchten, die die Nutzer:innen darüber informiert, dass sie ein Geschenk erhalten haben, können Sie diese basierend auf dem Reward-Ereignis auslösen.

Bei einer Registrierungs-Campaign können alle Registrierten für das Segment verwendet werden; daher ist kein angepasstes Braze-Segment erforderlich.

Erforderliche Punchh-Konfigurationen:
- Kampagne: Registrierung
- Segment: Alle Registrierten
- Reward: Kundenauswahl
Erforderliche Ereignisse:
- Reward-Ereignis
- Gast-Ereignis
Hinweise:
- Ausführungsverzögerung, empfohlen wird eine Verzögerung von 5–10 Minuten

![Ein Nutzer:innen-Segment wird in Punchh konfiguriert, und Gäste registrieren sich für ein Kundenbindungs-Programm. Danach wird das Gast-Ereignis ausgelöst, und die Braze-Messaging-Kampagne wird getriggert. Anschließend wird die Punchh-Registrierungs-Gifting-Kampagne nach 10 Minuten ausgelöst, was das Reward-Ereignis und eine optionale Folgenachricht triggert.]({% image_buster /assets/img/punchh/usecase3.png %})
{% endtab %}

{% tab Braze-Willkommen %}
#### Braze-Willkommens-Campaign {#braze-welcome-campaign}

Wenn sich neue Nutzer:innen registrieren, sendet Punchh ein Gast-Ereignis an Braze, das die Nutzer:innen erstellt und ein angepasstes Attribut `signup_channel` sendet, das Sie verwenden können, um die Braze-Willkommens-Campaign auszulösen.

Um die Braze-Willkommens-Campaign einzurichten, führen Sie die folgenden Schritte aus:

1. Erstellen Sie in Braze eine aktionsbasierte Campaign.
2. Wählen Sie als Trigger **Change Custom Attribute Value** mit dem angepassten Attribut `signup_channel`, das auf **Any new value** gesetzt ist.
3. Fahren Sie mit der Erstellung Ihrer Campaign fort und senden Sie sie, wenn sie bereit ist!

{% endtab %}
{% tab Massenangebot %}
#### Massenangebots-Campaign {#mass-offer-campaign}

Wenn Sie eine Massenangebots-Campaign für Gifting nutzen, muss eine Massenangebots-Kampagne innerhalb von Punchh und eine Messaging-Kampagne in Braze konfiguriert werden.

Wenn Sie ein Braze-Segment für Ihre Campaign verwenden oder vor dem Gifting der Gäste auf der Punchh-Plattform eine Kommunikation von Braze senden möchten, ist ein [angepasstes Punchh-Segment]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/punchh#step-3-create-punchh-webhook-in-braze) für die Punchh-Gifting-Kampagne erforderlich.

Das Erstellen des Segments der Nutzer:innen, die dieses Angebot erhalten sollen, in Braze wird nur empfohlen, wenn Attribute verwendet werden, die innerhalb von Punchh nicht verfügbar sind. Andernfalls kann die Punchh-Segmentierung verwendet werden, und die Braze-Messaging-Kampagne wird als aktionsbasierte Campaign erstellt, die durch den Erhalt des Rewards der Nutzer:innen ausgelöst wird (das von Punchh getriggerte Reward-Ereignis).

Erforderliche Punchh-Konfigurationen:
- Kampagne: Massenangebot
- Segment: Angepasste Liste oder Kundenauswahl
- Reward: Kundenauswahl

**Verwendung von Punchh für Segmentierung und Gifting sowie Braze für Messaging:**<br>
Beispiel: Ein Rabatt von 2 $ wird an ein innerhalb von Punchh konfigurierbares Segment gesendet, wobei das Messaging über Braze erfolgt.<br>
![Ein Nutzer:innen-Segment kann in Punchh konfiguriert werden, und Nutzer:innen erhalten ein Geschenk über eine Punchh-Massenangebots-Kampagne. Anschließend wird ein Reward-Ereignis ausgelöst, und dann wird die Braze-Messaging-Kampagne getriggert.]({% image_buster /assets/img/punchh/usecase6.png %}){: style="max-width:80%;"}

**Verwendung von Braze für Segmentierung und Messaging sowie Punchh für Gifting:**<br>
Beispiel: Ein Rabatt von 2 $ und Messaging an ein Segment mit Attributen, die in Punchh nicht verfügbar sind.<br>
![Ein Nutzer:innen-Segment kann in Braze konfiguriert werden, und anschließend kann eine Nachricht vom Braze-Segment an das Braze-Segment gesendet werden. Dann werden die Nutzer:innen über einen Braze-Webhook mit Segment- und Nutzer:innen-ID an das angepasste Punchh-Segment gesendet. Danach erhalten die Nutzer:innen ein Geschenk über die Punchh-Massenangebots-Kampagne mit einem angepassten Segment. Anschließend wird das Reward-Ereignis ausgelöst.]({% image_buster /assets/img/punchh/usecase5.png %}){: style="max-width:80%;"}

**Verwendung von Braze für Segmentierung und Punchh für Gifting oder Messaging oder beides:**<br>
Beispiel: Ein Rabatt von 2 $ wird an ein Segment mit Attributen gesendet, die in Punchh nicht verfügbar sind, aber kein Messaging erforderlich ist, oder das Messaging kann über Punchh gesendet werden (beachten Sie, dass alle Gäste in Punchh vorhanden sein müssen).<br>
![Ein Nutzer:innen-Segment kann in Braze konfiguriert werden, und die Nutzer:innen werden über einen Braze-Webhook mit Segment- und Nutzer:innen-ID an das angepasste Punchh-Segment gesendet. Danach erhalten die Nutzer:innen ein Geschenk über die Punchh-Massenangebots-Kampagne mit einem angepassten Segment. Anschließend wird das Reward-Ereignis ausgelöst.]({% image_buster /assets/img/punchh/usecase4.png %})

{% endtab %}
{% tab Wiederkehrendes Massenangebot %}
#### Wiederkehrende Massenangebots-Campaign {#recurring-mass-offer-campaign}

Wenn Sie eine wiederkehrende Massenangebots-Campaign für Gifting nutzen, muss eine Massenangebots-Kampagne innerhalb von Punchh und eine Messaging-Kampagne in Braze eingerichtet werden. Ein angepasstes Punchh-Segment ist erforderlich, wenn die Kund:in die Braze-Segmentierung verwenden möchte (nur empfohlen, wenn Attribute verwendet werden, die innerhalb von Punchh nicht verfügbar sind). Andernfalls kann die Punchh-Segmentierung verwendet werden, und die Braze-Messaging-Kampagne wird basierend auf dem Reward-Ereignis ausgelöst.

Erforderliche Punchh-Konfigurationen:
- Kampagne: Wiederkehrendes Massenangebot
- Segment: Angepasste Liste oder Kundenauswahl
- Reward: Kundenauswahl
Hinweise:
- Campaign-IDs und Campaign-Namen werden als Ereigniseigenschaft im Ereignis an Braze gesendet. Wenn Sie einen Punchh-Campaign-Bezeichner in Braze verwenden möchten, um die Zielgruppe der Campaign weiter zu filtern, müssen Sie den Campaign-Namen verwenden, da sich die Campaign-IDs täglich ändern.

{% endtab %}
{% tab Post-Check-in-Angebot mit Benachrichtigung %}
#### Post-Check-in-Angebots-Campaign mit Benachrichtigung {#post-check-in-offer-campaign-with-notification}

Wenn Sie eine Post-Check-in-Angebots-Campaign nutzen, sendet Braze die Benachrichtigung über das Gifting, und wenn Gäste einen Check-in durchführen, erhalten sie das Geschenk von der Punchh-Post-Check-in-Kampagne. Daher muss eine Post-Check-in-Angebots-Kampagne innerhalb von Punchh und eine Messaging-Kampagne in Braze konfiguriert werden (falls Kund:innen über die Kampagne benachrichtigt werden sollen).

Erforderliche Punchh-Konfigurationen:
- Kampagne: Post-Check-in-Angebot
- Segment: Angepasste Liste
- Reward: Kundenauswahl

Beispiel: Eine E-Mail, die Gäste informiert, dieses Wochenende für doppelte Punkte vorbeizukommen, wird an ein Segment mit Attributen gesendet, die in Punchh nicht verfügbar sind. Punchh gewährt diesem Segment nach einem qualifizierenden Check-in Punkte und sendet optional Messaging von Braze.

![Ein Nutzer:innen-Segment wird in Braze konfiguriert, und Nachrichten werden von der Braze-Post-Check-in-Campaign gesendet. Anschließend werden die qualifizierenden Nutzer:innen über einen Braze-Webhook mit Segment- und Nutzer:innen-ID an das angepasste Punchh-Segment gesendet. Zuletzt führen die qualifizierenden Nutzer:innen im angepassten Segment einen Check-in durch und erhalten das Geschenk und eine optionale Nachricht über die Post-Check-in-Kampagne.]({% image_buster /assets/img/punchh/update7.png %})

{% endtab %}
{% tab Post-Check-in-Angebot ohne Benachrichtigung %}
#### Post-Check-in-Angebots-Campaign ohne Benachrichtigung {#post-check-in-offer-campaign-without-notification}

Wenn Sie eine Post-Check-in-Angebots-Campaign nutzen, bei der Kund:innen nicht zuerst benachrichtigt werden, wird die Kampagne ein Geschenk senden (optional mit Messaging) und eine Benachrichtigung innerhalb von Braze auslösen. Daher muss eine Post-Check-in-Angebots-Kampagne innerhalb von Punchh konfiguriert werden; eine angepasste Liste ist jedoch nicht erforderlich. Stattdessen können Sie das gewünschte Segment innerhalb von Punchh auswählen.

Erforderliche Punchh-Konfigurationen:
- Kampagne: Post-Check-in-Angebot
- Segment: Kundenauswahl
- Reward: Kundenauswahl

Beispiel: Eine Überraschungs- und Freude-Braze-Campaign wird an ein in Punchh verfügbares Segment gesendet, um Gästen für ihren Besuch zu danken und sie mit 2 $ Rabatt auf ihren nächsten Besuch zu belohnen.

![Ein qualifizierendes Nutzer:innen-Segment kann innerhalb von Punchh konfiguriert werden, und qualifizierende Nutzer:innen führen einen Check-in durch und erhalten ein Geschenk über eine Punchh-Post-Check-in-Kampagne. Danach wird ein Reward-Ereignis ausgelöst, und die Erinnerungsnachricht wird gesendet, die die Gäste über den von Braze gesendeten Reward benachrichtigt.]({% image_buster /assets/img/punchh/usecase2.png %})

{% endtab %}
{% tab Jubiläum %}
#### Jubiläums-Campaign {#anniversary-campaign}

Wenn Sie eine Jubiläums-Campaign nutzen, erhalten Nutzer:innen zuerst ein Geschenk für ihr Jubiläum von der Punchh-Kampagne. Dieses Gifting (Reward-Ereignis) löst die Messaging-Kampagne innerhalb von Braze aus, die die Nutzer:innen über das Geschenk informiert. Daher ist keine angepasste Liste erforderlich. Stattdessen können Sie das Segment und die Jubiläumseinstellungen innerhalb von Punchh auswählen.

Erforderliche Punchh-Konfigurationen:
- Kampagne: Jubiläums-Kampagne
- Segment: Kundenauswahl
- Reward: Kundenauswahl
Hinweise:
- Gifting im Monat der Registrierung
- Gültigkeitsdauer (Wie lange ist der Geburtstags-Reward gültig?)
- Wiederkehrende Kampagnen, Zeitplan erforderlich

![Ein optionales Segment kann innerhalb von Punchh erstellt werden, und qualifizierende Nutzer:innen erhalten einen Reward über eine Punchh-Jubiläums-Kampagne. Danach wird ein Reward-Ereignis ausgelöst, und die Erinnerungsnachricht wird gesendet, die die Gäste über den von Braze gesendeten Reward benachrichtigt.]({% image_buster /assets/img/punchh/usecase1.png %})

{% endtab %}
{% tab Rückruf %}
#### Rückruf-Campaign {#recall-campaign}

Wenn Sie Nutzer:innen basierend auf Inaktivität ansprechen möchten, kann eine Rückruf-Campaign verwendet werden. Die Kund:in kann das Segment und die Kampagne innerhalb von Punchh erstellen, aber Braze für das Messaging verwenden.

Wenn Sie eine in Braze erstellte Segmentierung verwenden möchten, kann ein [angepasstes Punchh-Segment]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/punchh#step-3-create-punchh-webhook-in-braze) basierend auf Inaktivität an eine wiederkehrende Massenangebots-Kampagne angehängt werden.

Erforderliche Punchh-Konfigurationen:
- Kampagne: Rückruf-Kampagne
- Segment: Kundenauswahl
- Reward: Kundenauswahl
Hinweise:
- Die Kampagne wird nach einem Zeitplan ausgeführt

![Ein optionales Segment kann innerhalb von Punchh erstellt werden, und qualifizierende Nutzer:innen erhalten einen Reward über eine Punchh-Rückruf-Kampagne. Danach wird ein Reward-Ereignis ausgelöst, und die Rückrufnachricht wird gesendet, die die Gäste über den von Braze gesendeten Reward benachrichtigt.]({% image_buster /assets/img/punchh/usecase.png %})

{% endtab %}
{% endtabs %}