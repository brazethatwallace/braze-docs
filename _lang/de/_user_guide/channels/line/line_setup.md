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
- [LINE Messaging-API-Kanal](https://developers.line.biz/en/docs/line-developers-console/overview/#channel)

Der Versand von LINE-Nachrichten über Braze wird von den Message- oder Action-Credits Ihres Kontos abgezogen.

{% alert note %}
**`native_line_id` festlegen**: Sie können `native_line_id` festlegen, indem Sie Nutzer:innen-Aktualisierungen an Braze senden (zum Beispiel mit dem [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)-Endpunkt, per [CSV-Import]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv) oder über [Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)). Wenn das SDK Ihrer App kein dediziertes Feld für `native_line_id` hat, senden Sie es in serverseitigen Nutzer:innen-Aktualisierungen mit einer dieser Methoden.
{% endalert %}

## Arten von LINE-Konten {#types-of-line-accounts}

| Kontotyp | Beschreibung |
| --- | --- |
| Nicht verifiziertes Konto | Ein nicht überprüftes Konto, das von jeder Person (Einzelperson oder Unternehmen) eingerichtet werden kann. Dieses Konto wird mit einem grauen Badge dargestellt und erscheint nicht in den Suchergebnissen innerhalb der LINE-App. |
| Verifiziertes Konto | Ein Konto, das die LINE-Yahoo-Prüfung bestanden hat. Dieses Konto wird mit einem blauen Badge dargestellt und erscheint in den Suchergebnissen innerhalb der LINE-App.<br><br>Dieses Konto ist nur für Konten verfügbar, die in Japan, Taiwan, Thailand und Indonesien ansässig sind. |
| Premium-Konto | Ein Konto, das die LINE-Yahoo-Prüfung bestanden hat. Dieses Konto wird mit einem grünen Badge dargestellt und erscheint in den Suchergebnissen innerhalb der LINE-App. Dieser Kontotyp wird während der Prüfung automatisch nach Ermessen von LINE vergeben. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Arten von LINE-Konten" }

### Erforderlicher Kontotyp {#required-account-type}

Um Follower in Braze zu synchronisieren, muss Ihr LINE-Konto verifiziert oder ein Premium-Konto sein. Wenn Sie ein Konto erstellen, ist der Standardstatus „nicht verifiziert“. Sie müssen eine Kontoverifizierung beantragen.

### Beantragung eines verifizierten LINE-Kontos {#applying-for-a-verified-line-account}

{% alert important %}
Verifizierte Konten sind nur für Konten verfügbar, die in Japan, Taiwan, Thailand und Indonesien ansässig sind.
{% endalert %}

1. Wählen Sie auf der LINE-Seite **Official Account** die Option **Settings** aus.
2. Wählen Sie unter **Information Disclosure Verification Status** die Option **Request Account Verification** aus.
3. Geben Sie die erforderlichen Informationen ein.
4. Warten Sie auf eine Benachrichtigung mit den Prüfungsergebnissen.

## Integration von LINE {#integrating-line}

Um konsistente Nutzer:innen-Aktualisierungen einzurichten, die LINE-IDs vorhandener Nutzer:innen zu übernehmen und sie alle mit den Abo-Status von LINE zu synchronisieren:

