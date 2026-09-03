---
nav_title: Content-Card erstellen
article_title: Content-Card erstellen
page_order: 1
description: "Dieser Referenzartikel beschreibt, wie Sie Content Cards mit Braze-Kampagnen und Canvases erstellen, verfassen, konfigurieren und versenden."
tool:
  - Canvas
  - Campaigns
channel:
  - content cards
search_rank: 3.9

---

# Content-Card erstellen {#create-a-content-card}

> Dieser Artikel beschreibt, wie Sie eine Content-Card in Braze erstellen, wenn Sie Kampagnen und Canvases aufbauen. Hier führen wir Sie durch die Auswahl eines Nachrichtentyps, das Verfassen Ihrer Karte und die Planung Ihrer Nachrichtenzustellung.

## Schritt 1: Wählen Sie, wo Sie Ihre Nachricht erstellen möchten {#step-1-choose-where-to-build-your-message}

Verwenden Sie Campaigns für einfache, einzelne Nachrichten (z. B. um Nutzer:innen mit einer einzigen Nachricht über ein Produkt zu informieren). Verwenden Sie Canvases für mehrstufige Nutzer:innen-Journeys (z. B. um maßgeschneiderte Produktvorschläge basierend auf dem Nutzer:innenverhalten im Laufe der Zeit zu senden).

{% tabs %}
{% tab Campaign %}

1. Gehen Sie zu **Messaging** > **Campaigns** und wählen Sie **Create Campaign** aus.
2. Wählen Sie **Content Cards** oder, für Campaigns, die auf mehrere Kanäle abzielen, **Multichannel** aus.
3. Geben Sie Ihrer Campaign einen klaren und aussagekräftigen Namen.
4. Fügen Sie bei Bedarf [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams) und [Tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) hinzu.
   * Tags erleichtern das Auffinden und Auswerten Ihrer Campaigns. Wenn Sie zum Beispiel den [Berichts-Builder]({{site.baseurl}}/user_guide/analytics/reports/report_builder) verwenden, können Sie nach den relevanten Tags filtern.
5. Fügen Sie so viele Varianten hinzu, wie Sie möchten, und benennen Sie diese. Sie können für jede hinzugefügte Variante unterschiedliche Plattformen, Nachrichtentypen und Layouts wählen. Weitere Informationen zu Varianten finden Sie unter [Multivariate und A/B-Tests]({{site.baseurl}}/user_guide/messaging/ab_testing).

{% alert tip %}
Wenn alle Nachrichten in Ihrer Campaign ähnlich sind oder denselben Inhalt haben, verfassen Sie Ihre Nachricht, bevor Sie weitere Varianten hinzufügen. Wählen Sie dann **Copy from Variant** aus dem **Add Variant**-Dropdown aus.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. [Erstellen Sie Ihren Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) mit dem Canvas-Composer.
2. Nachdem Sie Ihren Canvas eingerichtet haben, fügen Sie einen Nachrichtenschritt im Canvas-Builder hinzu. Geben Sie Ihrem Schritt einen klaren und aussagekräftigen Namen.
3. Wählen Sie **Content Cards** als Ihren Messaging-Kanal.
4. Legen Sie fest, wann Braze die Zielgruppeneignung und Personalisierung für die Content Card berechnet. Dies kann beim Schritt-Eintritt oder bei der ersten Impression (empfohlen) erfolgen. Schritte mit Content Cards können geplant oder aktionsbasiert sein.
5. Legen Sie fest, ob Content Cards entfernt werden sollen, wenn Nutzer:innen einen Kauf abschließen oder ein angepasstes Event ausführen.
6. Legen Sie ein Ablaufdatum für die Content Card fest (Verweildauer im Feed). Dies kann nach einer bestimmten Zeitspanne oder zu einem bestimmten Zeitpunkt sein.
7. Filtern Sie bei Bedarf Ihre Zielgruppe bzw. die Empfänger:innen für diesen Schritt in den **Zustellungseinstellungen**. Sie können Ihre Zielgruppe weiter verfeinern, indem Sie Segments angeben und zusätzliche Filter hinzufügen. Die Zielgruppenoptionen werden nach der Verzögerung zum Zeitpunkt des Nachrichtenversands geprüft.
8. Wählen Sie weitere Messaging-Kanäle, die Sie mit Ihrer Nachricht kombinieren möchten.

{% endtab %}
{% endtabs %}

## Schritt 2: Nachrichtentypen festlegen {#step-2-specify-your-message-types}

Wählen Sie einen der drei grundlegenden Content-Card-Typen aus: **Klassisch**, **Hervorgehobenes Bild** und **Nur Bild**.

Weitere Informationen zum erwarteten Verhalten und Aussehen der einzelnen Typen finden Sie unter [Kreative Details]({{site.baseurl}}/user_guide/channels/content_cards/creative_details) oder in den Links in der folgenden Tabelle. Diese Content-Card-Typen werden sowohl von mobilen Apps als auch von Webanwendungen unterstützt.

