---
nav_title: Orchestrierung einrichten
article_title: Orchestrierung einrichten
page_order: 4
page_type: reference
description: "Dieser Artikel erklärt, wie Sie die Orchestrierung für BrazeAI Decisioning Studio einrichten, einschließlich der Auswahl Ihrer CEP, der Zusammenstellung der erforderlichen Zugangsdaten und der Konfiguration Ihrer Integration."
toc_headers: h2
---

# Orchestrierung einrichten {#set-up-orchestration}

> Decisioning Agents müssen sich mit einer Customer-Engagement-Plattform (CEP) verbinden, um Kommunikation zu orchestrieren, nachdem sie Kundendaten aufgenommen und auf 1:1-Ebene personalisiert haben. Dieser Artikel beschreibt, was Sie vorbereiten müssen und wie Sie die Integration für jede unterstützte CEP konfigurieren.

## Was ist Orchestrierung? {#what-is-orchestration}

Orchestrierung ist die Verbindung zwischen Decisioning Studio und Ihrer Customer-Engagement-Plattform (CEP). Sobald Ihr Decisioning-Agent die optimale Aktion für jede:n Kund:in ermittelt hat, setzt die Orchestrierung diese Entscheidungen um, indem sie personalisierte Kommunikation über Ihre CEP auslöst.

Stellen Sie es sich so vor:

- **Decisioning Studio** entscheidet, was gesendet wird und wann es gesendet wird
- **Ihre CEP** übernimmt, wie es gesendet wird

## CEP auswählen {#choose-your-cep}

Der erste Schritt besteht darin, zu entscheiden, welche CEP Sie mit Decisioning Studio verwenden möchten. Ihre Wahl beeinflusst die Komplexität der Einrichtung und die verfügbaren Features.

### Unterstützte CEPs {#supported-ceps}

| CEP | Integrationstyp | Komplexität der Einrichtung |
|-----|-----------------|------------------|
| **Braze** | Native API-Integration (empfohlen) | Niedrig |
| **Salesforce Marketing Cloud** | API-Events + Journey Builder | Mittel |
| **Andere CEPs** | Angepasst (Empfehlungsdatei) | Hoch |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Unterstützte CEPs" }

{% alert tip %}
Wenn Sie Braze bereits als Ihre CEP verwenden, empfehlen wir die native Braze-Integration für eine möglichst reibungslose Einrichtung.
{% endalert %}

## Voraussetzungen {#prerequisites}

Bevor Sie die Orchestrierung einrichten, sammeln Sie die folgenden Elemente basierend auf Ihrer gewählten CEP.

{% tabs %}
{% tab Braze %}

| Anforderung | Beschreibung |
|------|-------------|
| **Representational State Transfer-API-Schlüssel** | Ein neuer API-Schlüssel mit Berechtigungen für Nutzerdaten, Nachrichten, Campaigns, Canvas, Segments und Templates. |
| **Braze-Dashboard-URL** | Die URL Ihrer Braze-Instanz (zum Beispiel `https://dashboard-01.braze.com`). |
| **App-ID** | Der API-Schlüssel, der mit der App verknüpft ist, die Sie tracken möchten (zu finden unter **Einstellungen** > **App-Einstellungen**). |
| **E-Mail-Anzeigename und -Adresse** | Die Absenderinformationen, die Sie für Ihre Campaigns verwenden möchten (zu finden unter **Einstellungen** > **E-Mail-Einstellungen**). |
| **Basis-Templates** | Die Nachrichten-Templates, die Ihr Agent für die Orchestrierung verwendet. Sie erstellen API-getriggerte Campaigns für jedes Template. |
| **Testnutzer:in-ID** | Eine Nutzer:in-ID zum Testen der Integration vor dem Launch. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

{% endtab %}
{% tab Salesforce Marketing Cloud %}

