---
nav_title: Stylitics
article_title: Stylitics
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Stylitics, einer cloudbasierten SaaS-Plattform, die es Ihnen erlaubt, Ihre bestehenden E-Mail-Campaigns mit ansprechenden und relevanten gebündelten Inhalten zu erweitern und so ein personalisiertes Kundenerlebnis zu schaffen."
alias: /partners/stylitics/
page_type: partner
search_tag: Partner

---

# Stylitics

> [Stylitics](https://stylitics.com/) ist eine cloudbasierte SaaS-Plattform für Einzelhändler, die visuelle Inhalte in großem Umfang automatisieren und verbreiten möchten. Stylitics-Bundles inspirieren durch kontextuelle Produktzusammenstellungen, stärken das Kaufvertrauen und steigern das Engagement – was letztendlich zu einem höheren durchschnittlichen Bestellwert und höheren Konversionsraten führt.

_Diese Integration wird von Stylitics gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Braze und Stylitics erlaubt es Ihnen, Ihre bestehenden E-Mail-Campaigns mit ansprechenden und relevanten gebündelten Inhalten zu erweitern und so ein personalisiertes Kundenerlebnis zu schaffen.

![Beispiel für gebündelte Stylitics-Inhalte, eingebettet in ein Braze-E-Mail-Erlebnis.]({% image_buster /assets/img/stylitics.png %}){: style="max-width:60%;"}

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Stylitics-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Stylitics-Konto](https://stylitics.com/). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Anwendungsfälle {#use-cases}

Im Folgenden finden Sie einige Beispiele für häufig getriggerte E-Mail-Programme:
- E-Mails bei Warenkorb-Abbruch
- E-Mails bei abgebrochenem Browsing
- E-Mails zur Versandbestätigung
- E-Mails nach dem Kauf

## Integration

Stylitics stellt für diese Integration die Bundle-Daten bereit. Ihr E-Mail-Anbieter kann das E-Mail-Template erstellen oder aktualisieren, um Stylitics-Bundles einzubinden. Stylitics kann das Layout oder Design der E-Mails nicht verändern.

1. Integrieren Sie das Bundle in die E-Mail. Der ESP bestimmt die Position und Anpassung.
2. Der ESP aktualisiert den Code der getriggerten E-Mail, um Stylitics-Inhalte einzubeziehen.
3. Der ESP testet, zeigt eine Vorschau an und startet die aktualisierte getriggerte Serie.

Stylitics stellt nur die Bundle-Daten für die Artikel bereit. Sie und Ihr ESP verfügen über die Nutzerdaten und können die Stylitics-Bundle-Daten einfügen, um sie an die Nutzer:innen zu senden.

## Datenaustausch {#data-exchange}

Die folgenden drei Ansätze erlauben es Ihnen, Stylitics-Bundles in Ihre getriggerten E-Mails einzubinden.

### 1. API-Ansatz (empfohlen) {#1-api-approach-recommended}

Sie oder Ihr ESP können pro Artikel einen API-Aufruf tätigen, um die Bundle-Daten in Ihre E-Mail einzupflegen. Stylitics empfiehlt Ihnen, die Stylitics-API für API-Aufrufe zu verwenden, da sie sofort einsatzbereit ist.

{% alert note %}
Wenn Sie einen von Stylitics durchgeführten A/B-Test nutzen, müssen die Parameter `styliticsCID` und `styliticsoverride` an die PDP-URLs der Stylitics-Artikel angehängt werden, auf die Nutzer:innen in der E-Mail klicken.
<br><br>
Zum Beispiel: {% raw %}`&styliticsoverride=001?styliticsCID=email[clientname]`{% endraw %}
{% endalert %}

### 2. Flat-File-Ansatz {#2-flat-file-approach}

Sie oder Ihr ESP können die Bundle-Daten eines Artikels in einer Flat File referenzieren, um Bundle-Daten in Ihre E-Mail einzufügen. Stylitics kann die Bundle-Daten in das CSV-, TXT- oder XML-Format umwandeln und Ihnen täglich zusenden. Stylitics kann auch dabei helfen, das Dateiformat an die Anforderungen Ihres ESP anzupassen. Beachten Sie, dass die Erstellung dieser Datei 2–3 Wochen dauert.

#### Anforderungen: {#requirements}
- **Speicherort**: Stylitics kann die Datei auf dem Stylitics-SFTP-Server ablegen, damit Sie sie täglich abholen können, oder Sie können Stylitics Ihre SFTP-Zugangsdaten senden, um die Datei dort abzulegen.
- **Zeitpunkt**: Stylitics liefert die Datei täglich am Morgen. Teilen Sie Stylitics mit, falls Sie die Datei bis zu einem bestimmten Zeitpunkt benötigen.
- **Datei-Schlüssel**: Sie und Stylitics müssen sich darauf einigen, welcher Artikeldaten-String als Schlüssel für die Datei verwendet wird, damit Ihr ESP die Daten referenzieren kann. SKU, `item_group_id` oder `item_number` werden häufig verwendet.

### 3. Ansatz zur Website-Datenextraktion {#3-website-data-extraction-approach}

Anbieter können das Frontend Ihrer Website nach Stylitics-Inhalten durchsuchen und Bundle-Daten in E-Mails einfügen. Es ist keine zusätzliche Arbeit von Stylitics erforderlich.

## Best Practices für E-Mail-Templates {#email-template-best-practices}

Sie und Ihr ESP erstellen ein HTML-E-Mail-Template, um Stylitics-Daten und -Bundles einzufügen. Hier finden Sie einige bewährte Verfahren und Empfehlungen.
- Zeigen Sie 2–4 Bundles in der E-Mail für den teuersten Artikel oder den ersten Vollpreisartikel an, den Nutzer:innen gekauft oder mit dem sie interagiert haben
- Rufen Sie mehrere `item_numbers` auf und zeigen Sie die ersten Bundle-Ergebnisse an
- Halten Sie eine Fallback-Option bereit, falls für den Artikel keine Bundles verfügbar sind
	- Blenden Sie den Bereich aus, in dem sich die Stylitics-Bundles befinden
	- Zeigen Sie Bundles für den nächsten Artikel an, den Nutzer:innen angesehen haben
- Zeigen Sie Bundle-Bilder sowie eine Liste von Produkttiteln und Miniaturbildern an, um sicherzustellen, dass Nutzer:innen einen klaren Click-through haben

{% alert note %}
Das Stylitics-Widget-JavaScript kann nicht in E-Mails eingefügt werden, da E-Mails kein JavaScript unterstützen.
{% endalert %}

## Analytics

Stylitics stellt die Bundle-Daten für diese Art von E-Mail-Programm bereit. Daher bitten wir um einen offenen Datenaustausch zwischen Ihnen, Ihrem ESP und Stylitics. Wenn möglich, hoffen wir, die folgenden Metriken von Ihnen zu erhalten, um die Wirkung zu verstehen und das Programm zu verbessern:
- Versendete E-Mails
- Geöffnete E-Mails
- Aufrufe und Engagement
- Click-through-Rate
- In den Warenkorb gelegt
- Käufe

## Nächste Schritte {#next-steps}

Wenden Sie sich an Ihren Stylitics Account Manager, um die nächsten Schritte und den Zeitplan für das E-Mail-Programm zu koordinieren. Einige nächste Schritte sind:
- Entscheiden Sie, welche E-Mails Sie verwenden möchten
- Verbinden Sie Stylitics mit Ihrem ESP, um den Datenaustausch zu besprechen und zwischen der API-Option oder der Flat-File-Option zu entscheiden
- Erstellen Sie Mockups mit Ihrem ESP
- Stimmen Sie sich zu Analytics ab
- Stimmen Sie den Zeitplan für die Markteinführung ab