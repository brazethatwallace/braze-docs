---
nav_title: Fullstory
article_title: Fullstory
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Fullstory."
alias: /partners/fullstory/
page_type: partner
search_tag: Partner
---

# Fullstory

> Die Plattform für Verhaltensdaten von [Fullstory](https://www.fullstory.com/) hilft Technologieführern, bessere und fundiertere Entscheidungen zu treffen. Durch das Einspeisen digitaler Verhaltensdaten in ihren Analytics-Stack erschließt die patentierte Technologie von Fullstory die Leistungsfähigkeit hochwertiger Verhaltensdaten im großen Maßstab und verwandelt jeden digitalen Besuch in umsetzbare Insights.

*Diese Integration wird von Fullstory gepflegt.*

## Über diese Integration {#about-this-integration}

Sie können Fullstory-Insights in Braze nutzen, um ein lückenloses Bild des Website- oder App-Erlebnisses Ihrer Nutzer:innen zu erstellen und so hochgradig kontextuelles Messaging zu ermöglichen. Die Session Summary API von Fullstory ermöglicht es, detaillierte Metadaten zum Browsing-Verhalten von Nutzer:innen zu erfassen und in Braze-Nachrichten zu verwenden. Das ist besonders leistungsstark, wenn es in einer mehrstufigen Messaging-Journey wie einem Canvas eingesetzt wird.

Der Realtime-Wert der Session-Summary-Daten von Fullstory lässt sich am besten über Connected-Content nutzen. Indem Sie Connected-Content in einem Canvas-Context-Schritt verwenden, können Sie die Daten von Fullstory über die gesamte Canvas-Journey von Nutzer:innen hinweg speichern und in allen nachfolgenden Canvas-Schritten verwenden. So entfällt auch die Notwendigkeit, diese Daten über angepasste Events oder Attribute in ein Braze-Nutzerprofil zu schreiben.

Im folgenden Beispiel werden Canvas-Context-Daten in einem Agent-AI-Canvas-Schritt genutzt, um die optimale Nachricht zu generieren, die Nutzer:innen dazu ermutigt, einen abgebrochenen Warenkorb wieder aufzugreifen. Sie können die Daten jedoch auch nutzen, um die Nachricht direkt zu personalisieren, die Journey von Nutzer:innen über Zielgruppenpfade zu steuern oder den Text bzw. die Assets in nachfolgenden Messaging-Schritten festzulegen.

## Voraussetzungen {#prerequisites}

Bevor Sie beginnen, benötigen Sie Folgendes:

|Voraussetzung     | Beschreibung |
|-----------------------|-----------------|
| Ein Fullstory Session API Authorization Token   | Siehe Schritt 1 in diesem Leitfaden. |
| Ein aktiviertes Braze Connected-Content Authorization Token | Siehe den Hinweis zum Early Access in diesem Abschnitt. |
| Ein Braze-Canvas-Context-Schritt | Siehe den Hinweis zum Early Access in diesem Abschnitt. |
| Ein aktivierter Braze AI Agent-Schritt | Siehe den Hinweis zum Early Access in diesem Abschnitt. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Fullstory integrieren {#integrate-fullstory}

### Schritt 1: Fullstory für die Session Summary API einrichten {#step-1}

#### Schritt 1.1: Authentifizierungstoken für den Session Summary API-Endpunkt abrufen {#step-11-retrieve-the-authentication-token-for-the-session-summary-api-endpoint}

So erstellen Sie einen [Fullstory API-Schlüssel](https://developer.fullstory.com/server/authentication/):

1. Gehen Sie in Fullstory zu **Settings** > **API Keys**.
2. Wählen Sie die Berechtigungsstufe **Standard** aus.
3. Kopieren Sie den Schlüsselwert sofort, da er nur einmal angezeigt wird.

#### Schritt 1.2: Session-Summary-Profil-ID erstellen {#step-12-create-a-session-summary-profile-id}

Erstellen Sie gemäß der [Anleitung von Fullstory](https://developer.fullstory.com/anywhere/activation/ai-session-summary-api/#step-1-creating-and-managing-summary-profiles) ein Session-Summary-Profil über den dafür vorgesehenen Endpunkt. Hier legen Sie fest, welche Art von Daten die Session-Summary-Antwort an Braze liefern soll.

In der Antwort auf diese Anfrage stellt Fullstory eine Session-Profil-ID bereit. Diese Profil-ID ist ein wesentlicher Bestandteil des Connected-Content-Anfragekörpers, der im folgenden Anwendungsfall verwendet wird.

### Schritt 2: Connected-Content-Token-Authentifizierung erstellen {#step-2-create-the-connected-content-token-authentication}

1. Gehen Sie in Braze zu **Settings** > **Workspace Settings** > **Connected Content** > **Add Credential** > **Token Authentication**.
2. Benennen Sie die Authentifizierung `fullstory`.
3. Fügen Sie den Header-Schlüssel „Authorization“ hinzu. Geben Sie den Header-Wert ein, den Fullstory im vorherigen Schritt bereitgestellt hat.
4. Geben Sie unter **Allowed Domain** den Wert **api.fullstory.com** ein.

![Screenshot von Braze mit den Feldern „Edit Credential“]({% image_buster /assets/img/fullstory/1.png %}){: style="max-width:50%;"}

## Anwendungsfälle {#use-cases}

### Dynamische Nachrichten-Journeys erstellen {#create-dynamic-message-journeys}

Mit den [Activation Streams](https://help.fullstory.com/hc/en-us/articles/360045134554-Streams) von Fullstory können Sie Braze Canvases unmittelbar nach wichtigen Nutzerinteraktionen triggern. Die Stärke dieser Integration liegt in der eindeutigen `client_session_id` (zugänglich über {% raw %}`{{canvas_entry_properties.${client_session_id}}}`{% endraw %}), die das System automatisch von Fullstory an Braze übergibt. Diese ID fungiert als Schlüssel und ermöglicht es Braze, die vollständige Sitzungszusammenfassung dessen abzurufen, was die Nutzer:innen erlebt haben.

Durch die Nutzung von Canvas-Context-Schritten und Connected-Content können Sie diese ID verwenden, um eine API-Anfrage an Fullstory zu senden, die Sitzungsdaten abzurufen und sie als Variable für die spätere Verwendung im Journey zu speichern.

![Braze-Canvas-Context-Schritt, der zeigt, wie die Kontextvariable „summary_result“ erstellt und mit einem Connected-Content-Aufruf an Fullstory befüllt wird, um eine Sitzungszusammenfassung abzurufen]({% image_buster /assets/img/fullstory/2.png %})

Verwenden Sie mit dem zuvor erstellten Autorisierungs-Token die folgende Anfragestruktur, um die Daten der Sitzungszusammenfassung abzurufen.

{% raw %}
```bash
{% connected_content https://api.fullstory.com/v2/sessions/{{canvas_entry_properties.${client_session_id} | url_encode}}/summary?config_profile=[YOUR-FULLSTORY-PROFILE-ID] :auth_credentials fullstory :save summary_result %}
{{summary_result | as_json_string }}
```
{% endraw %}

{% alert note %}
Die Antwort wird als Liquid-Tag {% raw %}`{{context.${summary_result}.response}}`{% endraw %} gespeichert. Verwenden Sie diesen Context-Tag in nachfolgenden Canvas-Schritten.
{% endalert %}

In diesem Stadium kann der Canvas auf die Antwort des Connected-Content-Aufrufs zugreifen, die den gesamten Nachrichten-Payload für die Sitzung der Nutzer:innen enthält.

{% details Beispiel-Payload der Session Summary API %}

{% raw %}
```bash
{
    "response": {
        "primary_goal": "User attempted to update payment method.",
        "issues_encountered": [
            "Received 'invalid card number' error twice.",
            "Clicked 'Submit' button multiple times with apparent frustration (based on event patterns)."
        ],
        "final_action": "Navigated away from payment page to dashboard.",
        "reason_for_termination_suggestion": "Could not update payment method successfully.",
        "help_pages_visited": [
            "/help/payment-errors"
        ]
    },
    "response_schema": {
        "type": "OBJECT",
        "properties": {
            "primary_goal": {
                "type": "STRING",
                "description": "A summary of the user's main objective during the session."
            },
            "issues_encountered": {
                "type": "ARRAY",
                "description": "A list of problems or errors the user faced.",
                "items": {
                    "type": "STRING",
                    "description": "A description of a single issue."
                }
            },
            "final_action": {
                "type": "STRING",
                "description": "The last significant action the user took before the session ended."
            },
            "reason_for_termination_suggestion": {
                "type": "STRING",
                "description": "A suggested reason for why the user ended their session."
            },
            "help_pages_visited": {
                "type": "ARRAY",
                "description": "A list of URLs for help or documentation pages the user visited.",
                "items": {
                    "type": "STRING",
                    "description": "The URL of a help page."
                }
            }
        },
        "required": [
            "primary_goal",
            "issues_encountered",
            "final_action",
            "reason_for_termination_suggestion",
            "help_pages_visited"
        ]
    }
}
```
{% endraw %}
{% enddetails %}

Sie können alle im vorhergehenden Objekt verfügbaren Daten mithilfe des Context-Liquid-Tags später im Canvas-Journey der Nutzer:innen nutzen. Die folgenden Schritte zeigen, wie Sie diese Daten in einem [Agent]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step)-Schritt verwenden können.

{% alert note %}
Um unerwartetes Verhalten zu vermeiden, fügen Sie nach dem Context-Schritt einen Zielgruppenpfad-Schritt ein, der Nutzer:innen aus dem Context entfernen kann, wenn ihr Context-Tag leer ist – was darauf hinweist, dass der Connected-Content-Aufruf fehlgeschlagen ist oder keine Informationen zurückgegeben hat.

![Der Zielgruppenpfad-Schritt in Braze]({% image_buster /assets/img/fullstory/3.png %})

{% endalert %}

### Passenden Text erstellen {#produce-appropriate-copy}

Indem Sie einen [Agent-Schritt]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents) in einem durch Fullstory getriggerten Canvas erstellen und den in diesem Abschnitt beschriebenen Context-Schritt einbinden, können Sie die Sitzungszusammenfassungsdaten von Fullstory im Agent referenzieren.

In diesem Beispiel nutzen Sie diese Daten, damit der Braze-Agent passenden Nachrichtentext für die Verwendung in einer Content-Card generieren kann, die Nutzer:innen dazu ermutigen soll, zu ihrem abgebrochenen Warenkorb zurückzukehren.

![Screenshot des Braze-Agent-Context-Erstellers mit dem Prompt]({% image_buster /assets/img/fullstory/4.png %})

Verwenden Sie für den in diesem Schritt erstellten Context-Liquid-Tag denselben Namen wie für den Context-Liquid-Tag, der im zuvor erstellten AI-Agent-Schritt verwendet wird.

Der für Ihren Anwendungsfall erforderliche Prompt variiert. Best Practices zur Erstellung effektiver Agent-Prompts finden Sie unter [Anweisungen schreiben]({{site.baseurl}}/user_guide/brazeai/agents/reference#writing-instructions).

Wählen Sie in Ihrem Canvas einen AI-Agent-Schritt aus und wählen Sie dann den **Session Context**-Agent aus dem Dropdown. Speichern Sie die Ausgabe als Variable – in diesem Fall „message“ – die Sie mithilfe des Liquid-Tags {% raw %}`{{context.${message}.message}}`{% endraw %} in den Nachrichtentext einfügen können.

![Screenshot des Braze-Agent-Context-Canvas-Schritts mit dem Prompt]({% image_buster /assets/img/fullstory/5.png %})

Erstellen Sie einen Nachrichten-Schritt, der den vom AI-Agent erstellten Text nutzt. Verwenden Sie den Liquid-Tag in diesem Schritt.

{% alert important %}
Die Session Summary API von Fullstory kann sensible identifizierbare Nutzerdaten zurückgeben. Um die Compliance beim Umgang mit PII (personenbezogenen Daten) sicherzustellen, bestätigen Sie, dass Ihre Fullstory-Datenerfassungsregeln PII ausschließen, bevor Sie diesen Anwendungsfall nutzen.
{% endalert %}