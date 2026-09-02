---
nav_title: Angepasste Attribute
article_title: Angepasste Attribute
page_order: 1
page_type: reference
description: "Diese Seite beschreibt angepasste Attribute und erläutert die verschiedenen Datentypen für angepasste Attribute."
search_rank: 1
---

# [![Braze-Lernkurs]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"}Angepasste Attribute {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomcustom-events-and-attributes-stylefloatrightwidth120pxborder0-classnoimgbordercustom-attributes}

> Auf dieser Seite finden Sie Informationen zu angepassten Attributen, die eine Sammlung eindeutiger Eigenschaften Ihrer Nutzer:innen darstellen. Angepasste Attribute eignen sich am besten zum Speichern von Attributen über Ihre Nutzer:innen oder von Informationen über geringwertige Aktionen innerhalb Ihrer Anwendung.

In Braze gespeicherte angepasste Attribute können zum Aufbau von Zielgruppen-Segmenten und zur Personalisierung von Nachrichten mit Liquid verwendet werden. Denken Sie daran, dass Braze keine Zeitreiheninformationen für angepasste Attribute speichert, sodass Sie keine darauf basierenden Diagramme erhalten können, wie dies bei angepassten Events der Fall ist.

{% alert important %}
**Namen sind exakte Übereinstimmungen.** Schlüssel für angepasste Attribute sind **case-sensitiv** – zum Beispiel sind `Home_City` und `home_city` zwei verschiedene Attribute. Wenn Sie Daten über die [REST API]({{site.baseurl}}/api/endpoints/user_data/post_user_track) oder ein SDK senden, **entfernt Braze führende und nachgestellte Leerzeichen** aus Attributnamen, sodass `greeting` und ` greeting ` zum selben Schlüssel aufgelöst werden. Verwenden Sie überall, wo Sie ein Attribut referenzieren, dieselbe Schreibweise und Groß-/Kleinschreibung – in **Dateneinstellungen** > **Angepasste Attribute**, API- und SDK-Payloads sowie CSV-Importen. Informationen dazu, wie Braze eingehende Werte konvertiert, wenn Sie [einen Datentyp erzwingen]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data#data-type-coercion), finden Sie unter [Angepasste Daten verwalten]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data).
{% endalert %}

## Anwendungsfälle {#use-cases}

Einige gängige Anwendungsfälle für angepasste Attribute sind:

- Targeting und Unterdrückung von Zielgruppen durch Segmentierung von Nutzer:innen anhand von Merkmalen wie Treuestufe, Abo-Status, bevorzugter Sprache oder Tarifart
- Personalisierung von Nachrichten mit [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) durch Referenzierung von Attributen wie dem Vornamen, den Rewards-Punkten oder der Lieblingskategorie
- Tracking von Lifecycle-Phasen und Nutzerzuständen, wie Onboarding-Phase, Kontostatus oder Enddatum der Testphase
- Zählen von Aktionen mit geringem Wert mithilfe von [numerischen Attributen]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types), z. B. durch Inkrementieren eines `feature_views_count`-Attributs bei jedem Aufruf eines Features
- Aufzeichnen, wann Aktionen mit geringem Wert zuletzt stattgefunden haben, mithilfe von [Zeitattributen]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types), wie `last_support_ticket_at` oder `last_password_reset_at`
- Speichern von Interessen und Verlauf als [Arrays]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types), z. B. Lieblingsgenres oder kürzlich angesehene Inhalte, für interessenbasiertes Targeting
- Speichern umfangreicherer Profildaten als [Objekte]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support) oder [Arrays von Objekten]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects), z. B. strukturierte Präferenzen oder mehrere gespeicherte Adressen
- Auslösen von aktionsbasierten Nachrichten bei Änderung eines Attributwerts mithilfe von [Attribut-Triggern]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers), z. B. Versand einer Stufenaufstiegs-Benachrichtigung, wenn sich das Attribut `rewards_tier` ändert

## Angepasste Attribute verwalten {#managing-custom-attributes}

