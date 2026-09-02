---
nav_title: Link Aliasing
article_title: Link Aliasing
alias: /link_aliasing/
page_order: 3
description: "Dieser Artikel beschreibt, wie Link Aliasing funktioniert, und enthält Beispiele dafür, wie Ihre Links aussehen werden."
channel:
  - email

---

# [![Braze-Lernkurs]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/link-aliasing){: style="float:right;width:120px;border:0;" class="noimgborder"}Link Aliasing {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomlink-aliasing-stylefloatrightwidth120pxborder0-classnoimgborderlink-aliasing}

> Verwenden Sie Link Aliasing, um erkennbare, selbst erstellte Namen zur Identifizierung von Links zu erstellen, die in E-Mail-Nachrichten von Braze gesendet werden. Diese Links stehen für Segmentierungs-Retargeting, aktionsbasiertes Triggern und Link-Analytics zur Verfügung.

## Über Link Aliasing {#about-link-aliasing}

Mit Link Aliasing können Sie benutzerdefinierte Namen erstellen, um Links in E-Mails zu identifizieren und zu verfolgen. Auf diese Weise können Sie diese wiedererkennbaren Link-Aliase effizient in Ihren E-Mails verwenden, um das Engagement zu verfolgen und die Campaign-Performance zu analysieren, ohne auf den vollständigen Link verweisen zu müssen.

Mit Link Aliasing können Sie:

- **Nutzer:innen retargeten, die auf bestimmte Links geklickt haben:** Identifizieren und erreichen Sie Nutzer:innen, die auf einen Link geklickt haben.
- **Aktionsbasierte Trigger erstellen:** Senden Sie eine E-Mail, wenn ein:e Nutzer:in auf einen Link klickt.
- **Metriken analysieren:** Vergleichen Sie, wie viele Nutzer:innen auf Link A im Vergleich zu Link B geklickt haben.

### So funktioniert es {#how-it-works}

Braze identifiziert Links in E-Mails eindeutig, indem jeder Link-URL ein zusätzlicher Parameter namens `lid` (auch als Link-Bezeichner bekannt) hinzugefügt wird. Dieser `lid`-Wert ermöglicht es Braze, Nutzerinteraktionen mit dem Link zu verfolgen, zu überwachen und zu aggregieren, auch wenn sich die übrigen URL-Parameter unterscheiden können. Dies hilft dabei, Insights darüber zu gewinnen, wie Nutzer:innen mit den Inhalten in Ihren E-Mail-Campaigns interagieren.

Link-Bezeichner werden auch aktualisiert, wenn eine E-Mail-Campaign, ein Canvas mit einer E-Mail-Nachricht oder ein Content-Block dupliziert wird.

## Link Alias erstellen {#creating-a-link-alias}

{% alert important %}
**Link Management** wird im E-Mail-Composer der Campaign oder des Canvas angezeigt, wenn Braze das Link-Management für Ihr Konto aktiviert hat. Um **Link-Aliase** zu erstellen und zu bearbeiten, muss Link Aliasing aktiviert sein. Falls **Link Management** fehlt, wenden Sie sich an Ihre:n Account Manager:in:in, um Link Aliasing aktivieren zu lassen.
{% endalert %}

Um einen Link Alias zu erstellen, öffnen Sie Ihren E-Mail-Body im Campaign- oder Canvas-Komponenten-Composer und öffnen Sie dann **Link Management** im Bereich **Content**. Der Drag-and-drop- und der HTML-Composer verwenden dasselbe Seitenleisten-Layout:

### Drag-and-drop-Editor {#drag-and-drop-editor}

1. Wählen Sie **Edit Email Body** aus, um den Drag-and-drop-Composer zu öffnen.
2. Wählen Sie in der Composer-Seitenleiste **Content** aus (neben **Sending Settings** und **Preview & Test**). Weitere Informationen zu diesem Layout finden Sie unter [E-Mail per Drag-and-drop erstellen]({{site.baseurl}}/user_guide/channels/email/drag_and_drop).
3. Wählen Sie im Untermenü **Content** den Punkt **Link Management** aus (dieser befindet sich unter **Design and Build**). Falls das Untermenü eingeklappt ist, klappen Sie es über das Pfeilsymbol in der Seitenleiste aus.

