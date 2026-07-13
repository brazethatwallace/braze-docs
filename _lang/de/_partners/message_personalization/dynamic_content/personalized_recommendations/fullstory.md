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

Sie können die Insights von Fullstory in Braze nutzen, um Moment-für-Moment-Abbildungen des Website- oder App-Erlebnisses von Nutzer:innen zu erstellen und hochgradig kontextuelles Messaging zu liefern. Die Session Summary API von Fullstory ermöglicht die Erfassung detaillierter Metadaten über das Surfverhalten von Nutzer:innen zur Verwendung im Braze-Messaging, was besonders leistungsstark ist, wenn es in einer mehrstufigen Messaging-Journey wie einem Canvas genutzt wird.

Der Realtime-Wert der Session-Summary-Daten von Fullstory lässt sich am besten durch Connected-Content nutzen. Durch die Verwendung von Connected-Content in einem Canvas-Kontext-Schritt können Sie die Daten von Fullstory während der gesamten Canvas-Journey von Nutzer:innen speichern und in allen nachfolgenden Canvas-Schritten verwenden. Dadurch wird auch vermieden, dass diese Daten über angepasste Events oder Attribute in ein Braze-Nutzerprofil geschrieben werden müssen.

Im folgenden Beispiel werden Canvas-Kontextdaten in einem KI-Agent-Canvas-Schritt genutzt, um die optimale Nachricht zu generieren, die Nutzer:innen dazu ermutigt, einen abgebrochenen Warenkorb wieder aufzugreifen. Sie können die Daten jedoch auch nutzen, um die Nachricht direkt zu personalisieren, die Journey von Nutzer:innen über Zielgruppenpfade zu bestimmen oder die in den nachfolgenden Messaging-Schritten verwendeten Texte oder Assets festzulegen.

## Voraussetzungen {#prerequisites}

Bevor Sie beginnen, benötigen Sie Folgendes:

