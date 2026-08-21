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

Verwenden Sie Campaigns für einfache, einzelne Nachrichten (z. B. um Nutzer:innen mit einer einzelnen Nachricht über ein Produkt zu informieren). Verwenden Sie Canvases für mehrstufige User-Journeys (z. B. um maßgeschneiderte Produktvorschläge basierend auf dem Nutzer:innenverhalten über einen bestimmten Zeitraum zu senden).

{% tabs %}
{% tab Campaign %}

1. Gehen Sie zu **Messaging** > **Campaigns** und wählen Sie **Create Campaign**.
2. Wählen Sie **Content Cards** oder, für Campaigns, die auf mehrere Kanäle abzielen, wählen Sie **Multichannel**.
3. Geben Sie Ihrer Campaign einen klaren und aussagekräftigen Namen.
4. Fügen Sie nach Bedarf [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams) und [Tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) hinzu.
   * Tags erleichtern das Auffinden Ihrer Campaigns und das Erstellen von Berichten. Wenn Sie beispielsweise den [Berichts-Builder]({{site.baseurl}}/user_guide/analytics/reports/report_builder) verwenden, können Sie nach den relevanten Tags filtern.
5. Fügen Sie so viele Varianten hinzu und benennen Sie diese, wie Sie möchten. Sie können für jede hinzugefügte Variante unterschiedliche Plattformen, Nachrichtentypen und Layouts auswählen. Weitere Informationen zu Varianten finden Sie unter [Multivariate und A/B-Tests]({{site.baseurl}}/user_guide/messaging/ab_testing).

{% alert tip %}
Wenn alle Nachrichten in Ihrer Campaign ähnlich sind oder denselben Inhalt haben, verfassen Sie Ihre Nachricht, bevor Sie weitere Varianten hinzufügen. Sie können dann **Copy from Variant** aus dem **Add Variant**-Dropdown auswählen.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. [Erstellen Sie Ihren Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) mit dem Canvas-Composer.
2. Nachdem Sie Ihren Canvas eingerichtet haben, fügen Sie im Canvas-Builder einen Nachrichten-Schritt hinzu. Geben Sie Ihrem Schritt einen klaren und aussagekräftigen Namen.
3. Wählen Sie **Content Cards** als Ihren Messaging-Kanal.
4. Legen Sie fest, wann Braze die Zielgruppeneignung und Personalisierung für die Content-Card berechnet. Dies kann beim Schritt-Eintritt oder bei der ersten Impression (empfohlen) erfolgen. Schritte mit Content Cards können geplant oder aktionsbasiert sein.
5. Legen Sie fest, ob Content Cards entfernt werden sollen, wenn Nutzer:innen einen Kauf abschließen oder ein angepasstes Event ausführen.
6. Legen Sie eine Ablaufzeit für die Content-Card fest (Verweildauer im Feed). Dies kann nach einer bestimmten Zeitspanne oder zu einem bestimmten Zeitpunkt sein.
7. Filtern Sie Ihre Zielgruppe bzw. die Empfänger:innen für diesen Schritt nach Bedarf in den **Zustellungseinstellungen**. Sie können Ihre Zielgruppe weiter verfeinern, indem Sie Segmente angeben und zusätzliche Filter hinzufügen. Die Zielgruppenoptionen werden nach der Verzögerung zum Zeitpunkt des Nachrichtenversands überprüft.
8. Wählen Sie alle weiteren Messaging-Kanäle aus, die Sie mit Ihrer Nachricht kombinieren möchten.

{% endtab %}
{% endtabs %}

## Schritt 2: Nachrichtentypen festlegen {#step-2-specify-your-message-types}

Wählen Sie einen der drei wesentlichen Content-Card-Typen aus: **Klassisch**, **Hervorgehobenes Bild** und **Nur Bild**.

Weitere Informationen zum erwarteten Verhalten und Erscheinungsbild der einzelnen Typen finden Sie unter [Kreative Details]({{site.baseurl}}/user_guide/channels/content_cards/creative_details). Sie können auch die Links in der folgenden Tabelle nutzen. Diese Content-Card-Typen werden sowohl von mobilen Apps als auch von Webanwendungen unterstützt.

