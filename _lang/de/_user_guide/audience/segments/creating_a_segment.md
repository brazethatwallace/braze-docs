---
nav_title: Segment erstellen
article_title: Segment erstellen
page_order: 1
page_type: tutorial
description: "Dieser Artikel zeigt Ihnen Schritt für Schritt, wie Sie mit Braze ein Segment einrichten und erstellen."
tool: Segments
search_rank: 3
---

# [![Braze-Lernkurs]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/segmentation-course){: style="float:right;width:120px;border:0;" class="noimgborder"}Segment erstellen {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomsegmentation-course-stylefloatrightwidth120pxborder0-classnoimgbordercreate-a-segment}

> Mit der Segmentierung können Sie Nutzer:innen anhand ihrer demografischen, verhaltensbezogenen oder technischen Merkmale und Aktionen ansprechen. Der kreative und intelligente Einsatz von Segmentierung und Messaging-Automatisierung ermöglicht es Ihnen, Ihre Nutzer:innen nahtlos vom ersten Kontakt bis hin zu langfristigen Kund:innen zu begleiten. Segmente werden in Realtime aktualisiert, wenn sich Daten ändern, und Sie können so viele Segmente erstellen, wie Sie für Ihr Targeting und Ihre Messaging-Zwecke benötigen.

## Schritt 1: Zum Bereich „Segmente“ navigieren {#step-1-navigate-to-the-segments-section}

Gehen Sie zu **Audience** > **Segments**.

## Schritt 2: Segment benennen {#step-2-name-your-segment}

Wählen Sie **Create Segment** aus, um mit dem Erstellen Ihres Segments zu beginnen. Benennen Sie Ihr Segment, indem Sie die Art der Nutzer:innen beschreiben, die Sie filtern möchten. So können Sie das Segment leichter identifizieren, wenn Sie es für Ihre Campaigns oder Canvases als Zielgruppe verwenden möchten. Vage Segmenttitel können verwirrend sein.

Sie können auch Operator bitten, die Filterlogik Ihres Segments anhand einer Beschreibung Ihrer Zielgruppe zu erstellen. Weitere Informationen finden Sie unter [Was Sie mit Operator tun können]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#campaigns-and-audiences).

Optional können Sie Folgendes tun:
- Eine Beschreibung zum Segment hinzufügen, um weitere Details zur Absicht dieser Zielgruppe anzugeben und Notizen für andere Teammitglieder zu hinterlassen.
- Ein [Team]({{site.baseurl}}/user_guide/administer/global/user_management/teams) zu Ihrem Segment hinzufügen.
- [Tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) zu Ihrem Segment hinzufügen, um es besser zu organisieren.

Segmente werden gespeichert, sobald Sie **Create Segment** auswählen. Sie müssen nicht zuerst im Segment-Editor **Save** auswählen.

{% alert note %}
Wenn Sie die Berechtigung „Segmente bearbeiten“ nur auf Team-Ebene haben (nicht auf Workspace-Ebene), weist Braze beim Erstellen des Segments ein Team zu:
<br><br>
- **Ein berechtigtes Team:** Dieses Team wird automatisch zugewiesen.
- **Mehrere berechtigte Teams:** Braze weist das erste Team in Ihrer Liste der berechtigten Teams zu. Sie können das Team im Segment-Editor ändern, bevor Sie das Segment teilen oder verwenden.
{% endalert %}

## Schritt 3: App oder Plattform auswählen {#step-3-choose-your-app-or-platform}

Wählen Sie aus, welche Apps oder Plattformen Sie ansprechen möchten, indem Sie **Nutzer:innen aus allen Apps** (Standard) oder **Nutzer:innen aus bestimmten Apps** auswählen. **Nutzer:innen aus bestimmten Apps** richtet sich an Nutzer:innen mit mindestens einer Sitzung in den angegebenen Apps.

