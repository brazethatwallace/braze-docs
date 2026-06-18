---
nav_title: Mozart Data
article_title: Mozart Data
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Mozart Data, einer modernen All-in-One-Datenplattform, die es Ihnen erlaubt, mit Fivetran Daten in Snowflake zu importieren, Transformationen zu erstellen, Daten zu kombinieren und vieles mehr."
alias: /partners/mozart_data/
page_type: partner
search_tag: Partner

---

# Mozart Data

{% multi_lang_include video.html id="HU6dSOClcQ0" align="right" %}

> [Mozart Data](https://mozartdata.com/) ist eine moderne All-in-One-Datenplattform, die auf Fivetran, Portable und Snowflake basiert.

Die Integration von Braze und Mozart Data ermöglicht es Ihnen:
- Fivetran zu verwenden, um Braze-Daten in Snowflake zu importieren
- Transformationen zu erstellen, indem Sie Braze-Daten mit anderen Anwendungsdaten kombinieren und das Nutzer:innen-Verhalten effektiv analysieren
- Daten aus Snowflake in Braze zu importieren, um neue Customer-Engagement-Möglichkeiten zu schaffen
- Braze-Daten mit anderen Anwendungsdaten zu kombinieren, um ein ganzheitlicheres Verständnis des Nutzer:innen-Verhaltens zu erhalten
- Ein Business-Intelligence-Tool zu integrieren, um die in Snowflake gespeicherten Daten weiter zu untersuchen

## Voraussetzungen {#prerequisites}

<style>
table th:nth-child(1) {
    width: 25%;
}
table th:nth-child(2) {
    width: 75%;
}
table td {
    word-break: break-word;
}
</style>

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Mozart Data-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, ist ein Mozart Data-Konto erforderlich. [Registrieren Sie sich hier.](https://app.mozartdata.com/signup)|
| Snowflake-Konto<br>Option 1: Neues Konto | Wählen Sie **Create a New Snowflake Account** während des Erstellungsprozesses für das Mozart Data-Konto aus, damit Mozart Data ein neues Snowflake-Konto für Sie einrichtet. |
| Snowflake-Konto<br>Option 2: Bestehendes Konto | Wenn Ihr Unternehmen bereits über ein Snowflake-Konto verfügt, können Sie die Option Mozart Data Connected verwenden.<br><br>Wählen Sie die Option **Already Have a Snowflake Account**, um ein bestehendes Snowflake-Konto zu verbinden. Um diese Option zu nutzen, müssen Nutzer:innen mit Berechtigungen auf Kontoebene [die folgenden Schritte ausführen](https://help.mozartdata.com/docs/setting-up-data-warehouse#existingsnowflakeaccount). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

Die Integration wird sowohl für die Synchronisierung von Daten von [Braze zu Mozart Data](#syncing-data-from-braze-to-mozart-data) als auch von [Mozart Data zu Braze](#syncing-data-from-mozart-data-to-braze) unterstützt.

### Daten von Braze zu Mozart Data synchronisieren {#syncing-data-from-braze-to-mozart-data}

#### 1. Schritt: Braze-Konnektor einrichten {#step-1-set-up-braze-connector}

1. Gehen Sie in Mozart Data zu **Connectors** und klicken Sie auf **Add Connector**.
2. Suchen Sie nach „Braze“ und wählen Sie die Konnektor-Karte aus.
3. Geben Sie den Namen eines Zielschemas ein, in dem alle synchronisierten Daten aus Braze gespeichert werden sollen. Wir empfehlen, den Standard-Schemanamen `braze` zu verwenden.
4. Klicken Sie auf **Add Connector**.

#### 2. Schritt: Fivetran-Konnektor-Formular ausfüllen {#step-2-fill-out-the-fivetran-connector-form}

Sie werden auf die Seite des Fivetran-Konnektors weitergeleitet. Füllen Sie auf dieser Seite die vorgegebenen Felder aus. Klicken Sie anschließend auf **Continue** > **Save & Test**, um den Fivetran-Konnektor fertigzustellen.

Fivetran beginnt mit der Synchronisierung der Daten von Ihrem Braze-Konto in Ihr Snowflake Data Warehouse. Sie können auf Abfragedaten von Mozart Data zugreifen, nachdem der Konnektor die Synchronisierung abgeschlossen hat.

### Daten von Mozart Data zu Braze synchronisieren {#syncing-data-from-mozart-data-to-braze}

#### 1. Schritt: Snowflake Data Warehouse einrichten {#step-1-set-up-a-snowflake-data-warehouse}

Folgen Sie den Anweisungen zur [Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/?tab=snowflake), um eine Tabelle, einen Nutzer und Berechtigungen über die Snowflake-Schnittstelle einzurichten. Beachten Sie, dass dieser Schritt Snowflake-Zugriff auf Admin-Ebene erfordert.

#### 2. Schritt: Snowflake-Integration in Braze einrichten {#step-2-set-up-your-snowflake-integration-in-braze}

Nachdem Sie Ihr Snowflake Warehouse eingerichtet haben, gehen Sie in Mozart Data auf die Seite **Integration** und wählen Sie **Braze** aus. Hier finden Sie die Zugangsdaten, die Sie Braze zur Verfügung stellen müssen.

![]({% image_buster /assets/img/mozartdata/mozartdata-braze-integrationpage.png %}){: style="max-width:80%;"}

Gehen Sie dann, während Sie bei Braze angemeldet sind, zu **Integrations > Technology Partners > Snowflake**, um den Integrationsprozess zu starten. Kopieren Sie die Zugangsdaten von Mozart Data und fügen Sie sie auf der Snowflake-Datenimportseite hinzu. Klicken Sie auf **Set up sync details** und geben Sie Ihr Snowflake-Konto und die Informationen zur Quelltabelle ein.

![]({% image_buster /assets/img/mozartdata/mozartdata-braze-snowflakecredentials.png %}){: style="max-width:80%;"}

Wählen Sie als Nächstes einen Namen für Ihre Synchronisierung, geben Sie Kontakt-E-Mails an und wählen Sie einen Datentyp und eine Synchronisierungshäufigkeit auf dem Bildschirm für den Braze-Snowflake-Datenimport aus.

#### 3. Schritt: Public Key zum Braze-Nutzer hinzufügen {#step-3-add-a-public-key-to-the-braze-user}

An dieser Stelle müssen Sie zu Snowflake zurückkehren, um die Einrichtung abzuschließen. Fügen Sie den Public Key, der auf dem Braze-Dashboard angezeigt wird, dem Nutzer hinzu, den Sie für die Verbindung von Braze mit Snowflake erstellt haben.

Weitere Informationen dazu finden Sie in der [Snowflake-Dokumentation](https://docs.snowflake.com/en/user-guide/key-pair-auth.html). Wenn Sie die Schlüssel zu einem beliebigen Zeitpunkt austauschen möchten, kann Mozart Data ein neues Schlüsselpaar erzeugen und Ihnen den neuen Public Key zur Verfügung stellen.

```sql
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='Braze12345...';
```

#### 4. Schritt: Verbindung testen {#step-4-test-connection}

Sobald der Nutzer mit dem Public Key aktualisiert wurde, kehren Sie zum Braze-Dashboard zurück und klicken Sie auf **Test connection**. Bei Erfolg sehen Sie eine Vorschau der Daten. Wenn die Verbindung aus irgendeinem Grund nicht zustande kommt, wird eine Fehlermeldung angezeigt, die Sie bei der Fehlerbehebung unterstützt.

![]({% image_buster /assets/img/mozartdata/mozartdata-braze-testsyncpublickey.png %}){: style="max-width:80%;"}

{% alert note %}
Sie müssen eine Integration erfolgreich testen, bevor sie vom Entwurfsstatus in den aktiven Status übergehen kann. Wenn Sie die Erstellungsseite verlassen müssen, wird Ihre Integration gespeichert, und Sie können die Detailseite erneut aufrufen, um Änderungen vorzunehmen und zu testen.
{% endalert %}

## Verwendung dieser Integration {#using-this-integration}

### So greifen Sie als Mozart Data-Nutzer:in auf Braze-Daten zu {#how-to-access-braze-data-as-a-mozart-data-user}
Nach erfolgreicher Einrichtung eines Mozart Data-Kontos können Sie von Mozart Data aus auf Ihre mit Ihrem Snowflake Data Warehouse synchronisierten Braze-Daten zugreifen.

#### Transformationen {#transforms}
Mozart Data bietet eine SQL-Transformationsschicht, mit der Nutzer:innen eine Ansicht oder Tabelle erstellen können. Sie können eine Dimensionstabelle auf Nutzer:innen-Ebene erstellen (z. B. `dim_users`), um die Daten zur Produktnutzung, den Transaktionsverlauf und die Engagement-Aktivitäten jeder Nutzer:in mit Braze-Nachrichten zusammenzufassen.

#### Analyse {#analysis}
Mithilfe der Transformationsmodelle oder der von Braze synchronisierten Rohdaten können Sie das Engagement der Nutzer:innen mit Braze-Nachrichten analysieren. Darüber hinaus können Sie die Braze-Daten mit anderen Anwendungsdaten kombinieren und analysieren, wie sich die Insights, die Sie aus der Interaktion der Nutzer:innen mit den Braze-Nachrichten gewonnen haben, auf andere Daten beziehen, die Ihnen über die Nutzer:innen vorliegen. Zum Beispiel ihre demografischen Daten, den Einkaufsverlauf, die Produktnutzung und das Customer-Engagement.

Dies kann Ihnen helfen, fundiertere Entscheidungen über Engagement-Strategien zu treffen, um die Bindung der Nutzer:innen zu verbessern. Das alles können Sie innerhalb der Schnittstelle von Mozart Data mit dem Abfragetool erledigen. Dort können Sie die Ergebnisse in ein Google Sheet oder eine CSV-Datei exportieren, um sie für eine Präsentation vorzubereiten.

#### Business-Intelligence (BI)
Sind Sie bereit, Ihre Insights zu visualisieren und mit anderen Teammitgliedern zu teilen? Mozart Data lässt sich mit fast allen BI-Tools integrieren. Wenn Sie noch kein BI-Tool besitzen, wenden Sie sich an Mozart Data, um ein kostenloses Metabase-Konto einzurichten.