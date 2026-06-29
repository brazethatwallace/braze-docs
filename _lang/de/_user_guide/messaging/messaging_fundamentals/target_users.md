---
nav_title: Zielgruppe zusammenstellen
article_title: Zielgruppe zusammenstellen
page_order: 12
page_type: reference
description: "Dieser Referenzartikel beschreibt, wie Sie Ihre Zielgruppe in Ihren Campaign- und Canvas-Editoren zusammenstellen."
tool:
    - Campaigns
    - Canvas
---

# Zielgruppe zusammenstellen {#target-users}

> Die Entscheidung, wie Sie Ihre Nutzer:innen ansprechen, ist einer der wichtigsten Schritte beim Erstellen einer Campaign oder eines Canvas. Indem Sie verstehen, wie Sie Ihre Zielgruppe basierend auf Verhalten, Präferenzen und demografischen Merkmalen segmentieren können, können Sie Ihre Nachrichten individuell anpassen und personalisieren.

## Eine Zielgruppe erstellen {#creating-a-target-audience}

### 1. Schritt: Nutzer:innen auswählen {#step-1-choose-users}

Unter **Targeting-Optionen** können Sie die folgenden Optionen verwenden, um auszuwählen, welche Nutzer:innen Sie mit Ihrer Campaign oder Ihrem Canvas ansprechen möchten. Nur Nutzer:innen, die Ihren definierten Kriterien entsprechen, erhalten die Nachricht. Beachten Sie, dass die genaue Segment-Zugehörigkeit immer unmittelbar vor dem Versand der Nachricht berechnet wird.

{% tabs local %}
{% tab Einzelnes Segment %}
Um Mitglieder eines zuvor erstellten Segments anzusprechen, wählen Sie ein Segment aus dem Dropdown unter **Zielgruppen nach Segment zusammenstellen** aus.
{% endtab %}

{% tab Mehrere Segmente %}
Um Nutzer:innen anzusprechen, die in mehrere zuvor erstellte Segmente fallen, fügen Sie mehrere Segmente aus dem Dropdown unter **Zielgruppen nach Segment zusammenstellen** hinzu. Die resultierende Zielgruppe besteht aus Nutzer:innen, die sowohl im ersten Segment als auch im zweiten Segment und im dritten Segment usw. enthalten sind.
{% endtab %}

{% tab Mehrere Filter %}
Um Nutzer:innen ohne Hinzufügen eines Segments anzusprechen, können Sie eine Reihe von Filtern verwenden. Dies ist eine Ad-hoc-Zielgruppe während der Nachrichtenerstellung und ermöglicht es Ihnen, die Segment-Erstellung zu überspringen, wenn Sie an einmalige Zielgruppen senden.

![Zusätzliche Filter für eine Nachricht, die Nutzer:innen anspricht, die die App zuletzt innerhalb des Tages geöffnet haben, noch nie eine Campaign oder einen Canvas-Schritt erhalten haben und vor weniger als 30 Tagen einen Kauf getätigt haben.]({% image_buster /assets/img_archive/additional_filters.png %}){: style="max-width:90%;"}
{% endtab %}

{% tab Segmente und Filter %}
Sie können auch Nutzer:innen eines oder mehrerer zuvor erstellter Segmente ansprechen, die zusätzlich unter weitere Filter fallen. Nachdem Sie zunächst Ihre Segmente ausgewählt haben, können Sie Ihre Zielgruppe im Abschnitt **Zusätzliche Filter** weiter eingrenzen. Dies wird im folgenden Screenshot demonstriert, der Nutzer:innen anspricht, die im Segment „Daily Active Users“ und im Segment „Never opened email“ enthalten sind und vor mehr als 30 Tagen einen Kauf getätigt haben.

![Targeting-Optionen für eine Nachricht, die zwei Segmente enthält und einen zusätzlichen Filter für einen letzten Kauf vor weniger als 30 Tagen hat.]({% image_buster /assets/img_archive/target_segmenter.png %}){: style="max-width:90%;"}
{% endtab %}

{% tab Bestimmte Apps %}

Sie können eine Campaign-Nachricht oder einen Canvas-Schritt an bestimmte Apps senden, z. B. eine In-App-Nachricht oder Push-Benachrichtigung nur an Android- oder iOS-Apps.

Beachten Sie jedoch, dass es möglich ist, dass eine:r Nutzer:in mehrere Apps verwendet. Der Filter „Hat App“ identifiziert alle Nutzer:innen, die die ausgewählte App haben, steuert aber nicht, welche Apps Nachrichten erhalten. Wenn Sie beispielsweise einen Segment-Filter anwenden, bei dem „Hat App“ auf Android gesetzt ist, erhalten alle Nutzer:innen, die auch die iOS-App haben, die Nachricht ebenfalls auf ihrer iOS-App.

![Ein Filter für Nutzer:innen, die die App „Hello, World (Android)“ haben.]({% image_buster /assets/img_archive/has_app_hello_world.png %}){: style="max-width:60%;"}