Wenn Sie beispielsweise eine In-App-Nachricht nur an iOS-Geräte senden möchten, wählen Sie Ihre iOS-App aus. So wird sichergestellt, dass Nutzer:innen, die sowohl ein iOS- als auch ein Android-Gerät verwenden, die Nachricht nur auf ihrem iOS-Gerät erhalten. In der Liste der bestimmten Apps können Sie mit der Option **Nutzer:innen ohne Apps** Nutzer:innen ohne Sitzungen und ohne App-Daten einschließen (die in der Regel über Nutzerimport oder REST API erstellt wurden).

![Panel „Segmentdetails“ mit der ausgewählten Option „Nutzer:innen aus allen Apps“ im Abschnitt „Verwendete Apps“.]({% image_buster /assets/img_archive/Segment2.png %}){: style="max-width:80%;"}

## Schritt 4: Filter zu Ihrem Segment hinzufügen {#step-4-add-filters-to-your-segment}

Fügen Sie Ihrem Segment mindestens einen Filter hinzu. Sie können beliebig viele Filter kombinieren, um Ihre Segmentierung spezifischer zu gestalten.

{% multi_lang_include alerts/note_alerts.md alert='Segment profiles first app use' %}

### Filtergruppen {#filter-groups}

Filter sind in Filtergruppen organisiert. Jeder Filter muss Teil einer Filtergruppe sein, die mindestens einen Filter enthält. Ein Segment kann mehrere Filtergruppen haben. Um eine hinzuzufügen, wählen Sie **Filtergruppe hinzufügen** aus. Bearbeiten Sie den Namen der Filtergruppe, indem Sie das Symbol auswählen, das erscheint, wenn Sie den Mauszeiger daneben bewegen.

![Filtergruppe mit einem Bearbeitungssymbol neben ihrem Namen.]({% image_buster /assets/img_archive/edit_filter_group_name.png %})

Wählen Sie die Symbole neben jedem Filter aus, um den Filter-Editor ein- oder auszuklappen oder einzelne Filter zu duplizieren. Nach dem Duplizieren eines Filters können Sie dessen Werte in jedem Dropdown-Menü anpassen.

### Segmentierungslogik mit AND und OR {#segmentation-logic-using-and-and-or}

Innerhalb einer Filtergruppe können Filter entweder mit „AND“ oder „OR“ verknüpft werden. Zwischen Filtergruppen können Gruppen ebenfalls mit „AND“ oder „OR“ verknüpft werden. Bei der Verwendung von Filtergruppen können Sie Segmentierungslogik wie die folgende erstellen:
- (A AND B AND C) OR (C AND E AND F)
- (A OR B OR C) AND (C OR D OR F)

Wenn Sie „OR“ für Ihre Filter auswählen, enthält Ihr Segment Nutzer:innen, die eine beliebige Kombination aus einem, einigen oder allen dieser Filter erfüllen. Wenn Sie „AND“ auswählen, werden Nutzer:innen, die diesen Filter nicht erfüllen, nicht in Ihr Segment aufgenommen.

