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

## 1. Schritt: Zum Bereich „Segmente“ navigieren {#step-1-navigate-to-the-segments-section}

Gehen Sie zu **Audience** > **Segments**.

## 2. Schritt: Segment benennen {#step-2-name-your-segment}

Wählen Sie **Segment erstellen**, um mit der Erstellung Ihres Segments zu beginnen. Benennen Sie Ihr Segment, indem Sie den Typ der Nutzer:innen beschreiben, nach denen Sie filtern möchten. So können Sie das Segment leichter identifizieren, wenn Sie es für Ihre Campaigns oder Canvases als Zielgruppe verwenden möchten. Vage Segmenttitel können verwirrend sein.

Optional können Sie Folgendes tun:
- Eine Beschreibung zum Segment hinzufügen, um weitere Details zur Absicht dieser Zielgruppe bereitzustellen und Notizen für andere Teammitglieder zu hinterlassen.
- Ein [Team]({{site.baseurl}}/user_guide/administer/global/user_management/teams) zu Ihrem Segment hinzufügen.
- [Tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) zu Ihrem Segment hinzufügen, um es besser zu organisieren.

![Modal „Segment erstellen“, in dem das Segment „Lapsed Users“ benannt ist, mit der Segmentbeschreibung „This is our main Lapsed User segment to target non-actives within the past fourteen days.“ und zwei Buttons: „Abbrechen“ und „Segment erstellen“.]({% image_buster /assets/img_archive/segment_app_selection.png %}){: style="max-width:80%;"}

## 3. Schritt: App oder Plattform auswählen {#step-3-choose-your-app-or-platform}

Wählen Sie aus, welche Apps oder Plattformen Sie ansprechen möchten, indem Sie **Users from all apps** (Standard) oder **Users from specific apps** auswählen. **Users from specific apps** richtet sich an Nutzer:innen mit mindestens einer Sitzung in den angegebenen Apps.

Wenn Sie beispielsweise eine In-App-Nachricht nur an iOS-Geräte senden möchten, wählen Sie Ihre iOS-App aus. So wird sichergestellt, dass Nutzer:innen, die möglicherweise sowohl ein iOS- als auch ein Android-Gerät verwenden, die Nachricht nur auf ihrem iOS-Gerät erhalten. In der Liste der spezifischen Apps können Sie mit der Option **Users from no apps** Nutzer:innen ohne Sitzungen und ohne App-Daten einschließen (die in der Regel über Nutzerimport oder REST API erstellt wurden).

![Panel „Segmentdetails“ mit der ausgewählten Option „Users from all apps“ im Abschnitt „Apps Used“.]({% image_buster /assets/img_archive/Segment2.png %}){: style="max-width:80%;"}

## 4. Schritt: Filter zu Ihrem Segment hinzufügen {#step-4-add-filters-to-your-segment}

Fügen Sie mindestens einen Filter zu Ihrem Segment hinzu. Sie können beliebig viele Filter kombinieren, um Ihre Segmentierung präziser zu gestalten.

{% multi_lang_include alerts/note_alerts.md alert='Segment profiles first app use' %}

### Filtergruppen {#filter-groups}

Filter sind in Filtergruppen organisiert. Jeder Filter muss Teil einer Filtergruppe sein, die mindestens einen Filter enthält. Ein Segment kann mehrere Filtergruppen haben. Um eine hinzuzufügen, wählen Sie **Filtergruppe hinzufügen**. Bearbeiten Sie den Namen der Filtergruppe, indem Sie auf das Symbol klicken, das erscheint, wenn Sie mit der Maus darüber fahren.

![Filtergruppe mit einem Bearbeitungssymbol neben ihrem Namen.]({% image_buster /assets/img_archive/edit_filter_group_name.png %})

Wählen Sie die Symbole neben jedem Filter, um den Filtereditor ein- oder auszuklappen oder einzelne Filter zu duplizieren. Nach dem Duplizieren eines Filters können Sie seine Werte in jedem Dropdown anpassen.

### Segmentierungslogik mit AND und OR {#segmentation-logic-using-and-and-or}

