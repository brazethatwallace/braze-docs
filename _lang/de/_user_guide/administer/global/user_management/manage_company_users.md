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

Sie benötigen Administratorberechtigungen, um Nutzer:innen zu Ihrem Braze-Konto hinzuzufügen.

So fügen Sie eine:n neue:n Nutzer:in hinzu:

1. Gehen Sie zu **Einstellungen** > **Nutzer:innenverwaltung** > **Unternehmensnutzer:innen**.
2. Wählen Sie **+ Add New User**.
3. Geben Sie die erforderlichen Informationen ein, einschließlich E-Mail-Adresse, Abteilung und [Nutzerrolle]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/#creating-a-role).
4. Wählen Sie für Nutzer:innen, die keine Administratoren sind, die [Berechtigungen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/#editing-a-users-permissions) auf Unternehmens- und Workspace-Ebene aus, die diese:r Nutzer:in haben soll.

![Berechtigungen auf Workspace-Ebene mit einem Abschnitt für angepasste Berechtigungsfelder.]({% image_buster /assets/img/add_new_user_3.png %})

### Anforderungen an die E-Mail-Adresse {#email-address-requirements}

Jede E-Mail-Adresse, die in einer [Instanz]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints/) verwendet wird, muss eindeutig sein. Das bedeutet: Wenn Sie versuchen, eine E-Mail-Adresse hinzuzufügen, die bereits mit einer Nutzerin oder einem Nutzer verknüpft ist, die oder der Zugriff auf einen Unternehmens-Workspace in dieser Instanz hatte oder noch hat, wird eine Fehlermeldung angezeigt.

Wenn Ihr Team Gmail verwendet und Sie Probleme beim Hinzufügen einer E-Mail-Adresse haben, können Sie einen Alias erstellen, indem Sie ein Pluszeichen (+) wie „+1“ oder „+test“ zur E-Mail-Adresse hinzufügen. Beispielsweise kann `contractor@braze.com` den Alias `contractor+1@braze.com` haben. E-Mails an `contractor+1@braze.com` werden weiterhin an `contractor@braze.com` zugestellt, aber der Alias wird als eindeutige E-Mail-Adresse erkannt.