| Nachrichtentyp | Beispiel | Beschreibung |
|---|---|---|
| [Klassisch]({{site.baseurl}}/user_guide/channels/content_cards/creative_details#content-card-types) | ![Eine klassische Content-Card mit einem kleinen Symbol und Text, der dazu einlädt, einen Trainingskurs zu buchen.]({% image_buster/assets/img_archive/cc_steppington_classic.png %}) | Die klassische Karte hat ein übersichtliches Layout mit einem fettgedruckten Titel, Nachrichtentext und einem optionalen Bild, das am Anfang des Titels und Textes platziert wird. Für die klassische Karte eignet sich am besten ein quadratisches Bild oder Symbol. |
| [Hervorgehobenes Bild]({{site.baseurl}}/user_guide/channels/content_cards/creative_details#content-card-types) | ![Eine hervorgehobene Content-Card mit dem Bild eines Gewichthebers und Text, der dazu einlädt, einen Trainingskurs zu buchen.]({% image_buster/assets/img_archive/cc_steppington_captioned.png %}) | Die hervorgehobene Content-Card präsentiert Ihren Content mit Text und einem aufmerksamkeitsstarken Bild. |
| [Nur Bild]({{site.baseurl}}/user_guide/channels/content_cards/creative_details#content-card-types) | ![Eine Content-Card „Nur Bild“ mit ausschließlich Text.]({% image_buster/assets/img_archive/cc_steppington_banner.png %}) | Die Karte „Nur Bild“ zieht die Aufmerksamkeit auf sich und bietet Platz für Bilder, GIFs und andere kreative, nicht-textbasierte Inhalte. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Schritt 2: Nachrichtentypen festlegen" }

## Schritt 3: Eine Content-Card verfassen {#step-3-compose-a-content-card}

Sie können alle Aspekte des Inhalts und Verhaltens Ihrer Nachricht im Tab **Verfassen** des Nachrichteneditors bearbeiten.

![Beispielhafte Content-Card-Details im Tab „Verfassen“ des Nachrichteneditors.]({% image_buster /assets/img/content_card_compose.png %})

Der Inhalt hier variiert je nach dem im vorherigen Schritt gewählten **Kartentyp**, kann aber eine der folgenden Optionen umfassen:

### Sprache {#language}

Wählen Sie **Sprachen hinzufügen**, um Ihre gewünschten Sprachen aus der bereitgestellten Liste hinzuzufügen. Dadurch wird [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic#conditional-logic) in Ihre Nachricht eingefügt. Wir empfehlen, Ihre Sprachen auszuwählen, bevor Sie Ihren Inhalt verfassen, damit Sie Ihren Text an der richtigen Stelle im Liquid einfügen können. Eine vollständige Liste der verfügbaren Sprachen finden Sie unter [Unterstützte Sprachen]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization#languages-supported).

![Ein Fenster mit Englisch, Spanisch und Französisch als ausgewählte Sprachen sowie Titel, Beschreibung und Linktext als Felder zur Internationalisierung.]({% image_buster /assets/img/add_languages.png %}){: style="max-width:70%;"}

#### Nachrichten von rechts nach links erstellen {#create-right-to-left-messages}

Das endgültige Erscheinungsbild von Nachrichten mit Rechts-nach-links-Schrift hängt weitgehend davon ab, wie Dienstanbieter sie darstellen. Best Practices für die Erstellung von Rechts-nach-links-Nachrichten, die möglichst korrekt angezeigt werden, finden Sie unter [Nachrichten von rechts nach links erstellen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages).

#### Titel und Nachricht {#title-and-message}

Schreiben Sie, was Sie möchten. Es gibt keine Beschränkungen, aber je schneller Sie Ihre Botschaft vermitteln und Ihre Kund:innen zum Klicken bewegen können, desto besser! Wir empfehlen klare und prägnante Titel und Nachrichteninhalte. Beachten Sie, dass diese Felder für reine Bildkarten nicht verfügbar sind.

#### Bild {#image}

Um ein Bild zu Ihrer Content-Card hinzuzufügen, können Sie **Bild hinzufügen** auswählen oder eine Bild-URL angeben. Durch Auswahl von **Bild hinzufügen** wird die **Medienbibliothek** geöffnet, in der Sie ein zuvor hochgeladenes Bild auswählen oder ein neues hinzufügen können.

Jeder Nachrichtentyp und jede Plattform kann eigene empfohlene Proportionen und Anforderungen haben. Prüfen Sie diese daher unbedingt, bevor Sie ein Bild in Auftrag geben oder von Grund auf erstellen. Beachten Sie, dass die Felder für Content-Card-Nachrichten auf insgesamt 2&nbsp;KB begrenzt sind.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

#### An den Anfang pinnen {#pin-to-top}

Braze zeigt eine gepinnte Karte oben im Feed der Nutzer:innen an, und die Nutzer:innen können sie nicht verwerfen. Wenn der Feed von Nutzer:innen mehrere gepinnte Karten enthält, ordnet Braze diese chronologisch an. Wenn Braze eine Content-Card zustellt, ist sie entweder gepinnt oder nicht gepinnt, und dieser Status ändert sich für die gesamte Lebensdauer der Karte nicht. Wenn Sie die Pinning-Einstellung einer Campaign ändern, gilt die Aktualisierung nur für Karten, die nach der Änderung gesendet werden. Der gepinnte Status von Karten, die sich bereits im Feed der Nutzer:innen befinden, wird nicht geändert.

![Nebeneinander-Ansicht der Content-Card-Vorschau in Braze für Mobilgeräte und Internet mit der ausgewählten Option „Diese Karte oben im Feed anpinnen“.]({% image_buster /assets/img/cc_pin_to_top.png %}){:style="border:none"}

#### Klickverhalten {#on-click-behavior}

Wenn Ihre Kund:innen auf einen angezeigten Link in der Karte klicken, kann der Link sie entweder tiefer in Ihre App oder zu einer anderen Website führen. Wenn Sie ein Klickverhalten für Ihre Content-Card festlegen, denken Sie daran, Ihren **Linktext** entsprechend zu aktualisieren.

Die folgenden Aktionen sind für Content-Card-Links verfügbar:

| Aktion | Beschreibung |
|---|---|
| Weiterleitung zu Web-URL | Öffnet eine nicht-native Webseite. |
| [Deeplink in die App]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls#deep-link-to-in-app-content) | Deeplink zu einem vorhandenen Bildschirm in Ihrer App. |
| Angepasstes Event protokollieren | Wählen Sie ein [angepasstes Event]({{site.baseurl}}/user_guide/data/activation/events/custom_events) zum Auslösen. Kann verwendet werden, um eine weitere Content-Card anzuzeigen oder zusätzliches Messaging auszulösen. |
| Angepasstes Attribut protokollieren | Wählen Sie ein [angepasstes Attribut]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes), das für die aktuellen Nutzer:innen gesetzt werden soll. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Klickverhalten" }

Die Optionen **Angepasstes Event protokollieren** und **Angepasstes Attribut protokollieren** erfordern die folgenden SDK-Mindestversionen:

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

## Schritt 4: Zusätzliche Einstellungen konfigurieren (optional) {#step-4-configure-additional-settings-optional}

Sie können [Schlüssel-Wert-Paare]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs) verwenden, um Kategorien für Ihre Karten zu erstellen, [mehrere Content-Card-Feeds]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed#multiple-feeds) einzurichten und die Sortierung von Karten anzupassen.

Um Schlüssel-Wert-Paare zu Ihrer Nachricht hinzuzufügen, gehen Sie zum Tab **Einstellungen** und wählen Sie **Neues Paar hinzufügen**.

## Schritt 5: Erstellen Sie den Rest Ihrer Kampagne oder Ihres Canvas {#step-5-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

Erstellen Sie den Rest Ihrer Kampagne. In den folgenden Abschnitten finden Sie weitere Details zur optimalen Nutzung unserer Tools für Content Cards.

### Wählen Sie einen Zustellungszeitplan oder Trigger {#choose-a-delivery-schedule-or-trigger}

Content Cards können basierend auf einem geplanten Zeitpunkt, einer Aktion oder einem API-Trigger zugestellt werden. Weitere Informationen finden Sie unter [Ihre Kampagne planen]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign).

Sie können auch die Dauer der Kampagne und [Ruhezeiten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours) festlegen sowie das Ablaufdatum der Content-Card bestimmen. Legen Sie ein bestimmtes Ablaufdatum oder die Anzahl der Tage bis zum Ablauf einer Karte fest – bis zu 30 Tage. Alle Varianten müssen dasselbe Ablaufdatum verwenden (Dauer oder bestimmter Zeitpunkt).

Der Ablauf-Countdown beginnt ab dem Sendezeitpunkt der Karte:

- **Geplante Kampagnen:** Der Countdown beginnt zum geplanten Startzeitpunkt.
- **Aktionsbasierte Kampagnen:** Der Countdown beginnt, wenn die Nutzer:innen die auslösende Aktion ausführen.

Wenn beispielsweise eine aktionsbasierte Content-Card heute um 14 Uhr gesendet wird und ein Ablauf von 1 Tag eingestellt ist, läuft sie am folgenden Tag um 14 Uhr ab.

{% multi_lang_include alerts/note_alerts.md alert='Content Cards frequency capping' %}

Bei aktionsbasierter Zustellung gibt es eine erwartete kurze Verzögerung, bevor die Content-Card erscheint. Details dazu, warum dies geschieht und wie Sie die Verzögerung minimieren können, finden Sie unter [Warum erscheinen Content Cards nicht sofort nach einem Trigger-Event?]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card#why-dont-content-cards-appear-immediately-after-a-trigger-event).

#### Geplante Zustellung {#scheduled-delivery}

Für Content-Card-Kampagnen mit geplanter Zustellung können Sie festlegen, wann Braze die Zielgruppeneignung und Personalisierung für neue Content-Card-Kampagnen ermittelt, indem Sie bestimmen, wann die Karte erstellt wird. Weitere Informationen finden Sie unter [Kartenerstellung]({{site.baseurl}}/card_creation).

#### Zielgruppe zusammenstellen {#choose-users-to-target}

Als Nächstes [stellen Sie Ihre Zielgruppe zusammen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users), indem Sie Segmente oder Filter auswählen, um Ihre Zielgruppe einzugrenzen. Sie erhalten automatisch eine Vorschau der ungefähren Segmentgröße. Beachten Sie, dass die genaue Segmentzugehörigkeit immer berechnet wird, bevor die Nachricht gesendet wird.

{% multi_lang_include audience/target_audiences.md %}

#### Konversions-Events auswählen {#choose-conversion-events}

Braze ermöglicht es Ihnen zu verfolgen, wie oft Nutzer:innen bestimmte Aktionen, sogenannte [Konversions-Events]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events), nach Erhalt einer Kampagne ausführen. Sie haben die Möglichkeit, ein Zeitfenster von bis zu 30 Tagen festzulegen, in dem eine Konversion gezählt wird, wenn die Nutzer:innen die angegebene Aktion ausführen.

