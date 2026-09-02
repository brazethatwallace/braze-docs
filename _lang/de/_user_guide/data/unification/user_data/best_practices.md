---
nav_title: Best Practices bei der Datenerfassung
article_title: Best Practices bei der Datenerfassung
page_order: 4
page_type: reference
description: "Der folgende Artikel erläutert verschiedene Methoden und Best Practices zur Erfassung neuer und bestehender Nutzerdaten."

---

# Best Practices bei der Datenerfassung {#collection-best-practices}

> Zu wissen, wann und wie Nutzerdaten für bekannte und unbekannte Nutzer:innen erfasst werden, kann eine Herausforderung darstellen, wenn man den Kundenprofil or Nutzerprofil-Lebenszyklus Ihrer Kund:innen betrachtet. Dieser Artikel erläutert verschiedene Methoden und Best Practices zur Erfassung neuer und bestehender Nutzerdaten, indem er Sie durch einen Anwendungsfall führt.

Das folgende Beispiel ist ein Anwendungsfall für die E-Mail-Erfassung, aber die Logik gilt für viele verschiedene Szenarien der Datenerfassung. In diesem Beispiel gehen wir davon aus, dass Sie bereits ein Registrierungsformular oder eine Möglichkeit zur Erfassung von Nutzerinformationen integriert haben.

Nachdem ein:e Nutzer:in Ihnen Informationen zur Verfügung gestellt hat, empfehlen wir Ihnen, zu überprüfen, ob die Daten bereits in Ihrer Datenbank vorhanden sind, und gegebenenfalls ein Nutzer-Alias-Profil zu erstellen oder das vorhandene Kundenprofil or Nutzerprofil zu Update or aktualisieren or aktualisieren.

Wenn ein:e unbekannte:r Nutzer:in Ihre Website besucht und zu einem späteren Zeitpunkt ein Konto erstellt oder sich durch eine E-Mail-Registrierung identifiziert, muss das Zusammenführen von Profilen sorgfältig gehandhabt werden. Je nach der Methode, mit der Sie die Zusammenführung vornehmen, können Alias-Nutzerdaten oder anonyme Daten überschrieben werden.

## Nutzerdaten über ein Webformular erfassen {#capturing-user-data-through-a-web-form}

### Schritt 1: Prüfen, ob der/die Nutzer:in bereits existiert {#step-1-check-if-the-user-exists}

Wenn ein/eine Nutzer:in Inhalte über ein Webformular eingibt, prüfen Sie, ob ein/eine Nutzer:in mit dieser E-Mail-Adresse bereits in Ihrer Datenbank existiert. Sie können dies auf eine der folgenden Weisen tun:

- **Interne Datenbank prüfen (empfohlen):** Wenn Sie einen externen Datensatz oder eine Datenbank mit den bereitgestellten Nutzerinformationen haben, die außerhalb von Braze existiert, verwenden Sie diese zum Zeitpunkt der E-Mail-Übermittlung oder Kontoerstellung, um zu bestätigen, dass die Informationen nicht bereits erfasst wurden.
- **[`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track):** Verwenden Sie `email` als Bezeichner, und es wird ein neues Kundenprofil or Nutzerprofil erstellt, wenn die E-Mail-Adresse noch nicht existiert.
- **[`/subscription/status/get`-Endpunkt]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status):** Wenn Sie E-Mail-Adressen über ein benutzerdefiniertes Formular erfassen und dann die Abo-Gruppen-Zugehörigkeit über die Representational State Transfer API festlegen, rufen Sie zuerst diesen Endpunkt auf. Wenn kein passendes Profil existiert, erstellen oder abonnieren Sie den/die Nutzer:in mit dem [`/subscription/status/set`-Endpunkt]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status). Andernfalls Update or aktualisieren or aktualisieren Sie das bestehende Profil, anstatt ein Duplikat zu erstellen.

### Schritt 2: Nutzer:in protokollieren oder Update or aktualisieren or aktualisieren {#step-2-log-or-update-user}

- **Wenn ein/eine Nutzer:in existiert:**
  - Erstellen Sie kein neues Profil.
  - Protokollieren Sie ein angepasstes Attribut (zum Beispiel `newsletter_subscribed: true`) im Profil des/der Nutzer:in, um anzuzeigen, dass er/sie die E-Mail-Adresse über ein Newsletter-Abo übermittelt hat. Wenn mehrere Braze-Nutzerprofile mit derselben E-Mail-Adresse existieren, werden alle Profile exportiert.<br><br>
- **Wenn ein/eine Nutzer:in nicht existiert:**
  - Erstellen Sie ein Alias-only-Profil über den [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track). Dieser Endpunkt akzeptiert ein [`user_alias`-Objekt]({{site.baseurl}}/api/objects_filters/user_alias_object) und erstellt ein Alias-only-Profil, wenn `update_existing_only` auf `false` gesetzt ist. Legen Sie die E-Mail-Adresse des/der Nutzer:in als Nutzer-Alias fest, um diese/n Nutzer:in in Zukunft referenzieren zu können (da der/die Nutzer:in keine `external_id` hat).

![Diagramm, das den Prozess zur Aktualisierung eines Alias-only-Nutzerprofils zeigt. Ein/eine Nutzer:in übermittelt die E-Mail-Adresse und ein angepasstes Attribut, die Postleitzahl, auf einer Marketing-Landing-Page. Ein Pfeil von der Landing-Page-Erfassung zu einem Alias-only-Nutzerprofil zeigt eine Braze-API-Anfrage an den Track-User-Endpunkt, wobei der Anfragekörper den Alias-Namen, das Alias-Label, die E-Mail und die Postleitzahl enthält. Das Profil trägt die Bezeichnung „Alias-only-Nutzer:in erstellt in Braze“ mit den Attributen aus dem Anfragekörper, um zu zeigen, dass die Daten im neu erstellten Profil widergespiegelt werden.]({% image_buster /assets/img/user_profile_process3.png %}){: style="max-width:90%;"}

## E-Mail-Adressen über ein E-Mail-Erfassungsformular sammeln {#capturing-user-emails-through-an-email-capture-form}

Verwenden Sie ein E-Mail-Erfassungsformular, um Nutzer:innen aufzufordern, ihre E-Mail-Adresse einzugeben, die dann zu ihrem Kundenprofil or Nutzerprofil hinzugefügt wird. Weitere Informationen zur Einrichtung dieses Formulars finden Sie unter [E-Mail-Erfassungsformular]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/email_capture_form).

Wenn Sie ein angepasstes Formular verwenden und die Abo-Gruppen-Zugehörigkeit über die Representational State Transfer API festlegen, prüfen Sie zunächst, ob bereits ein Profil vorhanden ist, bevor Sie eine:n Nutzer:in erstellen. Siehe [Schritt 1: Prüfen, ob der/die Nutzer:in existiert](#step-1-check-if-user-exists).

## Alias-only-Nutzer:innen identifizieren {#identifying-alias-only-users}

Beim Identifizieren von Nutzer:innen bei der Kontoerstellung können Alias-only-Nutzer:innen über den [`/users/identify`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) identifiziert und einer externen ID zugewiesen werden, indem das Alias-only-Profil mit dem bekannten Profil zusammengeführt wird.

Um zu prüfen, ob ein:e Nutzer:in alias-only ist, [überprüfen Sie, ob der/die Nutzer:in existiert](#step-1-check-if-user-exists) in Ihrer Datenbank.
- Falls ein externer Datensatz vorhanden ist, können Sie den `/users/identify/`-Endpunkt aufrufen.
- Falls der [`/users/export/id`-Endpunkt]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) eine `external_id` zurückgibt, können Sie den `/users/identify/`-Endpunkt aufrufen.
- Falls der Endpunkt nichts zurückgibt, sollte kein `/users/identify/`-Aufruf erfolgen.

## Nutzerdaten erfassen, wenn bereits Nur-Alias-Nutzerinformationen vorhanden sind {#capturing-user-data-when-alias-only-user-information-is-already-present}

Wenn Nutzer:innen ein Konto erstellen oder sich durch eine E-Mail-Registrierung identifizieren, können Sie die Profile zusammenführen. Eine Liste der Felder, die zusammengeführt werden können, finden Sie unter [Verhalten bei Zusammenführungsaktualisierungen]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior).

### Doppelte Nutzerprofile zusammenführen {#merging-duplicate-user-profiles}

Wenn Ihre Nutzerdaten wachsen, können Sie doppelte Nutzerprofile über das Braze-Dashboard zusammenführen. Diese doppelten Profile müssen mithilfe derselben Suchanfrage gefunden werden. Weitere Informationen zum Zusammenführen doppelter Nutzerprofile finden Sie unter [Doppelte Nutzer:innen zusammenführen]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users).

Sie können auch den [Endpunkt „Nutzer:innen zusammenführen“]({{site.baseurl}}/api/endpoints/user_data/post_users_merge) verwenden, um ein Kundenprofil or Nutzerprofil mit einem anderen zusammenzuführen.

{% alert note %}
Nachdem Nutzerprofile zusammengeführt wurden, kann diese Aktion nicht rückgängig gemacht werden.
{% endalert %}

## Zusätzliche Ressourcen {#additional-resources}
- Lesen Sie unseren Artikel zum Braze [Kundenprofil or Nutzerprofil-Lebenszyklus]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle) für weiteren Kontext.<br>
- Sehen Sie sich unsere Dokumentation zum Festlegen von Nutzer-IDs und zum Aufrufen der `changeUser()`-Methode für [Android]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=android), [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=swift#naming-best-practices) und [Internet]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web) an.