---
nav_title: Aktionen überprüfen
article_title: Aktionen von BrazeAI Operator<sup>TM</sup> überprüfen
page_order: 2
description: "Erfahren Sie, wie Sie Aktionen überprüfen und genehmigen können, wenn BrazeAI Operator Änderungen im Dashboard vorschlägt."
---

# Aktionen von BrazeAI Operator überprüfen {#reviewing-brazeai-operator-actions}

> Erfahren Sie, wie Sie Aktionen überprüfen und genehmigen können, wenn BrazeAI Operator<sup>TM</sup> Änderungen im Dashboard vorschlägt.

![Operator präsentiert vorgeschlagene Aktionskarten zur Überprüfung.]({% image_buster /assets/img/operator/suggested_actions.png %}){: style="max-width:40%; border:none; float:right; margin-left:15px;"}

## Funktionsweise von Aktionskarten {#how-action-cards-work}

Wenn Operator Änderungen im Dashboard vorschlägt (z. B. das Ausfüllen von Formularfeldern, das Update or aktualisieren or aktualisieren von Einstellungen oder das Generieren von Bildern), wird jede Änderung als Aktionskarte zur Überprüfung angezeigt.

1. **Operator fasst den Plan zusammen:** Operator erklärt, was es vorhat, bevor Aktionskarten angezeigt werden.
2. **Einzelne Aktionskarten erscheinen:** Jede vorgeschlagene Änderung wird als separate Karte dargestellt, die zeigt, was Operator im Dashboard ändern oder tun möchte. Bei Änderungen an bestehenden Werten werden sowohl der vorherige als auch der vorgeschlagene Wert nebeneinander zum Vergleich angezeigt.
3. **Überprüfen und genehmigen:** Überprüfen Sie jede Karte und genehmigen oder lehnen Sie sie ab.
4. **Aktion wird ausgeführt:** Genehmigte Aktionen werden in Braze ausgeführt. Abgelehnte Aktionen werden nicht angewendet.

Wenn eine Aktion nach der Genehmigung fehlschlägt, benachrichtigt Operator Sie mit Details zum Fehler.

### Verfügbarkeit {#availability}

Operator kann Aktionskarten auf unterstützten Dashboard-Seiten vorschlagen, einschließlich Nachrichten-Editoren, Listen- und Übersichtsseiten, Einstellungen und anderen Oberflächen, auf denen es agieren kann. Eine repräsentative Übersicht finden Sie unter [Was Sie mit Operator tun können]({{site.baseurl}}/user_guide/brazeai/operator/capabilities). Informationen zu unterstützten Nachrichtenkanälen und Editoren finden Sie unter [Nachrichten generieren]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-messages).

Die Abdeckung wird regelmäßig erweitert. Wenn Operator auf der Seite, auf der Sie sich befinden, nicht agieren kann, stellt es stattdessen eine Liste von Schritten bereit, die Sie in der UI ausführen können.

## Plan ändern {#modify-a-plan}

Um den Plan des Operators zu ändern, genehmigen oder lehnen Sie zunächst die ausstehenden Aktionen ab. Beschreiben Sie dann die gewünschte Änderung in einer neuen Chat-Nachricht.

Genehmigte Aktionen können nicht über den Operator rückgängig gemacht werden. Beschreiben Sie die neue Änderung dem Operator oder nehmen Sie die Änderungen manuell im Dashboard vor.

## Aktionen automatisch genehmigen {#auto-approve-actions}

Der Umschalter **Aktionen automatisch genehmigen** befindet sich im Operator-Chat-Panel.

- **Ein:** Die von Operator vorgeschlagenen Aktionen werden sofort ausgeführt, ohne dass eine manuelle Genehmigung erforderlich ist – einschließlich des [Navigierens zu einer anderen Seite]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#navigate-the-dashboard), um Ihre Anfrage abzuschließen. Einige Aktionen erfordern aus Sicherheitsgründen weiterhin eine ausdrückliche Genehmigung, z. B. das Generieren von Bildern oder das Ändern von Einstellungen auf Workspace-Ebene.
- **Aus (Standard):** Alle vorgeschlagenen Aktionen folgen dem beschriebenen manuellen Überprüfungsprozess, einschließlich der Seitennavigation – Operator schlägt den Wechsel vor und wartet auf Ihre Genehmigung, bevor Sie dorthin weitergeleitet werden.

![Der Umschalter für die automatische Genehmigung und das Bestätigungsmodal im Operator-Chat-Panel.]({% image_buster /assets/img/operator/auto-approval_toggle.png %}){: style="max-width:50%;"}

Die automatische Genehmigung wird zurückgesetzt, wenn Sie die Seite Update or aktualisieren or aktualisieren, einen neuen Tab öffnen oder sich ab- und wieder anmelden. Das Wechseln zwischen Seiten im Dashboard setzt sie nicht zurück. Die automatische Genehmigung kann jederzeit deaktiviert werden.

Informationen zur Einschränkung des Operator-Zugriffs und zur Überprüfung der Team-Nutzung finden Sie unter [Datenschutz und Sicherheit]({{site.baseurl}}/user_guide/brazeai/operator/data_privacy_security).