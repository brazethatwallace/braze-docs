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

## 1. Schritt: Wählen Sie, wo Sie Ihre Nachricht erstellen möchten {#step-1-choose-where-to-build-your-message}

Verwenden Sie Kampagnen für einfache, einzelne Nachrichten (z. B. um Nutzer:innen mit einer einzelnen Nachricht über ein Produkt zu informieren). Verwenden Sie Canvases für mehrstufige Journeys (z. B. um maßgeschneiderte Produktvorschläge basierend auf dem Nutzerverhalten über einen bestimmten Zeitraum zu senden).

{% tabs %}
{% tab Campaign %}

1. Gehen Sie zu **Messaging** > **Campaigns** und wählen Sie **Kampagne erstellen**.
2. Wählen Sie **Content Cards** oder, für Kampagnen, die auf mehrere Kanäle abzielen, **Multichannel**.
3. Geben Sie Ihrer Kampagne einen klaren und aussagekräftigen Namen.
4. Fügen Sie bei Bedarf [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams/) und [Tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags/) hinzu.
   * Tags erleichtern das Auffinden Ihrer Kampagnen und das Erstellen von Berichten. Wenn Sie beispielsweise den [Berichts-Builder]({{site.baseurl}}/user_guide/analytics/reports/report_builder/) verwenden, können Sie nach den relevanten Tags filtern.
5. Fügen Sie so viele Varianten hinzu und benennen Sie sie, wie Sie möchten. Sie können für jede hinzugefügte Variante unterschiedliche Plattformen, Nachrichtentypen und Layouts wählen. Weitere Informationen zu Varianten finden Sie unter [Multivariate und A/B-Tests]({{site.baseurl}}/user_guide/messaging/ab_testing/).

{% alert tip %}
Wenn alle Nachrichten in Ihrer Kampagne ähnlich sein oder denselben Inhalt haben werden, verfassen Sie Ihre Nachricht, bevor Sie zusätzliche Varianten hinzufügen. Anschließend können Sie **Aus Variante kopieren** aus dem Dropdown **Variante hinzufügen** auswählen.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. [Erstellen Sie Ihren Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/) mit dem Canvas-Composer.
2. Nachdem Sie Ihren Canvas eingerichtet haben, fügen Sie im Canvas-Builder einen Nachrichten-Schritt hinzu. Geben Sie Ihrem Schritt einen klaren und aussagekräftigen Namen.
3. Wählen Sie **Content Cards** als Ihren Messaging-Kanal.
4. Wählen Sie, wann Braze die Zielgruppeneignung und Personalisierung für die Content-Card berechnet. Dies kann beim Eintritt in den Schritt oder bei der ersten Impression (empfohlen) erfolgen. Schritte mit Content Cards können geplant oder aktionsbasiert sein.
5. Wählen Sie, ob Content Cards entfernt werden sollen, wenn Nutzer:innen einen Kauf abschließen oder ein angepasstes Event ausführen.
6. Legen Sie eine Ablaufzeit für die Content-Card fest (Verweildauer im Feed). Dies kann nach einer bestimmten Dauer oder zu einem bestimmten Zeitpunkt sein.
7. Filtern Sie Ihre Zielgruppe bzw. die Empfänger:innen für diesen Schritt nach Bedarf in den **Zustellungseinstellungen**. Sie können Ihre Zielgruppe weiter verfeinern, indem Sie Segmente angeben und zusätzliche Filter hinzufügen. Zielgruppenoptionen werden nach der Verzögerung zum Zeitpunkt des Nachrichtenversands überprüft.
8. Wählen Sie alle weiteren Messaging-Kanäle, die Sie mit Ihrer Nachricht kombinieren möchten.

{% endtab %}
{% endtabs %}

## 2. Schritt: Geben Sie Ihre Nachrichtentypen an {#step-2-specify-your-message-types}

Wählen Sie einen der drei grundlegenden Content-Card-Typen: **Klassisch**, **Hervorgehobenes Bild** und **Nur Bild**.

Um mehr über das erwartete Verhalten und Aussehen jedes Typs zu erfahren, lesen Sie [Kreative Details]({{site.baseurl}}/user_guide/channels/content_cards/creative_details/) oder schauen Sie sich die Links in der folgenden Tabelle an. Diese Content-Card-Typen werden sowohl von mobilen Apps als auch von Webanwendungen unterstützt.