| Nachrichtentyp | Beispiel | Beschreibung |
|---|---|---|
| [Klassisch]({{site.baseurl}}/user_guide/channels/content_cards/creative_details#content-card-types) | ![Eine klassische Content Card mit einem kleinen Symbol und Text, der dazu einlädt, einen Trainingskurs zu buchen.]({% image_buster/assets/img_archive/cc_steppington_classic.png %}) | Die klassische Karte hat ein einfaches Layout mit einem fettgedruckten Titel, Nachrichtentext und einem optionalen Bild, das links neben dem Titel und Text platziert wird. Am besten verwenden Sie ein quadratisches Bild oder Symbol für die klassische Karte. |
| [Hervorgehobenes Bild]({{site.baseurl}}/user_guide/channels/content_cards/creative_details#content-card-types) | ![Eine hervorgehobene Content Card mit dem Bild eines Gewichthebers und Text, der dazu einlädt, einen Trainingskurs zu buchen.]({% image_buster/assets/img_archive/cc_steppington_captioned.png %}) | Die hervorgehobene Content-Card präsentiert Ihren Content mit Text und einem aufmerksamkeitsstarken Bild. |
| [Nur Bild]({{site.baseurl}}/user_guide/channels/content_cards/creative_details#content-card-types) | ![Eine Content Card vom Typ „Nur Bild“ mit ausschließlich Text.]({% image_buster/assets/img_archive/cc_steppington_banner.png %}) | Die Karte „Nur Bild“ erregt Aufmerksamkeit und bietet Platz für Bilder, GIFs und andere kreative nicht-textbasierte Inhalte. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Schritt 2: Nachrichtentypen festlegen" }

## Schritt 3: Eine Content Card verfassen {#step-3-compose-a-content-card}

Sie können alle Aspekte des Inhalts und Verhaltens Ihrer Nachricht im Tab **Verfassen** des Nachrichteneditors bearbeiten.

![Beispielhafte Content-Card-Details im Tab „Verfassen“ des Nachrichteneditors.]({% image_buster /assets/img/content_card_compose.png %})

Der Inhalt hier variiert je nach dem im vorherigen Schritt gewählten **Kartentyp**, kann aber eine der folgenden Optionen umfassen:

### Sprache {#language}

Wählen Sie **Sprachen hinzufügen**, um Ihre gewünschten Sprachen aus der bereitgestellten Liste hinzuzufügen. Dadurch wird [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic#conditional-logic) in Ihre Nachricht eingefügt. Wir empfehlen, Ihre Sprachen auszuwählen, bevor Sie Ihren Inhalt schreiben, damit Sie Ihren Text an der richtigen Stelle im Liquid einfügen können. Eine vollständige Liste der verfügbaren Sprachen finden Sie unter [Unterstützte Sprachen]({{site.baseurl}}/developer_guide/localization?tab=android).

![Ein Fenster mit Englisch, Spanisch und Französisch als ausgewählte Sprachen sowie Titel, Beschreibung und Linktext als Felder zur Internationalisierung.]({% image_buster /assets/img/add_languages.png %}){: style="max-width:70%;"}

#### Nachrichten von rechts nach links erstellen {#create-right-to-left-messages}

Das endgültige Erscheinungsbild von Rechts-nach-links-Nachrichten hängt weitgehend davon ab, wie Dienstanbieter sie rendern. Best Practices zum Erstellen von Rechts-nach-links-Nachrichten, die so genau wie möglich dargestellt werden, finden Sie unter [Rechts-nach-links-Nachrichten erstellen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages).

#### Titel und Nachricht {#title-and-message}

Schreiben Sie, was Sie möchten. Es gibt keine Einschränkungen, aber je schneller Sie Ihre Botschaft vermitteln und Ihre Kund:innen zum Klicken bringen, desto besser! Wir empfehlen klare und prägnante Titel und Nachrichteninhalte. Beachten Sie, dass diese Felder für reine Bildkarten nicht zur Verfügung stehen.

#### Bild {#image}

Um ein Bild zu Ihrer Content Card hinzuzufügen, können Sie **Bild hinzufügen** auswählen oder eine Bild-URL angeben. Durch Auswahl von **Bild hinzufügen** wird die **Medienbibliothek** geöffnet, in der Sie ein zuvor hochgeladenes Bild auswählen oder ein neues hinzufügen können.

Jeder Nachrichtentyp und jede Plattform kann eigene empfohlene Proportionen und Anforderungen haben. Prüfen Sie diese daher unbedingt, bevor Sie ein Bild in Auftrag geben oder von Grund auf erstellen. Beachten Sie, dass Content-Card-Nachrichtenfelder insgesamt auf eine Größe von 2&nbsp;KB begrenzt sind.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

#### An den Anfang pinnen {#pin-to-top}

Braze zeigt eine gepinnte Karte am Anfang des Feeds einer Nutzer:in an, und die Nutzer:in kann sie nicht schließen. Wenn der Feed einer Nutzer:in mehrere gepinnte Karten enthält, ordnet Braze diese chronologisch an. Wenn Braze eine Content Card zustellt, ist sie entweder gepinnt oder nicht gepinnt, und dieser Status ändert sich für die gesamte Lebensdauer der Karte nicht. Wenn Sie die Pin-Einstellung einer Campaign ändern, gilt die Aktualisierung nur für Karten, die nach der Änderung gesendet werden. Der Pin-Status bereits im Feed einer Nutzer:in befindlicher Karten wird nicht geändert.

![Nebeneinanderdarstellung der Content-Card-Vorschau in Braze für Mobilgeräte und Web mit der ausgewählten Option „Diese Karte oben im Feed anpinnen“.]({% image_buster /assets/img/cc_pin_to_top.png %}){:style="border:none"}

#### Klickverhalten {#on-click-behavior}

Wenn Ihre Kund:innen auf einen angezeigten Link in der Karte klicken, kann der Link sie entweder tiefer in Ihre App oder zu einer anderen Website führen. Wenn Sie ein Klickverhalten für Ihre Content Card festlegen, denken Sie daran, Ihren **Linktext** entsprechend zu aktualisieren.

Die folgenden Aktionen sind für Content-Card-Links verfügbar:

| Aktion | Beschreibung |
|---|---|
| Weiterleitung zu Web-URL | Öffnet eine nicht-native Webseite. |
| [Deeplink in die App]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls#deep-link-to-in-app-content) | Erstellt einen Deeplink zu einem vorhandenen Bildschirm in Ihrer App. |
| Angepasstes Event protokollieren | Wählen Sie ein [angepasstes Event]({{site.baseurl}}/user_guide/data/activation/events/custom_events), das ausgelöst werden soll. Kann verwendet werden, um eine weitere Content Card anzuzeigen oder zusätzliches Messaging auszulösen. |
| Angepasstes Attribut protokollieren | Wählen Sie ein [angepasstes Attribut]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes), das für die aktuelle Nutzer:in gesetzt werden soll. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Klickverhalten" }

Die Optionen **Angepasstes Event protokollieren** und **Angepasstes Attribut protokollieren** erfordern die folgende SDK-Versionskompatibilität:

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

## Schritt 4: Zusätzliche Einstellungen konfigurieren (optional) {#step-4-configure-additional-settings-optional}

Sie können [Schlüssel-Wert-Paare]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs) verwenden, um Kategorien für Ihre Karten zu erstellen, [mehrere Content-Card-Feeds]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed#implementing-multiple-feeds) einzurichten und die Sortierung der Karten anzupassen.

Um Schlüssel-Wert-Paare zu Ihrer Nachricht hinzuzufügen, gehen Sie zum Tab **Einstellungen** und wählen Sie **Neues Paar hinzufügen** aus.

## Schritt 5: Erstellen Sie den Rest Ihrer Campaign oder Ihres Canvas {#step-5-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

Erstellen Sie den Rest Ihrer Campaign. In den folgenden Abschnitten erfahren Sie, wie Sie unsere Tools optimal für die Erstellung von Content Cards nutzen können.

### Wählen Sie einen Zustellungszeitplan oder Trigger {#choose-a-delivery-schedule-or-trigger}

Content Cards können basierend auf einem geplanten Zeitpunkt, einer Aktion oder einem API-Trigger zugestellt werden. Weitere Informationen finden Sie unter [Ihre Campaign planen]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign).

Sie können auch die Dauer der Campaign und die [Ruhezeiten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours) festlegen sowie das Ablaufdatum der Content Card bestimmen. Legen Sie ein bestimmtes Ablaufdatum oder die Anzahl der Tage bis zum Ablauf einer Karte fest – maximal 30 Tage. Alle Varianten müssen dasselbe Ablaufdatum verwenden (Dauer oder bestimmter Zeitpunkt).

Der Ablauf-Countdown beginnt ab dem Sendezeitpunkt der Karte:

- **Geplante Campaigns:** Der Countdown beginnt zum geplanten Startzeitpunkt.
- **Aktionsbasierte Campaigns:** Der Countdown beginnt, wenn die Nutzer:in die auslösende Aktion ausführt.

Wenn beispielsweise eine aktionsbasierte Content Card heute um 14 Uhr gesendet wird und ein Ablauf von 1 Tag festgelegt ist, läuft sie am folgenden Tag um 14 Uhr ab.

{% multi_lang_include alerts/note_alerts.md alert='Content Cards frequency capping' %}

Bei aktionsbasierter Zustellung gibt es eine erwartete kurze Verzögerung, bevor die Content Card erscheint. Details dazu, warum dies geschieht und wie Sie die Verzögerung minimieren können, finden Sie unter [Warum erscheinen Content Cards nicht sofort nach einem Trigger-Event?]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card#why-dont-content-cards-appear-immediately-after-a-trigger-event).

#### Geplante Zustellung {#scheduled-delivery}

Für Content-Card-Campaigns mit geplanter Zustellung können Sie festlegen, wann Braze die Zielgruppeneignung und Personalisierung für neue Content-Card-Campaigns ermittelt, indem Sie bestimmen, wann die Karte erstellt wird. Weitere Informationen finden Sie unter [Kartenerstellung]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/card_creation).

