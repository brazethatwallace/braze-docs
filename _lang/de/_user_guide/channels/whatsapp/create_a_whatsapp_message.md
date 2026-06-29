---
nav_title: WhatsApp-Nachricht erstellen
article_title: WhatsApp-Nachricht erstellen
page_order: 1
description: "Dieser Referenzartikel behandelt die Schritte zum Erstellen und Verfassen einer WhatsApp-Nachricht."
page_type: reference
tool:
  - Campaigns
channel:
  - WhatsApp
search_rank: 1
---

# WhatsApp-Nachricht erstellen {#create-a-whatsapp-message}

> WhatsApp-Kampagnen eignen sich hervorragend, um Ihre Kund:innen direkt zu erreichen und programmatisch mit ihnen zu kommunizieren. Sie können Liquid und andere dynamische Inhalte nutzen, um ein persönliches Erlebnis für Ihre Nutzer:innen zu schaffen und eine Umgebung zu fördern, die ein unaufdringliches Nutzererlebnis mit Ihrer Marke unterstützt und verbessert.

## Voraussetzungen {#prerequisites}

Bevor Sie WhatsApp-Nachrichten erstellen können, müssen Sie die folgenden Punkte aus der [WhatsApp-Übersicht]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/) überprüfen und abschließen:
  - Richtlinien, Limits und Inhaltsregeln bestätigen
  - Ihre WhatsApp-Verbindung einrichten
  - Erste Templates in Meta erstellen, die Sie in Ihren Nachrichten verwenden möchten

## Nachricht erstellen {#creating-a-message}

### 1. Schritt: Wählen Sie, wo Sie Ihre Nachricht erstellen möchten {#step-1-choose-where-to-build-your-message}

{% alert note %}
WhatsApp erstellt unterschiedliche [Nachrichten-Templates](#template-messages) für jede Sprache. Erstellen Sie entweder eine Kampagne pro Sprache mit Segmentierung, um den Nutzer:innen das richtige Template zuzustellen, oder verwenden Sie Canvas.
{% endalert %}

Sind Sie unsicher, ob Ihre Nachricht über eine Kampagne oder ein Canvas gesendet werden sollte? Campaigns eignen sich besser für einzelne, gezielte Messaging-Kampagnen, während Canvases besser für mehrstufige User-Journeys geeignet sind.

{% tabs %}
{% tab Campaign %}

**Schritte:**

1. Gehen Sie zur Seite **Campaigns** und klicken Sie auf <i class="fas fa-plus"></i> **Kampagne erstellen**.
2. Wählen Sie **WhatsApp** oder, für Campaigns, die mehrere Kanäle ansprechen, **Multichannel Campaign**.
3. Geben Sie Ihrer Kampagne einen klaren und aussagekräftigen Namen.
4. Fügen Sie nach Bedarf [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams/) und [Tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags/) hinzu.
   * Tags erleichtern das Auffinden Ihrer Campaigns und das Erstellen von Berichten. Wenn Sie beispielsweise den [Berichts-Builder]({{site.baseurl}}/user_guide/analytics/reports/report_builder/) verwenden, können Sie nach bestimmten Tags filtern.
5. Fügen Sie so viele Varianten hinzu und benennen Sie sie, wie Sie für Ihre Kampagne benötigen. Sie können für jede hinzugefügte Variante unterschiedliche Plattformen, Nachrichtentypen und Layouts wählen. Weitere Informationen zu diesem Thema finden Sie unter [Multivariate und A/B-Tests]({{site.baseurl}}/user_guide/messaging/ab_testing/).

{% alert tip %}
Wenn alle Nachrichten in Ihrer Kampagne ähnlich sind oder denselben Inhalt haben, verfassen Sie Ihre Nachricht, bevor Sie zusätzliche Varianten hinzufügen. Anschließend können Sie im Dropdown **Variante hinzufügen** die Option **Von Variante kopieren** wählen.
{% endalert %}

{% endtab %}
{% tab Canvas %}

**Schritte:**

1. [Erstellen Sie Ihr Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/) mit dem Canvas-Composer.
2. Nachdem Sie Ihr Canvas eingerichtet haben, fügen Sie im Canvas-Builder einen Schritt hinzu. Geben Sie Ihrem Schritt einen klaren und aussagekräftigen Namen.
3. Wählen Sie einen [Schritt-Zeitplan]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types/#schedule-delay) und legen Sie bei Bedarf eine Verzögerung fest.
4. Filtern Sie die Zielgruppe für diesen Schritt nach Bedarf. Sie können die Empfänger:innen dieses Schritts weiter eingrenzen, indem Sie Segmente angeben und zusätzliche Filter hinzufügen. Die Zielgruppenoptionen werden nach der Verzögerung zum Zeitpunkt des Nachrichtenversands überprüft.
5. Wählen Sie Ihr [Fortschrittsverhalten]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases/).
6. Wählen Sie alle weiteren Messaging-Kanäle, die Sie mit Ihrer Nachricht kombinieren möchten.