Um ein Konto über mehrere Unternehmen hinweg ohne Aliase zu verwenden, lesen Sie [Multi-Unternehmens-Entwickler:innen verwenden]({{site.baseurl}}/user_guide/administer/personal/accessing_your_account/#use-multi-company-developers). Wenn Sie SSO verwenden, lesen Sie [Hinweise zu Single Sign-on (SSO)]({{site.baseurl}}/user_guide/administer/personal/accessing_your_account/#considerations-for-single-sign-on-sso), bevor Sie sich mit mehreren E-Mail-Adressen registrieren.

### Kann ich die E-Mail-Adresse meines Braze-Kontos ändern? {#can-i-change-my-braze-accounts-email-address}

Aus Sicherheitsgründen können Nutzer:innen die mit ihrem Braze-Konto verknüpfte E-Mail-Adresse nicht ändern. Wenn eine Nutzerin oder ein Nutzer ihre bzw. seine E-Mail-Adresse aktualisieren möchte, sollte ein:e Administrator:in [ein neues Konto erstellen](#adding-company-users) mit der gewünschten E-Mail-Adresse.

## Nutzerzugriff und Verantwortlichkeiten zuweisen {#assigning-user-access-and-responsibilities}

{% multi_lang_include permissions/differences.md content="Differences" %}

## Unternehmensnutzer:innen sperren {#suspending-company-users}

Durch das Sperren wird das Konto einer Nutzerin oder eines Nutzers in einen inaktiven Zustand versetzt, in dem sich die Person nicht mehr anmelden kann, die mit dem Konto verknüpften Daten jedoch erhalten bleiben. Nur Administratoren können Unternehmensnutzer:innen sperren oder entsperren. Beachten Sie, dass gesperrte Nutzer:innen weiterhin Benachrichtigungen von Braze erhalten können.

Um eine:n Nutzer:in zu sperren, gehen Sie zu **Einstellungen** > **Nutzer:innenverwaltung** > **Unternehmensnutzer:innen**, suchen Sie den Nutzernamen und wählen Sie <i class="fa-solid fa-user-lock"></i> **Sperren**.

![Option zum Sperren einer Nutzerin oder eines Nutzers.]({% image_buster /assets/img_archive/suspend_user.png %})

Administratoren können eine:n Nutzer:in auch sperren, indem sie den Namen in der Liste auswählen und in der Fußzeile **Nutzer:in sperren** wählen.

![Eine:n Nutzer:in sperren beim Bearbeiten der Nutzerdetails.]({% image_buster /assets/img_archive/suspend_user2.png %}){: style="max-width:70%;"}

## Unternehmensnutzer:innen löschen {#deleting-company-users}

Um eine:n Nutzer:in zu löschen, gehen Sie zu **Einstellungen** > **Nutzer:innenverwaltung** > **Unternehmensnutzer:innen**, suchen Sie den Nutzernamen und wählen Sie <i class="fa fa-trash-can"></i> **Nutzer:in löschen**.

Nur Administratoren können Unternehmensnutzer:innen löschen, und Unternehmensnutzer:innen können ihre eigenen Konten nicht löschen. Ein:e Administrator:in kann das eigene Dashboard-Konto nicht löschen; ein:e andere:r Administrator:in muss dies übernehmen.

![Eine:n Nutzer:in löschen.]({% image_buster /assets/img_archive/delete_user_new.png %})

Nachdem eine Nutzerin oder ein Nutzer gelöscht wurde, speichert Braze keine der folgenden Kontodaten mehr:

- Alle Attribute, die die Nutzerin oder der Nutzer hatte
- E-Mail-Adresse
- Telefonnummer
- Externe Nutzer-ID
- Geschlecht
- Land
- Sprache
- Andere ähnliche Daten

Braze behält die folgenden Kontodaten:

- Angepasste Attribute oder Testdaten, die mit dem Konto verknüpft sind
- Campaigns oder Canvases, die erstellt wurden (der Name der Nutzerin oder des Nutzers wird jedoch nicht mehr angezeigt, z. B. in der Spalte **Zuletzt bearbeitet von**)

### Auswirkungen des Löschens einer Dashboard-Nutzerin oder eines Dashboard-Nutzers {#impact-of-deleting-a-dashboard-user}

Wenn eine Dashboard-Nutzerin oder ein Dashboard-Nutzer gelöscht wird, hat dies keine wesentlichen Auswirkungen auf die im Dashboard erstellten Assets wie Campaigns, Segmente und Canvases. Allerdings zeigt das Feld **Erstellt von** für diese Assets einen „null“-Wert anstelle der E-Mail-Adresse der gelöschten Nutzerin oder des gelöschten Nutzers an.

Wenn anschließend eine neue Dashboard-Nutzerin oder ein neuer Dashboard-Nutzer mit derselben E-Mail-Adresse wie die gelöschte Person erstellt wird, verknüpft Braze die von der gelöschten Person erstellten Assets nicht erneut mit der neuen Nutzerin oder dem neuen Nutzer. Die neue Dashboard-Nutzerin oder der neue Dashboard-Nutzer beginnt mit einem leeren Konto und wird nicht als Ersteller:in bestehender Assets im Dashboard aufgeführt.

## Fehlerbehebung {#troubleshooting}

### „Aktion kann nicht ausgeführt werden“ beim Hinzufügen einer Nutzerin oder eines Nutzers {#unable-to-perform-action-when-adding-a-user}

Wenn das Hinzufügen einer Dashboard-Nutzerin oder eines Dashboard-Nutzers mit dem Fehler „Unable to perform action“ (oder einem ähnlichen Fehler) fehlschlägt:

- Entfernen Sie führende oder nachgestellte Leerzeichen und versteckte Zeichen aus der E-Mail-Adresse.
- Bestätigen Sie, dass die Adresse ein gültiges E-Mail-Format für Ihre Organisation hat. Einige Sonderzeichen werden abgelehnt.
- Dieselbe E-Mail kann nicht für zwei Dashboard-Nutzer:innen im selben [Cluster]({{site.baseurl}}/user_guide/administer/personal/accessing_your_account/) verwendet werden. Wenn die Adresse bereits in einem anderen Workspace in diesem Cluster registriert ist, verwenden Sie eine andere Adresse oder einen Alias wie `user+1@company.com`.

### „E-Mail ist bereits vergeben“ beim Versuch, eine:n Nutzer:in hinzuzufügen {#email-is-already-taken-when-trying-to-add-a-user}

Wenn Sie versuchen, eine:n neue:n Nutzer:in hinzuzufügen und eine Fehlermeldung erhalten, dass die E-Mail bereits vergeben ist, die Person aber nicht in Ihrer Nutzerliste finden können, existiert diese:r Nutzer:in höchstwahrscheinlich in einer anderen Instanz desselben Braze-Dashboard-Clusters.

Um diese:n neue:n Nutzer:in zu erstellen, können Sie eine der folgenden Optionen wählen:

1. Löschen Sie die Nutzerin oder den Nutzer aus der anderen Instanz, bevor Sie sie oder ihn in der neuen erstellen, oder
2. Erstellen Sie die Nutzerin oder den Nutzer mit einem anderen E-Mail-String (z. B. `testing+01@braze.com`) oder einem anderen E-Mail-Alias.

Wenn Sie die Aktivierungsnachricht nicht in Ihrem Posteingang erhalten, wenn Sie `testing+01@braze.com` verwenden, bestätigen Sie mit Ihrem IT-Team, dass Sie Nachrichten von dieser Art von E-Mail-Adresse empfangen können. Einige Administratoren filtern Nachrichten, die an E-Mail-Adressen mit einem `+` gesendet werden.

## Nächste Schritte {#next-steps}

Nachdem Sie Nutzer:innen hinzugefügt haben, verwalten Sie deren Zugriff:

- [Berechtigungen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/), um festzulegen, was jede:r Nutzer:in im Dashboard tun kann.
- [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams/), um Nutzer:innen in Gruppen mit gemeinsamem Zugriff auf bestimmte Dashboard-Objekte zu organisieren.