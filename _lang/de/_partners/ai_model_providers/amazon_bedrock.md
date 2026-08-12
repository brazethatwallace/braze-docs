---
nav_title: Amazon Bedrock
article_title: Amazon Bedrock
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Amazon Bedrock, mit der Sie Bedrock-Modelle mit Braze verbinden können, um sie mit angepassten KI-Agenten zu verwenden."
alias: /partners/amazon_bedrock/
page_type: partner
search_tag: Partner

---

# Amazon Bedrock

> [Amazon Bedrock](https://aws.amazon.com/bedrock/) ist ein vollständig verwalteter AWS-Dienst, der über eine einheitliche API Zugang zu Foundation-Modellen führender KI-Unternehmen bietet, sodass Marken generative KI-Anwendungen auf AWS erstellen und skalieren können.

{% multi_lang_include alerts/early_access_beta_alert.md feature='The Amazon Bedrock integration' %}

## Über die Integration {#about-the-integration}

Die Integration von Braze und Amazon Bedrock ermöglicht es Ihnen, Ihre Amazon-Bedrock-Zugangsdaten mit Braze zu verbinden, damit Sie Bedrock-gehostete Modelle beim Erstellen angepasster KI-Agenten verwenden können. Mit dieser Integration können Ihre Agenten personalisierte Texte generieren, Realtime-Entscheidungen treffen oder Katalogfelder mithilfe von Modellen aktualisieren, die über Amazon Bedrock verfügbar sind.

Wenn Sie Amazon Bedrock verbinden, zeigt Braze eine kuratierte Auswahl an Bedrock-Modellen für angepasste Agenten an. Die in Braze verfügbaren Modelle können sich vom vollständigen Katalog in Ihrem AWS-Konto unterscheiden.

{% multi_lang_include alerts/important_alerts.md alert='Braze Agents' %}

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
|---|---|
| Ein AWS-Konto mit Amazon-Bedrock-Zugang | Ein AWS-Konto mit Zugang zu Amazon Bedrock in der AWS-Region, in der Ihre Modelle gehostet werden. Wenden Sie sich bei Fragen an Ihre:n Administrator:in oder den [AWS-Support](https://aws.amazon.com/support). |
| Zugang zu Amazon-Bedrock-Modellen | Zugang in Ihrem AWS-Konto zu den Bedrock-Modellen, die Sie verwenden möchten. Für einige Modelle, wie die von Anthropic, muss der Zugang in Ihrem AWS-Konto gewährt werden. Nicht alle Modelle sind in jeder AWS-Region verfügbar. |
| Authentifizierungs-Zugangsdaten | Entweder ein langfristiger [Amazon Bedrock API-Schlüssel](https://docs.aws.amazon.com/bedrock/latest/userguide/api-keys.html) oder – wenn die IAM-Rollenauthentifizierung für Ihren Workspace aktiviert ist – eine IAM-Rolle, die Braze übernehmen kann. |
| Braze-Instanz | Sie finden Ihre Braze-Instanz auf der [API-Übersichtsseite]({{site.baseurl}}/api/basics#endpoints) oder über Ihre:n Braze-Onboarding-Manager:in. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

So verbinden Sie Amazon Bedrock mit Braze:

1. Gehen Sie im Braze-Dashboard zu **Partnerintegrationen** > **Technologie-Partner** und suchen Sie nach **Amazon Bedrock**.
2. Wählen Sie unter **Authentifizierungsmethode** entweder **API-Schlüssel** oder **AWS IAM-Rolle** (sofern verfügbar).
3. Schließen Sie die Einrichtung für die gewählte Methode ab:
   - **API-Schlüssel:** Geben Sie Ihren langfristigen **Amazon Bedrock API-Schlüssel** ein. Wählen Sie die **AWS-Region** aus, in der Ihre Bedrock-Modelle gehostet werden. Wählen Sie **Speichern**.
   - **AWS IAM-Rolle:** Verwenden Sie die von Braze angezeigten Werte, um die Vertrauensrichtlinie Ihrer IAM-Rolle zu konfigurieren, und geben Sie dann die Rollendetails in Braze ein:
     1. Kopieren Sie die **Braze AWS-Konto-ID** und vertrauen Sie diesem Konto in der Vertrauensrichtlinie Ihrer IAM-Rolle.
     2. Kopieren Sie die **Braze externe ID** und fordern Sie diese in der Vertrauensrichtlinie Ihrer Rolle mit einer `sts:ExternalId`-Bedingung an. Wählen Sie **Neue externe ID generieren**, wenn Sie einen neuen Wert benötigen.
     3. Geben Sie den **AWS-Rollen-ARN** für die IAM-Rolle ein, die über Amazon-Bedrock-Berechtigungen verfügt. Der ARN muss dem Muster `arn:aws:iam::<account-id>:role/<role-name>` entsprechen.
     4. Wählen Sie die **AWS-Region** aus, in der Ihre Bedrock-Modelle gehostet werden.
     5. Wählen Sie **Speichern**.

{% alert note %}
**AWS IAM-Rolle** wird nur für Workspaces angezeigt, bei denen diese Authentifizierungsoption aktiviert ist. Bei der IAM-Rollenauthentifizierung übernimmt Braze Ihre Rolle, um kurzlebige Amazon-Bedrock-Zugangsdaten zu generieren, und speichert keinen langfristigen API-Schlüssel.
{% endalert %}

Nach dem Speichern zeigt Braze einen Verbindungsstatus mit Datum und Uhrzeit der Verbindung an. Sie können Amazon-Bedrock-Modelle auswählen, wenn Sie in der Agent Console [einen angepassten Agenten erstellen]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents).

{% alert note %}
Nicht alle Amazon-Bedrock-Modelle sind in jeder AWS-Region verfügbar. Wählen Sie eine Region, die die Modelle unterstützt, die Sie verwenden möchten. Modelle, die in Ihrer verbundenen Region nicht verfügbar sind, geben bei der Agentenausführung Fehler zurück.
{% endalert %}

Um zu bestätigen, dass die Integration funktioniert, gehen Sie zur Agent Console und erstellen Sie einen Testagenten mit einem Ihrer Bedrock-Modelle. Geben Sie eine Anweisung wie „Erzähl mir einen Witz“ ein und führen Sie einen Testaufruf durch, um zu überprüfen, ob das Modell wie erwartet antwortet.

Um die Integration zu entfernen, wählen Sie **Trennen** auf der Seite **Amazon Bedrock-Integration**.

Bei Problemen mit Ihrem Amazon-Bedrock-Konto oder Ihren Zugangsdaten wenden Sie sich an den [AWS-Support](https://aws.amazon.com/support).