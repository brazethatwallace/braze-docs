---
nav_title: Workspace-Ruhezeiten
article_title: Workspace-Ruhezeiten
page_order: 4
page_type: reference
description: "Dieser Referenzartikel behandelt Workspace-Ruhezeiten, wie Braze Nachrichten während der Ruhezeit verarbeitet und wie Ruhezeiten mit intelligentem Timing interagieren."
---

# Workspace-Ruhezeiten {#workspace-quiet-hours}

> Mit Workspace-Ruhezeiten können Sie ein Standard-Ruhezeitfenster für einen Messaging-Kanal in Ihrem gesamten Workspace festlegen. Jede Campaign und jedes Canvas, die auf diesem Kanal senden, respektieren das Fenster automatisch, sodass Sie Ruhezeiten nicht für jede Campaign oder jedes Canvas einzeln konfigurieren müssen.

Workspace-Ruhezeiten sind getrennt von Ruhezeiten auf Campaign- und Canvas-Ebene, die weiterhin gelten, wenn Sie sie konfigurieren. Verwenden Sie Workspace-Ruhezeiten für den Standardfall (zum Beispiel eine Compliance-Anforderung für alle SMS-Sendungen). Behalten Sie Ruhezeiten auf Campaign- und Canvas-Ebene für Ausnahmen bei.

{% alert important %}
Workspace-Ruhezeiten sind derzeit im Early Access verfügbar. Die Konfigurationsoptionen können sich vor der allgemeinen Verfügbarkeit ändern. Kontaktieren Sie Ihr Braze-Kontoteam, um Zugang anzufordern.
{% endalert %}

## Funktionsweise {#how-it-works}

