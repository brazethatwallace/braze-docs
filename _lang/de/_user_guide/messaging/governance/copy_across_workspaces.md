---
nav_title: Zwischen Workspaces kopieren
article_title: Zwischen Workspaces kopieren
page_order: 3
alias: "/copying_to_workspaces/"
page_type: reference
description: "Dieser Referenzartikel bietet einen Überblick darüber, wie Sie Campaigns, Canvases und Landing-Pages in verschiedene Workspaces kopieren können."
tool:
    - Campaigns
    - Canvas
---

# Campaigns, Canvases und Landing-Pages zwischen Workspaces kopieren {#copy-campaigns-canvases-and-landing-pages-across-workspaces}

> Das Kopieren von Campaigns, Canvases und Landing-Pages zwischen Workspaces ermöglicht es Ihnen, Ihre Inhaltserstellung zu beschleunigen, indem Sie vorhandene Inhalte aus einem anderen Workspace als Ausgangspunkt verwenden. Diese Seite beschreibt, wie Sie Campaigns, Canvases und Landing-Pages in verschiedene Workspaces kopieren und listet auf, was kopiert wird und was nicht.

Wenn Sie eine Campaign, ein Canvas oder eine Landing-Page in einen anderen Workspace kopieren, bleibt die Kopie als Entwurf erhalten, bis Sie sie bearbeiten und die Campaign oder das Canvas starten bzw. die Landing-Page veröffentlichen. So können Sie Ihre erfolgreichen Messaging-Strategien beibehalten und darauf aufbauen.

{% tabs local %}
{% tab Campaigns %}

{% alert important %}
Das Kopieren von Campaigns zwischen Workspaces ist allgemein verfügbar. Kanalunterstützung für Content Cards ist derzeit nicht verfügbar.
{% endalert %}

Sie können Campaigns zwischen Workspaces für diese unterstützten Kanäle kopieren: SMS, In-App-Nachrichten, Push-Benachrichtigungen, E-Mail und Webhooks. Sie können auch E-Mail-Templates, Feature-Flags und Content Blocks kopieren. Beachten Sie, dass Multichannel-Kampagnen mit nicht unterstützten Kanälen nicht in einen anderen Workspace kopiert werden können.

So kopieren Sie eine Campaign in einen anderen Workspace:

1. Wählen Sie das <i class="fas fa-cog" aria-label="Zahnradsymbol"></i> Zahnradsymbol neben der ausgewählten Campaign.
2. Wählen Sie **In Workspace kopieren**.
3. Überprüfen und testen Sie nach dem Kopieren Ihre Campaign, um sicherzustellen, dass alle Felder ordnungsgemäß funktionieren.

{% endtab %}
{% tab Canvas %}

{% alert important %}
Das Kopieren von Canvases zwischen Workspaces ist allgemein verfügbar. Die folgenden Kanäle werden derzeit nicht unterstützt: LINE, Content Cards und WhatsApp.
{% endalert %}

Sie können Canvases zwischen Workspaces für diese unterstützten Kanäle kopieren: E-Mail, In-App-Nachrichten, Push, Webhooks und SMS.

So kopieren Sie ein Canvas in einen anderen Workspace:

1. Wählen Sie das <i class="fa-solid fa-ellipsis-vertical" aria-label="Menü"></i>&nbsp;Menü neben dem ausgewählten Canvas.
2. Wählen Sie **In Workspace kopieren**.
3. Überprüfen und testen Sie nach dem Kopieren Ihr Canvas, um sicherzustellen, dass alle Felder ordnungsgemäß funktionieren.

Beim Kopieren eines Canvas mit Audience-Sync-Schritten werden die Einstellungen nicht in den Ziel-Workspace kopiert, aber die Schritte in der Journey werden übernommen.

{% endtab %}
{% tab Landing-Pages %}

Sie können Landing-Pages zwischen Workspaces kopieren.

So kopieren Sie eine Landing-Page in einen anderen Workspace:

1. Gehen Sie zu **Messaging** > **Landing-Pages**.
2. Wählen Sie das <i class="fa-solid fa-ellipsis-vertical" aria-label="Menü"></i>&nbsp;Menü neben der ausgewählten Landing-Page.
3. Wählen Sie **In Workspace kopieren**.
4. Überprüfen und testen Sie Ihre Landing-Page, um sicherzustellen, dass alle Felder ordnungsgemäß funktionieren.

{% endtab %}
{% endtabs %}

{% alert note %}
Sie können eine Campaign oder ein Canvas jederzeit in einen anderen Workspace kopieren – auch nachdem sie gestartet wurde. Braze kopiert die aktive Version.<br><br>Wenn Sie [gespeicherte Entwurfsänderungen]({{site.baseurl}}/user_guide/messaging/campaigns/manage_campaigns/change_your_campaign_after_launch#campaign-drafts) für eine Campaign oder [einen gespeicherten Canvas-Entwurf]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/canvas_drafts) haben, den Sie noch nicht gestartet haben, werden diese ausstehenden Änderungen von Braze nicht übernommen. Starten Sie den Entwurf zuerst im ursprünglichen Workspace und kopieren Sie ihn dann.
{% endalert %}

## Was zwischen Workspaces kopiert wird {#whats-copied-across-workspaces}

Beachten Sie, dass die folgenden Tabellen Campaign- und Canvas-Felder abdecken und keine vollständige Liste dessen darstellen, was zwischen Workspaces kopiert oder ausgelassen wird. Als Best Practice sollten Sie die Campaign-, Canvas- und Landing-Page-Details überprüfen und testen, um sicherzustellen, dass Ihre Nachricht wie erwartet funktioniert.

Landing-Pages werden als Entwürfe kopiert. Bevor Sie eine kopierte Landing-Page veröffentlichen, überprüfen Sie deren Seiten-URL, benutzerdefinierte Domain-Einstellungen, Formularübermittlungsverarbeitung sowie alle Liquid- oder Workspace-spezifischen Referenzen.

{% alert note %}
Übersetzungen werden beim Kopieren von E-Mail-Campaigns, Canvases oder Templates zwischen Workspaces nicht übernommen. Geben Sie nach dem Kopieren die Übersetzungen im Ziel-Workspace erneut ein oder laden Sie sie erneut hoch.
{% endalert %}

### Details {#details}

{% tabs local %}
{% tab campaigns %}

| Kopiert | Ausgelassen |
|---|---|
| Beschreibung | Gebiete |
| Typ | Tags |
| Aktionen (verschachtelt) | Segmente und Filter |
| Konversionsverhalten (verschachtelt) | [Genehmigungen]({{site.baseurl}}/user_guide/messaging/governance/approvals) |
| Ruhezeit-Konfigurationen | Trigger-Zeitplan |
| Frequency-Capping-Konfigurationen | Campaign-Zusammenfassungen |
| Abo-Status der Empfänger:innen |  |
| Wiederkehrender Zeitplan |  |
| Ist transaktional |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Details" }

{% endtab %}
{% tab canvas %}

| Kopiert | Ausgelassen |
|---|---|
| Beschreibung | Gebiete |
| Typ | Tags |
| Aktionen (verschachtelt) | Segmente und Filter |
| Konversionsverhalten (verschachtelt) | [Genehmigungen]({{site.baseurl}}/user_guide/messaging/governance/approvals) |
| Ruhezeit-Konfigurationen | Trigger-Zeitplan |
| Frequency-Capping-Konfigurationen | Canvas-Zusammenfassungen |
| Abo-Status der Empfänger:innen |  |
| Wiederkehrender Zeitplan | Exit-Kriterien |
| Ist transaktional |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Details" }

Filterkriterien aus Canvas-Schritten (z. B. [Decision-Split]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split)-Schritte) werden nicht in den Ziel-Workspace kopiert. Konfigurieren Sie diese Filter nach dem Kopieren neu.

{% endtab %}
{% endtabs %}

### Konversionsverhalten {#conversion-behaviors}

{% tabs local %}
{% tab campaigns %}

| Kopiert | Ausgelassen |
|---|---|
| Verhaltenstyp | Workspace-IDs |
| Campaign-Interaktion | Campaign-ID |
| Name des angepassten Events |  |
| Produktname |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Konversionsverhalten" }

