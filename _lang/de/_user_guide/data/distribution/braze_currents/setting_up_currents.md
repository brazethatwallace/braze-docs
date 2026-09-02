---
nav_title: Currents einrichten
article_title: Currents einrichten
page_order: 1
page_type: tutorial
description: "Diese Anleitung führt Sie durch die Integration und Konfiguration von Braze-Currents."
tool: Currents
search_rank: 8
---

# [![Braze-Lernkurs]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/currents-the-basics-2/){: style="float:right;width:120px;border:0;" class="noimgborder"}Currents einrichten {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomcurrents-the-basics-2-stylefloatrightwidth120pxborder0-classnoimgborderset-up-currents}

> Auf dieser Seite wird der allgemeine Prozess zur Integration und Konfiguration von Braze-Currents beschrieben.

{% alert important %}
Currents sind in bestimmten Braze-Paketen enthalten. Wenden Sie sich an Ihre Vertretung von Braze, wenn Sie Fragen haben oder Zugang erhalten möchten.
{% endalert %}

## Fehlerbehebung {#troubleshooting}

### Neue Currents-Integration kann nicht hinzugefügt werden {#cannot-add-a-new-currents-integration}

Wenn beim Hinzufügen einer neuen Integration die Meldung „You do not have any remaining Currents integrations“ angezeigt wird oder der Button zum Hinzufügen eines neuen Currents-Konnektors ausgegraut ist, sind häufige Ursachen:

- Für diesen Workspace wurde kein Currents-Kontingent erworben.
- Das Currents-Kontingent ist in einem anderen Workspace Ihres Unternehmens verfügbar.

Um das Problem zu beheben, prüfen Sie andere Workspaces in Ihrem Unternehmen. Ein anderer Workspace zeigt möglicherweise ein verfügbares Currents-Kontingent an. Wenn Sie ein Kontingent anfordern oder Ihre Konfiguration anpassen müssen, wenden Sie sich an Ihren Braze Account Manager:in.

### Zusätzliches Event-Tracking kann nicht aktiviert werden {#cannot-enable-additional-event-tracking}

Wenn Sie einen Konnektor erstellen oder bearbeiten können, aber einen der optionalen Tracking-Schalter nicht aktivieren können, hat Ihr Workspace möglicherweise ein Kontingentlimit für diese Event-Kategorie erreicht.

- **Track Customer Behavior and User Events** erfordert verfügbare Kontingente für **Customer Behavior Events**.
- **Track user profiles and attributes** erfordert verfügbare Kontingente für **User Profiles and Attributes**.

Wenn Sie zusätzliche Kontingente benötigen oder Hilfe bei der Anpassung Ihrer Konfiguration brauchen, wenden Sie sich an Ihren Braze Account Manager:in.

## Anforderungen {#requirements}

Die Verwendung von Currents mit einem unserer Partner erfordert dieselben grundlegenden Parameter und dieselbe Verbindungsmethodik.

Jeder Partner setzt voraus, dass Braze die Berechtigung hat, Datendateien an ihn zu schreiben und zu senden, und Braze fragt nach dem Speicherort, an den diese Dateien geschrieben werden sollen – insbesondere Bucket-Namen oder Schlüssel.

Die folgenden Anforderungen sind die grundlegenden Mindestanforderungen für die Integration mit den meisten unserer Partner. Einige Partner erfordern zusätzliche Parameter, die in der jeweiligen [Partnerdokumentation]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners) zusammen mit etwaigen Besonderheiten dieser grundlegenden Anforderungen aufgeführt sind.

