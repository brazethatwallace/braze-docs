---
nav_title: "Erweiterte Push-Campaign-Einstellungen"
article_title: "Erweiterte Push-Campaign-Einstellungen"
page_order: 5
page_layout: reference
description: "Dieser Referenzartikel behandelt erweiterte Android-Push-Campaign-Einstellungen wie Priorität, benutzerdefinierte URLs, Zustellungsoptionen und mehr."
platform: Android
channel:
  - push
tool:
  - Campaigns

---

# Erweiterte Push-Campaign-Einstellungen {#advanced-push-campaign-settings}

> Für Android- und Fire OS-Push-Benachrichtigungen, die über das Braze-Dashboard gesendet werden, stehen zahlreiche erweiterte Einstellungen zur Verfügung. Dieser Artikel beschreibt diese Features und wie Sie sie erfolgreich einsetzen.

## Benachrichtigungs-ID {#notification-id}

Eine Benachrichtigungs-ID ist ein eindeutiger Bezeichner für eine von Ihnen gewählte Nachrichtenkategorie, der den Messaging-Dienst anweist, nur die aktuellste Nachricht mit dieser ID zu berücksichtigen. Durch das Setzen einer Benachrichtigungs-ID können Sie nur die aktuellste und relevanteste Nachricht senden, anstatt einen Stapel veralteter, irrelevanter Nachrichten.

Um eine Benachrichtigungs-ID zuzuweisen, navigieren Sie zur Erstellungsseite der Push-Benachrichtigung, die Sie aktualisieren möchten, und wählen Sie den Tab **Settings** aus. Geben Sie dann eine Ganzzahl im Abschnitt **Notification ID** ein. Um diese Benachrichtigung nach dem Versand zu aktualisieren, senden Sie eine weitere Benachrichtigung mit derselben ID, die Sie zuvor verwendet haben.

![Feld für die Benachrichtigungs-ID.]({% image_buster /assets/img_archive/notification_ids.png %}){: style="max-width:60%;" }

## Gültigkeitsdauer (TTL) {#ttl}

Das Feld **TTL** ermöglicht es Ihnen, eine benutzerdefinierte Speicherdauer für Nachrichten beim Push-Messaging-Dienst festzulegen. Wenn das Gerät über die TTL hinaus offline bleibt, läuft die Nachricht ab und wird nicht zugestellt.

Um die Gültigkeitsdauer für Ihre Android-Push-Benachrichtigung zu bearbeiten, gehen Sie zum Composer und wählen Sie den Tab **Settings** aus. Suchen Sie das Feld **TTL** und geben Sie einen Wert in Tagen, Stunden oder Sekunden ein.

Die Standardwerte für die Gültigkeitsdauer werden von Ihren Admins auf der Seite [Push-Einstellungen]({{site.baseurl}}/user_guide/administer/global/workspace_settings/push_settings) festgelegt. Standardmäßig setzt Braze die Push TTL auf den Maximalwert für jeden Push-Messaging-Dienst. Während die Standard-TTL-Einstellungen global gelten, können Sie sie bei der Campaign-Erstellung auf Nachrichtenebene überschreiben. Dies ist hilfreich, wenn verschiedene Campaigns unterschiedliche Dringlichkeiten oder Zustellungsfenster erfordern.

Nehmen wir zum Beispiel an, Ihre App veranstaltet einen wöchentlichen Quizwettbewerb. Sie senden eine Push-Benachrichtigung eine Stunde vor Beginn. Indem Sie die TTL auf 1 Stunde setzen, stellen Sie sicher, dass Nutzer:innen, die die App nach Beginn des Wettbewerbs öffnen, keine Benachrichtigung über ein bereits gestartetes Ereignis erhalten.

{% details Best Practices %}

### Wann kürzere TTL sinnvoll sind {#when-to-use-shorter-ttl}

Kürzere TTLs stellen sicher, dass Nutzer:innen zeitnahe Benachrichtigungen für Ereignisse oder Aktionen erhalten, die schnell an Relevanz verlieren. Zum Beispiel:

- **Einzelhandel:** Senden einer Push-Benachrichtigung für einen Flash-Sale, der in 2 Stunden endet (TTL: 1–2 Stunden)
- **Essenslieferung:** Nutzer:innen benachrichtigen, wenn ihre Bestellung in der Nähe ist (TTL: 10–15 Minuten)
- **Transport-Apps:** Ankunfts-Updates für Fahrten teilen (TTL: wenige Minuten)
- **Erinnerungen:** Nutzer:innen benachrichtigen, wenn ein Webinar bald beginnt (TTL: unter 1 Stunde)

### Wann kürzere TTL vermieden werden sollten {#when-to-avoid-shorter-ttl}