{% alert tip %}
Wenn ein aktionsbasiertes Canvas durch eine eingehende WhatsApp-Nachricht getriggert wird, können Sie in jedem Canvas-Schritt bis zum nächsten Aktions-Pfad auf WhatsApp-Eigenschaften verweisen.
{% endalert %}

{% endtab %}
{% endtabs %}

### 2. Schritt: Verfassen Sie Ihre WhatsApp-Nachricht {#step-2-compose-your-whatsapp-message}

Wählen Sie, ob Sie eine WhatsApp-[Template-Nachricht](#template-messages) oder eine Antwortnachricht erstellen möchten, je nach Ihrem Anwendungsfall. Jede vom Unternehmen initiierte Konversation muss mit einem genehmigten Template beginnen, während Antwortnachrichten als Antworten auf eingehende Nachrichten von Nutzer:innen innerhalb eines 24-Stunden-Fensters verwendet werden können.

![Der Bereich „Nachrichtenvarianten“ ermöglicht die Auswahl einer Abo-Gruppe und eines von zwei Nachrichtentypen: WhatsApp-Template-Nachricht und Antwortnachricht.]({% image_buster /assets/img/whatsapp/whatsapp_message_variants.png %}){: style="max-width:80%;"}

{% tabs %}
{% tab Template-Nachrichten %}

Sie können [genehmigte WhatsApp-Template-Nachrichten]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/#step-3-create-whatsapp-templates
) verwenden, um Konversationen mit Ihren Nutzer:innen auf WhatsApp zu initiieren. Diese Nachrichten werden vorab zur Inhaltsgenehmigung an WhatsApp übermittelt, was bis zu 24 Stunden dauern kann. Alle Änderungen, die Sie am Text vornehmen, müssen bearbeitet und erneut bei WhatsApp eingereicht werden.

Deaktivierte Textfelder (grau hervorgehoben) können nicht bearbeitet werden, da sie Teil des genehmigten WhatsApp-Templates sind. Um Aktualisierungen am deaktivierten Text vorzunehmen, müssen Sie Ihr Template bearbeiten und erneut genehmigen lassen.

#### Sprachen {#languages}

Jedes Template hat eine zugewiesene Sprache, daher müssen Sie für jede Sprache eine Kampagne oder einen Canvas-Schritt erstellen, um die Nutzer:innen korrekt zuzuordnen. Wenn Sie beispielsweise ein Canvas erstellen, das Templates für Indonesisch und Englisch verwendet, müssen Sie einen Canvas-Schritt für das indonesische Template und einen Canvas-Schritt für das englische Template erstellen.

![Liste von Templates mit Vorschauen ihrer Nachrichten, ihren zugewiesenen Sprachen und ihrem Genehmigungsstatus.]({% image_buster /assets/img/whatsapp/whatsapp_templates.png %}){: style="max-width:80%;"}

Wenn Sie Text in einer Sprache hinzufügen, die von rechts nach links geschrieben wird, beachten Sie, dass das endgültige Erscheinungsbild von Rechts-nach-links-Nachrichten weitgehend davon abhängt, wie Dienstanbieter sie darstellen. Best Practices zum Erstellen von Rechts-nach-links-Nachrichten, die so genau wie möglich angezeigt werden, finden Sie unter [Rechts-nach-links-Nachrichten erstellen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages/).

#### Variablen {#variables}