Um angepasste Attribute im Dashboard zu erstellen und zu verwalten, gehen Sie zu **Dateneinstellungen** > **Angepasste Attribute**.

![Vier angepasste Attribute, die boolesche Werte sind.]({% image_buster /assets/img/export_custom_attributes.png %})

In der Spalte **Letztes Update** sehen Sie, wann das angepasste Attribut das letzte Mal bearbeitet wurde, z. B. wann es zuletzt auf Blockliste oder aktiv gesetzt wurde.

{% alert note %}
Wenn ein angepasstes Array-Attribut in einem Kundenprofil ohne Werte angezeigt wird, überprüfen Sie, ob die **Maximale Länge** des Attributs größer als `0` ist. Eine schrittweise Fehlerbehebung finden Sie unter [Datentypen]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#arrays).
{% endalert %}

{% alert important %}
Für ein korrektes Nachrichten-Targeting stellen Sie sicher, dass der Datentyp Ihres angepassten Attributs mit dem tatsächlichen angepassten Attribut übereinstimmt. <br><br>Wenn beispielsweise `newsletter_subscribed` als String definiert ist, sollte Ihre Liquid-Syntax so aussehen: {% raw %}`{% if {{custom_attribute.${newsletter_subscribed}}} == 'true' %}`{% endraw %}. Wenn `newsletter_subscribed` als boolescher Wert definiert ist, sollte die Liquid-Syntax keine einfachen Anführungszeichen enthalten: {% raw %}`{% if {{custom_attribute.${newsletter_subscribed}}} == true %}`{% endraw %}.
{% endalert %}

### Fehlerbehebung bei doppelten angepassten Attributen oder Events {#troubleshooting-duplicate-custom-attributes-or-events}

{% multi_lang_include data_activation/troubleshooting_duplicate_custom_data_entries.md %}

Von dieser Seite aus können Sie vorhandene angepasste Attribute anzeigen, verwalten, erstellen oder auf die Blockliste setzen. Wählen Sie das Menü neben einem angepassten Attribut für die folgenden Aktionen:

### Blockliste {#blocklisting}

Sie können einzelne angepasste Attribute über das Aktionsmenü auf die Blockliste setzen oder bis zu 100 Attribute gleichzeitig auswählen und in einem Schritt blockieren.

Wenn Sie ein angepasstes Attribut blockieren:

- Werden keine zukünftigen Daten mehr für dieses Attribut erfasst.
- Sind vorhandene Daten nicht verfügbar, es sei denn, das Attribut wird wieder freigegeben.
- Wird dieses Attribut nicht in Filtern oder Diagrammen angezeigt.

Wenn ein blockiertes angepasstes Attribut derzeit von Filtern oder Triggern in anderen Bereichen von Braze referenziert wird, erscheint zusätzlich ein Warnhinweis, der erklärt, dass alle Instanzen der Filter oder Trigger, die darauf verweisen, entfernt und archiviert werden.

Weitere Details zum Blockieren und Löschen angepasster Daten finden Sie unter [Angepasste Daten blockieren]({{site.baseurl}}/user_guide/data/activation/custom_data/blocklist_custom_data).

### Als personenbezogene Daten (PII) markieren {#mark-as-personally-identifiable-information-pii}

Administrator:innen können auf dieser Seite auch angepasste Attribute erstellen und als PII markieren. Diese Attribute sind nur für Administrator:innen und Dashboard-Nutzer:innen mit der Berechtigung „Angepasste Attribute anzeigen, die als PII markiert sind“ sichtbar.

### Beschreibungen hinzufügen {#add-descriptions}

Sie können einem angepassten Attribut nach der Erstellung eine Beschreibung hinzufügen, wenn Sie die [Nutzerberechtigung]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) `Manage Events, Attributes, Purchases` haben. Wählen Sie **Beschreibung bearbeiten** für das angepasste Attribut und geben Sie ein, was Sie möchten, z. B. eine Notiz für Ihr Team.

### Tags hinzufügen {#add-tags}

