{% if include.section == "Differing audience size" %}

Die Größe der Zielpopulation, die in einer Campaign oder einem Canvas angezeigt wird, kann sich von der [Größe der erreichbaren Zielgruppe für ein Segment]({{site.baseurl}}/user_guide/engagement_tools/segments/measuring_segment_size#segment-membership-calculation) unterscheiden, selbst wenn Sie dieses Segment ohne zusätzliche Filter direkt in Ihre Campaign oder Ihr Canvas einfügen.
Dafür kann es mehrere Gründe geben:

- Wenn eine globale Kontrollgruppe für eine Campaign oder ein Canvas gilt, werden Nutzer:innen in dieser globalen Kontrollgruppe bei der Zählung der erreichbaren Nutzer:innen ausgeschlossen.
- Die Zielpopulation einer Campaign oder eines Canvas schließt Nutzer:innen aus, die nicht über die verschiedenen Nachrichten-Kanäle kontaktiert werden können; das Verhalten unterscheidet sich von Kanal zu Kanal. So schließt die erreichbare Zielgruppe für eine Campaign oder ein Canvas beispielsweise Nutzer:innen aus, die abgemeldet, als Spam markiert (bei E-Mails) oder als Hard Bounce (bei E-Mails) eingestuft sind. Das Segment selbst schließt jedoch nur Opt-outs aus, wenn es die geschätzte Anzahl der per E-Mail erreichbaren Nutzer:innen anzeigt.
- Braze sendet SMS-Nachrichten nur an Nutzer:innen innerhalb der ausgewählten Abo-Gruppe. Daher schließt die SMS-Zielpopulation für eine Campaign oder ein Canvas auch alle Nutzer:innen aus, die nicht zu Ihrer ausgewählten Abo-Gruppe gehören.

{% endif %}

{% if include.section == "Refresh settings" %}

Wenn Sie Ihre Erweiterung nicht regelmäßig aktualisieren müssen, können Sie sie ohne Aktualisierungseinstellungen speichern. Braze generiert Ihre Segmenterweiterung dann standardmäßig auf Grundlage der aktuellen Nutzerzugehörigkeit zu diesem Zeitpunkt. Verwenden Sie das Standardverhalten, wenn Sie die Zielgruppe nur einmal generieren und sie dann mit einer einmaligen Campaign ansprechen möchten.

Die Verarbeitung Ihres Segments beginnt immer nach dem ersten Speichern. Jedes Mal, wenn Ihr Segment aktualisiert wird, führt Braze das Segment erneut aus und aktualisiert die Segmentmitgliedschaft, um die Nutzer:innen in Ihrem Segment zum Zeitpunkt der Aktualisierung widerzuspiegeln. So können Ihre wiederkehrenden Campaigns die relevantesten Nutzer:innen erreichen.

#### Einrichten einer wiederkehrenden Aktualisierung {#setting-up-a-recurring-refresh}

Um einen wiederkehrenden Zeitplan einzurichten, wählen Sie **Aktualisierung aktivieren**. Die Option zur Festlegung von Aktualisierungseinstellungen ist für alle Arten von Segmenterweiterungen verfügbar, einschließlich SQL-Segmente, CDI-Segmenterweiterungen und einfache formularbasierte Segmenterweiterungen.

{% alert important %}
Um Ihre Datenverwaltung zu optimieren, werden die Aktualisierungseinstellungen für nicht verwendete Segmenterweiterungen automatisch deaktiviert. Segmenterweiterungen gelten als ungenutzt, wenn sie:

- In keinen aktiven oder inaktiven (Entwurf, gestoppt, archiviert) Campaigns, Canvases oder Segmenten verwendet werden; oder
- Seit mehr als 7 Tagen nicht geändert wurden

Braze benachrichtigt den Unternehmenskontakt und die erstellende Person der Erweiterung, wenn diese Einstellung deaktiviert wird. Die Option, Erweiterungen täglich zu regenerieren, kann jederzeit wieder aktiviert werden.
{% endalert %}

#### Auswählen Ihrer Aktualisierungseinstellungen {#selecting-your-refresh-settings}

![Aktualisierungsintervall-Einstellungen mit einer wöchentlichen Aktualisierungsfrequenz, einer Startzeit von 10 Uhr und Montag als ausgewähltem Tag.]({% image_buster /assets/img/segment/segment_interval_settings.png %}){: style="max-width:50%;"}

Im Panel **Aktualisierungsintervall-Einstellungen** können Sie die Häufigkeit auswählen, mit der diese Segmenterweiterung aktualisiert wird: stündlich, täglich, wöchentlich oder monatlich. Sie müssen außerdem die genaue Uhrzeit (in der Zeitzone Ihres Unternehmens) für die Aktualisierung angeben, z. B.:

- Wenn Sie eine E-Mail-Campaign haben, die jeden Montag um 11 Uhr Unternehmenszeit versendet wird, und Sie sicherstellen möchten, dass Ihr Segment kurz vor dem Versand aktualisiert wird, sollten Sie einen wöchentlichen Aktualisierungszeitplan montags um 10 Uhr wählen.
- Wenn Sie möchten, dass Ihr Segment jeden Tag aktualisiert wird, wählen Sie die tägliche Aktualisierungshäufigkeit und dann die Tageszeit für die Aktualisierung aus.

{% alert note %}
Die Möglichkeit, einen stündlichen Aktualisierungszeitplan festzulegen, ist für formularbasierte Segmenterweiterungen nicht verfügbar (Sie können jedoch tägliche, wöchentliche oder monatliche Zeitpläne festlegen).
{% endalert %}

#### Credit-Verbrauch und zusätzliche Kosten {#credit-consumption-and-additional-costs}

Da bei Aktualisierungen die Abfrage Ihres Segments erneut ausgeführt wird, verbraucht jede Aktualisierung für SQL-Segmente SQL-Segment-Credits, und jede Aktualisierung für CDI-Segmenterweiterungen verursacht Kosten in Ihrem Drittanbieter-Data-Warehouse.

{% alert note %}
Segmente können aufgrund von Datenverarbeitungszeiten bis zu 60 Minuten für die Aktualisierung benötigen. Segmente, die gerade aktualisiert werden, haben in Ihrer Segmenterweiterungsliste den Status „In Bearbeitung“. Dies hat einige Auswirkungen:

- Um die Verarbeitung Ihres Segments vor einer bestimmten Zeit abzuschließen, wählen Sie eine Aktualisierungszeit, die 60 Minuten früher liegt.
- Für eine bestimmte Segmenterweiterung kann jeweils nur eine Aktualisierung gleichzeitig erfolgen. Wenn ein Konflikt auftritt, bei dem eine neue Aktualisierung gestartet wird, während eine bestehende Aktualisierung bereits verarbeitet wird, bricht Braze die neue Aktualisierungsanfrage ab und setzt die laufende Verarbeitung fort.
{% endalert %}

#### Kriterien zur automatischen Deaktivierung veralteter Erweiterungen {#criteria-to-automatically-disable-stale-extensions}

Geplante Aktualisierungen werden automatisch deaktiviert, sobald eine Segmenterweiterung veraltet ist. Eine Segmenterweiterung gilt als veraltet, wenn sie die folgenden Kriterien erfüllt:

- Nicht in aktiven Campaigns oder Canvases verwendet
- In keinem Segment verwendet, das in einer aktiven Campaign oder einem Canvas eingesetzt wird
- In keinem Segment verwendet, für das [Analytics-Tracking]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking) aktiviert ist
- Seit mehr als sieben Tagen nicht geändert wurde
- Seit mehr als sieben Tagen nicht zu einer Campaign, einem Canvas (einschließlich Entwürfen) oder einem Segment hinzugefügt wurde