- Wenn die Nachricht Ihrer Campaign über mehrere Tage oder Wochen relevant bleibt, wie z. B. Abo-Verlängerungserinnerungen oder laufende Aktionen.
- Wenn maximale Reichweite wichtiger ist als Dringlichkeit, wie bei App-Update-Ankündigungen oder Feature-Aktionen.

{% enddetails %}

## Firebase-Messaging-Zustellungspriorität {#fcm-priority}

Das Feld **Firebase Messaging Delivery Priority** ermöglicht es Ihnen zu steuern, ob eine Push-Benachrichtigung mit „normaler“ oder „hoher“ Priorität an Firebase Cloud Messaging gesendet wird. Diese Einstellung bestimmt, wie schnell Nachrichten zugestellt werden und wie sie sich auf die Akkulaufzeit des Geräts auswirken.

| Priorität | Beschreibung | Geeignet für |
|---------|-------------|----------|
| Normal | Akkuoptimierte Zustellung, die zur Schonung des Akkus verzögert werden kann | Nicht dringende Inhalte, Werbeangebote, Neuigkeiten |
| Hoch | Sofortige Zustellung mit höherem Akkuverbrauch | Zeitkritische Benachrichtigungen, wichtige Warnungen, Live-Event-Updates, Kontowarnungen, Eilmeldungen oder dringende Erinnerungen |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Firebase-Messaging-Zustellungspriorität" }

### Hinweise {#considerations}

- **Standardeinstellung**: Sie können eine Standard-FCM-Priorität für alle Android-Campaigns in Ihren [Push-Einstellungen]({{site.baseurl}}/user_guide/administer/global/workspace_settings/push_settings) festlegen. Diese Einstellung auf Campaign-Ebene überschreibt bei Bedarf den Standard.
- **Herabstufung**: Wenn FCM erkennt, dass Ihre App häufig Nachrichten mit hoher Priorität sendet, die nicht zu sichtbaren Benachrichtigungen oder Nutzer:innen-Engagement führen, können diese Nachrichten automatisch auf normale Priorität herabgestuft werden.
- **Akkuauswirkung**: Nachrichten mit hoher Priorität wecken schlafende Geräte aggressiver und verbrauchen mehr Akku. Verwenden Sie diese Priorität mit Bedacht.