{% endtab %}

{% tab Canvas %}

Falls noch nicht geschehen, vervollständigen Sie die verbleibenden Abschnitte Ihrer Canvas-Komponente. Weitere Details zum Aufbau Ihres Canvas, zur Implementierung von [multivariaten Tests]({{site.baseurl}}/user_guide/messaging/ab_testing) und [intelligenter Auswahl]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection) und mehr finden Sie im Schritt [Canvas erstellen]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-2-build-your-canvas) unserer Canvas-Dokumentation.

{% endtab %}
{% endtabs %}

## Schritt 6: Überprüfen und bereitstellen {#step-6-review-and-deploy}

Nachdem Sie Ihre Campaign oder Ihr Canvas fertig erstellt haben, überprüfen Sie die Details, [testen Sie sie]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages) und senden Sie sie ab. Weitere Informationen finden Sie unter [Testnachrichten senden]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=content%20card).

{% alert note %}
Content Cards erfordern in der Produktion zwar keine Push-Benachrichtigungen, aber für Testversendungen muss Push auf Ihren Testgeräten aktiviert sein, da die Karte über die Push-Payload zugestellt wird. Test-Content-Cards laufen ungefähr fünf Minuten nach dem Versand ab.
{% endalert %}

{% alert warning %}
Nachdem eine Content-Card gestartet wurde, kann sie nicht mehr bearbeitet werden. Sie kann nur daran gehindert werden, an neue Nutzer:innen gesendet zu werden, und aus den Feeds der Nutzer:innen entfernt werden. Unter [Gesendete Karten aktualisieren]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card#updating-launched-cards) erfahren Sie, wie Sie mit diesem Szenario umgehen können.
{% endalert %}

