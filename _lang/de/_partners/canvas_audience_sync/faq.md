---
nav_title: FAQ
article_title: Audience Sync – FAQ
alias: /partners/audience_sync_faq/
description: "Dieser Artikel enthält Antworten auf häufig gestellte Fragen zu Audience Sync."
page_order: 80
tool:
  - Canvas

---

# Häufig gestellte Fragen {#frequently-asked-questions}

> Dieser Artikel enthält Antworten auf einige häufig gestellte Fragen zu Audience Sync.

## Wie lange dauert es, bis meine Zielgruppen im Dashboard meines Audience-Sync-Partners angezeigt werden? {#how-long-does-it-take-for-my-audiences-to-populate-in-my-audience-sync-partner-dashboard}

Wie lange es dauert, eine Zielgruppe aufzubauen, hängt vom jeweiligen Partner ab. Alle Netzwerke verarbeiten die Anfragen von Braze und versuchen, Nutzer:innen zuzuordnen. Dieser Vorgang kann in der Regel zwischen 6 und 48 Stunden dauern.

Die genaue Zeitspanne können Sie im Abschnitt „Fehlerbehebung“ in der Dokumentation des jeweiligen Audience-Sync-Partners nachschlagen.

## Welche Art von First-Party-Daten kann ich in meiner Audience Sync verwenden? {#what-type-of-first-party-data-can-i-use-in-my-audience-sync}

Die spezifischen Felder, die für jeden Partner verwendet werden, können je nach den Anforderungen des Partners variieren.

Wenn Sie beispielsweise eine Audience Sync mit Facebook konfigurieren, können Sie eine Vielzahl von First-Party-Feldern wie E-Mail, Telefon, Vorname und Nachname verwenden, während Sie bei Snapchat nur E-Mail, Telefon oder die Mobile-Advertiser-ID auswählen können.

Bitte beachten Sie, dass die Nutzer:innen-Felder, die Sie für die Synchronisierung auswählen können, mit den Braze-Standardattributen und den Mobile-Advertising-IDs korrelieren. Sie müssen sicherstellen, dass Sie diese Daten ordnungsgemäß über unsere SDKs oder APIs übergeben.

## Was passiert, wenn meine Daten verarbeitet werden, um sie an die einzelnen Audience-Sync-Partner zu senden? {#what-happens-when-my-data-is-being-processed-to-send-to-each-audience-sync-partner}

Die Daten, die Sie zum Senden an Ihr Audience-Sync-Ziel auswählen, werden normalisiert. Jeder Partner kann je nach seinen API-Anforderungen unterschiedliche Spezifikationen für die Datennormalisierung haben. Prüfen Sie daher jeden partnerspezifischen Endpunkt für weitere Details.

Darüber hinaus hasht Braze alle Daten, bevor Nutzer:innen mit unseren Audience-Sync-Partnern synchronisiert werden, um sicherzustellen, dass alle PII mit SHA256 gehasht werden.

## Warum kann ich für einige Partner mehrere Bezeichner in einem Schritt auswählen, für andere aber nur einen Bezeichner? {#why-can-i-select-multiple-identifiers-in-one-step-for-some-partners-but-can-only-select-one-identifier-for-others}

Dies wird von den Methoden der Partnerintegration bestimmt und nicht von Braze kontrolliert. Bei einigen Partnern (z. B. Meta) können mehrere Bezeichner synchronisiert werden, während bei anderen Partnern (z. B. Google) immer nur ein einziger Bezeichner pro Nutzer:in synchronisiert werden kann.

## Wie kann ich meine Integration erneut verbinden? {#how-do-i-reconnect-my-integration}

Wenn die Person, die die Integration ursprünglich verbunden hat, nicht mehr in Ihrem Unternehmen tätig ist, müssen Sie die Integration mit einer neuen Person aktualisieren, indem Sie **Konto wechseln** auswählen. Wählen Sie dann **Bestätigen** und stellen Sie die Verbindung mit der neuen Person her. Wir empfehlen, den Wechsel durchzuführen, wenn keine aktiven Synchronisierungen stattfinden, z. B. vor einem geplanten Eingang von Nutzer:innen in einen Canvas, da eine Synchronisierung während des Übergangs von der vorherigen zur neuen Person aktive Canvases unterbrechen kann.