#### Zielgruppe zusammenstellen {#choose-users-to-target}

Als Nächstes [stellen Sie Ihre Zielgruppe zusammen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users), indem Sie Segments oder Filter auswählen, um Ihre Zielgruppe einzugrenzen. Sie erhalten automatisch eine Vorschau der ungefähren Segment-Population. Beachten Sie, dass die exakte Segment-Zugehörigkeit immer vor dem Senden der Nachricht berechnet wird.

{% multi_lang_include audience/target_audiences.md %}

#### Konversions-Events auswählen {#choose-conversion-events}

Braze ermöglicht es Ihnen zu tracken, wie oft Nutzer:innen bestimmte Aktionen – [Konversions-Events]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) – nach dem Empfang einer Campaign ausführen. Sie haben die Möglichkeit, ein Zeitfenster von bis zu 30 Tagen festzulegen, in dem eine Konversion gezählt wird, wenn die Nutzer:in die angegebene Aktion ausführt.

{% endtab %}

{% tab Canvas %}

Falls noch nicht geschehen, vervollständigen Sie die verbleibenden Abschnitte Ihrer Canvas-Komponente. Details zum Aufbau des restlichen Canvas, einschließlich multivariater Tests und [Optimierung mit BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#optimize-canvas-variants-with-brazeai), finden Sie unter [Canvas erstellen]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-2-build-your-canvas).

{% endtab %}
{% endtabs %}

## Schritt 6: Überprüfen und bereitstellen {#step-6-review-and-deploy}

Wenn Sie Ihre Campaign oder Ihr Canvas fertig erstellt haben, überprüfen Sie die Details, [testen Sie sie]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages) und senden Sie sie ab. Weitere Informationen finden Sie unter [Testnachrichten senden]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=content%20card).