- **Ein Zeitfenster pro Kanal:** Jeder Kanal unterstützt ein einzelnes Workspace-Ruhezeiten-Fenster, das durch eine Startzeit und eine Endzeit definiert wird.
- **Lokale Zeitzone:** Wie bei Ruhezeiten auf Campaign- und Canvas-Ebene gelten Workspace-Ruhezeiten in der jeweiligen Ortszeit der Empfänger:innen, nicht in der Zeitzone Ihres Unternehmens.
- **Zurückgehalten für spätere Zustellung:** Eine Nachricht, die andernfalls während des Zeitfensters gesendet würde, wird zurückgehalten und später zugestellt oder abgebrochen, je nach Campaign-Typ. Siehe [Was passiert mit einer zurückgehaltenen Nachricht](#what-happens-to-a-held-message). Ruhezeiten ändern niemals den Nachrichteninhalt. Sie beeinflussen nur das Timing.
- **Maximale Fensterlänge:** Ein Ruhezeiten-Fenster darf 20 Stunden nicht überschreiten. Dieses Limit verhindert, dass der gesamte Versand auf einem Kanal versehentlich pausiert wird (z. B. durch Setzen der Start- und Endzeit auf denselben Wert).

### Unterstützte Kanäle {#supported-channels}

Sie können ein Workspace-Ruhezeiten-Fenster für jeden der folgenden Kanäle festlegen:

- Content Cards
- E-Mail
- KakaoTalk
- LINE
- Push
   - Dies umfasst jede Push-Plattform in Ihrem Workspace. Es gibt keine Option, unterschiedliche Ruhezeiten für einzelne Plattformen festzulegen (z. B. iOS vs. Android).
- SMS/MMS/RCS
- Webhook
- WhatsApp

## Voraussetzungen {#prerequisites}

Um Ruhezeiten für den Workspace zu erstellen oder zu aktualisieren, benötigen Sie die Berechtigung „Ruhezeiten bearbeiten“.

| Berechtigung | Zugriff |
|---|---|
| Ruhezeiten bearbeiten | Ruhezeiten für den Workspace erstellen und aktualisieren. |
| Ruhezeiten anzeigen | Die Konfiguration der Ruhezeiten für den Workspace anzeigen, ohne sie zu bearbeiten. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Berechtigungen für Ruhezeiten" }

Bestehende Bearbeitungsberechtigungen für Campaigns und Canvases sind davon nicht betroffen. Nutzer:innen mit diesen Berechtigungen können Ruhezeiten weiterhin auf Campaign- oder Canvas-Ebene bearbeiten.

## Ruhezeiten für den Workspace einrichten {#set-up-workspace-quiet-hours}

### Das Workspace-Fenster konfigurieren {#configure-the-workspace-window}

1. Gehen Sie zu **Einstellungen** > **Ruhezeiten**.
2. Wählen Sie **Ruhezeiten hinzufügen** aus.
3. Wählen Sie einen Kanal aus und geben Sie dann eine Startzeit und eine Endzeit ein. Ein Kanal kann jeweils höchstens ein Workspace-Ruhezeiten-Fenster haben.
4. (Optional) Um einen weiteren Kanal hinzuzufügen, wählen Sie erneut **Ruhezeiten hinzufügen** aus.
5. Speichern Sie Ihre Änderungen.

![Die Seite „Ruhezeiten“ in den Workspace-Einstellungen mit SMS- und E-Mail-Ruhezeiten-Fenstern, jeweils mit einer Startzeit und einer Endzeit, sowie einer Option „Ruhezeiten hinzufügen“.]({% image_buster /assets/img/quiet_hours/workspace_quiet_hours_settings.png %}){: style="max-width:90%;"}

Änderungen an den Workspace-Ruhezeiten werden in einem Changelog aufgezeichnet, einschließlich der Information, wer die Änderung wann vorgenommen hat, da diese Einstellung jede Campaign und jeden Canvas auf dem Kanal betrifft.

### In einer Campaign oder einem Canvas anwenden oder überschreiben {#apply-or-override-in-a-campaign-or-canvas}

Nach dem Speichern wird das Workspace-Ruhezeiten-Fenster im Campaign- und Canvas-Editor für jeden Kanal angezeigt, für den ein Fenster eingerichtet ist. Sie können die Workspace-Standardeinstellung beibehalten oder sich abmelden und stattdessen ein Campaign- oder Canvas-spezifisches Fenster anwenden – genauso wie Sie sich von einem Frequency-Capping auf Workspace-Ebene abmelden.

1. Wählen Sie **Ruhezeiten für diese Campaign erzwingen** (oder die Canvas-Entsprechung) aus.
2. Wählen Sie **Workspace-Ruhezeiten verwenden**, um die Workspace-Standardeinstellung anzuwenden, oder wählen Sie **Benutzerdefinierte Ruhezeiten verwenden**, um ein Campaign- oder Canvas-spezifisches Fenster festzulegen.
3. Um das Workspace-Fenster für die verwendeten Kanäle zu überprüfen, wählen Sie **Ruhezeiten anzeigen** aus.

![Der Abschnitt „Ruhezeiten“ einer Campaign mit ausgewählter Option „Ruhezeiten für diese Campaign erzwingen“, ausgewählter Option „Workspace-Ruhezeiten verwenden“ und dem erweiterten E-Mail-Workspace-Fenster von 20:00 Uhr bis 8:00 Uhr.]({% image_buster /assets/img/quiet_hours/campaign_workspace_quiet_hours.png %}){: style="max-width:70%;"}

## Vorrang: Workspace- versus Campaign- oder Canvas-Ruhezeiten {#precedence-workspace-versus-campaign-or-canvas-quiet-hours}

Für jede Campaign oder jedes Canvas ist immer nur eine Ruhezeiten-Einstellung gleichzeitig aktiv (Workspace-Ruhezeiten, ein Campaign- oder Canvas-spezifisches Fenster oder keine). Ein Ruhezeiten-Fenster auf Campaign- oder Canvas-Ebene hat immer Vorrang vor der Workspace-Standardeinstellung.

Wie Ruhezeiten angewendet werden, hängt auch davon ab, wann die Campaign oder das Canvas erstellt wurde:

- **Bestehende Campaigns und Canvases** (erstellt, bevor Sie Workspace-Ruhezeiten aktiviert haben): Wenn die Campaign oder das Canvas kein eigenes Ruhezeiten-Fenster hat, gilt das Workspace-Ruhezeiten-Fenster für diesen Kanal automatisch. Wenn bereits ein Fenster auf Campaign- oder Canvas-Ebene vorhanden ist, wird dieses weiterhin angewendet.
- **Neue Campaigns und Canvases:** Wenn Sie eine Campaign oder ein Canvas erstellen, können Sie die Workspace-Ruhezeiten als Standard verwenden, ein angepasstes Fenster auf Campaign- oder Canvas-Ebene festlegen oder die Ruhezeiten vollständig deaktivieren.

| Vorhandene Konfiguration | Welche Ruhezeiten gelten |
|---|---|
| Campaign oder Canvas hat ein eigenes Ruhezeiten-Fenster | Das Fenster auf Campaign- oder Canvas-Ebene gilt. Workspace-Ruhezeiten werden für diese Campaign oder dieses Canvas ignoriert. |
| Campaign oder Canvas hat kein eigenes Ruhezeiten-Fenster, und es existiert ein Workspace-Ruhezeiten-Fenster für den verwendeten Kanal | Das Workspace-Ruhezeiten-Fenster gilt automatisch. Dies umfasst bestehende Campaigns und Canvases, für die nie Ruhezeiten konfiguriert wurden. |
| Campaign oder Canvas hat Ruhezeiten deaktiviert | Es gelten keine Ruhezeiten. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Vorrang der Ruhezeiten" }

### Was mit einer zurückgehaltenen Nachricht passiert {#what-happens-to-a-held-message}

Was mit einer Nachricht passiert, die in ein Ruhezeiten-Fenster fällt, hängt vom Zustellungstyp der Campaign oder des Canvas ab:

- **Aktionsbasierte Campaigns und Canvases:** Der Fallback kann entweder **Nachricht abbrechen** oder **Zum nächsten verfügbaren Zeitpunkt senden** sein – dieselben Optionen wie bei Ruhezeiten auf Campaign- und Canvas-Ebene.
- **Geplante Campaigns mit fester Sendezeit:** Der Fallback ist **Nachricht abbrechen**. Braze verzögert einen Versand mit fester Sendezeit nicht auf den nächsten verfügbaren Zeitpunkt, da dies ein großes Nachrichtenvolumen in ein komprimiertes Sendefenster nach Ende der Ruhezeiten drängen könnte.
- **Campaigns mit intelligentem Timing:** Es ist kein separater Fallback erforderlich. Braze berücksichtigt das Workspace-Ruhezeiten-Fenster bereits bei der Berechnung des optimalen Sendezeitpunkts für jede:n Nutzer:in, sodass Nachrichten von vornherein nicht innerhalb des Fensters geplant werden.
- **API-getriggerte Campaigns und API-Campaigns:** Der Fallback ist standardmäßig **Nachricht abbrechen**.

### API-getriggerte und API-Campaigns {#api-triggered-and-api-campaigns}

Ruhezeiten funktionieren bei API-getriggerten Campaigns und API-Campaigns anders.

#### API-getriggerte Campaigns {#api-triggered-campaigns}

API-getriggerte Campaigns folgen denselben Ruhezeiten-Optionen wie andere Campaigns im Dashboard. Sie können die Workspace-Ruhezeiten als Standard verwenden, ein angepasstes Fenster auf Campaign-Ebene festlegen oder die Ruhezeiten in der Campaign-Konfiguration deaktivieren. Es gibt keinen API-Parameter `ignore_workspace_quiet_hours` für API-getriggerte Sendungen.

Für geplante API-getriggerte Sendungen mit `at_optimal_time` werden Workspace-Ruhezeiten bereits in den optimalen Sendezeitpunkt einbezogen, ähnlich wie beim [intelligenten Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing).

#### API-Campaigns {#api-campaigns}

API-Campaigns können keine Ruhezeiten auf Campaign-Ebene verwenden. Es gilt nur das Workspace-Ruhezeiten-Fenster. Um während dieses Fensters zu senden, fügen Sie den optionalen Parameter `ignore_workspace_quiet_hours` in Ihre API-Anfrage ein.

### Ausnahmen {#exclusions}

Die folgenden Nachrichten werden unabhängig vom Kanal nie durch Workspace-Ruhezeiten zurückgehalten:

- Transaktions-E-Mail-Nachrichten
- Automatische SMS-Antworten (zum Beispiel Antworten auf die Schlüsselwörter `STOP` oder `HELP`)
- Testsendungen und Seed-Gruppe-Sendungen

## Weitere Überlegungen {#other-considerations}

- **Geplante Zustellungen in der Unternehmenszeit:** Ruhezeiten im Workspace basieren auf der Ortszeit der jeweiligen Empfänger:innen, aber die Sendezeit einer geplanten Campaign kann in der Zeitzone Ihres Unternehmens festgelegt sein. Diese Diskrepanz bedeutet, dass eine Sendezeit, die in der Unternehmenszeit passend erscheint, für einige Empfänger:innen dennoch in die Ruhezeiten fallen kann. Überprüfen Sie die im Campaign-Editor angezeigten Workspace-Ruhezeiten vor dem Senden.
- **Zustellung nach Ende der Ruhezeiten:** Wenn eine große Zielgruppe während des Zeitfensters zurückgehalten wurde, können all diese Nachrichten gleichzeitig zum Senden berechtigt werden, sobald das Zeitfenster endet. Planen Sie dies ein, wenn ein Kanal eine breite Zielgruppe und ein langes Ruhezeitfenster hat.
- **Unabhängig von Frequency-Capping und Rate-Limiting:** Workspace-Ruhezeiten gelten unabhängig von Frequency-Capping und Rate-Limiting. Eine Nachricht, die diese Kontrollen passiert, kann dennoch durch Ruhezeiten zurückgehalten werden, und eine durch Ruhezeiten zurückgehaltene Nachricht wird weiterhin gegen Rate-Limits geprüft, sobald sie zum Senden bereit ist.
- **Intelligentes Timing überschreibt Workspace-Ruhezeiten bei aktionsbasierten Multi-Channel-Campaigns. Um Sendezeiten einzuschränken, legen Sie stattdessen angepasste Ruhezeiten fest.

## Verwandte Einstellungen {#related-settings}

- [Ruhezeiten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours): Die bestehende Version dieses Features auf Campaign- und Canvas-Ebene. Workspace-Ruhezeiten ersetzen diese nicht, sondern legen den Standard fest, der gilt, wenn eine Campaign oder ein Canvas kein eigenes Zeitfenster konfiguriert.
- [Intelligentes Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing): Berechnet eine optimale Sendezeit pro Nutzer:in. Wenn es zusammen mit Workspace-Ruhezeiten aktiviert ist, werden die Ruhezeiten in diese Berechnung einbezogen.
- [Rate-Limiting und Frequency-Capping]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping): Separate Zustellungskontrollen, die unabhängig von Ruhezeiten gelten.