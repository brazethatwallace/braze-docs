---
nav_title: VWO
article_title: Integration von VWO mit Braze
description: "Erfahren Sie, wie Sie VWO in Braze integrieren können."
alias: /partners/vwo/
page_type: partner
search_tag: Partner
---

# VWO

> [VWO](https://vwo.com/) ist eine leistungsstarke Experimentierplattform, die Marken hilft, wichtige Geschäftsmetriken zu verbessern, indem sie Teams in die Lage versetzt, Programme zur Conversion-Optimierung auf der Grundlage von Daten zum Kundenverhalten durchzuführen. Mit VWO können Sie Kundendaten vereinheitlichen, Insights über das Verhalten gewinnen, Hypothesen aufstellen, A/B-Tests über mehrere Plattformen (Server, Web und Mobilgerät) durchführen, Features einführen, Erlebnisse personalisieren und die gesamte Customer Journey optimieren.

Durch die Integration von VWO mit Braze können Sie VWO-Experimentdaten nutzen, um gezielte Segmente zu erstellen und personalisierte Campaigns zuzustellen.

## Voraussetzungen {#prerequisites}

| Anforderung     | Beschreibung |
|-----------------|-------------|
| VWO-Konto     | Ein VWO-Konto mit Zugang zu Experimentierdaten. |
| Braze-Konto   | Ein aktives Braze-Konto mit Integration des [Braze Web SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web) auf Ihrer Webseite. Sie müssen außerdem die Segmentierung von Event-Eigenschaften aktivieren lassen. Informationen zur Anfrage finden Sie unter [Überlegungen](#request-event-property-segmentation). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration von VWO mit Braze {#integrating-vwo-with-braze}

### 1. Schritt: Aktivieren Sie die Braze-Integration in VWO {#step-1-enable-the-braze-integration-in-vwo}

1. Melden Sie sich bei Ihrem VWO-Konto an.
2. Gehen Sie im VWO-Dashboard zu **Configurations > Integrations**. Hier können Sie Integrationen auf Workspace-Ebene aktivieren, wodurch die Integration standardmäßig auf alle zukünftigen Testkampagnen angewendet wird.

   ![VWO-Integrationskonfiguration]({% image_buster /assets/img/vwo/vwo1_settings.png %})

4. Wählen Sie die Braze-Integration aus, um sie zu aktivieren.
5. Optional können Sie die Braze-Integration für bestehende Campaigns aktivieren. Wählen Sie dazu eine Campaign aus, gehen Sie dann zu **Configuration > Integrations** und aktivieren Sie Braze.

   ![Braze-Integration aktivieren]({% image_buster /assets/img/vwo/vwo2_enable_braze.png %})

6. Nachdem Sie die Integration aktiviert haben, beginnt VWO damit, Experimentdaten auf Campaign-Ebene an Braze zu senden.

### 2. Schritt: Erstellen Sie ein Segment in Braze mit VWO-Event-Eigenschaften {#step-2-create-a-segment-in-braze-with-vwo-event-properties}

1. Wählen Sie im Braze-Dashboard **Segments** > **+ Segment erstellen**.
3. Geben Sie im Fenster **Segment erstellen** einen Namen für das Segment ein und wählen Sie dann **Segment erstellen**.
4. Wählen Sie in Ihrem neu erstellten Segment **Filter** > **Filter hinzufügen** und wählen Sie dann **Angepasstes Event** als Filtertyp.
6. Suchen Sie in der Filter-Dropdown-Liste nach **VWO**.
7. Wählen Sie die entsprechende VWO-Eigenschaft aus und geben Sie den gewünschten Wert an.
8. Konfigurieren Sie bei Bedarf die Anzahl der Besuche und den Zeitrahmen. Wenn Sie fertig sind, wählen Sie **Speichern**.

   ![Braze-Segment erstellen]({% image_buster /assets/img/vwo/vwo3_braze_segment.png %})

9. Um die Anzahl der Nutzer:innen anzuzeigen, die Ihren Segmentkriterien entsprechen, wählen Sie **Exakte Statistik berechnen**.

   ![Braze-Segment-Statistik]({% image_buster /assets/img/vwo/vwo4_braze_segment_calculate_size.png %})

## Datenfluss {#data-flow}

VWO sendet die Daten der Campaign-Experimente als angepasstes Event im folgenden Format an Braze:

- **Event-Name:** VWO
- **Event-Eigenschaften:** `vwo_campaign_name`, `vwo_variation_name`

{% alert tip %}
Diese angepassten Event-Eigenschaften können auch zur Segmentierung und zum Targeting verwendet werden.
{% endalert %}

## Überlegungen {#considerations}

### Segmentierung von Event-Eigenschaften anfragen {#request-event-property-segmentation}

Bevor Sie die Segmentierung von Event-Eigenschaften verwenden können, müssen Sie diese in Braze aktivieren lassen. Verwenden Sie das folgende Template, um Ihren Braze-CSM oder das Support-Team zu kontaktieren.

   <table aria-label="Segmentierung von Event-Eigenschaften anfragen">
     <caption>Segmentierung von Event-Eigenschaften anfragen</caption>
   <thead>
      <tr>
         <th>Feld</th>
         <th>Details</th>
      </tr>
   </thead>
   <tbody>
      <tr>
         <td><strong>Betreff</strong></td>
         <td>Anfrage zur Aktivierung der Segmentierung von Event-Eigenschaften für die VWO-Integration</td>
      </tr>
      <tr>
         <td><strong>Nachricht</strong></td>
         <td>
         Hallo Braze-Team,<br><br>
         Wir möchten die Segmentierung von Event-Eigenschaften für Events aktivieren, die von unserer VWO&lt;&gt;Braze-Integration gesendet werden. Hier sind die Details:<br><br>
         - <strong>Event-Name:</strong> VWO<br>
         - <strong>Event-Eigenschaften:</strong> <code>vwo_campaign_name</code>, <code>vwo_variation_name</code><br><br>
         Bitte bestätigen Sie, sobald die Eigenschaften in unserem Konto aktiviert wurden.<br><br>
         Vielen Dank.
         </td>
      </tr>
   </tbody>
   </table>
   {: .reset-td-br-1 .reset-td-br-2 aria-label="Segmentierung von Event-Eigenschaften anfragen" }

### Braze-Datenpunkte {#braze-data-points}

Das angepasste Event, das von VWO an Braze gesendet wird&#8212;einschließlich aller für die Segmentierung aktivierten Event-Eigenschaften&#8212;protokolliert Datenpunkte in Ihrer Braze-Instanz.

### Einschränkungen

Derzeit unterstützt diese Integration keine Realtime-Synchronisation von Testdaten. Es kann eine Verzögerung von bis zu 15 Minuten geben, bis die Testdaten in Braze erscheinen.

## Fehlerbehebung {#troubleshooting}

Wenn Sie keine VWO-Daten in Braze sehen:

1. Rechtsklicken Sie auf die Seite, auf der Ihre Testkampagne läuft, und wählen Sie **Element inspizieren**.
2. Suchen Sie auf dem Tab **Netzwerk** nach **Braze**, um die Netzwerkaufrufe für Braze zu filtern.
3. Die Netzwerkaufrufe werden beim Laden der Seite aufgefüllt. Sie können die Seite neu laden, um die Netzwerkaufrufe zu sehen.
4. Wählen Sie einen Netzwerkaufruf aus, um weitere Details zu sehen.
5. Gehen Sie zum Abschnitt **Request Payload** im Tab **Payload**, wo Sie events: finden, die den Namen **ce** tragen, was auf ein Custom Event hinweist.
6. Erweitern Sie 0: und data:, um n: „VWO“ (Name des angepassten Events) und p: {vwo_campaign_name: „<Ihr VWO-Campaign-Name>“, vwo_variation_name: „<Variantenname>“} zu sehen. Diese zeigen an, dass die Werte von VWO an Braze gepusht werden.

 ![Braze-Fehlerbehebung]({% image_buster /assets/img/vwo/vwo5_troubleshooting.png %})

Wenn Sie zusätzliche Unterstützung benötigen, wenden Sie sich an Ihren CSM von VWO.