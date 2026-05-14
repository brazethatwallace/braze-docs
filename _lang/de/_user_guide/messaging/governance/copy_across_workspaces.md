---
nav_title: Zwischen Workspaces kopieren
article_title: Zwischen Workspaces kopieren
page_order: 3
alias: "/copying_to_workspaces/"
page_type: reference
description: "Dieser Referenzartikel bietet einen Überblick darüber, wie Sie Campaigns und Canvases in verschiedene Workspaces kopieren können."
tool:
    - Campaigns
    - Canvas
---

# Campaigns und Canvases zwischen Workspaces kopieren {#copy-campaigns-and-canvases-across-workspaces}

> Das Kopieren von Campaigns zwischen Workspaces ermöglicht es Ihnen, Ihre Nachrichtenkomposition zu beschleunigen, indem Sie mit einer Kopie einer Campaign in einem anderen Workspace beginnen. Diese Seite beschreibt, wie Sie Campaigns in verschiedene Workspaces kopieren und listet auf, was kopiert wird und was nicht.

Wenn Sie eine Campaign oder ein Canvas in einen anderen Workspace kopieren, bleibt die Kopie als Entwurf erhalten, bis Sie sie bearbeiten und starten. So können Sie Ihre erfolgreichen Messaging-Strategien beibehalten und darauf aufbauen.

{% tabs local %}
{% tab campaigns %}

{% alert important %}
Das Kopieren von Campaigns zwischen Workspaces ist allgemein verfügbar. Kanalunterstützung für Content Cards ist derzeit nicht verfügbar.
{% endalert %}

Sie können Campaigns zwischen Workspaces für diese unterstützten Kanäle kopieren: SMS, In-App-Nachrichten, Push-Benachrichtigungen, E-Mail und Webhooks. Sie können auch E-Mail-Templates, Feature-Flags und Content Blocks kopieren. Beachten Sie, dass Multichannel-Kampagnen mit nicht unterstützten Kanälen nicht in einen anderen Workspace kopiert werden können.

So kopieren Sie eine Campaign in einen anderen Workspace:

1. Wählen Sie das <i class="fas fa-cog"></i> Zahnradsymbol neben der ausgewählten Campaign.
2. Wählen Sie **In Workspace kopieren**.
3. Überprüfen und testen Sie nach dem Kopieren Ihre Campaign, um sicherzustellen, dass alle Felder ordnungsgemäß funktionieren.

{% endtab %}
{% tab canvas %}

{% alert important %}
Das Kopieren von Canvases zwischen Workspaces ist allgemein verfügbar. Die folgenden Kanäle werden derzeit nicht unterstützt: LINE, Content Cards und WhatsApp.
{% endalert %}

Sie können Canvases zwischen Workspaces für diese unterstützten Kanäle kopieren: E-Mail, In-App-Nachrichten, Push, Webhooks und SMS.

So kopieren Sie ein Canvas in einen anderen Workspace:

1. Wählen Sie das <i class="fa-solid fa-ellipsis-vertical"></i>&nbsp;Menü neben dem ausgewählten Canvas.
2. Wählen Sie **In Workspace kopieren**.
3. Überprüfen und testen Sie nach dem Kopieren Ihr Canvas, um sicherzustellen, dass alle Felder ordnungsgemäß funktionieren.

Beim Kopieren eines Canvas mit Audience-Sync-Schritten werden die Einstellungen nicht in den Ziel-Workspace kopiert, aber die Schritte in der Journey werden übernommen.

{% endtab %}
{% endtabs %}

## Was zwischen Workspaces kopiert wird {#whats-copied-across-workspaces}

Beachten Sie, dass die folgende Liste nicht vollständig ist und nicht alles aufführt, was zwischen Workspaces kopiert oder ausgelassen wird. Als Best Practice sollten Sie die Campaign- und Canvas-Details überprüfen und testen, um sicherzustellen, dass Ihre Nachricht wie erwartet funktioniert.

### Details {#details}

{% tabs local %}
{% tab campaigns %}

| Kopiert | Ausgelassen |
|---|---|
| Beschreibung | Gebiete |
| Typ | Tags |
| Aktionen (verschachtelt) | Segmente und Filter |
| Conversion-Verhalten (verschachtelt) | [Genehmigungen]({{site.baseurl}}/user_guide/messaging/governance/approvals/) |
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
| Conversion-Verhalten (verschachtelt) | [Genehmigungen]({{site.baseurl}}/user_guide/messaging/governance/approvals/) |
| Ruhezeit-Konfigurationen | Trigger-Zeitplan |
| Frequency-Capping-Konfigurationen | Canvas-Zusammenfassungen |
| Abo-Status der Empfänger:innen |  |
| Wiederkehrender Zeitplan | Ausstiegskriterien |
| Ist transaktional |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Details" }

Filterkriterien aus Canvas-Schritten (zum Beispiel [Decision-Split]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split/)-Schritte) werden nicht in den Ziel-Workspace kopiert. Konfigurieren Sie diese Filter nach dem Kopieren neu.

{% endtab %}
{% endtabs %}

### Conversion-Verhalten {#conversion-behaviors}

{% tabs local %}
{% tab campaigns %}

| Kopiert | Ausgelassen |
|---|---|
| Verhaltenstyp | Workspace-IDs |
| Campaign-Interaktion | Campaign-ID |
| Name des angepassten Events |  |
| Produktname |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conversion behaviors" }

