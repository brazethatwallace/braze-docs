---
nav_title: Unternehmensnutzer:innen
article_title: Unternehmensnutzer:innen verwalten
page_order: 0
page_type: reference
description: "Diese Seite behandelt die Verwaltung Ihrer Unternehmensnutzer:innen, z. B. das Hinzufügen und Löschen von Nutzer:innen, das Festlegen von Nutzerberechtigungen, das Erstellen von Teams und die Verwaltung von Unternehmenseinstellungen."
---

# Unternehmensnutzer:innen verwalten {#manage-company-users}

> Erfahren Sie, wie Sie Nutzer:innen in Ihrem Unternehmenskonto verwalten, einschließlich Hinzufügen, Sperren und Löschen von Nutzer:innen.

## Unternehmensnutzer:innen hinzufügen {#adding-company-users}

Sie müssen über Administratorberechtigungen verfügen, um Nutzer:innen zu Ihrem Braze-Konto hinzuzufügen.

So fügen Sie eine:n neue:n Nutzer:in hinzu:

1. Gehen Sie zu **Einstellungen** > **Unternehmenseinstellungen** > **Nutzer:innenverwaltung** > **Unternehmensnutzer:innen**.
2. Wählen Sie **+ Neue:n Nutzer:in hinzufügen** aus.
3. Geben Sie die erforderlichen Informationen ein, einschließlich E-Mail, Abteilung und [Nutzer:innenrolle]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#creating-a-role).
4. Wählen Sie für Nutzer:innen, die keine Administratoren sind, die [Berechtigungen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#edit-a-users-permissions) auf Firmen- und Workspace-Ebene aus, die diese:r Nutzer:in haben soll.

![Berechtigungen auf Workspace-Ebene mit einem Abschnitt für angepasste Berechtigungsfelder.]({% image_buster /assets/img/add_new_user_3.png %})

### Anforderungen an die E-Mail-Adresse {#email-address-requirements}

Jede E-Mail-Adresse, die in einer [Instanz]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints) verwendet wird, muss eindeutig sein. Das bedeutet, dass eine Fehlermeldung angezeigt wird, wenn Sie versuchen, eine E-Mail-Adresse hinzuzufügen, die bereits mit einer Person verknüpft ist, die Zugriff auf einen Firmen-Workspace in dieser Instanz hatte oder noch hat.

Wenn Ihr Team Gmail verwendet und Probleme beim Hinzufügen einer E-Mail-Adresse auftreten, können Sie einen Alias erstellen, indem Sie ein Pluszeichen (+) wie „+1“ oder „+test“ an die E-Mail-Adresse anhängen. Beispielsweise kann `contractor@braze.com` den Alias `contractor+1@braze.com` haben. E-Mails an `contractor+1@braze.com` werden weiterhin an `contractor@braze.com` zugestellt, aber der Alias wird als eindeutige E-Mail-Adresse erkannt.