Sehen Sie sich als Nächstes das [Content-Card-Reporting]({{site.baseurl}}/user_guide/channels/content_cards/reporting) an, um zu erfahren, wie Sie auf die Ergebnisse Ihrer Content-Card-Kampagnen zugreifen können.

## Wissenswertes {#things-to-know}

### Payload- und Feed-Beschränkungen {#payload-and-feed-limitations}

Zur Unterstützung der Performance haben Content Cards zwei wesentliche Einschränkungen: eine Begrenzung der Payload-Größe pro Karte und eine maximale Anzahl von Karten, die in einem Feed angezeigt werden können.

#### Größenbeschränkungen für Content Cards {#size-limitations-for-content-cards}

Die gesamte Daten-Payload einer einzelnen Content-Card darf **nach** dem Rendern jeglicher Liquid-Personalisierung 2 KB nicht überschreiten. Dazu gehören:

* Titel
* Nachricht
* Bild-URL (die Länge des URL-Strings selbst, nicht die Bilddateigröße)
* Linktext
* Link-URLs für alle angegebenen Plattformen (separate URLs für iOS, Android und Web zählen alle zur Gesamtgröße)
* Schlüssel-Wert-Paare (sowohl die Schlüsselnamen als auch deren Werte)

Die Verwendung von Liquid zum Abrufen langer Textstrings (z. B. aus angepassten Attributen) kann dazu führen, dass Sie das Limit überschreiten.

Der Campaign-Composer zeigt eine Warnung an, wenn Ihr statischer Content das Limit überschreitet. Für dynamischen Content mit Liquid wird die Größe nicht vorhergesagt. Wenn die Nachrichtengröße 2 KB überschreitet, wird sie zum Sendezeitpunkt abgebrochen. Sie können diese Abbrüche im Nachrichtenaktivitätsprotokoll mit dem Grund `Content card maximum size exceeded` einsehen.

{% alert important %}
Während Testsendungen können Content Cards, die 2 KB überschreiten, trotzdem zugestellt und korrekt angezeigt werden.
{% endalert %}

Hier sind einige Best Practices für die Verwaltung der Content-Card-Payload-Größe:

* Verwenden Sie URL-Shortener für lange Links. URLs, insbesondere solche mit umfangreichen Tracking-Parametern, können zu Problemen mit dem Größenlimit führen. Die Verwendung eines URL-Kürzungsdienstes kann die Zeichenanzahl drastisch reduzieren und Platz in der Payload freigeben.
* Kürzen Sie dynamischen Content mit Liquid. Wenn Sie Karten mit dynamischem Text aus Nutzer:innen-Attributen oder API-Aufrufen personalisieren, kann die Länge des Contents unvorhersehbar sein. Verwenden Sie proaktiv Liquid-Filter wie `truncate`, um die Länge jedes dynamischen Textes zu begrenzen.
* Gehen Sie effizient mit plattformübergreifenden URLs um. Das 2-KB-Limit umfasst die URLs für alle Plattformen, die Sie definieren. Die Verwendung langer, eindeutiger URLs für jede Plattform kann die Payload-Größe vervielfachen. Verwenden Sie nach Möglichkeit einen einzelnen Link, der plattformübergreifend funktioniert, oder nutzen Sie bei Bedarf URL-Shortener.
* Ziehen Sie Banner für reichhaltigeren Content in Betracht. Für Anwendungsfälle, die durchgehend große Mengen an Content erfordern, sind Content Cards möglicherweise nicht der richtige Kanal. Banner haben nicht dieselbe 2-KB-Payload-Beschränkung und eignen sich besser für die Einbettung reichhaltigerer Inhalte direkt in eine App- oder Website-Erfahrung.