{% alert note %}
Content Cards erfordern im Produktivbetrieb zwar keine Push-Benachrichtigungen, für Testsendungen muss Push jedoch auf Ihren Testgeräten aktiviert sein, da die Karte über die Push-Payload zugestellt wird. Test-Content-Cards laufen etwa fünf Minuten nach dem Versand ab.
{% endalert %}

{% alert warning %}
Nachdem eine Content Card gestartet wurde, kann sie nicht mehr bearbeitet werden. Sie kann lediglich daran gehindert werden, an neue Nutzer:innen gesendet zu werden, und aus den Feeds der Nutzer:innen entfernt werden. Lesen Sie [Gesendete Karten aktualisieren]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card#updating-launched-cards), um zu erfahren, wie Sie mit diesem Szenario umgehen können.
{% endalert %}

Sehen Sie sich als Nächstes [Content-Card-Reporting]({{site.baseurl}}/user_guide/channels/content_cards/reporting) an, um zu erfahren, wie Sie auf die Ergebnisse Ihrer Content-Card-Kampagnen zugreifen können.

## Wissenswertes {#things-to-know}

### Payload- und Feed-Beschränkungen {#payload-and-feed-limitations}

Um die Performance zu gewährleisten, unterliegen Content Cards zwei wesentlichen Einschränkungen: einer Begrenzung der Payload-Größe pro Karte und einer maximalen Anzahl von Karten, die in einem Feed angezeigt werden können.

#### Größenbeschränkungen für Content Cards {#size-limitations-for-content-cards}

Die gesamte Daten-Payload einer einzelnen Content Card darf **nach** dem Rendern einer etwaigen Liquid-Personalisierung 2 KB nicht überschreiten. Dazu zählen:

* Titel
* Nachricht
* Bild-URL (die Länge des URL-Strings selbst, nicht die Bilddateigröße)
* Linktext
* Link-URLs für alle angegebenen Plattformen (separate URLs für iOS, Android und Web zählen alle zur Gesamtgröße)
* Schlüssel-Wert-Paare (sowohl die Schlüsselnamen als auch deren Werte)

Die Verwendung von Liquid zum Abrufen langer Text-Strings (z. B. aus angepassten Attributen) kann dazu führen, dass Sie die Grenze überschreiten.

Der Campaign-Composer zeigt eine Warnung an, wenn Ihr statischer Content die Grenze überschreitet. Für dynamischen Content mit Liquid wird die Größe nicht vorhergesagt. Wenn die Nachrichtengröße 2 KB überschreitet, wird die Nachricht zum Sendezeitpunkt abgebrochen. Sie können diese Abbrüche im Nachrichtenaktivitätsprotokoll mit dem Grund `Content card maximum size exceeded` einsehen.

{% alert important %}
Während Testversendungen können Content Cards, die 2 KB überschreiten, dennoch zugestellt und korrekt angezeigt werden.
{% endalert %}

Hier sind einige Best Practices für die Verwaltung der Content-Card-Payload-Größe:

* Verwenden Sie URL-Shortener für lange Links. URLs, insbesondere solche mit umfangreichen Tracking-Parametern, können zu Problemen mit der Größenbegrenzung führen. Die Verwendung eines URL-Kürzungsdienstes kann die Zeichenanzahl drastisch reduzieren und Platz in der Payload freigeben.
* Kürzen Sie dynamischen Content mit Liquid. Wenn Sie Karten mit dynamischem Text aus Nutzer:innen-Attributen oder API-Aufrufen personalisieren, kann die Länge des Contents unvorhersehbar sein. Verwenden Sie proaktiv Liquid-Filter wie `truncate`, um die Länge von dynamischem Text zu begrenzen.
* Gehen Sie effizient mit plattformübergreifenden URLs um. Die 2-KB-Grenze umfasst die URLs für alle Plattformen, die Sie definieren. Die Verwendung langer, eindeutiger URLs für jede Plattform kann die Payload-Größe vervielfachen. Verwenden Sie nach Möglichkeit einen einzigen Link, der plattformübergreifend funktioniert, oder nutzen Sie URL-Shortener nach Bedarf.
* Ziehen Sie Banner für umfangreicheren Content in Betracht. Für Anwendungsfälle, die regelmäßig große Mengen an Content erfordern, ist der Content-Card-Kanal möglicherweise nicht die richtige Wahl. Banner unterliegen nicht der gleichen 2-KB-Payload-Beschränkung und eignen sich besser für die Einbettung umfangreicherer Inhalte direkt in eine App- oder Website-Erfahrung.

#### Anzahl der Karten im Feed {#number-of-cards-in-feed}

Jede:r Nutzer:in kann zu jedem Zeitpunkt bis zu 250 nicht abgelaufene Content Cards in ihrem/seinem Feed haben. Wenn diese Grenze überschritten wird, gibt Braze die ältesten Karten nicht mehr zurück, auch wenn sie ungelesen sind. Abgewiesene Karten zählen ebenfalls zu dieser Grenze, was bedeutet, dass eine hohe Anzahl abgewiesener Karten den verfügbaren Platz für ältere Karten reduzieren kann.

Um Probleme mit der Kartengrenze zu vermeiden, empfehlen wir die folgenden Best Practices:

- **Verwenden Sie kürzere Ablaufdaten:** Für zeitkritische Campaigns (z. B. einen Wochenendverkauf) legen Sie ein bestimmtes Ablaufdatum fest. So werden Karten automatisch aus dem Feed entfernt und zählen nach Ablauf ihrer Relevanz nicht mehr zur Grenze.
- **Nutzen Sie aktionsbasierte Entfernung:** Richten Sie Entfernungs-Events für transaktionale oder zielbasierte Karten ein. Beispielsweise sollte eine Karte, die Nutzer:innen auffordert, ihr Profil zu vervollständigen, entfernt werden, sobald ein `profile_completed`-Event protokolliert wird.
- **Überprüfen Sie langfristige Campaigns:** Prüfen Sie wiederkehrende oder laufende Campaigns regelmäßig, um sicherzustellen, dass sie nicht durch zu viele Karten im Laufe der Zeit eine schlechte Erfahrung für Ihre Nutzer:innen erzeugen.

### Erneute Qualifikation für Content Cards verstehen {#understanding-re-eligibility-for-content-cards}

Die erneute Qualifikation bestimmt, ob und wann Nutzer:innen eine Nachricht derselben Campaign mehr als einmal erhalten können. Bei Content Cards ist das Verständnis dieser Funktion entscheidend für die Verwaltung wiederkehrender Campaigns und die Vermeidung doppelter oder veralteter Nachrichten.

{% alert tip %}
Soll Ihr Content länger als 30 Tage bestehen bleiben? Probieren Sie [Banner]({{site.baseurl}}/user_guide/channels/banners).
{% endalert %}

#### Berechnung der erneuten Qualifikation {#how-re-eligibility-is-calculated}

Wenn Sie die erneute Qualifikation aktivieren, beginnt der Countdown für den „Wiedereintritt“ von Nutzer:innen in eine Campaign ab dem Zeitpunkt des Nachrichtenversands. Der genaue Zeitpunkt, zu dem dieser Countdown beginnt, hängt von Ihren Kartenerstellungseinstellungen ab:

- Content Cards, die [bei erster Impression]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/card_creation#differences) erstellt werden, verwenden den Impression-Zeitpunkt zur Berechnung der erneuten Qualifikation.
- Content Cards, die beim Campaign-Start, in Mehrkanalcampaigns oder beim Canvas-Schritt-Eintritt erstellt werden, verwenden den jeweils späteren Versand- oder Impression-Zeitpunkt.

#### Die 30-Tage-Ablaufzeit und erneute Qualifikation {#the-30-day-expiration-and-re-eligibility}

Eine häufige Verwechslung entsteht durch die Wechselwirkung zwischen der erneuten Campaign-Qualifikation und dem automatischen 30-Tage-Ablauf aller Content Cards.

Alle Content Cards werden 30 Tage nach dem Versand oder der Entfernung automatisch aus den Braze-Systemen gelöscht. Wenn Sie eine langfristige, wiederkehrende Campaign mit **deaktivierter** erneuter Qualifikation haben, können Nutzer:innen nach 30 Tagen dennoch dieselbe Karte erneut erhalten. Wenn die ursprüngliche Karte gelöscht wird, erkennt das System keinen Eintrag mehr, dass diese:r Nutzer:in die Campaign erhalten hat, und sie werden bei der nächsten Sitzung erneut qualifiziert.

