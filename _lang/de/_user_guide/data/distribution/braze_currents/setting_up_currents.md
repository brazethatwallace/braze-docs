---
nav_title: Currents einrichten
article_title: Currents einrichten
page_order: 1
page_type: tutorial
description: "Diese Anleitung führt Sie durch die Integration und Konfiguration von Braze-Currents."
tool: Currents
search_rank: 8
---

# [![Braze-Lernkurs]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/currents-the-basics-2/){: style="float:right;width:120px;border:0;" class="noimgborder"} Currents einrichten {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomcurrents-the-basics-2-stylefloatrightwidth120pxborder0-classnoimgborderset-up-currents}

> Auf dieser Seite wird der allgemeine Prozess zur Integration und Konfiguration von Braze-Currents beschrieben.

{% alert important %}
Currents sind in bestimmten Braze-Paketen enthalten. Wenden Sie sich an Ihre Vertretung von Braze, wenn Sie Fragen haben oder Zugang erhalten möchten.
{% endalert %}

Wenn beim Hinzufügen einer neuen Integration die Meldung „You do not have any remaining Currents integrations“ angezeigt wird, sind häufige Ursachen:

- Für diesen Workspace wurde kein Currents-Anspruch erworben.
- Der Currents-Anspruch ist in einem anderen Workspace Ihres Unternehmens verfügbar.

Wenden Sie sich an Ihren Braze-Account Manager, um einen Anspruch anzufordern oder Ihre Konfiguration anzupassen.

## Anforderungen {#requirements}

Die Verwendung von Currents mit einem unserer Partner erfordert dieselben grundlegenden Parameter und Verbindungsmethoden.

Jeder Partner benötigt die Erlaubnis von Braze, Daten zu schreiben und an ihn zu senden, und Braze fragt nach dem Standort, an den diese Dateien geschrieben werden sollen, insbesondere Bucket-Namen oder Schlüssel.

Die folgenden Anforderungen sind die grundlegenden Mindestanforderungen für die Integration mit den meisten unserer Partner. Einige Partner verlangen zusätzliche Parameter, die in der jeweiligen [Partnerdokumentation]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners/) aufgeführt sind, zusammen mit allen Besonderheiten, die mit diesen Grundanforderungen verbunden sind.

| Anforderung | Herkunft | Zugang | Beschreibung
|---|---|---|---|
| Konto bei einem Partner | Richten Sie ein Konto bei diesem Partner ein oder wenden Sie sich an Ihren Braze-Account Manager, um Vorschläge zu erhalten. | Besuchen Sie die Website des Partners oder kontaktieren Sie den Partner für die Registrierung. | Braze sendet keine Daten an einen Partner, wenn Sie nicht über Ihr Unternehmenskonto Zugriff auf diese Daten haben.
| Partner-API-Schlüssel oder Token | Normalerweise das Dashboard des Partners. | Kopieren Sie den Wert und fügen Sie ihn in das dafür vorgesehene Braze-Feld ein. | Braze hat dafür ein eigenes Feld auf der Integrationsseite für diesen Partner. Wir benötigen diese Informationen für die Zuordnung, wohin wir Ihre Daten übermitteln. **Bitte halten Sie Ihre Partnerschlüssel oder Tokens auf dem neuesten Stand; ungültige Zugangsdaten können Ihren Konnektor deaktivieren und Events verwerfen.**
| Authentifizierungscode/-schlüssel, geheimer Schlüssel, Zertifizierungsdatei | Kontaktieren Sie eine Vertretung für Ihr Konto bei diesem Partner. Kann auch im Dashboard des Partners vorhanden sein. | Kopieren Sie die Schlüssel und fügen Sie sie in das vorgesehene Braze-Feld ein. Generieren Sie `.json` oder andere Zertifizierungsdateien und laden Sie sie an die entsprechende Stelle in Braze hoch. | Braze hat dafür ein eigenes Feld auf der Integrationsseite für diesen Partner. Damit erhält Braze Zugangsdaten und wird autorisiert, Dateien auf Ihr Partner-Konto zu schreiben. **Es ist wichtig, dass Sie Ihre Authentifizierungsdaten auf dem neuesten Stand halten. Ungültige Zugangsdaten können dazu führen, dass Ihr Konnektor deaktiviert wird und Events verworfen werden.**
| Bucket, Ordnerpfad | Einige Partner organisieren und sortieren Daten nach Buckets. Dies sollte im Dashboard des Partners zu finden sein. | Falls erforderlich, kopieren Sie den Bucket-Namen oder den Dateipfad exakt in das dafür vorgesehene Feld in Braze. | Obwohl dies nur für einige Partner erforderlich ist, ist es wichtig, die Angaben korrekt einzutragen, wenn Sie sie benötigen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Anforderungen" }

{% alert important %}
Es ist wichtig, dass Sie Ihre Partner-Schlüssel, Partner-Tokens und Authentifizierungsdaten auf dem neuesten Stand halten. Wenn die Zugangsdaten Ihres Konnektors ablaufen, wird der Konnektor keine Events mehr senden. Sollte dieser Zustand länger als **5 Tage** andauern, werden die Events des Konnektors verworfen und die Daten gehen dauerhaft verloren.
{% endalert %}

## Currents einrichten {#setting-up-currents}

### 1. Schritt: Wählen Sie Ihren Partner {#step-1-choose-your-partner}

Braze-Currents ermöglicht Ihnen die Integration durch Datenspeicherung unter Verwendung von Flat Files oder zu unseren Partnern für Verhaltensanalysen und Kundendaten unter Verwendung von gebündelten JSON-Payloads an einen bestimmten Endpunkt.

