---
nav_title: Quikly
article_title: Quikly
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Quikly, einer Plattform für Dringlichkeits-Marketing, mit der Sie Conversions bei Events innerhalb einer Braze geschäftskunden Journey beschleunigen können."
alias: /partners/quikly/
page_type: partner
search_tag: Partner

---

# Quikly

> [Quikly](https://www.quikly.com), eine Plattform für Dringlichkeits-Marketing, nutzt Psychologie, um Verbraucher:innen zu motivieren, sodass Marken die Resonanz auf ihre wichtigsten Marketing-Initiativen sofort steigern können.

_Diese Integration wird von Quikly gepflegt._

## Über die Integration {#about-the-integration}

Die Partnerschaft von Braze und Quikly ermöglicht es Ihnen, Conversions bei Events innerhalb einer Braze geschäftskunden Journey zu beschleunigen. Quikly nutzt dazu die Psychologie der Dringlichkeit, um Verbraucher:innen auf unterhaltsame – und sofortige – Weise zu motivieren. Marken können Quikly beispielsweise nutzen, um sofort neue E-Mail- und SMS-Abonnent:innen direkt in Braze zu gewinnen oder andere wichtige Marketing-Ziele wie das Herunterladen Ihrer mobilen App zu fördern.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Quikly-Konto | Ein [Quikly](https://www.quikly.com)-Markenpartnerkonto ist erforderlich, um diese Partnerschaft nutzen zu können. |
| Braze REST-API-Schlüssel | Ein Braze REST-API-Schlüssel mit den Berechtigungen `users.track`, `subscription.status.set`, `users.export.ids` und `subscription.status.get`. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST-Endpunkt | [Ihre REST-Endpunkt-URL]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
| Quikly-API-Schlüssel (optional) | Ein Quikly-API-Schlüssel, der von Ihrem Client Success Manager bereitgestellt wird (nur Webhook). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Anwendungsfälle {#use-cases}

Quikly ermöglicht es Marken, die E-Mail- oder SMS-Akquise zu beschleunigen, und motiviert Abonnent:innen, First-Party-Daten direkt in Braze bereitzustellen. Sie können Braze auch verwenden, um inaktive Kund:innen mit einer Quikly-Aktivierung anzusprechen, die diese Zielgruppe reaktiviert und bindet. Darüber hinaus können Marketer diese Integration nutzen, um bestimmte geschäftskunden-Journey-Events mit einzigartigen Belohnungsstrukturen zu incentivieren.

Zum Beispiel:
 - Bauen Sie über Tage hinweg Vorfreude und Engagement auf, indem Verbraucher:innen sich für die Chance auf attraktive Rewards mit [Quikly Hype](https://www.quikly.com/urgency-marketing/platform/product-overview/hype) per Opt-in anmelden. First-Party-Daten werden automatisch an Braze übertragen.
 - Beschleunigen Sie die Gewinnung neuer E-Mail- und SMS-Abonnent:innen mit einzigartigen Realtime-Angeboten, die auf der Reaktionsgeschwindigkeit der Verbraucher:innen, dem Ranking gegenüber anderen, dem Zufallsprinzip oder dem Ablauf von Zeit oder Kontingenten basieren – mit [Quikly Swap](https://www.quikly.com/urgency-marketing/platform/product-overview/swap).
 - Motivieren Sie bestimmte Schritte in der geschäftskunden Journey mit einzigartigen Belohnungsstrukturen über Webhooks.
 - Wenden Sie angepasste Attribute oder Events auf das Nutzerprofil an, wenn Nutzer:innen an einer Quikly-Aktivierung teilnehmen.

## Integration

Im Folgenden werden vier verschiedene Integrationen beschrieben: E-Mail-Akquise, SMS-Akquise, angepasste Attribute und Webhooks. Welche Integration Sie wählen, hängt von Ihrer Quikly-Aktivierung und Ihrem Anwendungsfall ab.

{% tabs %}
{% tab E-Mail-Akquise %}

### E-Mail-Akquise {#email-acquisition}

Wenn Ihre Quikly-Aktivierungen E-Mail-Adressen oder Profildaten von Kund:innen erfassen, müssen Sie Quikly lediglich Ihren REST-API-Schlüssel und Endpunkt bereitstellen. Quikly konfiguriert Ihr Markenkonto so, dass diese Daten an Braze weitergeleitet werden. Wenn Sie zusätzliche Nutzerattribute einbeziehen möchten, erwähnen Sie dies bei der Übermittlung der API-Zugangsdaten an Quikly.

Im Folgenden finden Sie eine Übersicht, wie Quikly diesen Workflow ausführt.
1. Nach der Teilnahme an einer Quikly-Aktivierung plant Quikly eine Nutzersuche über die [Export-API]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier), um festzustellen, ob ein:e Nutzer:in mit einer bestimmten `email_address` existiert.
2. Nutzer:in protokollieren oder aktualisieren.
  - Wenn die/der Nutzer:in existiert:
    - Kein neues Profil erstellen.
    - Falls gewünscht, kann Quikly ein angepasstes Attribut im Nutzerprofil protokollieren, um anzuzeigen, dass die/der Nutzer:in an der Aktivierung teilgenommen hat.
  - Wenn die/der Nutzer:in nicht existiert:
    - Quikly erstellt über den Braze [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track) ein reines Alias-Profil, wobei die E-Mail als Nutzer-Alias festgelegt wird, um diese:n Nutzer:in in Zukunft zu referenzieren (da keine externe ID vorhanden ist).
    - Falls gewünscht, kann Quikly angepasste Events protokollieren, um anzuzeigen, dass dieses Profil an der Quikly-Aktivierung teilgenommen hat.

{% details /users/track request %}

#### Anfrage-Header {#request-headers}
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

#### Anfragetext {#request-body}
```
{
  "attributes": [{
    "_update_existing_only": false,
    "user_alias:": {
      "alias_name": "email@example.com",
      "alias_label: "email"
    },
    "email": "email@example.com"
  }]
}
```

{% enddetails %}

{% endtab %}
{% tab SMS-Akquise %}

### SMS-Abonnements {#sms-subscriptions}

Quikly-Aktivierungen können Mobilfunknummern direkt von Kund:innen erfassen und ein neues SMS-Abo einrichten. Um diese Integration zu aktivieren, stellen Sie Ihrem Quikly Client Success Manager die `subscription_group_id` zur Verfügung. Sie können auf die `subscription_group_id` einer Abo-Gruppe zugreifen, indem Sie zur Seite **Abo-Gruppe** navigieren.

Quikly führt eine Abo-Suche anhand der Telefonnummer der/des geschäftskunden durch und schreibt ihr/ihm bei der Aktivierung automatisch gut, wenn bereits ein SMS-Abo besteht. Andernfalls wird ein neues Abo eingeleitet, und nachdem der Abo-Status verifiziert wurde, wird der/dem geschäftskunden die Gutschrift erteilt.

Hier sehen Sie den vollständigen Workflow, wenn Kund:innen ihre Mobilfunknummer und Einwilligung über Quikly angeben:
1. Quikly führt eine Abo-Suche anhand des [Abo-Gruppenstatus]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status) durch, um festzustellen, ob eine bestimmte `phone` bei einer `subscription_group_id` abonniert ist. Wenn ein Abo besteht, wird der/dem Nutzer:in in der Quikly-Aktivierung gutgeschrieben. Es sind keine weiteren Maßnahmen erforderlich.
2. Quikly führt eine Nutzersuche über den [Endpunkt „Nutzerprofil nach Bezeichner exportieren“]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) durch, um festzustellen, ob ein Nutzerprofil mit einer bestimmten `email_address` existiert. Wenn kein:e Nutzer:in existiert, wird über den Braze [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track) ein reines Alias-Profil erstellt, wobei die E-Mail als Nutzer-Alias festgelegt wird, um diese:n Nutzer:in in Zukunft zu referenzieren (da keine externe ID vorhanden ist).
3. Aktualisieren Sie den Abo-Status über den [Endpunkt „Abo-Gruppenstatus der/des Nutzer:in aktualisieren“]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status).

Um bestehende Double-Opt-in-SMS-Abo-Workflows zu unterstützen, kann Quikly anstelle des oben beschriebenen Workflows ein angepasstes Event an Braze senden. In diesem Fall wird der Abo-Status nicht direkt aktualisiert, sondern das [angepasste Event triggert den Double-Opt-in-Prozess]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in), und der Abo-Status wird regelmäßig überwacht, um zu verifizieren, dass die/der Nutzer:in vollständig per Opt-in angemeldet ist, bevor die Gutschrift in der Quikly-Aktivierung erfolgt.

