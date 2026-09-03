---
nav_title: Zwischen Workspaces übertragen
article_title: Telefonnummern und Abo-Gruppen zwischen Workspaces übertragen
page_order: 3
description: "Dieser Referenzartikel beschreibt, wie Sie Ihre WhatsApp-Telefonnummer und Abo-Gruppen zwischen Workspaces übertragen."
page_type: reference
channel:
  - WhatsApp
---

# WhatsApp-Telefonnummern und Abo-Gruppen zwischen Workspaces übertragen {#transfer-whatsapp-phone-numbers-and-subscription-groups-between-workspaces}

> Auf dieser Seite erfahren Sie, wie Sie eine WhatsApp Business Account (WABA)-Telefonnummer und die zugehörige Abo-Gruppe von einem Workspace in einen anderen innerhalb von Braze verschieben können. Dieser Prozess vereinfacht Ihre Nutzung von WhatsApp mit Braze und reduziert den Bedarf an technischer Unterstützung.

## Voraussetzungen {#prerequisites}

- Stellen Sie sicher, dass Sie die [Nutzerberechtigung]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions) „Abo-Gruppen verwalten“ sowohl im ursprünglichen als auch im neuen Workspace besitzen.
- Der WABA kann nicht über mehrere [Braze-Cluster]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints) hinweg verwendet werden. Dies ist unwahrscheinlich, wenn Sie innerhalb eines Unternehmens arbeiten.

## Telefonnummer und Abo-Gruppe übertragen {#transferring-a-phone-number-and-subscription-group}

### 1. Schritt: Abo-Gruppe archivieren {#step-1-archive-the-subscription-group}

Um eine WhatsApp-Abo-Gruppe zu archivieren, gehen Sie wie folgt vor:

1. Wechseln Sie zum Workspace, in dem die Abo-Gruppe derzeit existiert.
2. Gehen Sie zu **Zielgruppe** > **Abo-Gruppen-Verwaltung** und suchen Sie die Abo-Gruppe, die mit der WhatsApp-Telefonnummer verknüpft ist, die Sie verschieben möchten.
3. Fahren Sie mit dem Mauszeiger über den Status der Abo-Gruppe und wählen Sie <i class="fa-solid fa-box-archive"></i> **Archivieren** aus. Dadurch wird die Abo-Gruppe als inaktiv markiert, aber nicht gelöscht.

![Der Button „Archivieren“ erscheint beim Überfahren des Status „Aktiv“ einer Abo-Gruppe mit dem Mauszeiger.]({% image_buster /assets/img/whatsapp/archive_subscription_group.png %}){: style="max-width:70%;"}

### 2. Schritt: WhatsApp-Telefonnummer in den neuen Workspace integrieren {#step-2-integrate-the-whatsapp-phone-number-into-the-new-workspace}

1. Wechseln Sie zum Workspace, in den Sie die WhatsApp-Telefonnummer verschieben möchten.
2. Gehen Sie zu **Partnerintegrationen** > **Technologie-Partner** > **WhatsApp** und scrollen Sie zum Abschnitt **WhatsApp Messaging Integration**.
3. Wählen Sie die Option **Neue Abo-Gruppe und Telefonnummer erstellen** aus.
4. Starten Sie den Integrationsprozess. Dabei können Sie die Telefonnummer aus der archivierten Abo-Gruppe auswählen.

### 3. Schritt: Integration überprüfen {#step-3-verify-the-integration}

1. Bestätigen Sie nach Abschluss der Integration, dass die WhatsApp-Telefonnummer nun mit der Abo-Gruppe im neuen Workspace verknüpft ist.
2. Testen Sie, ob Nachrichten über diese WhatsApp-Telefonnummer gesendet und empfangen werden können.

## Hinweise {#considerations}

- Wenn Sie die WhatsApp-Telefonnummer zurück in den ursprünglichen Workspace übertragen müssen, wiederholen Sie die Schritte. Archivieren Sie die Abo-Gruppe im Ziel-Workspace und integrieren Sie sie dann in den ursprünglichen Workspace.
- Sie müssen die WhatsApp-Telefonnummer während der Übertragung nicht aus Ihrem Meta Business Manager:in entfernen.