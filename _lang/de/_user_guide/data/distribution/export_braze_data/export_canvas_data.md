---
nav_title: Canvas-Daten
article_title: Canvas-Daten exportieren
page_order: 3
page_type: reference
description: "Dieser Referenzartikel beschreibt, wie Sie Canvas-Analytics exportieren können."
tool:
  - Canvas
  - Reports

---

# Canvas-Daten exportieren {#export-canvas-data}

> Nutzerdaten können in eine CSV-Datei exportiert werden. Auf dieser Seite erfahren Sie, wie Sie Daten für Ihren gesamten Canvas oder eine bestimmte Canvas-Komponente exportieren können.

## Daten für einen Canvas exportieren {#exporting-data-for-a-canvas}

Um Daten für einen Canvas zu exportieren, gehen Sie wie folgt vor:

1. Gehen Sie zu **Messaging** > **Canvas** und wählen Sie Ihren Canvas aus.
2. Wählen Sie das Dropdown-Menü **User Data** im Abschnitt **Canvas Details** aus.
3. Wählen Sie eine der folgenden Exportoptionen aus:
  - **CSV Export User Data** oder
  - **CSV Export Email Address**.

Sie können auch Nutzerdaten für alle Teilnehmer:innen eines Canvas als CSV-Datei exportieren.

## Nutzer:innen exportieren, die einen Canvas betreten oder erneut betreten haben {#export-users-who-entered-or-re-entered-a-canvas}

Wenn die [erneute Berechtigung]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility) aktiviert ist, können Nutzer:innen denselben Canvas mehrmals betreten. Die Option **CSV Export User Data** auf der Canvas-Detailseite exportiert Nutzer:innen, die den Canvas betreten haben, enthält jedoch nicht, wie oft jede:r Nutzer:in eingetreten ist oder den jeweiligen Eintrittszeitstempel.

Um zu analysieren, wann Nutzer:innen einen Canvas betreten oder erneut betreten haben, verwenden Sie eine der folgenden Optionen:

- **Letzter Eintritt pro Nutzer:in:** Exportieren Sie ein Segment mit dem Feld [`canvases_received`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) über den Endpunkt [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment). Für jeden Canvas enthält der Export die Zeitstempel `last_entered` und `last_exited` für diese:n Nutzer:in. Das Feld `canvases_received` enthält Daten der letzten 90 Tage.
- **Jeder Eintritt, einschließlich erneuter Eintritte:** Verwenden Sie [Canvas-Entry-Ereignisse]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#canvas-entry-events) in Braze-Currents oder Snowflake Data Sharing. Jedes `users.canvas.Entry`-Ereignis stellt einen Canvas-Eintritt dar und enthält einen `time`-Zeitstempel. Zählen Sie die Ereignisse pro Nutzer:in, um zu ermitteln, wie oft sie eingetreten sind.
- **Nutzerliste im Dashboard erstellen:** Erstellen Sie ein Segment mit dem Filter **Entered Canvas Variation** und exportieren Sie das Segment als CSV-Datei. Siehe [Canvas-Fehlerbehebung]({{site.baseurl}}/user_guide/messaging/canvas/troubleshooting#user-didnt-enter-the-canvas).

{% alert note %}
Wenn Sie Currents nicht integriert haben und jeden historischen Eintrittszeitstempel benötigen, wenden Sie sich an Ihren CSM or Customer-Success-Manager or Customer-Success-Manager:in bei Braze.
{% endalert %}

Für einen bestimmten Canvas-Schritt im Original-Workflow verwenden Sie **CSV Export User Data** auf der Detailseite des Schritts.

## Daten für eine Komponente exportieren (nur Original-Workflow) {#exporting-data-for-a-component-original-workflow-only}

Canvas-Ergebnisse können auf Basis einzelner Komponenten für den ursprünglichen Canvas-Workflow exportiert werden. Wählen Sie dazu die entsprechende Komponente aus und wählen Sie dann das Dropdown-Menü **User Data** auf der Seite **Canvas-Schritt Details**.

![Dropdown „Nutzerdaten“ auf der Seite „Canvas Details“.]({% image_buster /assets/img/canvas_csv_export.png %})

{% alert tip %}
Hilfe bei CSV- und API-Exporten finden Sie in unserem Artikel zur [Fehlerbehebung bei Exporten]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).
{% endalert %}