Um ein Konto ohne Aliase über mehrere Firmen hinweg zu nutzen, lesen Sie [Multi-Firmen-Entwickler:innen verwenden]({{site.baseurl}}/user_guide/administer/personal/accessing_your_account#use-multi-company-developers). Wenn Sie SSO verwenden, lesen Sie [Überlegungen zu Single Sign-on (SSO)]({{site.baseurl}}/user_guide/administer/personal/accessing_your_account#considerations-for-single-sign-on-sso), bevor Sie sich mit mehreren E-Mail-Adressen registrieren.

### Kann ich die E-Mail-Adresse meines Braze-Kontos ändern? {#can-i-change-my-braze-accounts-email-address}

Aus Sicherheitsgründen können Nutzer:innen die mit ihrem Braze-Konto verknüpfte E-Mail-Adresse nicht ändern. Wenn eine Person ihre E-Mail-Adresse aktualisieren möchte, sollte ein:e Administrator:in [ein neues Konto](#adding-company-users) mit der gewünschten E-Mail-Adresse erstellen.

## Zuweisen von Nutzerzugriff und Verantwortlichkeiten {#assigning-user-access-and-responsibilities}

{% multi_lang_include permissions/differences.md content="Differences" %}

## Unternehmensnutzer:innen sperren {#suspending-company-users}

Durch das Sperren wird das Konto einer Nutzerin oder eines Nutzers in einen inaktiven Zustand versetzt. Die Person kann sich dann nicht mehr anmelden, aber die mit dem Konto verknüpften Daten bleiben erhalten. Nur Administrator:innen können Unternehmensnutzer:innen sperren oder entsperren. Beachten Sie, dass gesperrte Nutzer:innen weiterhin Benachrichtigungen von Braze erhalten können.

Um eine Nutzerin oder einen Nutzer zu sperren, gehen Sie zu **Einstellungen** > **Unternehmenseinstellungen** > **Nutzer:innenverwaltung** > **Unternehmensnutzer:innen**, suchen Sie den Nutzernamen und wählen Sie <i class="fa-solid fa-user-lock" aria-label="Nutzer:in sperren"></i> **Sperren** aus.

![Option zum Sperren einer Nutzerin oder eines Nutzers.]({% image_buster /assets/img_archive/suspend_user.png %})

Administrator:innen können Nutzer:innen auch sperren, indem sie den Namen in der Liste auswählen und im Fußbereich **Nutzer:in sperren** wählen.

![Nutzer:in sperren beim Bearbeiten der Nutzerdetails.]({% image_buster /assets/img_archive/suspend_user2.png %}){: style="max-width:70%;"}

## Unternehmensnutzer:innen löschen {#deleting-company-users}

Um eine:n Nutzer:in zu löschen, gehen Sie zu **Einstellungen** > **Unternehmenseinstellungen** > **Nutzer:innenverwaltung** > **Unternehmensnutzer:innen**, suchen Sie den Namen der/des Nutzer:in und wählen Sie <i class="fa fa-trash-can"></i> **Nutzer:in löschen** aus.

Nur Administrator:innen können Unternehmensnutzer:innen löschen, und Unternehmensnutzer:innen können ihre eigenen Konten nicht löschen. Eine:r Administrator:in kann das eigene Dashboard-Konto nicht löschen; eine:r andere:r Administrator:in muss dies übernehmen.

![Eine:n Nutzer:in löschen.]({% image_buster /assets/img_archive/delete_user_new.png %})

Nachdem eine:r Nutzer:in gelöscht wurde, speichert Braze keine der folgenden Kontodaten mehr:

- Alle Attribute, die die/der Nutzer:in hatte
- E-Mail-Adresse
- Telefonnummer
- Externe Nutzer:innen-ID
- Geschlecht
- Land
- Sprache
- Andere ähnliche Daten

Braze behält die folgenden Kontodaten:

- Angepasste Attribute oder Testdaten, die mit dem Konto verknüpft sind
- Campaigns oder Canvases, die sie erstellt haben (der Name der/des Nutzer:in wird jedoch nicht mehr angezeigt, z. B. in der Spalte **Zuletzt bearbeitet von**)

### Auswirkungen des Löschens einer:s Dashboard-Nutzer:in {#impact-of-deleting-a-dashboard-user}

Das Löschen einer:s Dashboard-Nutzer:in hat keine wesentlichen Auswirkungen auf die im Dashboard erstellten Assets wie Campaigns, Segmente und Canvases. Das Feld **Erstellt von** für diese Assets zeigt jedoch einen „null“-Wert anstelle der E-Mail-Adresse der/des gelöschten Nutzer:in an.

Wenn anschließend eine:r neue:r Dashboard-Nutzer:in mit derselben E-Mail-Adresse wie die/der gelöschte Nutzer:in erstellt wird, verknüpft Braze die von der/dem gelöschten Nutzer:in erstellten Assets nicht erneut mit der/dem neuen Nutzer:in. Die/der neue Dashboard-Nutzer:in beginnt mit einem leeren Konto und wird nicht als Ersteller:in bestehender Assets im Dashboard aufgeführt.

## Fehlerbehebung {#troubleshooting}

### „Aktion kann nicht ausgeführt werden“ beim Hinzufügen einer Nutzer:in {#unable-to-perform-action-when-adding-a-user}

Wenn das Hinzufügen einer Dashboard-Nutzer:in mit dem Fehler „Aktion kann nicht ausgeführt werden“ (oder einem ähnlichen Fehler) fehlschlägt:

- Entfernen Sie führende oder nachgestellte Leerzeichen und versteckte Zeichen aus der E-Mail-Adresse.
- Bestätigen Sie, dass die Adresse ein gültiges E-Mail-Format für Ihre Organisation hat. Einige Sonderzeichen werden abgelehnt.
- Dieselbe E-Mail-Adresse kann nicht für zwei Dashboard-Nutzer:innen im selben [Cluster]({{site.baseurl}}/user_guide/administer/personal/accessing_your_account) verwendet werden. Wenn die Adresse bereits in einem anderen Workspace in diesem Cluster registriert ist, verwenden Sie eine andere Adresse oder einen Alias wie `user+1@company.com`.

### „E-Mail ist bereits vergeben“ beim Versuch, eine Nutzer:in hinzuzufügen {#email-is-already-taken-when-trying-to-add-a-user}

Wenn Sie versuchen, eine neue Nutzer:in hinzuzufügen, und eine Fehlermeldung erhalten, dass die E-Mail bereits vergeben ist, die Person aber nicht in Ihrer Nutzerliste finden können, existiert diese Nutzer:in höchstwahrscheinlich in einer anderen Instanz desselben Braze-Dashboard-Clusters.

Um diese neue Nutzer:in zu erstellen, können Sie eine der folgenden Optionen wählen:

1. Löschen Sie die Nutzer:in aus der anderen Instanz, bevor Sie sie in der neuen erstellen, oder
2. Erstellen Sie die Nutzer:in mit einem anderen E-Mail-String (z. B. `testing+01@braze.com`) oder einem anderen E-Mail-Alias.

Wenn Sie die Aktivierungsnachricht nicht in Ihrem Posteingang erhalten, wenn Sie `testing+01@braze.com` verwenden, bestätigen Sie mit Ihrem IT-Team, dass Sie Nachrichten von dieser Art von E-Mail-Adresse empfangen können. Einige Administratoren filtern Nachrichten, die an E-Mail-Adressen mit einem `+` gesendet werden.

## Nächste Schritte {#next-steps}

Verwalten Sie nach dem Hinzufügen von Nutzer:innen deren Zugriff:

- [Berechtigungen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions), um zu konfigurieren, was jede:r Nutzer:in im Dashboard tun kann.
- [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams), um Nutzer:innen in Gruppen mit gemeinsamem Zugriff auf bestimmte Dashboard-Objekte zu organisieren.