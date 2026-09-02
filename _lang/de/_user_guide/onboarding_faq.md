---
article_title: FAQ
hidden: true
permalink: /onboarding_faq/
excerpt_separator: ""
page_type: glossary
layout: onboarding_faq
description: "Diese Seite enthält eine Sammlung häufig gestellter Fragen, die nach Kategorien geordnet sind."

---

{% multi_lang_include video.html id="keAZAlBR9zc" source="youtube" %}


<!--- Users --->

{% api %}

### Wie gehe ich mit anonymen Nutzerdaten um? {#how-do-i-handle-anonymous-user-data}

{% apitags %}
Users
{% endapitags %}

Wenn ein Kundenprofil über das SDK erkannt wird, erstellt Braze zunächst ein anonymes Kundenprofil mit einer zugehörigen `braze_id`: einer eindeutigen Nutzerkennung, die von Braze festgelegt wird.

Um anonyme Nutzer:innen weiter zu verfolgen, können Sie [Nutzer-Aliase]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#user-aliases) implementieren, mit denen Sie anonyme Nutzer:innen mit einer Kennung versehen können. Diese Nutzer:innen können dann über ihre Aliase exportiert oder von der API referenziert werden.

Wenn ein anonymes Kundenprofil mit einem Alias zu einem späteren Zeitpunkt mit einer `external_id` erkannt wird, wird es wie ein normales identifiziertes Kundenprofil behandelt, behält aber seinen bestehenden Alias bei und kann weiterhin über diesen Alias referenziert werden.

Bei Alias-Nutzer:innen, die Sie mit identifizierten Nutzer:innen zusammenführen möchten, können Sie alle Felder zusammenführen, die für das tatsächliche Profil relevant sind, das Sie behalten möchten. Sie müssten diese Daten exportieren, bevor Sie sie mit unserem [Endpunkt „Kundenprofil nach Bezeichner exportieren“]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) aus dem Alias-Profil löschen. Anschließend können Sie unseren [Endpunkt „Nutzer:innen tracken“]({{site.baseurl}}/api/endpoints/user_data/post_user_track) verwenden, um diese Events in dem Profil zu veröffentlichen, das Sie behalten haben. Auf diese Weise bleiben alle Daten erhalten, die Sie beibehalten möchten, z. B. Attribute, die zuvor in einem Profil erfasst wurden, aber nicht im anderen.

Eine vollständige Aufschlüsselung der verschiedenen Methoden zur Erfassung neuer und bestehender Nutzerdaten in Braze finden Sie unter [Best Practices für die Datenerfassung]({{site.baseurl}}/user_guide/data/unification/user_data/best_practices).

{% endapi %}
{% api %}

### Wie kann ich Nutzer:innen importieren, die ich bereits außerhalb von Braze erfasst und identifiziert habe? {#how-can-i-import-users-i-have-already-collected-and-identified-outside-of-braze}

{% apitags %}
Users
{% endapitags %}

Um zuvor identifizierte Nutzer:innen zu importieren, können Sie eine CSV-Datei in Braze hochladen oder Daten über die API senden.

#### CSV

Sie können Nutzerprofile über CSV-Dateien unter **Zielgruppe** > **Nutzer:innen importieren** hochladen und aktualisieren. Beim Import Ihrer Kundendaten müssen Sie die eindeutige Kennung jedes Kunden angeben, auch bekannt als `external_id`.

Bevor Sie mit dem CSV-Import beginnen, sollten Sie mit Ihrem Entwicklerteam klären, wie die Nutzer:innen in Braze identifiziert werden. In der Regel handelt es sich dabei um eine intern verwendete Datenbank-ID. Diese sollte mit der Art und Weise übereinstimmen, wie Nutzer:innen vom Braze SDK auf Mobilgeräten und im Internet identifiziert werden, sodass jede:r Kund:in ein einziges Kundenprofil in Braze über alle Geräte hinweg hat. Erfahren Sie mehr über den [Kundenprofil-Lebenszyklus]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle) in Braze.

Wenn Sie in Ihrem Import eine `external_id` angeben, aktualisiert Braze alle vorhandenen Nutzer:innen mit derselben `external_id` oder erstellt eine:n neu identifizierte:n Nutzer:in mit dieser `external_id`, falls keine gefunden wird.

Weitere Informationen und den Download von CSV-Importvorlagen finden Sie unter [Nutzerimport]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv).

#### API

Um Nutzer:innen über die API hochzuladen, können Sie unseren [Endpunkt „Nutzer:innen tracken“]({{site.baseurl}}/api/endpoints/user_data/post_user_track) verwenden, um sie in Braze zu importieren.

Wenn Sie sich nicht sicher sind, ob die Person bereits in Braze existiert, können Sie unseren [Endpunkt „Kundenprofil nach Bezeichner exportieren“]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) implementieren, um dies zu überprüfen. Wenn Sie feststellen, dass die Person bereits in Braze vorhanden ist, können Sie unseren `/users/track`-Endpunkt verwenden, um die neuen Daten dem bereits vorhandenen Kundenprofil in Braze hinzuzufügen.

{% alert note %}
Beachten Sie die folgenden Besonderheiten bei der Verwendung des `/users/track`-Endpunkts:

- Wenn Sie über diesen Endpunkt Nutzer:innen erstellen, die nur einen Alias haben, müssen Sie das Flag `_update_existing_only` explizit auf „false“ setzen.
- Wenn Sie den Abo-Status mit diesem Endpunkt aktualisieren, wird sowohl die durch ihre externe ID angegebene Person (z. B. User1) als auch der Abo-Status aller Nutzer:innen mit derselben E-Mail-Adresse wie diese Person (User1) aktualisiert.
{% endalert %}

{% endapi %}
{% api %}

### Was ist der Unterschied zwischen den Push-Abo-Status? {#whats-the-difference-between-the-push-subscription-statuses}

