---
page_order: 3
nav_title: Segmentierungsfilter
article_title: Segmentierungsfilter
layout: glossary_page
glossary_top_header: "Segmentierungsfilter"
glossary_top_text: "Das Braze SDK bietet Ihnen ein leistungsstarkes Arsenal an Filtern, um Ihre Nutzer:innen anhand bestimmter Features und Attribute zu segmentieren und gezielt anzusprechen. Sie können diese Filter nach Filterkategorie durchsuchen oder eingrenzen.<br><br>Um mehr über die verschiedenen Datentypen angepasster Attribute zu erfahren, die Sie zur Segmentierung von Nutzer:innen verwenden können, lesen Sie <a href=\"/docs/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types\">Datentypen angepasster Attribute</a>."

page_type: glossary
tool: Segments
description: "Dieses Glossar listet die verfügbaren Filter auf, mit denen Sie Ihre Nutzer:innen segmentieren und gezielt ansprechen können."
search_rank: 2
glossary_tag_name: Filterkategorie
glossary_filter_text: "Wählen Sie eine Kategorie, um das Glossar einzugrenzen:"

glossary_tags:
  - name: Segment or CSV membership
  - name: Custom attribute
  - name: Custom events
  - name: Sessions
  - name: Retargeting
  - name: Channel subscription behavior
  - name: Purchase behavior
  - name: eCommerce
  - name: Demographic attributes
  - name: App
  - name: Uninstall
  - name: Devices
  - name: Location
  - name: Cohort membership
  - name: Install attribution
  - name: Intelligence and predictive
  - name: Social activity
  - name: Other Filters
  - name: Advertising use cases
  - name: User Attributes

