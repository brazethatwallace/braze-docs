---
nav_title: Kameleoon
article_title: Kameleoon
description: "Erfahren Sie, wie Sie Kameleoon in Braze integrieren"
alias: /partners/kameleoon/
page_type: partner
search_tag: Partner
---

# Kameleoon

>[Kameleoon](https://www.kameleoon.com) ist eine Optimierungslösung mit Funktionen für Experimente, KI-gestützte Personalisierung und Feature-Management in einer einzigen, einheitlichen Plattform.

## Voraussetzungen {#prerequisites}

Bevor Sie beginnen, benötigen Sie Folgendes:

| Anforderung | Beschreibung |
| --- | --- |
| Kameleoon-Konto | Ein Kameleoon-Konto ist erforderlich, um diese Partnerschaft zu nutzen. |
| Braze-Konto | Ein aktives Braze-Konto mit dem [Braze Web SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web), das auf Ihrer Webseite integriert ist. Außerdem muss die Segmentierung nach Event-Eigenschaften aktiviert sein. Informationen zur Anfrage finden Sie unter [Hinweise](#considerations). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Anwendungsfälle {#use-cases}

Kameleoon sendet angepasste Events an Braze, um Nutzer:innen zu identifizieren, die an Experimenten und Personalisierungs-Campaigns teilnehmen, und ermöglicht so ein präziseres Targeting und personalisiertes Messaging.

## Integration von Kameleoon {#integrating-kameleoon}

Diese Integration wird als JavaScript-Tracker über Kameleoons engine.js ausgeführt. Sie kann direkt über die Kameleoon-Plattform aktiviert werden.

### Schritt 1: Navigieren Sie zur Kameleoon-Integrationsseite {#step-1-go-to-the-kameleoon-integrations-page}

Wählen Sie in Ihrer Kameleoon-App in der Seitenleiste **Admin** und dann **Integrations** aus.

![Das Admin-Panel in der Kameleoon-Plattform.]({% image_buster /assets/img/kameleoon/img_1.png %}){: style="max-width:70%;"}

### Schritt 2: Installieren Sie das Braze-Tool {#step-2-install-the-braze-tool}

Standardmäßig ist das Braze-Tool nicht installiert. Suchen Sie das Braze-Symbol und wählen Sie dann **Install the tool** aus. ![Ein graues Quadrat mit einem nach unten zeigenden Pfeil.]({% image_buster /assets/img/kameleoon/img_2.png %})

Wählen Sie die Projekte aus, für die Sie das Braze-Tool aktivieren möchten, damit die Kameleoon-Daten korrekt an Braze übermittelt werden.

![Das Braze-Tool-Symbol in Kameleoon.]({% image_buster /assets/img/kameleoon/img_3.png %})

Nachdem Sie das Tool konfiguriert haben, wählen Sie **Validate** aus. Dadurch wird das Konfigurationspanel geschlossen. Neben dem Symbol des Braze-Tools erscheint ein **ON**-Schalter, einschließlich der Anzahl der Projekte, für die das Tool konfiguriert ist.

![Das Braze-Tool in Kameleoon auf „On“ umgeschaltet.]({% image_buster /assets/img/kameleoon/img_4.png %})

### Schritt 3: Verknüpfen Sie Braze mit Kameleoon-Campaigns {#step-3-associate-braze-with-kameleoon-campaigns}

#### Im grafischen Editor/Code-Editor {#in-the-graphiccode-editor}

Um Ihr Experiment abzuschließen, wählen Sie den Schritt **Integrations** aus, um Braze als Tracking-Tool zu konfigurieren, und wählen Sie dann **Braze** aus.

![Das Integrations-Dashboard in Kameleoon mit allen verfügbaren Integrationen, einschließlich der aktiven Integration Braze.]({% image_buster /assets/img/kameleoon/img_5.png %})

Braze wird in der Zusammenfassung vor der Veröffentlichung erwähnt. Kameleoon überträgt die Daten automatisch an Braze, und Sie können sie direkt in Braze für Analysen und Segmentierung nutzen.

##### Personalisierungserstellung {#personalization-creation}

Auf der Seite **Personalization Creation** können Sie Braze unter den Reporting-Tools auswählen, um Ihr Reporting zu personalisieren.

![Bereich „Reporting Tools“ mit Integrationen wie Heap, Mixpanel, Clarity, wobei Braze ausgewählt ist.]({% image_buster /assets/img/kameleoon/img_6.png %})

##### Feature-Flag-Erstellung {#feature-flag-creation}

Richten Sie die Integration in der Feature-Flag-Umgebung im Abschnitt **Integrations** ein. Aktivieren Sie sie für die Umgebungen, in denen sie aktiv sein soll.

![Die Feature-Flag-Seite in Kameleoon mit verfügbaren Integrationen. Für jeden Partner gibt es zwei Schalter: „Delivery rules“ und „Feature experiments“.]({% image_buster /assets/img/kameleoon/img_7.png %})

##### Ergebnisseite {#results-page}

Nachdem Braze als Reporting-Tool für ein Experiment festgelegt wurde, können Sie es auf der Kameleoon-Ergebnisseite im Menü **Experiment configuration** auswählen (oder abwählen).

{% alert note %}
Diese Integration erfordert eine [hybride Implementierung](https://developers.braze-presentation.preview.kameleoon.net/core-concepts/hybrid-experimentation?language=en#sending-exposure-events-to-third-party-analytics) und ist nur mit Web-SDKs kompatibel.
{% endalert %}

![Das Seitenpanel der Ergebnisseite in Kameleoon.]({% image_buster /assets/img/kameleoon/img_8.png %}){: style="max-width:50%;" }

Die mit dem Experiment verknüpften Reporting-Tools werden angezeigt. Wählen Sie **Edit** aus, um diese Auswahl zu bearbeiten.

### Schritt 4: Analysieren und nutzen Sie Ihre Kameleoon-Daten in Braze {#step-4-analyze-and-leverage-your-kameleoon-data-in-braze}

Nachdem die Integration eingerichtet ist, sendet Kameleoon angepasste Events namens `kameleoon_exposure` mit Eigenschaften wie **Experiment name**, **Experiment ID**, **Variation name** und **Variation ID** an Braze.

![Das Event-Nutzerprotokoll für angepasste Events in Braze, das ein Beispiel-Payload des von Kameleoon empfangenen Events zeigt.]({% image_buster /assets/img/kameleoon/img_9.png %})

Sie können diese Daten dann unter „Custom Events“ anzeigen, Berichte über angepasste Events erstellen, um die Kameleoon-Campaign-Exposition zu identifizieren, und die Segmentierung basierend auf Event-Eigenschaften aktivieren. Sie können angepasste Events verwenden, wenn Sie nachfolgende oder verknüpfte Campaigns und Canvases über [Aktionspfade]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths#action-groups), [aktionsbasierte Trigger]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery) oder beim Erstellen von [Segments]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) erstellen.

Darüber hinaus sind diese Events über [Currents-Objekte für angepasste Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) zugänglich, um umfassende Berichte und Analysen zu ermöglichen.

## Hinweise {#considerations}

### Segmentierung nach Event-Eigenschaften anfordern {#request-event-property-segmentation}

Bevor Sie die Segmentierung nach Event-Eigenschaften nutzen können, muss diese in Braze aktiviert werden. Verwenden Sie die folgende Vorlage, um Ihren Braze CSM oder das Support-Team um Zugang zu bitten.

   <table aria-label="Segmentierung nach Event-Eigenschaften anfordern">
     <caption>Segmentierung nach Event-Eigenschaften anfordern</caption>
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
   {: .reset-td-br-1 .reset-td-br-2 aria-label="Segmentierung nach Event-Eigenschaften anfordern" }

### Braze-Datenpunkte {#braze-data-points}

Das von Kameleoon an Braze gesendete angepasste Event – einschließlich aller für die Segmentierung aktivierten Event-Eigenschaften – protokolliert Datenpunkte in Ihrer Braze-Instanz.