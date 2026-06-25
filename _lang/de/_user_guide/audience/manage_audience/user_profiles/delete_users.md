---
nav_title: "Nutzer:innen löschen"
article_title: "Nutzer:innen löschen"
page_order: 6
toc_headers: h2
description: "Erfahren Sie, wie Sie einzelne Nutzer:innen oder ein Segment von Nutzer:innen direkt über das Braze-Dashboard löschen können."
alias: /delete_users/
---

# Nutzer:innen löschen {#delete-users}

> Erfahren Sie, wie Sie einzelne Nutzer:innen oder ein Segment von Nutzer:innen direkt über das Braze-Dashboard löschen können.

## Voraussetzungen {#prerequisites}

Um Nutzer:innen zu löschen, müssen Sie Admin sein oder über die Berechtigung **Delete Users** verfügen. Um Löschprotokolle von Nutzer:innen einzusehen, müssen Sie Admin sein oder über die Berechtigung **View User Deletion Records** verfügen. Die folgenden Berechtigungen steuern das Löschen von Nutzer:innen und die Löschprotokolle:

| Berechtigung | Beschreibung |
|------------|-------------|
| Nutzer:innen löschen | Nutzer:innen einzeln oder in großen Mengen dauerhaft löschen. |
| Löschprotokolle von Nutzer:innen einsehen | Löschprotokolle von Nutzer:innen einsehen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Über das Löschen von Nutzer:innen {#about-user-deletion}

Das Löschen von Nutzer:innen ermöglicht es Ihnen, Ihre Datenbank zu verwalten, indem Sie Profile entfernen, die nicht mehr benötigt werden, versehentlich erstellt wurden oder aus Compliance-Gründen gelöscht werden müssen (z. B. DSGVO oder CCPA).

| Aspekt | Details |
|---------------|---------|
| Maximale Größe | Sie können bis zu 10 Millionen Nutzerprofile löschen, wenn Sie ein Segment löschen. |
| Wartezeit | Alle Segment-Löschungen erfordern eine 7-tägige Wartezeit plus die Zeit, die für die Verarbeitung der Löschungen benötigt wird. |
| Auftragslimits | Es kann jeweils nur ein Segment gelöscht werden, einschließlich der 7-tägigen Wartezeit. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Über das Löschen von Nutzer:innen" }

## Nutzer:innen löschen {#deleting-users}

Sie können einzelne Nutzer:innen ([Einzelperson löschen](#delete-individual)) oder ein [Segment von Nutzer:innen](#delete-segment) über das Braze-Dashboard löschen:

### Einzelperson löschen {#delete-individual}

Um einzelne Nutzer:innen aus Braze zu löschen, gehen Sie zu **Audience** > **Search Users** und suchen und wählen Sie dann eine:n Nutzer:in aus. Wenn Sie ein doppeltes Nutzerprofil löschen, überprüfen Sie, ob Sie das richtige ausgewählt haben.

![Die Seite „Search Users“ in Braze.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/search_user.png %}){: style="max-width:75%;"}

{% alert warning %}
Löschungen einzelner Nutzer:innen sind dauerhaft – Profile können nach dem Löschen nicht wiederhergestellt werden.
{% endalert %}

Wählen Sie auf der Profilseite <i class="fa-solid fa-ellipsis-vertical"></i> **Show options** > **Delete User**. Beachten Sie, dass es einige Minuten dauern kann, bis die Nutzer:innen vollständig in Braze gelöscht sind.


### Segment löschen {#delete-segment}

Falls noch nicht geschehen, [erstellen Sie ein Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/), das die Nutzerprofile enthält, die Sie löschen möchten. Stellen Sie sicher, dass alle Nutzerprofile enthalten sind, wenn Sie doppelte Nutzer:innen löschen.

Gehen Sie in Braze zu **Audience** > **Manage Audience** und wählen Sie dann den Tab **Delete Users**.

![Der Tab „Delete Users“ im Bereich „Manage Audience“ des Braze-Dashboards.]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

Wählen Sie **Delete users**, wählen Sie das Segment aus, das Sie löschen möchten, und wählen Sie dann **Next**.

![Ein Pop-up-Fenster mit einem zur Löschung ausgewählten Segment.]({% image_buster /assets/img/audience_management/deleting_users/choose_segment_to_delete.png %}){: style="max-width:75%;"}

Geben Sie **DELETE** ein, um Ihre Anfrage zu bestätigen, und wählen Sie dann **Delete users**.

![Die Bestätigungsseite mit „DELETE“ im Bestätigungsfeld.]({% image_buster /assets/img/audience_management/deleting_users/confirm_segment_delete.png %}){: style="max-width:75%;"}

Die Nutzer:innen in diesem Segment werden nicht sofort gelöscht. Stattdessen werden sie für die nächsten 7 Tage als zur Löschung ausstehend markiert. Nach Ablauf dieser Zeit werden sie gelöscht und Sie erhalten eine E-Mail-Benachrichtigung.

{% alert tip %}
Um sicherzustellen, dass genau diese Nutzer:innen unabhängig von Segmentänderungen gelöscht werden, wird automatisch ein Segmentfilter namens **Pending Deletion** erstellt. Sie können [diesen Filter verwenden]({{site.baseurl}}/user_guide/audience/segments/managing_segments/#filters), um den Status ausstehender Löschungen zu überprüfen.
{% endalert %}

## Segment-Löschungen bestätigen {#confirming-segment-deletions}

Braze sendet eine Bestätigungs-E-Mail mit der Anzahl der zur Löschung ausstehenden Profile.

Um mit der Löschung fortzufahren, melden Sie sich bei Braze an und bestätigen Sie die Löschanfrage.

Wenn Sie nicht innerhalb des in der E-Mail angegebenen Zeitraums bestätigen, läuft die Löschanfrage ab und wird nicht ausgeführt.

## Segment-Löschungen abbrechen {#cancel}

Sie haben 7 Tage Zeit, um ausstehende Segment-Löschungen abzubrechen. Gehen Sie dazu zu **Audience** > **Manage Audience** und wählen Sie dann den Tab **Delete Users**.

![Der Tab „Delete Users“ im Bereich „Manage Audience“ des Braze-Dashboards.]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

Wählen Sie neben einer ausstehenden Segment-Löschung <i class="fa-solid fa-eye"></i> **View details**, um die Details des Löschprotokolls zu öffnen.

![Eine ausstehende Segment-Löschung auf dem Tab „Delete Users“.]({% image_buster /assets/img/audience_management/deleting_users/pending_deletion.png %})

Wählen Sie in den Details des Löschprotokolls **Cancel deletion**.

![Das Fenster „Deletion Record Details“ auf dem Tab „Delete Users“.]({% image_buster /assets/img/audience_management/deleting_users/deletion_record_details.png %}){: style="max-width:55%;"}

{% alert tip %}
Wenn eine Massenlöschung von Nutzer:innen in Bearbeitung ist, können Sie sie jederzeit abbrechen. Allerdings können Nutzer:innen, die vor dem Abbruch bereits gelöscht wurden, nicht wiederhergestellt werden.
{% endalert %}

## Löschstatus überprüfen {#status}

Sie können den Status einer Löschung mithilfe von [Segmentfiltern](#segment-filters), der Seite [Zielgruppe verwalten](#manage-audience) oder [Sicherheitsereignisberichten](#security-event-report) überprüfen.

### Segmentfilter {#segment-filters}

Wenn Sie die Löschung eines Segments von Nutzer:innen anfordern, wird automatisch ein [Segmentfilter]({{site.baseurl}}/user_guide/audience/segments/managing_segments/#filters) namens **Pending Deletion** erstellt. Sie können ihn verwenden, um:

- Die genaue Gruppe von Nutzer:innen zu sehen, die einem bestimmten Löschdatum zugeordnet sind.
- Diese Nutzer:innen von Campaigns auszuschließen, damit sie vor der Entfernung keine Nachrichten erhalten.
- Die Liste zu exportieren, falls Sie sie für Compliance- oder Aufbewahrungszwecke benötigen.

### Zielgruppe verwalten {#manage-audience}

{% alert note %}
Um die Liste der genauen Nutzer:innen zu erhalten, die gelöscht werden, verwenden Sie stattdessen den [Segmentfilter „Pending Deletion“](#segment-filters).
{% endalert %}

Gehen Sie zu **Audience** > **Manage Audience** und wählen Sie dann den Tab **Delete Users**.

![Der Tab „Delete Users“ im Bereich „Manage Audience“ des Braze-Dashboards.]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

Auf dieser Seite finden Sie die folgenden allgemeinen Informationen für alle aktuellen und ausstehenden Löschungen:

| Feld | Beschreibung |
|-------|-------------|
| Request Date | Das Datum, an dem die Anfrage ursprünglich gestellt wurde. Verwenden Sie es zusammen mit dem Filter **Pending Deletion**, um die Liste der zur Löschung ausstehenden Profile zu erhalten. |
| Requester | Die Person, die die Löschanfrage initiiert hat. |
| Segment Name | Der Name des Segments, das zur Auswahl der zur Löschung ausstehenden Nutzer:innen verwendet wurde. |
| Status | Zeigt an, ob die Löschanfrage ausstehend, in Bearbeitung oder abgeschlossen ist. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Zielgruppe verwalten" }

Für weitere Details zu einer bestimmten Anfrage wählen Sie <i class="fa-solid fa-eye"></i> **View details**, um die Details des Löschprotokolls anzuzeigen. Hier können Sie auch [ausstehende Segment-Löschungen abbrechen](#cancel).

![Eine ausstehende Segment-Löschung auf dem Tab „Delete Users“.]({% image_buster /assets/img/audience_management/deleting_users/pending_deletion.png %})

### Sicherheitsereignisbericht {#security-event-report}

Sie können den Status früherer Löschungen auch überprüfen, indem Sie einen Sicherheitsereignisbericht herunterladen. Weitere Informationen finden Sie unter [Sicherheitseinstellungen]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings/#security-event-report).

## Häufig gestellte Fragen {#faq}

### Kann ich Segmente mit mehr als 10 Millionen Nutzer:innen löschen? {#can-i-delete-segments-with-more-than-10-million-users}

Nein. Sie können keine Segmente mit mehr als 10 Millionen Nutzer:innen löschen. Wenn Sie Hilfe beim Löschen eines Segments dieser Größe benötigen, wenden Sie sich an den [Braze-Support]({{site.baseurl}}/user_guide/administer/personal/braze_support/).

### Ich kann nur bis zu 10 Millionen Nutzer:innen auf einmal löschen. Ist das ein Fehler? {#i-can-only-delete-up-to-10-million-users-at-a-time-is-this-a-bug}

Nein, das ist kein Fehler. Die maximale Anzahl von Nutzerprofilen, die in einem einzelnen Segment-Löschlauf gelöscht werden können, beträgt 10 Millionen.

### Beeinflusst die automatische Zusammenführung von Nutzer:innen das Löschen von Nutzer:innen? {#does-automated-user-merging-affect-user-deletion}

Wenn eine geplante Zusammenführung Nutzerprofile enthält, die zur Löschung ausstehen, überspringt Braze diese Profile und führt sie nicht zusammen. Um diese Profile zusammenzuführen, müssen Sie sie aus der Löschung entfernen.

### Was passiert mit Daten, die an zur Löschung ausstehende Nutzer:innen gesendet werden? {#what-happens-to-data-sent-to-users-pending-deletion}

Daten, die von externen Systemen oder SDKs gesendet werden, werden weiterhin akzeptiert, aber die Nutzer:innen werden unabhängig von der Aktivität wie geplant gelöscht.

### Werden Canvases und Campaigns für zur Löschung ausstehende Nutzer:innen ausgelöst? {#do-canvases-and-campaigns-trigger-for-users-pending-deletion}

Ja. Sie können jedoch einen Segment-Einschlussfilter hinzufügen, um alle Nutzer:innen mit dem [Segmentfilter](#segment-filters) **Pending Deletion** auszuschließen.

### Kann ich gelöschte Nutzerprofile wiederherstellen? {#can-i-recover-deleted-user-profiles}

Das Löschen einzelner Nutzer:innen ist dauerhaft.

Sie können [Segment-Löschungen](#cancel) innerhalb der ersten 7 Tage abbrechen. Allerdings können Nutzer:innen, die vor dem Abbruch bereits gelöscht wurden, nicht wiederhergestellt werden.

### Kann ich Nutzer:innen über die API statt über das Dashboard löschen? {#can-i-delete-users-with-the-api-instead-of-the-dashboard}

Ja. Für kleinere Mengen können Sie den [`/users/delete`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) verwenden, der bis zu 50 Bezeichner pro Anfrage akzeptiert und dem [Rate-Limit]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/#rate-limit) dieses Endpunkts unterliegt. Die segmentbasierte Löschung über das Dashboard eignet sich besser für sehr große Zielgruppen, beinhaltet jedoch die [7-tägige Wartezeit](#about-user-deletion).