Sie können einem angepassten Attribut nach der Erstellung Tags hinzufügen, wenn Sie die [Nutzerberechtigung]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) „Manage Events, Attributes, Purchases“ haben. Die Tags können dann verwendet werden, um die Liste der Attribute zu filtern.

### Angepasste Attribute entfernen {#remove-custom-attributes}

Es gibt zwei Möglichkeiten, angepasste Attribute aus Nutzerprofilen zu entfernen:

* Wählen Sie den Namen des zu entfernenden angepassten Attributs in einem [Nutzeraktualisierung-Schritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update#removing-custom-attributes) aus.
* Setzen Sie den Wert `null` in Ihrer API-Anfrage an den [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track).

### Daten exportieren {#export-data}

Um die Liste der angepassten Attribute als CSV-Datei zu exportieren, wählen Sie oben auf der Seite **Alle exportieren**. Die CSV-Datei wird generiert, und ein Download-Link wird Ihnen per E-Mail zugesendet.

## Typ eines angepassten Attributs ändern {#change-custom-attribute-type}

### Voraussetzungen {#prerequisites}

Das angepasste Attribut darf derzeit nicht in aktiven Campaigns, Canvases oder Segments verwendet werden. Wenn Sie versuchen, den Datentyp zu ändern, während das Attribut noch referenziert wird, zeigt das Dashboard einen Fehler an und blockiert die Änderung.

### Datentyp ändern {#changing-the-data-type}

1. Stoppen Sie alle aktiven Campaigns oder Canvases, die das Attribut in Segments oder Filtern verwenden.
2. Entfernen Sie das Attribut aus allen Segment-, Campaign- und Canvas-Filtern.
3. Gehen Sie zu **Dateneinstellungen** > **Angepasste Attribute** (oder **Angepasste Events**), suchen Sie das Attribut und aktualisieren Sie es auf den gewünschten Datentyp.
4. Aktualisieren Sie die Attributwerte in bestehenden Nutzerprofilen, damit sie dem neuen Datentyp entsprechen (z. B. mithilfe des [`/users/track`-Endpunkts]({{site.baseurl}}/api/endpoints/user_data/post_user_track)).
5. Wenden Sie das Attribut erneut auf die relevanten Segments, Campaigns und Canvases an und reaktivieren Sie alle gestoppten Campaigns oder Canvases.

### Wissenswert {#things-to-know}

- **Nutzerdaten werden nicht rückwirkend aktualisiert.** Wenn ein Kundenprofil das Attribut mit dem alten Datentyp enthielt, bleibt dieser Wert unverändert. Der Segmentierungsfilter sucht nach dem neuen Datentyp, sodass Nutzer:innen mit dem alten Wert aus übereinstimmenden Segments ausgeschlossen werden, bis ihr Profil aktualisiert wurde.
- **Neue Daten müssen dem neuen Datentyp entsprechen.** Nach der Änderung werden API-Aufrufe oder SDK-Events, die den vorherigen Datentyp für dieses Attribut senden, nicht akzeptiert. Nur Werte, die dem neuen Datentyp entsprechen, werden aufgenommen.
- **Filter werden nicht automatisch aktualisiert.** Segments und Campaign-Filter, die auf das geänderte Attribut verweisen, werden nicht rückwirkend aktualisiert. Sie müssen sie nach der Änderung entfernen und erneut hinzufügen.

## Nutzungsberichte anzeigen {#view-usage-reports}

Der Nutzungsbericht listet alle Canvases, Campaigns und Segments auf, die ein bestimmtes angepasstes Attribut verwenden. Diese Liste enthält keine Verwendungen von Liquid.

Sie können bis zu 100 Nutzungsberichte gleichzeitig anzeigen, indem Sie die Kontrollkästchen neben den jeweiligen angepassten Attributen aktivieren und dann **Nutzungsbericht anzeigen** auswählen.

### Tab „Values“ {#values-tab}

Wenn Sie einen Nutzungsbericht anzeigen, wählen Sie den Tab **Values** aus, um die häufigsten Werte der ausgewählten angepassten Attribute basierend auf einer Stichprobe von etwa 250.000 Nutzer:innen anzuzeigen. Da die Ergebnisse aus einer Teilmenge von Nutzer:innen stammen, enthält die Stichprobe nicht alle vorhandenen Werte. Das bedeutet, dass der Tab **Values** nicht zur Fehlerbehebung oder für Anwendungsfälle verwendet werden sollte, die Daten aller Nutzer:innen erfordern.

![Nutzungsbericht für ausgewählte angepasste Attribute mit geöffnetem Tab „Values“, der ein Kreisdiagramm der Länderattributwerte wie „US“ und „PR“ zeigt.]({% image_buster /assets/img/usage_report_values.png %}){: style="max-width:80%;"}

## Angepasste Attribute festlegen {#set-custom-attributes}

Die folgenden Listen zeigen Methoden auf verschiedenen Plattformen, die zum Festlegen angepasster Attribute verwendet werden.

{% details Dokumentation nach Plattform anzeigen %}

- [Android und FireOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes?sdktab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes?sdktab=swift)
- [Internet]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes?sdktab=web)
- [React Native]({{site.baseurl}}/developer_guide/analytics)
- [Unity]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes?sdktab=unity)
- [.NET MAUI (ehemals Xamarin)]({{site.baseurl}}/developer_guide/analytics?sdktab=xamarin)
- [Roku]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes)