| Nachrichtentyp | Beispiel | Beschreibung |
|---|---|---|
| [Klassisch]({{site.baseurl}}/user_guide/channels/content_cards/creative_details/#classic) | ![Eine klassische Content-Card mit einem kleinen Symbol und Text, der zur Buchung eines Fitnesskurses einlädt.]({% image_buster/assets/img_archive/cc_steppington_classic.png %}) | Die klassische Karte hat ein einfaches Layout mit einem fettgedruckten Titel, Nachrichtentext und einem optionalen Bild links neben Titel und Text. Am besten verwenden Sie ein quadratisches Bild oder Symbol für die klassische Karte. |
| [Hervorgehobenes Bild]({{site.baseurl}}/user_guide/channels/content_cards/creative_details/#captioned-image) | ![Eine hervorgehobene Content-Card mit dem Bild eines Gewichthebers und Text, der zur Buchung eines Fitnesskurses einlädt.]({% image_buster/assets/img_archive/cc_steppington_captioned.png %}) | Die hervorgehobene Content-Card präsentiert Ihren Inhalt mit Text und einem aufmerksamkeitsstarken Bild. |
| [Nur Bild]({{site.baseurl}}/user_guide/channels/content_cards/creative_details/#banner) | ![Eine Content-Card vom Typ „Nur Bild“ mit ausschließlich Text.]({% image_buster/assets/img_archive/cc_steppington_banner.png %}) | Die Karte „Nur Bild“ zieht die Aufmerksamkeit auf sich und bietet Platz für Bilder, GIFs und andere kreative, nicht-textliche Inhalte. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Nachrichtentypen angeben" }

## 3. Schritt: Content-Card verfassen {#step-3-compose-a-content-card}

Sie können alle Aspekte des Inhalts und Verhaltens Ihrer Nachricht im Tab **Verfassen** des Nachrichteneditors bearbeiten.

![Beispiel für Content-Card-Details im Tab „Verfassen“ des Nachrichteneditors.]({% image_buster /assets/img/content_card_compose.png %})

Der Inhalt hier variiert je nach dem im vorherigen Schritt gewählten **Kartentyp**, kann aber eine der folgenden Optionen umfassen:

#### Sprache {#language}

Wählen Sie **Sprachen hinzufügen**, um Ihre gewünschten Sprachen aus der bereitgestellten Liste hinzuzufügen. Dadurch wird [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic/#conditional-logic) in Ihre Nachricht eingefügt. Wir empfehlen, Ihre Sprachen auszuwählen, bevor Sie Ihren Inhalt schreiben, damit Sie Ihren Text an der richtigen Stelle im Liquid einfügen können. Eine vollständige Liste der verfügbaren Sprachen finden Sie unter [Unterstützte Sprachen]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported).

![Ein Fenster mit Englisch, Spanisch und Französisch als ausgewählte Sprachen sowie Titel, Beschreibung und Linktext als Felder zur Internationalisierung.]({% image_buster /assets/img/add_languages.png %}){: style="max-width:70%;"}

##### Nachrichten von rechts nach links erstellen {#create-right-to-left-messages}

Das endgültige Erscheinungsbild von Nachrichten, die von rechts nach links geschrieben werden, hängt weitgehend davon ab, wie Dienstanbieter sie darstellen. Best Practices für die Erstellung von Nachrichten, die von rechts nach links so genau wie möglich angezeigt werden, finden Sie unter [Nachrichten von rechts nach links erstellen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages/).

#### Titel und Nachricht {#title-and-message}

Schreiben Sie, was Sie möchten. Es gibt keine Beschränkungen, aber je schneller Sie Ihre Botschaft vermitteln und Ihre Kund:innen zum Klicken bewegen, desto besser! Wir empfehlen klare und prägnante Titel und Nachrichteninhalte. Beachten Sie, dass diese Felder für Karten vom Typ „Nur Bild“ nicht verfügbar sind.

#### Bild {#image}

Um ein Bild zu Ihrer Content-Card hinzuzufügen, können Sie **Bild hinzufügen** auswählen oder eine Bild-URL angeben. Wenn Sie **Bild hinzufügen** auswählen, öffnet sich die **Medienbibliothek**, in der Sie ein zuvor hochgeladenes Bild auswählen oder ein neues hinzufügen können.

Jeder Nachrichtentyp und jede Plattform kann eigene empfohlene Proportionen und Anforderungen haben. Prüfen Sie diese daher unbedingt, bevor Sie ein Bild in Auftrag geben oder von Grund auf erstellen. Beachten Sie, dass die Nachrichtenfelder von Content Cards insgesamt auf 2&nbsp;KB begrenzt sind.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

#### An den Anfang pinnen {#pin-to-top}

Braze zeigt eine gepinnte Karte oben im Feed der Nutzer:innen an, und diese können sie nicht verwerfen. Wenn der Feed mehrere gepinnte Karten enthält, ordnet Braze sie chronologisch. Wenn Braze eine Content-Card zustellt, ist sie entweder gepinnt oder nicht gepinnt, und dieser Status ändert sich während der gesamten Lebensdauer der Karte nicht. Wenn Sie die Pin-Einstellung einer Kampagne ändern, gilt die Aktualisierung nur für zukünftig gesendete Karten. Sie ändert nicht den Pin-Status von Karten, die sich bereits im Feed der Nutzer:innen befinden.

![Nebeneinander-Vorschau der Content-Card in Braze für Mobilgerät und Web mit der ausgewählten Option „Diese Karte an den Anfang des Feeds pinnen“.]({% image_buster /assets/img/cc_pin_to_top.png %}){:style="border:none"}

#### Klickverhalten {#on-click-behavior}

Wenn Ihre Kund:innen auf einen angezeigten Link in der Karte klicken, kann der Link sie entweder tiefer in Ihre App oder zu einer anderen Website führen. Wenn Sie ein Klickverhalten für Ihre Content-Card festlegen, denken Sie daran, Ihren **Linktext** entsprechend zu aktualisieren.

Die folgenden Aktionen sind für Content-Card-Links verfügbar:

| Aktion | Beschreibung |
|---|---|
| Weiterleitung zu Web-URL | Eine nicht-native Webseite öffnen. |
| [Deeplink in die App]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls/#deep-link-to-in-app-content) | Deeplink zu einem bestehenden Bildschirm in Ihrer App. |
| Angepasstes Event protokollieren | Ein [angepasstes Event]({{site.baseurl}}/user_guide/data/activation/events/custom_events/) auswählen, das getriggert werden soll. Kann verwendet werden, um eine weitere Content-Card anzuzeigen oder zusätzliches Messaging auszulösen. |
| Angepasstes Attribut protokollieren | Ein [angepasstes Attribut]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/) auswählen, das für die aktuelle Nutzerin oder den aktuellen Nutzer gesetzt werden soll. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Klickverhalten" }

Die Optionen **Angepasstes Event protokollieren** und **Angepasstes Attribut protokollieren** erfordern die folgende SDK-Versionskompatibilität:

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

## 4. Schritt: Zusätzliche Einstellungen konfigurieren (optional) {#step-4-configure-additional-settings-optional}

Sie können [Schlüssel-Wert-Paare]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs/) verwenden, um Kategorien für Ihre Karten zu erstellen, [mehrere Content-Card-Feeds]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#multiple-feeds) einzurichten und die Sortierung der Karten anzupassen.

Um Schlüssel-Wert-Paare zu Ihrer Nachricht hinzuzufügen, gehen Sie zum Tab **Einstellungen** und wählen Sie **Neues Paar hinzufügen**.

## 5. Schritt: Erstellen Sie den Rest Ihrer Kampagne oder Ihres Canvas {#step-5-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

Erstellen Sie den Rest Ihrer Kampagne. In den folgenden Abschnitten finden Sie weitere Details zur optimalen Nutzung unserer Tools für die Erstellung von Content Cards.

#### Wählen Sie einen Zustellungszeitplan oder Trigger {#choose-a-delivery-schedule-or-trigger}

Content Cards können basierend auf einem geplanten Zeitpunkt, einer Aktion oder einem API-Trigger zugestellt werden. Weitere Informationen finden Sie unter [Ihre Kampagne planen]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/).

Sie können auch die Dauer der Kampagne und [Ruhezeiten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours/) festlegen sowie die Ablaufzeit der Content-Card bestimmen. Legen Sie ein bestimmtes Ablaufdatum oder die Anzahl der Tage bis zum Ablauf einer Karte fest – bis zu maximal 30 Tage. Alle Varianten haben identische Ablaufdaten.

Wenn Sie festlegen, dass eine Karte nach einer bestimmten Dauer abläuft (z. B. nach zwei Wochen), wird die Ablaufzeit ab dem Sendezeitpunkt der Karte berechnet. Bei geplanten Kampagnen ist dies der geplante Startzeitpunkt. Bei aktionsbasierten Kampagnen ist dies der Zeitpunkt, zu dem die Nutzerin oder der Nutzer die auslösende Aktion ausführt. Wenn beispielsweise eine aktionsbasierte Karte heute um 14 Uhr gesendet wird und eine Ablaufzeit von 1 Tag hat, läuft sie am nächsten Tag um 14 Uhr ab.

{% multi_lang_include alerts/note_alerts.md alert='Content Cards frequency capping' %}

Bei aktionsbasierter Zustellung gibt es eine erwartete kurze Verzögerung, bevor die Content-Card erscheint. Wenn beispielsweise eine Kampagne bei Sitzungsstart getriggert wird, muss dieses Trigger-Event zunächst an die Braze-Server übermittelt werden. Anschließend wird die Berechtigung der Nutzerin oder des Nutzers für die Kampagne erfasst. Wenn das SDK synchronisiert, wird die Karte erstellt und in derselben Sync-Antwort zurückgegeben. Falls die SDK-Synchronisierung vor der Erfassung der Nutzerberechtigung stattfand, erhält die Person die Karte nicht. Für Erstnutzer:innen ist diese Verzögerung unvermeidbar. Für bestehende Nutzer:innen, die sofortige Verfügbarkeit benötigen, sollten Sie stattdessen die geplante Zustellung in Betracht ziehen.

##### Geplante Zustellung {#scheduled-delivery}

Für Content-Card-Kampagnen mit geplanter Zustellung können Sie festlegen, wann Braze die Zielgruppeneignung und Personalisierung für neue Content-Card-Kampagnen auswertet, indem Sie angeben, wann die Karte erstellt wird. Weitere Informationen finden Sie unter [Kartenerstellung]({{site.baseurl}}/card_creation/).

#### Zielgruppe zusammenstellen {#choose-users-to-target}

Als Nächstes [stellen Sie Ihre Zielgruppe zusammen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users/), indem Sie Segmente oder Filter auswählen, um Ihre Zielgruppe einzugrenzen. Sie erhalten automatisch eine Vorschau der ungefähren Segmentgröße. Beachten Sie, dass die genaue Segmentzugehörigkeit immer unmittelbar vor dem Nachrichtenversand berechnet wird.

{% multi_lang_include target_audiences.md %}

#### Konversions-Events auswählen {#choose-conversion-events}

Braze ermöglicht es Ihnen zu verfolgen, wie oft Nutzer:innen bestimmte Aktionen, sogenannte [Konversions-Events]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/), nach Erhalt einer Kampagne ausführen. Sie haben die Möglichkeit, ein Zeitfenster von bis zu 30 Tagen festzulegen, in dem eine Conversion gezählt wird, wenn die Nutzerin oder der Nutzer die angegebene Aktion ausführt.

