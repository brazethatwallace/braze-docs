---
nav_title: Unternehmensnutzer:innen
article_title: Unternehmensnutzer:innen verwalten
page_order: 0
page_type: reference
description: "Diese Seite behandelt die Verwaltung Ihrer Unternehmensnutzer:innen, z. B. das Hinzufügen und Löschen von Nutzer:innen, das Festlegen von Nutzerberechtigungen, das Erstellen von Teams und die Verwaltung von Unternehmenseinstellungen."
---

# Unternehmensnutzer:innen verwalten {#manage-company-users}

> Erfahren Sie, wie Sie Nutzer:innen in Ihrem Unternehmenskonto verwalten, einschließlich Hinzufügen, Sperren und Löschen von Nutzer:innen.

## Firmennutzer:innen hinzufügen {#adding-company-users}

Sie müssen über Administratorberechtigungen verfügen, um Nutzer:innen zu Ihrem Braze-Konto hinzuzufügen.

So fügen Sie eine:n neue:n Nutzer:in hinzu:

1. Gehen Sie zu **Einstellungen** > **Firmeneinstellungen** > **Nutzer:innenverwaltung** > **Firmennutzer:innen**.
2. Wählen Sie **+ Neue:n Nutzer:in hinzufügen** aus.
3. Geben Sie die erforderlichen Informationen ein, einschließlich E-Mail, Abteilung und [Nutzer:innenrolle]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#creating-a-role).
4. Wählen Sie für Nutzer:innen, die keine Administrator:innen sind, die [Berechtigungen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#edit-a-users-permissions) auf Firmen- und Workspace-Ebene aus, die diese:r Nutzer:in haben soll.

![Berechtigungen auf Workspace-Ebene mit einem Abschnitt für angepasste Berechtigungsfelder.]({% image_buster /assets/img/add_new_user_3.png %})

### Anforderungen an E-Mail-Adressen {#email-address-requirements}

Jede E-Mail-Adresse, die in einer [Instanz]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints) verwendet wird, muss eindeutig sein. Das bedeutet, dass Sie eine Fehlermeldung erhalten, wenn Sie versuchen, eine E-Mail-Adresse hinzuzufügen, die bereits mit einer Person verknüpft ist, die Zugriff auf einen Firmen-Workspace in dieser Instanz hatte oder noch hat.

Wenn Ihr Team Gmail nutzt und Sie Probleme beim Hinzufügen einer E-Mail-Adresse haben, können Sie einen Alias erstellen, indem Sie ein Pluszeichen (+) wie „+1“ oder „+test“ zur E-Mail-Adresse hinzufügen. Beispielsweise kann `contractor@braze.com` den Alias `contractor+1@braze.com` haben. E-Mails an `contractor+1@braze.com` werden weiterhin an `contractor@braze.com` zugestellt, aber der Alias wird als eindeutige E-Mail-Adresse erkannt.