{% enddetails %}

## Speicherung angepasster Attribute {#custom-attribute-storage}

Alle im **Kundenprofil** gespeicherten Daten, einschließlich angepasster Attribute, werden unbegrenzt aufbewahrt, solange jedes Profil <a href="/docs/user_archival#active-users">aktiv</a> ist.

Eine vollständige Übersicht aller Datentypen, die Sie als angepasste Attribute speichern können – einschließlich boolescher Werte, Zahlen, Strings, Arrays, Zeitangaben, Objekte und Arrays von Objekten – finden Sie unter [Datentypen für angepasste Attribute]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types).

### Leere Strings im Vergleich zu Null-Werten {#blank-strings-versus-null-values}

Beim Löschen oder Zurücksetzen eines angepassten Attributs unterscheidet sich das Verhalten je nachdem, ob Sie einen leeren String (`""`) oder `null` übergeben:

| Wert | Verhalten |
| --- | --- |
| `""` (leerer String) | Das Attribut wird auf einen leeren Wert gesetzt und bleibt im Kundenprofil sichtbar. |
| `null` | Das Attribut wird vollständig aus dem Kundenprofil entfernt. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Leere Strings im Vergleich zu Null-Werten" }
{: .reset-td-br-1 .reset-td-br-2 aria-label="Leere Strings im Vergleich zu Null-Werten" }
{: .reset-td-br-1 .reset-td-br-2 aria-label="Leere Strings im Vergleich zu Null-Werten" }

Dieses Verhalten wirkt sich auch auf die Segmentierung aus. Bei angepassten Attributen prüft der Filter **IS NOT BLANK**, ob ein nicht-leerer Wert vorliegt. Das bedeutet, dass ein leerer String (`""`) nicht übereinstimmt, obwohl das Attribut im Profil sichtbar bleibt. Ein `null`-Wert stimmt ebenfalls nicht überein, da das Attribut aus dem Profil entfernt wird.

{% alert important %}
Bei nicht-String-Datentypen, bei denen der Datentyp manuell im Braze-Dashboard festgelegt wird (nicht automatisch erkannt), müssen Sie `null` verwenden, um den Wert zurückzusetzen. Die Übergabe von `""` ist nur für String-Attribute gültig – beispielsweise wird das Setzen eines booleschen Attributs auf `""` als leerer String behandelt, was ein ungültiger Wert für diesen Typ ist. Um einen booleschen Wert zurückzusetzen, übergeben Sie `null`.

Beachten Sie, dass CSV-Importe `null` nicht unterstützen – boolesche Werte in CSV-Importen müssen `TRUE` oder `FALSE` sein.
{% endalert %}