#### Anzahl der Karten im Feed {#number-of-cards-in-feed}

Jede:r Nutzer:in kann zu jedem Zeitpunkt bis zu 250 nicht abgelaufene Content Cards in ihrem Feed haben. Wenn dieses Limit überschritten wird, gibt Braze die ältesten Karten nicht mehr zurück, selbst wenn sie ungelesen sind. Verworfene Karten zählen ebenfalls zu diesem Limit, was bedeutet, dass eine hohe Anzahl verworfener Karten den verfügbaren Platz für ältere Karten reduzieren kann.

Um Probleme mit dem Kartenlimit zu vermeiden, empfehlen wir die folgenden Best Practices:

- **Verwenden Sie kürzere Ablaufdaten:** Legen Sie für zeitkritische Campaigns (z. B. einen Wochenendverkauf) ein bestimmtes Ablaufdatum fest. Auf diese Weise werden Karten automatisch aus dem Feed entfernt und zählen nach Ablauf ihrer Relevanz nicht mehr zum Limit.
- **Nutzen Sie aktionsbasierte Entfernung:** Richten Sie Entfernungs-Events für transaktionale oder zielbasierte Karten ein. Beispielsweise sollte eine Karte, die Nutzer:innen auffordert, ihr Profil zu vervollständigen, entfernt werden, sobald ein `profile_completed`-Event protokolliert wird.
- **Überprüfen Sie langfristige Campaigns:** Überprüfen Sie wiederkehrende oder laufende Campaigns, um sicherzustellen, dass sie keine schlechte Erfahrung für Ihre Nutzer:innen schaffen, indem sie den Feed im Laufe der Zeit mit zu vielen Karten füllen.

### Erneute Berechtigung für Content Cards verstehen {#understanding-re-eligibility-for-content-cards}

Die erneute Berechtigung bestimmt, ob und wann Nutzer:innen eine Nachricht derselben Campaign mehr als einmal erhalten können. Für Content Cards ist das Verständnis dieser Funktionsweise entscheidend für die Verwaltung wiederkehrender Campaigns und um sicherzustellen, dass Nutzer:innen keine doppelten oder veralteten Nachrichten erhalten.

{% alert tip %}
Möchten Sie, dass Ihr Content länger als 30 Tage bestehen bleibt? Probieren Sie [Banner]({{site.baseurl}}/user_guide/channels/banners) aus.
{% endalert %}

#### Wie die erneute Berechtigung berechnet wird {#how-re-eligibility-is-calculated}

Wenn Sie die erneute Berechtigung aktivieren, beginnt der Countdown, wann Nutzer:innen eine Campaign erneut „betreten“ können, nachdem ihnen die Nachricht gesendet wurde. Der genaue Zeitpunkt, an dem dieser Countdown beginnt, hängt von Ihren Kartenerstellungseinstellungen ab:

- Content Cards, die [bei der ersten Impression]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/card_creation#differences) erstellt werden, verwenden den Impressionszeitpunkt zur Berechnung der erneuten Berechtigung.
- Content Cards, die beim Campaign-Start, in Multichannel-Campaigns oder beim Canvas-Schritt-Eintritt erstellt werden, verwenden den jeweils späteren Sende- oder Impressionszeitpunkt.

#### Die 30-Tage-Ablaufzeit und erneute Berechtigung {#the-30-day-expiration-and-re-eligibility}

Eine häufige Quelle der Verwirrung ist die Wechselwirkung zwischen der erneuten Berechtigung einer Campaign und dem automatischen 30-Tage-Ablauf aller Content Cards.

Alle Content Cards werden 30 Tage nach dem Senden oder Entfernen automatisch aus den Braze-Systemen gelöscht. Wenn Sie eine langfristige, wiederkehrende Campaign mit **deaktivierter** erneuter Berechtigung haben, können Nutzer:innen dieselbe Karte nach 30 Tagen trotzdem erneut erhalten. Wenn die ursprüngliche Karte gelöscht wird, sieht das System keinen Datensatz mehr darüber, dass diese:r Nutzer:in die Campaign erhalten hat, wodurch sie bei der nächsten Sitzung erneut berechtigt werden.

Damit Nutzer:innen eine Nachricht einer bestimmten Campaign nur einmal erhalten, fügen Sie Ihrer Campaign oder Ihrem Canvas-Schritt einen Zielgruppenfilter für Nutzer:innen hinzu, die keine Nachricht dieser Campaign erhalten haben. Dieser Filter ist die zuverlässigste Methode, um doppelte Sendungen bei langfristigen Campaigns zu verhindern.