| Anforderung | Beschreibung |
|------|-------------|
| **App-Paket-Zugangsdaten** | Client-ID, Client Secret, Authentication Base URI, Representational State Transfer Base URI und SOAP Base URI aus einem installierten Paket mit Server-zu-Server-API-Integration. |
| **API-Berechtigungen** | Scopes für Kanäle, Assets, Automatisierungen, Journeys, Kontakte, Data Extensions und Tracking-Events. |
| **Data Extensions** | Sie benötigen Data Extensions für Abonnent:innen-Daten, Engagement-Daten und Empfehlungen. |
| **E-Mail-Templates** | Die Templates, die Decisioning Studio verwenden soll, mit Template-IDs für jedes einzelne. |
| **Journey-Builder-Zugang** | Zugang zum Erstellen und Aktivieren von mehrstufigen Journeys mit API-Event-Einstiegsquellen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

{% endtab %}
{% tab Andere CEPs %}

Wenn Sie eine andere CEP als Braze oder Salesforce Marketing Cloud verwenden, kann Decisioning Studio über einen Empfehlungsdatei-Ansatz integriert werden:

| Element | Beschreibung |
|------|-------------|
| **Datenaufnahme-Fähigkeit** | Ihre CEP muss in der Lage sein, Empfehlungsdateien (typischerweise CSV oder JSON) aufzunehmen, die personalisierte Entscheidungen für jede:n Kund:in enthalten. |
| **Unterstützung für dynamischen Content** | Ihre Campaigns müssen das dynamische Befüllen von Feldern basierend auf Empfehlungsdaten unterstützen. |
| **Eigene Engineering-Ressourcen** | Ihr Team muss die Integration aufbauen, um Empfehlungsdateien zu lesen und Kommunikation auszulösen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

{% endtab %}
{% endtabs %}

## Campaigns planen {#plan-your-campaigns}

Bevor Sie die Orchestrierung einrichten, sollten Sie die folgenden Details berücksichtigen:

### Basis-Templates {#base-templates}

Ein Basis-Template ist jedes Nachrichten-Template, das Ihr Decisioning-Agent möglicherweise verwendet. Beachten Sie:

- **Wie viele Templates?** Ihr Agent kann mit einem oder mehreren Templates arbeiten. Bei mehreren kann der Agent personalisieren, welches Template jede:r Kund:in erhält.
- **Welche Kanäle?** E-Mail, Push, Kurzmitteilungsdienst or SMS oder eine Kombination. Jeder Kanal kann separate Templates und Campaigns erfordern.
- **Welche dynamischen Elemente?** Identifizieren Sie, welche Teile Ihrer Nachricht der Agent personalisiert (z. B. Betreffzeilen, CTAs, Angebote, Timing). Diese werden zu API-Trigger or triggern-Eigenschaften oder dynamischen Platzhaltern.

### Einstellungen für erneute Berechtigung {#re-eligibility-settings}

Ihre Campaigns sollten es Nutzer:innen ermöglichen, Nachrichten mehrfach zu erhalten:

- Zum Testen senden Sie dieselbe Campaign wiederholt an dieselbe:n Nutzer:in
- In der Produktion kann der Agent bestimmen, dass dieselbe Campaign an aufeinanderfolgenden Tagen optimal für eine:n Nutzer:in ist

{% alert note %}
Während Sie die erneute Berechtigung für Tests einrichten, sind Decisioning Studio-Agents so konzipiert, dass sie Frequency Caps respektieren und dieselbe Campaign in der Produktion nicht mehr als einmal pro Tag an eine:n Nutzer:in senden.
{% endalert %}

### API-Trigger or triggern-Eigenschaften {#api-trigger-properties}

Planen Sie für Braze-Integrationen, welche Dimensionen Ihr Agent optimiert. Diese werden zu API-Trigger or triggern-Eigenschaften, die dynamische Werte an Ihre Campaigns übergeben:

| Beispieldimension | API-Trigger or triggern-Eigenschaft |
|-------------------|---------------------|
| Betreffzeile | {% raw %}`{{api_trigger_properties.${subject_line}}}`{% endraw %} |
| Call-to-Action | {% raw %}`{{api_trigger_properties.${cta_message}}}`{% endraw %} |
| Angebot | {% raw %}`{{api_trigger_properties.${offer_id}}}`{% endraw %} |
| Rabattbetrag | {% raw %}`{{api_trigger_properties.${discount}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="API-Trigger or triggern-Eigenschaften" }

## Einrichtung der Integration {#integration-setup}

Wählen Sie Ihre Customer-Engagement-Plattform aus dieser Liste aus, um mit der Einrichtung der Integration zu beginnen.

{% tabs %}
{% tab Braze %}

## Braze-Integration einrichten {#set-up-braze-integration}

Befolgen Sie diese Schritte, um einen Decisioning Studio Agent mit den Orchestrierungsfunktionen von Braze zu integrieren (das Braze-Serviceleistungen-Team steht Ihnen dabei zur Verfügung):

### Schritt 1: API-Schlüssel erstellen {#step-1-create-an-api-key}

Gehen Sie zu **Einstellungen** > **API-Schlüssel** und erstellen Sie einen neuen Schlüssel mit den folgenden Berechtigungen:

{% multi_lang_include decisioning_studio/api_key_permissions.md %}

### Schritt 2: API-getriggerte Campaigns einrichten {#step-2-set-up-api-triggered-campaigns}

Richten Sie eine API-getriggerte Campaign für jedes Basis-Template ein, mit API-Trigger or triggern-Eigenschaften für alle optimierten Dimensionen.

Ein Basis-Template ist jedes Template, das der Decisioning Agent für die Orchestrierung von Nachrichten verwenden könnte. Ein Decisioning Agent kann ein einzelnes Basis-Template oder mehrere haben – in diesem Fall ist die Auswahl des richtigen Basis-Templates für jede:n Kund:in eine der Entscheidungen, die der Agent personalisiert.

### Schritt 3: Wiederberechtigung konfigurieren {#step-3-configure-re-eligibility}

Stellen Sie sicher, dass alle API-getriggerten Campaigns es Nutzer:innen ermöglichen, innerhalb von 15 Minuten erneut berechtigt zu werden.

![Decisioning Studio Diagramm zur Frequenzbegrenzung]({% image_buster /assets/img/decisioning_studio/decisioning_studio_frequency_cap.png %})

{% alert note %}
Obwohl der Decisioning Studio Agent dieselbe Campaign nie mehr als einmal pro Tag versendet, möchten Sie zu Testzwecken die Möglichkeit haben, dieselben Campaigns mehrmals am Tag zu versenden.
{% endalert %}

### Schritt 4: Dynamische Platzhalter hinzufügen {#step-4-add-dynamic-placeholders}

Diese dienen als dynamische Platzhalter für Entscheidungen, die der Decisioning Studio Agent optimiert.

#### Beispiel 1: E-Mail-Campaign {#example-1-email-campaign}

Angenommen, der Decisioning Studio Agent optimiert eine E-Mail-Campaign. Die Konfiguration könnte folgendermaßen aussehen:

![Decisioning Studio E-Mail-Beispiel 1]({% image_buster /assets/img/decisioning_studio/decisioning_email_example_1.png %})

Wenn der Agent die Auswahl von Templates und die Call-to-Action-Nachricht (CTA) optimiert, sollte für jedes Template eine API-getriggerte Campaign erstellt werden. Der CTA-Bereich eines Templates könnte so aussehen:

![Decisioning Studio E-Mail-Beispiel 2]({% image_buster /assets/img/decisioning_studio/decisioning_studio_braze_email_example_2.png %})

#### Beispiel 2: Push-Campaign {#example-2-push-campaign}

Angenommen, ein Decisioning Studio Agent optimiert die Nachricht einer Push-Campaign. Die Konfiguration könnte folgendermaßen aussehen:

![Decisioning Studio Push-Beispiel 1]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_1.png %})

![Decisioning Studio Push-Beispiel 2]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_2.png %})

Das Ergebnis ist die folgende Nachricht:

![Decisioning Studio Push-Beispiel 3]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_3.png %})

#### Beispiel 3: Kurzmitteilungsdienst or SMS-Campaign {#example-3-sms-campaign}

Angenommen, der Decisioning Studio Agent optimiert Felder in einer Kurzmitteilungsdienst or SMS-Campaign. Die Konfiguration könnte folgendermaßen aussehen:

![Decisioning Studio SMS-Beispiel 1]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_1.png %})

![Decisioning Studio SMS-Beispiel 2]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_2.png %})

Das Ergebnis ist die folgende Nachricht:

![Decisioning Studio SMS-Beispiel 3]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_3.png %})

{% endtab %}
{% tab Salesforce Marketing Cloud %}

## SFMC-Integration einrichten {#set-up-sfmc-integration}

Decisioning Studio unterstützt eine native Integration mit Salesforce Marketing Cloud. Decisioning Studio triggert API-Ereignisse in einer Journey mit den Daten, die zum Befüllen dynamischer Elemente erforderlich sind.

{% alert important %}
Für Ihre Konfiguration müssen API-IDs in Großbuchstaben eingegeben werden. Dies umfasst Journey-IDs, Campaign-IDs und alle anderen Bezeichner. Wenn API-IDs in Kleinbuchstaben eingegeben werden, Ihre SFMC-Daten jedoch UUIDs in Großbuchstaben enthalten, stimmen die Ereignisfilter nicht überein und die Berichtsmetriken werden nicht korrekt befüllt.
{% endalert %}

{% endtab %}
{% tab Andere CEPs %}

## Andere CEP-Integrationen einrichten {#set-up-other-cep-integrations}

Decisioning Studio kann mit jeder Customer-Engagement-Plattform integriert werden. Dies kann jedoch einige individuelle Entwicklungsarbeit von Ihrem Team erfordern, da Decisioning Studio Kommunikation nicht direkt Trigger or triggern or triggern kann.

In diesem Szenario liefert der Agent eine „Empfehlungsdatei“. Diese Datei enthält Zeilen für jede:n Kund:in mit Spalten, die alle personalisierten Entscheidungen für diese:n Kund:in angeben.

Zum Beispiel könnte die folgende Empfehlungsdatei:

![Decisioning Studio Beispiel einer benutzerdefinierten Empfehlungsdatei]({% image_buster /assets/img/decisioning_studio/decisioning_studio_custom_example_2.png %})

verwendet werden, um eine E-Mail-Campaign zu optimieren, die folgendermaßen aussieht:

![Decisioning Studio Beispiel einer benutzerdefinierten E-Mail-Campaign]({% image_buster /assets/img/decisioning_studio/decisioning_studio_custom_example_1.png %})

{% endtab %}
{% endtabs %}

## Best Practices {#best-practices}

Behalten Sie diese Best Practices im Hinterkopf, wenn Sie sich auf die Orchestrierung vorbereiten:

1. **Beginnen Sie mit einem engen Umfang:** Verwenden Sie zunächst einen Kanal und ein oder zwei Templates. Sie können später erweitern, wenn Sie wissen, was funktioniert.
2. **Testen Sie gründlich:** Testen Sie Ihre Integration vor dem Start mit einer kleinen Gruppe von Nutzer:innen, um sicherzustellen, dass dynamischer Content korrekt befüllt wird.
3. **Dokumentieren Sie Ihr Setup:** Behalten Sie den Überblick über Campaign-IDs, Template-IDs, API-Schlüssel und andere Bezeichner. Sie benötigen diese als Referenz im Decisioning Studio-Portal.
4. **Koordinieren Sie sich mit Ihrem Team:** Das Orchestrierungs-Setup kann Marketing-, Engineering- und Daten-Teams einbeziehen. Stellen Sie sicher, dass alle ihre Rolle im Prozess verstehen.
5. **Planen Sie für Feedback-Daten:** Die Orchestrierung sendet Nachrichten und sammelt Engagement- und Konversionsdaten, die Ihrem Agenten beim Lernen helfen. Weitere Details finden Sie unter [Daten vorbereiten]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/prepare_data).

## Nächste Schritte {#next-steps}

Nachdem Sie die Orchestrierung eingerichtet haben, fahren Sie mit dem Design Ihres Agenten fort:

- [Decisioning-Agenten entwerfen]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/design_agents)