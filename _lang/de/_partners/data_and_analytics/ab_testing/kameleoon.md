---
nav_title: Kameleoon
article_title: Kameleoon
description: "Erfahren Sie, wie Sie Kameleoon in Braze integrieren"
alias: /partners/kameleoon/
page_type: partner
search_tag: Partner
---

# Kameleoon

>[Kameleoon](https://www.kameleoon.com) ist eine Optimierungslösung mit Funktionen für Experimente, KI or künstliche Intelligenz-gestützte Personalisierung und Feature-Management in einer einzigen, einheitlichen Plattform.

## Voraussetzungen {#prerequisites}

Bevor Sie beginnen, benötigen Sie Folgendes:

| Anforderung | Beschreibung |
| --- | --- |
| Kameleoon-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Kameleoon-Konto. |
| Braze-Konto | Ein aktives Braze-Konto mit dem auf Ihrer Webseite integrierten [Braze Web SDK or Software-Development-Kit]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web). Außerdem muss die Segmentierung nach Event-Eigenschaften aktiviert sein. Informationen zur Anforderung finden Sie unter [Überlegungen](#considerations). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Anwendungsfälle {#use-cases}

Kameleoon sendet angepasste Events an Braze, um Nutzer:innen zu identifizieren, die an Experimentier- und Personalisierungskampagnen teilnehmen, und ermöglicht so ein präziseres Targeting und personalisiertes Messaging.

## Integration von Kameleoon {#integrating-kameleoon}

Diese Integration läuft als JavaScript-Tracker über Kameleoons engine.js. Sie kann schnell innerhalb der Kameleoon-Plattform aktiviert werden.

### 1. Schritt: Navigieren Sie zur Kameleoon-Integrationsseite {#step-1-go-to-the-kameleoon-integrations-page}

Wählen Sie in Ihrer Kameleoon-App **Admin** und dann **Integrations** in der Seitenleiste.

![Das Admin-Panel in der Kameleoon-Plattform.]({% image_buster /assets/img/kameleoon/img_1.png %}){: style="max-width:70%;"}

### 2. Schritt: Installieren Sie das Braze-Tool {#step-2-install-the-braze-tool}

Standardmäßig ist das Braze-Tool nicht installiert. Suchen Sie nach dem Braze-Symbol und wählen Sie dann **Install the tool**. ![Ein graues Quadrat mit einem nach unten zeigenden Pfeil.]({% image_buster /assets/img/kameleoon/img_2.png %})

Wählen Sie die Projekte aus, für die Sie das Braze-Tool aktivieren möchten, damit die Kameleoon-Daten korrekt an Braze übermittelt werden.

![Das Braze-Tool-Symbol in Kameleoon.]({% image_buster /assets/img/kameleoon/img_3.png %})

Nachdem Sie das Tool konfiguriert haben, wählen Sie **Validate**, um das Konfigurationspanel zu schließen. Neben dem Symbol des Braze-Tools sehen Sie dann einen **ON**-Schalter sowie die Anzahl der Projekte, für die das Tool konfiguriert ist.

![Das Braze-Tool in Kameleoon auf „On“ geschaltet.]({% image_buster /assets/img/kameleoon/img_4.png %})

{% alert important %}
Dieses Feature befindet sich in der Beta-Phase. Nehmen Sie am [Kameleoon-Beta-Programm](https://help.kameleoon.com/account-and-team-management/join-beta-program/) teil, um diese Integration zu nutzen.
{% endalert %}

### 3. Schritt: Verknüpfen Sie Braze mit Kameleoon-Kampagnen {#step-3-associate-braze-with-kameleoon-campaigns}

#### Im Grafik-/Code-Editor {#in-the-graphiccode-editor}

Um Ihr Experiment abzuschließen, wählen Sie den Schritt **Integrations**, um Braze als Tracking-Tool zu konfigurieren, und wählen Sie dann **Braze**.

![Das Integrations-Dashboard in Kameleoon mit allen verfügbaren Integrationen, einschließlich der aktiven Integration Braze.]({% image_buster /assets/img/kameleoon/img_5.png %})

Braze wird in der Zusammenfassung erwähnt, bevor Sie live gehen. Kameleoon überträgt die Daten automatisch an Braze, und Sie können sie direkt in Braze für Analyse und Segmentierung verwenden.

##### Personalisierung erstellen {#personalization-creation}

Auf der Seite **Personalization Creation** können Sie Braze unter den Berichtstools auswählen, um Ihre Berichte zu personalisieren.

![Der Abschnitt „Reporting Tools“ zeigt Integrationen wie Heap, Mixpanel, Clarity, wobei Braze ausgewählt ist.]({% image_buster /assets/img/kameleoon/img_6.png %})

##### Feature-Flag erstellen {#feature-flag-creation}

Richten Sie die Integration in der Feature-Flag-Umgebung im Abschnitt **Integrations** ein. Aktivieren Sie sie für die Umgebungen, in denen sie aktiv sein soll.

![Die Feature-Flag-Seite in Kameleoon mit den verfügbaren Integrationen. Für jeden Partner gibt es zwei Schalter: „Delivery rules“ und „Feature experiments“.]({% image_buster /assets/img/kameleoon/img_7.png %})

##### Ergebnisseite {#results-page}

Nachdem Braze als Berichtstool für ein Experiment festgelegt wurde, können Sie es auf der Kameleoon-Ergebnisseite im Menü **Experiment configuration** auswählen (oder die Auswahl aufheben).

{% alert note %}
Diese Integration erfordert eine [hybride Implementierung](https://developers.braze-presentation.preview.kameleoon.net/core-concepts/hybrid-experimentation?language=en#sending-exposure-events-to-third-party-analytics) und ist nur mit Web-SDKs kompatibel.
{% endalert %}

![Das Seitenpanel der Ergebnisseite in Kameleoon.]({% image_buster /assets/img/kameleoon/img_8.png %}){: style="max-width:50%;" }

Die mit dem Experiment verknüpften Berichtstools werden angezeigt. Wählen Sie **Edit**, um diese Auswahl zu ändern.

### 4. Schritt: Analysieren und nutzen Sie Ihre Kameleoon-Daten in Braze {#step-4-analyze-and-leverage-your-kameleoon-data-in-braze}

Nachdem die Integration eingerichtet ist, sendet Kameleoon angepasste Events namens `kameleoon_exposure` mit Eigenschaften wie **Experiment name**, **Experiment ID**, **Variation name** und **Variation ID** an Braze.

![Das Event-Nutzerprotokoll für angepasste Events in Braze mit einer Beispiel-Payload des Events, das Braze von Kameleoon erhalten hat.]({% image_buster /assets/img/kameleoon/img_9.png %})

Sie können diese Daten dann unter den angepassten Events einsehen, angepasste Event-Berichte erstellen, um die Exposition gegenüber Kameleoon-Kampagnen zu ermitteln, und eine Segmentierung auf Basis von Event-Eigenschaften aktivieren. Sie können angepasste Events verwenden, wenn Sie nachfolgende oder verknüpfte Campaigns und Canvase über [Aktionspfade]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/#action-groups), [aktionsbasierte Trigger or triggern]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/) oder die Erstellung von [Segmenten]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/) erstellen.

Darüber hinaus sind diese Events über [angepasste Event-Objekte von Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/) zugänglich, um eine umfassende Berichterstattung und Analyse zu ermöglichen.

## Überlegungen {#considerations}

### Segmentierung nach Event-Eigenschaften anfragen {#request-event-property-segmentation}

Bevor Sie die Segmentierung nach Event-Eigenschaften verwenden können, muss diese in Braze aktiviert werden. Verwenden Sie das folgende Template, um Ihren Braze-CSM or Customer-Success-Manager oder das Support-Team zu kontaktieren und den Zugang anzufragen.

   <table aria-label="Segmentierung nach Event-Eigenschaften anfragen">
     <caption>Segmentierung nach Event-Eigenschaften anfragen</caption>
   <thead>
      <tr>
         <th>Feld</th>
         <th>Details</th>
      </tr>
   </thead>
   <tbody>
      <tr>
         <td><strong>Betreff</strong></td>
         <td>Request to Enable Event Property Segmentation for Kameleoon Integration</td>
      </tr>
      <tr>
         <td><strong>Nachricht</strong></td>
         <td>
         Hello Braze Team,<br><br>
         We would like to enable event property segmentation for events sent from our Kameleoon&lt;&gt;Braze integration. Here are the details:<br><br>
         - <strong>Event Name:</strong> Kameleoon<br>
         - <strong>Event Properties:</strong> <code>kameleoon_campaign_name</code>, <code>kameleoon_variation_name</code><br><br>
         Please confirm once the properties have been enabled in our account.<br><br>
         Thank you.
         </td>
      </tr>
   </tbody>
   </table>
   {: .reset-td-br-1 .reset-td-br-2 aria-label="Segmentierung nach Event-Eigenschaften anfragen" }

### Braze-Datenpunkte {#braze-data-points}

Das angepasste Event, das von Kameleoon an Braze gesendet wird&#8212;einschließlich aller für die Segmentierung aktivierten Event-Eigenschaften&#8212;protokolliert Datenpunkte in Ihrer Braze-Instanz.