{% apitags %}
Users
{% endapitags %}

Es gibt drei Optionen für den Push-Abo-Status: abonniert, eingewilligt und abgemeldet.

Standardmäßig muss der Push-Abo-Status Ihrer Nutzer:innen entweder „abonniert“ oder „eingewilligt“ sein und Push muss aktiviert sein, damit sie Ihre Nachrichten per Push erhalten können. Sie können diese Einstellung bei Bedarf beim Verfassen einer Nachricht überschreiben.

| Einwilligungsstatus | Beschreibung |
|---|---|
| Abonniert | Standard-Push-Abo-Status, wenn ein Kundenprofil in Braze erstellt wird. |
| Eingewilligt | Eine Person hat ausdrücklich den Wunsch geäußert, Push-Benachrichtigungen zu erhalten. Braze ändert den Einwilligungsstatus automatisch auf `Opted-In`, wenn eine Person eine Push-Aufforderung auf Betriebssystemebene akzeptiert.<br><br>Dies gilt nicht für Nutzer:innen mit Android 12 oder darunter. |
| Abgemeldet | Eine Person hat sich über Ihre Anwendung oder andere von Ihrer Marke angebotene Methoden explizit von Push abgemeldet. Standardmäßig richten sich Push-Campaigns von Braze nur an Nutzer:innen, die `Subscribed` oder `Opted-in` für Push sind. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Was ist der Unterschied zwischen den Push-Abo-Status?" }

{% endapi %}
{% api %}

### Was ist, wenn ich doppelte Nutzer:innen identifiziert habe? {#what-if-ive-identified-duplicated-users}

{% apitags %}
Users
{% endapitags %}

Wenn Sie doppelte Nutzer:innen identifiziert haben, müssen Sie diese Nutzerprofile bereinigen. Gehen Sie dazu wie folgt vor:

1. Exportieren Sie die Nutzerprofile über unseren `/users/export/ids`-Endpunkt.
2. Identifizieren Sie das korrekte Kundenprofil (letztendlich muss Ihr Team über die richtigen Informationen entscheiden) und entweder:
    - Führen Sie alle relevanten Felder des tatsächlichen Profils, das Sie behalten möchten, über den `/user/track`-Endpunkt zusammen.
    - Löschen Sie das doppelte, nicht benötigte Profil ohne Datenzusammenführung über den users/delete-Endpunkt. Wenn Sie ein Kundenprofil löschen, **gibt es keine Möglichkeit, die Informationen wiederherzustellen**.

{% alert important %}
Wir empfehlen, zunächst die neuen Nutzerprofile mit der korrekten `external_id` und den entsprechenden angepassten Attributen und Events zu importieren. Nachdem Nutzerprofile gelöscht wurden, können sie nicht wiederhergestellt werden – das Löschen sollte daher der allerletzte Schritt sein.
{% endalert %}

Einige zusätzliche Hinweise:

- Alle Engagement-Daten (z. B. erhaltene Campaigns oder Canvases) auf doppelten Nutzerprofilen gehen verloren. Die einzige Möglichkeit, den historischen Engagement-Kontext beizubehalten, besteht darin, ihn als angepasstes Attribut hinzuzufügen (z. B. als Array-Attribut aller erhaltenen Campaigns oder Canvases).
- Bei der Migration von Nutzerprofilen muss Ihr Team auch entscheiden, welches der doppelten Nutzerprofile beibehalten werden soll. Braze kann diese Entscheidung nicht treffen und Ihnen keine Liste der zu löschenden Profile bereitstellen.
- Letztendlich ist es wichtig, dass Ihr Team den Registrierungsprozess aus der Perspektive Ihrer Nutzer:innen bewertet und sicherstellt, dass die Methode `changeUser()` nur dann aufgerufen wird, wenn eine Person identifiziert wird.

{% endapi %}
{% api %}

<!-- Segments -->

### Wie erstelle ich ein Segment, wenn ich eine Gruppe von Nutzer:innen per CSV importiere? {#how-do-i-create-a-segment-when-i-import-a-group-of-users-through-csv}

{% apitags %}
Segments
{% endapitags %}

Um Ihre CSV-Datei zu importieren, navigieren Sie zur Seite **Nutzerimport** im Abschnitt „Nutzer:innen“. Die Tabelle **Letzte Importe** listet bis zu zwanzig Ihrer letzten Importe auf, mit Dateinamen, Anzahl der Zeilen in der Datei, Anzahl der erfolgreich importierten Zeilen, Gesamtzahl der Zeilen in jeder Datei und dem Status jedes Imports.

Der Bereich **CSV importieren** enthält Importanweisungen und einen Button zum Starten des Imports. Klicken Sie auf **CSV-Datei auswählen** und wählen Sie die gewünschte Datei aus. Bevor Sie dann auf **Import starten** klicken, haben Sie die Möglichkeit, Braze unter „Was sollen wir mit den Nutzer:innen in dieser CSV-Datei tun“ mitzuteilen, was mit dieser Liste geschehen soll.

Wählen Sie **Nutzer:innen in dieser CSV importieren und es ermöglichen, diese bestimmte Gruppe von Nutzer:innen als Gruppe erneut anzusprechen**, und wählen Sie dann **Automatisch ein Segment aus den Nutzer:innen erstellen, die aus dieser CSV importiert werden**. Nachdem Sie auf **Import starten** geklickt haben, lädt Braze Ihre Datei hoch, überprüft die Spaltenüberschriften und die Datentypen der einzelnen Spalten und erstellt ein Segment.

Um eine CSV-Vorlage herunterzuladen, siehe [Nutzerimport]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv).

{% endapi %}
{% api %}

### Welche Arten von Filtern kann ich bei der Erstellung eines Segments verwenden? {#what-types-of-filters-can-i-use-when-creating-a-segment}

{% apitags %}
Segments
{% endapitags %}