Bevor Sie mit der Integration beginnen, sollten Sie entscheiden, welche Integration für Ihre Zwecke am besten geeignet ist. Wenn Sie beispielsweise bereits mParticle und Segment verwenden und Braze-Daten dorthin streamen möchten, wäre es am besten, einen gebündelten JSON-Payload zu verwenden. Wenn Sie die Daten lieber selbst bearbeiten möchten oder ein komplexeres System zur Datenanalyse haben, ist es vielleicht am besten, die Datenspeicherung zu verwenden ([Braze verwendet diese Methode]({{site.baseurl}}/user_guide/data/distribution/braze_currents/use_cases/how_braze_uses_currents/)!)

### 2. Schritt: Currents öffnen {#step-2-open-currents}

Um zu beginnen, gehen Sie zu **Partnerintegrationen** > **Currents**. Sie gelangen auf die Seite zur Verwaltung der Currents-Integration.

![Seite „Currents“ im Braze-Dashboard]({% image_buster /assets/img_archive/currents-main-page.png %})

### 3. Schritt: Ihren Partner hinzufügen {#step-3-add-your-partner}

Fügen Sie einen Partner hinzu, der manchmal auch als „Currents-Konnektor“ bezeichnet wird, indem Sie das Dropdown-Menü oben auf dem Bildschirm auswählen.

Für jeden Partner sind andere Konfigurationsschritte erforderlich. Um die einzelnen Integrationen zu aktivieren, sehen Sie sich unsere Liste der [verfügbaren Partner]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners/) an und folgen Sie den Anweisungen auf den jeweiligen Seiten.

### 4. Schritt: Events konfigurieren {#step-4-configure-your-events}

Wählen Sie die Events, die Sie an diesen Partner weitergeben möchten, indem Sie die gewünschten Optionen ankreuzen. Eine Auflistung dieser Events finden Sie in unseren Bibliotheken [Kundenverhalten-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/) und [Messaging-Engagement-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/).

![]({% image_buster /assets/img/current4.png %})

Bei Bedarf erfahren Sie mehr über unsere Events in unserem Artikel zur [Semantik der Zustellung von Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/event_delivery_semantics/).

### 5. Schritt: Feldtransformationen einrichten {#step-5-set-up-field-transformations}

Sie können Currents-Feldtransformationen verwenden, um ein String-Feld zu entfernen oder zu hashen.

- **Entfernen:** Ersetzt das String-Feld durch `[REDACTED]`. Dies ist hilfreich, wenn Ihr Partner Events mit fehlenden oder leeren Feldern ablehnt.
- **Hash:** Wendet einen SHA-256-Hashing-Algorithmus auf das String-Feld an.

Wenn Sie ein Feld für eine dieser Transformationen auswählen, wird diese Transformation auf alle Events angewendet, in denen dieses Feld vorkommt. Wenn Sie zum Beispiel `email_address` für die Hash-Funktion auswählen, wird das Feld `email_address` in den Events E-Mail-Versand, E-Mail-Öffnung, E-Mail-Bounce und Statusänderung der Abo-Gruppe gehasht.

![Hinzufügen von Feldtransformationen]({% image_buster /assets/img/current3.png %})

### 6. Schritt: Testen Sie Ihre Integration {#step-6-test-your-integration}

{% alert important %}
Currents verwirft Events mit übermäßig großen Payloads von mehr als 900&nbsp;KB.
{% endalert %}

Bevor Sie testen, sollten Sie sich unsere [Currents-Beispieldaten auf GitHub](https://github.com/Appboy/currents-examples) ansehen. Wenn Sie zum Testen bereit sind, wählen Sie unten eine Option aus:

#### Test-Events versenden {#sending-test-events}

Um Ihre Integration zu testen, können Sie **Test-Events senden** auswählen, um je ein Event aus jedem der von Ihnen ausgewählten Event-Typen an diesen Current zu senden. Ausführliche Informationen zu den einzelnen Event-Typen finden Sie in unseren Bibliotheken [Kundenverhalten-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/) und [Messaging-Engagement-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/).

![Die Seite „Currents Test“ im Braze-Dashboard.]({% image_buster /assets/img/currents/current_test_events.png %}){: style="max-width:70%;"}

#### Testen von Currents-Konnektoren {#testing-currents-connectors}

Test-Currents-Konnektoren sind kostenlose Versionen unserer bestehenden Konnektoren, die zum Testen und Ausprobieren verschiedener Ziele verwendet werden können. Test-Currents haben:

- Bis zu 10 Test-Currents-Konnektoren pro Workspace.
- Insgesamt maximal 1.500 Events pro festgelegtem Zeitraum von 24 Stunden, der um Mitternacht UTC zurückgesetzt wird. Diese Event-Summe wird stündlich auf dem Dashboard aktualisiert.

Sobald Ihre Test-Currents-Konnektoren das Sende-Limit erreicht haben, werden keine Events mehr gesendet, bis der nächste Tag (um Mitternacht UTC) beginnt.

Um Ihren Test-Currents-Konnektor zu upgraden, bearbeiten Sie die Integration im Dashboard und wählen Sie **Test-Integration upgraden**.

## Currents aktualisieren {#updating-currents}

{% multi_lang_include currents/updating_currents.md %}

## IP-Allowlisting {#ip-allowlisting}

Braze sendet Currents-Daten von den aufgeführten IPs:

{% multi_lang_include administer/data_centers.md datacenters='ips' %}