{% endtab %}

{% tab Canvas %}

Falls noch nicht geschehen, vervollständigen Sie die verbleibenden Abschnitte Ihrer Canvas-Komponente. Weitere Details zum Aufbau des restlichen Canvas, zur Implementierung von [Multivariate-Tests]({{site.baseurl}}/user_guide/messaging/ab_testing/) und [Intelligenter Auswahl]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection/) und mehr finden Sie im Schritt [Canvas erstellen]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#step-3-build-your-canvas) unserer Canvas-Dokumentation.

{% endtab %}
{% endtabs %}

## 6. Schritt: Überprüfen und bereitstellen {#step-6-review-and-deploy}

Nachdem Sie den letzten Teil Ihrer Kampagne oder Ihres Canvas fertiggestellt haben, überprüfen Sie die Details, [testen Sie]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages/) und senden Sie, wenn Sie bereit sind. Weitere Informationen finden Sie unter [Testnachrichten senden]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages/?tab=content%20card).

{% alert warning %}
Nachdem eine Content-Card gestartet wurde, kann sie nicht mehr bearbeitet werden. Sie kann nur daran gehindert werden, an neue Nutzer:innen gesendet zu werden, und aus den Feeds der Nutzer:innen entfernt werden. Lesen Sie [Gestartete Karten aktualisieren]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/#updating-launched-cards), um zu erfahren, wie Sie mit diesem Szenario umgehen können.
{% endalert %}