Das Braze SDK bietet Ihnen ein leistungsstarkes Arsenal an Filtern, mit denen Sie Ihre Nutzer:innen auf der Grundlage bestimmter Features und Attribute segmentieren und targetieren können. Sie können das Glossar der [Segmentierungsfilter]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) verwenden, um diese Filter nach Filterkategorie zu durchsuchen oder einzugrenzen (Angepasste Daten, Nutzeraktivität, Retargeting, Marketingaktivitäten, Nutzerattribute, Install-Attribution, soziale Aktivitäten, Tests, Sonstige).

{% endapi %}
{% api %}

### Wie richte ich Standort-Targeting ein, damit ich Nutzer:innen nach ihrem letzten Standort segmentieren und in meinen standortbezogenen Kampagnen und Strategien verwenden kann? {#how-do-i-set-up-location-targeting-so-that-i-can-segment-users-by-their-most-recent-location-and-use-it-in-my-location-based-campaigns-and-strategies}

{% apitags %}
Segments
{% endapitags %}

Navigieren Sie zur Seite **Segments** unter „Engagement“, um alle Ihre aktuellen Nutzersegmente anzuzeigen. Auf dieser Seite können Sie neue Segmente erstellen und benennen. Klicken Sie zum Starten auf **Segment erstellen** und geben Sie Ihrem Segment einen Namen.

Sobald Sie Ihr Segment erstellt haben, fügen Sie einen `Most Recent Location`-Filter hinzu, um Nutzer:innen nach dem letzten Ort zu targetieren, an dem sie Ihre App genutzt haben. Sie können Nutzer:innen entweder in einem kreisförmigen Standardbereich hervorheben oder einen benutzerdefinierten polygonalen Bereich erstellen.

- Bei kreisförmigen Bereichen können Sie den Ursprung verschieben und den Standortradius für Ihre Segmentierung anpassen.
- Bei polygonalen Bereichen können Sie genauer festlegen, welche Gebiete in Ihrem Segment enthalten sein sollen.

{% alert tip %}
Möchten Sie die Vorteile des Standort-Targetings mit Hilfe eines Braze-Partners nutzen? Schauen Sie sich unsere verfügbaren Braze-[Partner für kontextuelle Standortdaten]({{site.baseurl}}/partners/message_personalization) an.
{% endalert %}

{% endapi %}
{% api %}

### Wie kann ich präzise Listen von Nutzer:innen auf der Grundlage ihres angepassten Event- und Kaufverhaltens in den letzten 365 Tagen ansprechen? {#how-can-i-target-precise-lists-of-users-based-on-their-custom-event-and-purchase-behavior-in-the-past-365-days}

{% apitags %}
Segments
{% endapitags %}

Sie können [Segmenterweiterungen]({{site.baseurl}}/user_guide/audience/segments/segment_extension) verwenden! Segmenterweiterungen ermöglichen es Ihnen, eine präzisere Liste von Nutzer:innen zu targetieren, als dies mit einem regulären Segment möglich wäre.

Sie können bis zu 10 Segmenterweiterungen pro Workspace erstellen. Nachdem diese Erweiterungslisten generiert wurden, können sie als Filter in Ihre Segmente aufgenommen oder davon ausgeschlossen werden. Bei der Erstellung einer Segmenterweiterung können Sie auch angeben, dass die Liste alle 24 Stunden neu generiert werden soll.

1. Erweitern Sie unter „Engagements“ den Bereich **Segments** und klicken Sie auf **Segmenterweiterung**.
2. Klicken Sie in der Tabelle der Segmenterweiterungen auf **+ Neue Erweiterung erstellen**.
3. Benennen Sie Ihre Segmenterweiterung, indem Sie die Art der Nutzer:innen beschreiben, nach denen Sie filtern möchten. So stellen Sie sicher, dass diese Erweiterung bei der Verwendung als Filter in Ihrem Segment leicht und korrekt gefunden werden kann.
4. Wählen Sie zwischen einem Kauf- oder angepassten Event-Kriterium für das Targeting.
5. Wählen Sie aus, welchen gekauften Artikel oder welches angepasste Event Sie für Ihre Nutzerliste targetieren möchten.
6. Wählen Sie, wie oft (mehr als, weniger als oder gleich) die Person das Event abgeschlossen haben muss und wie viele Tage zurückgeblickt werden soll – bis zu 365 Tage.

Um die Targeting-Genauigkeit zu erhöhen, können Sie **Eigenschaftsfilter hinzufügen** wählen und anhand der spezifischen Eigenschaften Ihres Kaufs oder angepassten Events segmentieren. Braze unterstützt die Segmentierung von Event-Eigenschaften basierend auf String-, numerischen, booleschen und Zeitobjekten.

Wir unterstützen auch die Segmentierung basierend auf [verschachtelten Event-Eigenschaften]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects).

Segmenterweiterungen basieren auf der langfristigen Speicherung von Event-Eigenschaften und unterliegen nicht der 30-Tage-Speicherbegrenzung für angepasste Event-Eigenschaften. Das bedeutet, dass Sie auf Event-Eigenschaften zurückblicken können, die innerhalb des letzten Jahres getrackt wurden, und das Tracking wartet nicht, bis die Erweiterung eingerichtet wurde.

{% alert note %}
Die Verwendung von Event-Eigenschaften innerhalb von Segmenterweiterungen hat keinen Einfluss auf die Datenpunkt-Nutzung.
{% endalert %}

{% endapi %}
{% api %}

#### Segmenterweiterungen auf dem neuesten Stand halten {#keeping-segment-extensions-up-to-date}

{% apitags %}
Segments
{% endapitags %}

Sie können angeben, ob diese Erweiterung eine einmalige Momentaufnahme darstellen oder täglich neu generiert werden soll. Ihre Erweiterung beginnt immer nach dem ersten Speichern mit der Verarbeitung. Wenn Sie möchten, dass die Erweiterung täglich regeneriert wird, wählen Sie **Erweiterung täglich regenerieren** – die Regeneration beginnt dann jeden Tag gegen Mitternacht in der Zeitzone Ihres Unternehmens.