{% endtab %}
{% tab canvas %}

| Kopiert | Ausgelassen |
|---|---|
| Verhaltenstyp | Workspace-IDs |
| Canvas-Interaktion | Canvas-ID |
| Name des angepassten Events |  |
| Produktname |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Konversionsverhalten" }

{% endtab %}
{% endtabs %}

### Aktionen {#actions}

{% tabs local %}
{% tab campaigns %}

| Kopiert | Ausgelassen |
|---|---|
| Verhaltenstyp | Workspace-IDs |
| Campaign-Interaktion | Campaign-ID |
| Name des angepassten Events |  |
| Produktname |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Aktionen" }

{% endtab %}
{% tab canvas %}

| Kopiert | Ausgelassen |
|---|---|
| Verhaltenstyp | Workspace-IDs |
| Canvas-Interaktion | Canvas-ID |
| Name des angepassten Events |  |
| Produktname |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Aktionen" }

{% endtab %}
{% endtabs %}

### Nachrichtenvarianten {#message-variations}

{% tabs local %}
{% tab campaigns %}

| Kopiert | Ausgelassen |
|---|---|
| Sendeprozentsatz | API-ID |
| Typ | Seed-Gruppen-IDs |
|  | Link-Template-IDs |
|  | Interne Nutzer:innengruppen-IDs |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Nachrichtenvarianten" }

{% endtab %}
{% tab canvas %}

| Kopiert | Ausgelassen |
|---|---|
| Sendeprozentsatz | API-ID |
| Typ | Seed-Gruppen-IDs |
|  | Link-Template-IDs |
|  | Interne Nutzer:innengruppen-IDs |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Nachrichtenvarianten" }

{% endtab %}
{% endtabs %}


### E-Mail-Nachrichtenvariation {#email-message-variation}

{% tabs local %}
{% tab campaigns %}

| Kopiert | Ausgelassen |
|---|---|
| E-Mail-Text | Absenderadresse |
| Nachrichtenextras | Antwort an |
| Titel | BCC |
| Betreff | Link-Template |
|  | Link Aliasing |
|  | Übersetzungen |
{: .reset-td-br-1 .reset-td-br-2 aria-label="E-Mail-Nachrichtenvariation" }

{% endtab %}
{% tab canvas %}

| Kopiert | Ausgelassen |
|---|---|
| E-Mail-Text | Absenderadresse |
| Nachrichtenextras | Antwort an |
| Titel | BCC |
| Betreff | Link-Template |
|  | Link Aliasing |
|  | Übersetzungen |
{: .reset-td-br-1 .reset-td-br-2 aria-label="E-Mail-Nachrichtenvariation" }

{% endtab %}
{% endtabs %}

### E-Mail-Text {#email-body}

{% tabs local %}
{% tab campaigns %}

| Kopiert | Ausgelassen |
|---|---|
| Klartext | Link Aliasing |
| HTML- und Drag-and-Drop-Inhalte | Übersetzungen |
| Preheader |  |
| Inline-CSS |  |
| AMP-HTML |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="E-Mail-Text" }

{% endtab %}
{% tab canvas %}

| Kopiert | Ausgelassen |
|---|---|
| Klartext | Link Aliasing |
| HTML- und Drag-and-Drop-Inhalte | Übersetzungen |
| Preheader |  |
| Inline-CSS |  |
| AMP-HTML |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="E-Mail-Text" }

{% endtab %}
{% endtabs %}

### E-Mail-Templates {#email-templates}

{% tabs local %}
{% tab campaigns %}

| Kopiert | Ausgelassen |
|---|---|
| E-Mail-Text | API-IDs |
| Beschreibung | Bild-IDs |
| Betreff | Gebiete |
| Header | Tags |
| | Übersetzungen |
{: .reset-td-br-1 .reset-td-br-2 aria-label="E-Mail-Templates" }

{% endtab %}
{% tab canvas %}

| Kopiert | Ausgelassen |
|---|---|
| E-Mail-Text | API-IDs |
| Beschreibung | Bild-IDs |
| Betreff | Gebiete |
| Header | Tags |
| | Übersetzungen |
{: .reset-td-br-1 .reset-td-br-2 aria-label="E-Mail-Templates" }