Angenommen, Sie möchten eine In-App-Nachricht nur an Android-Apps senden.

1. Erstellen Sie ein Segment und setzen Sie **Angesprochene Apps und Websites** auf **Nutzer:innen aus bestimmten Apps**, und wählen Sie dann Ihre Android-App aus.

![Ein Segment, das Nutzer:innen aus einer bestimmten App anspricht, „Test_Android“.]({% image_buster /assets/img_archive/app_test_android.png %}){: style="max-width:60%;"}

{: start="2"}
2. Bestätigen Sie im Schritt **Zielgruppe**, dass Ihr Segment im Abschnitt **Zielgruppen nach Segment zusammenstellen** hinzugefügt ist.

![Der Schritt „Zielgruppe“ mit einem ausgewählten Beispiel-Segment.]({% image_buster /assets/img_archive/target_users_by_segment_example.png %})

{% alert note %}
Dies funktioniert nicht, wenn Sie Ihr Segment im Abschnitt **Zusätzliche Filter** über einen Segment-Zugehörigkeitsfilter hinzufügen. Sie müssen Ihr Segment direkt unter **Zielgruppen nach Segment zusammenstellen** referenzieren, um Ihre Nachricht nur an diese App zu senden.
{% endalert %}

{% endtab %}
{% endtabs %}

{% alert tip %}
Für E-Mail-Campaigns können Sie Seed-Gruppen im Abschnitt **Seed-Gruppen** ansprechen. Beachten Sie, dass Seed-Gruppen für API-Campaigns nicht verfügbar sind, obwohl Sie Seed-Gruppen über einen API-getriggerten Eintritt in eine Campaign einbeziehen können. Weitere Informationen finden Sie unter [Seed-Gruppen]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups/#seed-groups).
{% endalert %}

### 2. Schritt: Ihre Zielgruppe testen {#step-2-test-your-audience}

Nachdem Sie Segmente und Filter zu Ihrer Zielgruppe hinzugefügt haben, können Sie testen, ob Ihre Zielgruppe wie erwartet eingerichtet ist, indem Sie [eine:n Nutzer:in nachschlagen]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/), um zu bestätigen, ob sie den Zielgruppenkriterien entsprechen.

![Der Abschnitt „Nutzer:innen-Suche“ mit einem Button „Nutzer:in nachschlagen“.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:70%"}

#### Zielgruppen-Zusammenfassung {#audience-summary}

Die **Zielgruppen-Zusammenfassung** zeigt eine Übersicht darüber, wer sich in Ihrer Zielgruppe befindet. Hier können Sie Ihre Zielgruppe weiter einschränken, indem Sie eine maximale Nutzer:innen-Obergrenze festlegen oder die Zustellgeschwindigkeit mit [Rate-Limits]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/) begrenzen.

![Der Abschnitt „Zielgruppen-Zusammenfassung“ mit Optionen zum Festlegen einer maximalen Nutzer:innen-Obergrenze oder zur Begrenzung der Zustellgeschwindigkeit.]({% image_buster /assets/img_archive/audience_summary.png %})

#### A/B-Tests {#ab-testing}

Im Abschnitt **A/B-Tests** können Sie einen Test einrichten, um die Reaktionen der Nutzer:innen auf mehrere Versionen derselben Marketing-Campaign zu vergleichen. Diese Versionen verfolgen ähnliche Marketingziele, unterscheiden sich aber in Formulierung und Stil. Das Ziel ist es, die Version der Campaign zu identifizieren, die Ihre Marketingziele am besten erreicht.

Weitere Informationen und Best Practices finden Sie unter [Multivariate und A/B-Tests]({{site.baseurl}}/user_guide/messaging/ab_testing/).

#### Zielgruppenstatistiken {#audience-statistics}

Braze stellt detaillierte Zielgruppenstatistiken der angesprochenen Kanäle in der Fußzeile bereit. Je größer Ihre Nutzerbasis ist, desto wahrscheinlicher ist es, dass die Anzahl der **erreichbaren Nutzer:innen** eine grobe Schätzung darstellt. Die Anzahl der erreichbaren Nutzer:innen kann sinken, wenn Sie eine [globale Kontrollgruppe]({{site.baseurl}}/user_guide/audience/global_control_group/) verwenden oder die Nachrichtenberechtigung einrichten.

- Um eine genaue Anzahl Ihrer erreichbaren Nutzer:innen zu ermitteln, wählen Sie [Exakte Statistiken berechnen]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/#calculating-exact-statistics), da hierbei jede:r Nutzer:in in Ihrer Nutzerbasis durchsucht wird.
- Um zu sehen, welcher Prozentsatz Ihrer Nutzerbasis angesprochen wird oder den Lifetime-Value (LTV) für dieses Segment, wählen Sie **Zusätzliche Statistiken anzeigen**.

##### Warum die Zielgruppengröße von der Anzahl erreichbarer Nutzer:innen abweichen kann {#why-the-target-audience-count-could-differ-from-the-reachable-users-count}