1. [Vorhandene bekannte Nutzer:innen importieren oder aktualisieren](#step-1-import-or-update-existing-line-users)
2. [Den LINE-Kanal integrieren](#step-2-integrate-line-channel)
3. [Nutzer-IDs abgleichen](#step-3-reconcile-user-ids)
4. [Methoden zur Nutzer:innen-Aktualisierung ändern](#step-4-change-your-user-update-methods)
5. [(Optional) Nutzerprofile zusammenführen](#step-5-merge-profiles-optional)

{% alert note %}
Sie können nur ein LINE-Konto in einem einzelnen Workspace verwenden. Wenn Sie mehrere LINE-Konten haben, empfehlen wir, jedes in einem anderen Workspace zu verwenden.
{% endalert %}

## Schritt 1: Bestehende LINE-Nutzer:innen importieren oder aktualisieren {#step-1-import-or-update-existing-line-users}

Dieser Schritt ist erforderlich, wenn Sie bereits identifizierte LINE-Nutzer:innen haben, da Braze später automatisch deren Abo-Status abruft und das richtige Kundenprofil aktualisiert. Wenn Sie Nutzer:innen noch nicht mit ihrer LINE-ID abgeglichen haben, überspringen Sie diesen Schritt.

Sie können Nutzer:innen mit jeder von Braze unterstützten Methode importieren oder aktualisieren, einschließlich des [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)-Endpunkts, des [CSV-Imports]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv) oder der [Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion).

Unabhängig von der verwendeten Methode aktualisieren Sie die `native_line_id`, um die LINE-ID der Nutzer:innen anzugeben. Weitere Informationen zur `native_line_id` finden Sie unter [Nutzer-Setup](#user-setup).

{% alert note %}
Geben Sie nicht den Abo-Gruppenstatus an – er wird ignoriert. LINE ist die maßgebliche Quelle für den Abo-Status von Nutzer:innen, der über das Abo-Synchronisierungstool oder Ereignisaktualisierungen mit Braze synchronisiert wird.
{% endalert %}

## Schritt 2: LINE-Kanal integrieren {#step-2-integrate-line-channel}

Nachdem der Integrationsprozess abgeschlossen ist, ruft Braze automatisch die LINE-Follower dieses Kanals in Braze ab. Für alle LINE-IDs, die bereits mit einem Braze-Kundenprofil verknüpft sind, wird jedes Profil mit dem Status „subscribed“ aktualisiert, und alle verbleibenden LINE-IDs erzeugen anonyme Nutzer:innen. Darüber hinaus werden für neue Follower Ihres LINE-Kanals nicht identifizierte Nutzerprofile erstellt, wenn sie dem Kanal folgen.

### Schritt 2.1: Webhook-Einstellungen bearbeiten {#step-21-edit-webhook-settings}

1. Gehen Sie in LINE zum Tab **Messaging API** und bearbeiten Sie Ihre **Webhook settings**:
   - Setzen Sie die **Webhook URL** auf `https://anna.braze.com/line/events`.
      - Braze ändert diese URL bei der Integration automatisch basierend auf Ihrem Dashboard-Cluster in eine andere URL.
   - Aktivieren Sie **Use webhook** und **Webhook redelivery**. <br><br> ![Seite mit Webhook-Einstellungen zum Überprüfen oder Bearbeiten der Webhook-URL sowie zum Aktivieren oder Deaktivieren von „Use webhook“, „Webhook redelivery“ und „Error statistics aggregation“.]({% image_buster /assets/img/line/webhook_settings.png %}){: style="max-width:70%;"}
2. Notieren Sie die folgenden Informationen im Tab **Providers**:

| Informationstyp | Ort |
| --- | --- |
| Provider-ID | Wählen Sie Ihren Provider aus und gehen Sie dann zu **Settings** > **Basic information** |
| Channel-ID | Wählen Sie Ihren Provider aus und gehen Sie dann zu **Channels** > Ihr Kanal > **Basic settings** |
| Channel-Secret | Wählen Sie Ihren Provider aus und gehen Sie dann zu **Channels** > Ihr Kanal > **Basic settings**. |
| Channel-Access-Token | Wählen Sie Ihren Provider aus und gehen Sie dann zu **Channels** > Ihr Kanal > **Messaging API**. Wenn kein Channel-Access-Token vorhanden ist, wählen Sie **Issue**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 2.1: Webhook-Einstellungen bearbeiten" }

{% alert note %}
Sie können das Channel-Secret und den Channel-Access-Token für einen bereits integrierten LINE-Kanal aktualisieren oder rotieren, indem Sie zu **Partnerintegrationen** > **Technologie-Partner** > **LINE** gehen und Ihre Integration auswählen.
{% endalert %}

{: start="3"}
3. Gehen Sie zu Ihrer Seite **Settings** > **Response settings** und führen Sie Folgendes aus:
   - Deaktivieren Sie **Greeting message**. Dies kann in Braze durch Triggern bei Follow gehandhabt werden.
   - Deaktivieren Sie **Auto-response messages**. Alle getriggerten Nachrichten sollten über Braze erfolgen. Dies hindert Sie nicht daran, direkt von der LINE-Konsole aus zu senden.
   - Aktivieren Sie **Webhooks**.

![Seite mit Antworteinstellungen mit Umschaltern dafür, wie Ihr Konto Chats verarbeitet.]({% image_buster /assets/img/line/response_settings.png %}){: style="max-width:80%;"}

### Schritt 2.2: LINE-Abo-Gruppen in Braze generieren {#step-22-generate-line-subscription-groups-in-braze}

Braze erstellt eine [Abo-Gruppe]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups#line-subscription-groups) für jeden LINE-Kanal, den Sie integrieren. Informationen zur Funktionsweise von LINE-Abo-Gruppen finden Sie unter [LINE-Abo-Gruppen]({{site.baseurl}}/user_guide/channels/line/message_users/subscription_groups).

{% multi_lang_include alerts/note_alerts.md alert='subscription group limit' %}

1. Gehen Sie zur Braze-Technologie-Partnerseite für LINE und geben Sie die Informationen ein, die Sie sich aus dem Tab **Providers** Ihres LINE-Kontos notiert haben:
   - Provider-ID
   - Channel-ID
   - Channel-Secret
   - Channel-Access-Token

Wenn Sie IP-Whitelisting in Ihrem LINE-Konto hinzufügen möchten, fügen Sie alle IP-Adressen, die für Ihren Cluster unter [IP-Zulassungsliste]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#ip-allowlisting) aufgeführt sind, zu Ihrer Zulassungsliste hinzu.

{% alert important %}
Stellen Sie während der Integration sicher, dass Ihr Channel-Secret korrekt ist. Wenn es nicht korrekt ist, kann es zu Inkonsistenzen beim Abo-Status kommen.
{% endalert %}

![Seite zur LINE-Messaging-Integration mit dem Abschnitt zur LINE-Integration.]({% image_buster /assets/img/line/integration.png %}){: style="max-width:80%;"}

{: start="2"}
2. Nach der Verbindung generiert Braze automatisch eine Braze-Abo-Gruppe für jede LINE-Integration, die erfolgreich zu Ihrem Workspace hinzugefügt wurde. <br><br> Alle Änderungen an Ihrer Follower-Liste (z. B. neue Follower oder Entfolger) werden automatisch in Braze übertragen.

![Abschnitt „LINE-Abo-Gruppen“ mit einer Abo-Gruppe für den Kanal „LINE“.]({% image_buster /assets/img/line/line_subscription_groups.png %}){: style="max-width:80%;"}

## Schritt 3: Nutzer-IDs abgleichen {#step-3-reconcile-user-ids}

Kombinieren Sie die LINE-IDs Ihrer Nutzer:innen mit deren vorhandenen Braze-Nutzerprofilen, indem Sie die Schritte unter [Nutzer-ID-Abgleich](#user-id-reconciliation) befolgen.

## Schritt 4: Ihre Methoden zur Nutzeraktualisierung ändern {#step-4-change-your-user-update-methods}

Vorausgesetzt, Sie verfügen bereits über eine Methode, um Nutzeraktualisierungen an Braze zu übermitteln, müssen Sie diese aktualisieren, sodass sie das neue Feld `native_line_id` enthält, damit nachfolgende Nutzeraktualisierungen, die an Braze gesendet werden, dieses Feld einschließen.

In Braze können nicht identifizierte Nutzerprofile mit einer `native_line_id` vorhanden sein, die im Rahmen des Synchronisationsprozesses des Abo-Gruppenstatus erstellt wurden oder wenn ein:e neue:r Follower:in Ihrem Kanal gefolgt ist.

Wenn eine:r LINE-Nutzer:in in Ihrer Anwendung durch [Nutzer-ID-Abgleich](#user-id-reconciliation) oder auf anderem Wege identifiziert wird, können Sie ein potenziell nicht identifiziertes Kundenprofil in Braze über den Endpunkt [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) ansprechen. Jedes nicht identifizierte Kundenprofil mit einer `native_line_id` verfügt auch über einen Nutzer-Alias `line_id`, der verwendet werden kann, um das Kundenprofil zur Identifikation anzusprechen.

Hier ist ein Beispiel-Payload für `/users/identify`, der ein nicht identifiziertes Kundenprofil über den Nutzer-Alias `line_id` anspricht:

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

Wenn kein bestehendes Kundenprofil für die von Ihnen angegebene `external_id` existiert, wird diese dem nicht identifizierten Kundenprofil hinzugefügt und es dadurch identifiziert. Wenn bereits ein Kundenprofil für die `external_id` existiert, werden alle Attribute, die ausschließlich auf dem nicht identifizierten Kundenprofil vorhanden sind, in das bekannte Kundenprofil kopiert, einschließlich `native_line_id` und des Abo-Status der Nutzer:innen.

Sie können LINE-Nutzer:innen, die in Ihrer Anwendung bekannt sind, über den Endpunkt [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) aktualisieren, indem Sie deren externe Bezeichner und `native_line_id` übergeben. Wenn bereits ein nicht identifiziertes Kundenprofil für eine:n Nutzer:in existiert und dieselbe `native_line_id` über `/users/track` einem anderen Kundenprofil hinzugefügt wird, erbt dieses alle Abo-Status des nicht identifizierten Nutzerprofils. Es entstehen jedoch doppelte Nutzerprofile mit derselben `native_line_id`. Alle nachfolgenden Abo-Aktualisierungen durch Ereignis-Updates werden alle Profile entsprechend aktualisieren.

{% alert note %}
LINE-Abo-Status werden anhand der `native_line_id` verfolgt, nicht anhand der `external_id`. Wenn beispielsweise das Kundenprofil von Nutzer:in B mit derselben `native_line_id` wie Nutzer:in A erstellt wird, aber nicht mit derselben `external_id`, erbt Nutzer:in B den LINE-Abo-Status von Nutzer:in A.
{% endalert %}

Hier ist ein Beispiel-Payload für `/users/track`, der ein Kundenprofil anhand der externen Nutzer-ID aktualisiert, um eine `native_line_id` hinzuzufügen:

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

Wie bereits in diesem Abschnitt beschrieben, besteht die Möglichkeit, dass mehrere Nutzerprofile mit derselben `native_line_id` existieren. Wenn Ihre Aktualisierungsmethoden doppelte Nutzerprofile erzeugen, können Sie nicht identifizierte Nutzerprofile mit identifizierten Nutzerprofilen über den Endpunkt `/user/merge` zusammenführen.

Hier ist ein Beispiel-Payload für `/users/merge`, der ein nicht identifiziertes Kundenprofil anhand des Nutzer-Alias `line_id` anspricht:

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

## Nutzer:innen-Einrichtung {#user-setup}

LINE ist die maßgebliche Quelle für den Abo-Status von Nutzer:innen. Selbst wenn Sie die LINE-ID einer Nutzerin oder eines Nutzers haben (`native_line_id`): Wenn diese Person dem LINE-Kanal, von dem Sie senden, nicht folgt, stellt LINE keine Nachrichten an sie zu.

Um dies zu verwalten, bietet Braze Tools und Logik, die eine gut integrierte Nutzerbasis unterstützen – einschließlich Abo-Synchronisierung und Ereignis-Updates für LINE-Follows und -Unfollows.

### Abo-Synchronisierung und Ereignis-Logik {#subscription-syncing-and-event-logic}

Informationen dazu, wie das Tool zur Abo-Synchronisierung sowie Ereignis-Updates für Follows und Unfollows den LINE-Abo-Status mit Braze synchron halten, finden Sie unter [Abo-Status]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_status#line).

## Einen LINE-Kanal in einem anderen Workspace erneut integrieren {#re-integrate-a-line-channel-in-another-workspace}

So verwenden Sie einen LINE-Kanal in einem anderen Braze-Workspace:

1. Archivieren Sie im ursprünglichen Workspace die Abo-Gruppe für diesen Kanal.
2. Integrieren Sie im Ziel-Workspace den Kanal mithilfe von [Schritt 2: LINE-Kanal integrieren](#step-2-integrate-line-channel).

Stellen Sie sicher, dass Sie in beiden Workspaces über die Berechtigung [Abo-Gruppen verwalten]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions) verfügen. Ohne Berechtigungen in beiden Workspaces schlägt die Integration mit einer Fehlermeldung fehl, die besagt, dass der Kanal bereits verbunden ist.

Informationen dazu, wie sich die Archivierung auf Abo-Gruppen auswirkt, finden Sie unter [LINE-Abo-Gruppen]({{site.baseurl}}/user_guide/channels/line/message_users/subscription_groups#archive-behavior).

## Anwendungsfälle {#use-cases}

Dies sind Anwendungsfälle, wie Nutzer:innen aktualisiert werden können, nachdem Sie die Einrichtungsschritte durchgeführt haben.

### Bestehendes Braze-Kundenprofil folgt bereits einem LINE-Kanal {#existing-braze-user-profile-already-follows-line-channel}

1. Das Braze-Kundenprofil wird mit einem `native_line_id`-Attribut aktualisiert. Der Standard-Abo-Status ist `unsubscribed`.
2. Das Abo-Synchronisierungstool wird ausgeführt, stellt fest, dass die bzw. der Nutzer:in dem LINE-Kanal folgt, und aktualisiert dann das Kundenprofil mit dem Abo-Status `subscribed`.
3. Wenn sich der Abo-Status ändert (z. B. wenn die bzw. der Nutzer:in den Kanal blockiert, die Freundschaft aufhebt oder dem Kanal erneut folgt), erhält Braze das Update von LINE und aktualisiert das Kundenprofil mit der `native_line_id` entsprechend.

### Bestehendes Kundenprofil hat den LINE-Kanal blockiert, die Freundschaft aufgehoben oder entfolgt {#existing-user-profile-has-blocked-unfriended-or-unfollowed-line-channel}

1. Das Braze-Kundenprofil wird mit einem `native_line_id`-Attribut aktualisiert. Der Standard-Abo-Status ist `unsubscribed`.
2. Das Abo-Synchronisierungstool stellt nicht fest, dass die bzw. der Nutzer:in dem LINE-Kanal folgt, und der Abo-Status bleibt `unsubscribed`.
3. Wenn die bzw. der Nutzer:in dem Kanal später folgt, erhält Braze das Update von LINE und aktualisiert das Kundenprofil mit dem Abo-Status `subscribed`.

### Kundenprofil wird nach dem LINE-Follow erstellt {#user-profile-creation-occurs-after-line-follow}

1. Der Kanal bekommt eine:n neue:n LINE-Follower:in.
2. Braze erstellt ein anonymes Kundenprofil, bei dem das `native_line_id`-Attribut auf die LINE-ID der bzw. des Follower:in und ein Nutzer-Alias `line_id` auf die LINE-ID der bzw. des Follower:in gesetzt wird. Das Profil hat den Abo-Status `subscribed`.
3. Die bzw. der Nutzer:in wird über die [Nutzer-Abgleichung](#user-id-reconciliation) als Inhaber:in der LINE-ID identifiziert.
  - Das anonyme Kundenprofil kann mithilfe des [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify)-Endpunkts identifiziert werden. Nachfolgende Aktualisierungen (über den [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)-Endpunkt, [CSV-Import]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv) oder [Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)) an diesem Kundenprofil können die bzw. den Nutzer:in über die bekannte `external_id` ansprechen.

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

  - Ein neues Kundenprofil kann erstellt werden (über den [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)-Endpunkt, [CSV-Import]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv) oder [Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)), indem die `native_line_id` gesetzt wird. Dieses neue Profil übernimmt den Abo-Status des bestehenden anonymen Nutzerprofils. Beachten Sie, dass dadurch mehrere Profile dieselbe `native_line_id` teilen. Diese können jederzeit über den `/users/merge`-Endpunkt zusammengeführt werden, wie in [Schritt 5](#step-5-merge-profiles-optional) beschrieben.

### Kundenprofil wird vor dem LINE-Follow erstellt {#user-profile-creation-occurs-before-line-follow}

1. Sie gewinnen eine:n neue:n Nutzer:in und senden die Informationen an Braze. Ein neues Kundenprofil wird erstellt (Profil 1).
2. Die bzw. der Nutzer:in folgt Ihrem LINE-Konto.
3. Braze erhält ein Follow-Ereignis und erstellt ein anonymes Kundenprofil (Profil 2).
4. Die bzw. der Nutzer:in wird über die [Nutzer-Abgleichung](#user-id-reconciliation) als Inhaber:in der LINE-ID identifiziert.
5. Sie aktualisieren Profil 1, um das `native_line_id`-Attribut zu setzen. Dieses Profil übernimmt den Abo-Status von Profil 2.
  - Jetzt gibt es zwei Nutzerprofile mit derselben `native_line_id`. Diese können jederzeit über den `/users/merge`-Endpunkt zusammengeführt werden, wie in [Schritt 5](#step-5-merge-profiles-optional) beschrieben.

## Abgleich der Nutzer-ID {#user-id-reconciliation}

LINE-IDs werden von Braze automatisch empfangen, wenn Nutzer:innen Ihrem Kanal folgen oder wenn Sie den einmaligen Workflow „Follower synchronisieren“ verwenden. LINE-IDs sind außerdem spezifisch für den Kanal, dem Nutzer:innen folgen, sodass es unwahrscheinlich ist, dass Nutzer:innen ihre LINE-IDs selbst bereitstellen können.

Es gibt zwei Möglichkeiten, eine LINE-ID mit einem bestehenden Braze-Kundenprofil zu verknüpfen:

- [LINE Login](#line-login)
- [Nutzerkontoverknüpfung](#user-account-linking)

### LINE Login {#line-login}

Diese Methode nutzt Social-Media-Anmeldungen für den Abgleich. Wenn sich Nutzer:innen in Ihrer App anmelden, erhalten sie die Option, [LINE Login](https://developers.line.biz/en/docs/line-login/overview/) zu verwenden, um ein Nutzerkonto zu erstellen oder sich einzuloggen.

{% alert note %}
Um die korrekte LINE-ID für alle Nutzer:innen zu erhalten, richten Sie LINE Login unter demselben Anbieter ein wie Ihr mit Braze integriertes offizielles LINE-Konto oder Ihren LINE-Kanal.
{% endalert %}

1. Gehen Sie zur LINE Developer Console und [beantragen Sie die Berechtigung, E-Mail-Adressen von Nutzer:innen abzurufen](https://developers.line.biz/en/docs/line-login/integrate-line-login/#applying-for-email-permission), die sich über LINE Login in Ihrer App anmelden.

2. Befolgen Sie die entsprechenden Schritte von LINE, um LINE Login zu implementieren:<br><br>
  - [Anleitung für Web-Apps](https://developers.line.biz/en/docs/line-login/integrate-line-login/)
  - [Anleitung für native Apps](https://developers.line.biz/en/docs/line-login/secure-login-process/#using-openid-to-register-new-users)<br><br>Stellen Sie sicher, dass `email` in der [Scope-Konfiguration](https://developers.line.biz/en/docs/line-login/integrate-line-login/#scopes) für Verifizierungsanfragen enthalten ist.

{: start="3"}
3. Verwenden Sie den [Verify ID Token call](https://developers.line.biz/en/reference/line-login/#verify-id-token), um die E-Mail-Adresse der Nutzer:innen abzurufen.

4. Speichern Sie die LINE-ID (`native_line_id`) der Nutzer:innen im Kundenprofil mit einer übereinstimmenden E-Mail-Adresse in Ihrer Datenbank oder erstellen Sie ein neues Kundenprofil mit der E-Mail-Adresse und LINE-ID.

5. Senden Sie die neuen oder aktualisierten Nutzerinformationen über den [`/user/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track), [CSV-Import]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv) oder [Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion) an Braze.

#### Workflows {#workflows}

##### Bestehende:r Follower:in nutzt LINE Login {#existing-follower-uses-line-login}

**Szenario:** Eine anonyme Nutzer:in wurde während der initialen Abonnent:innen-Synchronisierung oder nach der Integration durch ein „Follow“-Ereignis erstellt.

1. Die Nutzer:in meldet sich über LINE Login in Ihrer App an.
2. LINE stellt Ihnen die E-Mail-Adresse der Nutzer:in bereit.
3. Sie senden Braze die aktualisierte Nutzer:in (das bestehende Kundenprofil mit dieser E-Mail-Adresse, um die LINE-ID hinzuzufügen) oder Sie aktualisieren die anonyme Nutzer:in mit der E-Mail-Adresse.

##### Neue:r Follower:in nutzt LINE Login {#new-follower-uses-line-login}

**Szenario:** Es existiert kein Kundenprofil in Braze mit der LINE-ID der Nutzer:in.

1. Die Nutzer:in meldet sich über LINE Login in Ihrer App an.
2. LINE stellt Ihnen die E-Mail-Adresse der Nutzer:in bereit.
3. Sie können entweder:
  - Ein bestehendes Kundenprofil mit dieser E-Mail-Adresse aktualisieren, um auch die LINE-ID der Nutzer:in hinzuzufügen.
  - Ein neues Kundenprofil mit der E-Mail-Adresse und LINE-ID erstellen.
4. Wenn die Nutzer:in Ihrem offiziellen LINE-Konto folgt, empfängt Braze ein Follow-Ereignis und aktualisiert den Abo-Status der Nutzer:in auf `subscribed`.

### Nutzerkontoverknüpfung {#user-account-linking}

Diese Methode ermöglicht es Nutzer:innen, ihr LINE-Konto mit dem Nutzerkonto Ihrer App zu verknüpfen. Sie können dann Liquid in Braze verwenden, z. B. {% raw %}`{{line_id}}`{% endraw %}, um eine personalisierte URL für die Nutzer:in zu erstellen, die die LINE-ID der Nutzer:in an Ihre Website oder App zurückgibt, wo sie einem bekannten Kundenprofil zugeordnet werden kann.

1. Erstellen Sie ein aktionsbasiertes Canvas, das auf einer Änderung des Abo-Status basiert und ausgelöst wird, wenn Nutzer:innen Ihren LINE-Kanal abonnieren.<br>![Canvas, das ausgelöst wird, wenn Nutzer:innen den LINE-Kanal abonnieren.]({% image_buster /assets/img/line/account_link_1.png %})
2. Erstellen Sie eine Nachricht, die Nutzer:innen dazu motiviert, sich auf Ihrer Website oder in Ihrer App anzumelden, wobei die LINE-ID der Nutzer:in als Query-Parameter (über Liquid) übergeben wird, z. B.:

```
Thanks for following Flash n' Thread on LINE! For personalized offers and 20% off your next purchase, sign-in to your account: https://flashandthread.com/sign_in?line_user_id={{line_id}}
```

{: start="3"}
3. Erstellen Sie eine Folgenachricht, die den Gutscheincode liefert.
4. (Optional) Erstellen Sie eine aktionsbasierte Campaign oder ein Canvas, das ausgelöst wird, wenn die LINE-Nutzer:in identifiziert wurde, um der Nutzer:in den Gutscheincode zu senden. <br>![Aktionsbasierte Campaign, die ausgelöst wird, wenn die LINE-Nutzer:in identifiziert wurde.]({% image_buster /assets/img/line/account_link_2.png %})

#### So funktioniert es {#how-it-works}

Nachdem sich die Nutzer:in angemeldet hat, wird auf Ihrer Website oder in Ihrer App eine Änderung vorgenommen, sodass die Nutzer-ID an Braze zurückgesendet wird, um sie mit der LINE-ID zu verknüpfen, die als Teil der URL übergeben wurde, mit beispielhaftem Code wie:

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

#### Workflows

##### Bestehende Nutzer:in folgt Ihrem LINE-Kanal {#existing-user-follows-your-line-channel}

**Szenario:** Eine bestehende Nutzer:in in Braze folgt Ihrem Kanal auf LINE.

1. LINE sendet Braze ein Follow-Ereignis.
2. Braze erstellt ein anonymes Kundenprofil mit der LINE-ID, dem Nutzer-Alias `line_id` und dem LINE-Abo-Gruppenstatus `subscribed`.
3. Die Nutzer:in erhält eine LINE-Nachricht mit einem Link zu Ihrer Website und App und meldet sich an. Ihr Kundenprofil ist nun bekannt.
4. Das zuvor erstellte anonyme Kundenprofil wird identifiziert und über den [/users/identify-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) mit dem bekannten Kundenprofil zusammengeführt. Das bekannte Kundenprofil enthält nun die LINE-ID und hat den Abo-Status `subscribed`.
5. (Optional) Die Nutzer:in erhält eine LINE-Nachricht mit dem Gutscheincode und Braze protokolliert den Versand im Braze-Kundenprofil.

## LINE-Testnutzer:innen in Braze erstellen {#creating-line-test-users-in-braze}

Sie können Ihren LINE-Kanal testen, bevor Sie die [Nutzer-Abgleichung](#user-id-reconciliation) einrichten, indem Sie ein „Wer bin ich“-Canvas oder eine Campaign erstellen.

1. Richten Sie ein Canvas ein, das bei einem bestimmten Trigger-Wort die Braze-Nutzer-ID zurückgibt. <br><br>Beispiel-Trigger <br><br>![Trigger, um die Campaign an Nutzer:innen zu senden, die eine eingehende LINE-Nachricht an eine bestimmte Abo-Gruppe gesendet haben.]({% image_buster /assets/img/line/trigger.png %}){: style="max-width:80%;"}<br><br>Beispiel-Nachricht<br><br>![LINE-Nachricht mit der Braze-Nutzer-ID.]({% image_buster /assets/img/line/message.png %}){: style="max-width:40%;"}<br><br>

2. In Braze können Sie die Braze-ID verwenden, um bestimmte Nutzer:innen zu suchen und nach Bedarf zu bearbeiten.

{% alert important %}
Stellen Sie sicher, dass das Canvas keine globalen Kontrollgruppen oder Kontrollgruppen hat, die den Versand verhindern.
{% endalert %}