Innerhalb einer Filtergruppe können Filter entweder mit „AND“ oder „OR“ verknüpft werden. Zwischen Filtergruppen können Gruppen ebenfalls mit „AND“ oder „OR“ verknüpft werden. Mit Filtergruppen können Sie Segmentierungslogik wie die folgende erstellen:
- (A AND B AND C) OR (C AND E AND F)
- (A OR B OR C) AND (C OR D OR F)

Wenn Sie „OR“ für Ihre Filter auswählen, enthält Ihr Segment Nutzer:innen, die eine beliebige Kombination aus einem, einigen oder allen dieser Filter erfüllen. Wenn Sie „AND“ auswählen, werden Nutzer:innen, die diesen Filter nicht erfüllen, nicht in Ihr Segment aufgenommen.

{% alert tip %}
Wenn Sie „OR“ für Filter auswählen, die einen negativen Filter enthalten (z. B. „ist nicht“ in einer Abo-Gruppe), denken Sie daran, dass Nutzer:innen nur einen der „OR“-Filter erfüllen müssen, um in das Segment aufgenommen zu werden. Um den negativen Filter unabhängig von den anderen Filtern anzuwenden, verwenden Sie eine [Ausschlussgruppe](#exclusion).
{% endalert %}

{% details Wann der OR-Operator vermieden werden sollte %}

Es gibt Situationen beim Nutzer-Targeting, in denen der `OR`-Operator vermieden werden sollte. Der `OR`-Operator erstellt eine Aussage, die als wahr ausgewertet wird, wenn ein:e Nutzer:in die Kriterien für einen oder mehrere der Filter in einer Aussage erfüllt. Wenn Sie beispielsweise ein Segment von Nutzer:innen erstellen möchten, die zu „Foodies“ gehören, aber weder zu „Non-foodies“ noch zu „Candy-lovers“, dann würde der `OR`-Operator hier funktionieren.

![Filtergruppe für Nutzer:innen im Segment „foodies“, die nicht in den Segmenten „non-foodies“ oder „candy-lovers“ sind.]({% image_buster /assets/img_archive/or_operator_segment.png %})

Wenn Ihr Ziel jedoch darin besteht, Nutzer:innen zu segmentieren, die zum Segment „Foodies“ gehören und gleichzeitig nicht in den Segmenten „Non-foodies“ und „Candy-lovers“ sind, dann verwenden Sie den `AND`-Operator. Auf diese Weise befinden sich Nutzer:innen, die die Campaign oder das Canvas erhalten, im beabsichtigten Segment („foodies“) und gleichzeitig nicht in den anderen Segmenten („Non-foodies“ und „Candy-lovers“).

Die folgenden negativen Targeting-Kriterien sollten nicht mit dem `OR`-Operator verwendet werden, wenn zwei oder mehr Filter dasselbe Attribut referenzieren:

- `not included`
- `is not`
- `does not equal`
- `does not match regex`

Wenn `not included`, `is not`, `does not equal` oder `does not match regex` mit dem `OR`-Operator zwei oder mehr Mal in einer Aussage verwendet werden, werden Nutzer:innen mit allen Werten für das relevante Attribut angesprochen.

{% enddetails %}

### Filteroperatoren {#filter-operators}

Je nach dem spezifischen Filter, den Sie auswählen, stehen Ihnen verschiedene Operatoren zur Identifizierung von Filterwerten zur Verfügung. Um tiefer in die verfügbaren Operatoren für verschiedene Typen angepasster Attribute einzutauchen, lesen Sie [Speicherung angepasster Attribute]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes#setting-custom-attributes). Beachten Sie, dass bei Verwendung des Operators „is any of“ die maximale Anzahl von Elementen, die Sie in dieses Feld aufnehmen können, 256 beträgt.

{% alert note %}
Braze erstellt keine Profile für Nutzer:innen, bis diese die App zum ersten Mal verwendet haben. Daher können Sie keine Nutzer:innen ansprechen, die Ihre App noch nicht geöffnet haben.
{% endalert %}

![Segmenter-Filtergruppen mit dem AND-Operator.]({% image_buster /assets/img_archive/segmenter_filter_groups.png %})

{% alert important %}
Segmente, die bereits den Filter **Segmentzugehörigkeit** verwenden, können nicht weiter in andere Segmente eingeschlossen oder verschachtelt werden. Dies verhindert einen Zyklus, bei dem Segment A Segment B einschließt, das dann versucht, Segment A wieder einzuschließen. Wenn das passieren würde, würde das Segment sich ständig selbst referenzieren, was es unmöglich macht, zu berechnen, wer tatsächlich dazugehört.

Außerdem erhöht die Verschachtelung von Segmenten die Komplexität und kann die Verarbeitung verlangsamen. Erstellen Sie stattdessen das Segment, das Sie einschließen möchten, mit denselben Filtern neu.
{% endalert %}

### Ausschlussgruppen (optional) {#exclusion}

Beim Erstellen eines Segments können Sie eine oder mehrere Ausschlussgruppen anwenden. Ausschlussgruppen enthalten Kriterien, die Nutzer:innen identifizieren, die von Ihrem Segment ausgeschlossen werden sollen, und sind immer mit einem „AND NOT“-Operator mit Ihren Filtergruppen verbunden.

Ausschlussgruppen überschreiben Segmentkriterien. Wenn ein:e Nutzer:in die Kriterien Ihrer Ausschlussgruppe erfüllt, wird er/sie nicht Teil Ihres Segments sein, selbst wenn er/sie die Kriterien innerhalb Ihrer Filtergruppen erfüllt.

Erstellen Sie eine Ausschlussgruppe, indem Sie Filter hinzufügen, wie Sie es für Filtergruppen tun würden. Die Statistik *Geschätzte erreichbare Nutzer:innen* in einer Ausschlussgruppe zeigt die geschätzte Anzahl der Nutzer:innen, die nach Anwendung der Ausschlusskriterien in Ihrem Segment verbleiben.

Ausgeschlossene Nutzer:innen werden nicht in der Statistik *Gesamte erreichbare Nutzer:innen* Ihres Segments gezählt.

![Eine Ausschlussgruppe mit zwei Filtern.]({% image_buster /assets/img_archive/segmenter_exclusion_groups.png %})

### Funnel-Statistiken anzeigen {#viewing-funnel-statistics}

Wählen Sie **Funnel-Statistiken anzeigen**, um die Statistiken für diese Filtergruppe anzuzeigen und zu sehen, wie sich jeder hinzugefügte Filter auf Ihre Segmentstatistiken auswirkt. Sie sehen eine geschätzte Anzahl und einen Prozentsatz der Nutzer:innen, die von allen Filtern bis zu diesem Punkt angesprochen werden. Sobald die Statistiken für eine Filtergruppe angezeigt werden, aktualisieren sie sich automatisch, wenn Sie die Filter ändern. Diese Statistiken sind Schätzungen und können einen Moment zur Generierung benötigen.

Beachten Sie, dass bei Verwendung von AND zwischen Ihren Filtern die Funnel-Statistiken abnehmen; bei Verwendung von OR zwischen Ihren Filtern nehmen die Funnel-Statistiken zu.

![Zwei Filter mit Segment-Funnel-Statistiken.]({% image_buster /assets/img_archive/segment_funnel_statistics.png %})

Durch das Hinzufügen von Filtern, die Ihren Nutzerfluss dokumentieren, können Sie die Punkte erkennen, an denen Nutzer:innen abspringen. Wenn Sie beispielsweise eine Social-Networking-App betreiben und sehen möchten, wo Sie während Ihres Onboarding-Prozesses Nutzer:innen verlieren, können Sie angepasste Datenfilter für die Registrierung, das Hinzufügen von Freunden und das Senden der ersten Nachricht hinzufügen. Wenn Sie feststellen, dass 85 % der Nutzer:innen sich registrieren und Freunde hinzufügen, aber nur 45 % die erste Nachricht gesendet haben, wissen Sie, dass Sie sich darauf konzentrieren sollten, während Ihres Onboardings und Ihrer Marketing-Kampagnen mehr Nachrichtenversand zu fördern.

### Segmente testen {#testing-segments}

Nachdem Sie Apps und Filter zu Ihrem Segment hinzugefügt haben, können Sie testen, ob Ihr Segment wie erwartet eingerichtet ist, indem Sie eine:n Nutzer:in nachschlagen, um zu bestätigen, ob er/sie die Segmentkriterien erfüllt. Suchen Sie dazu nach der `external_id` oder `braze_id` eines/einer Nutzer:in im Abschnitt **User Lookup**.

{% alert note %}
**User Lookup** akzeptiert nur `external_id` und `braze_id`. E-Mail-Adressen, Telefonnummern oder andere Bezeichner werden nicht akzeptiert. Um ein Profil anhand von E-Mail, Telefonnummer oder anderen Feldern zu finden, verwenden Sie stattdessen [**Nutzer:innen suchen**]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#access-profiles).
{% endalert %}

![Abschnitt „User Lookup“ mit einem Suchfeld.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:70%;"}

User Lookup ist verfügbar bei:
- Erstellen eines Segments
- Einrichten einer Campaign- oder Canvas-Zielgruppe
- Einrichten eines Zielgruppenpfad-Schritts

Wenn ein:e Nutzer:in die Segment-, Filter- und App-Kriterien erfüllt, wird eine entsprechende Meldung angezeigt.

![Ein User Lookup für „testuser“ löst eine Meldung aus, die besagt: „testuser matches all of the segments, filters, and apps.“]({% image_buster /assets/img_archive/user_lookup_match.png %})

Wenn ein:e Nutzer:in einen Teil oder alle Segment-, Filter- oder App-Kriterien nicht erfüllt, werden die fehlenden Kriterien zur Fehlerbehebung aufgelistet.

![Ein User Lookup mit einer Meldung, die besagt: „test1 does not match the following targeting criteria:“ und die fehlenden Kriterien anzeigt.]({% image_buster /assets/img_archive/user_lookup_nomatch.png %})

### Einzelnutzer-Segmente {#single-user-segments}

Sie können Einzelnutzer-Segmente (oder Segmente mit einer Handvoll Nutzer:innen) mithilfe eindeutiger Attribute erstellen, die Nutzer:innen identifizieren, wie z. B. ein Nutzername oder eine Nutzer-ID.

Allerdings zeigen die Segmentierungsstatistiken oder die Vorschau diese:n einzelne:n Nutzer:in möglicherweise nicht an, da Segmentstatistiken auf Basis einer Zufallsstichprobe mit einem Konfidenzintervall von 95 % berechnet werden, wobei das Ergebnis innerhalb von +/- 1 % liegt. Je größer Ihre Nutzerbasis ist, desto wahrscheinlicher ist es, dass die Größe Ihres Segments eine grobe Schätzung ist. Um sicherzustellen, dass Ihr Segment die einzelne Person enthält, die Sie ansprechen möchten, wählen Sie **Exakte Statistiken berechnen**. Dadurch wird die genaue Anzahl der Nutzer:innen in Ihrem Segment mit einer Genauigkeit von mehr als 99,999 % berechnet.

Braze bietet Testfilter, um bestimmte Nutzer:innen anhand der Nutzer-ID oder E-Mail-Adresse anzusprechen.

## 5. Schritt: Segment speichern {#step-5-save-your-segment}

Wählen Sie **Speichern**. Jetzt können Sie damit beginnen, Nachrichten an Ihre Nutzer:innen zu senden!

## Segmentgröße messen {#measuring-segment-size}

Informationen zur Überwachung der Zugehörigkeit und Größe Ihres Segments finden Sie unter [Segmentgröße messen]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size).

## Segmente archivieren {#archiving-segments}

Wenn Sie ein bestimmtes Segment nicht mehr benötigen oder außer Betrieb nehmen möchten, können Sie es archivieren, indem Sie zur Seite **Segments** gehen und **Archivieren** aus dem Menü in der Zeile dieses Segments auswählen.

{% alert warning %}
Wenn Sie ein Segment archivieren, werden auch alle Campaigns oder Canvases, die es verwenden (selbst wenn das Segment nur in einer einzelnen Canvas-Komponente verwendet wird), archiviert. Dies gilt auch für verschachtelte Segmente, bei denen sowohl die Segmente als auch alle Campaigns oder Canvases, die sie verwenden, ebenfalls archiviert werden.
<br><br>
Sie erhalten eine Warnung, die auflistet, welche Campaigns und Canvases durch das Archivieren des zugehörigen Segments ebenfalls archiviert werden.
{% endalert %}

Sie können das Segment dearchivieren, indem Sie auf der Seite **Segments** dorthin navigieren und dann **Dearchivieren** auswählen.

## Targeting-Verhalten bei Nutzer:innen mit mehreren Geräten {#targeting-behavior-when-users-have-multiple-devices}

Nutzer:innen haben mehr als ein Gerät, wenn sie sich auf mehreren Geräten bei demselben Konto anmelden. Sie können im Abschnitt **Letzte Geräte** eines [Nutzerprofils]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles) nach mehreren Geräten suchen.