| Anforderung | Beschreibung |
|-----------------------|-----------------|
| Ein Fullstory Session API Autorisierungs-Token | Siehe [Schritt 1](#step-1) in dieser Anleitung. |
| Ein aktiviertes Braze Connected-Content-Autorisierungs-Token | Siehe den Hinweis zu Early Access in diesem Abschnitt. |
| Ein Braze-Canvas-Kontext-Schritt | Siehe den Hinweis zu Early Access in diesem Abschnitt. |
| Aktivierter Braze-KI-Agent-Schritt | Siehe den Hinweis zu Early Access in diesem Abschnitt. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

{% alert important %}
Braze Agents, Canvas-Kontext und Connected-Content-Autorisierungs-Token befinden sich alle im Early Access. Wenn Sie diese Lösung nutzen möchten, sprechen Sie mit Ihrem Braze-CSM über die Aktivierung dieser Tools.
{% endalert %}

## Fullstory integrieren {#integrate-fullstory}

### Schritt 1: Fullstory für die Aktivierung der Session Summary API einrichten {#step-1}

#### Schritt 1.1: Authentifizierungs-Token für den Session Summary API-Endpunkt abrufen {#step-11-retrieve-the-authentication-token-for-the-session-summary-api-endpoint}

So erstellen Sie einen [Fullstory API-Schlüssel](https://developer.fullstory.com/server/authentication/):

1. Navigieren Sie in Fullstory zu **Settings** > **API Keys**.
2. Wählen Sie die Berechtigungsstufe **Standard** aus.
3. Kopieren Sie den Schlüsselwert sofort, da er nur einmal angezeigt wird.

#### Schritt 1.2: Eine Session-Summary-Profil-ID erstellen {#step-12-create-a-session-summary-profile-id}

Folgen Sie der [Anleitung von Fullstory](https://developer.fullstory.com/anywhere/activation/ai-session-summary-api/#step-1-creating-and-managing-summary-profiles) und erstellen Sie ein Session-Summary-Profil über den entsprechenden Endpunkt. Hier legen Sie fest, welche Art von Daten die Session-Summary-Antwort an Braze liefern soll.

In der Antwort auf diese Anfrage stellt Fullstory eine Session-Profil-ID bereit. Diese Profil-ID ist eine Schlüsselkomponente des Connected-Content-Anfragekörpers, der im folgenden Anwendungsfall verwendet wird.

### Schritt 2: Connected-Content-Token-Authentifizierung erstellen {#step-2-create-the-connected-content-token-authentication}

1. Navigieren Sie in Braze zu **Settings** > **Workspace Settings** > **Connected Content** > **Add Credential** > **Token Authentication**.
2. Benennen Sie die Authentifizierung `fullstory`.
3. Fügen Sie den Header-Schlüssel „Authorization“ hinzu. Geben Sie den Header-Wert ein, den Fullstory im vorherigen Schritt bereitgestellt hat.
4. Geben Sie unter **Allowed Domain** den Wert **api.fullstory.com** ein.

![Screenshot von Braze mit den Feldern „Zugangsdaten bearbeiten“]({% image_buster /assets/img/fullstory/1.png %}){: style="max-width:50%;"}

## Anwendungsfälle {#use-cases}

### Dynamische Nachrichten-Journeys erstellen {#create-dynamic-message-journeys}

Mit den [Activation Streams](https://help.fullstory.com/hc/en-us/articles/360045134554-Streams) von Fullstory können Sie Braze-Canvases unmittelbar nach wichtigen Interaktionen von Nutzer:innen triggern. Die Stärke dieser Integration liegt in der eindeutigen `client_session_id` (zugänglich über {% raw %}`{{canvas_entry_properties.${client_session_id}}}`{% endraw %}), die das System automatisch von Fullstory an Braze weitergibt. Diese ID dient als Schlüssel, der es Braze ermöglicht, die vollständige Session Summary dessen abzurufen, was Nutzer:innen erlebt haben.

Indem Sie Canvas-Kontext-Schritte und Connected-Content nutzen, können Sie diese ID verwenden, um eine API-Anfrage an Fullstory zu stellen, die Sitzungsdaten abzurufen und sie als Variable für die spätere Verwendung in der Journey zu speichern.

![Braze-Canvas-Kontext-Schritt, der zeigt, wie die Kontextvariable „summary_result“ erstellt und mit einem Connected-Content-Aufruf an Fullstory gefüllt wird, um eine Session Summary abzurufen]({% image_buster /assets/img/fullstory/2.png %})

Verwenden Sie mit dem zuvor erstellten Autorisierungs-Token die folgende Anfragestruktur, um die Session-Summary-Daten abzurufen.

{% raw %}
```bash
{% connected_content https://api.fullstory.com/v2/sessions/{{canvas_entry_properties.${client_session_id} | url_encode}}/summary?config_profile=[YOUR-FULLSTORY-PROFILE-ID] :auth_credentials fullstory :save summary_result %}
{{summary_result | as_json_string }}
```
{% endraw %}

{% alert note %}
Die Antwort wird als Liquid-Tag {% raw %}`{{context.${summary_result}.response}}`{% endraw %} gespeichert. Verwenden Sie diesen Context-Tag in nachfolgenden Canvas-Schritten.
{% endalert %}

In diesem Stadium kann der Canvas auf die Antwort des Connected-Content-Aufrufs zugreifen, die die gesamte Nachrichten-Payload für die Sitzung von Nutzer:innen enthält.

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

Sie können alle im obigen Objekt verfügbaren Daten nutzen, indem Sie den Context-Liquid-Tag später in der Canvas-Journey von Nutzer:innen verwenden. Die folgenden Schritte zeigen, wie Sie diese Daten in einem [Agent]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/agent_step)-Schritt verwenden können.

{% alert note %}
Um unerwartetes Verhalten zu vermeiden, fügen Sie nach dem Kontext-Schritt einen Zielgruppenpfad-Schritt ein, der Nutzer:innen aus dem Kontext herausnehmen kann, wenn ihr Context-Tag leer ist – was bedeutet, dass der Connected-Content-Aufruf fehlgeschlagen ist oder keine Informationen zurückgegeben hat.

![Der Zielgruppenpfad-Schritt in Braze]({% image_buster /assets/img/fullstory/3.png %})

{% endalert %}

### Passende Texte erstellen {#produce-appropriate-copy}

Indem Sie einen [Agent-Schritt]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents) in einem von Fullstory getriggerten Canvas erstellen und den in diesem Abschnitt beschriebenen Kontext-Schritt einbinden, können Sie die Session-Summary-Daten von Fullstory im Agenten referenzieren.

In diesem Beispiel verwenden Sie diese Daten, um dem Braze-Agenten die Möglichkeit zu geben, passende Nachrichtentexte für eine Content-Card zu generieren, die Nutzer:innen dazu ermutigen kann, zu ihrem abgebrochenen Warenkorb zurückzukehren.

![Screenshot des Braze-Agent-Context-Creators mit der Eingabeaufforderung]({% image_buster /assets/img/fullstory/4.png %})

Verwenden Sie für den in diesem Schritt erstellten Context-Liquid-Tag denselben Namen wie für den Context-Liquid-Tag, der im zuvor erstellten KI-Agent-Schritt verwendet wurde.

Die für Ihren Anwendungsfall erforderliche Eingabeaufforderung variiert. Best Practices für die Erstellung effektiver Agent-Eingabeaufforderungen finden Sie unter [Anweisungen schreiben]({{site.baseurl}}/user_guide/brazeai/agents/reference#writing-instructions).

Wählen Sie in Ihrem Canvas einen KI-Agent-Schritt und dann den **Session Context**-Agenten aus dem Dropdown-Menü aus. Speichern Sie die Ausgabe als Variable – in diesem Fall „message“ –, die Sie mit dem Liquid-Tag {% raw %}`{{context.${message}.message}}`{% endraw %} in den Nachrichtentext einfügen können.

![Screenshot des Braze-Agent-Context-Canvas-Schritts mit der Eingabeaufforderung]({% image_buster /assets/img/fullstory/5.png %})

Erstellen Sie einen Nachrichten-Schritt, der den vom KI-Agenten erstellten Text nutzt. Verwenden Sie in diesem Schritt den Liquid-Tag.

{% alert important %}
Die Session Summary API von Fullstory kann sensible, identifizierbare Nutzerdaten zurückgeben. Um die Einhaltung von Vorschriften im Umgang mit PII (personenbezogene Daten) zu gewährleisten, stellen Sie sicher, dass Ihre Fullstory-Datenerfassungsregeln PII ausschließen, bevor Sie diesen Anwendungsfall nutzen.
{% endalert %}