### Verwaltung aktiver Content Cards {#managing-live-content-cards}

Nachdem Content Cards gesendet wurden, warten sie in einem „Posteingang“ darauf, an die Nutzer:innen zugestellt zu werden (ähnlich wie bei E-Mails). Nachdem der Content in die Content-Card geladen wurde (zum Zeitpunkt der Anzeige), kann er während seiner Lebensdauer nicht mehr geändert werden. Dies gilt auch, wenn Sie eine API über Connected-Content aufrufen und sich die Daten vom Endpunkt ändern. Diese Daten werden nicht aktualisiert. Es kann nur verhindert werden, dass sie an neue Nutzer:innen gesendet werden, und sie können aus den Feeds der Nutzer:innen entfernt werden. Wenn Sie eine Campaign ändern, enthalten nur Karten, die nach der Änderung gesendet werden, die Aktualisierung.

#### Aktualisierung gestarteter Karten {#updating-launched-cards}

Um eine Karte für Nutzer:innen zu ändern, die sie bereits erhalten haben, müssen Sie eine der folgenden Methoden verwenden:

##### Option 1: Campaign duplizieren (empfohlen für sofortige Änderungen) {#option-1-duplicate-the-campaign-recommended-for-immediate-changes}

{% alert tip %}
Wir empfehlen diese Option für Nachrichten, bei denen Sie den neuesten Content in der Karte anzeigen, Änderungen sofort sichtbar sein müssen oder die erneute Berechtigung deaktiviert ist.
{% endalert %}

Der erste Ansatz besteht darin, die Campaign zu archivieren und eine neue, duplizierte Campaign zu starten:

1. Stoppen Sie die ursprüngliche Campaign und wählen Sie bei Aufforderung `Remove card after the next sync`.
2. Duplizieren Sie die Campaign, nehmen Sie Ihre Änderungen vor und starten Sie die neue Version.

Wenn Sie die Campaign duplizieren, müssen Sie die Zielgruppe für die neue Version definieren. Verwenden Sie Segmentierungsfilter, um zu steuern, wer die aktualisierte Karte erhält:
* Wenn Nutzer:innen nie erneut für eine Content-Card berechtigt sein sollen, können Sie nach Nutzer:innen filtern, die die vorherige Version der Content-Card nicht erhalten haben, indem Sie den Filter `Received Message from Campaign` auf die Bedingung `Has Not` setzen.
* Wenn Nutzer:innen, die die vorherige Karte erhalten haben, in X Tagen erneut berechtigt sein sollen, können Sie den Filter für `Last Received Message from specific campaign` auf mehr als X Tage her setzen **ODER** `Received Message from Campaign` mit der Bedingung `Has Not`.

###### Auswirkung {#impact}

- **Bestehende Empfänger:innen:** Neue und bestehende Empfänger:innen sehen die aktualisierte Karte bei der nächsten Feed-Aktualisierung, wenn sie berechtigt sind.
- **Reporting:** Jede Version der Karte hat separate Analytics.

Nehmen wir an, Sie haben eine Campaign eingerichtet, die durch einen Sitzungsstart getriggert wird, und die erneute Berechtigung ist auf 30 Tage eingestellt. Ein:e Nutzer:in hat die Campaign vor zwei Tagen erhalten, und Sie möchten den Text ändern. Archivieren Sie zunächst die Campaign und entfernen Sie die Karten aus dem Feed. Duplizieren Sie dann die Campaign und starten Sie sie mit dem neuen Text erneut. Wenn der:die Nutzer:in eine weitere Sitzung hat, erhält er:sie sofort die neue Karte.

##### Option 2: Dieselbe Campaign stoppen und neu starten {#option-2-stop-and-relaunch-the-same-campaign}

{% alert tip %}
Wir empfehlen diese Option für einzigartige Nachrichten in einem Benachrichtigungscenter oder Nachrichten-Posteingang (z. B. Aktionen), wenn es wichtig ist, dass die Analytics vereinheitlicht sind, oder wenn die Aktualität der Nachricht kein Problem darstellt (z. B. bestehende Empfänger:innen auf das Berechtigungsfenster warten können, bevor sie die aktualisierten Karten sehen).
{% endalert %}

Dieser Ansatz hält alle Ihre Analytics in einer einzigen Campaign vereinheitlicht. Neu berechtigte Nutzer:innen erhalten die neue Karte, aber die Aktualisierung für bestehende Empfänger:innen wird verzögert, bis sie erneut berechtigt sind:

1. Stoppen Sie Ihre Campaign und wählen Sie bei Aufforderung **Remove card after the next sync**.
2. Bearbeiten Sie Ihre Campaign nach Bedarf.
3. Starten Sie Ihre Campaign neu.

###### Auswirkung