| Anforderung | Herkunft | Zugang | Beschreibung
|---|---|---|---|
| Konto beim Partner | Richten Sie ein Konto bei dem Partner ein oder wenden Sie sich an Ihren Braze Account Manager:in für Vorschläge. | Besuchen Sie die Website des Partners oder kontaktieren Sie den Partner, um sich zu registrieren. | Braze sendet keine Daten an einen Partner, wenn Sie über das Konto Ihres Unternehmens keinen Zugriff auf diese Daten haben.
| Partner-API-Schlüssel oder Token / Textbaustein | In der Regel im Dashboard des Partners. | Kopieren Sie ihn und fügen Sie ihn in das entsprechende Braze-Feld ein. | Braze stellt dafür ein eigenes Feld auf der Integrationsseite des jeweiligen Partners bereit. Wir benötigen dies, um festzulegen, wohin wir Ihre Daten senden. **Halten Sie Ihre Partner-Schlüssel oder Token / Textbaustein aktuell. Ungültige Zugangsdaten können Ihren Konnektor deaktivieren und dazu führen, dass Events verworfen werden.**
| Authentifizierungscode/-schlüssel, geheimer Schlüssel, Zertifikatsdatei | Wenden Sie sich an eine Vertretung Ihres Kontos bei dem Partner. Kann auch im Dashboard des Partners zu finden sein. | Kopieren Sie die Schlüssel und fügen Sie sie in das entsprechende Braze-Feld ein. Generieren und laden Sie `.json`- oder andere Zertifikatsdateien an der entsprechenden Stelle in Braze hoch. | Braze stellt dafür ein eigenes Feld auf der Integrationsseite des jeweiligen Partners bereit. Dies gibt Braze die Zugangsdaten und berechtigt uns, Dateien in Ihr Partnerkonto zu schreiben. **Es ist wichtig, Ihre Authentifizierungsdetails aktuell zu halten. Ungültige Zugangsdaten können dazu führen, dass Ihr Konnektor deaktiviert wird und Events verworfen werden.**
| Bucket, Ordnerpfad | Einige Partner organisieren und sortieren Daten nach Buckets. Dies sollte im Dashboard des Partners zu finden sein. | Falls erforderlich, kopieren Sie den Bucket-Namen oder Dateipfad exakt in das dafür vorgesehene Feld in Braze. | Obwohl dies nur bei einigen Partnern erforderlich ist, ist es wichtig, die Angaben korrekt zu machen, wenn Sie sie benötigen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Anforderungen" }

{% alert important %}
Es ist wichtig, Ihre Partner-Schlüssel, Partner-Token / Textbaustein und Authentifizierungsdetails aktuell zu halten. Wenn die Zugangsdaten Ihres Konnektors ablaufen, stellt der Konnektor den Versand von Events ein. Wenn dies länger als **5 Tage** andauert, werden die Events des Konnektors verworfen und Daten gehen dauerhaft verloren.
{% endalert %}

## Einrichtung von Currents {#setting-up-currents}

### 1. Schritt: Partner auswählen {#step-1-choose-your-partner}

Braze-Currents ermöglicht die Integration über Data-Warehouse-Speicherung mithilfe von Flat-Files oder über unsere Partner für Verhaltensanalysen und Kundendaten mithilfe von gebündelten JSON-Payloads an einen bestimmten Endpunkt.

Bevor Sie mit der Integration beginnen, sollten Sie entscheiden, welche Integration für Ihre Zwecke am besten geeignet ist. Wenn Sie beispielsweise bereits mParticle und Segment nutzen und Braze-Daten dorthin streamen möchten, empfiehlt sich die Verwendung eines gebündelten JSON-Payloads. Wenn Sie die Daten lieber selbst bearbeiten oder ein komplexeres System zur Datenanalyse verwenden möchten, ist Data-Warehouse-Speicherung möglicherweise die bessere Wahl ([Braze verwendet diese Methode]({{site.baseurl}}/user_guide/data/distribution/braze_currents/use_cases/how_braze_uses_currents)!).

### 2. Schritt: Currents öffnen {#step-2-open-currents}

Navigieren Sie zu **Partnerintegrationen** > **Currents**. Sie werden zur Verwaltungsseite für Currents-Integrationen weitergeleitet.

![Currents-Seite im Braze-Dashboard]({% image_buster /assets/img_archive/currents-main-page.png %})

### 3. Schritt: Partner hinzufügen {#step-3-add-your-partner}

Fügen Sie einen Partner hinzu – manchmal auch als „Currents-Konnektor“ bezeichnet –, indem Sie das Dropdown-Menü oben auf dem Bildschirm auswählen.

