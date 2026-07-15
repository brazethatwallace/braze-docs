---
nav_title: "Einrichtung"
article_title: LINE-Einrichtung
description: "Dieser Artikel beschreibt, wie Sie den Braze LINE-Kanal einrichten, einschließlich Voraussetzungen und empfohlener nächster Schritte."
page_type: partner
search_tag: Partner
page_order: 0
channel:
 - LINE
alias: /line/line_setup/
---


# LINE-Einrichtung {#line-setup}

> Dieser Artikel beschreibt, wie Sie den LINE-Kanal in Braze einrichten, einschließlich der Einrichtung von Nutzer:innen, der Abstimmung von Nutzer-IDs und der Erstellung von LINE-Testnutzer:innen in Braze.

## Voraussetzungen {#prerequisites}

Für die Integration von LINE mit Braze benötigen Sie Folgendes:

- [LINE-Geschäftskonto](https://www.linebiz.com/jp-en/manual/OfficialAccountManager/tutorial-steps/?list=7171)
- Premium- oder verifizierter Kontostatus (erforderlich für die Synchronisierung bestehender Follower)
   - Siehe [LINE-Kontorichtlinien](https://terms2.line.me/official_account_guideline_oth)
- [LINE-Entwicklerkonto](https://developers.line.biz/en/docs/line-developers-console/login-account/)
- [LINE Messaging API-Kanal](https://developers.line.biz/en/docs/line-developers-console/overview/#channel)

Der Versand von LINE-Nachrichten über Braze wird von den Nachrichtenguthaben oder Aktionsguthaben Ihres Kontos abgezogen.

{% alert note %}
**`native_line_id` festlegen**: Sie können `native_line_id` festlegen, indem Sie Nutzeraktualisierungen an Braze senden (z. B. mit dem [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)-Endpunkt, [CSV-Import]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv) oder [Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)). Wenn Ihr clientseitiges SDK kein dediziertes Feld für `native_line_id` hat, senden Sie es in serverseitigen Nutzeraktualisierungen über eine dieser Methoden.
{% endalert %}

## Arten von LINE-Konten {#types-of-line-accounts}

| Kontotyp | Beschreibung |
| --- | --- |
| Nicht verifiziertes Konto | Ein nicht überprüftes Konto, das von jeder Person (Einzelperson oder Unternehmen) erstellt werden kann. Dieses Konto wird mit einem grauen Badge dargestellt und erscheint nicht in den Suchergebnissen der LINE-App. |
| Verifiziertes Konto | Ein Konto, das die LINE Yahoo-Überprüfung bestanden hat. Dieses Konto wird mit einem blauen Badge dargestellt und erscheint in den Suchergebnissen der LINE-App.<br><br>Dieses Konto ist nur für Konten mit Sitz in Japan, Taiwan, Thailand und Indonesien verfügbar. |
| Premium-Konto | Ein Konto, das die LINE Yahoo-Überprüfung bestanden hat. Dieses Konto wird mit einem grünen Badge dargestellt und erscheint in den Suchergebnissen der LINE-App. Dieser Kontotyp wird während der Überprüfung automatisch nach Ermessen von LINE vergeben. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Arten von LINE-Konten" }

### Erforderlicher Kontotyp {#required-account-type}

Um Follower in Braze zu synchronisieren, muss Ihr LINE-Konto verifiziert oder Premium sein. Wenn Sie ein Konto erstellen, ist der Standardstatus „nicht verifiziert“. Sie müssen eine Kontoverifizierung beantragen.

### Verifiziertes LINE-Konto beantragen {#applying-for-a-verified-line-account}

{% alert important %}
Verifizierte Konten sind nur für Konten mit Sitz in Japan, Taiwan, Thailand und Indonesien verfügbar.
{% endalert %}

1. Wählen Sie auf der LINE-Seite **Official Account** die Option **Settings**.
2. Wählen Sie unter **Information Disclosure Verification Status** die Option **Request Account Verification**.
3. Geben Sie die erforderlichen Informationen ein.
4. Warten Sie auf eine Benachrichtigung mit den Überprüfungsergebnissen.

## LINE integrieren {#integrating-line}

Um konsistente Nutzeraktualisierungen einzurichten, bestehende LINE-IDs von Nutzer:innen zu übernehmen und sie alle mit den Abo-Status von LINE zu synchronisieren:

1. [Bestehende bekannte Nutzer:innen importieren oder aktualisieren](#step-1-import-or-update-existing-line-users)
2. [LINE-Kanal integrieren](#step-2-integrate-line-channel)
3. [Nutzer-IDs abstimmen](#step-3-reconcile-user-ids)
4. [Methoden zur Nutzeraktualisierung ändern](#step-4-change-your-user-update-methods)
5. [(Optional) Nutzerprofile zusammenführen](#step-5-merge-profiles-optional)

{% alert note %}
Sie können nur ein LINE-Konto in einem einzelnen Workspace haben. Wenn Sie mehrere LINE-Konten haben, empfehlen wir, jedes in einem anderen Workspace zu verwenden.
{% endalert %}

## Schritt 1: Bestehende LINE-Nutzer:innen importieren oder aktualisieren {#step-1-import-or-update-existing-line-users}

Dieser Schritt ist erforderlich, wenn Sie bereits identifizierte LINE-Nutzer:innen haben, da Braze später automatisch deren Abo-Status abruft und das richtige Nutzerprofil aktualisiert. Wenn Sie Nutzer:innen noch nicht mit ihrer LINE-ID abgestimmt haben, überspringen Sie diesen Schritt.

Sie können Nutzer:innen mit jeder von Braze unterstützten Methode importieren oder aktualisieren, einschließlich des [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)-Endpunkts, [CSV-Import]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv) oder [Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion).

Unabhängig von der verwendeten Methode aktualisieren Sie `native_line_id`, um die LINE-ID der Nutzer:innen bereitzustellen. Weitere Informationen zu `native_line_id` finden Sie unter [Nutzereinrichtung](#user-setup).

{% alert note %}
Der Abo-Gruppenstatus sollte nicht angegeben werden und wird ignoriert. LINE ist die maßgebliche Quelle für den Abo-Status von Nutzer:innen, der entweder über das Abo-Synchronisierungstool oder durch Ereignisaktualisierungen mit Braze synchronisiert wird.
{% endalert %}

## Schritt 2: LINE-Kanal integrieren {#step-2-integrate-line-channel}

Nach Abschluss des Integrationsprozesses ruft Braze automatisch die LINE-Follower dieses Kanals in Braze ab. Für alle LINE-IDs, die bereits mit einem Braze-Nutzerprofil verknüpft sind, wird jedes Profil mit dem Status „abonniert“ aktualisiert, und alle verbleibenden LINE-IDs erzeugen anonyme Nutzer:innen. Zusätzlich werden für neue Follower Ihres LINE-Kanals nicht identifizierte Nutzerprofile erstellt, wenn sie dem Kanal folgen.

### Schritt 2.1: Webhook-Einstellungen bearbeiten {#step-21-edit-webhook-settings}

1. Gehen Sie in LINE zum Tab **Messaging API** und bearbeiten Sie Ihre **Webhook-Einstellungen**:
   - Setzen Sie die **Webhook URL** auf `https://anna.braze.com/line/events`.
      - Braze ändert diese automatisch in eine andere URL bei der Integration, basierend auf Ihrem Dashboard-Cluster.
   - Aktivieren Sie **Use webhook** und **Webhook redelivery**. <br><br> ![Seite mit Webhook-Einstellungen zum Überprüfen oder Bearbeiten der Webhook-URL, mit Umschaltern für „Use webhook“, „Webhook redelivery“ und „Error statistics aggregation“.]({% image_buster /assets/img/line/webhook_settings.png %}){: style="max-width:70%;"}
2. Notieren Sie sich die folgenden Informationen im Tab **Providers**:

| Informationstyp | Ort |
| --- | --- |
| Provider-ID | Wählen Sie Ihren Provider und gehen Sie dann zu **Settings** > **Basic information** |
| Kanal-ID | Wählen Sie Ihren Provider und gehen Sie dann zu **Channels** > Ihr Kanal > **Basic settings** |
| Kanalgeheimnis | Wählen Sie Ihren Provider und gehen Sie dann zu **Channels** > Ihr Kanal > **Basic settings** |
| Kanalzugriffstoken | Wählen Sie Ihren Provider und gehen Sie dann zu **Channels** > Ihr Kanal > **Messaging API**. Wenn kein Kanalzugriffstoken vorhanden ist, wählen Sie **Issue**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Webhook-Einstellungen bearbeiten" }

{% alert note %}
Wenn Sie das Kanalgeheimnis für einen bereits integrierten LINE-Kanal aktualisieren oder rotieren müssen, wenden Sie sich an den [Braze-Support]({{site.baseurl}}/braze_support), um eine Aktualisierung anzufordern.
{% endalert %}

{: start="3"}
3. Gehen Sie zu Ihrer Seite **Settings** > **Response settings** und führen Sie Folgendes aus:
   - Deaktivieren Sie **Greeting message**. Dies kann in Braze über einen Trigger bei Follow gehandhabt werden.
   - Deaktivieren Sie **Auto-response messages**. Alle getriggerten Nachrichten sollten über Braze erfolgen. Dies verhindert nicht, dass Sie direkt über die LINE-Konsole senden.
   - Aktivieren Sie **Webhooks**.

![Seite mit Antworteinstellungen mit Umschaltern für die Handhabung von Chats durch Ihr Konto.]({% image_buster /assets/img/line/response_settings.png %}){: style="max-width:80%;"}

### Schritt 2.2: LINE-Abo-Gruppen in Braze generieren {#step-22-generate-line-subscription-groups-in-braze}

{% multi_lang_include alerts/note_alerts.md alert='subscription group limit' %}

1. Gehen Sie zur Braze-Technologie-Partnerseite für LINE und geben Sie die Informationen ein, die Sie sich aus dem LINE-Tab **Providers** notiert haben:
   - Provider-ID
   - Kanal-ID
   - Kanalgeheimnis
   - Kanalzugriffstoken

Wenn Sie IP-Whitelisting in Ihrem LINE-Konto hinzufügen möchten, fügen Sie alle für Ihren Cluster aufgeführten IP-Adressen unter [IP-Allowlisting]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#ip-allowlisting) zu Ihrer Allowlist hinzu.

{% alert important %}
Stellen Sie während der Integration sicher, dass Ihr Kanalgeheimnis korrekt ist. Wenn es falsch ist, kann es zu Inkonsistenzen beim Abo-Status kommen.
{% endalert %}

![LINE-Messaging-Integrationsseite mit LINE-Integrationsabschnitt.]({% image_buster /assets/img/line/integration.png %}){: style="max-width:80%;"}

{: start="2"}
2. Nach der Verbindung generiert Braze automatisch eine Braze-Abo-Gruppe für jede LINE-Integration, die erfolgreich zu Ihrem Workspace hinzugefügt wurde. <br><br> Alle Änderungen an Ihrer Followerliste (z. B. neue Follower oder Entfollower) werden automatisch an Braze übertragen.

![Abschnitt LINE-Abo-Gruppen mit einer Abo-Gruppe für den Kanal „LINE“.]({% image_buster /assets/img/line/line_subscription_groups.png %}){: style="max-width:80%;"}

## Schritt 3: Nutzer-IDs abstimmen {#step-3-reconcile-user-ids}

Kombinieren Sie die LINE-IDs Ihrer Nutzer:innen mit ihren bestehenden Braze-Nutzerprofilen, indem Sie die Schritte unter [Nutzer-ID-Abstimmung](#user-id-reconciliation) befolgen.

## Schritt 4: Methoden zur Nutzeraktualisierung ändern {#step-4-change-your-user-update-methods}

Vorausgesetzt, Sie haben bereits eine Methode, um Nutzeraktualisierungen an Braze zu senden, müssen Sie diese aktualisieren, um das neue Feld `native_line_id` einzuschließen, damit nachfolgende Nutzeraktualisierungen, die an Braze gesendet werden, dieses Feld enthalten.

Nicht identifizierte Nutzerprofile mit einer `native_line_id` können in Braze existieren, die im Rahmen des Abo-Status-Synchronisierungsprozesses erstellt wurden oder wenn ein neuer Follower Ihrem Kanal gefolgt ist.

Wenn LINE-Nutzer:innen in Ihrer Anwendung durch [Nutzerabstimmung](#user-id-reconciliation) oder andere Mittel identifiziert werden, können Sie ein potenziell nicht identifiziertes Nutzerprofil in Braze über den [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify)-Endpunkt ansprechen. Jedes nicht identifizierte Nutzerprofil mit einer `native_line_id` hat auch einen Nutzer-Alias `line_id`, der verwendet werden kann, um das Nutzerprofil zur Identifizierung anzusprechen.

Hier ist ein Beispiel-Payload für `/users/identify`, der ein nicht identifiziertes Nutzerprofil über den Nutzer-Alias `line_id` anspricht:

{% raw %}
```json
{
   "aliases_to_identify": [
       {
           "external_id": "known_external_id_from_your_application",
           "user_alias": {
               "alias_name": "U89f4a626548ccd48482f529a482f138b",
               "alias_label": "line_id"
           }
       }
   ]
}
```
{% endraw %}

Wenn kein bestehendes Nutzerprofil für Ihre angegebene `external_id` existiert, wird es dem nicht identifizierten Nutzerprofil hinzugefügt und dieses damit identifiziert. Wenn ein Nutzerprofil für die `external_id` existiert, werden alle Attribute, die ausschließlich im nicht identifizierten Nutzerprofil vorhanden sind, in das bekannte Nutzerprofil kopiert, einschließlich `native_line_id` und des Abo-Status der Nutzer:innen.

Sie können LINE-Nutzer:innen, die in Ihrer Anwendung bekannt sind, über den [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)-Endpunkt aktualisieren, indem Sie deren externe Bezeichner und `native_line_id` übergeben. Wenn bereits ein nicht identifiziertes Nutzerprofil für Nutzer:innen existiert und dieselbe `native_line_id` über `/users/track` einem anderen Nutzerprofil hinzugefügt wird, erbt es alle Abo-Status des nicht identifizierten Nutzerprofils. Es werden jedoch doppelte Nutzerprofile mit derselben `native_line_id` existieren. Alle nachfolgenden Abo-Aktualisierungen durch Ereignisaktualisierungen werden alle Profile entsprechend aktualisieren.

{% alert note %}
LINE-Abo-Status werden anhand der `native_line_id` verfolgt, nicht anhand der `external_id`. Wenn beispielsweise das Nutzerprofil von Nutzer:in B mit derselben `native_line_id` wie Nutzer:in A erstellt wird, aber nicht mit derselben `external_id`, erbt Nutzer:in B den LINE-Abo-Status von Nutzer:in A.
{% endalert %}

Hier ist ein Beispiel-Payload für `/users/track`, der ein Nutzerprofil anhand der externen Nutzer-ID aktualisiert, um eine `native_line_id` hinzuzufügen:

{% raw %}
```json
{
   "attributes": [
       {
           "external_id": "known_external_id_from_your_application",
           "native_line_id": "U89f4a626548ccd48482f529a482f138b",
           "other": "attribute"
       }
   ]
}
```
{% endraw %}

## Schritt 5: Profile zusammenführen (optional) {#step-5-merge-profiles-optional}

Wie oben beschrieben, besteht die Möglichkeit, dass mehrere Nutzerprofile mit derselben `native_line_id` existieren. Wenn Ihre Aktualisierungsmethoden doppelte Nutzerprofile erstellen, können Sie nicht identifizierte Nutzerprofile mit identifizierten Nutzerprofilen über den `/user/merge`-Endpunkt zusammenführen.

Hier ist ein Beispiel-Payload für `/users/merge`, der ein nicht identifiziertes Nutzerprofil über den Nutzer-Alias `line_id` anspricht:

{% raw %}
```json
{
 "merge_updates": [
   {
     "identifier_to_merge": {
       "user_alias": {
         "alias_name": "U89f4a626548ccd48482f529a482f138b",
         "alias_label": "line_id"
       }
     },
     "identifier_to_keep": {
       "external_id": "known_external_id_from_your_application"
     }
   }
 ]
}
```
{% endraw %}

{% alert tip %}
Weitere Informationen zur Verwaltung doppelter Nutzer:innen in Braze finden Sie unter [Doppelte Nutzer:innen]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users).
{% endalert %}

## Nutzereinrichtung {#user-setup}

LINE ist die maßgebliche Quelle für die Abo-Status von Nutzer:innen. Selbst wenn Sie die LINE-ID für Nutzer:innen haben (`native_line_id`), wird LINE keine Nachrichten an die Nutzer:innen zustellen, wenn diese dem LINE-Kanal, von dem Sie senden, nicht gefolgt sind.

Um dies zu verwalten, bietet Braze Tools und Logik, die eine gut integrierte Nutzerbasis unterstützen, einschließlich Abo-Synchronisierung und Ereignisaktualisierungen für LINE-Follows und -Unfollows.

### Abo-Synchronisierung und Ereignislogik {#subscription-syncing-and-event-logic}

1. **Abo-Synchronisierungstool:** Dieses Tool wird nach einer erfolgreichen LINE-Kanalintegration automatisch bereitgestellt. Verwenden Sie es, um bestehende Profile zu aktualisieren und neue Profile zu erstellen.<br><br>Alle Braze-Nutzerprofile, die eine `native_line_id` haben und dem LINE-Kanal folgen, werden auf den Abo-Gruppenstatus `subscribed` aktualisiert. Jeder Follower des LINE-Kanals, der kein Braze-Nutzerprofil mit der `native_line_id` hat, erhält:<br><br>- Ein anonymes Nutzerprofil, bei dem `native_line_id` auf die LINE-ID der Nutzer:innen gesetzt wird, die dem Kanal folgen <br>- Einen Nutzer-Alias `line_id`, der auf die LINE-ID der Nutzer:innen gesetzt wird, die dem Kanal folgen <br>- Einen Abo-Gruppenstatus von `subscribed`

{: start="2"}
2. **Ereignisaktualisierungen:** Diese werden verwendet, um den Abo-Status von Nutzer:innen zu aktualisieren. Wenn Braze Nutzerereignisaktualisierungen für den integrierten LINE-Kanal erhält und das Ereignis ein Follow ist, erhält das Nutzerprofil den Abo-Gruppenstatus `subscribed`. Wenn das Ereignis ein Unfollow ist, erhält das Nutzerprofil den Abo-Gruppenstatus `unsubscribed`.<br><br>- Alle Braze-Nutzerprofile mit einer übereinstimmenden `native_line_id` werden automatisch aktualisiert. <br>- Wenn kein übereinstimmendes Nutzerprofil für ein Ereignis existiert, erstellt Braze [anonyme Nutzer:innen]({{site.baseurl}}/line/user_management).

## Anwendungsfälle {#use-cases}

Dies sind Anwendungsfälle, wie Nutzer:innen nach Befolgen der Einrichtungsschritte aktualisiert werden können.

### Bestehendes Braze-Nutzerprofil folgt bereits dem LINE-Kanal {#existing-braze-user-profile-already-follows-line-channel}

1. Das Braze-Nutzerprofil wird mit einem `native_line_id`-Attribut aktualisiert. Der Standard-Abo-Status ist `unsubscribed`.
2. Das Abo-Synchronisierungstool wird ausgeführt, stellt fest, dass die Nutzer:innen dem LINE-Kanal folgen, und aktualisiert das Nutzerprofil mit dem Abo-Status `subscribed`.
3. Wenn sich der Abo-Status ändert (z. B. wenn die Nutzer:innen den Kanal blockieren, entfreunden oder erneut folgen), erhält Braze die Aktualisierung von LINE und aktualisiert das Nutzerprofil mit der `native_line_id` entsprechend.

#### Bestehendes Nutzerprofil hat den LINE-Kanal blockiert, entfreundet oder entfolgt {#existing-user-profile-has-blocked-unfriended-or-unfollowed-line-channel}

1. Das Braze-Nutzerprofil wird mit einem `native_line_id`-Attribut aktualisiert. Der Standard-Abo-Status ist `unsubscribed`.
2. Das Abo-Synchronisierungstool stellt nicht fest, dass die Nutzer:innen dem LINE-Kanal folgen, und der Abo-Status bleibt `unsubscribed`.
3. Wenn die Nutzer:innen später dem Kanal folgen, erhält Braze die Aktualisierung von LINE und aktualisiert das Nutzerprofil mit dem Abo-Status `subscribed`.

##### Nutzerprofilerstellung erfolgt nach LINE-Follow {#user-profile-creation-occurs-after-line-follow}

1. Der Kanal erhält einen neuen LINE-Follower.
2. Braze erstellt ein anonymes Nutzerprofil, bei dem das `native_line_id`-Attribut auf die LINE-ID des Followers gesetzt wird, und einen Nutzer-Alias `line_id`, der auf die LINE-ID des Followers gesetzt wird. Das Profil hat den Abo-Status `subscribed`.
3. Die Nutzer:innen werden durch [Nutzer-ID-Abstimmung](#user-id-reconciliation) als Inhaber:innen der LINE-ID identifiziert.
  - Das anonyme Nutzerprofil kann über den [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify)-Endpunkt identifiziert werden. Nachfolgende Aktualisierungen (über den [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)-Endpunkt, [CSV-Import]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv) oder [Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)) dieses Nutzerprofils können die Nutzer:innen über diese bekannte `external_id` ansprechen.

{% raw %}
```json
{
   "aliases_to_identify": [
       {
           "external_id": "known_external_id_from_your_application",
           "user_alias": {
               "alias_name": "U89f4a626548ccd48482f529a482f138b",
               "alias_label": "line_id"
           }
       }
   ]
}
```
{% endraw %}

  - Ein neues Nutzerprofil kann erstellt werden (über den [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)-Endpunkt, [CSV-Import]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv) oder [Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)), indem die `native_line_id` gesetzt wird. Dieses neue Profil erbt den Abo-Status des bestehenden anonymen Nutzerprofils. Beachten Sie, dass dies zu mehreren Profilen mit derselben `native_line_id` führt. Diese können jederzeit über den `/users/merge`-Endpunkt im unter [Schritt 5](#step-5-merge-profiles-optional) beschriebenen Prozess zusammengeführt werden.

##### Nutzerprofilerstellung erfolgt vor LINE-Follow {#user-profile-creation-occurs-before-line-follow}

1. Sie gewinnen neue Nutzer:innen und senden die Informationen an Braze. Ein neues Nutzerprofil wird erstellt (Profil 1).
2. Die Nutzer:innen folgen Ihrem LINE-Konto.
3. Braze erhält ein Follow-Ereignis und erstellt ein anonymes Nutzerprofil (Profil 2).
4. Die Nutzer:innen werden durch [Nutzer-ID-Abstimmung](#user-id-reconciliation) als Inhaber:innen der LINE-ID identifiziert.
5. Sie aktualisieren Profil 1, um das `native_line_id`-Attribut zu setzen. Dieses Profil erbt den Abo-Status von Profil 2.
  - Jetzt gibt es zwei Nutzerprofile mit derselben `native_line_id`. Diese können jederzeit über den `/users/merge`-Endpunkt im unter [Schritt 5](#step-5-merge-profiles-optional) beschriebenen Prozess zusammengeführt werden.

## Nutzer-ID-Abstimmung {#user-id-reconciliation}

LINE-IDs werden automatisch von Braze empfangen, wenn Nutzer:innen Ihrem Kanal folgen oder wenn Sie den einmaligen Workflow „Follower synchronisieren“ verwenden. LINE-IDs sind auch spezifisch für den Kanal, dem Nutzer:innen folgen, sodass es unwahrscheinlich ist, dass Nutzer:innen ihre LINE-IDs selbst angeben können.

Es gibt zwei Möglichkeiten, eine LINE-ID mit einem bestehenden Braze-Nutzerprofil zu kombinieren:

- [LINE Login](#line-login)
- [Nutzerkontoverknüpfung](#user-account-linking)

### LINE Login {#line-login}

Diese Methode nutzt Social-Media-Logins zur Abstimmung. Wenn sich Nutzer:innen in Ihrer App anmelden, erhalten sie die Option, [LINE Login](https://developers.line.biz/en/docs/line-login/overview/) zu verwenden, um ein Nutzerkonto zu erstellen oder sich anzumelden.

{% alert note %}
Um die korrekte LINE-ID für alle Nutzer:innen zu erhalten, richten Sie LINE Login unter demselben Provider wie Ihr in Braze integriertes offizielles LINE-Konto oder Ihren Kanal ein.
{% endalert %}

1. Gehen Sie zur LINE Developer Console und [beantragen Sie die Berechtigung, die E-Mail-Adressen von Nutzer:innen zu erhalten](https://developers.line.biz/en/docs/line-login/integrate-line-login/#applying-for-email-permission), die sich über LINE Login in Ihrer App anmelden.

2. Befolgen Sie die entsprechenden von LINE bereitgestellten Schritte zur Implementierung von LINE Login:<br><br>
  - [Anleitung für Web-Apps](https://developers.line.biz/en/docs/line-login/integrate-line-login/)
  - [Anleitung für native Apps](https://developers.line.biz/en/docs/line-login/secure-login-process/#using-openid-to-register-new-users)<br><br>Stellen Sie sicher, dass `email` in der [Scope-Einrichtung](https://developers.line.biz/en/docs/line-login/integrate-line-login/#scopes) für Verifizierungsanfragen enthalten ist.

{: start="3"}
3. Verwenden Sie den [Verify ID Token-Aufruf](https://developers.line.biz/en/reference/line-login/#verify-id-token), um die E-Mail-Adresse der Nutzer:innen zu erhalten.

4. Speichern Sie die LINE-ID der Nutzer:innen (`native_line_id`) im Nutzerprofil mit einer übereinstimmenden E-Mail in Ihrer Datenbank oder erstellen Sie ein neues Nutzerprofil mit der E-Mail und LINE-ID der Nutzer:innen.

5. Senden Sie die neuen oder aktualisierten Nutzerinformationen an Braze über den [`/user/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track), [CSV-Import]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv) oder [Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion).

#### Abläufe {#workflows}

##### Bestehende:r Follower:in verwendet LINE Login {#existing-follower-uses-line-login}

**Szenario:** Anonyme Nutzer:innen wurden während der initialen Abo-Synchronisierung oder nach der Integration durch ein „Follow“-Ereignis erstellt.

1. Die Nutzer:innen melden sich über LINE Login in Ihrer App an.
2. LINE stellt Ihnen die E-Mail-Adresse der Nutzer:innen bereit.
3. Sie senden Braze die aktualisierten Nutzer:innen (das bestehende Nutzerprofil mit dieser E-Mail, um die LINE-ID hinzuzufügen) oder Sie aktualisieren die anonymen Nutzer:innen mit der E-Mail.

##### Neue:r Follower:in verwendet LINE Login {#new-follower-uses-line-login}

**Szenario:** In Braze existiert kein Nutzerprofil mit der LINE-ID der Nutzer:innen.

1. Die Nutzer:innen melden sich über LINE Login in Ihrer App an.
2. LINE stellt Ihnen die E-Mail-Adresse der Nutzer:innen bereit.
3. Sie können entweder:
  - Ein bestehendes Nutzerprofil mit dieser E-Mail aktualisieren, um auch die LINE-ID der Nutzer:innen hinzuzufügen.
  - Ein neues Nutzerprofil mit der E-Mail und LINE-ID erstellen.
4. Wenn die Nutzer:innen Ihrem offiziellen LINE-Konto folgen, erhält Braze ein Follow-Ereignis und aktualisiert den Abo-Status der Nutzer:innen auf `subscribed`.

### Nutzerkontoverknüpfung {#user-account-linking}

Diese Methode ermöglicht es Nutzer:innen, ihr LINE-Konto mit dem Nutzerkonto Ihrer App zu verknüpfen. Sie können dann Liquid in Braze verwenden, wie z. B. {% raw %}`{{line_id}}`{% endraw %}, um eine personalisierte URL für die Nutzer:innen zu erstellen, die deren LINE-ID an Ihre Website oder App zurückgibt, wo sie mit bekannten Nutzer:innen verknüpft werden kann.

1. Erstellen Sie einen aktionsbasierten Canvas, der auf einer Abo-Statusänderung basiert und ausgelöst wird, wenn Nutzer:innen Ihren LINE-Kanal abonnieren.<br>![Canvas, das ausgelöst wird, wenn Nutzer:innen den LINE-Kanal abonnieren.]({% image_buster /assets/img/line/account_link_1.png %})
2. Erstellen Sie eine Nachricht, die Nutzer:innen dazu motiviert, sich auf Ihrer Website oder App anzumelden, wobei die LINE-ID der Nutzer:innen als Abfrageparameter (über Liquid) übergeben wird, wie z. B.:

```
Thanks for following Flash n' Thread on LINE! For personalized offers and 20% off your next purchase, sign-in to your account: https://flashandthread.com/sign_in?line_user_id={{line_id}}
```

{: start="3"}
3. Erstellen Sie eine Folgenachricht, die den Gutscheincode liefert.
4. (Optional) Erstellen Sie eine aktionsbasierte Campaign oder ein Canvas, das ausgelöst wird, wenn die LINE-Nutzer:innen identifiziert werden, um ihnen den Gutscheincode zu senden. <br>![Aktionsbasierte Campaign, die ausgelöst wird, wenn die LINE-Nutzer:innen identifiziert werden.]({% image_buster /assets/img/line/account_link_2.png %})

#### So funktioniert es {#how-it-works}

Nachdem sich die Nutzer:innen angemeldet haben, wird auf Ihrer Website oder App eine Änderung vorgenommen, sodass die Nutzer-ID an Braze zurückgesendet wird, um sie mit der LINE-ID zu verknüpfen, die als Teil der URL übergeben wurde, mit Beispielcode wie:

```javascript
const currentUrl = new URL(window.location.href)
const queryParams = new URLSearchParams(currentUrl.search);
const lineUserId = queryParams.get("line_user_id")

if (user && isLoggedIn && lineUserId) {
  post(
   "https://rest.iad-03.braze.com	/users/identify",
   {
     "aliases_to_identify": [
       {
   "external_id": user.getUserId(),
   "user_alias": {
     "alias_name": lineUserId,
     "alias_label": "line_id"
   }
 }
      ]
    }
  )
  braze.logCustomEvent("identified_line_user_for_promotion");
}
```

#### Abläufe bei der Nutzerkontoverknüpfung

##### Bestehende Nutzer:innen folgen Ihrem LINE-Kanal {#existing-user-follows-your-line-channel}

**Szenario:** Bestehende Nutzer:innen in Braze folgen Ihrem Kanal auf LINE.

1. LINE sendet Braze ein Follow-Ereignis.
2. Braze erstellt ein anonymes Nutzerprofil mit der LINE-ID, dem Nutzer-Alias `line_id` und dem LINE-Abo-Gruppenstatus `subscribed`.
3. Die Nutzer:innen erhalten eine LINE-Nachricht mit einem Link zu Ihrer Website und App und melden sich an. Ihr Nutzerprofil ist jetzt bekannt.
4. Das erstellte anonyme Nutzerprofil wird identifiziert und über den [/users/identify-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) mit dem bekannten Nutzerprofil der Nutzer:innen zusammengeführt. Das bekannte Nutzerprofil enthält jetzt die LINE-ID und hat den Abo-Status `subscribed`.
5. (Optional) Die Nutzer:innen erhalten eine LINE-Nachricht mit dem Gutscheincode und Braze protokolliert den Versand im Braze-Nutzerprofil.

## LINE-Testnutzer:innen in Braze erstellen {#creating-line-test-users-in-braze}

Sie können Ihren LINE-Kanal testen, bevor Sie die [Nutzer-ID-Abstimmung](#user-id-reconciliation) einrichten, indem Sie ein „Wer bin ich“-Canvas oder eine Campaign erstellen.

1. Richten Sie ein Canvas ein, das die Braze-Nutzer-ID bei einem bestimmten Triggerwort zurückgibt. <br><br>Beispiel-Trigger <br><br>![Trigger zum Senden der Campaign an Nutzer:innen, die eine eingehende LINE-Nachricht an eine bestimmte Abo-Gruppe gesendet haben.]({% image_buster /assets/img/line/trigger.png %}){: style="max-width:80%;"}<br><br>Beispielnachricht<br><br>![LINE-Nachricht mit der Braze-Nutzer-ID.]({% image_buster /assets/img/line/message.png %}){: style="max-width:40%;"}<br><br>

2. In Braze können Sie die Braze-ID verwenden, um bestimmte Nutzer:innen zu suchen und bei Bedarf zu ändern.

{% alert important %}
Stellen Sie sicher, dass das Canvas keine globale Kontrollgruppe oder Kontrollgruppen hat, die den Versand verhindern.
{% endalert %}