Damit Nutzer:innen eine Nachricht einer bestimmten Campaign nur einmal erhalten, fügen Sie Ihrer Campaign oder Ihrem Canvas-Schritt einen Zielgruppenfilter für Nutzer:innen hinzu, die keine Nachricht dieser Campaign erhalten haben. Dieser Filter ist der zuverlässigste Weg, um doppelte Versendungen bei langfristigen Campaigns zu vermeiden.

### Verwaltung aktiver Content Cards {#managing-live-content-cards}

Nachdem Content Cards versendet wurden, warten sie in einem „Posteingang“ darauf, den Nutzer:innen zugestellt zu werden (ähnlich wie bei E-Mails). Nachdem der Content in die Content Card geladen wurde (zum Zeitpunkt der Anzeige), kann er während seiner Lebensdauer nicht mehr geändert werden. Dies gilt auch dann, wenn Sie eine API über Connected-Content aufrufen und sich die Daten des Endpunkts ändern. Diese Daten werden nicht aktualisiert. Der Versand an neue Nutzer:innen kann lediglich gestoppt und die Karten aus den Feeds der Nutzer:innen entfernt werden. Wenn Sie eine Campaign ändern, enthalten nur nach der Änderung versendete Karten die Aktualisierung.

#### Aktualisierung bereits versendeter Karten {#updating-launched-cards}

Um eine Karte für Nutzer:innen zu ändern, die sie bereits erhalten haben, müssen Sie eine der folgenden Methoden verwenden:

##### Option 1: Campaign duplizieren (empfohlen für sofortige Änderungen) {#option-1-duplicate-the-campaign-recommended-for-immediate-changes}

{% alert tip %}
Wir empfehlen diese Option für Nachrichten, bei denen Sie den aktuellsten Content in der Karte anzeigen, Änderungen sofort sichtbar sein müssen oder die erneute Qualifikation deaktiviert ist.
{% endalert %}

Der erste Ansatz ist, die Campaign zu archivieren und eine neue, duplizierte Campaign zu starten:

1. Stoppen Sie die ursprüngliche Campaign und wählen Sie bei der Aufforderung `Remove card after the next sync`.
2. Duplizieren Sie die Campaign, nehmen Sie Ihre Änderungen vor und starten Sie die neue Version.

Beim Duplizieren der Campaign müssen Sie die Zielgruppe für die neue Version definieren. Verwenden Sie Segmentierungsfilter, um zu steuern, wer die aktualisierte Karte erhält:
* Wenn Nutzer:innen nie erneut für eine Content Card qualifiziert sein sollen, können Sie nach Nutzer:innen filtern, die die vorherige Version der Content Card nicht erhalten haben, indem Sie den Filter `Received Message from Campaign` auf die Bedingung `Has Not` setzen.
* Wenn Nutzer:innen, die die vorherige Karte erhalten haben, nach X Tagen erneut qualifiziert sein sollen, können Sie den Filter für `Last Received Message from specific campaign` auf mehr als X Tage setzen **ODER** `Received Message from Campaign` mit der Bedingung `Has Not` verwenden.

###### Auswirkungen {#impact}

- **Bestehende Empfänger:innen:** Neue und bestehende Empfänger:innen sehen die aktualisierte Karte beim nächsten Feed-Refresh, sofern sie qualifiziert sind.
- **Berichtswesen:** Jede Version der Karte hat separate Analytics.

Angenommen, Sie haben eine Campaign eingerichtet, die durch einen Sitzungsstart ausgelöst wird, mit einer erneuten Qualifikation von 30 Tagen. Ein:e Nutzer:in hat die Campaign vor zwei Tagen erhalten, und Sie möchten den Text ändern. Archivieren Sie zunächst die Campaign und entfernen Sie die Karten aus dem Feed. Duplizieren Sie dann die Campaign und starten Sie sie mit dem neuen Text erneut. Wenn der/die Nutzer:in eine weitere Sitzung hat, erhält er/sie sofort die neue Karte.

##### Option 2: Campaign stoppen und neu starten {#option-2-stop-and-relaunch-the-same-campaign}

{% alert tip %}
Wir empfehlen diese Option für einzelne Nachrichten in einem Benachrichtigungscenter oder Nachrichteneingang (z. B. Aktionen), wenn es wichtig ist, dass die Analytics zusammengefasst bleiben, oder wenn die zeitliche Relevanz der Nachricht kein Thema ist (d. h. bestehende Empfänger:innen können auf das Qualifikationsfenster warten, bevor sie die aktualisierten Karten sehen).
{% endalert %}

Dieser Ansatz fasst alle Ihre Analytics in einer einzigen Campaign zusammen. Neu qualifizierte Nutzer:innen erhalten die neue Karte, aber die Aktualisierung für bestehende Empfänger:innen verzögert sich bis zur erneuten Qualifikation:

1. Stoppen Sie Ihre Campaign und wählen Sie bei der Aufforderung **Remove card after the next sync**.
2. Bearbeiten Sie Ihre Campaign nach Bedarf.
3. Starten Sie Ihre Campaign neu.

