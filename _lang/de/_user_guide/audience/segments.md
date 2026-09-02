---
nav_title: Segments
article_title: Segments
page_order: 3
layout: dev_guide
guide_top_header: "Segments"
guide_top_text: "Zielgruppensegmentierung ist ein Schlüssel für strategisches Marketing – sie kann Sie davor bewahren, Kund:innen zu häufig anzusprechen, zu belästigen oder eine potenzielle Verbindung zu verpassen. Lesen Sie die folgenden Artikel, um zu erfahren, wie Sie Ihre Zielgruppe zu Ihrem (und deren) größten Vorteil segmentieren und filtern können."
descriptions: "Zielgruppensegmentierung ist ein Schlüssel für strategisches Marketing – sie kann Sie davor bewahren, Kund:innen zu häufig anzusprechen, zu belästigen oder eine potenzielle Verbindung zu verpassen. Besuchen Sie diese Landing-Page, um zu erfahren, wie Sie Ihre Zielgruppe zu Ihrem (und deren) größten Vorteil segmentieren und filtern können."
search_rank: 4
tool: Segments
page_type: landing
description: "Diese Landing-Page enthält Artikel zur Segmentierung innerhalb von Dashboard-Campaigns. Hier finden Sie Informationen zum Einrichten eines Segments, zu Filtern, Funnels, Insights, Erweiterungen und mehr."

guide_featured_title: "Abschnittsartikel"
guide_featured_list:
  - name: Ein Segment erstellen
    link: /docs/user_guide/audience/segments/creating_a_segment
    image: /assets/img/braze_icons/pie-chart-01.svg
  - name: Segments verwalten
    link: /docs/user_guide/audience/segments/managing_segments
    image: /assets/img/braze_icons/edit-05.svg
  - name: Segmentierungsfilter
    link: /docs/user_guide/audience/segments/segmentation_filters
    image: /assets/img/braze_icons/flag-02.svg
  - name: Segmentdaten
    link: /docs/user_guide/audience/segments/segment_data
    image: /assets/img/braze_icons/bar-chart-01.svg
  - name: Segmenterweiterungen
    link: /docs/user_guide/audience/segments/segment_extension
    image: /assets/img/braze_icons/users-01.svg
  - name: Segment-Insights
    link: /docs/user_guide/audience/segments/segment_insights
    image: /assets/img/braze_icons/pie-chart-01.svg

guide_menu_title: "Weitere Artikel"
guide_menu_list:
  - name: Standort-Targeting
    link: /docs/user_guide/audience/segments/location_targeting
    image: /assets/img/braze_icons/marker-pin-06.svg
  - name: Reguläre Ausdrücke
    link: /docs/user_guide/audience/segments/regex
    image: /assets/img/braze_icons/search-sm.svg
  - name: Segmentgröße messen
    link: /docs/user_guide/audience/segments/measuring_segment_size
    image: /assets/img/braze_icons/pie-chart-02.svg
  - name: "Anwendungsfall: Segment mit verschachtelten angepassten Attributen"
    link: /docs/user_guide/audience/segments/segment_with_nested_custom_attributes
    image: /assets/img/braze_icons/dataflow-02.svg
  - name: Fehlerbehebung
    link: /docs/user_guide/audience/segments/troubleshooting
    image: /assets/img/braze_icons/annotation-question.svg

---

## Über Braze-Segmente {#about-braze-segments}

In Braze sind Segmente dynamische Gruppen von Nutzer:innen, die bestimmte von Ihnen definierte Kriterien erfüllen, wie z. B. Nutzerattribute, Nutzerverhalten und angepasste Events. Sie können die Kriterien verfeinern, indem Sie Segmente in andere Segmente verschachteln und zusätzliche Features anwenden, um den Umfang Ihrer Zielgruppe einzugrenzen und hochgradig personalisierte und ansprechende Inhalte an die richtigen Nutzer:innen zu senden.

Sie können so viele Segmente erstellen, wie Sie möchten, um Nutzer:innen gezielt anzusprechen. Erkunden Sie verschiedene Kombinationen von Segment-Features und Segmentierungsfiltern, um kreative Wege zur Nutzung Ihrer Nutzerdaten zu entdecken und neue Möglichkeiten zu erschließen, relevante Nachrichten an Nutzer:innen zu senden und das Engagement zu steigern.

Sehen Sie sich die folgenden Anwendungsfälle an, um einen kleinen Einblick zu erhalten, wie Braze-Segmente Ihnen helfen können, Ihre Nutzer:innen gezielt anzusprechen.

### Anwendungsfälle {#use-cases}

- **Willkommensnachrichten:** Segmentieren Sie neue Nutzer:innen, um Onboarding-E-Mails oder In-App-Nachrichten zu senden, die sie in Ihre App einführen.
- **Loyalty-Rewards:** Segmentieren Sie Nutzer:innen basierend auf ihrer Kaufhäufigkeit, ihrem Mitgliedschaftsjubiläum oder anderen Meilensteinen und senden Sie exklusive Angebote oder Rewards an Ihre treuesten Nutzer:innen.
- **Verhaltensbasierte Trigger:** Segmentieren Sie Nutzer:innen basierend auf ihren Aktionen, wie z. B. dem Abbruch eines Warenkorbs beim Checkout, um In-App-Nachrichten oder Push-Benachrichtigungen auszulösen.
- **Artikelempfehlungen:** Segmentieren Sie Nutzer:innen, die bestimmte Produkte gekauft haben, und senden Sie ihnen Empfehlungen für ergänzende oder höherwertige Produkte.
- **A/B-Tests:** Segmentieren Sie Nutzer:innen für A/B-Tests verschiedener Nachrichten, Betreffzeilen oder Inhalte, um herauszufinden, was bei Nutzer:innen bestimmter Altersgruppen, Geschlechter und anderer Attribute am besten ankommt.

#### Anwendungsfälle für Segmenterweiterungen {#segment-extension-use-cases}

Sie können Ihre Segmente weiter verfeinern, indem Sie [Segmenterweiterungen]({{site.baseurl}}/user_guide/audience/segments/segment_extension) verwenden, um Nutzer:innen basierend auf angepassten Events oder Kaufverhalten anzusprechen, die für die gesamte Lebensdauer ihres Nutzerprofils gespeichert werden.

- **Historische Käufe:** Segmentieren Sie Nutzer:innen danach, ob sie eine bestimmte Farbe eines bestimmten Produkts in den letzten zwei Jahren mindestens zweimal gekauft haben.
- **Events und Nachrichteninteraktionen:** Segmentieren Sie Nutzer:innen danach, ob sie in den letzten dreißig Tagen einen Kauf getätigt und außerdem mit einer bestimmten In-App-Nachricht interagiert haben.
- **Daten abfragen:**
  - **Snowflake abfragen:** Segmentieren Sie Nutzer:innen mit Daten, die aus Braze und externen Quellen wie einem CRM oder einem Data Warehouse kombiniert werden, indem Sie [SQL-Segmenterweiterungen]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) verwenden, um Snowflake abzufragen.
  - **Aus Data Warehouse synchronisieren:** Segmentieren Sie Nutzer:innen mit Daten, die direkt aus Ihrem Data Warehouse oder Dateispeichersystem mit Braze synchronisiert werden, indem Sie [CDI-Segmenterweiterungen]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments) verwenden.