Um ein Konto ohne Aliase in mehreren Firmen zu verwenden, lesen Sie [Multi-Firmen-Entwickler:innen verwenden]({{site.baseurl}}/user_guide/administer/personal/accessing_your_account#use-multi-company-developers). Wenn Sie Single Sign-on nutzen, lesen Sie [Hinweise zu Single Sign-on (SSO)]({{site.baseurl}}/user_guide/administer/personal/accessing_your_account#considerations-for-single-sign-on-sso), bevor Sie sich mit mehreren E-Mail-Adressen registrieren.

### Kann ich die E-Mail-Adresse meines Braze-Kontos ändern? {#can-i-change-my-braze-accounts-email-address}

Aus Sicherheitsgründen können Nutzer:innen die mit ihrem Braze-Konto verknüpfte E-Mail-Adresse nicht ändern. Wenn eine Person ihre E-Mail-Adresse aktualisieren möchte, sollte ein:e Administrator:in [ein neues Konto](#adding-company-users) mit der gewünschten E-Mail-Adresse erstellen.

## Zuweisen von Nutzerzugriff und Verantwortlichkeiten {#assigning-user-access-and-responsibilities}

{% multi_lang_include permissions/differences.md content="Differences" %}

## Unternehmensnutzer:innen sperren {#suspending-company-users}

Wenn Sie Nutzer:innen sperren, wird deren Konto in einen inaktiven Zustand versetzt. Die gesperrten Nutzer:innen können sich nicht mehr anmelden, aber die mit ihrem Konto verknüpften Daten bleiben erhalten. Nur Administrator:innen können Unternehmensnutzer:innen sperren oder die Sperrung aufheben. Beachten Sie, dass gesperrte Nutzer:innen weiterhin Benachrichtigungen von Braze erhalten können.

Um Nutzer:innen zu sperren, gehen Sie zu **Einstellungen** > **Unternehmenseinstellungen** > **Nutzer:innenverwaltung** > **Unternehmensnutzer:innen**, suchen Sie den entsprechenden Nutzernamen und wählen Sie <i class="fa-solid fa-user-lock" aria-label="Nutzer:in sperren"></i> **Sperren** aus.

![Option zum Sperren von Nutzer:innen.]({% image_buster /assets/img_archive/suspend_user.png %})

Administrator:innen können Nutzer:innen auch sperren, indem sie den Namen in der Liste auswählen und in der Fußzeile **Nutzer:in sperren** wählen.

![Nutzer:innen beim Bearbeiten der Nutzerdetails sperren.]({% image_buster /assets/img_archive/suspend_user2.png %}){: style="max-width:70%;"}

## Nutzer:innen des Unternehmens löschen {#deleting-company-users}

Um eine:n Nutzer:in zu löschen, gehen Sie zu **Einstellungen** > **Unternehmenseinstellungen** > **Nutzer:innenverwaltung** > **Unternehmensnutzer:innen**, suchen Sie den Namen der Person und wählen Sie <i class="fa fa-trash-can"></i> **Nutzer:in löschen** aus.

Nur Administrator:innen können Unternehmensnutzer:innen löschen, und Unternehmensnutzer:innen können ihre eigenen Konten nicht löschen. Administrator:innen können ihr eigenes Dashboard-Konto nicht löschen; ein:e andere:r Administrator:in muss es für sie löschen.

![Eine:n Nutzer:in löschen.]({% image_buster /assets/img_archive/delete_user_new.png %})

Nachdem eine:r Nutzer:in gelöscht wurde, speichert Braze keine der folgenden Kontodaten mehr:

- Alle Attribute, die die Person hatte
- E-Mail-Adresse
- Telefonnummer
- Externe Nutzer:innen-ID
- Geschlecht
- Land
- Sprache
- Andere ähnliche Daten

Braze speichert die folgenden Kontodaten:

- Angepasste Attribute oder Testdaten, die mit dem Konto verknüpft sind
- Campaigns oder Canvases, die erstellt wurden (der Name der Person erscheint jedoch nicht mehr darin, z. B. in der Spalte **Zuletzt bearbeitet von**)

### Auswirkungen des Löschens von Dashboard-Nutzer:innen {#impact-of-deleting-a-dashboard-user}

Das Löschen von Dashboard-Nutzer:innen hat keine wesentlichen Auswirkungen auf die von ihnen im Dashboard erstellten Assets wie Campaigns, Segments und Canvases. Das Feld **Erstellt von** für diese Assets zeigt jedoch einen „null“-Wert anstelle der E-Mail-Adresse der gelöschten Person an.

Wenn anschließend neue Dashboard-Nutzer:innen mit derselben E-Mail-Adresse wie die gelöschte Person erstellt werden, verknüpft Braze die von der gelöschten Person erstellten Assets nicht erneut mit den neuen Nutzer:innen. Die neuen Dashboard-Nutzer:innen starten mit einem leeren Konto und werden nicht als Ersteller:in bestehender Assets im Dashboard aufgeführt.

## Fehlerbehebung {#troubleshooting}

### „Aktion kann nicht ausgeführt werden“ beim Hinzufügen von Nutzer:innen {#unable-to-perform-action-when-adding-a-user}

Wenn das Hinzufügen von Dashboard-Nutzer:innen mit dem Fehler „Unable to perform action“ (oder einem ähnlichen Fehler) fehlschlägt:

- Entfernen Sie führende oder nachgestellte Leerzeichen sowie versteckte Zeichen aus der E-Mail-Adresse.
- Überprüfen Sie, ob die Adresse ein gültiges E-Mail-Format für Ihre Organisation hat. Einige Sonderzeichen werden abgelehnt.
- Dieselbe E-Mail-Adresse kann nicht für zwei Dashboard-Nutzer:innen im selben [Cluster]({{site.baseurl}}/user_guide/administer/personal/accessing_your_account) verwendet werden. Wenn die Adresse bereits in einem anderen Workspace auf diesem Cluster registriert ist, verwenden Sie eine andere Adresse oder einen Alias wie `user+1@company.com`.

### „Email is already taken“ beim Versuch, Nutzer:innen hinzuzufügen {#email-is-already-taken-when-trying-to-add-a-user}

Wenn Sie versuchen, neue Nutzer:innen hinzuzufügen, und eine Fehlermeldung erhalten, dass die E-Mail-Adresse bereits vergeben ist, Sie die Person aber nicht in Ihrer Nutzerliste finden können, existiert diese Person höchstwahrscheinlich in einer anderen Instanz desselben Braze-Dashboard-Clusters.

Um diese neuen Nutzer:innen zu erstellen, können Sie eine der folgenden Optionen wählen:

1. Löschen Sie die Nutzer:innen aus der anderen Instanz, bevor Sie sie in der neuen erstellen, oder
2. Erstellen Sie die Nutzer:innen mit einem anderen E-Mail-String (z. B. `testing+01@braze.com`) oder einem anderen E-Mail-Alias.

Wenn Sie die Aktivierungsnachricht nicht in Ihrem Posteingang erhalten, wenn Sie `testing+01@braze.com` verwenden, bestätigen Sie mit Ihrem IT-Team, dass Sie Nachrichten von dieser Art von E-Mail-Adresse empfangen können. Einige Administrierende filtern Nachrichten, die an E-Mail-Adressen mit einem `+` gesendet werden.

## Nächste Schritte {#next-steps}

Nachdem Sie Nutzer:innen hinzugefügt haben, verwalten Sie deren Zugriff:

{% article_tiles %}
- name: Berechtigungen
  link: /docs/user_guide/administer/global/user_management/permissions
  description: Konfigurieren Sie, was jede:r Nutzer:in im Dashboard tun kann.
- name: Teams
  link: /docs/user_guide/administer/global/user_management/teams
  description: Organisieren Sie Nutzer:innen in Gruppen mit gemeinsamen Zugriffsrechten auf bestimmte Dashboard-Objekte.
{% endarticle_tiles %}