Schauen Sie sich als Nächstes [Content-Card-Reporting]({{site.baseurl}}/user_guide/channels/content_cards/reporting/) an, um zu erfahren, wie Sie auf die Ergebnisse Ihrer Content-Card-Kampagnen zugreifen können.

## Wissenswertes {#things-to-know}

### Payload- und Feed-Beschränkungen {#payload-and-feed-limitations}

Um die Performance zu gewährleisten, haben Content Cards zwei wesentliche Einschränkungen: ein Limit für die Payload-Größe jeder einzelnen Karte und eine maximale Anzahl von Karten, die in einem Feed angezeigt werden können.

#### Größenbeschränkungen für Content Cards {#size-limitations-for-content-cards}

Die gesamte Daten-Payload einer einzelnen Content-Card darf 2 KB **nach** dem Rendern jeglicher Liquid-Personalisierung nicht überschreiten. Dies umfasst:

* Titel
* Nachricht
* Bild-URL (die Länge des URL-Strings selbst, nicht die Bilddateigröße)
* Linktext
* Link-URLs für alle angegebenen Plattformen (separate URLs für iOS, Android und Web zählen alle zur Gesamtgröße)
* Schlüssel-Wert-Paare (sowohl die Schlüsselnamen als auch deren Werte)

Die Verwendung von Liquid zum Abrufen langer Textstrings (z. B. aus angepassten Attributen) kann dazu führen, dass Sie das Limit überschreiten.