Wenn die geplante Aktualisierung für eine Segmenterweiterung deaktiviert wird, erhält diese Erweiterung eine entsprechende Benachrichtigung.

![Eine Benachrichtigung mit dem Hinweis: „Geplante Aktualisierungen wurden für diese Erweiterung deaktiviert, da sie in keinen aktiven Campaigns, Canvases oder Segmenten verwendet wird. Die Segmenterweiterung wurde am 23. Februar 2025 um 00:00 Uhr deaktiviert.“]({% image_buster /assets/img/segment/segment_extension_disabled.png %})

Wenn Sie bereit sind, eine veraltete Segmenterweiterung zu verwenden, überprüfen Sie die Aktualisierungseinstellungen, wählen Sie den Aktualisierungszeitplan, der zu Ihrem Anwendungsfall passt, und speichern Sie dann alle Änderungen.

{% endif %}

{% if include.section == "same channel identifier" %}

Wenn eine Nachricht empfangen, geöffnet oder angeklickt wird, aktualisiert Braze die Daten für alle Profile, die denselben Kanal-Bezeichner wie das Profil teilen, das die Interaktion protokolliert hat (z. B. dieselbe E-Mail-Adresse bei E-Mails oder dieselbe Telefonnummer bei SMS oder WhatsApp). Nutzer:innen, die einen Bezeichner mit einer Person teilen, die die Nachricht empfangen, geöffnet oder angeklickt hat, können diesem Filter entsprechen, auch wenn sie ursprünglich nicht in der Campaign enthalten waren oder die Nachricht nicht direkt erhalten haben.

{% endif %}

{% if include.section == "Canvas-Variante archived segment" %}

### Eine Canvas-Variante kann aufgrund eines archivierten Segments nicht gelöscht werden {#cant-delete-a-canvas-variant-because-of-an-archived-segment}

Wenn Braze das Löschen einer Canvas-Variante blockiert, weil ein Segment-Filter diese Variante noch referenziert, öffnen Sie das Segment, das die Referenz verwendet – einschließlich archivierter Segmente – und entfernen Sie die Variante aus den Filtern. Nachdem Sie das Segment gespeichert haben, kehren Sie zum Canvas zurück und versuchen Sie erneut, die Variante zu löschen.

Um herauszufinden, welche Segmente ein Canvas referenzieren, öffnen Sie das Canvas und überprüfen Sie seine Zielgruppenfilter, oder prüfen Sie den Abschnitt [Messaging-Nutzung]({{site.baseurl}}/user_guide/audience/segments/managing_segments#messaging-use) jedes Segments auf verknüpfte Canvases.

{% endif %}