{% alert important %}
Braze empfiehlt, bei der Erstellung neuer Nutzer:innen über den `/users/track`-Endpunkt eine Verzögerung von etwa 2 Minuten einzuhalten, bevor Nutzer:innen der entsprechenden Abo-Gruppe hinzugefügt werden, damit Braze Zeit hat, das Nutzerprofil vollständig zu erstellen.
{% endalert %}

{% details Detaillierte /subscription/status/set-Anfrage %}
#### Anfrage-Header
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

#### Anfragetext
```
{
  "subscription_group_id": "the-id-of-the-subscription-group",
    "subscription_status": "subscribed",
    "phone": "+13135551212"
  }]
}
```

{% enddetails %}

{% endtab %}
{% tab Angepasste Attribute %}
### Angepasste Attribute {#custom-attributes}

Je nach Ihrer Braze-Implementierung möchten Sie möglicherweise, dass Events innerhalb der Quikly-Aktivierung zur weiteren Verarbeitung durch Braze kaskadiert werden. Sie können beispielsweise ein angepasstes Nutzerattribut anwenden, das darauf basiert, welche Stufe oder welcher Anreiz bei der Quikly-Aktivierung erreicht wurde, sodass Sie die entsprechende Content-Card anzeigen können, wenn Nutzer:innen Ihre App öffnen oder sich auf Ihrer Website einloggen. Quikly arbeitet direkt mit Ihnen zusammen, um diese Integrationen zu implementieren.