Der Kampagnen-Composer zeigt eine Warnung an, wenn Ihr statischer Inhalt das Limit überschreitet. (Für dynamischen Content mit Liquid wird die Größe nicht vorhergesagt.) **Wenn die Nachrichtengröße 2 KB überschreitet, wird der Versand abgebrochen.** Sie können diese Abbrüche im Nachrichten-Aktivitätsprotokoll mit dem Grund `Content card maximum size exceeded` einsehen.

{% alert important %}
Während Testsendungen können Content Cards, die 2 KB überschreiten, dennoch zugestellt und korrekt angezeigt werden.
{% endalert %}

Hier sind einige Best Practices für die Verwaltung der Content-Card-Payload-Größe:

* Verwenden Sie URL-Shortener für lange Links. URLs, insbesondere solche mit umfangreichen Tracking-Parametern, können Probleme mit dem Größenlimit verursachen. Die Verwendung eines URL-Kürzungsdienstes kann die Zeichenanzahl drastisch reduzieren und Platz in der Payload freigeben.
* Kürzen Sie dynamischen Content mit Liquid. Wenn Sie Karten mit dynamischem Text aus Nutzerattributen oder API-Aufrufen personalisieren, kann die Länge des Inhalts unvorhersehbar sein. Verwenden Sie proaktiv Liquid-Filter wie `truncate`, um die Länge jedes dynamischen Texts zu begrenzen.
* Gehen Sie effizient mit plattformübergreifenden URLs um. Das 2-KB-Limit umfasst die URLs für alle Plattformen, die Sie definieren. Die Verwendung langer, einzigartiger URLs für jede Plattform kann die Payload-Größe vervielfachen. Verwenden Sie nach Möglichkeit einen einzelnen Link, der plattformübergreifend funktioniert, oder nutzen Sie bei Bedarf URL-Shortener.
* Ziehen Sie Banner für reichhaltigere Inhalte in Betracht. Für Anwendungsfälle, die durchgehend große Mengen an Inhalt erfordern, sind Content Cards möglicherweise nicht der richtige Kanal. Banner haben nicht die gleiche 2-KB-Payload-Beschränkung und eignen sich besser für die Einbettung reichhaltigerer Inhalte direkt in eine App- oder Website-Erfahrung.

#### Anzahl der Karten im Feed {#number-of-cards-in-feed}

Jede Nutzerin und jeder Nutzer kann zu jedem Zeitpunkt bis zu 250 nicht abgelaufene Content Cards in ihrem Feed haben. Wenn dieses Limit überschritten wird, gibt Braze die ältesten Karten nicht mehr zurück, selbst wenn sie ungelesen sind. Verworfene Karten zählen ebenfalls zu diesem Limit, was bedeutet, dass eine hohe Anzahl verworfener Karten den verfügbaren Platz für ältere Karten reduzieren kann.

Um Probleme mit dem Kartenlimit zu vermeiden, empfehlen wir die folgenden Best Practices:

- **Verwenden Sie kürzere Ablaufdaten:** Für zeitkritische Kampagnen (z. B. einen Wochenendverkauf) legen Sie ein bestimmtes Ablaufdatum fest. So werden Karten automatisch aus dem Feed entfernt und zählen nicht mehr zum Limit, nachdem sie nicht mehr relevant sind.
- **Nutzen Sie aktionsbasierte Entfernung:** Richten Sie Entfernungs-Events für transaktionale oder zielbasierte Karten ein. Beispielsweise sollte eine Karte, die Nutzer:innen auffordert, ihr Profil zu vervollständigen, entfernt werden, sobald ein `profile_completed`-Event protokolliert wird.
- **Überprüfen Sie langfristige Kampagnen:** Prüfen Sie wiederkehrende oder laufende Kampagnen, um sicherzustellen, dass sie keine schlechte Erfahrung für Ihre Nutzer:innen schaffen, indem sie den Feed im Laufe der Zeit mit zu vielen Karten füllen.

