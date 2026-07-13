---
nav_title: Best Practices bei der Datenerfassung
article_title: Best Practices bei der Datenerfassung
page_order: 4
page_type: reference
description: "Der folgende Artikel erläutert verschiedene Methoden und Best Practices zur Erfassung neuer und bestehender Nutzerdaten."

---

# Best Practices bei der Datenerfassung {#collection-best-practices}

> Zu wissen, wann und wie Nutzerdaten für bekannte und unbekannte Nutzer:innen erfasst werden, kann eine Herausforderung darstellen, wenn man den Nutzerprofil-Lebenszyklus Ihrer Kund:innen betrachtet. Dieser Artikel erläutert verschiedene Methoden und Best Practices zur Erfassung neuer und bestehender Nutzerdaten, indem er Sie durch einen Anwendungsfall führt.

Das folgende Beispiel ist ein Anwendungsfall für die E-Mail-Erfassung, aber die Logik gilt für viele verschiedene Szenarien der Datenerfassung. In diesem Beispiel gehen wir davon aus, dass Sie bereits ein Registrierungsformular oder eine Möglichkeit zur Erfassung von Nutzerinformationen integriert haben.

Nachdem ein:e Nutzer:in Ihnen Informationen zur Verfügung gestellt hat, empfehlen wir Ihnen, zu überprüfen, ob die Daten bereits in Ihrer Datenbank vorhanden sind, und gegebenenfalls ein Nutzer-Alias-Profil zu erstellen oder das vorhandene Nutzerprofil zu aktualisieren.

Wenn ein:e unbekannte:r Nutzer:in Ihre Website besucht und zu einem späteren Zeitpunkt ein Konto erstellt oder sich durch eine E-Mail-Registrierung identifiziert, muss das Zusammenführen von Profilen sorgfältig gehandhabt werden. Je nach der Methode, mit der Sie die Zusammenführung vornehmen, können Alias-Nutzerdaten oder anonyme Daten überschrieben werden.

## Erfassen von Nutzerdaten über ein Webformular {#capturing-user-data-through-a-web-form}

### 1. Schritt: Prüfen Sie, ob der oder die Nutzer:in existiert {#step-1-check-if-the-user-exists}

Wenn ein:e Nutzer:in Inhalte über ein Webformular eingibt, prüfen Sie, ob in Ihrer Datenbank bereits ein:e Nutzer:in mit dieser E-Mail existiert. Es gibt zwei Möglichkeiten, dies zu tun:

- **Interne Datenbank prüfen (empfohlen):** Wenn Sie über einen externen Datensatz oder eine externe Datenbank verfügen, der/die die angegebenen Nutzerinformationen enthält und außerhalb von Braze existiert, referenzieren Sie diesen/diese zum Zeitpunkt der E-Mail-Übermittlung oder der Kontoerstellung, um zu bestätigen, dass die Informationen nicht bereits erfasst wurden.
- **[`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track):** Verwenden Sie `email` als Bezeichner, und ein neues Nutzerprofil wird erstellt, falls die E-Mail-Adresse noch nicht vorhanden ist.

### 2. Schritt: Nutzer:innen protokollieren oder aktualisieren {#step-2-log-or-update-user}

- **Wenn ein:e Nutzer:in vorhanden ist:**
  - Legen Sie kein neues Profil an.
  - Protokollieren Sie ein angepasstes Attribut (z. B. `newsletter_subscribed: true`) im Nutzerprofil, um anzuzeigen, dass der oder die Nutzer:in seine oder ihre E-Mail über ein Newsletter-Abo übermittelt hat. Wenn mehrere Braze-Nutzerprofile mit der gleichen E-Mail-Adresse existieren, werden alle Profile exportiert.<br><br>
- **Wenn ein:e Nutzer:in nicht existiert:**
  - Erstellen Sie ein reines Alias-Profil über den [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track). Dieser Endpunkt akzeptiert ein [`user_alias`-Objekt]({{site.baseurl}}/api/objects_filters/user_alias_object) und erstellt ein reines Alias-Profil, wenn `update_existing_only` auf `false` festgelegt ist. Legen Sie die E-Mail des Nutzers oder der Nutzerin als Nutzer-Alias fest, um diese:n Nutzer:in in Zukunft zu referenzieren (da der oder die Nutzer:in keine `external_id` hat).

![Diagramm, das den Prozess zur Aktualisierung eines reinen Alias-Nutzerprofils zeigt. Ein:e Nutzer:in gibt seine/ihre E-Mail-Adresse und ein angepasstes Attribut, die Postleitzahl, auf einer Marketing-Landing-Page ein. Ein Pfeil, der von der Landing-Page-Erfassung zu einem reinen Alias-Nutzerprofil zeigt, stellt eine Braze-API-Anfrage an den Endpunkt „Nutzer:in verfolgen“ dar, wobei der Anfragetext den Aliasnamen, das Alias-Label, die E-Mail-Adresse und die Postleitzahl des Nutzers oder der Nutzerin enthält. Das Profil hat das Label „Nur in Braze erstellte:r Alias-Nutzer:in“ mit den Attributen aus dem Anfragetext, um die Daten anzuzeigen, die im neu erstellten Profil wiedergegeben werden.]({% image_buster /assets/img/user_profile_process3.png %}){: style="max-width:90%;"}

## Erfassen von Nutzer-E-Mails über ein E-Mail-Erfassungsformular {#capturing-user-emails-through-an-email-capture-form}

Verwenden Sie ein E-Mail-Erfassungsformular, um die Nutzer:innen aufzufordern, ihre E-Mail-Adresse anzugeben, die ihrem Nutzerprofil hinzugefügt wird. Weitere Informationen zum Einrichten dieses Formulars finden Sie unter [E-Mail-Erfassungsformular]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/email_capture_form).

## Identifizierung von reinen Alias-Nutzer:innen {#identifying-alias-only-users}

Bei der Identifizierung von Nutzer:innen bei der Kontoerstellung können reine Alias-Nutzer:innen über den [`/users/identify`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) identifiziert und mit einer externen ID versehen werden, indem der oder die Alias-Nutzer:in mit dem bekannten Profil zusammengeführt wird.

Um zu überprüfen, ob ein:e Nutzer:in nur über einen Alias verfügt, [prüfen Sie, ob der oder die Nutzer:in](#step-1-check-if-user-exists) in Ihrer Datenbank existiert.
- Wenn ein externer Datensatz existiert, können Sie den Endpunkt `/users/identify/` aufrufen.
- Wenn der [`/users/export/id`-Endpunkt]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) eine `external_id` zurückgibt, können Sie den Endpunkt `/users/identify/` aufrufen.
- Wenn der Endpunkt nichts zurückgibt, sollte der Aufruf von `/users/identify/` nicht durchgeführt werden.

## Erfassen von Nutzerdaten, wenn bereits Alias-Nutzerinformationen vorhanden sind {#capturing-user-data-when-alias-only-user-information-is-already-present}

Wenn ein:e Nutzer:in ein Konto erstellt oder sich per E-Mail-Registrierung identifiziert, können Sie die Profile zusammenführen. Eine Liste der Felder, die zusammengeführt werden können, finden Sie unter [Verhalten bei der Zusammenführung von Updates]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge_updates-behavior).

### Zusammenführen von doppelten Nutzerprofilen {#merging-duplicate-user-profiles}

Wenn Ihre Nutzerdaten immer umfangreicher werden, können Sie doppelte Nutzerprofile über das Braze-Dashboard zusammenführen. Diese doppelten Profile müssen mit der gleichen Suchanfrage gefunden werden. Weitere Informationen zum Zusammenführen von Nutzerprofilen finden Sie unter [Profile zusammenführen]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#merge-profiles).

Sie können auch den [Endpunkt „Nutzer:innen zusammenführen“]({{site.baseurl}}/api/endpoints/user_data/post_users_merge) verwenden, um ein Nutzerprofil mit einem anderen zusammenzuführen.

{% alert note %}
Nachdem Nutzerprofile zusammengeführt wurden, kann diese Aktion nicht mehr rückgängig gemacht werden.
{% endalert %}

## Zusätzliche Ressourcen {#additional-resources}
- Lesen Sie unseren Artikel über den [Nutzerprofil-Lebenszyklus]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle) von Braze, um weitere Informationen zu erhalten.<br>
- Sehen Sie sich unsere Dokumentation zum Festlegen von Nutzer-IDs und zum Aufrufen der Methode `changeUser()` für [Android]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=android), [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids#suggested-user-id-naming-convention) und [Web]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web) an.