{% alert tip %}
Wenn Sie „OR“ für Filter auswählen, die einen negativen Filter enthalten (z. B. „ist nicht“ in einer Abo-Gruppe), denken Sie daran, dass Nutzer:innen nur einen der „OR“-Filter erfüllen müssen, um in das Segment aufgenommen zu werden. Um den negativen Filter unabhängig von den anderen Filtern anzuwenden, verwenden Sie eine [Ausschlussgruppe](#exclusion).
{% endalert %}

{% details Wann der OR-Operator vermieden werden sollte %}

Es kann Targeting-Situationen geben, in denen die Verwendung des `OR`-Operators vermieden werden sollte. Der `OR`-Operator erstellt eine Aussage, die als wahr ausgewertet wird, wenn ein:e Nutzer:in die Kriterien für einen oder mehrere der Filter in einer Aussage erfüllt. Wenn Sie beispielsweise ein Segment von Nutzer:innen erstellen möchten, die zu „Foodies“ gehören, aber weder zu „Non-foodies“ noch zu „Candy-lovers“, dann würde der `OR`-Operator hier funktionieren.

![Filtergruppe für Nutzer:innen im Segment „Foodies“, die nicht in den Segmenten „Non-foodies“ oder „Candy-lovers“ sind.]({% image_buster /assets/img_archive/or_operator_segment.png %})

Wenn Ihr Ziel jedoch darin besteht, Nutzer:innen zu segmentieren, die zum Segment „Foodies“ gehören und gleichzeitig nicht in den Segmenten „Non-foodies“ und „Candy-lovers“ sind, dann verwenden Sie den `AND`-Operator. Auf diese Weise befinden sich Nutzer:innen, die die Campaign oder das Canvas erhalten, im beabsichtigten Segment („Foodies“) und gleichzeitig nicht in den anderen Segmenten („Non-foodies“ und „Candy-lovers“).

Die folgenden negativen Targeting-Kriterien sollten nicht mit dem `OR`-Operator verwendet werden, wenn zwei oder mehr Filter dasselbe Attribut referenzieren:

- `not included`
- `is not`
- `does not equal`
- `does not match regex`

Wenn `not included`, `is not`, `does not equal` oder `does not match regex` mit dem `OR`-Operator zwei oder mehr Mal in einer Aussage verwendet werden, werden Nutzer:innen mit allen Werten für das relevante Attribut angesprochen.

{% enddetails %}

### Filteroperatoren {#filter-operators}

Abhängig vom spezifischen Filter, den Sie auswählen, stehen Ihnen verschiedene Operatoren zur Identifizierung von Filterwerten zur Verfügung. Um tiefer in die verfügbaren Operatoren für verschiedene Typen angepasster Attribute einzutauchen, lesen Sie [Speicherung angepasster Attribute]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes#set-custom-attributes). Beachten Sie, dass bei Verwendung des Operators „is any of“ die maximale Anzahl von Elementen, die Sie in dieses Feld aufnehmen können, 256 beträgt.

{% alert note %}
Braze erstellt keine Profile für Nutzer:innen, bis diese die App zum ersten Mal verwendet haben. Daher können Sie keine Nutzer:innen ansprechen, die Ihre App noch nicht geöffnet haben.
{% endalert %}

![Segmenter-Filtergruppen mit dem AND-Operator.]({% image_buster /assets/img_archive/segmenter_filter_groups.png %})

#### Anzeige von Datums- und Aktualitätsfiltern {#date-and-recency-filter-display}

Wenn Sie einen relativen Zeitfilter mit Tagen festlegen (z. B. ein Ereignis, das vor mehr als 84&nbsp;Tagen und weniger als 91&nbsp;Tagen stattfand), wandelt Braze den Wert nach dem Speichern in Wochen um, wenn die Tagesanzahl gleichmäßig durch sieben teilbar ist. Beispielsweise werden 91&nbsp;Tage als 13&nbsp;Wochen angezeigt, aber 121&nbsp;Tage bleiben in Tagen, da sie nicht gleichmäßig teilbar sind. Dies ist nur eine Änderung der Anzeige – die Werte werden weiterhin als Tage gespeichert und verarbeitet.

{% alert important %}
Segmente, die bereits den Filter **Segment Membership** verwenden, können nicht weiter in andere Segmente eingeschlossen oder verschachtelt werden. Dies verhindert einen Zyklus, bei dem Segment A Segment B einschließt, das dann versucht, Segment A wieder einzuschließen. Wenn dies auftritt, referenziert das Segment sich selbst weiter, was es unmöglich macht, zu berechnen, wer dazugehört.
<br><br>
Außerdem erhöht das Verschachteln von Segmenten die Komplexität und kann die Verarbeitung verlangsamen. Erstellen Sie stattdessen das Segment, das Sie einschließen möchten, mit denselben Filtern neu.
{% endalert %}

### Ausschlussgruppen (optional) {#exclusion}

Beim Erstellen eines Segments können Sie eine oder mehrere Ausschlussgruppen anwenden. Ausschlussgruppen enthalten Kriterien, die Nutzer:innen identifizieren, die von Ihrem Segment ausgeschlossen werden sollen, und sind immer mit einem „AND NOT“-Operator mit Ihren Filtergruppen verbunden.

Ausschlussgruppen überschreiben Segmentkriterien. Wenn ein:e Nutzer:in die Kriterien Ihrer Ausschlussgruppe erfüllt, wird er/sie nicht Teil Ihres Segments sein, selbst wenn er/sie die Kriterien innerhalb Ihrer Filtergruppen erfüllt.

Erstellen Sie eine Ausschlussgruppe, indem Sie Filter hinzufügen, wie Sie es für Filtergruppen tun würden. Die Statistik *Geschätzte erreichbare Nutzer:innen* in einer Ausschlussgruppe zeigt die geschätzte Anzahl der Nutzer:innen, die nach Anwendung der Ausschlusskriterien in Ihrem Segment verbleiben.

Ausgeschlossene Nutzer:innen werden nicht in der Statistik *Gesamte erreichbare Nutzer:innen* Ihres Segments gezählt.

![Eine Ausschlussgruppe mit zwei Filtern.]({% image_buster /assets/img_archive/segmenter_exclusion_groups.png %})

### Funnel-Statistiken anzeigen {#viewing-funnel-statistics}

Wählen Sie **Funnel-Statistiken anzeigen** aus, um die Statistiken für diese Filtergruppe anzuzeigen und zu sehen, wie sich jeder hinzugefügte Filter auf Ihre Segmentstatistiken auswirkt. Sie sehen eine geschätzte Anzahl und einen Prozentsatz der Nutzer:innen, die von allen Filtern bis zu diesem Punkt angesprochen werden. Sobald die Statistiken für eine Filtergruppe angezeigt werden, aktualisieren sie sich automatisch, wenn Sie die Filter ändern. Diese Statistiken sind Schätzungen und können einen Moment zur Generierung benötigen.

Beachten Sie, dass bei Verwendung von AND zwischen Ihren Filtern die Funnel-Statistiken abnehmen; bei Verwendung von OR zwischen Ihren Filtern nehmen die Funnel-Statistiken zu.

![Zwei Filter mit Segment-Funnel-Statistiken.]({% image_buster /assets/img_archive/segment_funnel_statistics.png %})

Durch das Hinzufügen von Filtern, die Ihren Nutzerfluss dokumentieren, können Sie die Punkte erkennen, an denen Nutzer:innen abspringen. Wenn Sie beispielsweise eine Social-Networking-App betreiben und sehen möchten, wo Sie während Ihres Onboarding-Prozesses möglicherweise Nutzer:innen verlieren, können Sie angepasste Datenfilter für die Registrierung, das Hinzufügen von Freunden und das Senden der ersten Nachricht hinzufügen. Wenn Sie feststellen, dass 85 % der Nutzer:innen sich registrieren und Freunde hinzufügen, aber nur 45 % die erste Nachricht gesendet haben, wissen Sie, dass Sie sich darauf konzentrieren sollten, während Ihres Onboardings und Ihrer Marketing-Campaigns mehr Nachrichtenversand zu fördern.

### Testsegmente {#testing-segments}

Nachdem Sie Apps und Filter zu Ihrem Segment hinzugefügt haben, können Sie testen, ob Ihr Segment wie erwartet eingerichtet ist, indem Sie eine:n Nutzer:in nachschlagen, um zu bestätigen, ob er/sie die Segmentkriterien erfüllt. Suchen Sie dazu nach der `external_id` oder `braze_id` eines/einer Nutzer:in im Abschnitt **Nutzersuche**.

{% alert note %}
Die **Nutzersuche** akzeptiert nur `external_id` und `braze_id`. Sie akzeptiert keine E-Mail-Adressen, Telefonnummern oder andere Bezeichner. Um ein Profil nach E-Mail, Telefonnummer oder anderen Feldern zu finden, verwenden Sie stattdessen [**Nutzer:innen suchen**]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#access-profiles).
{% endalert %}

![Abschnitt „Nutzersuche“ mit einem Suchfeld.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:70%;"}

Die Nutzersuche ist verfügbar bei:
- Erstellen eines Segments
- Einrichten einer Campaign- oder Canvas-Zielgruppe
- Einrichten eines Zielgruppenpfad-Schritts

Wenn ein:e Nutzer:in die Segment-, Filter- und App-Kriterien erfüllt, wird eine Meldung dies bestätigen.

![Eine Nutzersuche nach „testuser“ löst eine Meldung aus, die besagt: „testuser erfüllt alle Segmente, Filter und Apps.“]({% image_buster /assets/img_archive/user_lookup_match.png %})

Wenn ein:e Nutzer:in einen Teil oder alle Segment-, Filter- oder App-Kriterien nicht erfüllt, werden die fehlenden Kriterien zur Fehlerbehebung aufgelistet.

![Eine Nutzersuche mit einer Meldung, die besagt: „test1 erfüllt die folgenden Targeting-Kriterien nicht:“ und fehlende Kriterien anzeigt.]({% image_buster /assets/img_archive/user_lookup_nomatch.png %})

### Einzelnutzer-Segmente {#single-user-segments}

Sie können Einzelnutzer-Segmente (oder Segmente mit einer Handvoll Nutzer:innen) mithilfe eindeutiger Attribute erstellen, die Nutzer:innen identifizieren, wie z. B. ein Nutzername oder eine Nutzer-ID.

Allerdings zeigen die Segmentierungsstatistiken oder die Vorschau diese:n einzelne:n Nutzer:in möglicherweise nicht an, da Segmentstatistiken auf Basis einer Zufallsstichprobe mit einem Konfidenzintervall von 95 % berechnet werden, wobei das Ergebnis innerhalb von +/- 1 % liegt. Je größer Ihre Nutzerbasis ist, desto wahrscheinlicher ist es, dass die Größe Ihres Segments eine grobe Schätzung ist. Um sicherzustellen, dass Ihr Segment die:den einzelne:n Nutzer:in enthält, die/den Sie ansprechen möchten, wählen Sie **Exakte Statistiken berechnen** aus. Dies berechnet die genaue Anzahl der Nutzer:innen in Ihrem Segment mit einer Genauigkeit von mehr als 99,999 %.

Braze bietet Testfilter, um bestimmte Nutzer:innen nach Nutzer-ID oder E-Mail-Adresse anzusprechen.

## Schritt 5: Segment speichern {#step-5-save-your-segment}

Wählen Sie **Save** aus. Jetzt können Sie damit beginnen, Nachrichten an Ihre Nutzer:innen zu senden!

## Segmentgröße messen {#measuring-segment-size}

Informationen zur Überwachung der Mitgliedschaft und Größe Ihres Segments finden Sie unter [Segmentgröße messen]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size).

## Segmente archivieren {#archiving-segments}

Wenn Sie ein bestimmtes Segment nicht mehr benötigen oder außer Betrieb nehmen möchten, können Sie es archivieren, indem Sie zur Seite **Segments** navigieren und im Menü der entsprechenden Segmentzeile **Archivieren** auswählen.

{% alert warning %}
Wenn Sie ein Segment archivieren, werden auch alle Campaigns oder Canvases, die es verwenden (selbst wenn das Segment nur in einer einzelnen Canvas-Komponente verwendet wird), archiviert. Dies gilt auch für verschachtelte Segmente, bei denen sowohl die Segmente als auch alle Campaigns oder Canvases, die sie verwenden, ebenfalls archiviert werden.
<br><br>
Sie erhalten eine Warnung mit einer Auflistung der Campaigns und Canvases, die durch das Archivieren des zugehörigen Segments ebenfalls archiviert werden.
{% endalert %}

Sie können das Segment wieder aus dem Archiv holen, indem Sie auf der Seite **Segments** dorthin navigieren und dann **Dearchivieren** auswählen.

## Targeting-Verhalten bei Nutzer:innen mit mehreren Geräten {#targeting-behavior-when-users-have-multiple-devices}

Nutzer:innen haben mehr als ein Gerät, wenn sie sich auf mehreren Geräten bei demselben Konto anmelden. Sie können im Abschnitt **Letzte Geräte** eines [Nutzerprofils]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles) nach mehreren Geräten suchen.

