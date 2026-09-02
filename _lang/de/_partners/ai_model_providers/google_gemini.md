---
nav_title: Google Gemini
article_title: Google Gemini
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Google Gemini, die es Ihnen ermöglicht, Gemini-Modelle mit Braze zu verbinden, um sie mit angepassten KI or künstliche Intelligenz-Agenten zu verwenden."
alias: /partners/gemini/
page_type: partner
search_tag: Partner

---

# Google Gemini

> [Google Gemini](https://deepmind.google/technologies/gemini/) ist Googles Familie von KI or künstliche Intelligenz-Modellen, die fortschrittliches Denken über Text, Code und Bilder hinweg kombiniert, um Marken dabei zu helfen, intelligentere und personalisiertere Erlebnisse zu schaffen.

{% multi_lang_include alerts/important_alerts.md alert='Braze Agents' %}

_Diese Integration wird von Google gepflegt._

## Über die Integration {#about-the-integration}

Mit der Integration von Braze und Google Gemini können Sie Gemini über einen API-Schlüssel oder durch Anmeldung mit Ihrem Google-Konto mit Braze verbinden, um Gemini-Modelle beim Erstellen angepasster KI or künstliche Intelligenz-Agenten zu verwenden. Mit dieser Integration können Ihre Agenten personalisierte Texte generieren, Entscheidungen in Realtime treffen oder Katalogfelder mithilfe der Gemini-Modelle von Google Update or aktualisieren or aktualisieren.

## Voraussetzungen {#prerequisites}

| Anforderungen | Beschreibung |
|---|---|
| Google Cloud-Konto | Ein Google Cloud-Konto mit Zugriff auf die Gemini API. Sie können sich mit einem API-Schlüssel authentifizieren oder Ihr Google-Konto verbinden und ein GCP-Projekt im Braze-Dashboard auswählen. Wenn Sie Hilfe benötigen, wenden Sie sich an Ihren Administrator oder den [Google Cloud-Support](https://cloud.google.com/support). |
| Braze-Instanz | Sie finden Ihre Braze-Instanz auf der [API-Übersichtsseite]({{site.baseurl}}/api/basics#endpoints) oder über Ihre:n Braze Onboarding-Manager:in:in. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

So verbinden Sie Google Gemini mit Braze:

1. Gehen Sie im Braze-Dashboard zu **Partnerintegrationen** > **Technologie-Partner** und suchen Sie Google Gemini.
2. Wählen Sie unter **Authentication Method** entweder **API Key** oder **Connect Google Account** aus.
3. Schließen Sie die Einrichtung für die gewählte Methode ab:
   - **API Key:** Wählen Sie unter **API Type** entweder **Gemini API** oder **Gemini Enterprise Agent Platform (formerly Vertex KI or künstliche Intelligenz)** aus. Geben Sie Ihren API-Schlüssel ein. Wenn Sie Gemini Enterprise Agent Platform ausgewählt haben, geben Sie zusätzlich Ihre **Project ID** ein. Wählen Sie **Save**.
   - **Connect Google Account:** Wählen Sie **Connect Google Account**, dann **Connect Google** und melden Sie sich mit Ihrem Google-Konto an. Wählen Sie Ihr **GCP Project** aus dem Dropdown-Menü aus. Wenn sowohl Gemini API als auch Gemini Enterprise Agent Platform in diesem Projekt aktiviert sind, wählen Sie den **API Type**, den Braze verwenden soll. Wählen Sie **Save**.

{% alert note %}
**Connect Google Account** wird nur für Workspaces angezeigt, in denen diese Authentifizierungsoption aktiviert ist.
{% endalert %}

Nach dem Speichern können Sie Gemini-Modelle auswählen, wenn Sie [einen angepassten Agenten erstellen]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents) – direkt in der Agentenkonsole.

Wenden Sie sich an den [Google Cloud-Support](https://cloud.google.com/support), wenn Sie Probleme oder Fragen zu Ihrer Integration haben.