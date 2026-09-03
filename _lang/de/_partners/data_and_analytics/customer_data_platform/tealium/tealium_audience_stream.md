---
nav_title: Tealium AudienceStream
article_title: Tealium AudienceStream
page_order: 2
alias: /partners/tealium_audience_stream/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Tealium, einem universellen Daten-Hub, der es Ihnen ermöglicht, mobile, Web- und alternative Daten mit anderen Drittanbieter-Quellen zu verbinden."
page_type: partner
search_tag: Partner

---

# Tealium AudienceStream

> Tealium [AudienceStream](https://docs.tealium.com/server-side/getting-started/audiencestream-cdp/introduction/) ist eine Omnichannel-Kundensegmentierung und Realtime-Action-Engine. AudienceStream nimmt die Daten, die in EventStream einfließen, und erstellt Besucherprofile, die die wichtigsten Attribute des Engagements Ihrer Kund:innen mit Ihrer Marke darstellen.

Die Integration von Braze und Tealium nutzt die AudienceStream-Besucherprofile. Gemeinsame Verhaltensweisen segmentieren diese Profile, um Gruppen von Besuchern mit gemeinsamen Merkmalen zu erstellen, die als Zielgruppen bezeichnet werden. Diese Zielgruppen können Ihren Marketingtechnologie-Stack in Realtime über Konnektoren unterstützen.

{% alert important %}
Tealium AudienceStreams und EventStreams bieten sowohl Batch- als auch Non-Batch-Konnektor-Aktionen. Der Non-Batch-Konnektor sollte verwendet werden, wenn Realtime-Anfragen für den Anwendungsfall wichtig sind und keine Bedenken bestehen, die Spezifikationen für die Rate-Limits der Braze-API zu überschreiten. Kontaktieren Sie den Braze-[Support]({{site.baseurl}}/braze_support) oder Ihren Customer-Success-Manager, wenn Sie Fragen haben.
{% endalert %}

## Voraussetzungen {#prerequisites}

| Name | Beschreibung |
| ---- | ----------- |
| Tealium-Konto | Ein [Tealium-Konto](https://my.tealiumiq.com/) mit serverseitigem Zugriff ist erforderlich. Wir empfehlen außerdem die Verwendung der clientseitigen Integrationen, um diese Partnerschaft optimal zu nutzen. |
| REST-API-Schlüssel | Ein Braze-REST-API-Schlüssel mit den Berechtigungen `users.track`, `users.delete` und `subscription.status.set`.<br><br>Dieser kann unter **Braze-Dashboard > Entwicklungskonsole > REST-API-Schlüssel > Neuen API-Schlüssel erstellen** erstellt werden. |
| [Braze-REST-Endpunkt]({{site.baseurl}}/api/basics#endpoints) | Ihre REST-Endpunkt-URL. Ihr Endpunkt hängt von der [Braze-URL für Ihre Instanz]({{site.baseurl}}/api/basics#endpoints) ab. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

### Schritt 1: Attribute und Badges einrichten {#step-1-set-up-attributes-and-badges}

#### Attribute verstehen {#understanding-attributes}

Der erste Schritt bei der Verwendung von AudienceStream besteht darin, Attribute zu erstellen. Attribute erlauben es Ihnen, die wichtigen Merkmale zu definieren, die die Gewohnheiten, Vorlieben, Aktionen und das Engagement eines Besuchers mit Ihrer Marke repräsentieren.

**Visit-Attribute**: Visit-Attribute beziehen sich auf den aktuellen Besuch (oder die Sitzung) der Nutzer:innen. Die in diesen Attributen gespeicherten Daten bleiben für die Dauer des Besuchs erhalten. Einige Beispiele für Visit-Attribute sind:
- Besuchsdauer (Zahl)
- Aktueller Browser (String)
- Aktuelles Gerät (String)
- Anzahl der Seitenaufrufe (Zahl)

**Visitor-Attribute**: Visitor-Attribute beziehen sich auf die aktuellen Nutzer:innen. Die in diesen Attributen gespeicherten Daten bleiben für die Lifetime der Nutzer:innen bestehen. Einige Beispiele für Visitor-Attribute sind:
- Lifetime-Bestellwert (Zahl)
- Vorname (String)
- Geburtsdatum (Datum)
- Gekaufte Marken (Tally)

Besuchen Sie [Tealium](https://docs.tealium.com/server-side/attributes/about/) für eine vollständige Liste der verfügbaren Datentypen.

##### Anreicherung von Attributen {#attribute-enrichment}

Sobald Sie die gewünschten Attribute identifiziert haben, können Sie diese mit [Anreicherungen](https://docs.tealium.com/server-side/getting-started/audiencestream-cdp/attributes-enrichments/) konfigurieren – Geschäftsregeln, die festlegen, wann und wie die Werte der Attribute aktualisiert werden sollen. Jeder Datentyp bietet eine eigene Auswahl an Anreicherungen, um den Wert des Attributs zu manipulieren. Dies steht im Zusammenhang mit der „WHEN“-Einstellung. Die folgenden Optionen stehen für jedes Visit- und Visitor-Attribut zur Verfügung:

- New Visitor: tritt auf, wenn ein Besucher zum ersten Mal auf Ihre Website kommt.
- New Visit: tritt bei einem neuen Besuch eines Besuchers auf.
- Any Event: tritt bei jedem Ereignis ein.
- Visit Ended: tritt auf, wenn ein Besuch endet.

Sie können auch eine angepasste Bedingung, eine sogenannte Regel, erstellen, die bestimmt, wann die Anreicherung stattfindet.

#### Badges

Badges sind spezielle Visitor-Attribute, die wertvolle Verhaltensmuster darstellen. Badges werden Besuchern auf der Grundlage der Logik ihrer Anreicherungen zugewiesen oder entzogen. Diese Logik kombiniert in der Regel mehrere Bedingungen, um Besuchersegmente zu erfassen, oder legt einen Schwellenwert fest, wenn ein bestimmter Wert erreicht wird.

#### Attribut- und Badge-Beispiel {#attribute-and-badge-example}

{% tabs local %}
{% tab Attribut %}

Erstellen Sie ein Visitor-Attribut „Lifetime Order Value“, das den kumulativen Betrag berechnet, den die Kund:innen für alle abgeschlossenen Bestellungen (Kauf-Event) ausgegeben haben (`order_total`). Um den Lifetime-Bestellwert in Ihrem Tealium-Konto einzurichten, befolgen Sie die folgenden Anweisungen:

1. Navigieren Sie zu **AudienceStream > Visitor/Visit Attributes** und klicken Sie auf **Add Attribute**.
2. Wählen Sie den Bereich als **Visitor** aus und klicken Sie auf **Continue**.
3. Wählen Sie den Datentyp **Number** aus und klicken Sie auf **Continue**.
4. Geben Sie den Namen des Attributs ein: „Lifetime Order Value“.
5. Klicken Sie auf **Add Enrichment** und wählen Sie **Increment or Decrement Number**.
6. Wählen Sie das Attribut aus, das den Wert enthält, um den erhöht werden soll (`order_total`).
7. Lassen Sie „WHEN“ auf „Any Event“ eingestellt und klicken Sie dann auf **Create a New Rule**.
8. Erstellen Sie eine Regel, die feststellt, wann ein Kauf-Event stattgefunden hat.
9. Klicken Sie auf **Save** und dann auf **Finish**.

Jetzt wird allen Kund:innen ein Lifetime-Bestellwert-Attribut zugewiesen.

{% endtab %}
{% tab Badge %}

Sie können Badges erstellen, die Ihnen helfen, Ihre Nutzer:innen anhand bestimmter Attribute zu klassifizieren und gezielt anzusprechen. Im folgenden Beispiel erstellen wir ein VIP-Badge für Nutzer:innen mit einem „Lifetime Order Value“ von über 500 $.

1. Navigieren Sie zu **AudienceStream > Visitor/Visit Attributes** und klicken Sie auf **Add Attribute**.
2. Wählen Sie den Bereich als **Visitor** aus und klicken Sie auf **Continue**.
3. Wählen Sie den Datentyp **Badge** aus und klicken Sie auf **Continue**.
4. Geben Sie den Namen des Badges ein: „VIP“.
5. Klicken Sie auf **Add Enrichment** und wählen Sie **Assign Badge**.
6. Lassen Sie „WHEN“ auf „Any Event“ eingestellt.
7. Erstellen Sie eine Regel für die Badge-Zuweisung, indem Sie **Create Rule** auswählen. Weisen Sie dieser Regel einen Titel zu und setzen Sie die Regel mithilfe des zuvor erstellten Attributs auf „...has attribute „Lifetime Order Value greater than 500“.
8. Klicken Sie auf **Save** und dann auf **Finish**.

{% endtab %}
{% endtabs %}

### Schritt 2: Eine Zielgruppe erstellen {#step-2-create-an-audience}

Wählen Sie auf der Tealium-Startseite unter **AudienceStream** in der Seitenleiste **Audiences** aus. Hier können Sie eine Zielgruppe von Nutzer:innen mit gemeinsamen Attributen erstellen. Der Eintritt oder Austritt von Nutzer:innen aus dieser Zielgruppe ist der Auslöser für die im nächsten Schritt eingerichtete Konnektor-Aktion, die diese Informationen an das Nutzerprofil in Braze weitergibt.

Benennen Sie zunächst Ihre Zielgruppe und überlegen Sie dann, welche Attribute auf die Art der Zielgruppe zutreffen, die Sie erstellen möchten. Um zum Beispiel eine Zielgruppe von VIP-Nutzer:innen zu erstellen, könnten Sie eine Zielgruppe von Besuchern erstellen, die das **VIP-Badge** haben.

Vergewissern Sie sich, dass Sie Ihre Zielgruppe **speichern/veröffentlichen**, wenn Sie fertig sind.

### Schritt 3: Einen Event-Konnektor erstellen {#step-3-create-an-event-connector}

Ein Konnektor ist eine Integration zwischen Tealium und einem anderen Anbieter, die zur Übertragung von Daten verwendet wird. Diese Konnektoren enthalten Aktionen, die die unterstützten APIs des Partners repräsentieren.

1. Navigieren Sie in der Seitenleiste von Tealium unter **Server-Side** zu **AudienceStream > Audience Connectors**.
2. Wählen Sie den blauen Button **+ Add Connector**, um den Konnektor-Marktplatz zu durchsuchen. In dem neu erscheinenden Dialogfeld verwenden Sie die Spotlight-Suche, um den **Braze**-Konnektor zu finden.
3. Um diesen Konnektor hinzuzufügen, klicken Sie auf die **Braze**-Konnektor-Kachel. Wenn Sie darauf klicken, können Sie die Verbindungsübersicht und eine Liste der erforderlichen Informationen, der unterstützten Aktionen und der Konfigurationsanweisungen anzeigen. Die Konfiguration umfasst drei Schritte: Quelle, Konfiguration und Aktion.

#### Quelle {#source}

Wählen Sie im daraufhin angezeigten **Source**-Dialog die Zielgruppe aus, die Sie im vorherigen Schritt erstellt haben, und einen Auslöser, den Sie für Ihre Situation für geeignet halten. Sie können auch die Frequenzbegrenzung aktivieren, um zu kontrollieren, wie oft diese Aktion ausgelöst wird.

![Konfiguration der AudienceStream-Konnektor-Quelle in Tealium mit Zielgruppen- und Auslöser-Auswahl.]({% image_buster /assets/img/tealium/create_source.png %}){: style="max-width:90%;"}

#### Konfiguration {#configuration}

Als Nächstes wird ein **Configuration**-Dialog angezeigt. Wählen Sie unten auf der Seite **Add Connector** aus. Benennen Sie Ihren Konnektor und geben Sie hier Ihren Braze-API-Endpunkt und den Braze-REST-API-Schlüssel an.

![Tealium-Konnektor-Konfigurationsdialog mit Feldern für Braze-Endpunkt und REST-API-Schlüssel.]({% image_buster /assets/img/tealium/create_configuration.png %}){: style="max-width:70%;"}

Wenn Sie bereits einen Konnektor erstellt haben, können Sie optional einen vorhandenen Konnektor aus der Liste der verfügbaren Konnektoren verwenden und ihn mit dem Bleistiftsymbol an Ihre Bedürfnisse anpassen oder mit dem Papierkorbsymbol löschen.

Nachdem Sie einen Konnektor zur Verknüpfung dieser Zielgruppe erstellt oder ausgewählt haben, klicken Sie auf **Done**, um fortzufahren.

#### Aktion {#action}

Benennen Sie als Nächstes Ihre Konnektor-Aktion und wählen Sie einen Aktionstyp aus, der Daten gemäß der von Ihnen konfigurierten Abbildung sendet. Hier bilden Sie Braze-Attribute auf Tealium-Attributnamen ab. Je nachdem, welchen Aktionstyp Sie auswählen, gibt es eine unterschiedliche Auswahl an Feldern, die Tealium benötigt. Im Folgenden finden Sie Beispiele und Erläuterungen zu diesen Feldern.

{% alert important %}
Nicht alle angebotenen Felder sind erforderlich.

![Tealium-Aktions-Abbildungspanel mit optionalen Feldern, die minimiert werden können.]({% image_buster /assets/img/tealium/minimize.gif %}){: style="max-width:90%"}
{% endalert %}

{% tabs local %}
{% tab Track User – Batch und Non-Batch %}

Mit dieser Aktion können Sie Nutzer:innen-, Event- und Kauf-Attribute in einer einzigen Aktion tracken. Obwohl die Aktion „Track User“ sowohl für AudienceStream als auch für EventStream gleich ist, empfiehlt Tealium, die Abbildungen der Nutzerattribute mit AudienceStream-Aktionen und die Event- und Kauf-Abbildungen mit EventStream-Aktionen einzurichten.

| Parameter | Beschreibung |
| ---------- | ----------- |
| Nutzer-ID | Verwenden Sie dieses Feld, um das Tealium-Nutzer-ID-Feld auf das entsprechende Braze-Feld abzubilden. Bilden Sie ein oder mehrere Nutzer-ID-Attribute ab. Wenn mehrere IDs angegeben werden, wird der erste nicht-leere Wert in der folgenden Prioritätsreihenfolge ausgewählt: Externe ID, Braze ID, Alias-Name und Alias-Label.<br><br>- Externe ID und Braze ID sollten beim Import von Push-Tokens nicht angegeben werden.<br>- Wenn Sie einen Nutzer-Alias angeben, sollten Alias-Name und Alias-Label festgelegt werden. <br><br>Weitere Informationen finden Sie unter dem Braze-[Endpunkt `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track). |
| Nutzerattribute | Verwenden Sie die vorhandenen Feldnamen der Braze-Nutzerprofile, um die Werte der Nutzerprofile im Braze-Dashboard zu aktualisieren, oder fügen Sie den Nutzerprofilen Ihre eigenen angepassten [Nutzerattribut]({{site.baseurl}}/api/objects_filters/user_attributes_object)-Daten hinzu.<br><br>- Standardmäßig werden neue Nutzer:innen angelegt, wenn noch keine vorhanden sind.<br>- Wenn Sie **Update Existing Only** auf `true` setzen, werden nur vorhandene Nutzer:innen aktualisiert und keine neuen Nutzer:innen angelegt.<br>- Wenn ein Tealium-Attribut leer ist, wird es in Null umgewandelt und aus dem Braze-Nutzerprofil entfernt. Anreicherungen sollten verwendet werden, wenn keine Nullwerte an Braze gesendet werden sollen, um ein Nutzerattribut zu entfernen. |
| Nutzerattribute ändern | Verwenden Sie dieses Feld, um bestimmte Nutzerattribute zu erhöhen oder zu verringern.<br><br>- Integer-Attribute können um positive oder negative ganze Zahlen inkrementiert werden.<br>- Array-Attribute können durch Hinzufügen oder Entfernen von Werten in bestehenden Arrays geändert werden. |
| Event | Ein Event stellt ein einzelnes Vorkommen eines angepassten Events durch bestimmte Nutzer:innen zu einem bestimmten Zeitstempel dar. Verwenden Sie dieses Feld zum Tracking und zur Abbildung von Event-Attributen, wie sie im Braze-[Event-Objekt]({{site.baseurl}}/api/objects_filters/event_object) enthalten sind. <br><br>- Das Event-Attribut `Name` ist für jedes zugeordnete Event erforderlich.<br>- Das Event-Attribut `Time` wird automatisch auf „jetzt“ gesetzt, wenn es nicht explizit abgebildet wird. <br>- Standardmäßig werden neue Events erstellt, wenn noch keines vorhanden ist. Wenn Sie `Update Existing Only` auf `true` setzen, werden nur bestehende Events aktualisiert und es wird kein neues Event erstellt.<br>- Bilden Sie Array-Typ-Attribute ab, um mehrere Events hinzuzufügen. Array-Typ-Attribute müssen gleich lang sein.<br>- Einzelwert-Attribute können verwendet und auf jedes Event angewendet werden. |
| Event-Template | Stellen Sie Event-Templates zur Verfügung, auf die in den Body-Daten referenziert werden kann. Templates können verwendet werden, um Daten zu transformieren, bevor sie an Braze gesendet werden. Weitere Informationen finden Sie in der [Template-Anleitung](https://docs.tealium.com/server-side/connectors/webhook-connectors/trimou-templating-engine/) von Tealium. |
| Event-Template-Variable | Stellen Sie Event-Template-Variablen als Dateneingabe bereit. Weitere Informationen finden Sie im [Leitfaden für Template-Variablen](https://docs.tealium.com/server-side/connectors/webhook-connectors/template-variables/) von Tealium. |
| Kauf | Verwenden Sie dieses Feld, um Nutzer-Kaufattribute zu tracken und abzubilden, wie sie im Braze-[Kauf-Objekt]({{site.baseurl}}/api/objects_filters/purchase_object) enthalten sind.<br><br>- Die Kaufattribute `Product ID`, `Currency` und `Price` sind für jeden zugeordneten Kauf erforderlich.<br>- Das Kaufattribut `Time` wird automatisch auf „jetzt“ gesetzt, wenn es nicht explizit abgebildet wird.<br>- Standardmäßig werden neue Käufe angelegt, wenn noch keine vorhanden sind. Wenn Sie `Update Existing Only` auf `true` setzen, werden nur bestehende Käufe aktualisiert und es wird kein neuer Kauf angelegt.<br>- Bilden Sie Array-Typ-Attribute ab, um mehrere Kaufartikel hinzuzufügen. Array-Typ-Attribute müssen gleich lang sein.<br>- Einzelwert-Attribute können verwendet werden und gelten dann für jeden Artikel. |
| Kauf-Template | Templates können verwendet werden, um Daten zu transformieren, bevor sie an Braze gesendet werden.<br>- Definieren Sie ein Kauf-Template, wenn Sie Unterstützung für verschachtelte Objekte benötigen.<br>- Wenn ein Kauf-Template definiert wird, wird die Konfiguration, die im Kaufbereich Ihrer Aktion eingerichtet wurde, ignoriert.<br>- Weitere Informationen finden Sie in der [Template-Anleitung](https://docs.tealium.com/server-side/connectors/webhook-connectors/trimou-templating-engine/) von Tealium. |
| Kauf-Template-Variable | Stellen Sie Produkt-Template-Variablen als Dateneingabe bereit. Weitere Informationen finden Sie im [Leitfaden für Template-Variablen](https://docs.tealium.com/server-side/connectors/webhook-connectors/template-variables/) von Tealium. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Aktion" }

![Beispiel einer Tealium-Track-User-Aktion mit zugeordneten Nutzerattributen und Event-Feldern.]({% image_buster /assets/img/tealium/track_user_example2.png %}){: style="max-width:90%"}

{% endtab %}
{% tab Delete User – Non-Batch %}

Diese Aktion erlaubt es Ihnen, Nutzer:innen aus dem Braze-Dashboard zu löschen.

| Parameter | Beschreibung |
| ---------- | ----------- |
| Nutzer-ID | Verwenden Sie dieses Feld, um das Tealium-Nutzer-ID-Feld auf das entsprechende Braze-Feld abzubilden.<br><br>- Bilden Sie ein oder mehrere Nutzer-ID-Attribute ab. Wenn mehrere IDs angegeben werden, wird der erste nicht-leere Wert in der folgenden Prioritätsreihenfolge ausgewählt: Externe ID, Braze ID, Alias-Name und Alias-Label.<br>- Wenn Sie einen Nutzer-Alias angeben, sollten sowohl Alias-Name als auch Alias-Label festgelegt werden.<br><br>Weitere Informationen finden Sie unter dem Braze-[Endpunkt `/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Aktion" }

![Tealium-Delete-User-Aktion mit konfigurierten Braze-Nutzer-ID-Abbildungen.]({% image_buster /assets/img/tealium/track_user_delete2.png %}){: style="max-width:90%"}

{% endtab %}
{% tab Abo-Gruppenstatus aktualisieren – Non-Batch %}
Mit dieser Aktion können Sie Nutzer:innen zu Braze-SMS- oder E-Mail-Abo-Gruppen hinzufügen oder daraus entfernen.

| Parameter | Beschreibung |
| ---------- | ----------- |
| Gruppentyp | Verwenden Sie dieses Feld, um anzugeben, ob es sich um eine SMS- oder E-Mail-Abo-Gruppe handelt. |
| Update-Typ | Bilden Sie diese Aktion auf ein Abmelde- oder Abo-Ereignis ab. |
| Attribute | - Abo-Gruppen-ID (erforderlich): Die ID der Abo-Gruppe, die sich auf den im vorhergehenden Feld abgebildeten Gruppentyp bezieht.<br>- Externe ID: Die externe ID der Nutzer:innen.<br><br>E-Mail-gruppenspezifisch:<br>- E-Mail: Die E-Mail-Adresse der Nutzer:innen.<br>**Wenn die externe ID nicht definiert ist, wird die E-Mail benötigt.**<br><br>SMS-gruppenspezifisch:<br>- Telefon: Die Telefonnummer im Format E.164. Zum Beispiel: +14155552671.<br>**Wenn die externe ID nicht definiert ist, wird die Telefonnummer benötigt.** |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Aktion" }

![Tealium-Aktion zum Aktualisieren des Abo-Gruppenstatus mit Abbildungen für Gruppentyp und Update-Typ.]({% image_buster /assets/img/tealium/update_subscription.png %}){: style="max-width:90%"}

{% endtab %}
{% endtabs %}

Wählen Sie **Finish**.

#### Zusammenfassung {#summary}

Sehen Sie sich die Zusammenfassung des von Ihnen erstellten Konnektors an. Wenn Sie die von Ihnen gewählten Optionen ändern möchten, wählen Sie **Back** zum Bearbeiten oder **Finish** zum Abschließen.

Ihr Konnektor wird nun in der Liste der Konnektoren auf Ihrer Tealium-Startseite angezeigt.

Stellen Sie sicher, dass Sie Ihren Konnektor speichern oder veröffentlichen, wenn Sie fertig sind. Die von Ihnen konfigurierten Aktionen werden nun ausgelöst, wenn die Trigger-Verbindungen erfüllt sind.

### Schritt 4: Ihren Tealium-Konnektor testen {#step-4-test-your-tealium-connector}

Nachdem Ihr Konnektor betriebsbereit ist, sollten Sie ihn testen, um sicherzustellen, dass er ordnungsgemäß funktioniert. Der einfachste Weg, dies zu testen, ist die Verwendung des Tealium **Trace Tools**. Um Trace nutzen zu können, müssen Sie die Tealium-Tools-Browsererweiterung hinzugefügt haben.

1. Um einen neuen Trace zu starten, wählen Sie **Trace** in der Seitenleiste unter **Server-Side**-Optionen. Klicken Sie auf **Start** und erfassen Sie die Trace-ID.
2. Öffnen Sie die Browsererweiterung und geben Sie die Trace-ID in AudienceStream Trace ein.
3. Prüfen Sie das Realtime-Protokoll.
4. Suchen Sie nach der Aktion, die Sie validieren möchten, indem Sie auf den Eintrag **Actions Triggered** klicken, um ihn zu erweitern.
5. Suchen Sie nach der Aktion, die Sie validieren möchten, und sehen Sie sich den Protokollstatus an.

Ausführlichere Anweisungen zur Implementierung des Trace-Tools von Tealium finden Sie in der [Trace-Dokumentation](https://docs.tealium.com/server-side/connectors/trace/about/) von Tealium.

## Integrationsdemo {#integration-demo}

<div class="video-container">
  <iframe width="560" height="315" src="https://drive.google.com/file/d/1m2JI4vdFt3fDePBdVvVcQWEjbC82ApGA/preview" title="Tealium AudienceStream Integrationsdemo" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Mögliche Datenpunkt-Mehrkosten {#potential-data-point-overages}

Es gibt drei Hauptursachen, durch die bei der Integration von Braze über Tealium versehentlich Datenpunkt-Mehrkosten entstehen können:

### Doppelte Daten senden – nur Braze-Deltas von Attributen senden {#sending-duplicate-data-only-send-braze-deltas-of-attributes}
Tealium sendet keine Braze-Deltas von Nutzerattributen. Wenn Sie beispielsweise eine EventStream-Aktion haben, die den Vornamen, die E-Mail-Adresse und die Handynummer eines Nutzers bzw. einer Nutzerin erfasst, sendet Tealium bei jedem Auslösen der Aktion alle drei Attribute an Braze. Tealium prüft nicht, was sich geändert hat oder aktualisiert wurde, um nur diese Informationen zu senden.<br><br>
**Lösung**: <br>Sie können Ihr Backend überprüfen, um festzustellen, ob sich ein Attribut geändert hat, und falls ja, die entsprechenden Tealium-Methoden aufrufen, um das Nutzerprofil zu aktualisieren. **Dies ist das übliche Vorgehen von Nutzer:innen, die Braze direkt integrieren.** <br>**ODER**<br> Wenn Sie keine eigene Version eines Nutzerprofils in Ihrem Backend speichern und nicht feststellen können, ob sich Attribute geändert haben, können Sie AudienceStream nutzen und [Enrichments erstellen](https://docs.tealium.com/server-side/attributes/manage-enrichments/add-enrichment/), um Nutzerattribute nur dann zu senden, wenn sich Werte geändert haben.

#### Irrelevante Daten senden oder Daten unnötig überschreiben {#sending-irrelevant-data-or-needlessly-overwriting-data}
Wenn Sie mehrere EventStreams haben, die denselben Event-Feed ansprechen, werden **alle für diesen Konnektor aktivierten Aktionen** automatisch ausgelöst, sobald eine einzelne Aktion getriggert wird. **Dies kann auch dazu führen, dass Daten in Braze überschrieben werden.**<br><br>
**Lösung**: <br>Richten Sie eine separate Event-Spezifikation oder einen separaten Feed ein, um jede Aktion zu verfolgen. <br>**ODER**<br> Deaktivieren Sie Aktionen (oder Konnektoren), die nicht ausgelöst werden sollen, indem Sie die Umschalter im Tealium-Dashboard verwenden.

#### Braze zu früh initialisieren {#initializing-braze-too-early}
Wenn Sie die Integration mit Tealium über den Braze Web SDK Tag durchführen, kann es zu einem drastischen Anstieg Ihrer MAU kommen. **Wenn Braze beim Laden der Seite initialisiert wird, erstellt Braze jedes Mal ein anonymes Profil, wenn ein:e Web-Nutzer:in die Website zum ersten Mal besucht.** Dies schließt Bot-Traffic ein, was Ihre Anzahl aktiver Nutzer:innen künstlich aufblähen kann. Einige möchten das Nutzerverhalten möglicherweise erst erfassen, wenn Nutzer:innen eine bestimmte Aktion abgeschlossen haben, wie z. B. „Angemeldet“ oder „Video angesehen“, um ihre MAU-Anzahl zu senken. <br><br>
**Lösung**: <br>Richten Sie [Laderegeln](https://docs.tealium.com/iq-tag-management/load-rules/about/) ein, um genau festzulegen, wann und wo ein Tag auf Ihrer Website geladen wird. Eine umfassendere Anleitung zum Filtern von Bot-Traffic und zur bedingten Initialisierung des SDK finden Sie unter [Bot-Traffic filtern]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web#web_bot-filtering).