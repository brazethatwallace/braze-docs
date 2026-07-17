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

Orchestrierung ist die Verbindung zwischen Decisioning Studio und Ihrer Customer-Engagement-Plattform (CEP). Sobald Ihr Decisioning Agent die optimale Aktion für jede:n Kund:in bestimmt hat, führt die Orchestrierung diese Entscheidungen aus, indem sie personalisierte Kommunikation über Ihre CEP triggert.

Stellen Sie es sich so vor:

- **Decisioning Studio** entscheidet, *was* gesendet wird und *wann* es gesendet wird
- **Ihre CEP** übernimmt, *wie* es gesendet wird

## Wählen Sie Ihre CEP {#choose-your-cep}

Der erste Schritt besteht darin, zu wählen, welche CEP Sie mit Decisioning Studio verwenden möchten. Ihre Wahl beeinflusst die Komplexität der Einrichtung und die verfügbaren Features.

### Unterstützte CEPs {#supported-ceps}

| CEP | Integrationstyp | Komplexität der Einrichtung |
|-----|-----------------|------------------|
| **Braze** | Native API-Integration (empfohlen) | Niedrig |
| **Salesforce Marketing Cloud** | API-Ereignisse + Journey Builder | Mittel |
| **Andere CEPs** | Angepasst (Empfehlungsdatei) | Hoch |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Unterstützte CEPs" }

{% alert tip %}
Wenn Sie Braze bereits als Ihre CEP verwenden, empfehlen wir die native Braze-Integration für die reibungsloseste Einrichtung.
{% endalert %}

## Voraussetzungen {#prerequisites}

Bevor Sie die Orchestrierung einrichten, sammeln Sie die folgenden Elemente basierend auf Ihrer gewählten CEP.

{% tabs %}
{% tab Braze %}

| Anforderung | Beschreibung |
|------|-------------|
| **REST-API-Schlüssel** | Ein neuer API-Schlüssel mit Berechtigungen für Nutzerdaten, Nachrichten, Campaigns, Canvas, Segmente und Templates. |
| **Braze-Dashboard-URL** | Die URL Ihrer Braze-Instanz (zum Beispiel `https://dashboard-01.braze.com`). |
| **App-ID** | Der API-Schlüssel, der mit der App verknüpft ist, die Sie tracken möchten (zu finden unter **Einstellungen** > **App-Einstellungen**). |
| **E-Mail-Anzeigename und -Adresse** | Die Absenderinformationen, die für Ihre Campaigns verwendet werden sollen (zu finden unter **Einstellungen** > **E-Mail-Einstellungen**). |
| **Basis-Templates** | Die Nachrichten-Templates, die Ihr Agent für die Orchestrierung verwenden wird. Sie erstellen API-getriggerte Campaigns für jedes Template. |
| **Testnutzer:in-ID** | Eine Nutzer:in-ID zum Testen der Integration vor dem Start. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

{% endtab %}
{% tab Salesforce Marketing Cloud %}

| Anforderung | Beschreibung |
|------|-------------|
| **App-Paket-Zugangsdaten** | Client-ID, Client Secret, Authentication Base URI, REST Base URI und SOAP Base URI aus einem installierten Paket mit Server-zu-Server-API-Integration. |
| **API-Berechtigungen** | Scopes für Kanäle, Assets, Automatisierungen, Journeys, Kontakte, Data Extensions und Tracking-Ereignisse. |
| **Data Extensions** | Sie benötigen Data Extensions für Abonnent:innen-Daten, Engagement-Daten und Empfehlungen. |
| **E-Mail-Templates** | Die Templates, die Decisioning Studio verwenden soll, mit Template-IDs für jedes einzelne. |
| **Journey-Builder-Zugang** | Zugang zum Erstellen und Aktivieren von mehrstufigen Journeys mit API-Ereignis-Einstiegsquellen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

{% endtab %}
{% tab Andere CEPs %}

Wenn Sie eine andere CEP als Braze oder Salesforce Marketing Cloud verwenden, kann Decisioning Studio über einen Empfehlungsdatei-Ansatz integriert werden:

| Element | Beschreibung |
|------|-------------|
| **Datenaufnahme-Fähigkeit** | Ihre CEP muss in der Lage sein, Empfehlungsdateien (typischerweise CSV oder JSON) aufzunehmen, die personalisierte Entscheidungen für jede:n Kund:in enthalten. |
| **Unterstützung für dynamischen Content** | Ihre Campaigns müssen das dynamische Befüllen von Feldern basierend auf Empfehlungsdaten unterstützen. |
| **Angepasste Engineering-Ressourcen** | Ihr Team muss die Integration erstellen, um Empfehlungsdateien zu lesen und Kommunikation zu triggern. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

{% endtab %}
{% endtabs %}

## Planen Sie Ihre Campaigns {#plan-your-campaigns}

Bevor Sie die Orchestrierung einrichten, berücksichtigen Sie die folgenden Details:

### Basis-Templates {#base-templates}

