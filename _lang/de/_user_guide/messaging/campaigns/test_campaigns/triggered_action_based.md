---
nav_title: API-getriggerte und aktionsbasierte Campaigns
article_title: API-getriggerte und aktionsbasierte Campaigns testen
page_order: 2
page_type: reference
description: "Dieser Referenzartikel erklärt, wie Sie API-getriggerte und aktionsbasierte Campaigns testen."

---

# API-getriggerte und aktionsbasierte Campaigns {#api-triggered-and-action-based-campaigns}

> Beim Einrichten von Campaigns ist es immer empfehlenswert, Ihre Nachrichten vor dem Start zu testen. Dieser Referenzartikel behandelt das Erstellen eines Testsegments für Nutzer:innen, mit dem Sie API-Anfragen und Payloads überprüfen sowie Zustellbarkeits-Protokolle einsehen können.

## 1. Schritt: Testsegment erstellen {#step-1-create-a-test-user-segment}

Die einzige Möglichkeit, das Trigger or triggern or triggern einer Campaign über die API oder ein angepasstes Event zu testen, besteht darin, die Campaign live zu schalten. Im Rahmen der Einführung einer neuen Campaign empfehlen wir dringend, beim Testen der Zustellbarkeit ein Testsegment zu Campaigns hinzuzufügen. Dies bietet ein Sicherheitsnetz und stellt sicher, dass eine Campaign, selbst wenn sie versehentlich gesendet wird, nur an interne Nutzer:innen geht.

1. **Testnutzer:innen importieren**<br>Testnutzer:innen können über eine CSV-Datei oder eine einmalige Batch-Anfrage über [Postman]({{site.baseurl}}/api/postman_collection) in Braze importiert werden. Beim Import dieser Nutzer:innen empfehlen wir, ein angepasstes Attribut in deren Profilen zu setzen (z. B. `internal_test_user: true`), das zum Erstellen eines Testgruppen-Segments verwendet werden kann. <br><br>
2. **Testnutzer:innen als von Braze erkannte Testnutzer:innen hinzufügen**<br>[Wenn Sie Ihre Testnutzer:innen als von Braze erkannte Testnutzer:innen markieren]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups), erhalten Sie im Dashboard Zugriff auf ausführliche Protokollierung für jede:n Nutzer:in. So können Sie API-Anfragen, deren Payloads überprüfen und Zustellbarkeits-Protokolle einsehen. Diese Protokolle helfen Ihnen festzustellen, ob es Probleme bei der Zustellung von Campaigns an Endnutzer:innen gab. <br><br>
3. **Segment erstellen**<br>Um ein Testsegment zu erstellen, erstellen Sie ein Segment von Nutzer:innen, bei denen das angepasste Attribut `internal_test_user` auf `true` gesetzt ist. Dieses Segment kann entfernt werden, wenn die Campaign live geht.

## 2. Schritt: Testversand durchführen {#step-2-testing-sends}

Als Nächstes können Sie einen Testversand über das Braze-Dashboard durchführen oder Inbox Vision (nur E-Mail) verwenden, um das Layout zu überprüfen, während sich die Campaign noch im Entwurfsmodus befindet. Anschließend können Sie die Campaign an Ihr Testsegment senden, um zu überprüfen, ob sie wie erwartet funktioniert. Unabhängig davon, ob die Campaign API-getriggert oder aktionsbasiert ist, verwenden Sie Postman, um eine einmalige Anfrage an die Braze-API zu senden und die Campaign zu Trigger or triggern or triggern.

## 3. Schritt: Braze-Protokollierung zur Überprüfung eingehender Ergebnisse nutzen {#step-3-use-braze-logging-to-inspect-inbound-results}

Verwenden Sie die Braze-Protokollierung, um Probleme beim Trigger or triggern or triggern, Senden und bei Events zu beheben.
- Das [Event-Nutzerprotokoll]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log) zeigt Ihnen den Roh-Payload der API-Trigger or triggern-Anfrage, das angepasste Event, das die Campaign triggert, sowie alle zugehörigen Trigger or triggern- oder Event-Eigenschaften.
- Das [Nachrichten-Aktivitätsprotokoll]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) protokolliert alle Fehler und hilft Ihnen zu verstehen, warum eine bestimmte Nachricht möglicherweise nicht zugestellt wurde.

## 4. Schritt: Testsegment entfernen und Campaign ausrollen {#step-4-remove-the-test-segment-and-roll-out-the-campaign}

Sobald die Nachricht korrekt getriggert und gerendert wird und alle angeklickten Links registriert sind, können Sie das Segment entfernen und die Campaign Update or aktualisieren or aktualisieren. Wenn Sie die Campaign lieber von Grund auf neu starten möchten, damit die wenigen Impressionen der Testnutzer:innen nicht enthalten sind, können Sie die Campaign duplizieren und ohne das Testsegment neu starten.