* **Bestehende Empfänger:innen:** Nutzer:innen, die die Karte bereits erhalten haben, erhalten die aktualisierten Karten erst, wenn sie erneut berechtigt sind. Wenn die erneute Berechtigung deaktiviert ist, erhalten sie die neue Karte nie.
* **Reporting:** Eine Campaign enthält alle Reporting-Analytics für die gestarteten Kartenversionen. Braze unterscheidet nicht zwischen den gestarteten Versionen.

Nehmen wir an, Sie haben eine Campaign, die durch einen Sitzungsstart getriggert wird und die erneute Berechtigung auf 30 Tage eingestellt hat. Ein:e Nutzer:in hat die Campaign vor zwei Tagen erhalten, und Sie möchten den Text ändern. Stoppen Sie zunächst die Campaign und entfernen Sie die Karte aus dem Feed. Veröffentlichen Sie dann die Campaign mit dem neuen Text erneut. Wenn der:die Nutzer:in eine weitere Sitzung hat, erhält er:sie die neue Karte in 28 Tagen.

{% alert note %}
Wenn Sie eine Campaign stoppen, die Entfernungs-Event-Einstellungen bearbeiten und die Campaign neu starten, ohne die Karten aus dem Feed zu entfernen, verwenden alle vorhandenen Karten in den Feeds der Nutzer:innen die aktualisierten Entfernungs-Event-Einstellungen. Die Karten behalten nicht die ursprüngliche Entfernungs-Event-Konfiguration bei, die beim ersten Senden galt.
{% endalert %}

#### Entfernen und Ablaufen von Karten {#removing-and-expiring-cards}

##### Manuelles Entfernen von Karten {#manual-card-removal}

Sie können Karten jederzeit manuell aus den Feeds aller Nutzer:innen entfernen, indem Sie die Campaign stoppen.

1. Öffnen Sie die Content-Card-Campaign und wählen Sie „Campaign stoppen“.
2. Wählen Sie bei Aufforderung **Remove card after the next sync**. Die Karte wird bei der nächsten Feed-Aktualisierung entfernt.

##### Automatisches Entfernen von Karten {#action-based-card-removal}

Sie können eine Karte automatisch entfernen, wenn Nutzer:innen eine bestimmte Aktion ausführen, z. B. einen Kauf abschließen oder ein Feature aktivieren.

Geben Sie in Ihrer Campaign oder Ihrem Canvas-Schritt ein Entfernungs-Event an. Wenn Nutzer:innen dieses Event ausführen, wird die Karte bei einer nachfolgenden Aktualisierung aus ihrem Feed entfernt, nachdem Braze das Event verarbeitet hat.

{% alert note %}
Diese Entfernung erfolgt nicht sofort. Es gibt eine Verarbeitungsverzögerung, sodass es mehrere Minuten und mehr als eine Feed-Aktualisierung dauern kann, bis die Karte verschwindet.
{% endalert %}

{% alert tip %}
Sie können mehrere angepasste Events und Käufe angeben, die eine Karte aus dem Feed von Nutzer:innen entfernen sollen. Wenn eine dieser Aktionen von Nutzer:innen ausgeführt wird, werden alle vorhandenen Karten, die von den Karten der Campaign gesendet wurden, entfernt. Berechtigte Karten werden weiterhin gemäß dem Zeitplan der Nachricht gesendet.
{% endalert %}

![Panel „Content-Card-Entfernungsbedingungen“ mit der Option „Content-Card-Entfernungs-Event“.]({% image_buster /assets/img/content_cards/content_card_removal_event.png %})

##### Kartenablauf {#card-expiration}

Content Cards bleiben bis zu 30 Tage nach dem Senden verfügbar; nach 30 Tagen entfernt Braze sie aus den Nutzer:innen-Feeds und löscht sie aus den Braze-Systemen.

#### Karten länger als 30 Tage verfügbar machen {#making-cards-last-longer-than-30-days}

{% alert tip %}
Für Anwendungsfälle, bei denen Nachrichten länger als das 30-Tage-Limit für Content Cards bestehen bleiben müssen, sollten Sie Banner in Betracht ziehen. Banner sind auf Dauerhaftigkeit ausgelegt und haben kein obligatorisches Ablaufdatum, sodass sie so lange sichtbar bleiben können, wie sie benötigt werden.
{% endalert %}

Wenn Sie möchten, dass eine Karte scheinbar immer verfügbar ist, können Sie eine wiederkehrende Campaign erstellen, die die Karte effektiv alle 30 Tage ersetzt:

1. Legen Sie die Dauer der Content-Card auf 30 Tage fest.
2. Setzen Sie die erneute Berechtigung der Campaign auf 30 Tage.
3. Stellen Sie die Campaign so ein, dass sie bei „Sitzungsstart“ getriggert wird.

### Synchronisierung und Aktualisierung von Content Cards {#content-card-sync-and-refresh}

Content Cards werden nach einem Zeitplan und beim Aktualisieren des Feeds durch Ihre App synchronisiert. Das Synchronisierungsverhalten unterscheidet sich zwischen vollständigen und teilweisen Synchronisierungen, und Ihre SDK-Integration beeinflusst, wann Karten beim Sitzungsstart aktualisiert werden. Implementierungsdetails finden Sie unter [Content-Card-Feed anpassen]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed) und [Content Cards erstellen]({{site.baseurl}}/developer_guide/content_cards/creating_cards).