{% endtab %}
{% tab Webhooks %}
### Webhooks
Verwenden Sie Webhooks, um Anreize für bestimmte Events in der geschäftskunden Journey zu triggern. Wenn Sie beispielsweise ein Braze-Event für den Fall haben, dass sich Nutzer:innen bei Ihrer App anmelden, Push-Benachrichtigungen aktivieren oder Ihren Shop-Locator verwenden, können Sie einen Webhook nutzen, um ein angepasstes Angebot für diese:n Nutzer:in auf Grundlage der Konfiguration einer bestimmten Quikly-Aktivierung zu triggern. Beispieltaktiken umfassen die Belohnung der ersten X Nutzer:innen, die eine Aktion ausführen (z. B. sich bei Ihrer App anmelden), mit einem angepassten Angebot oder die Bereitstellung eines Angebots, dessen Wert mit zunehmender Zeit abnimmt, um eine sofortige Reaktion zu motivieren.

### Erstellen eines Quikly-Webhooks in Braze {#create-a-quikly-webhook-in-braze}

Um ein Quikly-Webhook-Template für künftige Campaigns oder Canvases zu erstellen, navigieren Sie in der Braze-Plattform zu **Content** > **Webhook**. Wählen Sie dann **Webhook-Template erstellen** aus.

Wenn Sie eine einmalige Quikly-Webhook-Campaign erstellen oder ein bestehendes Template verwenden möchten, wählen Sie bei der Erstellung einer neuen Campaign **Webhook** in Braze aus.

Wählen Sie **Blank Template** aus und geben Sie Folgendes für die Webhook-URL und den Anfragetext ein:
- **Webhook-URL**: https://api.quikly.com/webhook/braze
- **Anfragetext**: JSON-Schlüssel-Wert-Paare

#### Anfrage-Header und Methode {#request-headers-and-method}

Quikly benötigt einen `HTTP Header` für die Autorisierung.

- **HTTP-Methode**: POST
- **Anfrage-Header**:
  - **Authorization**: Bearer [PARTNER_AUTHORIZATION_HEADER]
  - **Content-Type**: application/json

#### Anfragetext

Wählen Sie ***JSON key/value pairs*** aus und fügen Sie die folgenden Paare hinzu:
{% raw %}
```
"q_scope": "your-activations-scope-id"
"event": "your-event-identifier"
"email": {{${email_address}}
```
{% endraw %}

### Vorschau Ihrer Anfrage {#preview-your-request}

Zeigen Sie eine Vorschau Ihrer Anfrage im Panel **Preview** an oder navigieren Sie zum Tab `Test`, wo Sie eine:n zufällige:n Nutzer:in, eine:n bestehende:n Nutzer:in auswählen oder eigene Daten anpassen können, um Ihren Webhook zu testen.

{% alert important %}
Denken Sie daran, Ihr Template zu speichern, bevor Sie die Seite verlassen! <br>Aktualisierte Webhook-Templates finden Sie in der Liste **Gespeicherte Webhook-Templates**, wenn Sie eine neue [Webhook-Campaign]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook) erstellen.
{% endalert %}

{% endtab %}
{% endtabs %}

## Support
Kontaktieren Sie Ihren Client Success Manager bei Quikly, wenn Sie Fragen haben.