### HTML-Editor {#html-editor}

1. Navigieren Sie zu Ihrem E-Mail-Body im Composer.
2. Wählen Sie in der Composer-Seitenleiste **Content** aus.
3. Wählen Sie im Untermenü **Content** den Punkt **Link Management** unter **Design and Build** aus.

In **Link Management**:

1. Braze generiert automatisch eindeutige Standard-Link-Aliase für jeden Ihrer Links.
2. Geben Sie dem Alias einen Namen. Aliase müssen pro E-Mail-Kampagnenvariante oder Canvas-Komponente eindeutig benannt sein.

Sie können auch einen Alias festlegen, der verwendet wird, um einen bestimmten Link im Rahmen von Reporting oder Segmentierung zu referenzieren.

![Link-Management-Seite mit vier Link-Aliasen.]({% image_buster /assets/img/link_aliasing_composer.png %})

{% alert note %}
Link Aliasing wird nur in `href`-Attributen innerhalb von HTML-Anchor-Tags unterstützt, bei denen es sicher ist, einen Query-Parameter anzuhängen. Als Best Practice sollten Sie ein Fragezeichen (?) am Ende Ihres Links einfügen, damit Braze den `lid`-Wert einfach anhängen kann. Ohne das Anhängen des `lid`-Werts erkennt Braze die URL nicht für Link Aliasing.
{% endalert %}

{% alert important %}
Im Drag-and-drop-Editor muss Ihr Link ein Fragezeichen (`?`) vor dem Hash-Symbol (`#`) in Ihrer URL enthalten, damit der Link Alias im Tab **Link Management** angezeigt wird.
{% endalert %}

## Link-Aliase verwalten {#managing-link-aliases}

Um alle Ihre getrackten Link-Aliase anzuzeigen, gehen Sie wie folgt vor:

1. Gehen Sie zu **Einstellungen** > **E-Mail-Einstellungen** unter **Workspace-Einstellungen**.
2. Wählen Sie den Tab **Link-Aliasing-Einstellungen** aus.

Hier können Sie Link-Aliase sortieren, durchsuchen und das Tracking dafür deaktivieren.

![Seite „Getrackte Link-Aliase“ mit aktiven und inaktiven Link-Aliasen, die verschiedenen Campaigns zugeordnet sind.]({% image_buster /assets/img/tracked_aliases.png %})

{% alert tip %}
Verwenden Sie die Endpunkte [Link-Alias für Campaign auflisten]({{site.baseurl}}/get_campaign_link_alias) und [Link-Alias für Canvas auflisten]({{site.baseurl}}/get_canvas_link_alias), um den in jeder Nachrichtenvariante einer Campaign oder einer E-Mail-spezifischen Canvas-Komponente festgelegten `alias` zu extrahieren.
{% endalert %}

Braze empfiehlt, die Links in der E-Mail zu prüfen, Link-Templates hinzuzufügen und eine Namenskonvention zu verwenden, die für die Segmentierung und Berichterstellung geeignet ist. So behalten Sie den Überblick über alle Links.

Wenn Link Aliasing aktiviert ist, werden Nachrichten, Content Blocks und Link-Templates nicht verändert. Alle bestehenden Nachrichten, die Link-Templates oder Content Blocks verwenden, bleiben unverändert. Wenn Sie jedoch eine Nachricht aktualisieren, wird das Link-Alias-Markup auf alle Links angewendet, sodass Sie die Link-Templates erneut anwenden müssen, damit die Links sichtbar sind.

## Wie Links mit Link Aliasing aktualisiert werden {#how-links-are-updated-with-link-aliasing}

Die folgenden Tabellen zeigen Beispiele für Links im E-Mail-Text, Ergebnisse des Link Aliasing und Erklärungen dazu, wie der ursprüngliche Link mit Link Aliasing aktualisiert wird.

### Permalink {#permalink}

**Logik:** Braze fügt ein Fragezeichen (?) ein und ergänzt den ersten Abfrageparameter in der URL.

| Link im E-Mail-Text    | Link mit Aliasing                     |
|-----------------------|----------------------------------------|
| `https://www.braze.com` | `https://www.braze.com?lid=slfdldtqdhdk` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Permalink" }

### Link mit weiteren Abfrageparametern {#link-with-more-query-parameters}