Die Person, die die Verbindung wiederherstellt, muss sowohl Lese- als auch Schreibzugriff auf alle Zielgruppen haben, damit Nutzer:innen erfolgreich mit den Partnern synchronisiert werden können. Vergewissern Sie sich, dass die Person, die die Integration wiederherstellt, Zugriff auf dieselben Anzeigenkonten und Zielgruppen hat. Sie brauchen keine bestehenden Canvas-Schritte zu bearbeiten.

## Was sind häufige Fehler, die bei der Erstellung und Verwaltung meiner Audience Syncs auftreten können? {#what-are-common-errors-that-can-occur-when-creating-and-managing-my-audience-syncs}

| Fehler | Grund | Lösung |
| --- | --- | --- |
| Ungültiges Token / Textbaustein | Dies kann auftreten, wenn Sie Ihr Passwort für die Anmeldung bei einem bestimmten Anzeigennetzwerk geändert haben oder wenn Ihre Zugangsdaten abgelaufen sind. | Gehen Sie auf die jeweilige Partnerseite, um Ihr Konto zu trennen und wieder zu verbinden. |
| Zielgruppe zu klein | Dies kann vorkommen, wenn Sie einen Audience-Sync-Schritt erstellt haben, der Nutzer:innen aus Ihren Zielgruppen entfernt. Wenn die Größe Ihrer Zielgruppe gegen Null geht, kann das Netzwerk feststellen, dass die Zielgruppe zu klein ist, um bedient zu werden. | Vergewissern Sie sich, dass Sie eine Audience-Sync-Strategie verfolgen, bei der regelmäßig Nutzer:innen hinzugefügt und entfernt werden, ohne dass die Zielgruppe vollständig erschöpft wird. |
| Zielgruppe existiert nicht | Der Audience-Sync-Schritt verwendet eine Zielgruppe, die nicht existiert. Dies kann auch ausgelöst werden, wenn Sie nicht über die erforderliche Berechtigung zum Zugriff auf die Zielgruppe verfügen. | Fügen Sie eine aktive Zielgruppe in Ihrer Audience-Sync-Konfiguration hinzu oder erstellen Sie eine neue Zielgruppe. |
| Zugriff auf Anzeigenkonto | Dieser Fehler tritt auf, wenn Sie keine Berechtigung für das Anzeigenkonto, eine von Ihnen ausgewählte Zielgruppe oder beides haben. | Arbeiten Sie mit den Administratoren Ihres Anzeigenkontos zusammen, um den richtigen Zugang und die richtigen Berechtigungen zu erhalten. |
| Ungültige Einstellungen | Dies kann vorkommen, wenn Sie kein bestimmtes Audience-Sync-Ziel in Canvas konfiguriert haben, einschließlich der entsprechenden Felder für Anzeigenkonten, Zielgruppen oder Nutzer:innen. | Vervollständigen Sie die Konfiguration der einzelnen Partner, bevor Sie starten. |
| Nutzungsbedingungen | Bei einigen Audience-Sync-Zielen, wie z. B. Facebook, ist es vom Anzeigennetzwerk vorgeschrieben, bestimmte Nutzungsbedingungen zu akzeptieren, um das Audience-Sync-Feature nutzen zu können. Dieser Fehler wird ausgelöst, wenn Sie die entsprechenden Bedingungen nicht akzeptiert haben. | Bestätigen Sie, dass Sie die erforderlichen Bedingungen jedes Partners akzeptiert haben. Speziell für Facebook lesen Sie bitte die [Facebook-Fehlerbehebung]({{site.baseurl}}/partners/canvas_steps/facebook_audience_sync#troubleshooting). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Häufige Fehler bei der Erstellung und Verwaltung von Audience Syncs" }