Wenn Sie beim Erstellen des WhatsApp-Templates im Meta Business Manager Variablen hinzugefügt haben, werden diese Variablen als Leerfelder im Nachrichten-Editor angezeigt. Ersetzen Sie diese Leerfelder durch Liquid oder Klartext. Um Klartext zu verwenden, nutzen Sie das Format „Text hier“ in doppelten geschweiften Klammern. Wenn Sie sich beim Erstellen Ihres Templates für die Einbindung von Bildern entschieden haben, können Sie Bilder hochladen oder aus der Medienbibliothek hinzufügen oder eine Bild-URL referenzieren. Wir empfehlen nach Möglichkeit, Bilder direkt in Ihre Medienbibliothek hochzuladen, um Konsistenz und Zuverlässigkeit sicherzustellen.

Beachten Sie, dass deaktivierte Textfelder (grau hervorgehoben) nicht bearbeitet werden können, da sie Teil des genehmigten WhatsApp-Templates sind. Wenn Sie Aktualisierungen am deaktivierten Text vornehmen möchten, müssen Sie Ihr Template bearbeiten und erneut genehmigen lassen.

{% alert tip %}
{% raw %}
Wenn Sie Liquid verwenden möchten, stellen Sie sicher, dass Sie einen Standardwert für Ihre gewählte Personalisierung angeben, damit im Falle eines unvollständigen Nutzerprofils der Empfänger:in keine Nachricht mit fehlenden Variablen gesendet wird. Nachrichten mit fehlenden Liquid-Variablen werden von WhatsApp nicht gesendet.
{% endraw %}
{% endalert %}

![Das Tool „Personalisierung hinzufügen“ mit dem Attribut „first_name“ und dem Standardwert „you“.]({% image_buster /assets/img/whatsapp/whatsapp7.png %}){: style="max-width:80%;"}

### Dynamische Links {#dynamic-links}

Call-to-Action-URLs können Variablen enthalten, wobei Meta verlangt, dass diese am Ende der URL stehen, z. B. `{% raw %}https://example.com/{{variable}}{% endraw %}`, wobei die Variable dann in Braze durch Liquid ersetzt werden kann. Links können auch als Fließtext im Template-Body eingefügt werden. Beide Arten von Links können mit [Klick-Tracking]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/click_tracking/) gekürzt und getrackt werden.

### Dynamische Bilder {#dynamic-images}

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% endtab %}
{% tab Antwortnachrichten %}

Sie können Antwortnachrichten verwenden, um auf eingehende Nachrichten Ihrer Nutzer:innen zu antworten. Diese Nachrichten werden in Braze während des Verfassens erstellt und können jederzeit bearbeitet werden. Sie können Liquid verwenden, um die Sprache der Antwortnachricht den entsprechenden Nutzer:innen zuzuordnen.

Es gibt fünf Layouts für Antwortnachrichten:
- Schnellantwort
- Textnachricht
- Mediennachricht
- Call-to-Action-Button
- Listennachricht

![Der Antwortnachrichten-Composer für eine Antwortnachricht, die neue Nutzer:innen mit einem Rabattcode begrüßt.]({% image_buster /assets/img/whatsapp/whatsapp_response_messages.png %}){: style="max-width:80%;"}

{% endtab %}
{% endtabs %}

### 3. Schritt: Vorschau und Test Ihrer Nachricht {#step-3-preview-and-test-your-message}

Braze empfiehlt immer, Ihre Nachricht vor dem Senden in der Vorschau anzuzeigen und zu testen. Wechseln Sie zum Tab **Test**, um eine Test-WhatsApp-Nachricht an [Inhalts-Testgruppen]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups/#content-test-groups) oder einzelne Nutzer:innen zu senden, oder zeigen Sie die Nachricht direkt in Braze als Nutzer:in in der Vorschau an.

![Eine Vorschaunachricht für eine:n benutzerdefinierte:n Nutzer:in namens Max.]({% image_buster /assets/img/whatsapp/whatsapp8.png %}){: style="max-width:80%;"}

{% alert note %}
Zum Senden von Antwortnachrichten, einschließlich Testnachrichten, ist ein Konversationsfenster erforderlich. Um ein Konversationsfenster zu öffnen, senden Sie eine WhatsApp-Nachricht an die Telefonnummer, die der Abo-Gruppe zugeordnet ist, die Sie für diese Nachricht verwenden. Die zugehörige Telefonnummer wird im Hinweis auf dem Tab **Test** angezeigt.
{% endalert %}