### Auswirkung des Stoppens von Content-Card-Campaigns {#impact-of-stopping-content-cards-campaigns}

Wenn Sie eine Campaign stoppen und **Remove card after the next sync** auswählen, entfernt Braze die Karte bei der nächsten Aktualisierung aus den Nutzer:innen-Feeds. Die Impressionszahlen können niedriger sein als die Sendezahlen, da Nutzer:innen keine Impressions für Karten erzeugen können, die entfernt werden, bevor sie sie ansehen.

## Fehlerbehebung {#troubleshooting}

### Warum erscheinen Content Cards nicht sofort nach einem Trigger-Event? {#why-dont-content-cards-appear-immediately-after-a-trigger-event}

Bei Campaigns mit aktionsbasierter Zustellung (z. B. Sitzungsstart) gibt es eine erwartete kurze Verzögerung zwischen dem Trigger-Event und der Verfügbarkeit der Karte. Diese Verzögerung tritt auf, weil:

- Das Trigger-Event an die Braze-Server gesendet wird
- Die Campaign ausgelöst und die Zielgruppeneignung der Nutzer:innen erfasst wird
- Die Content-Card in der Datenbank für diese:n Nutzer:in erstellt wird
- Das SDK synchronisiert und alle verfügbaren Karten auf das Gerät lädt

Wenn die SDK-Synchronisierung stattfindet, bevor die Zielgruppeneignung der Nutzer:innen erfasst wurde, erhalten die Nutzer:innen die Karte nicht.

Für neue Nutzer:innen in ihrer ersten Sitzung ist diese Verzögerung unvermeidbar. Für bestehende Nutzer:innen, die sofortige Verfügbarkeit benötigen, sollten Sie stattdessen eine geplante Zustellung in Betracht ziehen.

Wenn Sie Verzögerungen sowohl für neue als auch für bestehende Nutzer:innen minimieren möchten, können Sie zwei Campaigns erstellen:

- **Bestehende Nutzer:innen mit einer Sitzungsanzahl größer als 0:** Verwenden Sie eine Campaign mit geplanter Zustellung. Karten werden vorab erstellt und sind sofort verfügbar.
- **Neue Nutzer:innen mit einer Sitzungsanzahl gleich 0:** Verwenden Sie eine aktionsgetriggerte Campaign. Karten werden nach dem ersten Sitzungs-Trigger erstellt.

Dieser Ansatz stellt sicher, dass bestehende Nutzer:innen Karten sofort sehen, während neue Nutzer:innen nach einer kurzen Verzögerung in ihrer ersten Sitzung ebenfalls erreicht werden. Weitere Strategien zur Verbesserung der Latenz finden Sie unter [Niedrige Latenz für Content Cards verbessern]({{site.baseurl}}/user_guide/channels/content_cards/best_practices/improving_low_latency_requirements).

### Warum liegen Impressions- oder Dismiss-Zeitstempel außerhalb des Campaign-Zeitplans? {#why-do-impression-or-dismiss-timestamps-fall-outside-the-campaign-schedule}

Impressions- und Dismiss-Zeitstempel in Analytics und Currents geben an, wann Nutzer:innen eine Content-Card angesehen oder verworfen haben – nicht, wann Braze die Karte erstellt oder gesendet hat. Eine Karte kann im Feed der Nutzer:innen verbleiben, bis Content Cards aktualisiert werden, sodass Impressions- und Dismiss-Zeitstempel nach dem Sendefenster der Campaign liegen können.

Wenn die Zeiten dennoch unerwartet erscheinen:

- Überprüfen Sie, ob Sie Analytics in der Zeitzone Ihres Unternehmens oder in der Zeitzone der Nutzer:innen in Currents betrachten.
- Stellen Sie sicher, dass die Nutzer:innen die Karte tatsächlich nach dem Empfang angesehen oder verworfen haben, anstatt nur mit der Sendezeit zu vergleichen.

Weitere Informationen zu Content-Card-Metriken finden Sie unter [Content-Card-Reporting]({{site.baseurl}}/user_guide/channels/content_cards/reporting).

### Fehler „All expiration values for a campaign must match“ {#all-expiration-values-for-a-campaign-must-match-error}

Dieser Fehler erscheint, wenn eine Content-Card-Campaign mit mehreren Varianten unterschiedliche Ablaufeinstellungen für die einzelnen Varianten verwendet. Legen Sie für jede Variante denselben Ablaufzeitraum (Dauer oder bestimmter Zeitpunkt) fest, oder reduzieren Sie die Campaign auf eine einzelne Variante, und speichern Sie dann erneut. Informationen zum Festlegen des Ablaufs beim Erstellen einer Campaign finden Sie unter [Zustellungszeitplan oder Trigger auswählen](#choose-a-delivery-schedule-or-trigger).