{% endtab %}
{% tab canvas %}

| Kopiert | Ausgelassen |
|---|---|
| Verhaltenstyp | Workspace-IDs |
| Canvas-Interaktion | Canvas-ID |
| Name des angepassten Events |  |
| Produktname |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conversion behaviors" }

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
{: .reset-td-br-1 .reset-td-br-2 aria-label="Actions" }

{% endtab %}
{% tab canvas %}

| Kopiert | Ausgelassen |
|---|---|
| Verhaltenstyp | Workspace-IDs |
| Canvas-Interaktion | Canvas-ID |
| Name des angepassten Events |  |
| Produktname |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Actions" }

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
{: .reset-td-br-1 .reset-td-br-2 aria-label="Message variations" }

{% endtab %}
{% tab canvas %}

| Kopiert | Ausgelassen |
|---|---|
| Sendeprozentsatz | API-ID |
| Typ | Seed-Gruppen-IDs |
|  | Link-Template-IDs |
|  | Interne Nutzer:innengruppen-IDs |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Message variations" }

{% endtab %}
{% endtabs %}


### E-Mail-Nachrichtenvariante {#email-message-variation}

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
{: .reset-td-br-1 .reset-td-br-2 aria-label="Email message variation" }

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
{: .reset-td-br-1 .reset-td-br-2 aria-label="Email message variation" }

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
{: .reset-td-br-1 .reset-td-br-2 aria-label="Email body" }

{% endtab %}
{% tab canvas %}

| Kopiert | Ausgelassen |
|---|---|
| Klartext | Link Aliasing |
| HTML- und Drag-and-Drop-Inhalte | Übersetzungen |
| Preheader |  |
| Inline-CSS |  |
| AMP-HTML |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Email body" }

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
{: .reset-td-br-1 .reset-td-br-2 aria-label="Email templates" }

{% endtab %}
{% tab canvas %}

| Kopiert | Ausgelassen |
|---|---|
| E-Mail-Text | API-IDs |
| Beschreibung | Bild-IDs |
| Betreff | Gebiete |
| Header | Tags |
| | Übersetzungen |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Email templates" }

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

### SMS-Nachrichtenvariante {#sms-message-variation}

{% tabs local %}
{% tab campaigns %}

| Kopiert | Ausgelassen |
|---|---|
| Text | Messaging-Dienst |
| Linkverkürzung | VCF-Medienelemente |
| Klick-Tracking |  |
| Medienelemente |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="SMS message variation" }

{% endtab %}
{% tab canvas %}

| Kopiert | Ausgelassen |
|---|---|
| Text | Messaging-Dienst |
| Linkverkürzung | VCF-Medienelemente |
| Klick-Tracking |  |
| Medienelemente |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="SMS message variation" }

{% endtab %}
{% endtabs %}

## Nachrichten mit Liquid-Referenzen kopieren {#copying-messages-that-contain-liquid}

Liquid-Referenzen innerhalb von Nachrichtentexten werden in den Ziel-Workspace kopiert, funktionieren dort aber möglicherweise nicht wie erwartet. Das bedeutet: Wenn ein Canvas aus Workspace A in Workspace B kopiert wird, kann Workspace B nicht auf die Details von Workspace A zugreifen, einschließlich Liquid-Referenzen. Beispielsweise werden Felder wie Trigger-Aktionen, Zielgruppen-Filter und [Decision-Split]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split/)-Filterkriterien nicht kopiert.

Behalten Sie die folgenden Liquid-Referenzen mit Abhängigkeiten im Blick, wenn Sie Campaigns und Canvases zwischen Workspaces kopieren:

- Katalog-Artikel-Tags
- Connected-Content-Tags
- Content Blocks
- Angepasste Attribute
- Präferenzzentren
- Produktempfehlungen
- Abo-Status-Tags
- Gutschein- und Aktions-Tags

## Nachrichten mit Feature-Flags kopieren {#copying-messages-with-feature-flags}

Um eine Feature-Flag-Campaign und ein Canvas mit einem Feature-Flag-Schritt zwischen Workspaces zu kopieren, stellen Sie sicher, dass im Ziel-Workspace ein [Feature-Flag-Experiment]({{site.baseurl}}/developer_guide/feature_flags/experiments/) mit einer ID konfiguriert ist, die entweder dem Feature-Flag in der ursprünglichen Campaign oder dem Feature-Flag-Schritt im ursprünglichen Canvas entspricht.

Wenn Sie eine Campaign oder ein Canvas mit einem Feature-Flag-Schritt kopieren, dessen Feature-Flag-ID im Ziel-Workspace nicht existiert, wird der Feature-Flag-Schritt kopiert, aber sein Inhalt nicht.

## Nachrichten mit Content Blocks kopieren {#copying-messages-with-content-blocks}

Wenn Sie eine Campaign zwischen Workspaces kopieren, werden Content Blocks nicht mitkopiert. Ein Content-Block kann jedoch im Ziel-Workspace referenziert werden, wenn dort ein Block mit demselben Namen existiert. Alternativ können Sie den Content-Block (oder diese Liquid-Referenzen) im Ziel-Workspace erstellen, um Fehler beim Starten einer Campaign zu vermeiden.

Bei Canvases, die einen Content-Block referenzieren, muss der Content-Block zuerst in den Ziel-Workspace kopiert werden.