![Ein Hinweis, der besagt, dass Sie ein Nachrichtenfenster öffnen sollen, indem Sie eine WhatsApp-Nachricht senden, und dann die Nachricht an die:den Testnutzer:in senden.]({% image_buster /assets/img/whatsapp/whatsapp_test_phone_number.png %}){: style="max-width:70%;"}

Weitere Informationen finden Sie unter [Testnachrichten senden]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages/?tab=whatsapp).

### 4. Schritt: Testergebnisse anzeigen {#step-4-view-test-send-results}

Nach dem Senden einer Test-WhatsApp-Nachricht können Sie einen detaillierten Zustellungsbericht direkt im Nachrichten-Editor einsehen. So können Sie bestätigen, dass Ihre Nachricht die beabsichtigten Empfänger:innen erreicht hat, und Fehler vor dem Start beheben.

Der Button **Testergebnisse anzeigen** wird angezeigt, wenn Testversanddaten für die aktuelle Kampagne oder den aktuellen Canvas-Schritt verfügbar sind. Wählen Sie ihn aus, um das Ergebnis-Panel zu öffnen.

Das Ergebnis-Panel zeigt jede Phase, die Ihre Nachricht auf dem Weg zur Empfänger:in durchlaufen hat:
- **Braze:** Ob Braze die Nachricht erfolgreich verarbeitet und versendet hat
- **Meta:** Ob Meta die Nachricht zur Zustellung akzeptiert hat
- **Nutzergerät:** Ob die Nachricht auf dem Gerät der Empfänger:in zugestellt wurde

Jede Phase zeigt ihren aktuellen Status an. Wenn eine Phase fehlgeschlagen ist, zeigt das Panel den aufgetretenen Fehler und eine Anleitung zur Behebung an. Die Ergebnisse bleiben erhalten, wenn Sie dieselbe Kampagne oder dasselbe Canvas schließen und erneut öffnen.

![Testergebnis-Panel mit zwei erfolgreichen Testversendungen und einer fehlgeschlagenen Testversendung.]({% image_buster /assets/img/whatsapp/whatsapp_test_results.png %}){: style="max-width:80%;"}

#### Wiederholungsversuche und frühere Versuche {#retries-and-past-attempts}

Wenn ein Testversand fehlschlägt, wiederholt Braze die Zustellung automatisch bis zu 24 Stunden lang. Das Ergebnis-Panel spiegelt dies mit zwei Tabs wider:

- **Aktuell:** Der letzte Zustellungsversuch, der in Echtzeit aktualisiert wird, wenn Wiederholungsversuche stattfinden
- **Frühere Versuche:** Ein Verlauf früherer Wiederholungsversuche, jeweils mit den Phasenstatus und aufgetretenen Fehlern

Wenn das endgültige Ergebnis feststeht (erfolgreiche Zustellung, erschöpfte Wiederholungsversuche oder ein Fehler, den Wiederholungsversuche nicht beheben können), werden die Tabs in **Ergebnis** und **Wiederholungsverlauf** umbenannt.

{% alert note %}
Da Wiederholungsversuche bis zu 24 Stunden andauern können, sehen Sie möglicherweise nicht sofort nach einem fehlgeschlagenen Versand ein endgültiges Ergebnis.
{% endalert %}

#### Fehler beheben {#troubleshoot-failures}

Wenn eine Phase einen Fehler anzeigt, zeigt das Panel den Fehler und empfohlene nächste Schritte an. Häufige Gründe, warum ein Testversand fehlschlagen kann, sind:

- Das Nachrichten-Template ist in Meta pausiert oder noch nicht genehmigt
- Die Telefonnummer der Empfänger:in ist ratenbegrenzt
- Liquid-Variablen in der Nachricht wurden für die:den ausgewählte:n Testnutzer:in nicht befüllt

Bei anhaltenden Problemen überprüfen Sie den Template-Status im Meta Business Manager oder stellen Sie sicher, dass Ihre:Ihr Testempfänger:in die erforderlichen Nutzerattribute in Braze hinterlegt hat.

### 5. Schritt: Erstellen Sie den Rest Ihrer Kampagne oder Ihres Canvas {#step-5-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

Erstellen Sie als Nächstes den Rest Ihrer Kampagne. In den folgenden Abschnitten finden Sie weitere Details zur optimalen Nutzung unserer Tools zum Erstellen von WhatsApp-Nachrichten.

