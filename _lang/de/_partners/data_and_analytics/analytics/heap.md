---
nav_title: Heap
article_title: "Heap Analytics"
description: "Dieser Referenzartikel beschreibt, wie Sie Braze-Currents verwenden, um Engagement-Ereignisse automatisch mit Heap, einer Plattform für digitale Insights, zu analysieren. Die Integration ermöglicht es Ihnen, Heap-Daten in Braze zu importieren, Nutzer:innen-Kohorten zu erstellen und Braze-Daten in Heap zu exportieren, um Segmente zu erstellen."
page_type: partner
alias: /partners/heap/
search_tag: Partner

---

# Heap Analytics

> Dieser Artikel beschreibt, wie Sie Engagement-Ereignisse automatisch von Braze zur Analyse an Heap senden. Weitere Informationen zur Integration von Heap und seinen anderen Funktionen, wie z. B. die [Synchronisierung von Heap-Kohorten]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/heap#data-import-integration) mit Braze, finden Sie im [Hauptartikel zu Heap]({{site.baseurl}}/partners/data_and_analytics/analytics/heap/heap_cohort_import).

## Datenexport-Integration {#data-export-integration}

Verwenden Sie Braze-Currents, um Engagement-Ereignisse (z. B. E-Mail gesendet, Push gesendet) automatisch von Braze an Heap zur Analyse zu senden.

### Schritt 1: Heap-Zugangsdaten abrufen {#step-1-get-heap-credentials}

Um diese Integration zu konfigurieren, benötigen Sie eine Webhook-Endpunkt-URL, die Sie von Ihrem Heap Account Manager:in erhalten.

### Schritt 2: Braze-Currents konfigurieren {#step-2-configure-braze-currents}

Navigieren Sie in Braze zu **Partnerintegrationen** > **Datenexport**, klicken Sie auf **Neuen Current erstellen** und wählen Sie **Heap-Export**.

Geben Sie Ihrem Export einen Namen und fahren Sie dann mit der Seite **Current-Details** fort. Geben Sie auf dieser Seite den Endpunkt und das optionale Bearer-Token / Textbaustein ein (falls vorhanden).

Nachdem Sie die Zugangsdaten für Ihre Integration konfiguriert haben, markieren Sie alle Nachrichten-Engagement-, Kundenverhalten- und Nutzer:innen-Ereignisse, die Sie in Heap exportieren möchten, und klicken Sie auf **Current starten**.

![Braze Heap Current-Einrichtungsseite mit Feldern für Endpunkt, Token und Ereignisauswahl.]({% image_buster /assets/img/heap/heap4.png %}){: style="max-width:90%;"}