**Logik:** Braze erkennt weitere Abfrageparameter und hängt `lid=` an das Ende der URL an.

| Link im E-Mail-Text                                            | Link mit Aliasing                                                             |
|---------------------------------------------------------------|--------------------------------------------------------------------------------|
| `https://www.braze.com?utm_campaign=retention&utm_source=email` | `https://www.braze.com?utm_campaign=retention&utm_source=email&lid=0goty30mviyz` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Link mit weiteren Abfrageparametern" }

### HTML-Link {#html-link}

**Logik:** Braze erkennt, dass ein Link eine URL ist und bereits ein Fragezeichen (?) enthält, sodass der `lid`-Abfrageparameter nach dem Fragezeichen angehängt wird.

| Link im E-Mail-Text                                                | Link mit Aliasing                                                                |
|-------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| {%raw%}`<a href="{{custom_attribute.{product_url}}}?">`{%endraw%} | {%raw%}`<a href="{{custom_attribute.{product_url}}}?lid=ac7a548g5kl7">`{%endraw%} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="HTML-Link" }

### Link mit Anker {#link-with-anchor}

**Logik:** Braze erwartet, dass die URL eine Standardstruktur verwendet, bei der Anker (#) nach einem Fragezeichen (?) stehen. Da Braze von links nach rechts liest, werden das Fragezeichen und der `lid`-Wert vor dem Anker angehängt.

| Link im E-Mail-Text                               | Link mit Aliasing                                                |
|--------------------------------------------------|-------------------------------------------------------------------|
| `https://www.braze.com#bookmark1?utm_source=email` | `https://www.braze.com?lid=eqslgd5a9m3y#bookmark1?utm_source=email` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Link mit Anker" }

### Link mit Anker und Capture-Tag {#link-with-anchor-and-capture-tag}

**Logik:** Bei Verwendung von Link Aliasing mit URLs, die Anker (#) enthalten, erwartet Braze, dass der Anker nach den Abfrageparametern steht. Das bedeutet, dass der `lid`-Wert **vor** dem Anker angehängt werden muss, damit das Tracking korrekt funktioniert. Da Braze die URL von links nach rechts liest, sollten das Fragezeichen (?) und der `lid`-Wert vor dem Anker stehen.

| Link im E-Mail-Text                                                                        | Link mit Aliasing                                                                                           |
|-------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| {%raw%}`<a href="https://www.braze.com/promotions#special-offer">Check out our special offer!</a>`{%endraw%}  | {%raw%}`<a href="https://www.braze.com/promotions?lid={{link_alias}}#special-offer">Check out our special offer!</a>` {%endraw%} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Link mit Anker und Capture-Tag" }

## Link-Aliase tracken {#tracking-link-aliases}

Wählen Sie in der Seitenleiste des Composers **Inhalt** > **Link-Verwaltung** (unter **Design und Erstellung**) aus und wählen Sie dann die Aliase aus, die Sie **tracken** möchten. Getrackte Aliase stehen in Segmentierungsfiltern zur Verfügung, die auf Link-Aliase verweisen (siehe [Segmentierungsfilter](#segmentation-filters)). Sie können auch aktionsbasierte Nachrichten senden oder Nutzer:innen durch einen Canvas weiterleiten, wenn diese auf einen Link-Alias in einer E-Mail klicken – siehe [Aktionsbasierte Filter](#action-based-filters). Die Einstellung **Getrackt** ändert nicht, ob Klicks auf diesen Link in der E-Mail-Performance-Berichterstattung gezählt werden.

{% alert tip %}
Um Metriken zum Link-Engagement zu tracken, stellen Sie sicher, dass Ihr Link mit HTTP oder HTTPS beginnt. Um das Klick-Tracking für bestimmte Links zu deaktivieren, lesen Sie [Universal Links und App Links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links#turning-off-click-tracking-on-a-link-to-link-basis).
{% endalert %}

Braze ermöglicht es Ihnen, eine unbegrenzte Anzahl von Links zum Tracken auszuwählen. Sie können Nutzer:innen jedoch nur anhand der zuletzt angeklickten Links retargeten. Nutzerprofile enthalten die 100 zuletzt angeklickten Links. Wenn Sie beispielsweise 500 Links tracken und ein:e Nutzer:in alle 500 anklickt, können Sie auf Basis der 100 zuletzt angeklickten Links retargeten oder Segments erstellen.

![Der Tab „Link-Verwaltung“ mit zwei ausgewählten Links.]({% image_buster /assets/img/link_management_dnd.png %})

{% alert note %}
Braze trackt auf Profilebene nur die letzten 100 angeklickten Link-Aliase.
{% endalert %}

### Aktionsbasierte Filter {#action-based-filters}

Wenn Link Aliasing für Ihren Workspace aktiviert ist, können Sie aktionsbasierte Nachrichten erstellen, die auf einen beliebigen Link abzielen (getrackt oder nicht getrackt), oder Nutzer:innen basierend darauf retargeten, ob sie auf einen Alias in einer beliebigen E-Mail-Campaign oder Canvas-Komponente geklickt haben.

![Aktionsbasierte Optionen, um Nutzer:innen anzusprechen, die auf einen Alias in einer Canvas-Komponente geklickt oder mit einer Campaign interagiert haben.]({% image_buster /assets/img/link_aliasing_action_based_filters.png %})

- Wenn eine Campaign archiviert wird, wird das Link-Tracking deaktiviert und dieser Link-Alias kann nicht in einem anderen Filter verwendet werden.
- Wenn ein Link mit aktiviertem Tracking angeklickt wurde, finden Sie die Campaign als verfügbare Option im Segmentfilter, selbst wenn das Link-Tracking inzwischen deaktiviert wurde – vorausgesetzt, mindestens ein Link in dieser Nachricht wird noch getrackt.
- Sie können einen getrackten Link nur als Filter auswählen, wenn er sich in einem aktiven (gestarteten) Canvas befindet, über das Dropdown **Clicked Alias in Canvas-Schritt**. Wenn der Link in einem Canvas-Entwurf getrackt wird, können Sie den getrackten Link nicht als Filter auswählen.

Um Links als nicht getrackt festzulegen, gehen Sie zu **Einstellungen** > **E-Mail-Einstellungen** > **Link-Aliasing-Einstellungen**.

### Segmentierungsfilter {#segmentation-filters}

Wenn Sie in Braze einen Link-Alias in Ihrer E-Mail haben und ein:e Nutzer:in darauf klickt, wird das Ereignis im Kundenprofil mit dem Alias erfasst.

Wenn Sie den Segmentierungsfilter „Clicked Alias in Any Campaign or Canvas-Schritt“ verwenden und später den Link-Alias umbenennen, werden die bisherigen Klickdaten im Kundenprofil **nicht** aktualisiert – sie zeigen weiterhin den vorherigen Link-Alias an. Wenn Sie also Nutzer:innen auf Basis des neuen Link-Alias ansprechen, enthält dies nicht die Daten des vorherigen Link-Alias.

Wenn Sie den Segmentierungsfilter „Clicked Alias in Campaign“ oder „Clicked Alias in Canvas“ verwenden, werden Ihre Nutzer:innen danach gefiltert, ob sie auf einen bestimmten Alias in einer bestimmten Campaign oder einem bestimmten Canvas geklickt haben. Wenn mehrere Nutzer:innen dieselbe E-Mail-Adresse teilen und der Link-Alias angeklickt wird, werden die Nutzerprofile aller anderen Nutzer:innen, die die E-Mail-Adresse teilen, aktualisiert. Diese Profile werden auch durch Zustellungs- und Öffnungsereignisse aktualisiert, nicht nur durch Klickereignisse.

Die folgenden Segmentierungsfilter gelten für Klickereignisse, die zum Zeitpunkt der Verarbeitung des Ereignisses getrackt werden. Das bedeutet, dass nicht getrackte Links keine vorhandenen Daten entfernen und das Tracken eines Links die Daten nicht rückwirkend auffüllt. Weitere Details finden Sie unter [Segmentierungsfilter]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters).

#### Tracking von Links aufheben {#untracking-links}

Das Aufheben des Trackings eines Links weist vorhandene Segments mit dem Filter nicht dem nicht getrackten Alias neu zu. Die alten Daten verbleiben in den Nutzerprofilen, bis sie durch neuere Daten ersetzt werden.

Links in archivierten Nachrichten werden automatisch nicht mehr getrackt. Wenn archivierte Nachrichten jedoch wiederhergestellt werden, müssen die Links erneut getrackt werden. Wenn Link-Aliase getrackt werden, wird die Link-Berichterstattung nach dem Alias anstelle von Top-Level-Domains oder vollständigen URLs indexiert.

Um alle Links in Ihrer E-Mail-Campaign und die jeweilige Gesamtzahl der Klicks anzuzeigen, gehen Sie zu **Nachrichtenanalyse** > **E-Mail-Performance** > **Vorschau & Heatmap** und schalten Sie den Schalter **Heatmap anzeigen** um.

![Panel „Link-Tabelle nach Gesamtklicks“ mit Link-Aliasen und deren Gesamtklicks.]({% image_buster /assets/img/link_alias_total_clicks.png %}){: style="max-width:60%;"}

### E-Mail-Klick-Ereignis {#email-clicks-event}

Wenn Sie Ihre Engagement-Daten mit Currents exportieren, unterscheidet sich ein E-Mail-Klick-Ereignis geringfügig, wenn Link Aliasing aktiviert ist. Es enthält zwei zusätzliche Felder für das [E-Mail-Klick-Ereignis]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#email-click-events), wenn Link Aliasing aktiviert ist: `link_id` und `link_alias`.

```json
// Email Click: users.messages.email.Click
{
  "id": (string) unique ID of this event,
  "user_id": (string) Braze user ID of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "campaign_id": (string) ID of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) ID of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) ID of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) ID of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) ID of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) ID of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "dispatch_id": (string) ID of the message dispatch (unique ID for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "email_address": (string) email address for this event,
  "url": (string) the URL that was clicked (Email Click events only),
  "user_agent": (string) description of the user's system and browser for the event (Email Click and Open events only),
  "ip_pool": (string) IP pool used for message sending,
  "link_id": (string) unique value generated by Braze for the URL,
  "link_alias": (string) alias name set when the message was sent
}
```

{% alert update %}
Das Verhalten von `dispatch_id` unterscheidet sich zwischen Canvas und Campaigns, da Braze Canvas-Schritte (mit Ausnahme von Entry-Schritten, die geplant werden können) als getriggerte Ereignisse behandelt, auch wenn sie „geplant“ sind. Erfahren Sie mehr über das [`dispatch_id`-Verhalten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/dispatch_id) in Canvas und Campaigns.

_Aktualisierung vermerkt im August 2019._
{% endalert %}

## Link Aliasing in Content Blocks {#link-aliasing-in-content-blocks}

Bei neuen Content Blocks werden die Links so geändert, dass Braze jedem Link, wo zutreffend, ein `lid={{placeholder}}` anfügt. Dieser Platzhalterwert wird aufgelöst, wenn er in eine E-Mail-Nachrichtenvariante eingefügt wird.

Um die Links in bestehenden Content Blocks zu ändern, die erstellt wurden, bevor Braze Link Aliasing aktiviert hat, duplizieren Sie die bestehenden Content Blocks und ändern Sie dann die Links in den duplizierten Content Blocks.

Wenn ein Content-Block ohne `lid`-Wert in eine neue Nachricht eingefügt wird, werden die Links aus diesem Content-Block nicht mit einem Alias verfolgt. Wenn ein neuer Content-Block in eine „alte“ Nachrichtenvariante eingefügt wird, werden die Links aus dieser Nachrichtenvariante durch Link Aliasing erkannt. Links aus dem Content-Block werden ebenfalls erkannt. Allerdings können „alte“ Content Blocks keine „neuen“ Content Blocks verschachteln.

{% alert tip %}
Für Content Blocks empfiehlt Braze, Kopien bestehender Content Blocks zu erstellen, um sie in neuen Nachrichten zu verwenden. Dies kann durch Massenduplizierung erfolgen, um Szenarien zu vermeiden, in denen Sie auf einen Content-Block verweisen, für den Link Aliasing in einer neuen Nachricht nicht aktiviert wurde.
{% endalert %}

## Link Aliasing für URLs, die durch Liquid generiert werden {#link-aliasing-for-urls-generated-by-liquid}

Für URLs, die durch Liquid generiert werden (zum Beispiel `assign` im HTML, Werte aus einem Content Block oder Liquid in einem angepassten Attribut), benötigt Braze eine eindeutige Stelle, um den Query-Parameter `lid` einzufügen. In den meisten Fällen, wenn Liquid in der URL verbleibt, leitet Braze nicht ab, ob ein neuer Query-String mit `?` begonnen oder ein bestehender Query mit `&` verbunden werden soll – es sei denn, Sie fügen dieses Trennzeichen selbst hinzu.

Gehen Sie wie folgt vor:

- Wenn die URL **noch keinen** Query-String enthält, hängen Sie `?` nach dem Liquid an (zum Beispiel `{{my_url}}?`).
- Wenn die URL **bereits** `?` und Query-Parameter enthält, hängen Sie `&` nach dem Liquid an (zum Beispiel `{{my_url}}&`).

{% alert note %}
Wenn Sie [Link-Templates]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_template) mit durch Liquid generierten URLs verwenden, kann Braze die gerenderte URL nach der Liquid-Ausführung konservativ normalisieren, wenn sie genau zwei `?`-Zeichen als Query-Trennzeichen enthält. Das zweite `?` kann in `&` umgeschrieben werden, damit Braze so wenig wie möglich an der URL ändert. <br><br>Braze versucht nicht, jedes doppelte `?`-Muster zu korrigieren, und die Behandlung komplexerer URLs bleibt bewusst eingeschränkt. Fügen Sie zuerst das korrekte `?` oder `&` in Ihrem Markup hinzu und betrachten Sie jede Normalisierung als begrenzten Schutzmechanismus – nicht als Ersatz für korrekt formatierte URLs oder dafür, dass Links in **Link Management** erkannt werden, wenn kein Trennzeichen vorhanden ist.
{% endalert %}

Ohne ein abschließendes `?` oder `&` (oder einen anderen unterstützten Einfügepunkt) erkennt Link Aliasing die URL nicht, **Link Management** listet sie nicht auf und Link-Templates werden nicht angewendet.

### URL-Fragmente (`#`) und Tracking-Parameter {#url-fragments-and-tracking-parameters}

Das Fragment (`#` und alles danach) wird bei einer normalen Link-Anfrage nicht an den Server gesendet. Braze fügt `lid` in den Query-String ein, der vor dem `#` erscheinen muss. Wenn Ihr `href` Liquid und ein `#`-Fragment enthält, aber kein `?` oder `&` vor dem `#`, kann Braze `lid` nicht sicher anhängen, sodass der Link möglicherweise nicht in **Link Management** erscheint oder als Link-Alias getrackt wird.

Dies kommt besonders häufig im Drag-and-Drop-Editor vor, wenn eine Button-URL Liquid mit einem hash-basierten Muster kombiniert (zum Beispiel ein statischer Pfad, dann `#`, dann zusätzliche Schlüssel-Wert-Paare). Fügen Sie in diesem Fall `?` unmittelbar vor dem `#` hinzu, damit der Query-String (einschließlich `lid`) vor dem Fragment geparst wird.

{% raw %}
```text
https://example.com/campaign/to/abc123?#user_id={{${user_id}}}&source=email
```
{% endraw %}

Im vorherigen Beispiel gibt das `?` vor `#` Braze ein Query-Segment, an das `lid` angehängt werden kann. Ohne dieses erscheint der Link möglicherweise nicht in **Link Management**.

Ohne die Möglichkeit zu erkennen, wo Query-Parameter angehängt werden sollen, erkennt Link Aliasing diese URLs nicht und Link-Templates werden nicht angewendet. Wenn Sie Fehler wie **Failed to be assigned an LID** für eine dynamische URL sehen, überprüfen Sie, ob das `href` das in den Beispielen in diesem Abschnitt gezeigte `?`- oder `&`-Muster verwendet.

### Hinweise zum Drag-and-Drop-Editor {#drag-and-drop-editor-considerations}

Im Drag-and-Drop-Editor validieren Felder, die einen Link enthalten (z. B. eine Button-**URL**), das zugrunde liegende `href`, bevor Liquid ausgeführt wird. Leerzeichen, Zeilenumbrüche und andere Zeichen, die nicht URL-sicher sind, können unerwartetes Verhalten verursachen, wenn Braze Link-Templates oder Link-Aliasing-Parameter anhängt. Wenn Sie verzweigendes Liquid für das Ziel benötigen, legen Sie die URL in einem HTML-Block mit `assign` fest (siehe den folgenden Abschnitt) und referenzieren Sie eine einzelne Variable im Drag-and-Drop-URL-Feld, anstatt komplexes Liquid direkt in dieses Feld zu setzen.

### Content-Block-Beispiel {#content-block-example}

{% raw %}
Wenn ein Content Block einen Link wie `https://www.braze.com/{{custom_attribute.${offer_id}}}` ohne abschließendes `?` oder `&` enthält, weiß Braze nicht, wo `lid` angehängt werden soll, sodass der Link nicht für **Link Management** erfasst wird. Fügen Sie `?` oder `&` am Ende der URL im Content Block hinzu (je nachdem, ob bereits ein Query-String vorhanden ist), speichern Sie den Content Block, und der Link kann erkannt werden.
{% endraw %}

### Reporting, wenn die URL pro Nutzer:in variiert {#reporting-when-the-url-varies-per-user}

Jedes eindeutige `href` in der Nachricht wird **einer** Link-ID und einem Link-Alias für **Link Management** und alias-basiertes Reporting zugeordnet. Wenn Link-Aliase getrackt werden, wird das E-Mail-Reporting im Dashboard nach dem Alias indiziert und nicht nach jeder möglichen aufgelösten URL.

Verwenden Sie zunächst die folgenden Ansätze in Braze:

- **Campaign- und Canvas-E-Mail-Analytics:** Überprüfen Sie aggregierte Klicks nach Link unter **Message Analytics** > **Email Performance** > **Preview & Heatmap** mit aktiviertem **Show Heatmap**, wie unter [Links vom Tracking ausschließen](#untracking-links) beschrieben.
- **Klicks pro Empfänger:in im Query Builder:** Führen Sie das **Email URLs clicked**-[Query-Builder-Template]({{site.baseurl}}/user_guide/analytics/reports/query_builder/query_templates#email-templates) für eine Campaign oder ein Canvas aus. Das Template zeigt depersonalisierte Links für zusammenfassende Zählungen an; der CSV-Export enthält die Nutzer-IDs der Klickenden, den angeklickten Link und einen Zeitstempel. (Depersonalisierte URLs entfernen Liquid-Tags für die Zusammenfassungsansicht; weitere Details finden Sie in der Template-Beschreibung.)
- **Aufschlüsselungen auf Alias-Ebene im Composer:** Wenn jedes Ziel (zum Beispiel jede `offer_id`) als eigene Zeile in **Link Management** und im alias-basierten Reporting erscheinen soll, verwenden Sie separate `href`-Werte (und damit separate Aliase) – zum Beispiel unterschiedliche Links pro Branch – anstatt eines Links, dessen Pfad sich pro Nutzer:in ändert.

Wenn Sie auch Streaming-Engagement-Exporte verwenden, enthalten E-Mail-Klick-Ereignisse ein **`url`**-Feld; unter [E-Mail-Klick-Ereignis](#email-clicks-event) auf dieser Seite erfahren Sie, wie diese Payload mit Link Aliasing zusammenhängt.

### Beispiel {#example}

Verwenden Sie dieses Muster, wenn die zugewiesene URL keine Query-Parameter enthält:

{% raw %}
```liquid
{% assign link1 = "https://www.braze1.com" %}

<a href="{{link1}}?">Visit Braze</a>
```
{% endraw %}

Wenn die zugewiesene URL bereits `?` und Query-Parameter enthält, hängen Sie `&` nach dem Liquid anstelle von `?` an:

{% raw %}
```liquid
{% assign link_with_params = "https://www.braze1.com?campaign=test" %}

<a href="{{link_with_params}}&">Visit Braze</a>
```
{% endraw %}

### URLs mit bedingtem Liquid {#urls-with-conditional-liquid}

Wenn bedingte Liquid-Tags innerhalb eines `href` verwendet werden (zum Beispiel um eine URL mit {% raw %}`{% if %}`, `{% elsif %}` oder `{% unless %}`{% endraw %} zu setzen), wird Link Aliasing auf diese Links nicht angewendet. Das bedeutet, diese Links erscheinen nicht in **Link Management** und erhalten kein `lid` für Klick-Tracking.

**Empfohlen:** Erstellen Sie die endgültige URL in einem HTML-Block mit `assign` (oder {% raw %}`{% capture %}`{% endraw %}) und referenzieren Sie diese Variable überall dort, wo Sie den Link benötigen. Fügen Sie im Drag-and-Drop-Editor die Variable in das Button-**URL**-Feld mit einem abschließenden `?` oder `&` ein, je nach Bedarf – zum Beispiel `{{url}}?`.

{% raw %}
```liquid
{% if {{custom_attribute.${account_tier}}} == "pro" %}
{% assign url = "https://example.com/pro/verify" %}
{% else %}
{% assign url = "https://example.com/retail/account" %}
{% endif %}
```
{% endraw %}

Verweisen Sie im Button-**URL**-Feld (Drag-and-Drop) oder im HTML mit dem `href` auf die Variable mit einem Trennzeichen:

{% raw %}
```liquid
<a href="{{ url }}?">Go to account</a>
```
{% endraw %}

Alternativ können Sie die URL in einer Variablen erfassen:

{% raw %}
```liquid
{% capture url %}
  {%- if condition -%}
    https://example.com/url1
  {%- else -%}
    https://example.com/url2
  {%- endif -%}
{% endcapture %}

<a href="{{ url }}?">Go to account</a>
```
{% endraw %}

## Fehlerbehebung {#troubleshooting}

### Ziele, die den `lid`-Parameter nicht akzeptieren {#destinations-that-dont-accept-the-lid-parameter}

Wenn Sie eine Testnachricht aus dem E-Mail-Editor senden, hängt Braze {% raw %}`lid={{placeholder}}`{% endraw %} an Ihre Links an (der Platzhalter wird zum Sendezeitpunkt durch einen eindeutigen Wert ersetzt). Falls die Zielwebsite oder API keine zusätzlichen Query-Parameter toleriert, kann der Link im Editor funktionieren, aber beim Öffnen aus der E-Mail fehlschlagen.

Ohne den `lid`-Wert behandelt Braze die URL nicht als link-aliased für Tracking und Segmentierung. Wir empfehlen, Ihr Backend oder Ihre Website so zu aktualisieren, dass der `lid`-Query-Parameter ignoriert wird, wenn er vorhanden ist. Dadurch bleiben Link Aliasing, Reporting und die in diesem Artikel beschriebenen Segment-Anwendungsfälle erhalten.

Alternativ können Sie Link Aliasing im Dashboard deaktivieren, während Sie eine Backend-Änderung planen. Gehen Sie zu **Einstellungen** > **E-Mail-Einstellungen** > **Link-Aliasing-Einstellungen**.

Falls Sie Ihre Zielsysteme nicht ändern können, wenden Sie sich an den [Braze-Support]({{site.baseurl}}/user_guide/administer/personal/braze_support), um Link Aliasing für Ihren Workspace zu deaktivieren. Beachten Sie die folgenden Hinweise, wenn Link Aliasing für Ihren Workspace deaktiviert wird:

- Neue E-Mail-Nachrichten und Content Blocks erhalten in der Regel keine neuen Link-Alias-Markierungen mehr (wie den `lid`-Query-Parameter).
- Bestehende Nachrichten, die erstellt wurden, als Link Aliasing aktiviert war, können weiterhin Link-Alias-Markierungen im HTML enthalten. Möglicherweise müssen Sie verbleibende `lid`-Parameter manuell entfernen, wo Sie sie nicht mehr benötigen.
- Wenn Sie eine bestehende Campaign, einen Canvas-E-Mail-Schritt oder einen Content Block bearbeiten, müssen Sie möglicherweise Link-Templates erneut hinzufügen, damit vorlagenbasierte Links korrekt angezeigt werden.
- Das Klick-Reporting für Sendungen, die durchgeführt wurden, als Link Aliasing aktiviert war, stimmt möglicherweise nicht sauber mit dem Reporting nach Deaktivierung des Features überein.
- Segments, die link-alias-basierte Filter verwenden (zum Beispiel **Clicked Alias**-Filter), liefern möglicherweise nicht mehr die erwarteten Zielgruppen.