### Re-Eligibility für Content Cards verstehen {#understanding-re-eligibility-for-content-cards}

Re-Eligibility bestimmt, ob und wann eine Nutzerin oder ein Nutzer eine Nachricht derselben Kampagne mehr als einmal erhalten kann. Für Content Cards ist das Verständnis dieser Funktionsweise entscheidend für die Verwaltung wiederkehrender Kampagnen und um sicherzustellen, dass Nutzer:innen keine doppelten oder veralteten Nachrichten erhalten.

{% alert tip %}
Möchten Sie, dass Ihr Inhalt länger als 30 Tage bestehen bleibt? Probieren Sie [Banner]({{site.baseurl}}/user_guide/channels/banners/) aus.
{% endalert %}

#### Wie Re-Eligibility berechnet wird {#how-re-eligibility-is-calculated}

Wenn Sie Re-Eligibility aktivieren, beginnt der Countdown, wann eine Nutzerin oder ein Nutzer erneut in eine Kampagne „eintreten“ kann, nachdem die Nachricht gesendet wurde. Der genaue Zeitpunkt, an dem dieser Countdown beginnt, hängt von Ihren Kartenerstellungseinstellungen ab:

- Content Cards, die [bei der ersten Impression]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/card_creation/#differences-between-creating-cards-at-launch-or-entry-versus-at-first-impression) erstellt werden, verwenden den Impressionszeitpunkt zur Berechnung der Re-Eligibility.
- Content Cards, die beim Kampagnenstart, in Multichannel-Kampagnen oder beim Canvas-Schritt-Eintritt erstellt werden, verwenden den jeweils späteren Zeitpunkt von Sendezeitpunkt oder Impressionszeitpunkt.

#### Die 30-Tage-Ablaufzeit und Re-Eligibility {#the-30-day-expiration-and-re-eligibility}

Eine häufige Quelle der Verwirrung ist die Wechselwirkung zwischen Kampagnen-Re-Eligibility und der automatischen 30-Tage-Ablaufzeit aller Content Cards.

Alle Content Cards werden 30 Tage nach dem Senden oder Entfernen automatisch aus den Braze-Systemen gelöscht. Wenn Sie eine langfristige, wiederkehrende Kampagne mit **deaktivierter** Re-Eligibility haben, kann eine Nutzerin oder ein Nutzer nach 30 Tagen dennoch dieselbe Karte erneut erhalten. Wenn die ursprüngliche Karte gelöscht wird, sieht das System keinen Datensatz mehr darüber, dass diese Person die Kampagne erhalten hat, und macht sie bei der nächsten Sitzung erneut berechtigt.

Damit Nutzer:innen eine Nachricht einer bestimmten Kampagne nur einmal erhalten, fügen Sie Ihrer Kampagne oder Ihrem Canvas-Schritt einen Zielgruppen-Filter für Nutzer:innen hinzu, die keine Nachricht dieser Kampagne erhalten haben. Dieser Filter ist der zuverlässigste Weg, um doppelte Sendungen bei langfristigen Kampagnen zu verhindern.

### Live-Content-Cards verwalten {#managing-live-content-cards}

Nachdem Content Cards gesendet wurden, warten sie in einer Art „Posteingang“ darauf, an die Nutzerin oder den Nutzer zugestellt zu werden (ähnlich wie bei E-Mails). Nachdem der Inhalt in die Content-Card geladen wurde (zum Zeitpunkt der Anzeige), kann er während seiner Lebensdauer nicht mehr geändert werden. Dies gilt auch, wenn Sie eine API über Connected-Content aufrufen und sich die Daten vom Endpunkt ändern. Diese Daten werden nicht aktualisiert. Die Karte kann nur daran gehindert werden, an neue Nutzer:innen gesendet zu werden, und aus den Feeds der Nutzer:innen entfernt werden. Wenn Sie eine Kampagne ändern, haben nur zukünftig gesendete Karten die Aktualisierung.

#### Gestartete Karten aktualisieren {#updating-launched-cards}

Um eine Karte für Nutzer:innen zu ändern, die sie bereits erhalten haben, müssen Sie eine der folgenden Methoden verwenden:

##### Option 1: Kampagne duplizieren (empfohlen für sofortige Änderungen) {#option-1-duplicate-the-campaign-recommended-for-immediate-changes}

