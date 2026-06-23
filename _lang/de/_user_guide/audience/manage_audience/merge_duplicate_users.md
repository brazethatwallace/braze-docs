---
nav_title: Doppelte Nutzer:innen zusammenführen
article_title: Doppelte Nutzer:innen zusammenführen
description: "Erfahren Sie, wie Sie doppelte Nutzer:innen in Ihrem Braze-Dashboard finden und zusammenführen."
page_order: 4
---

# Doppelte Nutzer:innen zusammenführen {#merge-duplicate-users}

> Erfahren Sie, wie Sie doppelte Nutzer:innen finden und zusammenführen, um die Effektivität Ihrer Campaigns und Canvases zu maximieren.

## REST API: Nutzer:innen identifizieren und zusammenführen {#rest-api-identify-and-merge-users}

Die Tools auf dieser Seite führen doppelte Profile im Dashboard zusammen. Sie können Profile auch über die [User-Data-Endpunkte]({{site.baseurl}}/api/endpoints/user_data/) von Braze kombinieren oder umleiten:

- [POST: Nutzer:innen identifizieren]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) (`/users/identify`): Kombiniert ein Nur-Alias-, Nur-E-Mail- oder Nur-Telefonnummer-Profil mit einem Profil, das eine `external_id` hat.
- [POST: Nutzer:innen zusammenführen]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) (`/users/merge`): Führt ein Nutzerprofil mit einem anderen zusammen, auch wenn beide Profile bereits eine `external_id` haben. Lesen Sie [Voraussetzungen]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#prerequisites) und [Zusammenführungsverhalten]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge-behavior), bevor Sie diesen Endpunkt aufrufen.

Wenn ein anonymes Profil einem bestehenden identifizierten Profil zugeordnet wird (z. B. durch einen SDK-`changeUser()`-Aufruf oder `/users/identify`), verwaist Braze das anonyme Profil und kopiert nur bestimmte Felder auf das identifizierte Profil. Weitere Informationen finden Sie unter [Was passiert, wenn Sie anonyme Nutzer:innen identifizieren]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/#what-happens-when-you-identify-anonymous-users).

Zusammenführungen von Nutzer:innen sind schwer rückgängig zu machen. Wenn Sie eine komplexe Zusammenführung über mehrere `external_id`-Werte oder große Profilmigrationen planen, wenden Sie sich an Ihren Customer-Success-Manager, bevor Sie sich auf `/users/merge` verlassen.

Braze behandelt drei Nutzertypen beim Zusammenführen unterschiedlich: zum Löschen markierte Nutzer:innen, Testnutzer:innen und Nutzer:innen der Globalen Kontrollgruppe. Weitere Details finden Sie unter [Zusammenführungsverhalten von Nutzer:innen]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users/merge_behavior/).

## Einzelnes Zusammenführen {#individual-merging}

Wenn eine Nutzersuche doppelte Profile zurückgibt, können Sie jedes Profil einzeln über das Nutzerprofil im Braze-Dashboard zusammenführen.

### 1. Schritt: Nach einem doppelten Profil suchen {#step-1-search-for-a-duplicate-profile}

Wählen Sie in Braze **Audience** > **User Search**.

![Die Kachel „User Search“ ist im Navigationsmenü hervorgehoben.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/select_search_users.png %}){: style="max-width:60%;"}

Geben Sie einen eindeutigen Bezeichner ein, z. B. eine E-Mail-Adresse oder Telefonnummer, für das doppelte Profil und wählen Sie dann **Search**.

![Die Seite „User Search“ im Braze-Dashboard.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/search_user.png %}){: style="max-width:60%;"}

### 2. Schritt: Duplikate zusammenführen {#step-2-merge-duplicates}

Um den Zusammenführungsprozess zu starten, wählen Sie **Merge duplicates**.

![Eines der doppelten Nutzerprofile.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/select_merge_duplicates.png %}){: style="max-width:50%;"}

Wählen Sie aus, welches Nutzerprofil beibehalten und welches zusammengeführt werden soll, und wählen Sie dann **Merge profiles**. Wiederholen Sie diesen Vorgang, bis Sie alle doppelten Profile zusammengeführt haben.


{% alert warning %}
Doppelte Nutzerprofile können nach dem Zusammenführen nicht wiederhergestellt werden.
{% endalert %}

