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

- **Ein Fenster pro Kanal:** Jeder Kanal unterstützt ein einzelnes Workspace-Ruhezeitfenster, definiert durch eine Start- und eine Endzeit.
- **Ortszeit:** Wie Ruhezeiten auf Campaign- und Canvas-Ebene gelten Workspace-Ruhezeiten in der Ortszeit jeder Empfängerin und jedes Empfängers, nicht in der Zeitzone Ihres Unternehmens.
- **Zurückgehalten für spätere Zustellung:** Eine Nachricht, die andernfalls während des Fensters gesendet würde, wird zurückgehalten und später zugestellt oder abgebrochen, abhängig vom Campaign-Typ. Siehe [Was passiert mit einer zurückgehaltenen Nachricht](#what-happens-to-a-held-message). Ruhezeiten ändern niemals den Nachrichteninhalt. Sie beeinflussen nur das Timing.
- **Maximale Fensterlänge:** Ein Ruhezeitfenster darf 20 Stunden nicht überschreiten. Dieses Limit verhindert, dass versehentlich alle Sendungen auf einem Kanal pausiert werden (zum Beispiel durch Setzen der Start- und Endzeit auf denselben Wert).

### Unterstützte Kanäle {#supported-channels}

Sie können ein Workspace-Ruhezeitfenster für jeden der folgenden Kanäle festlegen:

- Content Cards
- E-Mail
- KakaoTalk
- LINE
- Push
   - Dies umfasst jede Push-Plattform in Ihrem Workspace. Es gibt keine Option, unterschiedliche Ruhezeiten für einzelne Plattformen festzulegen (zum Beispiel iOS vs. Android).
- SMS/MMS/RCS
- Webhook
- WhatsApp

## Voraussetzungen {#prerequisites}

Um Workspace-Ruhezeiten zu erstellen oder zu aktualisieren, benötigen Sie die Berechtigung „Ruhezeiten bearbeiten“.

| Berechtigung | Zugriff |
|---|---|
| Ruhezeiten bearbeiten | Workspace-Ruhezeiten erstellen und aktualisieren. |
| Ruhezeiten anzeigen | Die Workspace-Ruhezeitkonfiguration anzeigen, ohne sie zu bearbeiten. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Berechtigungen für Ruhezeiten" }

Bestehende Bearbeitungsberechtigungen für Campaigns und Canvases sind nicht betroffen. Nutzer:innen mit diesen Berechtigungen können weiterhin Ruhezeiten auf Campaign- oder Canvas-Ebene bearbeiten.

## Workspace-Ruhezeiten einrichten {#set-up-workspace-quiet-hours}

### Das Workspace-Fenster konfigurieren {#configure-the-workspace-window}

1. Gehen Sie zu **Einstellungen** > **Ruhezeiten**.
2. Wählen Sie **Ruhezeiten hinzufügen**.
3. Wählen Sie einen Kanal aus und geben Sie eine Start- und Endzeit ein. Ein Kanal kann jeweils höchstens ein Workspace-Ruhezeitfenster haben.
4. (Optional) Um einen weiteren Kanal hinzuzufügen, wählen Sie erneut **Ruhezeiten hinzufügen**.
5. Speichern Sie Ihre Änderungen.

![Die Seite für Workspace-Ruhezeiteinstellungen mit SMS- und E-Mail-Ruhezeitfenstern, jeweils mit einer Start- und Endzeit, sowie einer Option zum Hinzufügen von Ruhezeiten.]({% image_buster /assets/img/quiet_hours/workspace_quiet_hours_settings.png %}){: style="max-width:90%;"}

Änderungen an Workspace-Ruhezeiten werden in einem Changelog protokolliert, einschließlich wer die Änderung vorgenommen hat und wann, da diese Einstellung jede Campaign und jedes Canvas auf dem Kanal betrifft.

### In einer Campaign oder einem Canvas anwenden oder überschreiben {#apply-or-override-in-a-campaign-or-canvas}

Nach dem Speichern erscheint das Workspace-Ruhezeitfenster im Campaign- und Canvas-Editor für jeden Kanal, der ein Fenster hat. Sie können den Workspace-Standard beibehalten oder sich abmelden und stattdessen ein Campaign- oder Canvas-spezifisches Fenster anwenden, genauso wie Sie sich von einem Frequency-Capping auf Workspace-Ebene abmelden.

1. Wählen Sie **Ruhezeiten für diese Campaign erzwingen** (oder das Canvas-Äquivalent).
2. Wählen Sie **Workspace-Ruhezeiten verwenden**, um den Workspace-Standard anzuwenden, oder wählen Sie **Angepasste Ruhezeiten verwenden**, um ein Campaign- oder Canvas-spezifisches Fenster festzulegen.
3. Um das Workspace-Fenster für die verwendeten Kanäle zu überprüfen, wählen Sie **Ruhezeiten anzeigen**.

![Der Abschnitt „Ruhezeiten“ einer Campaign mit ausgewählter Option „Ruhezeiten für diese Campaign erzwingen“, ausgewählter Option „Workspace-Ruhezeiten verwenden“ und dem erweiterten E-Mail-Workspace-Fenster von 20:00 Uhr bis 8:00 Uhr.]({% image_buster /assets/img/quiet_hours/campaign_workspace_quiet_hours.png %}){: style="max-width:70%;"}

## Vorrang: Workspace- versus Campaign- oder Canvas-Ruhezeiten {#precedence-workspace-versus-campaign-or-canvas-quiet-hours}

Für jede gegebene Campaign oder jedes Canvas ist immer nur eine Ruhezeiteinstellung gleichzeitig aktiv (Workspace-Ruhezeiten, ein Campaign- oder Canvas-spezifisches Fenster oder keine). Ein Ruhezeitfenster auf Campaign- oder Canvas-Ebene hat immer Vorrang vor dem Workspace-Standard.

Wie Ruhezeiten angewendet werden, hängt auch davon ab, wann die Campaign oder das Canvas erstellt wurde:

- **Bestehende Campaigns und Canvases** (erstellt bevor Sie Workspace-Ruhezeiten aktiviert haben): Wenn die Campaign oder das Canvas kein eigenes Ruhezeitfenster hat, gilt das Workspace-Ruhezeitfenster für diesen Kanal automatisch. Wenn bereits ein Fenster auf Campaign- oder Canvas-Ebene vorhanden ist, gilt dieses weiterhin.
- **Neue Campaigns und Canvases:** Wenn Sie eine Campaign oder ein Canvas erstellen, können Sie den Workspace-Ruhezeitstandard verwenden, ein angepasstes Fenster auf Campaign- oder Canvas-Ebene festlegen oder sich vollständig von Ruhezeiten abmelden.

| Vorhandene Konfiguration | Welche Ruhezeiten gelten |
|---|---|
| Campaign oder Canvas hat ein eigenes Ruhezeitfenster | Das Fenster auf Campaign- oder Canvas-Ebene gilt. Workspace-Ruhezeiten werden für diese Campaign oder dieses Canvas ignoriert. |
| Campaign oder Canvas hat kein eigenes Ruhezeitfenster, und ein Workspace-Ruhezeitfenster existiert für den verwendeten Kanal | Das Workspace-Ruhezeitfenster gilt automatisch. Dies schließt bestehende Campaigns und Canvases ein, die nie Ruhezeiten konfiguriert haben. |
| Campaign oder Canvas hat sich abgemeldet | Keine Ruhezeiten gelten. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Vorrang der Ruhezeiten" }

### Was passiert mit einer zurückgehaltenen Nachricht {#what-happens-to-a-held-message}

Was mit einer Nachricht passiert, die in ein Ruhezeitfenster fällt, hängt vom Zustellungstyp der Campaign oder des Canvas ab:

- **Aktionsbasierte Campaigns und Canvases:** Der Fallback kann entweder **Nachricht abbrechen** oder **Zum nächsten verfügbaren Zeitpunkt senden** sein, dieselben Optionen wie bei Ruhezeiten auf Campaign- und Canvas-Ebene.
- **Geplante Campaigns mit fester Sendezeit:** Der Fallback ist **Nachricht abbrechen**. Braze verzögert eine Sendung mit fester Zeit nicht auf den nächsten verfügbaren Slot, da dies ein großes Nachrichtenvolumen in ein komprimiertes Sendefenster nach Ende der Ruhezeiten drängen könnte.
- **Campaigns mit intelligentem Timing:** Kein separater Fallback erforderlich. Braze berücksichtigt das Workspace-Ruhezeitfenster bereits bei der optimalen Sendezeit, die für jede Nutzerin und jeden Nutzer berechnet wird, sodass Nachrichten von vornherein nicht innerhalb des Fensters geplant werden.
- **API-getriggerte Campaigns und API-Campaigns:** Der Fallback ist standardmäßig **Nachricht abbrechen**.

### API-getriggerte und API-Campaigns {#api-triggered-and-api-campaigns}

Ruhezeiten funktionieren bei API-getriggerten Campaigns und API-Campaigns anders.

#### API-getriggerte Campaigns {#api-triggered-campaigns}

API-getriggerte Campaigns folgen denselben Ruhezeitoptionen wie andere Campaigns im Dashboard. Sie können den Workspace-Ruhezeitstandard verwenden, ein angepasstes Fenster auf Campaign-Ebene festlegen oder sich in der Campaign-Konfiguration von Ruhezeiten abmelden. Es gibt keinen API-Parameter `ignore_workspace_quiet_hours` für API-getriggerte Sendungen.

Für geplante API-getriggerte Sendungen mit `at_optimal_time` werden Workspace-Ruhezeiten bereits in die optimale Sendezeit einbezogen, ähnlich wie beim [intelligenten Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing).

#### API-Campaigns {#api-campaigns}

API-Campaigns können keine Ruhezeiten auf Campaign-Ebene verwenden. Es gilt nur das Workspace-Ruhezeitfenster. Um während dieses Fensters zu senden, fügen Sie den optionalen Parameter `ignore_workspace_quiet_hours` in Ihre API-Anfrage ein.

### Ausnahmen {#exclusions}

Die folgenden werden unabhängig vom Kanal niemals von Workspace-Ruhezeiten zurückgehalten:

- Transaktionale und SLA-gebundene Nachrichten
- SMS-Auto-Antworten (zum Beispiel `STOP`- oder `HELP`-Schlüsselwortantworten)
- Testsendungen und Seed-Gruppen-Sendungen

## Weitere Überlegungen {#other-considerations}

- **Geplante Sendungen in Unternehmenszeit:** Workspace-Ruhezeiten basieren auf der Ortszeit jeder Empfängerin und jedes Empfängers, aber die Sendezeit einer geplanten Campaign kann in der Zeitzone Ihres Unternehmens festgelegt sein. Diese Diskrepanz bedeutet, dass eine Sendezeit, die in der Unternehmenszeit in Ordnung aussieht, für einige Empfänger:innen dennoch in die Ruhezeiten fallen könnte. Überprüfen Sie die im Campaign-Editor angezeigten Workspace-Ruhezeitdetails vor dem Senden.
- **Zustellung nach Ende der Ruhezeiten:** Wenn eine große Zielgruppe während des Fensters zurückgehalten wurde, können diese Nachrichten alle gleichzeitig zum Senden berechtigt werden, wenn das Fenster schließt. Planen Sie dies ein, wenn ein Kanal eine breite Zielgruppe und ein langes Ruhezeitfenster hat.
- **Unabhängig von Frequency-Capping und Rate-Limiting:** Workspace-Ruhezeiten gelten unabhängig von Frequency-Capping und Rate-Limiting. Eine Nachricht, die diese Kontrollen passiert, kann dennoch von Ruhezeiten zurückgehalten werden, und eine von Ruhezeiten zurückgehaltene Nachricht wird weiterhin gegen Rate-Limits geprüft, sobald sie zum Senden bereit ist.
- **Intelligentes Timing überschreibt Workspace-Ruhezeiten für aktionsbasierte Multi-Channel-Campaigns. Um Sendezeiten einzuschränken, legen Sie stattdessen angepasste Ruhezeiten fest.

## Verwandte Einstellungen {#related-settings}

- [Ruhezeiten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours): Die bestehende Version dieses Features auf Campaign- und Canvas-Ebene. Workspace-Ruhezeiten ersetzen sie nicht; sie legen den Standard fest, der gilt, wenn eine Campaign oder ein Canvas kein eigenes Fenster konfiguriert.
- [Intelligentes Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing): Berechnet eine optimale Sendezeit pro Nutzer:in. Wenn es zusammen mit Workspace-Ruhezeiten aktiviert ist, werden Ruhezeiten in diese Berechnung einbezogen.
- [Rate-Limiting und Frequency-Capping]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping): Separate Zustellungskontrollen, die unabhängig von Ruhezeiten gelten.