{% alert tip %}
Wir empfehlen diese Option für Nachrichten, bei denen Sie den neuesten Inhalt in der Karte anzeigen, Änderungen sofort sichtbar sein müssen oder wenn Re-Eligibility deaktiviert ist.
{% endalert %}

Der erste Ansatz besteht darin, die Kampagne zu archivieren und eine neue, duplizierte Kampagne zu starten:

1. Stoppen Sie die ursprüngliche Kampagne und wählen Sie bei der Aufforderung `Remove card after the next sync`.
2. Duplizieren Sie die Kampagne, nehmen Sie Ihre Änderungen vor und starten Sie die neue Version.

Wenn Sie die Kampagne duplizieren, müssen Sie die Zielgruppe für die neue Version definieren. Verwenden Sie Segmentierungs-Filter, um zu steuern, wer die aktualisierte Karte erhält:
* Wenn Nutzer:innen nie erneut für eine Content-Card berechtigt sein sollen, können Sie nach Nutzer:innen filtern, die die vorherige Version der Content-Card nicht erhalten haben, indem Sie den Filter `Received Message from Campaign` auf die Bedingung `Has Not` setzen.
* Wenn Nutzer:innen, die die vorherige Karte erhalten haben, in X Tagen erneut berechtigt sein sollen, können Sie den Filter für `Last Received Message from specific campaign` auf mehr als X Tage her setzen **ODER** `Received Message from Campaign` mit der Bedingung `Has Not`.

###### Auswirkungen {#impact}

* **Bestehende Empfänger:innen:** Neue und bestehende Empfänger:innen würden die aktualisierte Karte bei der nächsten Feed-Aktualisierung sehen, sofern sie berechtigt sind.
* **Reporting:** Jede Version der Karte hätte separate Analytics.

Nehmen wir an, Sie haben eine Kampagne eingerichtet, die bei Sitzungsstart getriggert wird und eine Re-Eligibility von 30 Tagen hat. Eine Nutzerin oder ein Nutzer hat die Kampagne vor zwei Tagen erhalten, und Sie möchten den Text ändern. Zuerst archivieren Sie die Kampagne und entfernen die Karten aus dem Feed. Zweitens duplizieren Sie die Kampagne und starten sie mit dem neuen Text neu. Wenn die Person eine weitere Sitzung hat, erhält sie sofort die neue Karte.

##### Option 2: Kampagne stoppen und neu starten {#option-2-stop-and-relaunch-the-same-campaign}

{% alert tip %}
Wir empfehlen diese Option für einzigartige Nachrichten in einem Benachrichtigungscenter oder Nachrichten-Posteingang (z. B. Aktionen), wenn es wichtig ist, dass die Analytics vereinheitlicht bleiben, oder wenn die Aktualität der Nachricht kein Problem darstellt (z. B. bestehende Empfänger:innen auf das Berechtigungsfenster warten können, bevor sie die aktualisierten Karten sehen).
{% endalert %}

Dieser Ansatz hält alle Ihre Analytics in einer einzigen Kampagne vereint. Neu berechtigte Nutzer:innen erhalten die neue Karte, aber die Aktualisierung für bestehende Empfänger:innen wird verzögert, bis sie erneut berechtigt sind:

1. Stoppen Sie Ihre Kampagne und wählen Sie bei der Aufforderung **Karte nach der nächsten Synchronisierung entfernen**.
2. Bearbeiten Sie Ihre Kampagne nach Bedarf.
3. Starten Sie Ihre Kampagne neu.

###### Auswirkungen

* **Bestehende Empfänger:innen:** Nutzer:innen, die die Karte bereits erhalten haben, würden die aktualisierten Karten erst erhalten, wenn sie erneut berechtigt werden. Wenn Re-Eligibility deaktiviert ist, würden sie die neue Karte nie erhalten.
* **Reporting:** Eine Kampagne enthält alle Reporting-Analytics für die gestarteten Kartenversionen. Braze unterscheidet nicht zwischen den gestarteten Versionen.

Nehmen wir an, Sie haben eine Kampagne, die bei Sitzungsstart getriggert wird und eine Re-Eligibility von 30 Tagen hat. Eine Nutzerin oder ein Nutzer hat die Kampagne vor zwei Tagen erhalten, und Sie möchten den Text ändern. Zuerst stoppen Sie die Kampagne und entfernen die Karte aus dem Feed. Zweitens veröffentlichen Sie die Kampagne mit dem neuen Text erneut. Wenn die Person eine weitere Sitzung hat, erhält sie die neue Karte in 28 Tagen.