## Massen-Zusammenführung {#bulk-merging}

Wenn Sie doppelte Nutzer:innen in einer Massen-Zusammenführung verarbeiten, findet Braze Profile mit übereinstimmenden Bezeichnern (z. B. einer E-Mail-Adresse) und behält ein Profil bei. Braze priorisiert zunächst Profile mit einer `external_id` und wendet dann Ihre Einstellungen unter **Resolving ties** an: **Resolve ties using** und **Prioritization**. Wenn es keine Profile mit einer `external_id` gibt, verwendet Braze **Resolve ties using** und **Prioritization** für Profile ohne `external_id`. Braze führt Nutzer:innen nur zusammen, wenn diese Einstellungen ein beizubehaltendes Profil identifizieren. Wenn beispielsweise **Resolve ties using** auf **Updated date** gesetzt ist und beide Profile denselben Zeitstempel der letzten Aktualisierung haben, kann Braze den Gleichstand nicht auflösen, sodass diese Nutzer:innen nicht zusammengeführt werden.

### 1. Schritt: Zu „Manage Audience“ navigieren {#step-1-go-to-manage-audience}

Wählen Sie im Braze-Dashboard **Audience** > **Manage Audience**.

![Die Kachel „Manage Audience“ ist im Navigationsmenü hervorgehoben.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_manage_audience.png %}){: style="max-width:60%;"}

### 2. Schritt: Ergebnisse in der Vorschau anzeigen (optional) {#step-2-preview-the-results-optional}

Um Ihre Ergebnisse vor dem Zusammenführen Ihrer Duplikate in der Vorschau anzuzeigen, wählen Sie **Generate list of duplicates**.

![Die Seite „Manage Audience“ mit hervorgehobener Option „Generate list of duplicates“.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_generate_list.png %})

Braze generiert Ihre Vorschau und sendet sie als CSV-Datei an Ihre E-Mail-Adresse.


Im folgenden Beispiel verwendet Braze die externe ID der Nutzer:innen, um doppelte Profile zu kennzeichnen und zu identifizieren, welches beibehalten werden soll. Wenn diese Profile in einer Massen-Zusammenführung verarbeitet werden, verwendet Braze das Profil mit einer externen ID als neues primäres Profil der Nutzer:innen.

{% tabs local %}
{% tab example csv file %}
| Email Address    | External ID | Phone Number   | Braze ID              | Identifier for rule | Profile to keep | Profile to merge |
| ---------------- | ----------- | -------------- | --------------------- | ------------------- | --------------- | ---------------- |
| alex@company.com | A8i3mkd99   | (555) 123-4567 | 65fcaa547f470494d1370 | email               | TRUE            | FALSE            |
| alex@company.com |             | (555) 987-6543 | 65fcaa547f47d004d1348 | email               | FALSE           | TRUE             |
| alex@company.com |             | (555) 321-0987 | 65fcaa547f47d0049135c | email               | FALSE           | TRUE             |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="2. Schritt: Ergebnisse in der Vorschau anzeigen (optional)" }
{% endtab %}
{% endtabs %}

#### Zusammenführungsverhalten {#merge-behavior}

Braze füllt leere Felder im beibehaltenen Profil mit Werten aus dem zusammengeführten Profil. Eine Liste der Felder, die gefüllt werden, finden Sie unter [Zusammenführungsverhalten]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge-behavior).

### 3. Schritt: Ihre Duplikate zusammenführen {#step-3-merge-your-duplicates}

Wenn Sie mit den Ergebnissen Ihrer Vorschau zufrieden sind, wählen Sie **Merge all duplicates**.

{% alert warning %}
Doppelte Nutzerprofile können nach dem Zusammenführen nicht wiederhergestellt werden.
{% endalert %}


## Regelbasiertes Zusammenführen {#rules-based-merging}

Sie können Regeln verwenden, um zu steuern, wie doppelte Profile beim Zusammenführen aufgelöst werden, damit das relevanteste Nutzerprofil beibehalten wird. Wenn Regeln festgelegt sind, behält Braze Profile bei, die Ihren Kriterien entsprechen.

### 1. Schritt: Ihre Regeln definieren {#step-1-define-your-rules}