Wenn Sie mit geräteabhängigen Filtern segmentieren (Gerätemodell, Geräte-Betriebssystem und App-Version), enthält Ihr Segment alle Nutzer:innen, die Ihren Filterkriterien entsprechen. Diese Nutzer:innen erhalten eine Nachricht auf allen ihren Geräten, einschließlich solcher, die Ihre Filterkriterien möglicherweise nicht erfüllen. Nehmen wir zum Beispiel an, Nutzer:in A hat zwei Geräte: Gerät 1 hat Betriebssystem 13.0 und Gerät 2 hat Betriebssystem 10.0. Wenn ein Segment Nutzer:innen mit Betriebssystem 10.0 anspricht, wird diese Person Teil dieses Segments und erhält Nachrichten auf beiden Geräten.

### Push-Benachrichtigungen {#push-notifications}

Sie können festlegen, dass nur eine Push-Benachrichtigung pro Nutzer:in gesendet wird. Wählen Sie beim [Verfassen Ihrer Nachricht]({{site.baseurl}}/user_guide/channels/push/create_a_push_message#step-4-compose-your-push-message) unter **Zusätzliche Einstellungen** die Option **Nur an das zuletzt verwendete Gerät senden** aus.

![„Zusätzliche Einstellungen“ mit einem Kontrollkästchen, um nur an das zuletzt verwendete Gerät zu senden.]({% image_buster /assets/img_archive/send_to_last_device.png %}){: style="max-width:60%;"}

### Überlegungen {#considerations}

- **Die Anzahl gesendeter Nachrichten kann die Zielgruppengröße übersteigen.** Wenn einige Nutzer:innen mehr als ein Gerät haben, kann jedes Gerät eine Nachricht empfangen. Dies führt zu einer höheren Anzahl gesendeter Nachrichten als Nutzer:innen in Ihrem Segment.
- **Die Segmentzugehörigkeit kann anders aussehen als erwartet.**
    - Nutzer:innen können auf ihrem aktuellen Gerät angesprochen werden, basierend auf Attributen, die mit einem anderen Gerät verknüpft sind. Wenn Sie nicht erwartet haben, dass Nutzer:innen eine Nachricht erhalten, überprüfen Sie deren Kundenprofil auf mehrere Geräte.
    - Nutzer:innen waren möglicherweise zum Sendezeitpunkt in Ihrem Zielsegment, gehören aber aufgrund von Verhaltensweisen, die mit einem ihrer Geräte verknüpft sind, danach nicht mehr zu diesem Segment. Dies kann dazu führen, dass Nutzer:innen eine Campaign oder ein Canvas erhalten, obwohl sie die Filterkriterien aktuell nicht erfüllen. <br><br>Zum Beispiel könnten Nutzer:innen eine Nachricht erhalten, die auf die neueste App-Version mit Betriebssystem 10.0 abzielt, obwohl sie aktuell Betriebssystem 13.0 haben. In diesem Fall hatten die Nutzer:innen Betriebssystem 10.0, als die Nachricht gesendet wurde, und haben danach auf Betriebssystem 13.0 aktualisiert.<br><br> Ebenso wird das Kundenprofil mit einer neuen aktuellen App-Version aktualisiert, wenn Nutzer:innen später ein Gerät mit einer anderen App-Version verwenden. Dies kann den Eindruck erwecken, dass die Nutzer:innen sich nicht für die Nachricht hätten qualifizieren sollen, obwohl sie zum Sendezeitpunkt qualifiziert waren.