glossaries:
  - name: Segment Membership
    description: "Ermöglicht es Ihnen, überall dort, wo Filter verwendet werden (z. B. in Segmenten, Campaigns und anderen), nach Segment-Zugehörigkeit zu filtern und mehrere verschiedene Segmente innerhalb einer Campaign anzusprechen. <br><br>Um die Segment-Zugehörigkeit zu einem bestimmten Zeitpunkt festzuhalten, exportieren Sie Nutzer:innen aus dem Segment im Dashboard oder rufen Sie den Endpunkt <a href=\"/docs/api/endpoints/export/user_data/post_users_segment/\"><code>/users/export/segment</code></a> auf, bevor Sie eine Campaign oder ein Canvas senden. Braze speichert keine nutzerbezogene Segmentierungshistorie, sodass Sie nicht rückwirkend prüfen können, ob ein:e Nutzer:in zu einem vergangenen Zeitpunkt in einem Segment war. Weitere Informationen finden Sie unter <a href=\"/docs/user_guide/data/distribution/export_braze_data/segment_data_to_csv/\">Segmentdaten als CSV exportieren</a>.<br><br>Beachten Sie, dass Segmente, die diesen Filter bereits verwenden, nicht weiter in andere Segmente eingeschlossen oder verschachtelt werden können, da dies einen Zyklus erzeugen könnte, bei dem Segment A Segment B einschließt, das dann wiederum versucht, Segment A einzuschließen. In diesem Fall würde das Segment sich ständig selbst referenzieren, sodass es unmöglich wäre zu berechnen, wer tatsächlich dazugehört. Außerdem erhöht eine solche Verschachtelung die Komplexität und kann die Verarbeitung verlangsamen. Erstellen Sie stattdessen das Segment, das Sie einschließen möchten, mit denselben Filtern neu.<br><br>Wenn ein Segment nicht im Dropdown-Menü des Filters **Segment Membership** erscheint, erstellen Sie es mit denselben Filtern neu und wählen Sie das neue Segment aus, oder bestätigen Sie, dass es nicht bereits auf eine Weise von dieser Zielgruppe abhängt, die einen Zyklus erzeugen würde."
    tags:
      - Segment or CSV membership
  - name: Braze Segment Extensions
    description: "Nachdem Sie eine Segmenterweiterung im Braze-Dashboard erstellt haben, können Sie diese Erweiterungen in Ihr Segment ein- oder ausschließen."
    tags:
      - Segment or CSV membership
  - name: Updated/Imported from CSV
    description: "Segmentiert Ihre Nutzer:innen danach, ob sie Teil eines CSV-Uploads waren oder nicht. Braze speichert pro Kundenprofil or Nutzerprofil nur die letzten 100 CSV-Importe für Segmentierungszwecke. Wenn ein:e Nutzer:in in mehr als 100 CSV-Importen vorkommt, die für Retargeting ausgewählt wurden, stehen nur die 100 neuesten für diesen Filter zur Verfügung. Ältere Importe stimmen nicht mehr mit diesem/dieser Nutzer:in überein."
    tags:
      - Segment or CSV membership
  - name: Custom Attributes
    description: "Bestimmt, ob ein:e Nutzer:in einem angepassten, aufgezeichneten Attributwert entspricht oder nicht. Der maximale Rückblickzeitraum beträgt 100 Jahre für Datums- und Zeitintervallvergleiche.<br><br>Zeitzone:<br>Zeitzone des Unternehmens"
    tags:
      - Custom attribute
  - name: Created At
    description: "Segmentiert Nutzer:innen danach, wann ihr Kundenprofil or Nutzerprofil erstellt wurde. Wenn ein:e Nutzer:in per CSV oder API hinzugefügt wurde, spiegelt dieser Filter das Datum wider, an dem sie hinzugefügt wurden. Wenn der/die Nutzer:in nicht per CSV oder API hinzugefügt wurde und die erste Sitzung vom SDK or Software-Development-Kit erfasst wird, spiegelt dieser Filter das Datum dieser ersten Sitzung wider. Der maximale Rückblickzeitraum beträgt 100 Jahre."
    tags:
      - Other Filters
  - name: Created From
    description: "Segmentiert Nutzer:innen danach, wo ihr Kundenprofil or Nutzerprofil erstellt wurde.<br><br>Die folgenden Werte werden unterstützt:<br>- SDK or Software-Development-Kit (<code>SDK or Software-Development-Kit</code>): Kundenprofil or Nutzerprofil über das Braze SDK or Software-Development-Kit erstellt.<br>- Representational State Transfer API (<code>Representational State Transfer</code>): Kundenprofil or Nutzerprofil über die Braze Representational State Transfer API erstellt.<br>- Push-Token / Textbaustein-Import (<code>pti</code>): Kundenprofil or Nutzerprofil über Push-Token / Textbaustein-Import erstellt.<br>- CSV (<code>csv</code>): Kundenprofil or Nutzerprofil über CSV-Import erstellt.<br>- Demo (<code>demo</code>): Kundenprofil or Nutzerprofil über Demodaten erstellt.<br>- Kurzmitteilungsdienst or SMS (<code>Kurzmitteilungsdienst or SMS</code>): Kundenprofil or Nutzerprofil über Kurzmitteilungsdienst or SMS erstellt.<br>- Shopify (<code>shopify</code>): Kundenprofil or Nutzerprofil über Shopify erstellt.<br>- WhatsApp (<code>whats_app</code>): Kundenprofil or Nutzerprofil über WhatsApp erstellt.<br>- Provider Event (<code>provider_event</code>): Kundenprofil or Nutzerprofil über ein Provider-Event erstellt.<br>- Provider Sync (<code>provider_sync</code>): Kundenprofil or Nutzerprofil über einen Provider-Sync erstellt.<br>- Landing-Page (<code>landing_page</code>): Kundenprofil or Nutzerprofil über eine Landing-Page erstellt."
    tags:
      - Other Filters
  - name: Nested Custom Attributes
    description: "Attribute, die Eigenschaften von angepassten Attributen sind.<br><br>Beim Filtern eines verschachtelten angepassten Zeitattributs können Sie wählen, ob nach „Tag des Jahres“ oder „Zeit“ gefiltert werden soll. „Tag des Jahres“ vergleicht nur Monat und Tag. „Zeit“ vergleicht den vollständigen Zeitstempel einschließlich des Jahres. Der maximale Rückblickzeitraum beträgt 100 Jahre für Zeitintervallvergleiche. Dieselbe Logik gilt beim Filtern nach Kontextvariablen in Canvas-Zielgruppenpfaden; siehe <a href=\"/docs/user_guide/messaging/design_and_edit/personalize/sources/context_variables/#day-of-year-and-time-filters-for-date-context-variables\">Tag-des-Jahres- und Zeitfilter für Datums-Kontextvariablen</a> für Details."
    tags:
      - Custom attribute
  - name: Day of Recurring Event
    description: "Dieser Filter betrachtet den Monat und Tag eines angepassten Attributs mit dem Datentyp „Datum“, berücksichtigt jedoch nicht das Jahr. Dieser Filter ist nützlich für jährliche Events.<br><br>Zeitzone&#58;<br>Dieser Filter passt sich an die jeweilige Zeitzone der Nutzer:innen an, sofern die Nachricht mit der Option für lokale Zeitplanung gesendet wird; andernfalls verwendet dieser Filter die Zeitzone Ihres Unternehmens."
    tags:
      - Custom attribute
  - name: Custom Event
    description: "Bestimmt, ob ein:e Nutzer:in ein speziell aufgezeichnetes Event ausgeführt hat oder nicht.<br><br>Beispiel:<br>Aktivität abgeschlossen mit Eigenschaft activity_name.<br><br>Zeitzone:<br>UTC – Kalendertag = 1 Kalendertag betrachtet 24–48 Stunden der Nutzerhistorie"
    tags:
      - Custom events
  - name: First Did Custom Event
    description: "Bestimmt den frühesten Zeitpunkt, zu dem ein:e Nutzer:in ein speziell aufgezeichnetes Event ausgeführt hat. Der maximale Rückblickzeitraum beträgt 100 Jahre. (24-Stunden-Zeitraum) <br><br>Beispiel:<br> Erster Warenkorb-Abbruch vor weniger als 1 Tag<br><br>Zeitzone:<br>Zeitzone des Unternehmens"
    tags:
      - Custom events
  - name: Last Did Custom Event
    description: "Bestimmt den letzten Zeitpunkt, zu dem ein:e Nutzer:in ein speziell aufgezeichnetes Event ausgeführt hat. Dieser Filter unterstützt Dezimalwerte, z. B. 0,25 Stunden. Der maximale Rückblickzeitraum beträgt 100 Jahre. (24-Stunden-Zeitraum) <br><br>Beispiel:<br> Letzter Warenkorb-Abbruch vor weniger als 1 Tag<br><br>Zeitzone:<br>Zeitzone des Unternehmens"
    tags:
      - Custom events
  - name: X Custom Event In Y Days
    description: "Bestimmt, ob ein:e Nutzer:in ein speziell aufgezeichnetes Event zwischen 0 und 50 Mal in der letzten angegebenen Anzahl von Kalendertagen zwischen 1 und 30 ausgeführt hat. (Kalendertag = 1 Kalendertag betrachtet 24–48 Stunden der Nutzerhistorie)<br> <a href=\"/docs/x-in-y-behavior\"> Mehr über das X-in-Y-Verhalten erfahren.</a> <br><br>Beispiel:<br>Warenkorb-Abbruch genau 0 Mal im letzten 1 Kalendertag<br><br>Zeitzone:<br>UTC – Um alle Zeitzonen zu berücksichtigen, betrachtet 1 Kalendertag 24–48 Stunden der Nutzerhistorie, abhängig vom Zeitpunkt der Segment-Auswertung; bei 2 Kalendertagen werden 48–72 Stunden der Nutzerhistorie betrachtet, und so weiter."
    tags:
      - Custom events
  - name: X Custom Event Property In Y Days
    description: "Bestimmt, ob ein:e Nutzer:in ein speziell aufgezeichnetes Event in Bezug auf eine bestimmte Eigenschaft zwischen 0 und 50 Mal in der letzten angegebenen Anzahl von Kalendertagen zwischen 1 und 30 ausgeführt hat. (Kalendertag = 1 Kalendertag betrachtet 24–48 Stunden der Nutzerhistorie)<br><a href=\"/docs/x-in-y-behavior\">Mehr über das X-in-Y-Verhalten erfahren.</a> <br><br>Beispiel:<br> Zu Favoriten hinzugefügt mit Eigenschaft „event_name“ genau 0 Mal im letzten 1 Kalendertag<br><br>Zeitzone:<br>UTC – Um alle Zeitzonen zu berücksichtigen, betrachtet 1 Kalendertag 24–48 Stunden der Nutzerhistorie, abhängig vom Zeitpunkt der Segment-Auswertung; bei 2 Kalendertagen werden 48–72 Stunden der Nutzerhistorie betrachtet, und so weiter."
    tags:
      - Custom events
  - name: Email Address
    description: "Ermöglicht es Ihnen, Ihre Kampagnenempfänger:innen anhand einzelner E-Mail-Adressen für Tests zu bestimmen. Dies kann auch verwendet werden, um Transaktions-E-Mails an alle Ihre Nutzer:innen (einschließlich abgemeldeter) zu senden, indem Sie den Spezifizierer „E-Mail-Adresse ist nicht leer“ im Filter verwenden, sodass Sie die Zustellung von E-Mails unabhängig vom Opt-in-Status maximieren können. <br><br>Dieser Filter prüft nur, ob Nutzerprofile eine E-Mail-Adresse haben, während der Filter <a href=\"/docs/user_guide/audience/segments/segmentation_filters#email-available\">E-Mail verfügbar</a> zusätzliche Kriterien prüft."
    tags:
      - Other Filters
  - name: External User ID
    description: "Ermöglicht es Ihnen, Ihre Kampagnenempfänger:innen anhand einzelner Nutzer-IDs für Tests zu bestimmen."
    tags:
      - Other Filters
  - name: "Random Bucket #"
    description: "Segmentiert Ihre Nutzer:innen anhand einer zufällig zugewiesenen Nummer (0 bis 9999 einschließlich). Ermöglicht die Erstellung gleichmäßig verteilter Segmente aus wirklich zufälligen Nutzer:innen für A/B- und multivariate Tests."
    tags:
      - Other Filters
  - name: Session Count
    description: "Segmentiert Ihre Nutzer:innen nach der Anzahl der Sitzungen, die sie in einer Ihrer Apps innerhalb Ihres Workspace hatten."
    tags:
      - Sessions
  - name: Session Count For App
    description: "Segmentiert Ihre Nutzer:innen nach der Anzahl der Sitzungen, die sie in einer bestimmten, festgelegten App hatten."
    tags:
      - Sessions
  - name: X Sessions In Last Y Days
    description: "Segmentiert Ihre Nutzer:innen nach der Anzahl der Sitzungen (zwischen 0 und 50), die sie in Ihrer App in der letzten angegebenen Anzahl von Kalendertagen zwischen 1 und 30 hatten. <br> <a href=\"/docs/x-in-y-behavior\">Mehr über das X-in-Y-Verhalten erfahren.</a>"
    tags:
      - Sessions
  - name: First Used App
    description: "Segmentiert Ihre Nutzer:innen nach dem frühesten aufgezeichneten Zeitpunkt, zu dem sie Ihre App geöffnet haben. <em>Dies erfasst die erste Sitzung mit einer Version Ihrer App, in die das Braze SDK or Software-Development-Kit integriert ist.</em> Der maximale Rückblickzeitraum beträgt 100 Jahre. (24-Stunden-Zeitraum)<br><br>Zeitzone:<br>Zeitzone des Unternehmens"
    tags:
      - Sessions
  - name: First Used Specific App
    description: "Segmentiert Ihre Nutzer:innen nach dem frühesten aufgezeichneten Zeitpunkt, zu dem sie eine Ihrer Apps innerhalb Ihres Workspace geöffnet haben. Der maximale Rückblickzeitraum beträgt 100 Jahre. (24-Stunden-Zeitraum)<br><br>Zeitzone:<br>Zeitzone des Unternehmens"
    tags:
      - Sessions
  - name: Last Used App
    description: "Segmentiert Ihre Nutzer:innen nach dem letzten Zeitpunkt, zu dem sie Ihre App geöffnet haben. Der maximale Rückblickzeitraum beträgt 100 Jahre. (24-Stunden-Zeitraum)<br><br>Zeitzone:<br>Zeitzone des Unternehmens"
    tags:
      - Sessions
  - name: Last Used Specific App
    description: "Segmentiert Ihre Nutzer:innen nach dem letzten Zeitpunkt, zu dem sie eine bestimmte, festgelegte App geöffnet haben. Der maximale Rückblickzeitraum beträgt 100 Jahre. (24-Stunden-Zeitraum)<br><br>Zeitzone:<br>Zeitzone des Unternehmens"
    tags:
      - Sessions
  - name: Median Session Duration
    description: "Segmentiert Ihre Nutzer:innen nach der medianen Länge ihrer Sitzungen in Ihrer App."
    tags:
      - Sessions
  - name: Received Message from Campaign
    description: "Segmentiert Ihre Nutzer:innen danach, ob sie eine bestimmte Campaign erhalten haben. <br><br>Für Content Cards, Banner und In-App-Nachrichten gilt dies, wenn ein:e Nutzer:in eine Impression protokolliert, nicht wenn die Card oder In-App-Nachricht gesendet wird.<br><br> Für Push und Webhooks gilt dies, wenn die Nachricht an den/die Nutzer:in gesendet wird.<br><br> Für WhatsApp gilt dies, wenn die letzte Nachrichten-API-Anfrage an WhatsApp gesendet wird, nicht wenn die Nachricht auf dem Gerät des/der Nutzer:in zugestellt wird.<br><br> Für E-Mails entspricht das Zielprofil diesem Filter, wenn eine E-Mail-Anfrage an den E-Mail-Anbieter gesendet wird (unabhängig davon, ob sie tatsächlich zugestellt wird).<br><br> Für Kurzmitteilungsdienst or SMS und RCS gelten Nutzer:innen als „empfangen“ zum Sendezeitpunkt. Selbst wenn die Nachricht das Gerät des/der Nutzer:in nicht erreicht, entspricht der/die Nutzer:in diesem Filter.<br><br> Wenn eine Nachricht zugestellt, geöffnet oder angeklickt wird, aktualisiert Braze die Daten für alle Profile, die denselben Kanalbezeichner teilen (z. B. E-Mail oder Telefonnummer), sodass Nutzer:innen, die einen Bezeichner mit jemandem teilen, der die Nachricht erhalten hat, diesem Filter entsprechen können, auch wenn ihr Profil die Campaign nicht direkt erhalten hat."
    tags:
      - Retargeting
  - name: Received Campaign Variant
    description: "Segmentiert Ihre Nutzer:innen danach, welche Variante einer multivariaten Campaign sie erhalten haben.<br><br>Dieser Filter gilt für multivariate und multivariate Quick-Push-Campaigns. API-Campaigns, standardmäßige Multichannel-Campaigns und Feature-Flag-Experiment-Campaigns erscheinen nicht in der Campaign-Auswahl. Reine Webhook-Campaigns erscheinen nicht in der Campaign-Auswahl.<br><br>Für Content Cards, Banner und In-App-Nachrichten gilt dies, wenn ein:e Nutzer:in eine Impression protokolliert, nicht wenn die Card oder In-App-Nachricht gesendet wird.<br><br> Für Push und Webhooks gilt dies, wenn die Nachricht an den/die Nutzer:in gesendet wird.<br><br> Für WhatsApp gilt dies, wenn die letzte Nachrichten-API-Anfrage an WhatsApp gesendet wird, nicht wenn die Nachricht auf dem Gerät des/der Nutzer:in zugestellt wird.<br><br> Für E-Mails entspricht das Zielprofil diesem Filter, wenn eine E-Mail-Anfrage an den E-Mail-Anbieter gesendet wird (unabhängig davon, ob sie tatsächlich zugestellt wird).<br><br> Für Kurzmitteilungsdienst or SMS und RCS gelten Nutzer:innen als „empfangen“ zum Sendezeitpunkt. Selbst wenn die Nachricht das Gerät des/der Nutzer:in nicht erreicht, entspricht der/die Nutzer:in diesem Filter.<br><br> Wenn eine Nachricht zugestellt, geöffnet oder angeklickt wird, aktualisiert Braze die Daten für alle Profile, die denselben Kanalbezeichner teilen (z. B. E-Mail oder Telefonnummer), sodass Nutzer:innen, die einen Bezeichner mit jemandem teilen, der die Nachricht erhalten hat, diesem Filter entsprechen können, auch wenn ihr Profil die Campaign nicht direkt erhalten hat."
    tags:
      - Retargeting
  - name: Received Message from Canvas Step
    description: "Segmentiert Ihre Nutzer:innen danach, ob sie eine bestimmte Canvas-Komponente erhalten haben.<br><br>Für Content Cards und In-App-Nachrichten gilt dies, wenn ein:e Nutzer:in eine Impression protokolliert, nicht wenn die Card oder In-App-Nachricht gesendet wird.<br><br> Für Push und Webhooks gilt dies, wenn die Nachricht an den/die Nutzer:in gesendet wird.<br><br> Für WhatsApp gilt dies, wenn die letzte Nachrichten-API-Anfrage an WhatsApp gesendet wird, nicht wenn die Nachricht auf dem Gerät des/der Nutzer:in zugestellt wird.<br><br> Für E-Mails entspricht das Zielprofil diesem Filter, wenn eine E-Mail-Anfrage an den E-Mail-Anbieter gesendet wird (unabhängig davon, ob sie tatsächlich zugestellt wird).<br><br> Für Kurzmitteilungsdienst or SMS und RCS gelten Nutzer:innen als „empfangen“ zum Sendezeitpunkt. Selbst wenn die Nachricht das Gerät des/der Nutzer:in nicht erreicht, entspricht der/die Nutzer:in diesem Filter.<br><br> Wenn eine Nachricht zugestellt, geöffnet oder angeklickt wird, aktualisiert Braze die Daten für alle Profile, die denselben Kanalbezeichner teilen (z. B. E-Mail oder Telefonnummer), sodass Nutzer:innen, die einen Bezeichner mit jemandem teilen, der die Nachricht erhalten hat, diesem Filter entsprechen können, auch wenn ihr Profil die Campaign nicht direkt erhalten hat."
    tags:
      - Retargeting
  - name: Last Received Message from Specific Canvas Step
    description: "Segmentiert Ihre Nutzer:innen danach, wann sie eine bestimmte Canvas-Komponente erhalten haben. Der maximale Rückblickzeitraum beträgt 100 Jahre.<br><br> Da die Daten für alle Profile aktualisiert werden, die denselben Kanalbezeichner teilen (z. B. E-Mail oder Telefonnummer), wenn eine Zustellung, ein Öffnen oder ein Klick erfolgt, kann ein:e Nutzer:in, der/die einen Bezeichner mit jemandem teilt, der eine Nachricht erhalten hat, diesem Filter möglicherweise nicht entsprechen, auch wenn ihm/ihr die Nachricht nie explizit gesendet wurde. Verwenden Sie „Entered Canvas Variation“, um Nutzerprofile von Duplikaten zu isolieren.<br><br> Dieser Filter berücksichtigt nicht, wann Nutzer:innen andere Canvas-Komponenten erhalten haben."
    tags:
      - Retargeting
  - name: Last Received Message from Specific Campaign
    description: "Segmentiert Ihre Nutzer:innen danach, ob sie eine bestimmte Campaign erhalten haben. Der maximale Rückblickzeitraum beträgt 100 Jahre.<br><br> Da die Daten für alle Profile aktualisiert werden, die denselben Kanalbezeichner teilen (z. B. E-Mail oder Telefonnummer), wenn eine Zustellung, ein Öffnen oder ein Klick erfolgt, kann ein:e Nutzer:in, der/die einen Bezeichner mit jemandem teilt, der eine Nachricht erhalten hat, diesem Filter möglicherweise nicht entsprechen, auch wenn ihm/ihr die Nachricht nie explizit gesendet wurde.<br><br> Dieser Filter berücksichtigt nicht, wann Nutzer:innen andere Campaigns erhalten haben."
    tags:
      - Retargeting
  - name: Received Message from Campaign or Canvas with Tag
    description: "Segmentiert Ihre Nutzer:innen danach, ob sie eine bestimmte Campaign oder ein bestimmtes Canvas mit einem bestimmten Tag erhalten haben.<br><br>Braze wertet nur die letzten 200 gesendeten Campaigns und Canvase aus, die den ausgewählten Tag verwenden, wenn dieser Filter ausgeführt wird.<br><br> Für Content Cards, Banner (nur Campaigns) und In-App-Nachrichten gilt dies, wenn ein:e Nutzer:in eine Impression protokolliert, nicht wenn die Card oder In-App-Nachricht gesendet wird.<br><br> Für Push und Webhooks gilt dies, wenn die Nachricht an den/die Nutzer:in gesendet wird.<br><br> Für WhatsApp gilt dies, wenn die letzte Nachrichten-API-Anfrage an WhatsApp gesendet wird, nicht wenn die Nachricht auf dem Gerät des/der Nutzer:in zugestellt wird.<br><br> Für E-Mails entspricht das Zielprofil diesem Filter, wenn eine E-Mail-Anfrage an den E-Mail-Anbieter gesendet wird (unabhängig davon, ob sie tatsächlich zugestellt wird).<br><br> Für Kurzmitteilungsdienst or SMS und RCS gelten Nutzer:innen als „empfangen“ zum Sendezeitpunkt. Selbst wenn die Nachricht das Gerät des/der Nutzer:in nicht erreicht, entspricht der/die Nutzer:in diesem Filter.<br><br> Wenn eine Nachricht zugestellt, geöffnet oder angeklickt wird, aktualisiert Braze die Daten für alle Profile, die denselben Kanalbezeichner teilen (z. B. E-Mail oder Telefonnummer), sodass Nutzer:innen, die einen Bezeichner mit jemandem teilen, der die Nachricht erhalten hat, diesem Filter entsprechen können, auch wenn ihr Profil die Campaign nicht direkt erhalten hat."
    tags:
      - Retargeting
  - name: Last Received Message from Campaign or Canvas With Tag
    description: "Segmentiert Ihre Nutzer:innen danach, wann sie eine bestimmte Campaign oder ein bestimmtes Canvas mit einem bestimmten Tag erhalten haben. Dieser Filter berücksichtigt nicht, wann Nutzer:innen andere Campaigns oder Canvase erhalten haben. Der maximale Rückblickzeitraum beträgt 100 Jahre. (24-Stunden-Zeitraum)"
    tags:
      - Retargeting
  - name: Has Never Received a Message from Campaign or Canvas Step
    description: "Segmentiert Ihre Nutzer:innen danach, ob sie jemals eine Campaign oder Canvas-Komponente erhalten haben."
    tags:
      - Retargeting
  - name: Last Received Email
    description: "Segmentiert Ihre Nutzer:innen nach dem letzten Zeitpunkt, zu dem sie eine Ihrer E-Mail-Nachrichten erhalten haben. Der maximale Rückblickzeitraum beträgt 100 Jahre. (24-Stunden-Zeitraum)<br><br>Zeitzone:<br>Zeitzone des Unternehmens"
    tags:
      - Retargeting
  - name: Last Received Push
    description: "Segmentiert Ihre Nutzer:innen nach dem letzten Zeitpunkt, zu dem sie eine Ihrer Push-Benachrichtigungen erhalten haben. Der maximale Rückblickzeitraum beträgt 100 Jahre. (24-Stunden-Zeitraum)<br><br>Zeitzone:<br>Zeitzone des Unternehmens"
    tags:
      - Retargeting
  - name: Last In App Message Impression
    description: "Segmentiert Ihre Nutzer:innen nach dem letzten Zeitpunkt, zu dem sie eine In-App-Nachricht angesehen haben. Der maximale Rückblickzeitraum beträgt 100 Jahre."
    tags:
      - Retargeting
  - name: Last Received SMS
    description: "Segmentiert Ihre Nutzer:innen nach dem Zeitpunkt, zu dem die letzte Kurzmitteilungsdienst or SMS-, MMS- oder RCS-Nachricht an den Kurzmitteilungsdienst or SMS- oder RCS-Anbieter zugestellt wurde. Dies garantiert nicht, dass die Nachricht auf dem Gerät des/der Nutzer:in zugestellt wurde. Der maximale Rückblickzeitraum beträgt 100 Jahre. (24-Stunden-Zeitraum)<br><br>Zeitzone:<br>Zeitzone des Unternehmens"
    tags:
      - Retargeting
  - name: Last Received Webhook
    description: "Segmentiert Ihre Nutzer:innen nach dem letzten Zeitpunkt, zu dem Braze einen Webhook für diese:n Nutzer:in gesendet hat. Der maximale Rückblickzeitraum beträgt 100 Jahre. (24-Stunden-Zeitraum)<br><br>Zeitzone:<br>Zeitzone des Unternehmens"
    tags:
      - Retargeting
  - name: Last Received WhatsApp
    description: "Segmentiert Ihre Nutzer:innen nach dem letzten Zeitpunkt, zu dem sie eine WhatsApp-Nachricht erhalten haben. Dies ist der Zeitpunkt, zu dem die letzte Nachrichten-API-Anfrage an WhatsApp gesendet wird, nicht wenn die Nachricht auf dem Gerät des/der Nutzer:in zugestellt wird. Der maximale Rückblickzeitraum beträgt 100 Jahre. (24-Stunden-Zeitraum)<br><br>Zeitzone:<br>Zeitzone des Unternehmens"
    tags:
      - Retargeting
  - name: Live Activities Push to Start Registered for App
    description: "Segmentiert Ihre Nutzer:innen danach, ob sie für den Start einer Live Activity über iOS-Push-Benachrichtigungen für eine bestimmte App registriert sind."
    tags:
      - Devices
  - name: Clicked/Opened Campaign
    description: "Filtert nach Interaktion mit einer bestimmten Campaign. Bei In-App-Nachrichten umfassen angeklickte In-App-Nachrichten Body- und Button-Klicks. Schließ- und Dismiss-Aktionen oder das Schließen der Nachricht mit dem X werden nicht gezählt.<br><br>Bei E-Mails umfasst das Öffnen-Event sowohl maschinelle als auch nicht-maschinelle Öffnungen. Dieser Filter bietet auch die Option, nach „beliebige E-Mail geöffnet (maschinelle Öffnungen)“ und „beliebige E-Mail geöffnet (andere Öffnungen)“ zu filtern. Klicks auf Abmeldelinks und Präferenzzentren werden bei diesem Filter nicht berücksichtigt. Wenn mehrere Nutzer:innen dieselbe E-Mail-Adresse teilen:<br>- Wenn die E-Mail geöffnet oder angeklickt wird, werden auch die Profile aller anderen Nutzer:innen mit derselben E-Mail-Adresse aktualisiert. <br>- Wenn der/die ursprüngliche Nutzer:in die E-Mail-Adresse nach dem Senden der Nachricht und vor dem Öffnen oder Klicken ändert, wird das Öffnen oder der Klick auf alle verbleibenden Nutzer:innen mit dieser E-Mail-Adresse anstatt auf den/die ursprüngliche:n Nutzer:in angewendet.<br><br>Für Kurzmitteilungsdienst or SMS und RCS wird eine Interaktion definiert als:<br>- Der/die Nutzer:in hat zuletzt eine Antwort-Kurzmitteilungsdienst or SMS oder -RCS gesendet, die einer bestimmten Keyword-Kategorie entspricht. Dies wird der zuletzt empfangenen Campaign aller Nutzer:innen mit dieser Telefonnummer zugeordnet. Die Campaign muss in den letzten vier Stunden empfangen worden sein.<br>- Der/die Nutzer:in hat zuletzt einen verkürzten Link in einer Kurzmitteilungsdienst or SMS- oder RCS-Nachricht mit aktiviertem Nutzer-Klick-Tracking aus einer bestimmten Campaign ausgewählt."
    tags:
      - Retargeting
  - name: Clicked/Opened Campaign or Canvas With Tag
    description: "Filtert nach Interaktion mit einer bestimmten Campaign, die einen bestimmten Tag hat. Bei In-App-Nachrichten umfassen angeklickte In-App-Nachrichten Body- und Button-Klicks. Schließ- und Dismiss-Aktionen oder das Schließen der Nachricht mit dem X werden nicht gezählt.<br><br>Bei E-Mails umfasst das Öffnen-Event sowohl maschinelle als auch nicht-maschinelle Öffnungen. Dieser Filter bietet auch die Option, nach „beliebige E-Mail geöffnet (maschinelle Öffnungen)“ und „beliebige E-Mail geöffnet (andere Öffnungen)“ zu filtern. Wenn mehrere Nutzer:innen dieselbe E-Mail-Adresse teilen:<br>- Wenn die E-Mail geöffnet oder angeklickt wird, werden auch die Profile aller anderen Nutzer:innen mit derselben E-Mail-Adresse aktualisiert. <br>- Wenn der/die ursprüngliche Nutzer:in die E-Mail-Adresse nach dem Senden der Nachricht und vor dem Öffnen oder Klicken ändert, wird das Öffnen oder der Klick auf alle verbleibenden Nutzer:innen mit dieser E-Mail-Adresse anstatt auf den/die ursprüngliche:n Nutzer:in angewendet.<br><br>Für Kurzmitteilungsdienst or SMS und RCS wird eine Interaktion definiert als:<br>- Der/die Nutzer:in hat zuletzt eine Antwort-Kurzmitteilungsdienst or SMS oder -RCS gesendet, die einer bestimmten Keyword-Kategorie entspricht. Dies wird der zuletzt empfangenen Campaign aller Nutzer:innen mit dieser Telefonnummer zugeordnet. Die Campaign muss in den letzten vier Stunden empfangen worden sein.<br>- Der/die Nutzer:in hat zuletzt einen verkürzten Link in einer Kurzmitteilungsdienst or SMS- oder RCS-Nachricht mit aktiviertem Nutzer-Klick-Tracking aus einer bestimmten Campaign oder einem Canvas-Schritt mit Tag ausgewählt."
    tags:
      - Retargeting
  - name: Clicked/Opened Step
    description: "Filtert nach Interaktion mit einer bestimmten Canvas-Komponente. Bei In-App-Nachrichten umfassen angeklickte In-App-Nachrichten auch Body- und Button-Klicks. Schließ- und Dismiss-Aktionen oder das Schließen der Nachricht mit dem X werden nicht gezählt.<br><br>Bei E-Mails umfasst das Öffnen-Event sowohl maschinelle als auch nicht-maschinelle Öffnungen. Dieser Filter bietet auch die Option, nach „beliebige E-Mail geöffnet (maschinelle Öffnungen)“ und „beliebige E-Mail geöffnet (andere Öffnungen)“ zu filtern.<br><br>Für Kurzmitteilungsdienst or SMS und RCS wird eine Interaktion definiert als:<br>- Der/die Nutzer:in hat zuletzt eine Antwort-Kurzmitteilungsdienst or SMS oder -RCS gesendet, die einer bestimmten Keyword-Kategorie entspricht. Dies wird der zuletzt empfangenen Campaign aller Nutzer:innen mit dieser Telefonnummer zugeordnet. Die Campaign muss in den letzten vier Stunden empfangen worden sein. <br>- Der/die Nutzer:in hat zuletzt einen verkürzten Link in einer Kurzmitteilungsdienst or SMS- oder RCS-Nachricht mit aktiviertem Nutzer-Klick-Tracking aus einem bestimmten Canvas-Schritt ausgewählt."
    tags:
      - Retargeting
  - name: Clicked Alias in Campaign
    description: "Filtert Ihre Nutzer:innen danach, ob sie einen bestimmten Alias in einer bestimmten Campaign angeklickt haben. Dies gilt nur für E-Mail-Nachrichten. <br><br> Wenn mehrere Nutzer:innen dieselbe E-Mail-Adresse teilen:<br>- Wenn die E-Mail geöffnet oder angeklickt wird, werden auch die Profile aller anderen Nutzer:innen mit derselben E-Mail-Adresse aktualisiert. <br>- Wenn der/die ursprüngliche Nutzer:in die E-Mail-Adresse nach dem Senden der Nachricht und vor dem Öffnen oder Klicken ändert, wird das Öffnen oder der Klick auf alle verbleibenden Nutzer:innen mit dieser E-Mail-Adresse anstatt auf den/die ursprüngliche:n Nutzer:in angewendet."
    tags:
      - Retargeting
  - name: Clicked Alias in Canvas Step
    description: "Filtert Ihre Nutzer:innen danach, ob sie einen bestimmten Alias in einem bestimmten Canvas angeklickt haben. Dies gilt nur für E-Mail-Nachrichten. <br><br> Wenn mehrere Nutzer:innen dieselbe E-Mail-Adresse teilen:<br>- Wenn die E-Mail geöffnet oder angeklickt wird, werden auch die Profile aller anderen Nutzer:innen mit derselben E-Mail-Adresse aktualisiert. <br>- Wenn der/die ursprüngliche Nutzer:in die E-Mail-Adresse nach dem Senden der Nachricht und vor dem Öffnen oder Klicken ändert, wird das Öffnen oder der Klick auf alle verbleibenden Nutzer:innen mit dieser E-Mail-Adresse anstatt auf den/die ursprüngliche:n Nutzer:in angewendet."
    tags:
      - Retargeting
  - name: Clicked Alias in Any Campaign or Canvas Step
    description: "Filtert Ihre Nutzer:innen danach, ob sie einen bestimmten Alias in einer beliebigen Campaign oder einem Canvas angeklickt haben. Dies gilt nur für E-Mail-Nachrichten. <br><br> Wenn mehrere Nutzer:innen dieselbe E-Mail-Adresse teilen:<br>- Wenn die E-Mail geöffnet oder angeklickt wird, werden auch die Profile aller anderen Nutzer:innen mit derselben E-Mail-Adresse aktualisiert. <br>- Wenn der/die ursprüngliche Nutzer:in die E-Mail-Adresse nach dem Senden der Nachricht und vor dem Öffnen oder Klicken ändert, wird das Öffnen oder der Klick auf alle verbleibenden Nutzer:innen mit dieser E-Mail-Adresse anstatt auf den/die ursprüngliche:n Nutzer:in angewendet."
    tags:
      - Retargeting
  - name: Hard Bounced
    description: "Segmentiert Ihre Nutzer:innen danach, ob ihre E-Mail-Adresse einen Hard Bounce verursacht hat (z. B. die E-Mail-Adresse ist ungültig). Um Nutzer:innen mit ungültigen E-Mails zu exportieren, rufen Sie den Endpunkt <a href=\"/docs/api/endpoints/email/get_list_hard_bounces/\"><code>/email/hard_bounces</code></a> auf oder erstellen Sie ein Segment mit Filtern wie „E-Mail-Adresse ist nicht leer“, „E-Mail ist nicht verfügbar“ und „E-Mail-Abo-Status ist nicht abgemeldet“."
    tags:
      - Retargeting
  - name: Soft Bounced
    description: "Segmentiert Ihre Nutzer:innen danach, ob sie X Mal in Y Tagen einen Soft Bounce hatten. Segmentfilter können nur 30 Tage zurückblicken, aber mit Segmenterweiterungen können Sie weiter zurückblicken.<br><br>Dieser Filter funktioniert anders als ein Soft-Bounce-Event in Currents. Der Soft-Bounce-Segmentfilter zählt einen Soft Bounce, wenn es während des 72-Stunden-Wiederholungszeitraums keine erfolgreiche Zustellung gab. In Currents wird jeder erfolglose Wiederholungsversuch als Soft-Bounce-Event gesendet."
    tags:
      - Retargeting
  - name: Has Marked You As Spam
    description: "Segmentiert Ihre Nutzer:innen danach, ob sie Ihre Nachrichten als Spam markiert haben."
    tags:
      - Retargeting
  - name: Invalid Phone Number
    description: "Segmentiert Ihre Nutzer:innen danach, ob ihre Telefonnummer ungültig ist."
    tags:
      - Retargeting
  - name: Last Sent Specific SMS Inbound Keyword Category
    description: "Segmentiert Ihre Nutzer:innen danach, wann sie zuletzt eine Kurzmitteilungsdienst or SMS, MMS oder RCS an eine bestimmte Abo-Gruppe innerhalb einer bestimmten Keyword-Kategorie gesendet haben. Der maximale Rückblickzeitraum beträgt 100 Jahre."
    tags:
      - Retargeting
  - name: Converted From Campaign
    description: "Segmentiert Ihre Nutzer:innen danach, ob sie bei einer bestimmten Campaign konvertiert haben. Dieser Filter schließt Nutzer:innen in der Kontrollgruppe nicht ein."
    tags:
      - Retargeting
  - name: Converted From Canvas
    description: "Segmentiert Ihre Nutzer:innen danach, ob sie bei einem bestimmten Canvas konvertiert haben. Dieser Filter schließt Nutzer:innen in der Kontrollgruppe nicht ein."
    tags:
      - Retargeting
  - name: In Campaign Control Group
    description: "Segmentiert Ihre Nutzer:innen danach, ob sie in der Kontrollgruppe einer bestimmten multivariaten Campaign waren."
    tags:
      - Retargeting
  - name: In Canvas Control Group
    description: "Segmentiert Ihre Nutzer:innen danach, ob sie in der Kontrollgruppe eines bestimmten Canvas waren. Dieser Filter wertet nur Nutzer:innen aus, die das Canvas betreten haben, sodass Nutzer:innen, die nie eingetreten sind, vollständig aus den Ergebnissen ausgeschlossen werden.<br><br>Wenn Sie beispielsweise nach Nutzer:innen filtern, die nicht in der Kontrollgruppe eines Canvas sind, erhalten Sie nur Nutzer:innen, die das Canvas betreten haben und einer Nicht-Kontroll-Variante zugewiesen wurden – Nutzer:innen, die das Canvas nie betreten haben, sind nicht enthalten. Um alle Nutzer:innen unabhängig vom Canvas-Eintritt einzuschließen, verwenden Sie stattdessen den Filter <code>Entered Canvas Variation</code>."
    tags:
      - Retargeting
  - name: Last Enrolled in Any Control Group
    description: "Segmentiert Ihre Nutzer:innen nach dem letzten Zeitpunkt, zu dem sie in die Kontrollgruppe einer Campaign aufgenommen wurden. Der maximale Rückblickzeitraum beträgt 100 Jahre. <br><br>Zeitzone:<br>Zeitzone des Unternehmens"
    tags:
      - Retargeting
  - name: Entered Canvas Variation
    description: "Segmentiert Ihre Nutzer:innen danach, ob sie einen Variationspfad eines bestimmten Canvas betreten haben. Dieser Filter wertet alle Nutzer:innen aus.<br><br>Wenn Sie beispielsweise nach Nutzer:innen filtern, die keine Canvas-Varianten-Kontrollgruppe betreten haben, erhalten Sie alle Nutzer:innen, die nicht in der Kontrollgruppe sind, unabhängig davon, ob sie das Canvas betreten haben."
    tags:
      - Retargeting
  - name: Last Received Any Message
    description: "Segmentiert Ihre Nutzer:innen, indem die letzte empfangene Nachricht bestimmt wird. Der maximale Rückblickzeitraum beträgt 100 Jahre. (24-Stunden-Zeitraum)<br><br>Für Content Cards, Banner und In-App-Nachrichten gilt dies, wenn ein:e Nutzer:in zuletzt eine Impression protokolliert hat, nicht wenn die Card oder In-App-Nachricht zuletzt gesendet wurde.<br><br>Für Push und Webhooks gilt dies, wenn eine beliebige Nachricht an den/die Nutzer:in gesendet wurde.<br><br> Für WhatsApp gilt dies, wenn die letzte Nachrichten-API-Anfrage an WhatsApp gesendet wurde, nicht wenn die Nachricht auf dem Gerät des/der Nutzer:in zugestellt wurde.<br><br> Für E-Mails entspricht das Zielprofil diesem Filter, wenn eine E-Mail-Anfrage an den E-Mail-Anbieter gesendet wird (unabhängig davon, ob sie tatsächlich zugestellt wird).<br><br> Für Kurzmitteilungsdienst or SMS und RCS gelten Nutzer:innen als „empfangen“ zum Sendezeitpunkt. Selbst wenn die Nachricht das Gerät des/der Nutzer:in nicht erreicht, entspricht der/die Nutzer:in diesem Filter.<br><br> Wenn eine Nachricht zugestellt, geöffnet oder angeklickt wird, aktualisiert Braze die Daten für alle Profile, die denselben Kanalbezeichner teilen (z. B. E-Mail oder Telefonnummer), sodass Nutzer:innen, die einen Bezeichner mit jemandem teilen, der die Nachricht erhalten hat, diesem Filter entsprechen können, auch wenn ihr Profil die Campaign nicht direkt erhalten hat.<br><br>Beispiel:<br>Letzte Nachricht erhalten vor weniger als 1 Tag = vor weniger als 24 Stunden<br><br>Zeitzone:<br>Zeitzone des Unternehmens"
    tags:
      - Retargeting
  - name: Last Engaged With Message
    description: "Segmentiert Ihre Nutzer:innen nach dem letzten Zeitpunkt, zu dem sie auf einen Ihrer Messaging-Kanäle geklickt oder ihn geöffnet haben (Banner, Content Cards, E-Mail, In-App, Kurzmitteilungsdienst or SMS, RCS, Push, WhatsApp).<br><br>Für Content Cards, Banner und In-App-Nachrichten gilt dies, wenn ein:e Nutzer:in eine Impression protokolliert, nicht wenn die Card oder In-App-Nachricht gesendet wird.<br><br> Für Push und Webhooks gilt dies, wenn die Nachricht an den/die Nutzer:in gesendet wird.<br><br> Für WhatsApp gilt dies, wenn die letzte Nachrichten-API-Anfrage an WhatsApp gesendet wird, nicht wenn die Nachricht auf dem Gerät des/der Nutzer:in zugestellt wird.<br><br> Bei E-Mail-Nachrichten umfasst das Öffnen-Event sowohl maschinelle als auch nicht-maschinelle Öffnungen. Der maximale Rückblickzeitraum beträgt 100 Jahre. (24-Stunden-Zeitraum)<br><br>Für E-Mails entspricht das Zielprofil diesem Filter, wenn eine E-Mail-Anfrage an den E-Mail-Anbieter gesendet wird (unabhängig davon, ob sie tatsächlich zugestellt wird). Dies umfasst auch die Option, nach „beliebige E-Mail geöffnet (maschinelle Öffnungen)“ und „beliebige E-Mail geöffnet (andere Öffnungen)“ zu filtern.<br><br> Für Kurzmitteilungsdienst or SMS und RCS gilt dies, wenn der/die Nutzer:in zuletzt einen verkürzten Link in einer Nachricht mit aktiviertem Nutzer-Klick-Tracking ausgewählt hat.<br><br> Wenn eine Nachricht zugestellt, geöffnet oder angeklickt wird, aktualisiert Braze die Daten für alle Profile, die denselben Kanalbezeichner teilen (z. B. E-Mail oder Telefonnummer), sodass Nutzer:innen, die einen Bezeichner mit jemandem teilen, der die Nachricht erhalten hat, diesem Filter entsprechen können, auch wenn ihr Profil die Campaign nicht direkt erhalten hat.<br><br>Zeitzone:<br>Zeitzone des Unternehmens"
    tags:
      - Retargeting
  - name: Clicked card
    description: "Segmentiert Ihre Nutzer:innen danach, ob sie eine bestimmte Content Card angeklickt haben. Dieser Filter ist als Unterfilter von „Campaign angeklickt/geöffnet“, „Campaign oder Canvas mit Tag angeklickt/geöffnet“ und „Schritt angeklickt/geöffnet“ verfügbar."
    tags:
      - Retargeting
  - name: Feature Flags
    description: "Das Segment Ihrer Nutzer:innen, bei denen ein bestimmtes <a href=\"/docs/developer_guide/feature_flags\">Feature-Flag</a> derzeit aktiviert ist."
    tags:
      - Retargeting
  - name: Subscription Group
    description: "Segmentiert Ihre Nutzer:innen nach ihrer Abo-Gruppe für E-Mail, Kurzmitteilungsdienst or SMS, MMS, RCS oder WhatsApp. Archivierte Gruppen werden nicht angezeigt und können nicht verwendet werden."
    tags:
      - Channel subscription behavior
  - name: Email Available
    description: "Segmentiert Ihre Nutzer:innen danach, ob sie eine gültige E-Mail-Adresse haben und ob sie E-Mails abonniert haben oder dafür angemeldet sind. Dieser Filter prüft drei Kriterien&#58; ob der/die Nutzer:in E-Mails abbestellt hat, ob Braze einen Hard Bounce erhalten hat und ob die E-Mail als Spam markiert wurde. Wenn eines dieser Kriterien erfüllt ist oder keine E-Mail für eine:n Nutzer:in existiert, wird der/die Nutzer:in nicht eingeschlossen.<br><br>Nutzer:innen, deren E-Mail-Verfügbarkeit <code>false</code> ist, werden aus der Kampagnenzielgruppe ausgeschlossen und erhalten die E-Mail nicht – selbst wenn Ihre Sendeeinstellungen so konfiguriert sind, dass an alle Nutzer:innen (einschließlich abgemeldeter) gesendet wird.<br><br>Für E-Mails, bei denen der Opt-in-Status relevant ist, verwenden Sie „E-Mail verfügbar“ anstelle von <a href=\"/docs/user_guide/audience/segments/segmentation_filters#email-address\">E-Mail-Adresse</a>. Die zusätzlichen Kriterien helfen Ihnen, Nutzer:innen anzusprechen, die berechtigt sind, E-Mails zu empfangen."
    tags:
      - Channel subscription behavior
  - name: Email Opt In Date
    description: "Segmentiert Ihre Nutzer:innen nach dem Datum, an dem sie sich für E-Mails angemeldet haben. Der maximale Rückblickzeitraum beträgt 100 Jahre."
    tags:
      - Channel subscription behavior
  - name: Email Subscription Status
    description: "Segmentiert Ihre Nutzer:innen nach ihrem Abo-Status für E-Mails."
    tags:
      - Channel subscription behavior
  - name: Email Unsubscribed Date
    description: "Segmentiert Ihre Nutzer:innen nach dem Datum, an dem sie sich von zukünftigen E-Mails abgemeldet haben. Der maximale Rückblickzeitraum beträgt 100 Jahre."
    tags:
      - Channel subscription behavior
  - name: Foreground Push Enabled
    description: "Segmentiert Ihre Nutzer:innen, die eine vorläufige Push-Autorisierung haben oder für Vordergrund-Push aktiviert sind. Konkret umfasst diese Zählung:<br>1. iOS-Nutzer:innen, die vorläufig für Push autorisiert sind. <br>2. Nutzer:innen, die für Vordergrund-Push aktiviert sind und deren Push-Abo-Status nicht „abgemeldet“ ist, für eine Ihrer Apps. Für diese Nutzer:innen umfasst diese Zählung nur Vordergrund-Push.<br><br>„Vordergrund-Push aktiviert“ schließt Nutzer:innen nicht ein, die sich abgemeldet haben. <br><br>Nach der Segmentierung mit diesem Filter können Sie im unteren Bereich, genannt <em>Erreichbare Nutzer:innen</em>, eine Aufschlüsselung sehen, wer in diesem Segment für Android, iOS und Web enthalten ist."
    tags:
      - Channel subscription behavior
  - name: Foreground Push Enabled for App
    description: "Segmentiert danach, ob Nutzer:innen Push für Ihre App auf ihrem Gerät aktiviert haben. Nutzer:innen, die für eine App Vordergrund-Push aktiviert haben. Dies berücksichtigt nicht den Push-Abo-Status. Diese Zählung umfasst Nutzer:innen, die vorläufig Vordergrund- und Hintergrund-Push-Token / Textbaustein autorisiert haben."
    tags:
      - Channel subscription behavior
  - name: Background or Foreground Push Enabled
    description: "Segmentiert danach, ob Nutzer:innen ein Push-Token / Textbaustein haben und sich nicht abgemeldet haben. Nutzer:innen, die für eine Ihrer Apps Hintergrund- oder Vordergrund-Push aktiviert haben."
    tags:
      - Channel subscription behavior
  - name: Push Opt In Date
    description: "Segmentiert Ihre Nutzer:innen nach dem Datum, an dem sie sich für Push angemeldet haben. Der maximale Rückblickzeitraum beträgt 100 Jahre."
    tags:
      - Channel subscription behavior
  - name: Push Subscription Status
    description: "Segmentiert Ihre Nutzer:innen nach ihrem <a href=\"/docs/user_guide/channels/push/push_setup/push_subscription_states\">Abo-Status</a> für Push."
    tags:
      - Channel subscription behavior
  - name: Push Unsubscribed Date
    description: "Segmentiert Ihre Nutzer:innen nach dem Datum, an dem sie sich von zukünftigen Push-Benachrichtigungen abgemeldet haben. Der maximale Rückblickzeitraum beträgt 100 Jahre."
    tags:
      - Channel subscription behavior
  - name: Purchased Product
    description: "Segmentiert Ihre Nutzer:innen nach in Ihrer App gekauften Produkten."
    tags:
      - Purchase behavior
  - name: Total Number of Purchases
    description: "Segmentiert Ihre Nutzer:innen danach, wie viele Käufe sie in Ihrer App getätigt haben."
    tags:
      - Purchase behavior
  - name: X Product Purchased In Y Days
    description: "Filtert Nutzer:innen danach, wie oft ein bestimmtes Produkt gekauft wurde."
    tags:
      - Purchase behavior
  - name: X Purchases in Last Y Days
    description: "Segmentiert Ihre Nutzer:innen nach der Anzahl der Käufe (zwischen 0 und 50), die sie in der letzten angegebenen Anzahl von Kalendertagen zwischen 1 und 30 getätigt haben. <br> <a href=\"/docs/x-in-y-behavior\">Mehr über das X-in-Y-Verhalten erfahren.</a>"
    tags:
      - Purchase behavior
  - name: X Purchase Property In Y Days
    description: "Segmentiert Ihre Nutzer:innen nach der Anzahl der Käufe in Bezug auf eine bestimmte Kaufeigenschaft in der letzten angegebenen Anzahl von Kalendertagen zwischen 1 und 30. <br> <a href=\"/docs/x-in-y-behavior\">Mehr über das X-in-Y-Verhalten erfahren.</a>"
    tags:
      - Purchase behavior
  - name: First Made Purchase
    description: "Segmentiert Ihre Nutzer:innen nach dem frühesten Zeitpunkt, zu dem ein:e Nutzer:in einen Kauf in Ihrer App getätigt hat. Der maximale Rückblickzeitraum beträgt 100 Jahre."
    tags:
      - Purchase behavior
  - name: First Purchase For App
    description: "Segmentiert Ihre Nutzer:innen nach dem frühesten Zeitpunkt, zu dem ein:e Nutzer:in einen Kauf über Ihre App getätigt hat. Der maximale Rückblickzeitraum beträgt 100 Jahre."
    tags:
      - Purchase behavior
  - name: Last Made Purchase
    description: "Filtert Nutzer:innen nach dem letzten Zeitpunkt, zu dem sie einen Kauf getätigt haben. Der maximale Rückblickzeitraum beträgt 100 Jahre."
    tags:
      - Purchase behavior
  - name: Last Purchased Product
    description: "Filtert Nutzer:innen danach, wann sie zuletzt ein bestimmtes Produkt gekauft haben. Der maximale Rückblickzeitraum beträgt 100 Jahre."
    tags:
      - Purchase behavior
  - name: Money Spent
    description: "Segmentiert Ihre Nutzer:innen nach dem Geldbetrag, den sie in Ihrer App ausgegeben haben."
    tags:
      - Purchase behavior
  - name: X Money Spent in Y Days
    description: "Segmentiert Ihre Nutzer:innen nach dem Geldbetrag, den sie in Ihrer App in der letzten angegebenen Anzahl von Kalendertagen zwischen 1 und 30 ausgegeben haben. Dieser Betrag umfasst nur die Summe der letzten 50 Käufe. <br> <a href=\"/docs/x-in-y-behavior\">Mehr über das X-in-Y-Verhalten erfahren.</a>"
    tags:
      - Purchase behavior
  - name: Last order placed (last 730 days)
    description: "Segmentiert Ihre Nutzer:innen danach, wann sie zuletzt eine Bestellung aufgegeben haben, basierend auf dem <a href=\"/docs/user_guide/data/activation/events/recommended_events/ecommerce_events\">empfohlenen E-Commerce-Event</a> für aufgegebene Bestellungen (Workspaces, die keine E-Commerce-Events tracken, haben keine Daten für diesen Filter). Nutzer:innen werden für diesen Filter einmal täglich ausgewertet, und das maximale Rückblickfenster beträgt die letzten 2 Jahre.<br><br>Dieser Filter befindet sich in der Beta-Phase. Kontaktieren Sie Ihren Braze Account Manager:in, wenn Sie diesen Filter verwenden möchten."
    tags:
      - eCommerce
  - name: Total orders count (last 730 days)
    description: "Segmentiert Ihre Nutzer:innen nach der Gesamtanzahl der Bestellungen eines/einer Nutzer:in innerhalb der letzten 2 Jahre, basierend auf dem <a href=\"/docs/user_guide/data/activation/events/recommended_events/ecommerce_events\">empfohlenen E-Commerce-Event</a> für aufgegebene Bestellungen (Workspaces, die keine E-Commerce-Events tracken, haben keine Daten für diesen Filter). Diese Zählung schließt stornierte Bestellungen aus, die mit dem <a href=\"/docs/user_guide/data/activation/events/recommended_events/ecommerce_events\">empfohlenen E-Commerce-Event</a> für stornierte Bestellungen getrackt werden müssen. Nutzer:innen werden für diesen Filter einmal täglich ausgewertet.<br><br>Dieser Filter befindet sich in der Beta-Phase. Kontaktieren Sie Ihren Braze Account Manager:in, wenn Sie diesen Filter verwenden möchten."
    tags:
      - eCommerce
  - name: Total orders count
    description: "Segmentiert Ihre Nutzer:innen nach der Gesamtanzahl der Bestellungen eines/einer Nutzer:in über die gesamte Lifetime, basierend auf dem <a href=\"/docs/user_guide/data/activation/events/recommended_events/ecommerce_events\">empfohlenen E-Commerce-Event</a> für aufgegebene Bestellungen (Workspaces, die keine E-Commerce-Events tracken, haben keine Daten für diesen Filter). Diese Zählung schließt stornierte Bestellungen aus, die mit dem <a href=\"/docs/user_guide/data/activation/events/recommended_events/ecommerce_events\">empfohlenen E-Commerce-Event</a> für stornierte Bestellungen getrackt werden müssen. Nutzer:innen werden für diesen Filter in Echtzeit ausgewertet.<br><br>Dieser Filter befindet sich in der Beta-Phase. Kontaktieren Sie Ihren Braze Account Manager:in, wenn Sie diesen Filter verwenden möchten."
    tags:
      - eCommerce
  - name: Total canceled orders count (last 730 days)
    description: "Segmentiert Ihre Nutzer:innen nach der Gesamtanzahl der Bestellungen, die ein:e Nutzer:in innerhalb der letzten 2 Jahre storniert hat, basierend auf dem <a href=\"/docs/user_guide/data/activation/events/recommended_events/ecommerce_events\">empfohlenen E-Commerce-Event</a> für aufgegebene Bestellungen (Workspaces, die keine E-Commerce-Events tracken, haben keine Daten für diesen Filter). Nutzer:innen werden für diesen Filter einmal täglich ausgewertet.<br><br>Dieser Filter befindet sich in der Beta-Phase. Kontaktieren Sie Ihren Braze Account Manager:in, wenn Sie diesen Filter verwenden möchten."
    tags:
      - eCommerce
  - name: Customer lifetime value (last 730 days)
    description: "Segmentiert Ihre Nutzer:innen nach dem Gesamtumsatz, den ein:e Nutzer:in voraussichtlich über die Kaufhistorie mit Ihrer Marke generieren wird. Die Berechnung berücksichtigt die letzten 730 Tage und nimmt den durchschnittlichen Bestellwert (AOV), multipliziert ihn mit der Gesamtanzahl der aufgegebenen Bestellungen und berücksichtigt dann die aktive Kaufdauer des/der Nutzer:in (die Zeitspanne zwischen der ersten und der letzten Bestellung). Dieser Filter verwendet Daten, die in <a href=\"/docs/user_guide/data/activation/events/recommended_events/ecommerce_events\">empfohlenen E-Commerce-Events</a> getrackt werden (Workspaces, die keine E-Commerce-Events tracken, haben keine Daten für diesen Filter). Nutzer:innen werden für diesen Filter einmal täglich ausgewertet.<br><br>Dieser Filter befindet sich in der Beta-Phase. Kontaktieren Sie Ihren Braze Account Manager:in, wenn Sie diesen Filter verwenden möchten."
    tags:
      - eCommerce
  - name: Total refund value (last 730 days)
    description: "Segmentiert Ihre Nutzer:innen nach dem Wert der Erstattungen, die einem/einer Nutzer:in in den letzten 2 Jahren gewährt wurden, basierend auf dem <a href=\"/docs/user_guide/data/activation/events/recommended_events/ecommerce_events\">empfohlenen E-Commerce-Event</a> für erstattete Bestellungen (Workspaces, die keine E-Commerce-Events tracken, haben keine Daten für diesen Filter). Nutzer:innen werden für diesen Filter einmal täglich ausgewertet.<br><br>Dieser Filter befindet sich in der Beta-Phase. Kontaktieren Sie Ihren Braze Account Manager:in, wenn Sie diesen Filter verwenden möchten."
    tags:
      - eCommerce
  - name: Total refund value
    description: "Segmentiert Ihre Nutzer:innen nach dem Gesamtwert der Erstattungen, die einem/einer Nutzer:in über die gesamte Lifetime gewährt wurden, basierend auf dem <a href=\"/docs/user_guide/data/activation/events/recommended_events/ecommerce_events\">empfohlenen E-Commerce-Event</a> für erstattete Bestellungen (Workspaces, die keine E-Commerce-Events tracken, haben keine Daten für diesen Filter). Nutzer:innen werden für diesen Filter in Echtzeit ausgewertet.<br><br>Dieser Filter befindet sich in der Beta-Phase. Kontaktieren Sie Ihren Braze Account Manager:in, wenn Sie diesen Filter verwenden möchten."
    tags:
      - eCommerce
  - name: Total revenue (last 730 days)
    description: "Segmentiert Ihre Nutzer:innen nach dem Gesamtumsatz aus den Bestellungen eines/einer Nutzer:in in den letzten 2 Jahren, berechnet durch Subtraktion des Umsatzes des <a href=\"/docs/user_guide/data/activation/events/recommended_events/ecommerce_events\">empfohlenen E-Commerce-Events</a> für erstattete Bestellungen vom Umsatz des E-Commerce-Events für aufgegebene Bestellungen (Workspaces, die keine E-Commerce-Events tracken, haben keine Daten für diesen Filter). Nutzer:innen werden für diesen Filter einmal täglich ausgewertet.<br><br>Dieser Filter befindet sich in der Beta-Phase. Kontaktieren Sie Ihren Braze Account Manager:in, wenn Sie diesen Filter verwenden möchten."
    tags:
      - eCommerce
  - name: Total revenue
    description: "Segmentiert Ihre Nutzer:innen nach dem Gesamtumsatz aus den Bestellungen eines/einer Nutzer:in über die gesamte Lifetime, berechnet durch Subtraktion des Umsatzes des <a href=\"/docs/user_guide/data/activation/events/recommended_events/ecommerce_events\">empfohlenen E-Commerce-Events</a> für erstattete Bestellungen vom Umsatz des E-Commerce-Events für aufgegebene Bestellungen (Workspaces, die keine E-Commerce-Events tracken, haben keine Daten für diesen Filter). Nutzer:innen werden für diesen Filter in Echtzeit ausgewertet.<br><br>Dieser Filter befindet sich in der Beta-Phase. Kontaktieren Sie Ihren Braze Account Manager:in, wenn Sie diesen Filter verwenden möchten."
    tags:
      - eCommerce
  - name: Average order value (last 730 days)
    description: "Segmentiert Ihre Nutzer:innen nach dem durchschnittlichen (Mittel-)Wert der Bestellungen eines/einer Nutzer:in in den letzten 2 Jahren, basierend auf dem <a href=\"/docs/user_guide/data/activation/events/recommended_events/ecommerce_events\">empfohlenen E-Commerce-Event</a> für aufgegebene Bestellungen (Workspaces, die keine E-Commerce-Events tracken, haben keine Daten für diesen Filter). Nutzer:innen werden für diesen Filter einmal täglich ausgewertet.<br><br>Dieser Filter befindet sich in der Beta-Phase. Kontaktieren Sie Ihren Braze Account Manager:in, wenn Sie diesen Filter verwenden möchten."
    tags:
      - eCommerce
  - name: Country
    description: "Segmentiert Ihre Nutzer:innen nach ihrem zuletzt angegebenen Standortland."
    tags:
      - Demographic attributes
  - name: City
    description: "Segmentiert Ihre Nutzer:innen nach ihrem zuletzt angegebenen Ort."
    tags:
      - Demographic attributes
  - name: Language
    description: "Segmentiert Ihre Nutzer:innen nach ihrer bevorzugten Sprache."
    tags:
      - Demographic attributes
  - name: Age
    description: "Segmentiert Ihre Nutzer:innen nach ihrem Alter, wie sie es in Ihrer App angegeben haben."
    tags:
      - Demographic attributes
  - name: Birthday
    description: "Segmentiert Ihre Nutzer:innen nach ihrem Geburtstag, wie sie ihn in Ihrer App angegeben haben. <br> Nutzer:innen mit einem Geburtstag am 29. Februar werden in Segmente eingeschlossen, die den 1. März umfassen.<br><br>Um Geburtstage im Dezember oder Januar anzusprechen, fügen Sie die Filterlogik nur innerhalb der 12-Monats-Spanne des Jahres ein, das Sie ansprechen möchten. Fügen Sie also keine Logik ein, die auf den Dezember des vorherigen Kalenderjahres zurückblickt oder auf den Januar des nächsten Jahres vorausblickt. Um beispielsweise Dezember-Geburtstage anzusprechen, können Sie nach „am 31. Dezember“, „vor dem 31. Dezember“ oder „nach dem 30. November“ filtern."
    tags:
      - Demographic attributes
  - name: Gender
    description: "Segmentiert Ihre Nutzer:innen nach Geschlecht, wie sie es in Ihrer App angegeben haben."
    tags:
      - Demographic attributes
  - name: Unformatted Phone Number
    description: "Segmentiert Ihre Nutzer:innen nach ihrer unformatierten Telefonnummer. Enthält keine Klammern, Bindestriche oder andere Symbole."
    tags:
      - Demographic attributes
  - name: First Name
    description: "Segmentiert Ihre Nutzer:innen nach ihrem Vornamen, wie sie ihn in Ihrer App angegeben haben."
    tags:
      - Demographic attributes
  - name: Last Name
    description: "Segmentiert Ihre Nutzer:innen nach ihrem Nachnamen, wie sie ihn in Ihrer App angegeben haben."
    tags:
      - Demographic attributes
  - name: Has App
    description: "Segmentiert danach, ob ein:e Nutzer:in Ihre App jemals installiert hat. Dies umfasst Nutzer:innen, die Ihre App derzeit installiert haben, und solche, die sie in der Vergangenheit deinstalliert haben. In der Regel müssen Nutzer:innen die App öffnen (eine Sitzung starten), um in diesem Filter enthalten zu sein. Es gibt jedoch einige Ausnahmen, z. B. wenn ein:e Nutzer:in in Braze importiert und manuell mit Ihrer App verknüpft wurde."
    tags:
      - App
  - name: Most Recent App Version Name
    description: "Segmentiert nach dem aktuellen Namen der App-Version des/der Nutzer:in.<br><br>Bei Verwendung von „kleiner als“ oder „kleiner als oder gleich“ gibt dieser Filter <code>true</code> zurück, wenn die Haupt-App-Version nicht existiert, da der/die Nutzer:in älter als die App-Version ist. Das bedeutet, dass der/die Nutzer:in automatisch dem Filter entspricht, wenn die letzte Haupt-App-Version nicht existiert."
    tags:
      - App
  - name: Most Recent App Version Number
    description: "Segmentiert nach der aktuellen App-Versionsnummer der App des/der Nutzer:in. Die Versionsnummer in den Klammern wird zum Filtern verwendet, während die vorangestellte Nummer als Referenz dient – z. B. ist bei „3.7.0(134.0.0.0)“ die gefilterte Versionsnummer „134.0.0.0“.<br><br>Bei Verwendung von „kleiner als“ oder „kleiner als oder gleich“ gibt dieser Filter <code>true</code> zurück, wenn die Haupt-App-Version nicht existiert, da der/die Nutzer:in älter als die App-Version ist. Das bedeutet, dass der/die Nutzer:in automatisch dem Filter entspricht, wenn die letzte Haupt-App-Version nicht existiert.<br><br>Es kann einige Zeit dauern, bis die aktuellen App-Versionen befüllt werden. Die App-Version im Kundenprofil or Nutzerprofil wird aktualisiert, wenn die Information vom SDK or Software-Development-Kit erfasst wird, was davon abhängt, wann Nutzer:innen ihre Apps öffnen. Wenn der/die Nutzer:in die App nicht öffnet, wird die aktuelle Version nicht aktualisiert. Diese Filter gelten auch nicht rückwirkend. Es empfiehlt sich, „größer als“ oder „gleich“ für aktuelle und zukünftige Versionen zu verwenden, aber die Verwendung von Filtern für vergangene Versionen kann zu unerwartetem Verhalten führen."
    tags:
      - App
  - name: Uninstalled
    description: "Segmentiert Ihre Nutzer:innen danach, ob sie derzeit im Backend als deinstalliert markiert sind. Nutzer:innen, die die App deinstalliert und später erneut installiert haben, sind nicht enthalten. Dieser Filter spiegelt den aktuellen Deinstallationsstatus wider, nicht ein historisches Protokoll jedes Deinstallations-Events. Der maximale Rückblickzeitraum beträgt 100 Jahre."
    tags:
      - Uninstall
  - name: Device Carrier
    description: "Segmentiert Ihre Nutzer:innen nach ihrem Mobilfunkanbieter."
    tags:
      - Devices
  - name: Device Count
    description: "Segmentiert Ihre Nutzer:innen danach, auf wie vielen Geräten sie Ihre App verwendet haben."
    tags:
      - Devices
  - name: Device Model
    description: "Segmentiert Ihre Nutzer:innen nach der Modellversion ihres Mobiltelefons."
    tags:
      - Devices
  - name: Device OS
    description: "Segmentiert Ihre Nutzer:innen, die ein oder mehrere Geräte mit dem angegebenen Betriebssystem haben. Um Nutzer:innen nach einem Bereich von Betriebssystemen zu segmentieren, verwenden Sie den Filter <a href=\"/docs/user_guide/audience/segments/segmentation_filters#device-os-version-number\">Geräte-Betriebssystem-Versionsnummer</a>."
    tags:
      - Devices
  - name: Device OS Version Number
    description: "Segmentiert Ihre Nutzer:innen, die ein oder mehrere Geräte mit einer Betriebssystemversion innerhalb eines bestimmten Bereichs haben. Sie können beispielsweise Nutzer:innen ansprechen, die eine iOS-Betriebssystemversion haben, die größer oder gleich 26.0 ist."
    tags:
      - Devices
  - name: Most Recent Device Locale
    description: "Segmentiert Ihre Nutzer:innen nach den <a href=\"/docs/user_guide/messaging/messaging_fundamentals/localization\">Locale-Informationen</a> des zuletzt verwendeten Geräts."
    tags:
      - Devices
  - name: Most Recent Watch Model
    description: "Segmentiert Ihre Nutzer:innen nach ihrem neuesten Smartwatch-Modell."
    tags:
      - Devices
  - name: Provisionally Authorized on iOS
    description: "Ermöglicht es Ihnen, Nutzer:innen zu finden, die auf iOS 12 für eine bestimmte App vorläufig autorisiert sind."
    tags:
      - Devices
  - name: Web Browser
    description: "Segmentiert Ihre Nutzer:innen nach dem Webbrowser, den sie für den Zugriff auf Ihre Website verwenden. Dieser Filter gleicht mit jedem Browser in der Gerätehistorie des/der Nutzer:in ab, nicht nur mit dem zuletzt verwendeten Browser."
    tags:
      - Devices
  - name: Device IDFA
    description: "Ermöglicht es Ihnen, Ihre Kampagnenempfänger:innen anhand der IDFA für Tests zu bestimmen."
    tags:
      - Advertising use cases
  - name: Device IDFV
    description: "Ermöglicht es Ihnen, Ihre Kampagnenempfänger:innen anhand der IDFV für Tests zu bestimmen."
    tags:
      - Advertising use cases
  - name: Device Google Ad ID
    description: "Segmentiert Ihre Nutzer:innen nach der Google-Werbe-ID."
    tags:
      - Advertising use cases
  - name: Device Roku Ad ID
    description: "Segmentiert Ihre Nutzer:innen nach der Roku-Werbe-ID."
    tags:
      - Advertising use cases
  - name: Device Windows Ad ID
    description: "Segmentiert Ihre Nutzer:innen nach der Windows-Werbe-ID."
    tags:
      - Advertising use cases
  - name: Ad Tracking Enabled
    description: "Ermöglicht es Ihnen, danach zu filtern, ob Ihre Nutzer:innen dem Werbe-Tracking zugestimmt haben. Werbe-Tracking bezieht sich auf die IDFA oder den „Identifier for Advertisers“, der allen iOS-Geräten von Apple zugewiesen wird und von SDKs gesetzt werden kann. Dieser Bezeichner ermöglicht es Werbetreibenden, Nutzer:innen zu tracken und ihnen gezielte Werbung auszuliefern."
    tags:
      - Advertising use cases
  - name: Most Recent Location
    description: "Segmentiert Ihre Nutzer:innen nach dem zuletzt aufgezeichneten Standort, an dem sie Ihre App verwendet haben."
    tags:
      - Location
  - name: Location Available
    description: "Segmentiert Ihre Nutzer:innen danach, ob sie ihren Standort gemeldet haben. Um diesen Filter zu verwenden, muss Ihre App <a href=\"/docs/search?query=location%20tracking\">Standort-Tracking integriert</a> haben."
    tags:
      - Location
  - name: Amplitude Cohorts
    description: "Kund:innen, die Amplitude verwenden, können ihre Segmente ergänzen, indem sie ihre Kohorten in Amplitude auswählen und importieren."
    tags:
      - Cohort membership
  - name: Census Cohorts
    description: "Kund:innen, die Census verwenden, können ihre Segmente ergänzen, indem sie ihre Kohorten in Census auswählen und importieren."
    tags:
      - Cohort membership
  - name: Heap Cohorts
    description: "Kund:innen, die Heap verwenden, können ihre Segmente ergänzen, indem sie ihre Kohorten in Heap auswählen und importieren."
    tags:
      - Cohort membership
  - name: Hightouch Cohorts
    description: "Kund:innen, die Hightouch verwenden, können ihre Segmente ergänzen, indem sie ihre Kohorten in Hightouch auswählen und importieren."
    tags:
      - Cohort membership
  - name: Kubit Cohorts
    description: "Kund:innen, die Kubit verwenden, können ihre Segmente ergänzen, indem sie ihre Kohorten in Kubit auswählen und importieren."
    tags:
      - Cohort membership
  - name: Mixpanel Cohorts
    description: "Kund:innen, die Mixpanel verwenden, können ihre Segmente ergänzen, indem sie ihre Kohorten in Mixpanel auswählen und importieren."
    tags:
      - Cohort membership
  - name: Segment Cohorts
    description: "Kund:innen, die Segment verwenden, können ihre Segmente ergänzen, indem sie ihre Kohorten in Segment auswählen und importieren."
    tags:
      - Cohort membership
  - name: Tinyclues Cohorts
    description: "Kund:innen, die Tinyclues verwenden, können ihre Segmente ergänzen, indem sie ihre Kohorten in Tinyclues auswählen und importieren."
    tags:
      - Cohort membership
  - name: Install Attribution Ad
    description: "Segmentiert Ihre Nutzer:innen nach der Anzeige, der ihre Installation zugeordnet wurde."
    tags:
      - User Attributes
  - name: Install Attribution Adgroup
    description: "Segmentiert Ihre Nutzer:innen nach der Anzeigengruppe, der ihre Installation zugeordnet wurde."
    tags:
      - Install attribution
  - name: Install Attribution Campaign
    description: "Segmentiert Ihre Nutzer:innen nach der Werbekampagne, der ihre Installation zugeordnet wurde."
    tags:
      - Install attribution
  - name: Install Attribution Source
    description: "Segmentiert Ihre Nutzer:innen nach der Quelle, der ihre Installation zugeordnet wurde."
    tags:
      - Install attribution
  - name: Churn Risk Category
    description: "Segmentiert Ihre Nutzer:innen nach der Abwanderung or Abwanderung, Churn or Abwanderung, churnen-Risiko-Kategorie gemäß einer bestimmten Prognose."
    tags:
      - Intelligence and predictive
  - name: Churn Risk Score
    description: "Segmentiert Ihre Nutzer:innen nach dem Abwanderung or Abwanderung, Churn or Abwanderung, churnen-Risiko-Score gemäß einer bestimmten Prognose."
    tags:
      - Intelligence and predictive
  - name: Event Likelihood Category
    description: "Segmentiert Ihre Nutzer:innen nach der Wahrscheinlichkeit, ein Event auszuführen, gemäß einer bestimmten Prognose."
    tags:
      - Intelligence and predictive
  - name: Event Likelihood Score
    description: "Segmentiert Ihre Nutzer:innen nach dem Wahrscheinlichkeits-Score, ein Event auszuführen, gemäß einer bestimmten Prognose."
    tags:
      - Intelligence and predictive
  - name: Intelligent Channel
    description: "Segmentiert Ihre Nutzer:innen nach ihrem aktivsten Kanal in den letzten drei Monaten."
    tags:
      - Intelligence and predictive
  - name: Message Open Likelihood
    description: "Filtert Ihre Nutzer:innen basierend auf ihrer <a href=\"/docs/user_guide/brazeai/intelligence_suite/intelligent_channel#individual-channels\">Wahrscheinlichkeit, eine Nachricht auf einem bestimmten Kanal zu öffnen</a>, auf einer Skala von 0–100 %. Nutzer:innen ohne ausreichende Daten zur Messung einer Wahrscheinlichkeit für einen Kanal können mit „ist leer“ ausgewählt werden.<br><br>Für E-Mails werden maschinelle Öffnungen von der Wahrscheinlichkeitsberechnung ausgeschlossen."
    tags:
      - Intelligence and predictive
  - name: Number of Facebook Friends Using App
    description: "Segmentiert Ihre Nutzer:innen danach, wie viele Facebook-Freunde sie haben, die dieselbe App nutzen."
    tags:
      - Social activity
  - name: Connected Facebook
    description: "Segmentiert Ihre Nutzer:innen danach, ob sie Ihre App mit Facebook verbunden haben."
    tags:
      - Social activity
  - name: Connected Twitter
    description: "Segmentiert Ihre Nutzer:innen danach, ob sie Ihre App mit X (ehemals Twitter) verbunden haben."
    tags:
      - Social activity
  - name: Number of Twitter Followers
    description: "Segmentiert Ihre Nutzer:innen danach, wie viele X-(ehemals Twitter-)Follower sie haben."
    tags:
      - Social activity
  - name: Phone Number
    description: "Segmentiert Ihre Nutzer:innen nach dem E.164-formatierten Telefonnummernfeld.<br><br> Wenn eine Telefonnummer an Braze gesendet wird, versucht Braze, sie in das <a href=\"/docs/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers#import-phone-numbers\">E.164-Format</a> zu konvertieren, das für den Versand über Kurzmitteilungsdienst or SMS-, RCS- und WhatsApp-Kanäle verwendet wird. Der Konvertierungsprozess kann fehlschlagen, wenn die Nummer nicht korrekt formatiert ist, was dazu führt, dass das Kundenprofil or Nutzerprofil eine unformatierte Telefonnummer, aber keine Sende-Telefonnummer hat. Dieser Segmentfilter gibt Nutzer:innen nach ihrer E.164-formatierten Telefonnummer zurück (sofern verfügbar).<br><br>Anwendungsfälle:<br> - Verwenden Sie diesen Filter, um die genaueste Zielgruppengröße beim Senden von Kurzmitteilungsdienst or SMS-, RCS- oder WhatsApp-Nachrichten zu ermitteln.  <br>- Verwenden Sie reguläre Ausdrücke (Regex) mit diesem Filter, um nach Telefonnummern mit einem bestimmten Ländercode zu segmentieren. <br>- Verwenden Sie diesen Filter, um Nutzer:innen nach Telefonnummern zu segmentieren, bei denen die E.164-Konvertierung fehlgeschlagen ist."
    tags:
      - Other Filters
---