Ein Basis-Template ist jedes Nachrichten-Template, das Ihr Decisioning Agent verwenden könnte. Berücksichtigen Sie:

- **Wie viele Templates?** Ihr Agent kann mit einem Template oder mehreren arbeiten. Bei mehreren kann der Agent personalisieren, welches Template jede:r Kund:in erhält.
- **Welche Kanäle?** E-Mail, Push, SMS oder eine Kombination. Jeder Kanal kann separate Templates und Campaigns erfordern.
- **Welche dynamischen Elemente?** Identifizieren Sie, welche Teile Ihrer Nachricht der Agent personalisieren wird (Betreffzeilen, CTAs, Angebote, Timing usw.). Diese werden zu API-Trigger-Eigenschaften oder dynamischen Platzhaltern.

### Einstellungen zur erneuten Berechtigung {#re-eligibility-settings}

Ihre Campaigns sollten es Nutzer:innen ermöglichen, Nachrichten mehrfach zu erhalten:

- Zum Testen möchten Sie dieselbe Campaign wiederholt an dieselbe:n Nutzer:in senden
- In der Produktion kann der Agent bestimmen, dass dieselbe Campaign an aufeinanderfolgenden Tagen optimal für eine:n Nutzer:in ist

{% alert note %}
Während Sie die erneute Berechtigung zum Testen einrichten, sind Decisioning Studio Agents so konzipiert, dass sie Frequency Caps respektieren und dieselbe Campaign in der Produktion nicht mehr als einmal pro Tag an eine:n Nutzer:in senden.
{% endalert %}

### API-Trigger-Eigenschaften {#api-trigger-properties}

Für Braze-Integrationen planen Sie, welche Dimensionen Ihr Agent optimieren wird. Diese werden zu API-Trigger-Eigenschaften, die dynamische Werte in Ihre Campaigns übergeben:

| Beispieldimension | API-Trigger-Eigenschaft |
|-------------------|---------------------|
| Betreffzeile | {% raw %}`{{api_trigger_properties.${subject_line}}}`{% endraw %} |
| Call to Action | {% raw %}`{{api_trigger_properties.${cta_message}}}`{% endraw %} |
| Angebot | {% raw %}`{{api_trigger_properties.${offer_id}}}`{% endraw %} |
| Rabattbetrag | {% raw %}`{{api_trigger_properties.${discount}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="API-Trigger-Eigenschaften" }

## Einrichtung der Integration {#integration-setup}

Wählen Sie Ihre CEP aus dieser Liste aus, um mit der Einrichtung der Integration zu beginnen.

{% tabs %}
{% tab Braze %}

## Braze-Integration einrichten {#set-up-braze-integration}

Befolgen Sie diese Schritte, um einen Decisioning Studio Agent mit den Orchestrierungsfunktionen von Braze zu integrieren (das Braze-Serviceteam steht Ihnen zur Unterstützung zur Verfügung):

### Schritt 1: API-Schlüssel erstellen {#step-1-create-an-api-key}

Gehen Sie zu **Einstellungen** > **API-Schlüssel** und erstellen Sie einen neuen Schlüssel mit den folgenden Berechtigungen:

{% multi_lang_include decisioning_studio/api_key_permissions.md %}

### Schritt 2: API-getriggerte Campaigns einrichten {#step-2-set-up-api-triggered-campaigns}

Richten Sie eine API-getriggerte Campaign für jedes Basis-Template mit API-Trigger-Eigenschaften für alle optimierten Dimensionen ein.

Ein Basis-Template ist jedes Template, das der Decisioning Agent für die Orchestrierung von Nachrichten verwenden könnte. Ein Decisioning Agent kann ein Basis-Template oder mehrere haben. Im letzteren Fall wird die Auswahl des richtigen Basis-Templates für jede:n Kund:in eine der Entscheidungen sein, die der Agent personalisiert.

### Schritt 3: Erneute Berechtigung konfigurieren {#step-3-configure-re-eligibility}

Stellen Sie sicher, dass alle API-getriggerten Campaigns es Nutzer:innen ermöglichen, innerhalb von 15 Minuten erneut berechtigt zu werden.

![Diagramm zur Frequency-Cap-Konfiguration in Decisioning Studio]({% image_buster /assets/img/decisioning_studio/decisioning_studio_frequency_cap.png %})

{% alert note %}
Obwohl der Decisioning Studio Agent dieselbe Campaign nie mehr als einmal pro Tag sendet, möchten Sie die Möglichkeit haben, dieselben Campaigns zu Testzwecken mehrmals am Tag zu senden.
{% endalert %}

### Schritt 4: Dynamische Platzhalter hinzufügen {#step-4-add-dynamic-placeholders}

Diese dienen als dynamische Platzhalter für Entscheidungen, die der Decisioning Studio Agent optimiert.

#### Beispiel 1: E-Mail-Campaign {#example-1-email-campaign}

Angenommen, der Decisioning Studio Agent optimiert eine E-Mail-Campaign. Dies könnte so konfiguriert werden:

![Konfigurationsbeispiel für eine E-Mail-Campaign in Decisioning Studio]({% image_buster /assets/img/decisioning_studio/decisioning_email_example_1.png %})

Angenommen, der Agent optimiert die Auswahl von Templates und Call-to-Action-(CTA)-Nachrichten, dann sollte eine API-getriggerte Campaign für jedes Template erstellt werden, und der CTA-Abschnitt eines Templates könnte so aussehen:

![CTA-Abschnitt eines E-Mail-Templates mit dynamischen Platzhaltern]({% image_buster /assets/img/decisioning_studio/decisioning_studio_braze_email_example_2.png %})

#### Beispiel 2: Push-Campaign {#example-2-push-campaign}

Angenommen, ein Decisioning Studio Agent optimiert die Nachricht einer Push-Campaign. Dies könnte so konfiguriert werden:

![Konfigurationsbeispiel für eine Push-Campaign in Decisioning Studio]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_1.png %})

![Weitere Konfigurationsdetails für die Push-Campaign]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_2.png %})

Das Ergebnis ist die folgende Nachricht:

![Resultierende Push-Nachricht mit personalisierten Inhalten]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_3.png %})

#### Beispiel 3: SMS-Campaign {#example-3-sms-campaign}

Angenommen, der Decisioning Studio Agent optimiert Felder in einer SMS-Campaign. Dies könnte so konfiguriert werden:

![Konfigurationsbeispiel für eine SMS-Campaign in Decisioning Studio]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_1.png %})

![Weitere Konfigurationsdetails für die SMS-Campaign]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_2.png %})

Das Ergebnis ist die folgende Nachricht:

![Resultierende SMS-Nachricht mit personalisierten Inhalten]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_3.png %})

{% endtab %}
{% tab Salesforce Marketing Cloud %}

## SFMC-Integration einrichten {#set-up-sfmc-integration}

Decisioning Studio unterstützt eine native Integration mit Salesforce Marketing Cloud. Decisioning Studio triggert API-Ereignisse in eine Journey mit den Daten, die zum Befüllen dynamischer Elemente erforderlich sind.

Für detaillierte Schritte zur Konfiguration der SFMC-Integration folgen Sie den [SFMC-Anweisungen]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration) in der Decisioning Studio Go-Dokumentation.

{% endtab %}
{% tab Andere CEPs %}

## Andere CEP-Integrationen einrichten {#set-up-other-cep-integrations}

Decisioning Studio kann mit jeder Customer-Engagement-Plattform integriert werden. Dies kann jedoch einige angepasste Engineering-Arbeit von Ihrem Team erfordern, da Decisioning Studio Kommunikation nicht direkt triggern kann.

In diesem Szenario liefert der Agent eine „Empfehlungsdatei“. Diese Datei enthält Zeilen für jede:n Kund:in mit Spalten, die alle personalisierten Entscheidungen für diese:n Kund:in angeben.

Zum Beispiel die folgende Empfehlungsdatei:

![Beispiel einer Empfehlungsdatei mit personalisierten Entscheidungen pro Kund:in]({% image_buster /assets/img/decisioning_studio/decisioning_studio_custom_example_2.png %})

Könnte verwendet werden, um eine E-Mail-Campaign zu optimieren, die so aussieht:

![E-Mail-Campaign-Beispiel mit dynamischen Feldern aus der Empfehlungsdatei]({% image_buster /assets/img/decisioning_studio/decisioning_studio_custom_example_1.png %})

{% endtab %}
{% endtabs %}

## Best Practices {#best-practices}

Behalten Sie diese Best Practices im Hinterkopf, während Sie sich auf die Orchestrierung vorbereiten:

1. **Beginnen Sie mit einem engen Umfang.** Verwenden Sie zunächst einen Kanal und ein oder zwei Templates. Sie können später erweitern, wenn Sie gelernt haben, was funktioniert.
2. **Testen Sie gründlich.** Bevor Sie starten, testen Sie Ihre Integration mit einer kleinen Gruppe von Nutzer:innen, um zu überprüfen, dass dynamischer Content korrekt befüllt wird.
3. **Dokumentieren Sie Ihre Einrichtung.** Behalten Sie den Überblick über Campaign-IDs, Template-IDs, API-Schlüssel und andere Bezeichner. Sie müssen diese im Decisioning Studio-Portal referenzieren.
4. **Koordinieren Sie mit Ihrem Team.** Die Einrichtung der Orchestrierung kann Marketing-, Engineering- und Datenteams einbeziehen. Stellen Sie sicher, dass alle ihre Rolle im Prozess verstehen.
5. **Planen Sie für Feedback-Daten.** Orchestrierung umfasst das Senden von Nachrichten und das Sammeln von Engagement- und Conversion-Daten, die Ihrem Agent beim Lernen helfen. Weitere Details finden Sie unter [Bereiten Sie Ihre Daten vor]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/prepare_data).

## Nächste Schritte {#next-steps}

Nachdem Sie die Orchestrierung eingerichtet haben, fahren Sie mit dem Entwerfen Ihres Agents fort:

- [Decisioning Agents entwerfen]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/design_agents)