Bei der Segmentierung mit geräteabhängigen Filtern (Gerätemodell, Geräte-OS und App-Version) enthält Ihr Segment alle Nutzer:innen, die Ihre Filterkriterien erfüllen. Diese Nutzer:innen erhalten eine Nachricht auf allen ihren Geräten, einschließlich solcher, die Ihre Filterkriterien möglicherweise nicht erfüllen. Nehmen wir beispielsweise an, Nutzer:in A hat zwei Geräte: Gerät 1 hat OS 13.0 und Gerät 2 hat OS 10.0. Wenn ein Segment Nutzer:innen mit OS 10.0 anspricht, wird diese:r Nutzer:in Teil dieses Segments sein und Nachrichten auf beiden Geräten erhalten.

### Push-Benachrichtigungen {#push-notifications}

Sie können festlegen, dass nur eine Push-Benachrichtigung pro Nutzer:in gesendet wird. Wenn Sie [Ihre Nachricht verfassen]({{site.baseurl}}/user_guide/channels/push/create_a_push_message#step-4-compose-your-push-message), wählen Sie unter **Zusätzliche Einstellungen** die Option **Nur an das zuletzt verwendete Gerät des/der Nutzer:in senden**.

![„Zusätzliche Einstellungen“ mit einem Kontrollkästchen, um nur an das zuletzt verwendete Gerät des/der Nutzer:in zu senden.]({% image_buster /assets/img_archive/send_to_last_device.png %}){: style="max-width:60%;"}

### Hinweise {#considerations}

- **Gesendete Nachrichten können die Zielgruppengröße übersteigen.** Wenn einige Nutzer:innen mehr als ein Gerät haben, kann jedes Gerät eine Nachricht erhalten. Dies führt zu einer höheren Anzahl gesendeter Nachrichten als Nutzer:innen in Ihrem Segment.
- **Die Segmentzugehörigkeit eines/einer Nutzer:in sieht möglicherweise nicht so aus, wie Sie es erwarten würden.**
    - Ein:e Nutzer:in kann auf seinem/ihrem aktuellen Gerät basierend auf Attributen angesprochen werden, die mit einem anderen Gerät verknüpft sind. Wenn Sie nicht erwartet haben, dass ein:e Nutzer:in eine Nachricht erhält, überprüfen Sie sein/ihr Nutzerprofil auf mehrere Geräte.
    - Ein:e Nutzer:in war möglicherweise zum Sendezeitpunkt in Ihrem Zielsegment, gehört aber aufgrund von Verhaltensweisen, die mit einem seiner/ihrer Geräte verbunden sind, danach möglicherweise nicht mehr zu diesem Segment. Dies kann dazu führen, dass ein:e Nutzer:in eine Campaign oder ein Canvas erhält, obwohl er/sie die Filterkriterien derzeit nicht erfüllt. <br><br>Beispielsweise könnte ein:e Nutzer:in eine Nachricht erhalten, die auf Nutzer:innen mit der neuesten App-Version OS 10.0 abzielt, obwohl er/sie derzeit OS 13.0 hat. In diesem Fall hatte der/die Nutzer:in OS 10.0, als die Nachricht gesendet wurde, und hat danach auf OS 13.0 aktualisiert.<br><br> Wenn ein:e Nutzer:in später ein Gerät mit einer anderen App-Version verwendet, wird sein/ihr Nutzerprofil mit einer neuen aktuellen App-Version aktualisiert. Dies könnte den Eindruck erwecken, dass der/die Nutzer:in sich nicht für die Nachricht hätte qualifizieren sollen, obwohl er/sie sich zum Sendezeitpunkt qualifiziert hatte.