###### Auswirkungen

* **Bestehende Empfänger:innen:** Nutzer:innen, die die Karte bereits erhalten haben, erhalten die aktualisierten Karten erst, wenn sie erneut qualifiziert werden. Wenn die erneute Qualifikation deaktiviert ist, erhalten sie die neue Karte nie.
* **Berichtswesen:** Eine Campaign enthält alle Berichts-Analytics für die veröffentlichten Kartenversionen. Braze unterscheidet nicht zwischen den veröffentlichten Versionen.

Angenommen, Sie haben eine Campaign, die durch einen Sitzungsstart ausgelöst wird, mit einer erneuten Qualifikation von 30 Tagen. Ein:e Nutzer:in hat die Campaign vor zwei Tagen erhalten, und Sie möchten den Text ändern. Stoppen Sie zunächst die Campaign und entfernen Sie die Karte aus dem Feed. Veröffentlichen Sie dann die Campaign mit dem neuen Text erneut. Wenn der/die Nutzer:in eine weitere Sitzung hat, erhält er/sie die neue Karte in 28 Tagen.

{% alert note %}
Wenn Sie eine Campaign stoppen, die Einstellungen für das Entfernungs-Event bearbeiten und die Campaign neu starten, ohne die Karten aus dem Feed zu entfernen, verwenden alle bestehenden Karten in den Feeds der Nutzer:innen die aktualisierten Entfernungs-Event-Einstellungen. Die Karten behalten nicht die ursprüngliche Entfernungs-Event-Konfiguration bei, die beim ersten Versand galt.
{% endalert %}

#### Karten entfernen und ablaufen lassen {#removing-and-expiring-cards}

##### Manuelle Kartenentfernung {#manual-card-removal}

Sie können Karten jederzeit manuell aus den Feeds aller Nutzer:innen entfernen, indem Sie die Campaign stoppen.

1. Öffnen Sie die Content-Card-Campaign und wählen Sie „Campaign stoppen“.
2. Wählen Sie bei der Aufforderung **Remove card after the next sync**. Die Karte wird beim nächsten Feed-Refresh entfernt.

##### Automatische Kartenentfernung {#action-based-card-removal}

Sie können eine Karte automatisch entfernen lassen, wenn Nutzer:innen eine bestimmte Aktion ausführen, z. B. einen Kauf abschließen oder ein Feature aktivieren.

Geben Sie in Ihrer Campaign oder Ihrem Canvas-Schritt ein Entfernungs-Event an. Wenn Nutzer:innen dieses Event ausführen, wird die Karte bei einem nachfolgenden Refresh aus dem Feed entfernt, nachdem Braze das Event verarbeitet hat.

{% alert note %}
Diese Entfernung erfolgt nicht sofort. Es gibt eine Verarbeitungsverzögerung, sodass es mehrere Minuten und mehr als einen Feed-Refresh dauern kann, bis die Karte verschwindet.
{% endalert %}

{% alert tip %}
Sie können mehrere angepasste Events und Käufe angeben, die eine Karte aus dem Feed von Nutzer:innen entfernen sollen. Wenn eine dieser Aktionen von Nutzer:innen ausgeführt wird, werden alle bestehenden Karten, die von der Campaign versendet wurden, entfernt. Qualifizierte Karten werden weiterhin gemäß dem Nachrichtenzeitplan versendet.
{% endalert %}

![Panel „Content-Card-Entfernungsbedingungen“ mit der Option „Content-Card-Entfernungs-Event“.]({% image_buster /assets/img/content_cards/content_card_removal_event.png %})

##### Kartenablauf {#card-expiration}

Content Cards sind bis zu 30 Tage nach dem Versand verfügbar; nach 30 Tagen entfernt Braze sie aus den Feeds der Nutzer:innen und löscht sie aus den Braze-Systemen.

#### Karten länger als 30 Tage verfügbar machen {#making-cards-last-longer-than-30-days}

{% alert tip %}
Für Anwendungsfälle, bei denen Nachrichten länger als die 30-Tage-Content-Card-Grenze bestehen bleiben müssen, sollten Sie Banner in Betracht ziehen. Banner sind auf Langlebigkeit ausgelegt und haben kein Pflichtablaufdatum, sodass sie so lange sichtbar bleiben können, wie sie benötigt werden.
{% endalert %}

Wenn eine Karte den Anschein erwecken soll, immer verfügbar zu sein, können Sie eine wiederkehrende Campaign erstellen, die die Karte effektiv alle 30 Tage ersetzt:

1. Legen Sie die Dauer der Content Card auf 30 Tage fest.
2. Setzen Sie die erneute Campaign-Qualifikation auf 30 Tage.
3. Stellen Sie die Campaign so ein, dass sie bei „Sitzungsstart“ ausgelöst wird.

### Synchronisierung und Refresh von Content Cards {#content-card-sync-and-refresh}