Wenn Sie fertig sind, klicken Sie auf **Speichern**. Ihre Erweiterung wird nun verarbeitet. Die Dauer der Generierung hängt davon ab, wie viele Nutzer:innen Sie haben, wie viele angepasste Events oder Kauf-Events Sie erfassen und wie viele Tage Sie im Verlauf zurückblicken.

Nachdem Sie eine Erweiterung erstellt haben, können Sie sie als Filter verwenden, wenn Sie ein Segment erstellen oder eine Zielgruppe für eine Campaign oder ein Canvas definieren. Wählen Sie zunächst `Braze Segment Extension` aus der Filterliste im Abschnitt **Nutzerattribute**. Wählen Sie in der Filterliste der Braze-Segmenterweiterung die Erweiterung aus, die Sie in dieses Segment aufnehmen oder davon ausschließen möchten. Um die Erweiterungskriterien einzusehen, klicken Sie auf **Erweiterungsdetails anzeigen**. Jetzt können Sie wie gewohnt mit der Erstellung Ihres Segments fortfahren.

{% endapi %}
{% api %}

<!-- Campaigns -->

### Wie erstelle ich eine Multichannel-Campaign? {#how-do-you-create-a-multichannel-campaign}

{% apitags %}
Campaigns
{% endapitags %}