1. Gehen Sie zu **Audience** > **Manage Audience** > **Edit rules**.
2. Wählen Sie im Abschnitt **Profile to keep** des Panels **Edit rules** den **Identifier** für die Profile aus, die beim Zusammenführen von Duplikaten beibehalten werden sollen. Dies kann die E-Mail-Adresse oder Telefonnummer sein.
3. Wählen Sie im Abschnitt **Resolving ties** die Kriterien aus, um Gleichstände zwischen Profilen mit übereinstimmenden Kriterien aus **Profile to keep** aufzulösen. Sie können Folgendes auswählen:<br>
- **Resolve ties using**: Created date, Updated date, Last session
- **Prioritization**: Newest, Oldest

![Das Panel „Edit rules“ mit Abschnitten zur Auswahl von Optionen für „Profile to keep“ und „Resolving ties“.]({% image_buster /assets/img/audience_management/duplicate_users/edit_rules.png %}){: style="max-width:40%;"}

Beispielsweise könnten Sie das Profil beibehalten, das eine Telefonnummer hat. Wenn mehrere Nutzer:innen dieselbe Telefonnummer haben, könnten Sie Gleichstände über das Feld **Updated date** auflösen und die zuletzt aktualisierte Person priorisieren.

### 2. Schritt: Ergebnisse in der Vorschau anzeigen (optional)

Nachdem Sie Ihre Regeln gespeichert haben, können Sie eine Vorschau anzeigen, wie sie funktionieren, indem Sie **Generate a list of duplicates** auswählen. Braze generiert Ihre Vorschau und sendet sie als CSV-Datei an Ihre E-Mail-Adresse, die zeigt, welche Nutzer:innen beibehalten und zusammengeführt würden, wenn Ihre Regeln angewendet werden.

### 3. Schritt: Duplikate zusammenführen {#step-3-merge-duplicates}

Wenn Sie mit den Ergebnissen Ihrer Vorschau zufrieden sind, kehren Sie zur Seite **Manage Audience** zurück und wählen Sie **Merge all duplicates**.

{% alert warning %}
Doppelte Nutzerprofile können nach dem Zusammenführen nicht wiederhergestellt werden.
{% endalert %}

## Geplantes Zusammenführen {#scheduled-merging}

Ähnlich wie beim regelbasierten Zusammenführen ermöglicht Ihnen das geplante Zusammenführen, die Zusammenführung von Nutzerprofilen auf täglicher Basis mithilfe vorkonfigurierter Regeln zu automatisieren.

![Die Seite „Manage Audience“ mit dem Button „schedule“.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_scheduled_merge_rules.png %})

Nachdem das Feature aktiviert wurde, weist Braze automatisch ein Zeitfenster zu, um den Zusammenführungsprozess täglich gegen 0:00 Uhr in der Zeitzone des Unternehmens durchzuführen. Sie können das geplante Zusammenführen jederzeit deaktivieren. Braze benachrichtigt die Admins Ihres Workspace 24 Stunden vor der geplanten Zusammenführung, um eine Erinnerung und Zeit zur Überprüfung der Konfiguration zu geben.

{% alert warning %}
Doppelte Nutzerprofile können nach dem Zusammenführen nicht wiederhergestellt werden.
{% endalert %}

## Warum sind mehrere Nutzerprofile mit derselben E-Mail-Adresse verknüpft? {#why-are-multiple-user-profiles-associated-with-the-same-email-address}

Braze speichert mehrere Nutzerprofile, die dieselbe E-Mail-Adresse teilen, wenn Profile über verschiedene Bezeichner, Importe oder anonyme Sitzungen vor der Identifizierung erstellt werden. Dies ist ein erwartetes Verhalten, wenn Nutzer:innen keine gemeinsame `external_id` haben.

Bevor Sie Duplikate zusammenführen, verwenden Sie den [Endpunkt „Nutzerprofil nach Bezeichner exportieren“]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/), um zu bestätigen, welche Profile für eine E-Mail-Adresse existieren und welche Felder jedes Profil enthält. Sie können auch in **Audience** > **User Search** nach E-Mail suchen, um Duplikate im Dashboard zu überprüfen.

## Verwandte Artikel {#related-articles}

- [Zusammenführungsverhalten von Nutzer:innen]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users/merge_behavior/)
- [POST: Nutzer:innen zusammenführen]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/)
- [Nutzer:innen löschen]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/delete_users/)