Weitere detaillierte Informationen zur Nachrichtenverarbeitung und Herabstufung finden Sie in der [FCM-Dokumentation](https://firebase.google.com/docs/cloud-messaging/concept-options#setting-the-priority-of-a-message) und unter [Nachrichtenverarbeitung und Herabstufung auf Android](https://firebase.google.com/docs/cloud-messaging/android/message-priority#deprioritize).

## Zusammenfassungstext {#summary-text}

Der Zusammenfassungstext ermöglicht es Ihnen, zusätzlichen Text in der erweiterten Benachrichtigungsansicht festzulegen. Er dient auch als Bildunterschrift für Benachrichtigungen mit Bildern.

![Eine Android-Nachricht mit dem Titel „This is the title for the notification.“ und dem Zusammenfassungstext „This is the summary text for the notification.“]({% image_buster /assets/img/android/push/collapsed-android-notification.png %}){: style="max-width:65%;"}

Der Zusammenfassungstext wird unter dem Nachrichtentext in der erweiterten Ansicht angezeigt.

![Eine Android-Nachricht mit dem Titel „This is the title for the notification.“ und dem Zusammenfassungstext „This is the summary text for the notification.“]({% image_buster /assets/img/android/push/expanded-android-notification.png %}){: style="max-width:65%;"}

Bei Push-Benachrichtigungen mit Bildern wird der Nachrichtentext in der eingeklappten Ansicht angezeigt, während der Zusammenfassungstext als Bildunterschrift dargestellt wird, wenn die Benachrichtigung erweitert wird.

## Benutzerdefinierte URIs {#custom-uris}

Das Feature **Custom URI** ermöglicht es Ihnen, eine Web-URL oder eine Android-Ressource anzugeben, zu der navigiert wird, wenn die Benachrichtigung angeklickt wird. Wenn kein benutzerdefinierter URI angegeben ist, werden Nutzer:innen beim Klicken auf die Benachrichtigung in Ihre App geleitet. Sie können den benutzerdefinierten URI verwenden, um Deep-Links innerhalb Ihrer App zu erstellen sowie Nutzer:innen zu Ressourcen außerhalb Ihrer App weiterzuleiten. Dies kann über unsere [Messaging-API]({{site.baseurl}}/api/endpoints/messaging) oder im Tab **Compose** des Push-Composers angegeben werden.

![Feld für benutzerdefinierten URI.]({% image_buster /assets/img_archive/deep_link.png %}){: style="max-width:60%;"}

## Benachrichtigungs-Anzeigepriorität {#notification-display-priority}

{% multi_lang_include alerts/important_alerts.md alert='Android notification priority' %}

Die Prioritätsstufe einer Push-Benachrichtigung beeinflusst, wie Ihre Benachrichtigung im Benachrichtigungsbereich im Verhältnis zu anderen Benachrichtigungen angezeigt wird. Sie kann auch die Geschwindigkeit und Art der Zustellung beeinflussen, da Nachrichten mit normaler und niedrigerer Priorität mit etwas höherer Latenz gesendet oder gebündelt werden können, um die Akkulaufzeit zu schonen, während Nachrichten mit hoher Priorität immer sofort gesendet werden.

Dieses Feature ist nützlich, um Ihre Nachrichten danach zu unterscheiden, wie kritisch oder zeitkritisch sie sind. Beispielsweise wäre eine Benachrichtigung über gefährliche Straßenverhältnisse ein guter Kandidat für eine hohe Priorität, während eine Benachrichtigung über einen laufenden Sale eine niedrigere Priorität erhalten sollte. Sie sollten abwägen, ob eine störende Priorität für die Benachrichtigung, die Sie senden, tatsächlich notwendig ist, da das ständige Einnehmen der obersten Position im Posteingang Ihrer Nutzer:innen oder das Unterbrechen anderer Aktivitäten negative Auswirkungen haben kann.

In Android O wurde die Benachrichtigungspriorität zu einer Eigenschaft von Benachrichtigungskanälen. Sie müssen mit Ihren Entwickler:innen zusammenarbeiten, um die Priorität für einen Kanal während seiner Konfiguration festzulegen, und dann das Dashboard verwenden, um den richtigen Kanal beim Senden Ihrer Benachrichtigungstöne auszuwählen. Für Geräte mit Android-Versionen vor O ist es möglich, eine Prioritätsstufe für Android- und Fire OS-Benachrichtigungen über das Braze-Dashboard und die Messaging-API festzulegen.

Um Ihre gesamte Nutzerbasis mit einer bestimmten Priorität zu erreichen, empfehlen wir, die Priorität indirekt über die [Benachrichtigungskanal-Konfiguration](https://developer.android.com/training/notify-user/channels#importance) (für O+-Geräte) festzulegen und die individuelle Priorität über das Dashboard zu senden (für &#60;O-Geräte).

In der folgenden Tabelle finden Sie die Prioritätsstufen, die Sie für Android- oder Fire OS-Push-Benachrichtigungen festlegen können:

| Priorität | Beschreibung | `priority`-Wert (für API-Nachrichten) |
|------|-----------|----------------------------|
| Max | Dringende oder zeitkritische Nachrichten. | `2` |
| Hoch | Wichtige Kommunikation, wie eine neue Nachricht von einem Freund. | `1` |
| Standard | Die meisten Benachrichtigungen. Verwenden Sie diese, wenn Ihre Nachricht nicht explizit unter einen der anderen Prioritätstypen fällt. | `0` |
| Niedrig | Informationen, über die Nutzer:innen Bescheid wissen sollen, die aber kein sofortiges Handeln erfordern. | `-1`|
| Min | Kontextuelle oder Hintergrundinformationen. | `-2`|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Benachrichtigungs-Anzeigepriorität" }

Weitere Informationen finden Sie in der Google-Dokumentation zu [Android-Benachrichtigungen](http://developer.android.com/design/patterns/notifications.html).

## Push-Kategorie {#push-category}

Android-Push-Benachrichtigungen bieten die Möglichkeit anzugeben, ob Ihre Benachrichtigung in eine vordefinierte Kategorie fällt. Die Android-System-UI kann diese Kategorie verwenden, um Entscheidungen über die Einordnung oder Filterung zu treffen, wo die Benachrichtigung im Benachrichtigungsbereich der Nutzer:innen platziert wird.

![Tab „Settings“ mit der Kategorie „None“, was die Standardeinstellung ist.]({% image_buster /assets/img_archive/braze_category.png %}){: style="max-width:60%;"}

| Kategorie | Beschreibung |
|---|-------|
| None | Standardoption. |
| Alarm | Alarm oder Timer. |
| Call | Eingehender Anruf (Sprache oder Video) oder ähnliche synchrone Kommunikationsanfrage. |
| Email | Asynchrone Massennachricht (E-Mail). |
| Error | Fehler bei einem Hintergrundvorgang oder Authentifizierungsstatus. |
| Event | Kalenderereignis. |
| Message | Eingehende Direktnachricht (SMS, Sofortnachricht usw.). |
| Progress | Fortschritt eines lang laufenden Hintergrundvorgangs. |
| Promotion | Aktion oder Werbung. |
| Recommendation | Eine spezifische, zeitnahe Empfehlung für eine einzelne Sache. |
| Reminder | Von Nutzer:innen geplante Erinnerung. |
| Service | Anzeige eines laufenden Hintergrunddienstes. |
| Social | Update aus einem sozialen Netzwerk oder einer Sharing-Funktion. |
| Status | Laufende Informationen über den Geräte- oder Kontextstatus. |
| System | System- oder Gerätestatusupdate. Reserviert für Systemnutzung. |
| Transport | Medientransportsteuerung für die Wiedergabe. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Push-Kategorie" }

## Push-Sichtbarkeit {#push-visibility}

Android-Push-Benachrichtigungen bieten ein optionales Feld, um festzulegen, wie eine Benachrichtigung auf dem Sperrbildschirm der Nutzer:innen angezeigt wird. In der folgenden Tabelle finden Sie die Sichtbarkeitsoptionen und Beschreibungen.

| Sichtbarkeit | Beschreibung |
|---|-----|
| Public | Benachrichtigung wird auf dem Sperrbildschirm angezeigt |
| Private | Benachrichtigung wird mit „Inhalt ausgeblendet“ als Nachricht angezeigt |
| Secret | Benachrichtigung wird nicht auf dem Sperrbildschirm angezeigt |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Push-Sichtbarkeit" }

Darüber hinaus können Android-Nutzer:innen die Anzeige von Push-Benachrichtigungen auf ihrem Sperrbildschirm überschreiben, indem sie die Datenschutzeinstellung für Benachrichtigungen auf ihrem Gerät ändern. Diese Einstellung überschreibt die Sichtbarkeit der Push-Benachrichtigung.

![Position der Push-Priorität im Dashboard mit aktivierter und auf „Private“ gesetzter Sichtbarkeit.]({% image_buster /assets/img_archive/braze_visibility.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Unabhängig von der Sichtbarkeit werden alle Benachrichtigungen auf dem Sperrbildschirm der Nutzer:innen angezeigt, wenn die Datenschutzeinstellung für Benachrichtigungen auf ihrem Gerät auf **Alle Inhalte anzeigen** (Standardeinstellung) gesetzt ist. Ebenso werden Benachrichtigungen nicht auf dem Sperrbildschirm angezeigt, wenn die Datenschutzeinstellung auf **Benachrichtigungen nicht anzeigen** gesetzt ist. Die Sichtbarkeit hat nur dann eine Auswirkung, wenn die Datenschutzeinstellung auf **Sensible Inhalte ausblenden** gesetzt ist.

Die Sichtbarkeit hat keine Auswirkung auf Geräte vor Android Lollipop 5.0.0, d. h. alle Benachrichtigungen werden auf diesen Geräten angezeigt.

Weitere Informationen finden Sie in unserer [Android-Dokumentation](https://developer.android.com/guide/topics/ui/notifiers/notifications).

## Benachrichtigungstöne {#notification-sounds}

In Android O wurden Benachrichtigungstöne zu einer Eigenschaft von Benachrichtigungskanälen. Sie müssen mit Ihren Entwickler:innen zusammenarbeiten, um den Ton für einen Kanal während seiner Konfiguration festzulegen, und dann das Dashboard verwenden, um den richtigen Kanal beim Senden Ihrer Benachrichtigungen auszuwählen.

Für Geräte mit Android-Versionen vor Android O ermöglicht Braze Ihnen, den Ton einer einzelnen Push-Nachricht über den Dashboard-Composer festzulegen. Sie können dies tun, indem Sie eine lokale Soundressource auf dem Gerät angeben (zum Beispiel `android.resource://com.mycompany.myapp/raw/mysound`).

Wenn Sie in diesem Feld **Default** auswählen, wird der Standard-Benachrichtigungston des Geräts abgespielt. Dies kann über unsere [Messaging-API]({{site.baseurl}}/api/endpoints/messaging) oder in den **Settings** im Push-Composer angegeben werden.

![Das Feld „Sound“.]({% image_buster /assets/img_archive/sound_android.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Geben Sie als Nächstes den vollständigen Sound-Ressourcen-URI (zum Beispiel `android.resource://com.mycompany.myapp/raw/mysound`) in das Dashboard-Eingabefeld ein.

Um Ihre gesamte Nutzerbasis mit einem bestimmten Ton zu erreichen, empfehlen wir, den Ton indirekt über die [Benachrichtigungskanal-Konfiguration](https://developer.android.com/training/notify-user/channels) (für O+-Geräte) festzulegen und den individuellen Ton über das Dashboard zu senden (für &#60;O-Geräte).