Informationen zu den Einrichtungsschritten, unterstützten Kanälen und dem Wechsel zwischen Editoren finden Sie unter [Multichannel-Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign#create-a-multichannel-campaign) in **Campaign erstellen**.

{% endapi %}
{% api %}

### Wie kann ich mit dem Testen und Optimieren von Campaigns beginnen? {#what-are-some-ways-i-can-start-testing-and-optimizing-campaigns}

{% apitags %}
Campaigns
{% endapitags %}

Die Erstellung multivariater Campaigns und die Durchführung von Canvases mit mehreren Varianten sind ein guter Ansatzpunkt! Sie können zum Beispiel eine [multivariate Campaign]({{site.baseurl}}/user_guide/messaging/ab_testing) durchführen, um eine Nachricht mit verschiedenen Texten oder Betreffzeilen zu testen. Canvases mit mehreren Varianten sind hilfreich, um ganze Workflows zu testen.

{% endapi %}
{% api %}

### Warum gibt es einen Unterschied zwischen der Anzahl der eindeutigen Empfänger:innen und der Anzahl der Sendungen für eine bestimmte Campaign oder ein bestimmtes Canvas? {#why-is-there-a-difference-between-the-number-of-unique-recipients-and-the-number-of-sends-for-a-given-campaign-or-canvas}

{% apitags %}
Campaigns
{% endapitags %}

Eine mögliche Erklärung für diesen Unterschied könnte darin liegen, dass bei der Campaign oder dem Canvas die Wiederzulassung aktiviert ist. Wenn diese Option aktiviert ist, können Nutzer:innen, die sich für das Segment und die Zustellungseinstellungen qualifizieren, die Nachricht mehr als einmal erhalten. Wenn die Wiederzulassung nicht aktiviert ist, liegt die wahrscheinliche Erklärung für den Unterschied zwischen Sendungen und eindeutigen Empfänger:innen darin, dass Nutzer:innen mehrere Geräte über verschiedene Plattformen hinweg mit ihren Profilen verknüpft haben.

Wenn Sie z. B. ein Canvas haben, das sowohl iOS- als auch Web-Push-Benachrichtigungen enthält, könnte eine Person mit sowohl einem mobilen als auch einem Desktop-Gerät mehr als eine Nachricht erhalten.

{% endapi %}
{% api %}

### Was bietet die Zustellung in der lokalen Zeitzone? {#what-does-local-time-zone-delivery-offer}

{% apitags %}
Campaigns
{% endapitags %}

Die Zustellung in der lokalen Zeitzone ermöglicht es Ihnen, Messaging-Campaigns an ein Segment basierend auf der individuellen Zeitzone der Nutzer:innen zu senden. Ohne die Zustellung in der lokalen Zeitzone werden Campaigns auf der Grundlage der Zeitzoneneinstellungen Ihres Unternehmens in Braze geplant.

Wenn beispielsweise ein in London ansässiges Unternehmen eine Campaign um 12 Uhr mittags versendet, erreicht sie die Nutzer:innen an der amerikanischen Westküste um 4 Uhr morgens. Wenn Ihre App nur in bestimmten Ländern verfügbar ist, stellt dies möglicherweise kein Risiko für Sie dar. Andernfalls empfehlen wir Ihnen dringend, das Versenden von Push-Benachrichtigungen am frühen Morgen an Ihre Nutzerbasis zu vermeiden!

{% endapi %}
{% api %}

### Wie erkennt Braze die Zeitzone einer Person? {#how-does-braze-recognize-a-users-time-zone}

{% apitags %}
Campaigns
{% endapitags %}

Braze ermittelt automatisch die Zeitzone einer Person anhand ihres Geräts. Dies dient der Zeitzonengenauigkeit und der vollständigen Abdeckung Ihrer Nutzer:innen. Nutzer:innen, die über die User API oder anderweitig ohne Zeitzone erstellt werden, haben die Zeitzone Ihres Unternehmens als Standardzeitzone, bis sie in Ihrer App vom SDK erkannt werden.

Sie können die Zeitzone Ihres Unternehmens in Ihren [Unternehmenseinstellungen]({{site.baseurl}}/user_guide/administer/global/admin_settings) überprüfen.

{% endapi %}
{% api %}

### Wie plane ich eine Campaign für die lokale Zeitzone? {#how-do-i-schedule-a-local-time-zone-campaign}

{% apitags %}
Campaigns
{% endapitags %}

Wenn Sie eine Campaign planen, müssen Sie auswählen, dass sie zu einer bestimmten Zeit gesendet werden soll, und dann die Option **Campaign an Nutzer:innen in ihrer lokalen Zeitzone senden** wählen.

Braze empfiehlt ausdrücklich, alle Campaigns mit lokaler Zeitzone 24 Stunden im Voraus zu planen. Da eine solche Campaign im Laufe eines ganzen Tages versendet werden muss, stellt eine 24-Stunden-Vorausplanung sicher, dass Ihre Nachricht Ihr gesamtes Segment erreicht. Sie können diese Campaigns jedoch bei Bedarf auch weniger als 24 Stunden im Voraus planen. Beachten Sie, dass Braze keine Nachrichten an Nutzer:innen sendet, die die Sendezeit um mehr als 1 Stunde verpasst haben.

Wenn es beispielsweise 13 Uhr ist und Sie eine Campaign für die lokale Zeitzone um 15 Uhr planen, wird die Campaign sofort an alle Nutzer:innen gesendet, deren Ortszeit zwischen 15 und 16 Uhr liegt, aber nicht an Nutzer:innen, deren Ortszeit 17 Uhr ist. Außerdem muss die Sendezeit, die Sie für Ihre Campaign wählen, in der Zeitzone Ihres Unternehmens noch nicht verstrichen sein.

Das Bearbeiten einer Campaign mit lokaler Zeitzone, die weniger als 24 Stunden im Voraus geplant wurde, ändert den Zeitplan der Nachricht nicht. Wenn Sie eine Campaign mit lokaler Zeitzone so bearbeiten, dass sie zu einem späteren Zeitpunkt gesendet wird (z. B. 19 Uhr statt 18 Uhr), erhalten die Nutzer:innen, die sich zum Zeitpunkt der ursprünglichen Sendezeit im Zielsegment befanden, die Nachricht weiterhin zur ursprünglichen Zeit (18 Uhr). Wenn Sie eine Campaign mit lokaler Zeitzone bearbeiten, um zu einer früheren Zeit zu senden (z. B. 16 Uhr statt 17 Uhr), wird die Campaign trotzdem an alle Segmentmitglieder zur ursprünglichen Zeit (17 Uhr) gesendet.

{% alert note %}
Bei Canvas-Schritten müssen Nutzer:innen nicht 24 Stunden im Schritt sein, um den nächsten Schritt bei der Zustellung zur Ortszeit zu erhalten.
{% endalert %}

Wenn Sie Nutzer:innen erlaubt haben, sich erneut für die Campaign zu qualifizieren, erhalten sie sie wieder zur ursprünglichen Zeit (17 Uhr). Bei allen nachfolgenden Vorkommen Ihrer Campaign werden Ihre Nachrichten jedoch nur zur aktualisierten Zeit gesendet.

{% endapi %}
{% api %}

### Wann werden Änderungen an Campaigns mit lokaler Zeitzone wirksam? {#when-do-changes-to-local-time-zone-campaigns-take-effect}

{% apitags %}
Campaigns
{% endapitags %}

Zielsegmente für Campaigns mit lokaler Zeitzone sollten bei zeitbasierten Filtern ein Zeitfenster von mindestens 48 Stunden enthalten, um die Zustellung an das gesamte Segment zu gewährleisten. Betrachten Sie zum Beispiel ein Segment, das Nutzer:innen an ihrem zweiten Tag mit den folgenden Filtern targetiert:

- App erstmals vor mehr als 1 Tag verwendet
- App erstmals vor weniger als 2 Tagen verwendet

Die Zustellung in der lokalen Zeitzone kann Nutzer:innen in diesem Segment verfehlen, abhängig von der Zustellungszeit und der lokalen Zeitzone der Nutzer:innen. Das liegt daran, dass eine Person das Segment zu dem Zeitpunkt verlassen kann, zu dem ihre Zeitzone die Zustellung triggert.

{% endapi %}
{% api %}

### Welche Änderungen kann ich an geplanten Campaigns vor dem Start vornehmen? {#what-changes-can-i-make-to-scheduled-campaigns-ahead-of-launch}

{% apitags %}
Campaigns
{% endapitags %}

Wenn die Campaign geplant ist, müssen Änderungen an allem außer der Nachrichtenkomposition vorgenommen werden, bevor wir die Nachrichten in die Warteschlange stellen. Wie bei allen Campaigns können Sie Konversions-Events nicht mehr bearbeiten, nachdem die Campaign gestartet wurde.

{% endapi %}
{% api %}

### Was ist die „sichere Zone“, bevor Nachrichten einer geplanten Campaign in die Warteschlange gestellt werden? {#what-is-the-safe-zone-before-messages-on-a-scheduled-campaign-are-queued}

{% apitags %}
Campaigns
{% endapitags %}

- Einmalig geplante Campaigns können bis zur geplanten Sendezeit bearbeitet werden.
- Wiederkehrend geplante Campaigns können bis zur geplanten Sendezeit bearbeitet werden.
- Campaigns mit lokaler Sendezeit können bis zu 24 Stunden vor der geplanten Sendezeit bearbeitet werden.
- Campaigns mit optimaler Sendezeit können bis zu 24 Stunden vor dem Tag, an dem die Campaign versendet werden soll, bearbeitet werden.

{% endapi %}
{% api %}

### Was passiert, wenn ich eine Bearbeitung innerhalb der „sicheren Zone“ vornehme? {#what-if-i-make-an-edit-within-the-safe-zone}

{% apitags %}
Campaigns
{% endapitags %}

Eine Änderung der Sendezeit von Campaigns innerhalb dieses Zeitraums kann zu unerwünschtem Verhalten führen, zum Beispiel:

- Braze sendet keine Nachrichten an Nutzer:innen, die die Sendezeit um mehr als eine Stunde verpasst haben.
- Nachrichten, die bereits in der Warteschlange waren, werden möglicherweise weiterhin zur ursprünglich eingereihten Zeit gesendet und nicht zur angepassten Zeit.

{% endapi %}
{% api %}

### Was soll ich tun, wenn die „sichere Zone“ bereits überschritten ist? {#what-should-i-do-if-the-safe-zone-has-already-passed}

{% apitags %}
Campaigns
{% endapitags %}

Um sicherzustellen, dass Campaigns wie gewünscht funktionieren, empfehlen wir, die aktuelle Campaign zu stoppen (dadurch werden alle Nachrichten in der Warteschlange gestoppt). Sie können die Campaign dann duplizieren, die erforderlichen Änderungen vornehmen und die neue Campaign starten. Möglicherweise müssen Sie Nutzer:innen von dieser Campaign ausschließen, die bereits die erste Campaign erhalten haben.

Stellen Sie sicher, dass Sie die Campaign-Zeitpläne so anpassen, dass der Versand in der jeweiligen Zeitzone berücksichtigt wird.

{% endapi %}
{% api %}

### Wann bewertet Braze Nutzer:innen für die Zustellung in der lokalen Zeitzone? {#when-does-braze-evaluate-users-for-local-time-zone-delivery}

{% apitags %}
Campaigns
{% endapitags %}

Braze bewertet Nutzer:innen auf ihre Zugangsberechtigung zu folgenden Zeitpunkten:

- Zur Samoa-Zeit (UTC+13) des geplanten Tages
- Zur Ortszeit der Person am geplanten Tag

Damit eine Person für den Eintritt berechtigt ist, muss sie beide Prüfungen bestehen. Wenn ein Canvas beispielsweise am 7. August 2021 um 14 Uhr Ortszeit gestartet werden soll, würde das Targeting einer Person in New York die folgenden Berechtigungsprüfungen erfordern:

- New York am 6. August 2021 um 21 Uhr
- New York am 7. August 2021 um 14 Uhr

Um einzutreten, muss eine Person Ihre Zielgruppe und Filter zu beiden Bewertungszeitpunkten erfüllen. Wenn die Person bei der ersten Prüfung nicht berechtigt ist, führt Braze die zweite Prüfung nicht durch. Es gibt keine Mindestdauer, die eine Person vor dem Start im Segment gewesen sein muss – es zählt nur die Berechtigung bei jeder Prüfung.

Dieses Bewertungsverhalten ist unabhängig davon, [wie weit im Voraus Sie die Campaign im Dashboard planen]({{site.baseurl}}/user_guide/messaging/campaigns/faq#how-do-i-schedule-a-local-time-zone-campaign). Die vollständige Erklärung, Beispiele und Planungshinweise finden Sie unter [Wann bewertet Braze Nutzer:innen für die Zustellung in der lokalen Zeitzone?]({{site.baseurl}}/user_guide/messaging/campaigns/faq#when-does-braze-evaluate-users-for-local-time-zone-delivery) und [Wie plane ich eine Campaign für die lokale Zeitzone?]({{site.baseurl}}/user_guide/messaging/campaigns/faq#how-do-i-schedule-a-local-time-zone-campaign) in den Campaign-FAQ.

{% endapi %}
{% api %}

### Warum stimmt die Anzahl der Nutzer:innen, die eine Campaign betreten, nicht mit der erwarteten Anzahl überein? {#why-does-the-number-of-users-entering-a-campaign-not-match-the-expected-number}

{% apitags %}
Campaigns
{% endapitags %}

Die Anzahl der Nutzer:innen, die eine Campaign betreten, kann von der erwarteten Anzahl abweichen, da Zielgruppen und Trigger unterschiedlich ausgewertet werden. In Braze wird eine Zielgruppe vor dem Trigger ausgewertet (außer bei einem [Trigger „Attributänderung“]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers#change-custom-attribute-value)). Dies führt dazu, dass Nutzer:innen aus der Campaign herausfallen, wenn sie zunächst nicht Teil Ihrer ausgewählten Zielgruppe sind, bevor Trigger-Aktionen ausgewertet werden.

{% endapi %}
{% api %}

<!-- Canvases -->

### Was passiert, wenn die Zielgruppe und die Sendezeit bei einem Canvas mit einer Variante, aber mehreren Verzweigungen identisch sind? {#what-happens-if-the-audience-and-send-time-are-identical-for-a-canvas-that-has-one-variant-but-multiple-branches}

{% apitags %}
Canvases
{% endapitags %}

Für jeden Schritt wird ein Auftrag in die Warteschlange gestellt – sie werden ungefähr zur gleichen Zeit ausgeführt, und einer von ihnen „gewinnt“. In der Praxis kann dies einigermaßen gleichmäßig verteilt sein, aber es ist wahrscheinlich, dass zumindest eine leichte Tendenz zu dem Schritt besteht, der zuerst erstellt wurde.

Außerdem können wir keine Garantien dafür geben, wie diese Verteilung genau aussehen wird. Wenn Sie eine gleichmäßige Aufteilung sicherstellen möchten, fügen Sie einen Filter für [zufällige Bucket-Nummern]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers) hinzu.

{% endapi %}
{% api %}

### Was passiert, wenn Sie ein Canvas stoppen? {#what-happens-when-you-stop-a-canvas}

{% apitags %}
Canvases
{% endapitags %}

Wenn Sie ein Canvas stoppen, gilt Folgendes:

- Nutzer:innen werden daran gehindert, das Canvas zu betreten.
- Es werden keine weiteren Nachrichten gesendet, unabhängig davon, wo sich eine Person im Ablauf befindet.
    - **Ausnahme:** E-Mail-Canvases lassen sich nicht sofort stoppen. Nachdem die Sendeanfragen an SendGrid gesendet wurden, können wir nicht mehr verhindern, dass sie zugestellt werden.

{% alert note %}
Das Stoppen eines Canvas beendet nicht den Aufenthalt von Nutzer:innen, die in einem Schritt warten. Wenn Sie das Canvas wieder aktivieren und die Nutzer:innen noch warten, werden sie den Schritt abschließen und zur nächsten Komponente übergehen. Wenn jedoch der Zeitpunkt, zu dem die Person zur nächsten Komponente hätte weitergehen sollen, bereits verstrichen ist, wird sie stattdessen das Canvas verlassen.
{% endalert %}

{% endapi %}
{% api %}

### Wann wird ein Ausnahme-Event ausgelöst? {#when-does-an-exception-event-trigger}

{% apitags %}
Canvases
{% endapitags %}

Ausnahme-Events werden nur ausgelöst, während die Person auf die Canvas-Komponente wartet, mit der das Event verknüpft ist. Wenn eine Person eine Aktion im Voraus durchführt, wird das Ausnahme-Event nicht ausgelöst.

Wenn Sie Nutzer:innen ausschließen möchten, die ein bestimmtes Event bereits durchgeführt haben, verwenden Sie stattdessen [Filter]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters).

{% endapi %}
{% api %}

### Wie wirkt sich die Bearbeitung eines Canvas auf Nutzer:innen aus, die sich bereits im Canvas befinden? {#how-does-editing-a-canvas-affect-users-already-in-the-canvas}

{% apitags %}
Canvases
{% endapitags %}

Wenn Sie einige Schritte eines mehrstufigen Canvas bearbeiten, erhalten Nutzer:innen, die bereits in der Zielgruppe waren, aber die Schritte noch nicht erhalten haben, die aktualisierte Version der Nachricht. Beachten Sie, dass dies nur geschieht, wenn sie für den Schritt noch nicht ausgewertet wurden.

Weitere Informationen darüber, was Sie nach dem Start bearbeiten können und was nicht, finden Sie unter [Canvas nach dem Start ändern]({{site.baseurl}}/post-launch_edits).

{% endapi %}
{% api %}

### Wie werden Nutzer-Conversions in einem Canvas getrackt? {#how-are-user-conversions-tracked-in-a-canvas}

{% apitags %}
Canvases
{% endapitags %}

Eine Person kann nur einmal pro Canvas-Eintritt konvertieren.

Conversions werden der zuletzt empfangenen Nachricht für diesen Eintritt zugeordnet. Der Zusammenfassungsblock am Anfang eines Canvas spiegelt alle Conversions wider, die von Nutzer:innen innerhalb dieses Pfads durchgeführt wurden, unabhängig davon, ob sie eine Nachricht erhalten haben. Jeder nachfolgende Schritt zeigt nur Conversions an, die stattfanden, während dieser der letzte Schritt war, den die Person erhalten hat.

{% details Anwendungsfälle %}

#### Anwendungsfall 1 {#use-case-1}

Es gibt einen Canvas-Pfad mit 10 Push-Benachrichtigungen und das Konversions-Event ist „Sitzungsbeginn“ („App öffnen“):

- Person A öffnet die App nach dem Eintritt, aber bevor sie die erste Nachricht erhält.
- Person B öffnet die App nach jeder Push-Benachrichtigung.

**Ergebnis:**
Die Zusammenfassung zeigt zwei Conversions an, während die einzelnen Schritte eine Conversion beim ersten Schritt und null bei allen nachfolgenden Schritten anzeigen.

{% alert note %}
Wenn Ruhezeiten zum Zeitpunkt des Konversions-Events aktiv sind, gelten die gleichen Regeln.
{% endalert %}

#### Anwendungsfall 2 {#use-case-2}

Es gibt ein einstufiges Canvas mit Ruhezeiten:

1. Die Person betritt das Canvas.
2. Der erste Schritt hat keine Verzögerung, liegt aber innerhalb der Ruhezeiten, sodass die Nachricht unterdrückt wird.
3. Die Person führt das Konversions-Event durch.

**Ergebnis:**
Die Person wird in der gesamten Canvas-Variante als konvertiert gezählt, aber nicht im Schritt, da sie den Schritt nicht erhalten hat.

{% enddetails %}

{% endapi %}
{% api %}

### Ist Canvas Analytics oder der Segmenter genauer, wenn es um die Anzahl der eindeutigen Nutzer:innen geht? {#when-looking-at-the-number-of-unique-users-is-canvas-analytics-or-the-segmenter-more-accurate}

{% apitags %}
Canvases
{% endapitags %}

Der Segmenter liefert genauere Statistiken für eindeutige Nutzerdaten als Canvas- oder Campaign-Statistiken. Das liegt daran, dass Canvas- und Campaign-Statistiken Zahlen sind, die Braze inkrementiert, wenn etwas passiert – es gibt also Variablen, die dazu führen können, dass diese Zahl von der des Segmenters abweicht. So können Nutzer:innen zum Beispiel mehr als einmal für ein Canvas oder eine Campaign konvertieren.

{% endapi %}
{% api %}

### Warum stimmt die Anzahl der Nutzer:innen, die ein Canvas betreten, nicht mit der erwarteten Anzahl überein? {#why-does-the-number-of-users-entering-a-canvas-not-match-the-expected-number}

{% apitags %}
Canvases
{% endapitags %}

Die Anzahl der Nutzer:innen, die ein Canvas betreten, kann von der erwarteten Anzahl abweichen, da Zielgruppen und Trigger unterschiedlich ausgewertet werden. In Braze wird eine Zielgruppe vor dem Trigger ausgewertet (außer bei einem Trigger [„Attributänderung“]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers#change-custom-attribute-value)). Dies führt dazu, dass Nutzer:innen aus dem Canvas herausfallen, wenn sie nicht Teil Ihrer ausgewählten Zielgruppe sind, bevor Trigger-Aktionen ausgewertet werden.

{% endapi %}
{% api %}

<!-- Analytics -->

### Welche Metriken misst Braze? {#what-metrics-does-braze-measure}

{% apitags %}
Analytics
{% endapitags %}

Je nach Kanal misst Braze eine Vielzahl von Metriken, die es Ihnen ermöglichen, den Erfolg einer Campaign zu bestimmen und zukünftige Campaigns zu planen. Eine umfassende Liste finden Sie in unserem [Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/analytics/metrics_glossary).

{% endapi %}
{% api %}

### Wie wird der Umsatz in Braze berechnet? {#how-is-revenue-calculated-in-braze}

{% apitags %}
Analytics
{% endapitags %}

Auf der Seite **Umsatz** können Sie Daten zu Umsätzen oder Käufen über bestimmte Zeiträume, für ein bestimmtes Produkt oder die Gesamtumsätze bzw. Gesamtkäufe Ihrer App einsehen. Diese Umsatzzahlen werden aus den Käufen generiert, die von Campaign-Empfänger:innen innerhalb eines bestimmten Conversion-Zeitraums getätigt werden.

Dabei ist es wichtig zu beachten, dass Braze ein Marketing-Tool und kein Tool zur Umsatzverwaltung ist. Unser [Kauf-Objekt]({{site.baseurl}}/api/objects_filters/purchase_object) unterstützt keine Erstattungen und Stornierungen, sodass Sie beim Vergleich mit anderen Tools möglicherweise Abweichungen feststellen.

{% endapi %}
{% api %}

### Welche Berichtsfunktionen bietet Currents? {#what-reporting-capabilities-does-currents-enable}

{% apitags %}
Analytics
{% endapitags %}

Unser Currents-Tool streamt kontinuierlich sowohl Messaging-Engagement- als auch Kundenverhaltensdaten an einen unserer zahlreichen Datenpartner. So können Sie die einzigartigen und wertvollen Daten, die Braze erstellt, nutzen, um Ihre Business-Intelligence- und Analytics-Bemühungen bei anderen erstklassigen Partnern voranzubringen.

Diese Daten gehen über Messaging-Engagement-Metriken hinaus und können auch komplexere Zahlen wie die Performance von angepassten Attributen und Events umfassen. Weitere Details finden Sie in unserem [Glossar der Currents-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events).

{% endapi %}
{% api %}

### Wie kann ich einen wiederkehrenden Engagement-Bericht planen? {#how-can-i-schedule-a-recurring-engagement-report}

{% apitags %}
Analytics
{% endapitags %}

So planen Sie einen wiederkehrenden Engagement-Bericht:

1. Navigieren Sie in Ihrem Dashboard-Konto unter **Daten** zu **Engagement-Berichte**.
2. Klicken Sie auf **+ Neuen Bericht erstellen**.
3. Fügen Sie die [Campaigns und Canvas-Nachrichten]({{site.baseurl}}/user_guide/analytics/reports/engagement_reports#manually-select-campaigns-or-canvases) (einzeln oder [nach Tag]({{site.baseurl}}/user_guide/analytics/reports/engagement_reports#automatically-select-campaigns-or-canvases)) hinzu, die Sie in Ihrem Bericht zusammenstellen möchten.
4. [Fügen Sie Statistiken]({{site.baseurl}}/user_guide/analytics/reports/engagement_reports#add-statistics-to-your-reports) zu Ihrem Bericht hinzu.
5. Wählen Sie die Komprimierung und das Trennzeichen für Ihren Bericht.
6. Geben Sie die E-Mail-Adressen der Unternehmensnutzer:innen ein, die diesen Bericht erhalten sollen.
7. Wählen Sie den [Zeitraum]({{site.baseurl}}/user_guide/analytics/reports/engagement_reports#select-time-frame) aus, für den Ihr Bericht Daten auswerten soll.
8. Wählen Sie die [Intervalle (täglich, wöchentlich usw.)]({{site.baseurl}}/user_guide/analytics/reports/engagement_reports#select-data-display), in denen Sie die Aufschlüsselung Ihrer Daten sehen möchten.
9. Planen Sie Ihren Bericht so, dass er [sofort gesendet wird]({{site.baseurl}}/user_guide/analytics/reports/engagement_reports#schedule-your-report) oder zu einem [bestimmten Zeitpunkt in der Zukunft]({{site.baseurl}}/user_guide/analytics/reports/engagement_reports#schedule-your-report).
10. Führen Sie den Bericht aus und öffnen Sie ihn in Ihrer E-Mail, wenn er eintrifft!

{% endapi %}
{% api %}

### Was ist der Unterschied zwischen Engagement-Berichten und dem Berichts-Builder? {#whats-the-difference-between-engagement-reports-and-the-report-builder}

{% apitags %}
Analytics
{% endapitags %}

Engagement-Berichte liefern Ihnen CSVs mit Engagement-Statistiken für bestimmte Nachrichten aus Campaigns und Canvases über eine getriggerte E-Mail. Bestimmte Daten werden auf Campaign- oder Canvas-Ebene aggregiert und nicht auf Ebene der einzelnen Varianten oder Schritte. Berichte werden nicht im Dashboard gespeichert, und eine erneute Ausführung des Berichts kann zu aktualisierten Statistiken führen.

Der Berichts-Builder ermöglicht es Ihnen, die Ergebnisse mehrerer Campaigns oder Canvases in einer einzigen Ansicht zu vergleichen, sodass Sie leicht feststellen können, welche Engagement-Strategien Ihre Schlüsselmetriken am stärksten beeinflusst haben. Sowohl für Campaigns als auch für Canvases können Sie Ihre Daten exportieren und Ihren Bericht speichern, um ihn in Zukunft einzusehen.

Weitere Informationen zur Verwendung von Berichten und Analytics in Braze finden Sie in der [Übersicht über Berichte]({{site.baseurl}}/user_guide/analytics/reports).

{% endapi %}