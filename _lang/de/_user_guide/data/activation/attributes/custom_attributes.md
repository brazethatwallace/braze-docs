---
nav_title: Angepasste Attribute
article_title: Angepasste Attribute
page_order: 1
page_type: reference
description: "Diese Seite beschreibt angepasste Attribute und erläutert die verschiedenen Datentypen für angepasste Attribute."
search_rank: 1
---

# [![Braze-Lernkurs]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"}Angepasste Attribute {#custom-attributes}

> Auf dieser Seite finden Sie Informationen zu angepassten Attributen, die eine Sammlung eindeutiger Eigenschaften Ihrer Nutzer:innen darstellen. Angepasste Attribute eignen sich am besten zum Speichern von Attributen über Ihre Nutzer:innen oder von Informationen über geringwertige Aktionen innerhalb Ihrer Anwendung.

In Braze gespeicherte angepasste Attribute können zum Aufbau von Zielgruppen-Segmenten und zur Personalisierung von Nachrichten mit Liquid verwendet werden. Denken Sie daran, dass Braze keine Zeitreiheninformationen für angepasste Attribute speichert, sodass Sie keine darauf basierenden Diagramme erhalten können, wie dies bei angepassten Events der Fall ist.

{% alert important %}
**Namen sind exakte Übereinstimmungen.** Schlüssel für angepasste Attribute sind **case-sensitiv** – zum Beispiel sind `Home_City` und `home_city` zwei verschiedene Attribute. Wenn Sie Daten über die [REST API]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) oder ein SDK senden, **entfernt Braze führende und nachgestellte Leerzeichen** aus Attributnamen, sodass `greeting` und ` greeting ` zum selben Schlüssel aufgelöst werden. Verwenden Sie überall, wo Sie ein Attribut referenzieren, dieselbe Schreibweise und Groß-/Kleinschreibung – in **Data Settings** > **Custom Attributes**, API- und SDK-Payloads sowie CSV-Importen. Informationen dazu, wie Braze eingehende Werte konvertiert, wenn Sie [einen Datentyp erzwingen]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data/#data-type-coercion), finden Sie unter [Angepasste Daten verwalten]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data/).
{% endalert %}

## Anwendungsfälle {#use-cases}

Einige häufige Anwendungsfälle für angepasste Attribute sind:

- Targeting und Unterdrückung von Zielgruppen durch Segmentierung von Nutzer:innen basierend auf Merkmalen wie Treuestufe, Abo-Status, bevorzugter Sprache oder Tariftyp
- Personalisierung von Nachrichten mit [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/) durch Referenzierung von Attributen wie dem Vornamen, Rewards-Punkten oder der Lieblingskategorie
- Tracking von Lebenszyklusphasen und Nutzerstatus, wie z. B. Onboarding-Phase, Kontostatus oder Testende-Datum
- Zählen von geringwertigen Aktionen mithilfe von [numerischen Attributen]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types/#numbers), z. B. durch Inkrementieren eines `feature_views_count`-Attributs bei jedem Aufruf eines Features
- Aufzeichnung, wann geringwertige Aktionen zuletzt stattfanden, mithilfe von [Zeitattributen]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types/#time), wie z. B. `last_support_ticket_at` oder `last_password_reset_at`
- Speichern von Nutzerinteressen und -verlauf als [Arrays]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types/#arrays), z. B. Lieblingsgenres oder kürzlich angesehene Inhalte, für interessenbasiertes Targeting
- Speichern umfangreicherer Profildaten als [Objekte]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support/) oder [Arrays von Objekten]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects/), z. B. strukturierte Präferenzen oder mehrere gespeicherte Adressen
- Auslösen aktionsbasierter Nachrichten bei Änderung eines Attributwerts mithilfe von [Attribut-Triggern]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers/), z. B. Senden einer Stufenaufstiegs-Benachrichtigung, wenn sich die `rewards_tier` einer Nutzerin oder eines Nutzers ändert

## Angepasste Attribute verwalten {#managing-custom-attributes}

Um angepasste Attribute im Dashboard zu erstellen und zu verwalten, gehen Sie zu **Dateneinstellungen** > **Angepasste Attribute**.

![Vier angepasste Attribute, die Boolesche Werte sind.]({% image_buster /assets/img/export_custom_attributes.png %})

In der Spalte **Letztes Update** sehen Sie, wann das angepasste Attribut das letzte Mal bearbeitet wurde, z. B. wann es zuletzt auf Blockliste oder aktiv gesetzt wurde.