{% multi_lang_include audience/segments.md section='Differing audience size' %}

![Der Abschnitt „Gesamtpopulation“ mit geschätzten Zahlen für erreichbare Nutzer:innen in jedem angesprochenen Kanal.]({% image_buster /assets/img_archive/multi_channel_footer.png %})

{% alert note %}
Die Berechnung exakter Statistiken kann einige Minuten dauern. Diese Funktion berechnet die exakten Statistiken nur auf Segment-Ebene, nicht auf Filter- oder Filtergruppen-Ebene.<br><br>
Bei großen Segmenten ist es normal, dass selbst bei der Berechnung exakter Statistiken leichte Abweichungen auftreten. Die Genauigkeit dieser Funktion liegt bei 99,999 % oder höher.
{% endalert %}

## Wie Zielgruppe und Eintrittskriterien zusammenwirken {#how-target-audience-and-entry-criteria-work-together}

Wenn Sie eine Campaign oder ein Canvas in Braze erstellen, erfolgt das Targeting in zwei Teilen:

1. **Zielgruppe:** Wer qualifiziert sich
2. **Eintrittskriterien:** Was die Zustellung auslöst

Die Reihenfolge ist wichtig: Braze prüft, ob jemand zur Zielgruppe gehört, bevor die Eintrittskriterien ausgewertet werden. Wenn eine:r Nutzer:in zu diesem Zeitpunkt nicht bereits für die Zielgruppe qualifiziert ist, tritt sie oder er nicht in die Campaign oder das Canvas ein – selbst wenn sie oder er später das Eintrittsereignis auslöst. Stellen Sie sich die Zielgruppe als Warteraum vor: Nur Nutzer:innen, die sich bereits darin befinden, wenn der Trigger ausgelöst wird, können weitergehen.

### Beispiel 1 {#example-1}

Sie möchten eine Push-Nachricht während der ersten Sitzung einer:s Nutzer:in senden.

Sie legen fest:

- **Zielgruppe:** Nutzer:innen mit Sitzungsanzahl = 0
- **Eintrittsereignis:** Sitzungsstart

Wenn die:der Nutzer:in Ihre App öffnet, sieht Braze, dass die Sitzungsanzahl jetzt 1 beträgt – und sie oder er nicht mehr für die Zielgruppe qualifiziert ist. Das Eintrittsereignis tritt ein, nachdem die Berechtigung bereits nicht mehr besteht, sodass die Nachricht nicht gesendet wird.

Damit dies funktioniert, muss die:der Nutzer:in sich für die Zielgruppe qualifizieren, bevor die Sitzung beginnt (kehren Sie Zielgruppe und Eintritts-Trigger um).

### Beispiel 2 {#example-2}

Sie möchten eine E-Mail an Nutzer:innen senden, die in den letzten 7 Tagen mehr als 10 $ ausgegeben haben.

Sie legen fest:

- **Zielgruppe:** Nutzer:innen, die in den letzten 7 Tagen mehr als 10 $ ausgegeben haben
- **Eintrittsereignis:** Beliebiger Kauf

Stellen Sie sich nun vor, eine:r Nutzer:in gibt heute 12 $ aus. Das löst die Nachricht nicht aus – es macht sie oder ihn nur berechtigt, in die Zielgruppe einzutreten. Sie oder er erhält die E-Mail erst, wenn sie oder er später einen weiteren Kauf tätigt.

Ein besserer Ansatz wäre, eine breitere Zielgruppe zu verwenden und den Filter in die Eintrittskriterien zu verschieben:

- **Zielgruppe:** Alle Nutzer:innen (oder Ihre Basiszielgruppe)
- **Eintrittsereignis:** Kauf tätigen
- **Eintrittsfilter:** Gesamtausgaben in den letzten 7 Tagen > 10 $

Auf diese Weise erfüllt ein qualifizierender Kauf sowohl den Filter als auch den Trigger für die Nachricht – keine zweite Aktion erforderlich.

## Best Practices {#best-practices}

- Stellen Sie sicher, dass das Zielgruppen-Segment Nutzer:innen enthält, bevor die Eintrittskriterien eintreten.
- Vermeiden Sie Zielgruppen-Filter, die erst nach Ihrem Ereignis greifen. Wenn ein Filter von etwas abhängt, das zum Zeitpunkt des Triggers geschieht (wie „Sitzungsanzahl = 0“), ist die:der Nutzer:in möglicherweise nicht mehr qualifiziert, wenn Braze die Prüfung durchführt.
- Setzen Sie zeitbasierte Logik durchdacht ein. Wenn Sie beispielsweise neue Nutzer:innen ansprechen möchten:
    - Setzen Sie Ihre Zielgruppe auf „App erstmals innerhalb der letzten 7 Tage verwendet“.
    - Setzen Sie Ihr Eintrittsereignis auf „Sitzungsstart“.
    - Auf diese Weise qualifizieren sich nur Nutzer:innen, die sich noch in ihrer ersten Woche befinden, und treten ein, wenn sie eine Sitzung starten.