#### Karten entfernen und ablaufen lassen {#removing-and-expiring-cards}

##### Manuelle Kartenentfernung {#manual-card-removal}

Sie können Karten jederzeit manuell aus den Feeds aller Nutzer:innen entfernen, indem Sie die Kampagne stoppen.

1. Öffnen Sie die Content-Card-Kampagne und wählen Sie **Kampagne anhalten**.
2. Wählen Sie bei der Aufforderung **Karte nach der nächsten Synchronisierung entfernen**. Die Karte wird bei der nächsten Feed-Aktualisierung entfernt.

##### Automatische Kartenentfernung {#action-based-card-removal}

Sie können eine Karte automatisch entfernen, wenn eine Nutzerin oder ein Nutzer eine bestimmte Aktion ausführt, z. B. einen Kauf abschließt oder ein Feature aktiviert.

Geben Sie in Ihrer Kampagne oder Ihrem Canvas-Schritt ein Entfernungs-Event an. Wenn eine Nutzerin oder ein Nutzer dieses Event ausführt, wird die Karte bei einer nachfolgenden Aktualisierung aus ihrem Feed entfernt, nachdem Braze das Event verarbeitet hat.

{% alert note %}
Diese Entfernung erfolgt nicht sofort. Es gibt eine Verarbeitungsverzögerung, sodass es mehrere Minuten und mehr als eine Feed-Aktualisierung dauern kann, bis die Karte verschwindet.
{% endalert %}

{% alert tip %}
Sie können mehrere angepasste Events und Käufe angeben, die eine Karte aus dem Feed einer Nutzerin oder eines Nutzers entfernen sollen. Wenn **eine** dieser Aktionen von der Person ausgeführt wird, werden alle bestehenden Karten, die von der Kampagne gesendet wurden, entfernt. Alle zukünftigen berechtigten Karten werden weiterhin gemäß dem Zeitplan der Nachricht gesendet.
{% endalert %}

![Bereich „Content-Card-Entfernungsbedingungen“ mit der Option „Content-Card-Entfernungs-Event“.]({% image_buster /assets/img/content_cards/content_card_removal_event.png %})

##### Kartenablauf {#card-expiration}

Content Cards bleiben bis zu 30 Tage nach dem Senden verfügbar; nach 30 Tagen entfernt Braze sie aus den Nutzer-Feeds und löscht sie aus den Braze-Systemen.

#### Karten länger als 30 Tage bestehen lassen {#making-cards-last-longer-than-30-days}

{% alert tip %}
Für Anwendungsfälle, bei denen Nachrichten länger als das 30-Tage-Limit von Content Cards bestehen bleiben müssen, sollten Sie Banner in Betracht ziehen. Banner sind auf Dauerhaftigkeit ausgelegt und haben kein obligatorisches Ablaufdatum, sodass sie so lange sichtbar bleiben können, wie sie benötigt werden.
{% endalert %}

Wenn Sie möchten, dass eine Karte scheinbar immer verfügbar ist, können Sie eine wiederkehrende Kampagne erstellen, die die Karte effektiv alle 30 Tage ersetzt:

1. Legen Sie die Dauer der Content-Card auf 30 Tage fest.
2. Setzen Sie die Kampagnen-Re-Eligibility auf 30 Tage.
3. Stellen Sie die Kampagne so ein, dass sie bei „Sitzungsstart“ getriggert wird.

### Synchronisierung und Aktualisierung von Content Cards {#content-card-sync-and-refresh}

Content Cards werden nach einem Zeitplan und beim Aktualisieren des Feeds durch Ihre App synchronisiert. Das Synchronisierungsverhalten unterscheidet sich zwischen vollständigen und teilweisen Synchronisierungen, und Ihre SDK-Integration beeinflusst, wann Karten bei Sitzungsstart aktualisiert werden. Implementierungsdetails finden Sie unter [Content-Card-Feed anpassen]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed/) und [Content Cards erstellen]({{site.baseurl}}/developer_guide/content_cards/creating_cards/).

### Auswirkungen des Stoppens von Content-Card-Kampagnen {#impact-of-stopping-content-cards-campaigns}

Wenn Sie eine Kampagne stoppen und **Karte nach der nächsten Synchronisierung entfernen** auswählen, entfernt Braze die Karte bei der nächsten Aktualisierung aus den Nutzer-Feeds. Die Impressionszahlen können niedriger als die Sendezahlen sein, da Nutzer:innen keine Karten sehen können, die entfernt wurden, bevor sie sie angesehen haben.