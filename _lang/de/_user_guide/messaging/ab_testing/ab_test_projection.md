---
nav_title: A/B-Test-Projektion
article_title: A/B-Test-Projektion
page_order: 20
hidden: true
page_type: reference
description: "Dieser Artikel erklärt, wie die A/B-Test-Projektion funktioniert, wie Sie eine Projektion durchführen und wie Braze Ihre Daten verwendet."
---

# A/B-Test-Projektion {#ab-test-projection}

> Die A/B-Test-Projektion verwendet neuronale Netzwerke, um vorherzusagen, welche Betreffzeilen am besten abschneiden. Unser Modell extrahiert sprachliche Merkmale aus erfolgreichen A/B-Tests, die auf Braze durchgeführt wurden, und nutzt diese statistischen Sprachmuster, um unserer KI beizubringen, was bessere Betreffzeilen ausmacht.

{% alert important %}
Dieses Feature befindet sich derzeit in der Early-Access-Phase. Wenden Sie sich an Ihren Braze-Kundenerfolgs- oder Account Manager, wenn Sie an einer Teilnahme am Early Access interessiert sind.
{% endalert %}

## Eine Projektion durchführen {#running-a-projection}

Fügen Sie bei der Campaign-Erstellung Ihre Nachrichtenvarianten und deren Betreffzeilen in den Editor ein. Wenn Sie bereit sind, gehen Sie zum Schritt **Target Audience** im Campaign-Erstellungsablauf. Wählen Sie im Panel **A/B Testing** die Option **Run Projection** aus.

<img width="518" alt="Bild" src="https://github.com/braze-inc/braze-docs/assets/17167198/8e74835c-76e4-4241-9763-c4f86a622c75">

Es öffnet sich ein Modal mit den Betreffzeilen aller Nachrichtenvarianten, die Sie bereits erstellt haben. Optional können Sie zusätzliche Betreffzeilen (bis zu maximal zehn) hinzufügen, indem Sie eine manuell in das Feld eingeben und die Projektion ausführen. Wählen Sie **Run Projection** aus.

<img width="722" alt="Bild" src="https://github.com/braze-inc/braze-docs/assets/17167198/f9ad45a3-6565-467b-a7f6-35277bef7699">

Die Betreffzeile, die unsere KI als beste vorhersagt, wird mit dem Label **Projected Winner** hervorgehoben.

{% alert note %}
Für [Push-Campaigns für mehrere Plattformen]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/multiple_platform_push) werden A/B-Tests unterstützt, wenn Sie mehrere Plattformen auswählen.
{% endalert %}

### Wie genau sind die Projektionen? {#how-accurate-are-the-projections}

In Tests haben wir festgestellt, dass die Projektionen bei der Auswahl zwischen Nachrichtenpaaren in echten A/B-Tests eine Genauigkeit von etwa 70 % aufweisen. Berücksichtigen Sie dies bei der Interpretation der Nachrichten, die das Modell als Gewinnervariante projiziert.

### Wie verwenden wir Ihre Daten? {#how-do-we-use-your-data}

Dieses Feature lernt aus vergangenen A/B-Tests, die auf Braze durchgeführt wurden. Der tatsächliche Text Ihrer Nachrichten oder der Nachrichten anderer Braze-Kund:innen wird dem Modell niemals zur Verfügung gestellt. Wir extrahieren zunächst die übergeordneten Sprachmuster, die erfolgreiche Nachrichten in A/B-Tests vorhersagen. Anschließend stellen wir diese Muster unserer KI zur Verfügung, um ihr beizubringen, welche sprachlichen Merkmale überlegene Betreffzeilen ausmachen.