{% endtab %}
{% endtabs %}

### Content Blocks

{% tabs local %}
{% tab campaigns %}

| Kopiert | Ausgelassen |
|---|---|
| Name | Link Aliasing |
| Beschreibung | API-Schlüssel |
| Inhalt | Gebiete |
| HTML- und Drag-and-Drop-Inhalte | Tags |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Content Blocks" }

{% endtab %}
{% tab canvas %}

| Kopiert | Ausgelassen |
|---|---|
| Name | Link Aliasing |
| Beschreibung | API-Schlüssel |
| Inhalt | Gebiete |
| HTML- und Drag-and-Drop-Inhalte | Tags |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Content Blocks" }

{% endtab %}
{% endtabs %}

### SMS-Nachrichtenvariation {#sms-message-variation}

{% tabs local %}
{% tab campaigns %}

| Kopiert | Ausgelassen |
|---|---|
| Text | Messaging-Dienst |
| Linkverkürzung | VCF-Medienelemente |
| Klick-Tracking |  |
| Medienelemente |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="SMS-Nachrichtenvariation" }

{% endtab %}
{% tab canvas %}

| Kopiert | Ausgelassen |
|---|---|
| Text | Messaging-Dienst |
| Linkverkürzung | VCF-Medienelemente |
| Klick-Tracking |  |
| Medienelemente |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="SMS-Nachrichtenvariation" }

{% endtab %}
{% endtabs %}

## Nachrichten mit Liquid kopieren {#copying-messages-that-contain-liquid}

Liquid-Referenzen innerhalb von Nachrichtentexten werden in den Ziel-Workspace kopiert, funktionieren dort aber möglicherweise nicht wie erwartet. Das bedeutet: Wenn ein Canvas aus Workspace A in Workspace B kopiert wird, kann Workspace B nicht auf die Details von Workspace A zugreifen, einschließlich Liquid-Referenzen. Beispielsweise werden Felder wie Aktionen triggern, Zielgruppenfilter und Filterkriterien für [Decision-Splits]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split) nicht mitkopiert.

Behalten Sie die folgenden Liquid-Referenzen mit Abhängigkeiten im Blick, wenn Sie Campaigns, Canvases und Landing-Pages zwischen Workspaces kopieren:

- Katalog-Artikel-Tags
- Connected-Content-Tags
- Content Blocks
- Angepasste Attribute
- Präferenzcenter
- Produktempfehlungen
- Abo-Status-Tags
- Gutschein- und Aktions-Tags

## Nachrichten mit Feature-Flags kopieren {#copying-messages-with-feature-flags}

Um eine Feature-Flag-Campaign und ein Canvas mit einem Feature-Flag-Schritt zwischen Workspaces zu kopieren, stellen Sie sicher, dass im Ziel-Workspace ein [Feature-Flag-Experiment]({{site.baseurl}}/developer_guide/feature_flags/experiments) konfiguriert ist, dessen ID entweder mit dem Feature-Flag übereinstimmt, auf das in der ursprünglichen Campaign verwiesen wird, oder mit dem Feature-Flag-Schritt, auf den im ursprünglichen Canvas verwiesen wird.

Wenn Sie eine Campaign oder ein Canvas mit einem Feature-Flag-Schritt kopieren, dessen Feature-Flag-ID im Ziel-Workspace nicht existiert, wird der Feature-Flag-Schritt kopiert, aber sein Inhalt nicht.

## Nachrichten mit Content Blocks kopieren {#copying-messages-with-content-blocks}

Wenn Sie eine Campaign über Workspaces hinweg kopieren, werden Content Blocks nicht mitkopiert. Ein Content-Block kann jedoch im Ziel-Workspace referenziert werden, wenn dort ein Block mit demselben Namen existiert. Alternativ können Sie den Content-Block (oder diese Liquid-Referenzen) im Ziel-Workspace erstellen, um Fehler beim Starten einer Campaign zu vermeiden.

Bei Canvases, die auf einen Content-Block verweisen, muss der Content-Block zuerst in den Ziel-Workspace kopiert werden.