#### Wählen Sie einen Zustellungszeitplan oder Trigger {#choose-a-delivery-schedule-or-trigger}

WhatsApp-Nachrichten können basierend auf einem geplanten Zeitpunkt, einer Aktion oder einem API-Trigger zugestellt werden. Weitere Informationen finden Sie unter [Ihre Kampagne planen]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/).

Für die aktionsbasierte Zustellung können Sie auch die Dauer der Kampagne und [Ruhezeiten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours/) festlegen.

In diesem Schritt können Sie auch Zustellungs-Kontrollgruppen festlegen, z. B. ob Nutzer:innen [erneut berechtigt]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility/#campaigns) werden können, die Kampagne zu erhalten, oder ob [Frequency-Capping]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#frequency-capping)-Regeln aktiviert werden sollen.

#### Wählen Sie die Zielgruppe {#choose-users-to-target}

Als Nächstes müssen Sie die [Zielgruppe zusammenstellen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users/), indem Sie Segmente oder Filter auswählen, um Ihre Zielgruppe einzugrenzen. Sie sollten bereits die Abo-Gruppe ausgewählt haben, die Nutzer:innen nach dem Grad oder der Kategorie der Kommunikation eingrenzt, die sie mit Ihnen wünschen. In diesem Schritt wählen Sie die größere Zielgruppe aus Ihren Segmenten aus und grenzen dieses Segment mit unseren Filtern weiter ein. Sie erhalten automatisch eine Momentaufnahme der ungefähren Segmentgröße. Beachten Sie, dass die genaue Segmentzugehörigkeit immer unmittelbar vor dem Nachrichtenversand berechnet wird.

{% multi_lang_include audience/target_audiences.md %}

#### Wählen Sie Konversions-Events {#choose-conversion-events}

Braze ermöglicht es Ihnen zu tracken, wie oft Nutzer:innen bestimmte Aktionen, sogenannte [Konversions-Events]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/), nach Erhalt einer Kampagne ausführen. Sie können ein Zeitfenster von bis zu 30 Tagen festlegen, in dem eine Conversion gezählt wird, wenn die Nutzer:innen die angegebene Aktion ausführen.

Sie können auch benutzerdefinierte Konversions-Events basierend auf Ihrem spezifischen Anwendungsfall festlegen. Seien Sie kreativ und überlegen Sie, wie Sie den Erfolg dieser Kampagne wirklich messen möchten.

{% endtab %}

{% tab Canvas %}

Falls noch nicht geschehen, vervollständigen Sie die verbleibenden Abschnitte Ihrer Canvas-Komponente. Weitere Details zum Aufbau des restlichen Canvas, zur Implementierung von multivariaten Tests und Intelligenter Auswahl und mehr finden Sie im Schritt [Canvas erstellen]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message/) unserer Canvas-Dokumentation.

Da Konversationsfenster pro eingehender Nachricht nur 24 Stunden dauern können, prüft Braze, ob zwischen einer eingehenden Nachricht und einer Antwortnachricht keine Verzögerungen von mehr als 24 Stunden bestehen.

{% endtab %}
{% endtabs %}

### 5. Schritt: Überprüfen und bereitstellen {#step-5-review-and-deploy}

Nachdem Sie den letzten Teil Ihrer Kampagne oder Ihres Canvas fertiggestellt haben, überprüfen Sie die Details, testen Sie sie und senden Sie sie ab!

Sehen Sie sich als Nächstes das [WhatsApp-Reporting]({{site.baseurl}}/user_guide/channels/whatsapp/reporting/) an, um zu erfahren, wie Sie auf die Ergebnisse Ihrer WhatsApp-Campaigns zugreifen können.

## Unterstützte WhatsApp-Features {#supported-whatsapp-features}

### Ausgehende Nachrichten {#outbound-messages}

Die folgenden Features werden für ausgehende WhatsApp-Nachrichten unterstützt, die Sie über Braze senden:

| Feature | Details | Max. Größe | Unterstützte Formate |
| ------- | ------- | ------------- | ---------------------- |
| Header-Text | Strings und Variablenparameter werden unterstützt. | — | — |
| Body-Text | Strings und Variablenparameter werden unterstützt. | — | — |
| Footer-Text | Strings und Variablenparameter werden unterstützt. | — | — |
| CTA-Links | Verschiedene Call-to-Action (CTA)-Typen werden unterstützt. Weitere Details finden Sie unter [Call-to-Action-Typen](#ctas). | — | — |
| Bilder | Bilder können in den Body-Text eingebettet werden. Sie müssen 8-Bit sein und entweder ein RGB- oder RGBA-Farbmodell verwenden. | < 5 MB | `.png`, `.jpg`, `.jpeg` |
| Dokumente | Dokumente können in den Body-Text eingebettet werden. Dateien müssen über eine URL gehostet werden. | < 100 MB | `.txt`, `.xls`, `.xlsx`, `.doc`, `.docx`, `.ppt`, `.pttx`, `.pdf` |
| Videos | Videos können in den Body-Text eingebettet werden. Dateien müssen über eine URL oder in der [Braze-Medienbibliothek]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/) gehostet werden. | < 16 MB | `.3gp`, `.mp4` |
| Audio | Audio wird nur über Antwortnachrichten unterstützt. Dateien müssen über eine URL gehostet werden. | < 16 MB | `.aac`, `.amr`, `.mp3`, `.mp4`, `.ogg` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Ausgehende Nachrichten" }

{% multi_lang_include alerts/important_alerts.md alert='Meta MP4 video issue' %}

### Eingehende Nachrichten {#inbound-messages}

Die folgenden Features werden für eingehende WhatsApp-Nachrichten unterstützt, die Sie über Braze empfangen:

| Feature | Details | Unterstützte Formate |
| ------- | ------- | ------------------ |
| Body-Text | Nur Standard-Strings werden unterstützt. | — |
| Bilder | Bilder müssen 8-Bit sein und entweder ein RGB- oder RGBA-Farbmodell verwenden. Dateien müssen kleiner als 5 MB sein. | `.jpg`, `.png` |
| Audio | Nur Ogg-Dateien, die mit dem Opus-Codec codiert sind, werden unterstützt. Andere Ogg-Formate werden nicht unterstützt. | `.aac`, `.mp4`, `.mpeg`, `.amr`, `.ogg (Opus only)` |
| Dokumente | Dokumente werden über Nachrichtenanhänge unterstützt. | `.txt`, `.pdf`, `.ppt`, `.doc`, `.xls`, `.docx`, `.pptx`, `.xlsx` |
| Video | Nur der H.264-Video-Codec und der AAC-Audio-Codec werden unterstützt. Videos müssen entweder einen einzelnen Audiostream oder keinen Audiostream haben. | `.mp4`, `.3gp` |
| CTA-Links | Verschiedene Call-to-Action (CTA)-Typen werden unterstützt. Weitere Details finden Sie unter [Call-to-Action-Typen](#ctas). | — |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Eingehende Nachrichten" }

### Call-to-Action-Typen {#ctas}

Die folgenden Call-to-Action-Typen werden für WhatsApp-Nachrichten unterstützt, die Sie über Braze senden:

| CTA-Typ | Details |
| ----------- | ---------------- |
| Website besuchen | Maximal ein Button (einschließlich Variablenparameter). |
| Telefonnummer anrufen | Nur für Nachrichten-Templates verfügbar. <br>Maximal ein Button. |
| Benutzerdefinierte Schnellantwort-Buttons | Maximal drei Buttons. |
| Marketing-Opt-out-Button | Standardmäßig werden Abo-Status nicht automatisch aktualisiert. Eine vollständige Anleitung finden Sie unter [Opt-ins und Opt-outs]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs/#marketing-opt-out-selection). |
| Aktionscode-Nachrichten-Templates | Nur für Nachrichten-Templates verfügbar. <br>Diese können wie andere Nachrichten-Templates geöffnet und bearbeitet werden und sind mit Liquid und Braze-Aktionscodes kompatibel. |
| CTA-Antwortnachrichten | Erstellen Sie eine Antwortnachricht, die einen Call-to-Action-Button enthält. |
| [Listen-Antwortnachrichten]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/messaging_users/#list-messages) | Erstellen Sie eine Antwortnachricht, die eine Liste mit bis zu 10 Optionen enthält, aus denen Nutzer:innen wählen können. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Call-to-Action-Typen" }