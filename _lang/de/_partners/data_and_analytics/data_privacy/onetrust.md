---
nav_title: OneTrust
article_title: OneTrust
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und OneTrust, einem Anbieter von Datenschutz- und Sicherheitssoftware, die es Ihnen erlaubt, mit dem OneTrust Workflow Builder Sicherheits-Workflows für Ihr Produkt zu erstellen."
alias: /partners/onetrust/
page_type: partner
search_tag: Partner

---

# OneTrust

> [OneTrust](https://www.onetrust.com/) ist ein Anbieter von Datenschutz- und Sicherheitssoftware, der Ihnen die Transparenz bietet, die Sie benötigen, um Ihre Vertrauenslandschaft besser zu verstehen, leistungsstarke Insights zu nutzen und durch Automatisierung einen Vorsprung vor der Konkurrenz zu erzielen.

_Diese Integration wird von OneTrust gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Braze und OneTrust erlaubt es Ihnen, den OneTrust Workflow Builder zu verwenden, um Sicherheits-Workflows für Ihr Produkt zu erstellen.
## Voraussetzungen {#prerequisites}

| Anforderungen | Beschreibung |
|---|---|
| OneTrust-Konto | Ein [OneTrust-Konto](https://www.onetrust.com/), um von dieser Partnerschaft zu profitieren. |
| Braze-API-Schlüssel | Ein Braze-Representational State Transfer-API-Schlüssel mit den erforderlichen Berechtigungen für den Endpunkt, den Ihre OneTrust-Aktion verwenden wird.<br><br>Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze-Instanz | Ihre Braze-Instanz erhalten Sie von Ihrem Braze-Onboarding-Manager:in oder auf der [API-Übersichtsseite]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

Die folgende Integration bietet eine Anleitung zum Erstellen eines Workflows für das Update or aktualisieren der Nutzer:innen-Einwilligung und eines Workflows zum Löschen von Nutzer:innen. Weitere Einzelheiten zu zusätzlich unterstützten Braze-Endpunkten finden Sie unter [Andere unterstützte Aktionen](#Other-supported-actions).

### Braze-Zugangsdaten zu OneTrust hinzufügen {#add-braze-credentials-to-onetrust}

Navigieren Sie im OneTrust-Menü **Integrations** zu **Credentials** > Button **Add New**, um den Bildschirm **Select System** aufzurufen. Suchen Sie hier **Braze** und klicken Sie dann auf den Button **Next**.

Folgen Sie den Aufforderungen auf dem Bildschirm **Enter Credential Details** und geben Sie die folgenden Informationen ein. Speichern Sie Ihre Zugangsdaten, wenn Sie fertig sind.
  - Zugangsdaten-Name
  - Setzen Sie den Konnektor-Typ auf **Web App**
  - Hostname: `<your-braze-instance-url>`
  - **Anfrage-Header**:
    - **Authorization**: Bearer
    - **Content-Type**: application/json
  - Token / Textbaustein: `<your-braze-api-key>`

### Braze als System hinzufügen {#add-braze-as-a-system}

#### 1. Schritt: Einen Workflow erstellen {#step-1-create-a-workflow}

{% tabs %}
{% tab User Consent Update or aktualisieren %}
1. Navigieren Sie im OneTrust-Integrationsmenü zu **Gallery** > **Braze** > **Add**, um einen neuen Workflow zu erstellen.![OneTrust-Galerie mit der Braze-Integration und einem „Add“-Button.]({% image_buster /assets/img/onetrust/onetrust.png %})<br><br>
2. Geben Sie einen Namen und eine Benachrichtigungs-E-Mail im Workflow-Modal an. Klicken Sie auf den Button **Create**. Bei der Erstellung werden Sie zum Workflow Builder weitergeleitet. Ihr Braze-Workflow wird mit API-Aufrufen und Aktionen bestückt, die für die Bearbeitung von Löschanfragen verwendet werden können. <br><br>
3. Wählen Sie im Workflow Builder die Aktion, die Sie im Workflow triggern möchten.<br>![OneTrust Workflow Builder für ein Einwilligungs-Update-Ereignis einer betroffenen Person.]({% image_buster /assets/img/onetrust/onetrust2.png %})

{% endtab %}
{% tab User Deletion %}

1. Navigieren Sie im OneTrust-Integrationsmenü zu **Gallery** > **Braze** > **Add**, um einen neuen Workflow zu erstellen.![OneTrust-Galerie mit der Braze-Integration und einem „Add“-Button.]({% image_buster /assets/img/onetrust/onetrust.png %})<br><br>
2. Geben Sie einen Namen und eine Benachrichtigungs-E-Mail im Workflow-Modal an. Klicken Sie auf den Button **Create**. Bei der Erstellung werden Sie zum Workflow Builder weitergeleitet. Ihr Braze-Workflow wird mit API-Aufrufen und Aktionen bestückt, die für die Bearbeitung von Löschanfragen verwendet werden können. <br><br>
3. Wählen Sie im Workflow Builder die Aktion, die Sie im Workflow triggern möchten.<br>![OneTrust Workflow Builder für ein Löschungs-Ereignis einer betroffenen Person.]({% image_buster /assets/img/onetrust/onetrust8.png %})
{% endtab %}
{% endtabs %}

#### 2. Schritt: Aktion auswählen {#step-2-select-action}
{% tabs %}
{% tab User Consent Update or aktualisieren %}

1. Wenn Sie fertig sind, klicken Sie auf **Done** und wählen Sie **Add Action**. Beachten Sie, dass die von Ihnen gewählte Aktion davon abhängt, welche Art von Einstellung aktualisiert werden soll und welchen Endpunkt Sie bevorzugen.
- Um die globalen Abo-Einstellungen von Nutzer:innen zu Update or aktualisieren or aktualisieren, wählen Sie die Aktion **POST User track - attributes**.
- Um die Abo-Gruppen-Einstellungen von Nutzer:innen zu aktualisieren, wählen Sie die Aktion **POST User Track - Attributes** oder die Aktion **POST Set Users Subscription Group Status**.<br>![OneTrust-Menü „Add Action“ mit der Option „POST User track - attributes“.]({% image_buster /assets/img/onetrust/onetrust4.png %})<br><br>
2. Wählen Sie die gewünschte Aktion, wählen Sie Ihre zuvor erstellten Braze-Zugangsdaten aus und klicken Sie auf **Next**.<br>![OneTrust-Zugangsdatenauswahl für eine „POST User track - attributes“-Aktion.]({% image_buster /assets/img/onetrust/onetrust5.png %})

{% endtab %}
{% tab User Deletion %}

1. Wenn Sie fertig sind, klicken Sie auf **Done** und wählen Sie **Add Action**.
- Um Nutzer:innen aus Braze zu löschen, wählen Sie die Aktion **POST User Delete Action**.
<br>![OneTrust-Menü „Add Action“ mit der Option „POST User Delete“.]({% image_buster /assets/img/onetrust/onetrust9.png %})<br><br>
2. Wählen Sie die gewünschte Aktion, wählen Sie Ihre zuvor erstellten Braze-Zugangsdaten aus und klicken Sie auf **Next**.<br>![OneTrust-Zugangsdatenauswahl für eine „POST User Delete“-Aktion.]({% image_buster /assets/img/onetrust/onetrust5.png %})

{% endtab %}
{% endtabs %}
#### 3. Schritt: Anfrage-Body Update or aktualisieren or aktualisieren {#step-3-update-request-body}
{% tabs %}
{% tab User Consent Update or aktualisieren %}

1. Update or aktualisieren or aktualisieren Sie den Body, um alle notwendigen dynamischen Werte aufzunehmen. Stellen Sie sicher, dass der Body der Aktion mit dem [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) und dem [`/subscription/status/set`-Endpunkt]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) übereinstimmt.
2. Passen Sie den Workflow mit zusätzlichen Parametern oder bedingter Logik an die Anforderungen Ihres Unternehmens an.
3. Wenn Sie mit der Bearbeitung fertig sind, klicken Sie auf **Finish** und dann auf **Activate**, um den Workflow zu aktivieren.

{% alert note %}
Wenn Sie die OneTrust-Workflows verwenden, um die Einstellungen für Abo-Gruppen in Braze zu Update or aktualisieren or aktualisieren, muss die `subscription_group_id` mit der ID übereinstimmen, die von Braze bei der Erstellung der Abo-Gruppe festgelegt wurde. Sie können auf die `subscription_group_id` einer Abo-Gruppe zugreifen, indem Sie im Braze-Dashboard zur Seite **Abo-Gruppe** navigieren.
{% endalert %}

![OneTrust-Anfrage-Body für „POST User track - attributes“ mit Abo-Gruppen-Feldern.]({% image_buster /assets/img/onetrust/onetrust6.png %})

{% endtab %}
{% tab User Deletion %}

1. Update or aktualisieren or aktualisieren Sie den Body, um alle notwendigen dynamischen Werte aufzunehmen. Stellen Sie sicher, dass der Body der Aktion mit dem [`/users/delete`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) übereinstimmt.
2. Wenn Sie mit der Bearbeitung fertig sind, wählen Sie **Finish** und dann **Activate**, um den Workflow zu aktivieren.

![OneTrust-Anfrage-Body für „POST User Delete“ mit einem external_id-Feld.]({% image_buster /assets/img/onetrust/onetrust10.png %})

#### Workflow für Betroffenenanfragen Update or aktualisieren or aktualisieren {#update-the-data-subject-request-workflow}
1. Wählen Sie im Menü **Privacy Rights Automation** die Option **Workflows** aus.
2. Wählen Sie den Workflow aus, den Sie mit der Braze-Integration Update or aktualisieren or aktualisieren möchten.
3. Wählen Sie den Button **Edit**, um die Bearbeitung zu aktivieren.
4. Wählen Sie dann den Workflow-Schritt aus, zu dem Sie die Braze-Integration hinzufügen möchten, und klicken Sie auf **Add Connection**.
5. Fügen Sie den zuvor erstellten Braze-Workflow als System-Unteraufgabe hinzu.

{% endtab %}
{% endtabs %}

## Andere unterstützte Aktionen {#other-supported-actions}

Zusätzlich zu den Aktionen **POST User track - Attributes**, **POST Set Users Subscription Group Status** und **POST User Delete** unterstützt Braze weitere Endpunkte, die zur Erstellung angepasster Workflows und als Unteraufgaben innerhalb bestehender Workflows verwendet werden können.

Um eine vollständige Liste der unterstützten Aktionen zu sehen:
1. Klicken Sie in OneTrust in Ihrem Menü **Integrations** auf **Systems**.
2. Wählen Sie das **Braze**-System.
3. Navigieren Sie zum Tab **Actions**.

![OneTrust-Braze-System-Tab „Actions“ mit einer Liste unterstützter API-Aktionen.]({% image_buster /assets/img/onetrust/onetrust7.png %})