Jeder Partner erfordert andere Konfigurationsschritte. Um eine Integration zu aktivieren, lesen Sie unsere Liste der [verfügbaren Partner]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners) und folgen Sie den Anweisungen auf den jeweiligen Seiten.

{% multi_lang_include currents/contact_email_notifications.md %}

### 4. Schritt: Events konfigurieren {#step-4-configure-your-events}

Wählen Sie die Events aus, die Sie an diesen Partner übermitteln möchten, indem Sie die verfügbaren Optionen markieren. Eine Auflistung dieser Events finden Sie in unseren Bibliotheken für [Kundenverhalten-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) und [Nachrichteninteraktion-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events).

![Currents-Konfigurationsseite mit ausgewählten Partner-Events für den Export.]({% image_buster /assets/img/current4.png %})

Bei Bedarf erfahren Sie mehr über unsere Events im Artikel zur [Semantik der Zustellung von Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/event_delivery_semantics).

### 5. Schritt: Feldtransformationen einrichten {#step-5-set-up-field-transformations}

Sie können Currents-Feldtransformationen verwenden, um ein String-Feld zu entfernen oder zu hashen.

- **Entfernen:** Ersetzt das String-Feld durch `[REDACTED]`. Dies ist hilfreich, wenn Ihr Partner Events mit fehlenden oder leeren Feldern ablehnt.
- **Hashen:** Wendet einen SHA-256-Hashing-Algorithmus auf das String-Feld an.

Wenn Sie ein Feld für eine dieser Transformationen auswählen, wird die Transformation auf alle Events angewendet, in denen dieses Feld vorkommt. Wenn Sie beispielsweise `email_address` zum Hashen auswählen, wird das Feld `email_address` in E-Mail-Versand-, E-Mail-Öffnungs-, E-Mail-Bounce- und Abo-Gruppenstatusänderungs-Events gehasht.

![Feldtransformationen hinzufügen]({% image_buster /assets/img/current3.png %})

### 6. Schritt: Integration testen {#step-6-test-your-integration}

{% alert important %}
Currents verwirft Events mit übermäßig großen Payloads von mehr als 900&nbsp;KB.
{% endalert %}

Bevor Sie testen, sollten Sie sich unsere [Currents-Beispieldaten auf GitHub](https://github.com/Appboy/currents-examples) ansehen. Wenn Sie bereit zum Testen sind, wählen Sie eine Option im folgenden Abschnitt:

#### Test-Events senden {#sending-test-events}

Um Ihre Integration zu testen, können Sie **Test-Events senden** auswählen, um jeweils ein Event von allen ausgewählten Event-Typen an diesen Current zu senden. Ausführliche Informationen zu jedem Event-Typ finden Sie in unseren Bibliotheken für [Kundenverhalten-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) und [Nachrichteninteraktion-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events).

![Die Seite „Currents Test“ im Braze-Dashboard.]({% image_buster /assets/img/currents/current_test_events.png %}){: style="max-width:70%;"}

#### Test-Currents-Konnektoren {#testing-currents-connectors}

Test-Currents-Konnektoren sind kostenlose Versionen unserer bestehenden Konnektoren, die zum Testen und Ausprobieren verschiedener Ziele verwendet werden können. Test-Currents bieten:

- Bis zu 10 Test-Currents-Konnektoren pro Workspace.
- Ein aggregiertes Maximum von 1.500 Events pro festem 24-Stunden-Zeitraum, der um Mitternacht UTC zurückgesetzt wird. Dieser Event-Gesamtwert wird stündlich im Dashboard aktualisiert.

Nachdem Ihre Test-Currents-Konnektoren das Sendelimit erreicht haben, sendet Ihr Konnektor bis zum nächsten Tag (um Mitternacht UTC) keine Events mehr.

Um Ihren Test-Currents-Konnektor upzugraden, bearbeiten Sie die Integration im Dashboard und wählen Sie **Test-Integration upgraden**.

## Currents aktualisieren {#updating-currents}

{% multi_lang_include currents/updating_currents.md %}

## IP-Allowlisting {#ip-allowlisting}

Braze sendet Currents-Daten von den aufgelisteten IPs:

{% multi_lang_include administer/data_centers.md datacenters='ips' %}