{% alert important %}
Für ein korrektes Nachrichten-Targeting stellen Sie sicher, dass der Datentyp Ihres angepassten Attributs mit dem tatsächlichen angepassten Attribut übereinstimmt. <br><br>Wenn beispielsweise `newsletter_subscribed` als String definiert ist, sollte Ihre Liquid-Syntax so aussehen: {% raw %}`{% if {{custom_attribute.${newsletter_subscribed}}} == 'true' %}`{% endraw %}. Wenn `newsletter_subscribed` als Boolescher Wert definiert ist, sollte die Liquid-Syntax keine einfachen Anführungszeichen enthalten: {% raw %}`{% if {{custom_attribute.${newsletter_subscribed}}} == true %}`{% endraw %}.
{% endalert %}

Von dieser Seite aus können Sie vorhandene angepasste Attribute anzeigen, verwalten, erstellen oder auf die Blockliste setzen. Wählen Sie das Menü neben einem angepassten Attribut für die folgenden Aktionen:

### Blockliste {#blocklisting}

Sie können einzelne angepasste Attribute über das Aktionsmenü auf die Blockliste setzen oder bis zu 100 Attribute gleichzeitig auswählen und in einem Schritt blockieren.

Wenn Sie ein angepasstes Attribut blockieren:

- Werden keine zukünftigen Daten mehr für dieses Attribut erfasst.
- Sind vorhandene Daten nicht verfügbar, es sei denn, das Attribut wird wieder freigegeben.
- Wird dieses Attribut nicht in Filtern oder Diagrammen angezeigt.

Wenn ein blockiertes angepasstes Attribut derzeit von Filtern oder Triggern in anderen Bereichen von Braze referenziert wird, erscheint zusätzlich ein Warnhinweis, der erklärt, dass alle Instanzen der Filter oder Trigger, die darauf verweisen, entfernt und archiviert werden.

Weitere Details zum Blockieren und Löschen angepasster Daten finden Sie unter [Angepasste Daten blockieren]({{site.baseurl}}/user_guide/data/activation/custom_data/blocklist_custom_data/).

### Als personenbezogene Daten (PII) markieren {#mark-as-personally-identifiable-information-pii}

Administrator:innen können auf dieser Seite auch angepasste Attribute erstellen und als PII markieren. Diese Attribute sind nur für Administrator:innen und Dashboard-Nutzer:innen mit der Berechtigung „Angepasste Attribute anzeigen, die als PII markiert sind“ sichtbar.

### Beschreibungen hinzufügen {#add-descriptions}

Sie können einem angepassten Attribut nach der Erstellung eine Beschreibung hinzufügen, wenn Sie die [Nutzerberechtigung]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/) `Manage Events, Attributes, Purchases` haben. Wählen Sie **Beschreibung bearbeiten** für das angepasste Attribut und geben Sie ein, was Sie möchten, z. B. eine Notiz für Ihr Team.

### Tags hinzufügen {#add-tags}

Sie können einem angepassten Attribut nach der Erstellung Tags hinzufügen, wenn Sie die [Nutzerberechtigung]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/) „Manage Events, Attributes, Purchases“ haben. Die Tags können dann verwendet werden, um die Liste der Attribute zu filtern.

### Angepasste Attribute entfernen {#remove-custom-attributes}

Es gibt zwei Möglichkeiten, angepasste Attribute aus Nutzerprofilen zu entfernen:

* Wählen Sie den Namen des zu entfernenden angepassten Attributs in einem [Nutzeraktualisierung-Schritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update/#removing-custom-attributes) aus.
* Setzen Sie den Wert `null` in Ihrer API-Anfrage an den [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#user-track).

### Daten exportieren {#export-data}

Um die Liste der angepassten Attribute als CSV-Datei zu exportieren, wählen Sie oben auf der Seite **Alle exportieren**. Die CSV-Datei wird generiert, und ein Download-Link wird Ihnen per E-Mail zugesendet.

## Datentyp eines angepassten Attributs ändern {#change-custom-attribute-type}

### Voraussetzungen {#prerequisites}

Das angepasste Attribut darf derzeit nicht in aktiven Campaigns, Canvases oder Segmenten verwendet werden. Wenn Sie versuchen, den Datentyp zu ändern, während das Attribut noch referenziert wird, zeigt das Dashboard einen Fehler an und blockiert die Änderung.

### Den Datentyp ändern {#changing-the-data-type}

1. Stoppen Sie alle aktiven Campaigns oder Canvases, die das Attribut in Segmenten oder Filtern verwenden.
2. Entfernen Sie das Attribut aus allen Segment-, Campaign- und Canvas-Filtern.
3. Gehen Sie zu **Dateneinstellungen** > **Angepasste Attribute** (oder **Angepasste Events**), suchen Sie das Attribut und aktualisieren Sie es auf den gewünschten Datentyp.
4. Aktualisieren Sie die Attributwerte in vorhandenen Nutzerprofilen, damit sie dem neuen Datentyp entsprechen (z. B. über den [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)).
5. Wenden Sie das Attribut erneut auf die relevanten Segmente, Campaigns und Canvases an und reaktivieren Sie dann alle gestoppten Campaigns oder Canvases.

### Wichtige Hinweise {#things-to-know}

- **Nutzerdaten werden nicht rückwirkend aktualisiert.** Wenn ein Nutzerprofil das Attribut mit dem alten Datentyp hatte, bleibt dieser Wert unverändert. Der Segmentierungsfilter sucht nach dem neuen Datentyp, sodass Nutzer:innen mit dem alten Wert von passenden Segmenten ausgeschlossen werden, bis ihr Profil aktualisiert wird.
- **Neue Daten müssen dem neuen Datentyp entsprechen.** Nach der Änderung werden API-Aufrufe oder SDK-Events, die den vorherigen Datentyp für dieses Attribut senden, nicht akzeptiert. Nur Werte, die dem neuen Datentyp entsprechen, werden aufgenommen.
- **Filter werden nicht automatisch aktualisiert.** Segmente und Campaign-Filter, die auf das geänderte Attribut verweisen, werden nicht rückwirkend aktualisiert. Sie müssen sie nach der Änderung entfernen und erneut hinzufügen.

## Nutzungsberichte anzeigen {#view-usage-reports}

Der Nutzungsbericht listet alle Canvases, Campaigns und Segmente auf, die ein bestimmtes angepasstes Attribut verwenden. Diese Liste enthält keine Liquid-Verwendungen.

Sie können bis zu 100 Nutzungsberichte gleichzeitig anzeigen, indem Sie die Kontrollkästchen neben den jeweiligen angepassten Attributen aktivieren und dann **Nutzungsbericht anzeigen** auswählen.

### Tab „Werte“ {#values-tab}

Wenn Sie einen Nutzungsbericht anzeigen, wählen Sie den Tab **Werte**, um die häufigsten Werte der ausgewählten angepassten Attribute basierend auf einer Stichprobe von etwa 250.000 Nutzer:innen anzuzeigen. Beachten Sie, dass die Ergebnisse aus einer Teilmenge von Nutzer:innen stammen und die Stichprobe daher nicht alle vorhandenen Werte enthält. Das bedeutet, dass der Tab **Werte** nicht für die Fehlerbehebung oder für Anwendungsfälle verwendet werden sollte, die Daten aller Nutzer:innen erfordern.

![Nutzungsbericht für ausgewählte angepasste Attribute mit einem geöffneten Tab „Werte“, der ein Kreisdiagramm der Länderattributwerte wie „US“ und „PR“ zeigt.]({% image_buster /assets/img/usage_report_values.png %}){: style="max-width:80%;"}

## Angepasste Attribute setzen {#set-custom-attributes}

Im Folgenden finden Sie Methoden für verschiedene Plattformen, die zum Setzen angepasster Attribute verwendet werden.

{% details Für plattformspezifische Dokumentation aufklappen %}

- [Android und FireOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-custom-attributes)
- [Unity]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=unity)
- [.NET MAUI (ehemals Xamarin)]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#setting-custom-attributes)
- [Roku]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/)

{% enddetails %}

## Speicherung angepasster Attribute {#custom-attribute-storage}

Alle im **Nutzerprofil** gespeicherten Daten, einschließlich angepasster Attributdaten, werden auf unbestimmte Zeit aufbewahrt, solange jedes Profil [aktiv]({{site.baseurl}}/user_archival/#active-users) ist.

Eine vollständige Referenz aller Datentypen, die Sie als angepasste Attribute speichern können – einschließlich Boolescher Werte, Zahlen, Strings, Arrays, Zeitangaben, Objekte und Arrays von Objekten – finden Sie unter [Datentypen für angepasste Attribute]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types/).