Content Cards werden nach einem Zeitplan und beim Refresh des Feeds durch Ihre App synchronisiert. Das Synchronisierungsverhalten unterscheidet sich zwischen vollständiger und teilweiser Synchronisierung, und Ihre SDK-Integration beeinflusst, wann Karten beim Sitzungsstart aktualisiert werden. Für Implementierungsdetails siehe [Content-Card-Feed anpassen]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed) und [Content Cards erstellen]({{site.baseurl}}/developer_guide/content_cards/creating_cards).

### Auswirkungen des Stoppens von Content-Card-Campaigns {#impact-of-stopping-content-cards-campaigns}

Wenn Sie eine Campaign stoppen und **Remove card after the next sync** auswählen, entfernt Braze die Karte beim nächsten Refresh aus den Feeds der Nutzer:innen. Die Impression-Zahlen können niedriger sein als die Versandzahlen, da Nutzer:innen keine Impressions für Karten erzeugen können, die entfernt wurden, bevor sie angesehen werden konnten.

## Fehlerbehebung {#troubleshooting}

### Warum erscheinen Content Cards nicht sofort nach einem Trigger-Event? {#why-dont-content-cards-appear-immediately-after-a-trigger-event}

Bei Campaigns mit aktionsbasierter Zustellung (z. B. Sitzungsstart) gibt es eine erwartete kurze Verzögerung zwischen dem Trigger-Event und der Verfügbarkeit der Karte. Diese Verzögerung entsteht, weil:

- Das Trigger-Event an die Braze-Server gesendet wird
- Die Campaign ausgelöst und die Zielgruppeneignung der Nutzer:innen erfasst wird
- Die Content Card in der Datenbank für diese Nutzer:innen erstellt wird
- Das SDK synchronisiert und alle verfügbaren Karten auf das Gerät lädt

Wenn die SDK-Synchronisierung erfolgt, bevor die Zielgruppeneignung der Nutzer:innen erfasst wurde, erhalten die Nutzer:innen die Karte nicht.

Für neue Nutzer:innen in ihrer ersten Sitzung ist diese Verzögerung unvermeidbar. Für bestehende Nutzer:innen, die sofortige Verfügbarkeit benötigen, sollten Sie stattdessen eine geplante Zustellung in Betracht ziehen.

Wenn Sie die Verzögerung sowohl für neue als auch bestehende Nutzer:innen minimieren möchten, können Sie zwei Campaigns erstellen:

- **Bestehende Nutzer:innen mit einer Sitzungsanzahl größer als 0:** Verwenden Sie eine Campaign mit geplanter Zustellung. Karten werden vorab erstellt und sind sofort verfügbar.
- **Neue Nutzer:innen mit einer Sitzungsanzahl gleich 0:** Verwenden Sie eine aktionsgetriggerte Campaign. Karten werden nach dem ersten Sitzungs-Trigger erstellt.

Dieser Ansatz stellt sicher, dass bestehende Nutzer:innen Karten sofort sehen, während neue Nutzer:innen nach einer kurzen Verzögerung in ihrer ersten Sitzung ebenfalls erreicht werden. Weitere Strategien zur Verbesserung der Latenz finden Sie unter [Niedrige Latenz für Content Cards verbessern]({{site.baseurl}}/user_guide/channels/content_cards/best_practices/improving_low_latency_requirements).

### Warum liegen Impression- oder Dismiss-Zeitstempel außerhalb des Campaign-Zeitplans? {#why-do-impression-or-dismiss-timestamps-fall-outside-the-campaign-schedule}

Impression- und Dismiss-Zeitstempel in Analytics und Currents geben an, wann Nutzer:innen eine Content Card angesehen oder geschlossen haben – nicht, wann Braze die Karte erstellt oder gesendet hat. Eine Karte kann im Feed der Nutzer:innen verbleiben, bis Content Cards aktualisiert werden, sodass Impression- und Dismiss-Zeitstempel nach dem Sendefenster der Campaign liegen können.

Wenn die Zeiten dennoch unerwartet erscheinen:

- Prüfen Sie, ob Sie Analytics in Ihrer Unternehmenszeitzone oder in der Zeitzone der Nutzer:innen in Currents anzeigen.
- Stellen Sie sicher, dass die Nutzer:innen die Karte tatsächlich nach dem Erhalt angesehen oder geschlossen haben, anstatt nur mit der Sendezeit zu vergleichen.

Weitere Informationen zu Content-Card-Metriken finden Sie unter [Content-Card-Berichte]({{site.baseurl}}/user_guide/channels/content_cards/reporting).

### Fehler „All expiration values for a campaign must match“ {#all-expiration-values-for-a-campaign-must-match-error}

Dieser Fehler tritt auf, wenn eine Content-Card-Campaign mit mehreren Varianten unterschiedliche Ablaufeinstellungen für die einzelnen Varianten verwendet. Legen Sie für jede Variante denselben Ablauf (Dauer oder bestimmten Zeitpunkt) fest, oder reduzieren Sie die Campaign auf eine einzelne Variante, und speichern Sie erneut. Informationen zum Festlegen des Ablaufs beim Erstellen einer Campaign finden Sie unter [Zustellungszeitplan oder Trigger auswählen](#choose-a-delivery-schedule-or-trigger).