---
nav_title: DOTS.ECO
article_title: DOTS.ECO
description: "Dieser Referenzartikel beschreibt die Integration von Braze und DOTS.ECO."
alias: /partners/dots.eco/
page_type: partner
search_tag: Partner
---

# DOTS.ECO

> Mit [DOTS.ECO](https://dots.eco) können Sie Nutzer:innen mit nachvollziehbaren digitalen Zertifikaten für ihren realen Umwelteinfluss belohnen. Jedes Zertifikat kann Metadaten wie eine teilbare Zertifikats-URL und eine Bild-URL enthalten, sodass Nutzer:innen ihren Wirkungsnachweis einsehen (und wieder aufrufen) können.

_Diese Integration wird von DOTS.ECO gepflegt._

## Über diese Integration {#about-this-integration}

Braze und DOTS.ECO verbinden Customer-Engagement-Journeys mit realen Impact-Rewards. Von einem Braze-Canvas- oder Campaign-Schritt aus können Sie eine Anfrage zur Erstellung eines DOTS.ECO-Zertifikats mithilfe von Connected-Content auslösen. DOTS.ECO gibt Zertifikats-Metadaten (wie `certificate_url` und `certificate_image_url`) zurück, die Sie im Kundenprofil als angepasste Attribute speichern und über Kanäle wie In-App-Nachrichten, Content Cards und Push-Benachrichtigungen wiederverwenden können.

## Anwendungsfälle {#use-cases}

- Triggern Sie ein Wirkungszertifikat, wenn Nutzer:innen ein wichtiges Ereignis abschließen (Kauf, Levelabschluss, Abo, Empfehlung).
- Zeigen Sie ein personalisiertes Zertifikatsbild in einer In-App-Nachricht an, nachdem der Connected-Content-Schritt erfolgreich war.
- Fügen Sie eine Content-Card „Ihr Zertifikat anzeigen“ mit der Zertifikats-URL für den späteren Zugriff hinzu.
- Speichern Sie Zertifikats-Metadaten (wie `certificate_url`, `certificate_image_url`, `certificate_header` und `greeting`) als angepasste Attribute zur Wiederverwendung in zukünftigen Nachrichten.
- Weisen Sie Zertifikate unter Verwendung einer Remote-Nutzer-ID zu, sodass Nutzer:innen ihre Wirkung später beanspruchen und einsehen können.
- Führen Sie A/B-Tests zu Impact-Messaging durch (unterschiedliche Texte/Bilder), während Sie denselben DOTS.ECO-Nutzeraktualisierungsfluss beibehalten.


## Voraussetzungen {#prerequisites}

Bevor Sie beginnen, benötigen Sie Folgendes:

| Voraussetzung | Beschreibung |
|---|---|
| DOTS.ECO-Konto | Zugang zu einem DOTS.ECO-Konto. |
| DOTS.ECO-Zugangsdaten | Für die Anfrage in diesem Artikel benötigen Sie ein DOTS.ECO-App-Token, einen API-Schlüssel und eine Zuordnungs-ID. Um diese abzurufen, wenden Sie sich an Ihren DOTS.ECO-CSM. |
| Braze-REST-API-Schlüssel | Ein Braze-REST-API-Schlüssel mit `users.track`-Berechtigungen. Erstellen Sie diesen Schlüssel im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel**. |
| Braze-REST-Endpunkt | [Ihre REST-Endpunkt-URL]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## DOTS.ECO integrieren {#integrating-dotseco}

### 1. Schritt: Canvas erstellen und einen Nutzeraktualisierungsschritt hinzufügen {#step-1-create-a-canvas-and-add-a-user-update-step}

Erstellen Sie im Braze-Dashboard ein neues Canvas, das triggert, wenn Nutzer:innen ein Schlüsselereignis abschließen (z. B. einen Kauf, ein Abo oder einen Meilenstein).

Fügen Sie direkt nach dem Eingangsschritt einen Nutzeraktualisierungsschritt hinzu. Dieser Schritt wird verwendet, um die DOTS.ECO-API über Connected-Content aufzurufen und die zurückgegebenen Zertifikatsdaten im Kundenprofil zu speichern.

Verwenden Sie diesen Schritt, um die DOTS.ECO-API über Connected-Content aufzurufen und die zurückgegebenen Zertifikatsdaten im Kundenprofil zu speichern.

### 2. Schritt: Erweitertes JSON verfassen – POST-Anfrage an DOTS.ECO mit Connected-Content stellen {#step-2-compose-advanced-json-make-a-post-request-to-dotseco-using-connected-content}

Wechseln Sie im Schritt **Nutzeraktualisierung** zum **Advanced JSON Editor** und verwenden Sie Connected-Content, um eine POST-Anfrage an die DOTS.ECO-Zertifikats-API zu stellen.

Verwenden Sie den `capture`-Tag und eine Connected-Content-Anfrage, um den Zertifikats-Endpunkt von DOTS.ECO aufzurufen. Speichern Sie dann die Antwort als angepasste Attribute im Kundenprofil.

**Connected-Content- und Nutzeraktualisierungsbeispiel**
{% raw %}
```
{% capture post_body %}
{
  "remote_user_email": "{{${email_address} | default: 'braze+user@example.com'}}",
  "app_token": "YOUR_DOTS.ECO_APP_TOKEN",
  "impact_qty": 1,
  "remote_user_id": "{{${user_id} | default: ${braze_id}}}",
  "allocation_id": "YOUR_DOTS.ECO_ALLOCATION_ID"
}
{% endcapture %}

{% connected_content https://impact.dots.eco/api/v1/certificate/add?format=sdk
  :method post
  :headers { "auth-token": "YOUR_DOTS.ECO_AUTH_TOKEN" }
  :body {{post_body}}
  :content_type application/json
  :save result
%}

{
  "attributes": [
    {
      "certificate_image_url": "{{result.certificate_image_url}}",
      "certificate_url": "{{result.certificate_url}}",
      "certificate_id": "{{result.certificate_id}}"
    }
  ]
}
```
{% endraw %}

Senden Sie die Anfrage an `https://impact.dots.eco/api/v1/certificate/add?format=sdk`.

![DOTS.ECO-Nutzeraktualisierungsschritt.]({% image_buster /assets/img/dots_eco/dotseco_user_update.png %})

{% alert important %}
Diese Integration verwendet Connected-Content innerhalb eines Canvas-Schrittes zur **Nutzeraktualisierung**, um die DOTS.ECO-API aufzurufen. Testen Sie Anfragen zunächst mit einem API-Client (z. B. Postman), um Ihr Token und die Nutzdaten zu validieren.
{% endalert %}

### 3. Schritt: Das Zertifikat in Nachrichten anzeigen {#step-3-display-the-certificate-in-messages}

Wenn die Zertifikatsattribute im Kundenprofil gespeichert sind, können sie in nachgelagerten Canvas-Nachrichtenschritten referenziert werden.

![DOTS.ECO-Fluss.]({% image_buster /assets/img/dots_eco/dots.eco_flow.png %})

![DOTS.ECO-Nachrichtenschritt.]({% image_buster /assets/img/dots_eco/dotseco_messages.png %})

![DOTS.ECO-Abschnitt „Nachrichten verfassen“.]({% image_buster /assets/img/dots_eco/dotseco_messages_compose.png %})

Zum Beispiel:
- Zeigen Sie das Zertifikatsbild in einer In-App-Nachricht mit {% raw %}`{{custom_attribute.${certificate_image_url}}}`{% endraw %} an.
- Verlinken Sie auf das gehostete Zertifikat mit {% raw %}`{{custom_attribute.${certificate_url}}}`{% endraw %}.

![DOTS.ECO-Klickverhalten bei Nachrichten.]({% image_buster /assets/img/dots_eco/dotseco_messages_compose_onclickbehavior.png %})


Damit können Sie In-App-Nachrichten, Content Cards oder Push-Benachrichtigungen mit einer Wirkungsbestätigung personalisieren.

## Fehlerbehebung {#troubleshooting}

Überprüfen Sie Connected-Content-Fehler im Braze-Dashboard unter **Einstellungen** > **Nachrichten-Aktivitätsprotokoll**.

- **Connected-Content gibt leere Ergebnisse zurück**: Stellen Sie sicher, dass `:save result` gesetzt ist und dass Sie auf die erwarteten Antwortfelder verweisen.
- **Attribute werden im Nachrichtenschritt nicht angezeigt**:
  - Stellen Sie sicher, dass die Namen der angepassten Attribute in Braze genau mit den Attributen übereinstimmen, die Sie im Nutzeraktualisierungsschritt festgelegt haben.
  - Verwenden Sie im Nutzeraktualisierungsschritt den Tab **Vorschau und Test**, um zu bestätigen, dass die Attribute befüllt werden. Senden Sie dann einen Test an eine:n Nutzer:in und bestätigen Sie, dass die Attribute in deren Kundenprofil gespeichert sind.
- **`422`-Fehler (nicht verarbeitbare Entität)**: Stellen Sie sicher, dass Ihr App-Token und die Impact-Menge gültig sind.
- **`401`-Fehler**: Stellen Sie sicher, dass das Auth-Token vorhanden und korrekt ist.
- **Keine Bildvorschau im Nachrichtenschritt**: Wählen Sie im Nutzeraktualisierungsschritt **Test an Nutzer:in senden** und zeigen Sie dann eine Vorschau der Nachricht mit derselben/demselben Nutzer:in an.