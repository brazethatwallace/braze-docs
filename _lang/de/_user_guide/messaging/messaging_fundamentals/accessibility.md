---
nav_title: Barrierefreiheit
article_title: Barrierefreie Nachrichten in Braze erstellen
page_order: 0.5
page_type: reference
description: "Dieser Referenzartikel erklärt, warum Barrierefreiheit in Marketinginhalten wichtig ist, wie die Barrierefreiheitssprache (HTML lang) in Braze kanalübergreifend funktioniert und wie Sie barrierefreie Nachrichten in Braze erstellen können."
---

# Barrierefreie Nachrichten in Braze erstellen {#build-accessible-messages-in-braze}

> Erfahren Sie, warum Barrierefreiheit in Ihren Marketinginhalten wichtig ist und wie Sie barrierefreie Nachrichten in Braze erstellen können. Weitere Informationen finden Sie in unserem Kurs [Accessible Messaging Foundations](https://learning.braze.com/accessible-messaging-foundations) auf Braze Learning.

Marketinginhalte, die Menschen mit Behinderungen ausschließen – selbst unbeabsichtigt – können Millionen von Menschen daran hindern, mit Ihrer Marke zu interagieren. Barrierefreiheit im Marketing bedeutet, allen Menschen zu ermöglichen, Ihr Marketing zu erleben, Ihre Kommunikation zu verstehen und die Möglichkeit zu haben, in Ihr Produkt, Ihren Dienst oder Ihre Marke zu investieren oder ein Fan davon zu werden.

Nehmen Sie sich beim Entwerfen Ihrer Nachrichten die zusätzliche Zeit, um zu überlegen, wie Sie Ihre Designs für alle Ihre Kund:innen zugänglich machen können.

{% alert important %}
Dieser Inhalt dient als allgemeine Orientierung und garantiert keine Einhaltung von Barrierefreiheitsstandards wie den WCAG. Braze bietet Tools, die die Erstellung barrierefreierer Nachrichten unterstützen, aber es liegt in Ihrer Verantwortung sicherzustellen, dass Ihre endgültigen Inhalte alle geltenden Anforderungen erfüllen. Barrierefreiheit ist ein komplexes Thema mit vielen Aspekten. Viele Unternehmen arbeiten mit Barrierefreiheitsspezialist:innen oder Berater:innen zusammen, um sicherzustellen, dass ihre Inhalte, Designs und Entwicklungspraktiken den Bedürfnissen aller Nutzer:innen gerecht werden.
{% endalert %}

## Barrierefreiheit bei Braze {#accessibility-at-braze}

Barrierefreie Kommunikation zu unterstützen bedeutet, offen, neugierig und lernbereit zu bleiben. Bei Braze liegt uns daran, Menschen zu verbinden – und wir wissen, dass Raum für alle zu schaffen ein Teil davon ist. Barrierefreiheit ist etwas, das wir nie als „erledigt“ betrachten, und wir begrüßen die Möglichkeit, weiter zu lernen.

{% multi_lang_include accessibility/feedback.md %}

## Zu berücksichtigende Behinderungsbereiche {#areas-of-disability-to-consider}

*Dieser Abschnitt ist teilweise adaptiert von [W3C: Diverse Abilities and Barriers](https://www.w3.org/WAI/people-use-web/abilities-barriers/).*

{% tabs local %}
{% tab Visuell %}

Visuelle Behinderungen können von leichtem oder mäßigem Sehverlust in einem oder beiden Augen bis hin zu erheblichem oder vollständigem Sehverlust in beiden Augen reichen. Manche Menschen haben eine verminderte oder fehlende Empfindlichkeit für bestimmte Farben oder eine erhöhte Empfindlichkeit gegenüber hellen Farben.

Um mit Ihren Inhalten zu interagieren, benötigen diese Nutzer:innen die Möglichkeit:

- Textgröße und Bilder zu vergrößern oder zu verkleinern
- Einstellungen für Schriftarten, Farben und Abstände anzupassen
- Sich den Inhalt per Text-to-Speech-Synthese vorlesen zu lassen (also einen Screenreader zu verwenden)
- Sich Audiobeschreibungen von Videos anzuhören
- Text über eine aktualisierbare Braillezeile zu lesen

{% alert note %}
- Weltweit haben mindestens 2,2 Milliarden Menschen eine Nah- oder Fernsehbeeinträchtigung (siehe [WHO](https://www.who.int/news-room/fact-sheets/detail/blindness-and-visual-impairment))
- Etwa 1 von 12 Männern und 1 von 200 Frauen haben eine Form von Farbsehschwäche – geschätzt 300 Millionen Menschen weltweit (siehe [NHS](https://www.nhs.uk/conditions/colour-vision-deficiency/))
{% endalert %}

{% endtab %}
{% tab Auditiv %}

Hör- oder auditive Behinderungen können leichte bis mäßige Hörbeeinträchtigungen in einem oder beiden Ohren umfassen. Selbst ein teilweiser Hörverlust kann bei Audioinhalten problematisch sein.

Um Ihre Inhalte zu verstehen, sind diese Nutzer:innen angewiesen auf:

- Transkripte und Untertitel von Audioinhalten
- Mediaplayer, die Untertitel anzeigen und Optionen zur Anpassung von Textgröße und Farben der Untertitel bieten
- Optionen zum Stoppen, Pausieren und Anpassen der Lautstärke von Audioinhalten (unabhängig von der Systemlautstärke)
- Hochwertige Vordergrund-Audioinhalte, die sich deutlich von Hintergrundgeräuschen unterscheiden

{% alert note %}
- Jede achte Person in den Vereinigten Staaten (13 % oder 30 Millionen) ab 12 Jahren hat einen Hörverlust in beiden Ohren, basierend auf standardisierten Hörtests
- Etwa 15 % der amerikanischen Erwachsenen (37,5 Millionen) ab 18 Jahren berichten von Hörproblemen (siehe [NIH](https://www.nidcd.nih.gov/health/statistics/quick-statistics-hearing))
{% endalert %}

{% endtab %}
{% tab Motorisch %}

Motorische Behinderungen können Schwäche und Einschränkungen der Muskelkontrolle oder -empfindung, Gelenkerkrankungen, Schmerzen, die die Bewegung behindern, und fehlende Gliedmaßen umfassen.

Diese Nutzer:innen sind auf Tastaturunterstützung angewiesen, um Funktionen zu aktivieren (auch wenn sie keine Standardtastatur verwenden). Um mit Ihren Inhalten zu interagieren, benötigen diese Nutzer:innen:

- Große klickbare Bereiche
- Ausreichend Zeit, um Aufgaben abzuschließen
- Sichtbare Indikatoren für den aktuellen Fokus
- Mechanismen zum Überspringen von Inhaltsblöcken, wie Seitenüberschriften oder Navigationsleisten

{% alert note %}
Fast 2 Millionen Menschen in den USA leben mit dem Verlust einer Gliedmaße (siehe [Amputee Coalition](https://www.amputee-coalition.org/limb-loss-resource-center/resources-filtered/resources-by-topic/limb-loss-statistics/limb-loss-statistics/#1))
{% endalert %}

{% endtab %}
{% tab Kognitiv %}

Kognitive, Lern- und neurologische Behinderungen umfassen Neurodiversität und neurologische Störungen sowie Verhaltens- und psychische Gesundheitsstörungen, die nicht unbedingt neurologischer Natur sind. Sie können jeden Teil des Nervensystems betreffen und beeinflussen, wie gut Menschen hören, sich bewegen, sehen, sprechen und Informationen verstehen.

Je nach individuellen Bedürfnissen sind diese Nutzer:innen angewiesen auf:

- Klar strukturierte Inhalte
- Konsistente Beschriftung von Formularen, Buttons und anderen Inhalten
- Vorhersehbare Linkziele und allgemeine Interaktion
- Verschiedene Navigationsmöglichkeiten, wie Menüs und Suchleisten
- Einstellungen zum Deaktivieren von blinkenden, blitzenden oder anderweitig ablenkenden Inhalten
- Einfacheren Text, der durch Bilder unterstützt wird


{% alert note %}
- Jede fünfte Person in den Vereinigten Staaten hat Lern- und Aufmerksamkeitsprobleme (siehe [LDA](https://ldaamerica.org/lda_today/the-state-of-learning-disabilities-today/#:~:text=LD%20Today,have%20learning%20and%20attention%20issues.))
- Etwa 10–20 % der Weltbevölkerung gelten als neurodivergent (siehe [Deloitte](https://www2.deloitte.com/us/en/insights/topics/talent/neurodiversity-in-the-workplace.html))
- Etwa 1 von 100 Kindern weltweit hat Autismus (siehe [WHO](https://www.who.int/news-room/fact-sheets/detail/autism-spectrum-disorders))
{% endalert %}

{% endtab %}
{% endtabs %}

## Best Practices {#best-practices}

Barrierefreie Inhalte zu erstellen muss nicht überwältigend sein. Kleine, durchdachte Entscheidungen können einen großen Unterschied machen. Dieser Abschnitt führt Sie durch praktische Tipps, die mehr Menschen helfen, Ihre Nachrichten erfolgreich zu lesen, zu navigieren und mit ihnen zu interagieren. Ob Sie Ihren Text anpassen, Ihre Buttons gestalten oder Alt-Text zu Bildern hinzufügen – jede Verbesserung trägt zu einem inklusiveren Erlebnis bei. Legen wir los.

### Inhalt {#content}

#### Struktur und Aufbau {#structure-and-flow}

Beginnen wir mit dem Fundament. Wenn Ihre Inhalte eine klare Struktur haben, ist es für alle einfacher zu folgen – besonders für Menschen, die auf Screenreader oder Tastaturnavigation angewiesen sind.

- **Gliedern Sie Ihre Inhalte in Abschnitte:** Die Verwendung von Überschriften, Aufzählungszeichen und Listen hilft Menschen, Ihre Inhalte schnell zu verstehen und zu überfliegen – auch wenn sie es eilig haben.
- **Überspringen Sie keine Überschriftenebenen:** Überschriften geben Ihren Inhalten Struktur und helfen Leser:innen, schnell zu verstehen, wie Abschnitte zueinander in Beziehung stehen. Wenn Sie Überschriftenebenen überspringen (zum Beispiel direkt von einer H2 zu einer H4 springen), brechen Sie diese logische Struktur auf. Das erschwert es Nutzer:innen, insbesondere denen, die Screenreader verwenden, Ihre Nachricht zu navigieren und zu verstehen. Folgen Sie immer einer logischen, sequenziellen Hierarchie von Überschriften (H1 zu H2 zu H3 usw.), um sicherzustellen, dass Ihre Inhalte organisiert, barrierefrei und für alle leicht verständlich bleiben.

#### Lesbarkeit {#readability}

Sobald Ihre Struktur steht, ist der nächste Schritt sicherzustellen, dass Ihre Worte tatsächlich leicht zu lesen sind. Das bedeutet, Dinge einfach, übersichtlich und auf verschiedenen Geräten und für verschiedene Nutzerbedürfnisse komfortabel lesbar zu halten.

- **Schreiben Sie kurze, klare Sätze:** Kurze Sätze sind für alle leicht verständlich, besonders für Menschen, die Screenreader verwenden oder Schwierigkeiten haben, komplexe Informationen zu verarbeiten. Schreiben Sie auf dem Leseniveau der siebten Klasse in den USA. Sie können Ressourcen wie die [Hemingway App](https://hemingwayapp.com/) verwenden, um das Leseniveau Ihres Textes zu überprüfen.
- **Wählen Sie lesbare Schriftgrößen und Abstände:** Text, der zu klein ist, kann schwer zu lesen sein – besonders auf Mobilgeräten. Verwenden Sie mindestens 14px für Fließtext. Machen Sie Überschriften größer, damit Nutzer:innen den Unterschied deutlich erkennen können. Zusätzlicher Zeilenabstand (etwa 1,5-fache Zeilenhöhe) und Absatzabstände verbessern die Lesbarkeit, besonders für Menschen mit visuellen oder kognitiven Bedürfnissen.
- **Vermeiden Sie Blocksatz:** Blocksatz erzeugt ungleichmäßige Abstände zwischen Wörtern, was das Lesen für Menschen mit Legasthenie oder kognitiven Behinderungen erschwert. Erwägen Sie, Inhalte, die über mehr als zwei Zeilen umbrechen, für Links-nach-rechts-Sprachen linksbündig oder für [Rechts-nach-links-Sprachen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages) rechtsbündig auszurichten.
- **Verwenden Sie Fett, Kursiv und Großbuchstaben sparsam:** Zu viel hervorgehobener Text erschwert das Lesen – besonders für Menschen mit Legasthenie oder Sehbeeinträchtigungen. Halten Sie es einfach.

#### Klarheit und Benutzerfreundlichkeit {#clarity-and-usability}

Zum Schluss sprechen wir über die feineren Details – die Dinge, die Nutzer:innen helfen, Ihre Inhalte nicht nur zu sehen, sondern auch zu verstehen und mit ihnen zu interagieren.

- **Beschriften Sie Links und Buttons klar:** Stellen Sie sicher, dass Ihr [Link](#links)- und [Button](#buttons)-Text klar erklärt, was als Nächstes passiert. Das hilft Menschen, die Screenreader verwenden oder mit der Tastatur navigieren, zu wissen, was sie erwartet.
- **Gehen Sie sparsam mit Symbolen und Emojis um:** Sonderzeichen und Emojis können Ihre Inhalte verspielt machen, aber sie können verwirrend sein, wenn sie von Screenreadern vorgelesen werden. Verwenden Sie sie sparsam und stellen Sie sicher, dass sie keinen klaren, beschreibenden Text ersetzen.
- **Testen Sie auf Textabschneidung:** Testen Sie Ihren Text immer, indem Sie eine [Testnachricht senden]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages), um sicherzustellen, dass Ihr Text nicht abgeschnitten wird. Wenn Ihre Nachricht abgeschnitten wird, schadet das sowohl Ihnen als auch Ihrer Zielgruppe, da Ihre Inhalte sie nicht erreichen.

### Barrierefreiheitssprache {#accessibility-language}

Die **Barrierefreiheitssprache** teilt Screenreadern und anderen assistiven Tools mit, in welcher Sprache Ihr Inhalt verfasst ist. Für Kanäle, die eine vollständige HTML-Seite oder E-Mail senden, kann Braze ein Sprach-Tag (`lang`) hinzufügen, wenn Sie es im Editor oder über Liquid festlegen. Das unterstützt das [WCAG 2.1 Erfolgskriterium 3.1.1 Sprache der Seite (Stufe A)](https://www.w3.org/WAI/WCAG21/Understanding/language-of-page.html).

Wenn Sie die Barrierefreiheitssprache leer lassen und kein sicherer Standardwert verfügbar ist, lässt Braze das Sprach-Tag weg. Wenn keine Sprache festgelegt ist, greifen assistive Tools oft auf die Telefon- oder Computersprache der Person zurück. Wenn diese von der Nachrichtensprache abweicht, kann die Aussprache falsch klingen.

Campaigns und Canvases verwenden dieselben Editoren für diese Optionen, es sei denn, ein Feature ist für Ihren Workspace nicht verfügbar.

#### Barrierefreiheitssprache konfigurieren {#configure-accessibility-language}

Wenn Ihr Editor diese Option enthält, gehen Sie zum Abschnitt **Accessibility** in den Nachrichteneinstellungen. Wählen Sie eine Sprache aus dem Dropdown oder verwenden Sie Liquid (zum Beispiel {% raw %}`{{accessibility_language}}`{% endraw %}, wenn [mehrsprachige Nachrichten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) aktiviert sind und die **Einstellungen für die Lokalisierung** konfiguriert sind).

#### Mehrsprachige Nachrichten {#multi-language-messages}

Legen Sie in den **Einstellungen für die Lokalisierung** eine Barrierefreiheitssprache für jede Locale fest, damit Liquid {% raw %}`{{accessibility_language}}`{% endraw %} für lokalisierte Sendungen ausfüllen kann. Ob dieser Wert für neue Nachrichten bereits vorausgewählt ist, hängt vom Kanal ab. Für CSV- und Übersetzungs-Workflows beginnen Sie mit [Spracheinstellungen und Barrierefreiheit]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages#language-settings-and-accessibility).

#### Kanal- und Editor-Unterstützung {#channel-and-editor-support}

Verwenden Sie diese Tabelle, um Kanäle zu vergleichen. Standardwerte können abweichen, prüfen Sie daher stichprobenartig, was Ihre Zielgruppe tatsächlich erhält.

| Kanal | Wissenswertes |
| --- | --- |
| E-Mail (Drag-and-Drop, vollständiges Template) | Legen Sie die Sprache im Editor fest. Bei mehrsprachigen Nachrichten kann ein vollständiges E-Mail-Template die Sprache jeder Locale automatisch zuordnen. Wenn Sie nur Content Blocks (einzelne Zeile) verwenden, funktionieren diese Abkürzungen nicht auf die gleiche Weise – wählen Sie die Sprache selbst, wo der Editor es erlaubt. |
| E-Mail (HTML-Code) | Braze fügt kein Sprach-Tag für Sie hinzu. Fügen Sie es in Ihrem HTML hinzu, wenn Sie es benötigen. |
| In-App-Nachrichten (Drag-and-Drop) | Wenn Sie unter **Accessibility** eine Sprache auswählen, fügt Braze diese Sprache dem äußeren HTML der Nachricht hinzu, sodass Screenreader die gesamte Nachricht als diese Sprache behandeln. Bei aktivierten mehrsprachigen Nachrichten können neue Nachrichten standardmäßig Ihre Locale-Sprachen verwenden. Die **Vorschau** zeigt möglicherweise keine Sprache an, bis Sie eine unter **Einstellungen** auswählen. |
| Banner | Gleiches Verhalten wie bei In-App-Nachrichten. |
| Landing-Pages | Sie können die Sprache auf der Live-Seite festlegen. Wählen Sie eine Sprache oder verwenden Sie Liquid, wenn Ihr Konto Liquid auf Landing-Pages erlaubt. Standardwerte unterscheiden sich ebenfalls von In-App-Nachrichten und Bannern – prüfen Sie die veröffentlichte Seite. |
| Content Cards | Cards verwenden ein **Language**-Feld für Apps anstelle einer expliziten Barrierefreiheitssprache. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Kanal- und Editor-Unterstützung" }

Wenn Sie HTML selbst schreiben, können Sie trotzdem ein Sprach-Tag für einen Teil der Nachricht hinzufügen (zum Beispiel einen Satz in einer anderen Sprache). Weitere Muster finden Sie unter [Benutzerdefiniertes HTML](#custom-html).

#### Standardreferenz {#standards-reference}

Wenn Braze ein Sprach-Tag auf Root-Ebene zum HTML hinzufügt, folgt es der HTML-Regel [`lang`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/lang). Testtools suchen oft nach [`html-has-lang`](https://dequeuniversity.com/rules/axe/4.2/html-has-lang). Content Cards verwenden stattdessen Ihr **Language**-Feld anstelle dieses HTML-Musters.

### Buttons {#buttons}

Verwenden Sie **Buttons**, um eine Aktion anzuzeigen, wie das Absenden eines Formulars oder das Abspielen eines Karussells. Wenn Sie zu einer neuen URL navigieren, erwägen Sie stattdessen die Verwendung eines [Links](#links).

#### Schreiben Sie klaren, handlungsorientierten Text {#write-clear-action-oriented-text}

Ähnlich wie bei Linktexten sollten Button-Beschriftungen die Aktion klar beschreiben. Effektiver Button-Text ist spezifisch und handlungsorientiert. Zum Beispiel sagt „Bestellung absenden“ den Nutzer:innen klar, was passiert, wenn sie klicken, während einfach „Absenden“ mehrdeutig sein kann. Jede Beschriftung sollte die beabsichtigte Aktion genau beschreiben, damit Screenreader und alle Nutzer:innen das Ergebnis leicht verstehen und vorhersagen können, wenn sie mit Ihren Buttons interagieren.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">
        Guter Button-Text <span aria-hidden="true">✅</span>
      </th>
      <th style="width: 50%">
        Schlechter Button-Text <span aria-hidden="true">🚫</span>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>„Bestellung absenden“</td>
      <td>„Absenden“</td>
    </tr>
    <tr>
      <td>„Konto erstellen“</td>
      <td>„Registrieren“</td>
    </tr>
    <tr>
      <td>„Unsere Broschüre herunterladen“</td>
      <td>„Herunterladen“</td>
    </tr>
    <tr>
      <td>„Produktdetails anzeigen“</td>
      <td>„Mehr erfahren“</td>
    </tr>
    <tr>
      <td>„Updates abonnieren“</td>
      <td>„Abonnieren“</td>
    </tr>
  </tbody>
</table>

Halten Sie Button-Texte kurz, um Abschneidung zu vermeiden. Wenn der Text eines Buttons zu lang ist, wird er möglicherweise mit Auslassungspunkten abgeschnitten, anstatt umzubrechen.

#### Verwenden Sie ausreichenden Farbkontrast {#use-sufficient-color-contrast}

Button-Text muss vor der Hintergrundfarbe des Buttons gut lesbar sein. Überprüfen Sie, ob Ihr Button-Text die WCAG 2.2 AA [Kontrastminima](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) erfüllt:

- 4,5:1 Kontrastverhältnis für normalgroßen Text (die meisten Buttons)
- 3:1 Kontrastverhältnis für großen Text (typischerweise 18pt oder größer)

Hoher Kontrast hilft sicherzustellen, dass Buttons für alle lesbar und klickbar bleiben, einschließlich Nutzer:innen mit Sehbeeinträchtigungen oder solchen, die Ihre Nachricht unter schwierigen Bedingungen betrachten. Weitere Informationen finden Sie im Abschnitt [Farbkontrast](#color-contrast).

#### Machen Sie Buttons leicht antippbar {#make-buttons-easy-to-tap}

Stellen Sie sicher, dass Ihre Buttons (und Links) groß genug sind und weit genug voneinander entfernt sind, damit Nutzer:innen auf Mobilgeräten sie leicht bedienen können. Kleine oder eng beieinander liegende [Touch-Ziele](#touch-targets) können für Nutzer:innen mit motorischen Behinderungen frustrierend oder unmöglich zu bedienen sein.

### Links {#links}

Verwenden Sie Links zur Navigation, zum Beispiel um Nutzer:innen auf eine externe Seite zu leiten.

#### Schreiben Sie beschreibenden Linktext {#write-descriptive-link-text}

Schreiben Sie Linktexte, die klar beschreiben, wohin der Link die Nutzer:innen führt. Screenreader-Nutzer:innen springen oft von Link zu Link, um Inhalte zu überfliegen. Stellen Sie daher sicher, dass Ihr Linktext für sich allein stehen kann. Vermeiden Sie Formulierungen wie „hier klicken“, „mehr“ und „für Details klicken“, da diese ohne Kontext mehrdeutig sind.

Überlegen Sie zum Beispiel, wie Sie einen Link zu einem Wetterbericht formulieren könnten.

| Schlecht | Besser | Am besten |
| --- | --- | --- |
| Hier klicken | Hier klicken, um den heutigen Wetterbericht aufzurufen | Heutiger Wetterbericht |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Beschreibenden Linktext schreiben" }

Wie bei allen Inhalten gilt: Halten Sie es unkompliziert mit so wenig überflüssigen Wörtern wie möglich.

#### Vermeiden Sie es, Links wie Buttons zu gestalten {#avoid-styling-links-like-buttons}

Die Drag-and-Drop-Editoren von Braze geben standardmäßig semantisches HTML aus, sodass Links dort nicht wie Buttons gestaltet werden. Wenn Sie jedoch mit [benutzerdefiniertem HTML](#custom-html) arbeiten oder Änderungen auf Code-Ebene vornehmen, beachten Sie Folgendes:

- **Links (`<a>`)** reagieren auf die <kbd>Enter</kbd>-Taste.
- **Buttons (`<button>`)** reagieren sowohl auf die <kbd>Enter</kbd>- als auch auf die <kbd>Leertaste</kbd>.

Einen Link so zu gestalten, dass er wie ein Button aussieht, kann Menschen verwirren, die mit der Tastatur navigieren – sie könnten versuchen, die <kbd>Leertaste</kbd> zu drücken und erwarten, dass es funktioniert.

Verwenden Sie das richtige Element für die Aktion:

- Verwenden Sie `<button>` für Aktionen, wie das Absenden eines Formulars oder das Öffnen eines Modals.
- Verwenden Sie `<a>` für Navigation, wie das Verlinken auf eine andere Seite oder Datei.

{% raw %}

```html
<!-- Recommended: A true button for an action -->
<button type="button">Download report</button>

<!-- Not recommended: A link styled as a button -->
<a href="#" class="btn">Download report</a>
```

{% endraw %}

### Touch-Ziele {#touch-targets}

Touch-Ziele sind alle Teile Ihrer Nachricht, die Nutzer:innen antippen, um eine Aktion auszuführen, wie Buttons, Links oder Symbole. Diese Elemente müssen groß genug und weit genug voneinander entfernt sein, damit Menschen sie leicht antippen können, besonders auf Mobilgeräten.

Wenn Touch-Ziele zu klein oder zu nah beieinander sind, kann es für Nutzer:innen mit Mobilitäts- oder Geschicklichkeitseinschränkungen frustrierend oder unmöglich sein, mit Ihrer Nachricht zu interagieren. Eine Verbesserung kann dazu beitragen, Fehler zu reduzieren und ein reibungsloseres Erlebnis für alle zu schaffen.

Hier ist, worauf Sie achten sollten:
- **Verwenden Sie eine angemessene Touch-Ziel-Größe.** Streben Sie eine Mindestgröße von 44 x 44 Pixeln für Touch-Ziele an. Dies entspricht den WCAG 2.2-Richtlinien für [Touch-Ziele](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) und gängigen Standards für mobile Benutzerfreundlichkeit.
- **Geben Sie jedem Ziel Freiraum.** Wenn Tippziele zu nah beieinander liegen – wie gestapelte Links oder eng gruppierte Buttons – kann es leicht passieren, dass man daneben tippt oder das falsche Element trifft. Fügen Sie Abstände oder Padding zwischen den Elementen hinzu, um das zu verhindern.
- **Verlassen Sie sich nicht nur auf visuelle Darstellung.** Selbst kleine Symbole können durch zusätzliches Padding benutzerfreundlicher gemacht werden, sodass sie die Mindestgrößenanforderungen erfüllen, ohne das Layout zu verändern.
- **Vorschau auf Mobilgeräten.** Testen Sie Ihre Nachricht auf verschiedenen Bildschirmgrößen und stellen Sie sicher, dass interaktive Elemente leicht zu bedienen sind.

Die Verbesserung von Touch-Zielen ist eine der effektivsten Möglichkeiten, Ihre Nachricht auf Mobilgeräten barrierefreier zu machen – und es ist gute UX für alle.

### Bilder {#images}

#### Alt-Text bereitstellen {#provide-alt-text}

Alternativer Text (Alt-Text) ist eine kurze Beschreibung des Inhalts oder der Funktion eines Bildes, die Screenreader und andere assistive Technologien den Nutzer:innen bereitstellen. Schreiben Sie für jedes bedeutungsvolle Bild beschreibenden Alt-Text, damit Nutzer:innen, die die visuellen Inhalte nicht sehen können, Ihre Nachricht oder Ihren Call-to-Action trotzdem verstehen.

#### Vermeiden Sie Bilder mit Text {#avoid-images-of-text}

Vermeiden Sie es nach Möglichkeit, Text in Bilder einzubetten – Screenreader können bildbasierten Text nicht lesen, und Nutzer:innen können Schriftgröße oder -farbe nicht einfach für bessere Sichtbarkeit anpassen. Beachten Sie diese Tipps:

- **Entfernen Sie Text, wo möglich:** Verschieben Sie beschreibenden oder werblichen Text aus dem Bild in ein Textfeld in Ihrer Nachricht. So können Nutzer:innen ihn nach Bedarf mit ihren Geräte- oder Browsereinstellungen vergrößern oder umfärben.
- **Testen Sie auf Lesbarkeit und Kontrast:** Wenn Sie Text im Bild beibehalten müssen, befolgen Sie die Best Practices für [Farbkontrast](#color-contrast) und verwenden Sie eine [große Schriftgröße](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html#dfn-large-scale). Das bedeutet, dass Text mindestens 18 Punkt (etwa 24 Pixel) für nicht fetten Text oder 14 Punkt (etwa 18 Pixel) für fetten Text betragen sollte. Diese Größen helfen, dass Text lesbar bleibt, ohne dass Nutzer:innen hineinzoomen müssen, und verbessern den Gesamtkontrast und die Lesbarkeit des Inhalts. Testen Sie, ob er auf kleineren Bildschirmen noch lesbar ist.
- **Stellen Sie Alt-Text bereit:** Für wesentlichen Text, der im Bild bleiben muss, fügen Sie Alt-Text hinzu, der die Worte beschreibt.

Wenn Bilder Text enthalten, der nicht bearbeitet werden kann, verlieren Nutzer:innen mit Sehbeeinträchtigungen die Flexibilität, Leseanpassungen vorzunehmen. Indem Sie Text von Bildern trennen, helfen Sie mehr Nutzer:innen, Ihre Nachricht komfortabel zu lesen und mit ihr zu interagieren.

#### Tipps zum Schreiben von Alt-Text {#tips-for-writing-alt-text}

- [Beschreiben Sie, was tatsächlich im Bild zu sehen ist](#tip-1)
- [Halten Sie es kurz, aber spezifisch](#tip-2)
- [Vermeiden Sie „Bild von“ oder „Foto von“](#tip-3)
- [Geben Sie Text wieder, der im Bild erscheint](#tip-4)
- [Bleiben Sie beim relevanten Kontext – kein zusätzlicher Marketing-Jargon](#tip-5)
- [Berücksichtigen Sie den Zweck des Bildes](#tip-6)

##### Beschreiben Sie, was tatsächlich im Bild zu sehen ist {#tip-1}

Screenreader-Nutzer:innen sind auf Alt-Text angewiesen, um den Inhalt oder die Funktion eines Bildes zu verstehen. Vermeiden Sie generisches „Marketing-Sprech“, das nicht zu dem passt, was visuell gezeigt wird.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">
        Gute Beispiele <span aria-hidden="true">✅</span>
      </th>
      <th style="width: 50%">
        Schlechte Beispiele <span aria-hidden="true">🚫</span>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>„Lächelnde Frau in blauer Jeansjacke, die eine Einkaufstasche hält.“</td>
      <td>„Zeit, sich etwas zu gönnen!“ (Keine Erwähnung dessen, was tatsächlich im Bild zu sehen ist)</td>
    </tr>
    <tr>
      <td>„Mann in schwarzem T-Shirt, der sich in einer Stadtstraße an ein Fahrrad lehnt.“</td>
      <td>„Lebe dein bestes Leben!“ (Ignoriert das Fahrrad und die Stadtkulisse)</td>
    </tr>
    <tr>
      <td>„Blaues Mehrfamilienhaus mit einem „Zu vermieten“-Schild davor."</td>
      <td>„Der Schlüssel zu einem besseren Morgen!“ (Spiegelt weder die Wohnung noch das Schild wider)</td>
    </tr>
  </tbody>
</table>

##### Halten Sie es kurz, aber spezifisch {#tip-2}

Prägnanter Alt-Text erleichtert es Nutzer:innen, die Information zu verarbeiten. Fügen Sie genug Details hinzu, um den Zweck zu vermitteln, aber lassen Sie Überflüssiges weg. Als Faustregel gilt: Halten Sie Alt-Text auf 125 Zeichen oder weniger. Wenn mehr als ein kurzer Satz nötig ist, erwägen Sie die Verwendung einer der [Methoden für lange Beschreibungen](https://www.w3.org/WAI/tutorials/images/complex/) von W3C.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">Gute Beispiele <span aria-hidden="true">✅</span></th>
      <th style="width: 50%">Schlechte Beispiele <span aria-hidden="true">🚫</span></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>„Rote Laufschuhe auf weißem Hintergrund“</td>
      <td>„Laufschuhe, die extrem bequem und perfekt für Ihren aktiven Lebensstil in einem lebhaften Rotton sind.“ (Zu lang und voller Werbefloskeln)</td>
    </tr>
    <tr>
      <td>„Vier Laptops auf einem Displayständer“</td>
      <td>„Entdecken Sie den ultimativen Produktivitätsbooster, der Ihre Arbeitsweise jeden Tag und auf jede erdenkliche Weise neu definiert.“ (Beschreibt nicht, was tatsächlich gezeigt wird)</td>
    </tr>
    <tr>
      <td>„Gruppe von Freunden, die an einem sonnigen Tag Eis essen“</td>
      <td>„Fangen Sie pures Glück mit dem süßesten Genuss ein – das Leben ist besser mit unserem Markeneis!“ (Zu abstrakt und markenfokussiert)</td>
    </tr>
  </tbody>
</table>

##### Vermeiden Sie „Bild von“ oder „Foto von“ {#tip-3}

Screenreader kündigen ein Bild bereits an. Beginnen Sie direkt mit der Beschreibung des Motivs.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">
        Gute Beispiele <span aria-hidden="true">✅</span>
      </th>
      <th style="width: 50%">
        Schlechte Beispiele <span aria-hidden="true">🚫</span>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>„Für einen Brunch gedeckter Tisch mit Pfannkuchen, Obst und Kaffee.“</td>
      <td>„Bild eines für einen Brunch gedeckten Tisches“</td>
    </tr>
    <tr>
      <td>„Straßenplakat mit fettem „Große Eröffnung“-Text"</td>
      <td>„Foto eines Plakats am Straßenrand“</td>
    </tr>
    <tr>
      <td>„Verschneite Berglandschaft bei Sonnenuntergang“</td>
      <td>„Foto von Schnee und Bergen“</td>
    </tr>
  </tbody>
</table>

##### Geben Sie Text wieder, der im Bild erscheint {#tip-4}

Wenn ein Bild wesentlichen Text enthält, fügen Sie diese Information in den Alt-Text ein, damit Nutzer:innen sie nicht verpassen.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">
        Gute Beispiele <span aria-hidden="true">✅</span>
      </th>
      <th style="width: 50%">
        Schlechte Beispiele <span aria-hidden="true">🚫</span>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>„Banner mit dem Text „Sommerschlussverkauf – 50 % Rabatt auf alle Bademode.“"</td>
      <td>„Banner, das einen Verkauf bewirbt.“ (Erwähnt den tatsächlichen Rabatt nicht)</td>
    </tr>
    <tr>
      <td>„Logo mit dem Text „Café Toscana“ in Schreibschrift"</td>
      <td>„Logo-Bild für ein Café.“ (Enthält nicht den Text „Café Toscana“)</td>
    </tr>
    <tr>
      <td>„Anzeige mit dem Text „Konzerttickets jetzt erhältlich – Start am 5. Juni“"</td>
      <td>„Konzertanzeige.“ (Keine Veranstaltungsdetails)</td>
    </tr>
  </tbody>
</table>

##### Bleiben Sie beim relevanten Kontext – kein zusätzlicher Marketing-Jargon {#tip-5}

Füllen Sie Alt-Text nicht mit SEO-Begriffen oder Handlungsaufforderungen auf, die nicht direkt mit dem Bild zusammenhängen. Bieten Sie Mehrwert für diejenigen, die das Bild nicht sehen können.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">Gute Beispiele <span aria-hidden="true">✅</span></th>
      <th style="width: 50%">Schlechte Beispiele <span aria-hidden="true">🚫</span></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>„Laptop, der das Braze-Dashboard-Analytics-Chart zeigt“</td>
      <td>„Steigern Sie Conversions und katapultieren Sie den ROI mit der besten Plattform der Welt!“ (Fügt unnötige Marketingsprache hinzu)</td>
    </tr>
    <tr>
      <td>„Hinterhof-Terrassenset mit vier Stühlen und einem Glastisch“</td>
      <td>„Veranstalten Sie eine unglaubliche Sommerparty für alle Ihre Freunde und Familie!“ (Beschreibt ein Szenario, nicht das Bild)</td>
    </tr>
    <tr>
      <td>„Mobiltelefon, das eine Wetter-App mit 24 °C anzeigt“</td>
      <td>„Erleben Sie Realtime-Innovationen im Wetter-Tracking, die alles verändern“ (Spiegelt nicht wider, was sichtbar gezeigt wird)</td>
    </tr>
  </tbody>
</table>

##### Berücksichtigen Sie den Zweck des Bildes {#tip-6}

Wenn ein Bild als Link oder Call-to-Action fungiert, beschreiben Sie die beabsichtigte Aktion („Einkaufen“, „Link zu“, „Anmelden“), nicht nur das Label oder das gezeigte Produkt.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">Gute Beispiele <span aria-hidden="true">✅</span></th>
      <th style="width: 50%">Schlechte Beispiele <span aria-hidden="true">🚫</span></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>„Herbstkollektion einkaufen“</td>
      <td>„Herbstkollektion“ (Beabsichtigte Aktion fehlt)</td>
    </tr>
    <tr>
      <td>„Link zum kostenlosen E-Book“</td>
      <td>„Kostenloses E-Book“ (Macht nicht deutlich, dass es sich um einen Link handelt)</td>
    </tr>
    <tr>
      <td>„Für den Newsletter anmelden“</td>
      <td>„Newsletter“ (Beschreibt nicht, was die Nutzer:innen tun können)</td>
    </tr>
  </tbody>
</table>

Wenn das Bild keinen Zweck hat, machen Sie das ebenfalls deutlich. Dekorative Bilder, wie Logos, sollten ein leeres Alt-Tag (`alt=""`) haben, damit Screenreader wissen, dass sie es überspringen können. Ohne dieses wird normalerweise stattdessen der Bilddateiname vorgelesen.

### Videos {#videos}

Videos sind ansprechend, aber wenn sie nicht barrierefrei sind, riskieren Sie, einen Teil Ihrer Zielgruppe auszuschließen. Verwenden Sie die folgenden Tipps, um Ihre Videoinhalte inklusiver zu gestalten:

- [Stellen Sie Untertitel bereit](#closed-captions)
- [Stellen Sie Wiedergabesteuerungen bereit](#playback-controls)
- [Vermeiden Sie automatische Wiedergabe](#no-auto-play)
- [Vermeiden Sie blinkende oder stroboskopische Inhalte](#no-seizures)

#### Stellen Sie Untertitel bereit {#closed-captions}

Fügen Sie Ihren Videos Untertitel hinzu, damit Nutzer:innen den Dialogen, Soundeffekten und anderen Audioinhalten folgen können. Untertitel helfen:

- Menschen, die gehörlos oder schwerhörig sind
- Zuschauer:innen, die in einer lautlosen Umgebung schauen
- Nicht-Muttersprachler:innen, die lieber mitlesen

Untertitel können ein- und ausgeschaltet werden, sodass Nutzer:innen wählen können, was für sie am besten funktioniert.

{% multi_lang_include accessibility/video.md %}

#### Stellen Sie Wiedergabesteuerungen bereit {#playback-controls}

Stellen Sie sicher, dass Ihr eingebettetes Video barrierefreie Wiedergabesteuerungen enthält – wie Abspielen, Pause, Stummschalten und Spulen – damit Nutzer:innen auf die für sie beste Weise damit interagieren können.

#### Vermeiden Sie automatische Wiedergabe {#no-auto-play}

Vermeiden Sie es nach Möglichkeit, Videos auf automatische Wiedergabe einzustellen. Automatische Wiedergabe kann irritierend oder desorientierend sein für:

- Nutzer:innen, die auf Screenreader oder Tastaturnavigation angewiesen sind
- Menschen mit Bewegungsempfindlichkeit
- Alle in einer ruhigen Umgebung (wie am Arbeitsplatz oder spätabends)

Lassen Sie Nutzer:innen selbst entscheiden, wann sie ein Video abspielen, indem Sie klare Steuerungen bereitstellen.

#### Vermeiden Sie blinkende oder stroboskopische Inhalte {#no-seizures}

Verwenden Sie keine Videos mit blinkenden oder stroboskopischen Effekten, insbesondere bei hoher Frequenz. Diese können bei Nutzer:innen mit photosensitiver Epilepsie Anfälle auslösen und bei anderen Unbehagen verursachen.

### Farbkontrast {#color-contrast}

Ausreichender Farbkontrast hilft sicherzustellen, dass Ihre Nachrichten für alle leicht lesbar sind, einschließlich Menschen mit Sehschwäche oder solchen, die Ihre Inhalte bei hellem Licht oder unter schwierigen Bedingungen betrachten. Streben Sie Kontrastverhältnisse an, die den [WCAG 2.2 AA-Anforderungen](https://www.w3.org/TR/WCAG/#contrast-minimum) entsprechen:

- 4,5:1 Kontrastverhältnis für normalen Text (Fließtext, Buttons und Links)
- 3:1 Kontrastverhältnis für großen Text (Überschriften und größere Beschriftungen)

Sie können Ihre Farbwahl mit dem [WebAim Contrast Checker Tool](https://webaim.org/resources/contrastchecker/) testen.

{% multi_lang_include accessibility/color.md %}

### Benutzerdefiniertes HTML {#custom-html}

Wenn Sie benutzerdefiniertes HTML in Ihren Nachrichten verwenden:

- Verwenden Sie [semantisches HTML](https://developer.mozilla.org/en-US/docs/Learn/Accessibility/HTML). Das bedeutet, die richtigen HTML-Elemente für ihren vorgesehenen Zweck zu verwenden, anstatt ein Element so zu gestalten, dass es wie ein anderes aussieht. Die meisten HTML-Elemente haben eine eigene integrierte Barrierefreiheitsunterstützung.
- Für die Sprache auf Dokumentebene, bei der Braze HTML-Metadaten beim Export hinzufügen kann, lesen Sie den Abschnitt [Barrierefreiheitssprache](#accessibility-language); das Verhalten variiert je nach Kanal. Wenn Sie Inhalte selbst auszeichnen, setzen Sie das [`lang`-Attribut](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/lang) in Ihrem HTML, um die Sprache Ihres Inhalts zu identifizieren. Screenreader verwenden für jede Sprache unterschiedliche Klangbibliotheken, basierend auf der Aussprache und den Eigenschaften dieser Sprache. Wenn dies nicht angegeben ist, nimmt ein Screenreader an, dass der Inhalt in der Standardsprache geschrieben ist, die der/die Nutzer:in beim Einrichten des Screenreaders gewählt hat. Wenn die Nachricht nicht tatsächlich in der Standardsprache verfasst ist, kann der Screenreader die Nachricht möglicherweise nicht korrekt aussprechen.

{% raw %}
```html
<html lang="en-us">
```
{% endraw %}

{% alert note %}
Bei Verwendung des E-Mail-Drag-and-Drop-Editors legen Sie die Sprache über den Tab **Einstellungen** fest, wenn diese Steuerung verfügbar ist. Vollständige Templates und reine Content-Block-E-Mails können unterschiedliche Standardwerte für die Barrierefreiheitssprache verwenden – siehe [Barrierefreiheitssprache](#accessibility-language). Andere Kanäle werden ebenfalls in diesem Abschnitt behandelt.
{% endalert %}

- Verwenden Sie [ARIA-Attribute](#aria-attributes), um zusätzlichen Kontext bereitzustellen. Diese Attribute liefern assistiven Technologien zusätzliche Informationen und helfen, die Rolle, den Zustand oder die Eigenschaften von UI-Elementen zu verdeutlichen, die andernfalls unklar sein könnten.

### ARIA-Attribute {#aria-attributes}

Wenn Sie benutzerdefinierten Code in Braze-Editoren verwenden, können Sie Accessible Rich Internet Applications ([ARIA](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA)) nutzen, um zusätzliche Barrierefreiheitsunterstützung für Nutzer:innen bereitzustellen, die auf assistive Technologien angewiesen sind. ARIA-Rollen und -Attribute helfen Screenreadern, Ihre Inhalte klarer zu interpretieren, besonders wenn Sie Elemente verwenden, die von sich aus keine Bedeutung vermitteln (wie `<div>` oder `<span>`).

{% alert important %}
Obwohl ARIA dafür konzipiert ist, Webinhalte barrierefreier zu machen, kann es bei falscher Verwendung mehr schaden als nützen. ARIA ersetzt kein semantisches HTML, es ergänzt es – verwenden Sie ARIA daher nur, wenn native HTML-Elemente Ihre Anforderungen nicht erfüllen.
{% endalert %}

Hier sind einige Beispiele, die besonders in Messaging-Kontexten nützlich sind:

- [aria-label](#aria-label)
- [aria-labelledby](#aria-labelledby)
- [aria-hidden="true"](#aria-hiddentrue)
- [role="presentation"](#rolepresentation)
- [aria-live="polite"](#aria-livepolite)

#### aria-label {#aria-label}

`aria-label` fügt Elementen, die keinen sichtbaren Text haben, einen barrierefreien Namen hinzu. Wenn Sie ein Symbol ohne Text verwenden (wie einen Papierkorb oder ein „X“ zum Schließen), weiß jemand, der einen Screenreader verwendet, nicht, was es tut – es sei denn, Sie beschriften es. `aria-label` gibt diesem Symbol eine Stimme.

{% raw %}
```html
<button aria-label="Close message">
  <svg ...></svg>
</button>
```
{% endraw %}

#### aria-labelledby {#aria-labelledby}

`aria-labelledby` verbindet ein Element mit etwas, das bereits ein sichtbares Label hat. Wenn Sie also ein Banner oder einen Bereich haben, der mit einem Titel laut vorgelesen werden soll, können Sie `aria-labelledby` verwenden, um assistiver Technologie mitzuteilen: „Verwende diese Überschrift dort drüben, um diesen Teil zu benennen.“

{% raw %}
```html
<h2 id="banner-title">Important Update</h2>
<div role="region" aria-labelledby="banner-title">...</div>
```
{% endraw %}

#### aria-hidden="true" {#aria-hiddentrue}

`aria-hidden="true"` verbirgt Dinge vor Screenreadern. Es ist hilfreich für Text oder visuelle Elemente, die keine wichtige Bedeutung vermitteln – wie ein Glitzern, ein Häkchen oder ein Emoji, das rein dekorativ verwendet wird.

Das hält das Erlebnis für Screenreader-Nutzer:innen sauberer, die sonst möglicherweise redundante oder verwirrende Inhalte hören würden. Es ist auch nützlich, um Dinge wie Offscreen-Akkordeon-Inhalte zu verbergen, die noch nicht aufgeklappt wurden.

{% raw %}
```html
<span aria-hidden="true">✔️</span>
```
{% endraw %}

Im Allgemeinen ist es besser, `alt=""` für [dekorative Bilder](#images) und Symbole zu verwenden als `aria-hidden="true"`. Während semantisches HTML von allen Screenreadern und assistiver Software weitgehend unterstützt wird, variiert die ARIA-Unterstützung. Selbst wenn Sie `aria-hidden` verwenden, sollten Sie trotzdem ein leeres Alt-Attribut einfügen.

#### role="presentation" {#rolepresentation}

`role="presentation"` teilt assistiver Technologie mit, rein layoutbezogene Elemente zu ignorieren, wie Design-Tabellen. E-Mails verwenden beispielsweise oft Tabellen nur zur Ausrichtung. Ohne diese Rolle könnten Screenreader annehmen, dass Ihr Layout eine Datentabelle ist, und beginnen, Zeilen- und Spaltennummern vorzulesen.

{% raw %}
```html
<table role="presentation">...</table>
```
{% endraw %}

E-Mails, die im E-Mail-Drag-and-Drop-Editor erstellt werden, haben Präsentationselemente automatisch mit dem ARIA-Attribut `role="presentation"` gekennzeichnet.

#### aria-live="polite" {#aria-livepolite}

`aria-live="polite"` kündigt Aktualisierungen an, wenn sich Inhalte ändern, ohne dass eine Nutzerinteraktion erforderlich ist. Verwenden Sie es, wenn Sie dynamische Aktualisierungen innerhalb einer Nachricht anzeigen, wie Erfolgsmeldungen, Fehler oder andere Benachrichtigungen.

{% raw %}
```html
<div aria-live="polite">Your preferences have been saved.</div>
```
{% endraw %}

## Automatisierte Barrierefreiheitstests {#automated-accessibility-testing}

Um Ihnen zu helfen, Barrierefreiheitsprobleme frühzeitig zu erkennen und zu beheben, bietet Braze automatisierte Barrierefreiheitstests in den folgenden Bereichen:

- [Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision#accessibility-testing) für E-Mails
- [Barrierefreiheits-Scanner]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=in-app%20message#accessibility-scanner) für Nachrichten, die mit unserem HTML-Editor erstellt wurden (zum Beispiel HTML-In-App-Nachrichten, HTML Content Blocks, [benutzerdefinierte E-Mail-Fußzeilen]({{site.baseurl}}/user_guide/channels/email/customize/custom_email_footer), [E-Mail-Opt-in-Seiten]({{site.baseurl}}/user_guide/channels/email/subscriptions#creating-a-custom-opt-in-page) und [E-Mail-Abmeldeseiten]({{site.baseurl}}/user_guide/channels/email/subscriptions#creating-a-custom-unsubscribe-page)).

Diese Tests prüfen Ihre Nachricht anhand des Standards der Web Content Accessibility Guidelines ([WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)) – einer Reihe international anerkannter technischer Standards für barrierefreie Inhalte. Alle Probleme, die automatisch erkannt werden können, werden markiert und nach Schweregrad kategorisiert, um Ihnen bei der Priorisierung zu helfen.

{% alert note %}
Inbox Vision funktioniert sowohl für HTML- als auch für Drag-and-Drop-E-Mails. Der Scanner läuft nur bei Inhalten, die mit dem HTML-Editor erstellt wurden.
{% endalert %}

### Was automatisierte Tests erkennen können und was nicht {#what-automated-testing-can-and-cant-catch}

Automatisierte Barrierefreiheitstests sind ein guter Ausgangspunkt – aber sie können nicht alles erkennen. Einige Probleme erfordern eine menschliche Beurteilung, besonders wenn Kontext oder visuelles Design eine Rolle dabei spielen, wie Nutzer:innen Ihre E-Mail erleben.

Möglicherweise sehen Sie einige Probleme, die als **Überprüfung erforderlich** markiert sind. Das sind Fälle, in denen der Checker nicht sicher feststellen kann, ob etwas ein Barrierefreiheitsproblem darstellt. In diesem Fall empfehlen wir, es manuell zu überprüfen.

Einige Beispiele für das, was automatisierte Tools nicht zuverlässig erkennen können:

- Ob die Fokusreihenfolge interaktiver Elemente einer logischen Abfolge folgt
- Ob Inhalte vollständig mit einer Tastatur bedienbar sind, ohne dass eine Maus erforderlich ist
- Ob Alt-Text ein Bild sinnvoll beschreibt
- Ob Überschriften richtig verwendet werden, um Inhalte zu strukturieren
- Ob Links und Buttons klar beschriftet und leicht verständlich sind
- Ob Touch-Ziele groß genug und angemessen beabstandet sind
- Ob Text auf Hintergrundbildern die Farbkontrastanforderungen erfüllt
- Ob Anweisungen oder Beschriftungen klar und für alle Nutzer:innen hilfreich sind

Diese Einschränkungen sind nicht Braze-spezifisch – sie gelten für alle automatisierten Barrierefreiheitstools. Automatisierte Prüfungen können nicht jede assistive Technologie, jeden Screenreader oder jedes Nutzerbedürfnis simulieren. Deshalb ist Barrierefreiheit keine einmalige Prüfung&#8212;sie ist eine kontinuierliche Praxis.

Selbst wenn Ihre Nachricht jede automatisierte Prüfung besteht, ist es dennoch wichtig:

- Markierte Probleme sorgfältig zu überprüfen, insbesondere solche, die als **Überprüfung erforderlich** gekennzeichnet sind.
- Wo möglich manuell zu testen, besonders bei Layout- und Interaktionsmustern.
- Tools wie Screenreader, reine Tastaturnavigation und Browser-Zoom zu verwenden, um verschiedene Zugangsbedürfnisse zu simulieren.

Indem Sie automatisierte Tests mit durchdachter manueller Überprüfung kombinieren, erkennen Sie mehr potenzielle Probleme und erstellen inklusivere, benutzerfreundlichere Campaigns für alle Empfänger:innen.