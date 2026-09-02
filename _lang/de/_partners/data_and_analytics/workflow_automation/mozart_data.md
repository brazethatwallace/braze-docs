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
{% multi_lang_include partners/workflow_automation/mozart_data_integration_bullets.md %}

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
| Mozart Data-Konto | Ein Mozart Data-Konto ist erforderlich, um diese Partnerschaft nutzen zu können. [Registrierung Sie sich für ein Mozart Data-Konto](https://app.mozartdata.com/signup)|
| Snowflake-Konto<br>Option 1: Neues Konto | Wählen Sie während des Mozart Data-Kontoerstellungsprozesses **Create a New Snowflake Account** aus, damit Mozart Data ein neues Snowflake-Konto für Sie bereitstellt. |
| Snowflake-Konto<br>Option 2: Bestehendes Konto | Wenn Ihre Organisation bereits über ein Snowflake-Konto verfügt, können Sie die Option „Mozart Data Connected“ verwenden.<br><br>Wählen Sie die Option **Already Have a Snowflake Account** aus, um ein bestehendes Snowflake-Konto zu verbinden. Um diese Option zu nutzen, muss eine Nutzer:in mit Berechtigungen auf Kontoebene [diese Schritte befolgen](https://help.mozartdata.com/docs/setting-up-data-warehouse#existingsnowflakeaccount). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

Die Integration wird sowohl für die Synchronisierung von Daten von [Braze zu Mozart Data](#syncing-data-from-braze-to-mozart-data) als auch von [Mozart Data zu Braze](#syncing-data-from-mozart-data-to-braze) unterstützt.

### Daten von Braze zu Mozart Data synchronisieren {#syncing-data-from-braze-to-mozart-data}

#### Schritt 1: Braze-Konnektor einrichten {#step-1-set-up-braze-connector}

1. Gehen Sie in Mozart Data zu **Connectors** und klicken Sie auf **Add Connector**.
2. Suchen Sie nach „Braze“ und wählen Sie die Konnektor-Karte aus.
3. Geben Sie den Namen eines Zielschemas ein, in dem alle synchronisierten Daten aus Braze gespeichert werden sollen. Wir empfehlen, den Standard-Schemanamen `braze` zu verwenden.
4. Klicken Sie auf **Add Connector**.

#### Schritt 2: Fivetran-Konnektor-Formular ausfüllen {#step-2-fill-out-the-fivetran-connector-form}

Sie werden auf die Seite des Fivetran-Konnektors weitergeleitet, nachdem Sie Schritt 1 abgeschlossen haben. Füllen Sie die vorgegebenen Felder aus und klicken Sie anschließend auf **Continue** > **Save & Test**, um den Fivetran-Konnektor fertigzustellen.

Fivetran beginnt mit der Synchronisierung der Daten von Ihrem Braze-Konto in Ihr Snowflake Data Warehouse. Sie können auf Abfragedaten von Mozart Data zugreifen, nachdem der Konnektor die Synchronisierung abgeschlossen hat.

### Daten von Mozart Data zu Braze synchronisieren {#syncing-data-from-mozart-data-to-braze}

#### Schritt 1: Snowflake Data Warehouse einrichten {#step-1-set-up-a-snowflake-data-warehouse}

Folgen Sie den Anweisungen zur [Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/?tab=snowflake), um eine Tabelle, einen Nutzer und Berechtigungen über die Snowflake-Schnittstelle einzurichten. Beachten Sie, dass dieser Schritt Snowflake-Zugriff auf Admin-Ebene erfordert.

#### Schritt 2: Snowflake-Integration in Braze einrichten {#step-2-set-up-your-snowflake-integration-in-braze}

Nachdem Sie Ihr Snowflake Warehouse eingerichtet haben, gehen Sie in Mozart Data auf die Seite **Integration** und wählen Sie **Braze** aus. In der **Braze**-Integrationsansicht finden Sie die Zugangsdaten, die Sie in Braze kopieren müssen.

![Mozart Data-Integrationsseite mit ausgewähltem Braze und Snowflake-Verbindungszugangsdaten zur Verwendung in Braze.]({% image_buster /assets/img/mozartdata/mozartdata-braze-integrationpage.png %}){: style="max-width:80%;"}

Gehen Sie dann, während Sie bei Braze angemeldet sind, zu **Integrations > Technology Partners > Snowflake**, um den Integrationsprozess zu starten. Kopieren Sie die Zugangsdaten von Mozart Data und fügen Sie sie auf der Snowflake-Datenimportseite hinzu. Klicken Sie auf **Set up sync details** und geben Sie Ihr Snowflake-Konto und die Informationen zur Quelltabelle ein.

![Braze-Snowflake-Partnerintegrationsformular mit Feldern für Konto, Warehouse, Datenbank und Schema, die mit Mozart Data-Zugangsdaten ausgefüllt sind.]({% image_buster /assets/img/mozartdata/mozartdata-braze-snowflakecredentials.png %}){: style="max-width:80%;"}

Wählen Sie als Nächstes einen Namen für Ihre Synchronisierung, geben Sie Kontakt-E-Mails an und wählen Sie einen Datentyp und eine Synchronisierungshäufigkeit auf dem Bildschirm für die Braze-Snowflake-Importkonfiguration aus.

#### Schritt 3: Public Key zum Braze-Nutzer hinzufügen {#step-3-add-a-public-key-to-the-braze-user}

An dieser Stelle müssen Sie zu Snowflake zurückkehren, um die Einrichtung abzuschließen. Fügen Sie den Public Key, der auf dem Braze-Dashboard angezeigt wird, dem Nutzer hinzu, den Sie für die Verbindung von Braze mit Snowflake erstellt haben.

Weitere Informationen dazu finden Sie in der [Snowflake-Dokumentation](https://docs.snowflake.com/en/user-guide/key-pair-auth.html). Wenn Sie die Schlüssel zu einem beliebigen Zeitpunkt austauschen möchten, kann Mozart Data ein neues Schlüsselpaar erzeugen und Ihnen den neuen Public Key zur Verfügung stellen.

```sql
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='Braze12345...';
```

#### Schritt 4: Verbindung testen {#step-4-test-connection}

Sobald der Nutzer mit dem Public Key aktualisiert wurde, kehren Sie zum Braze-Dashboard zurück und klicken Sie auf **Test connection**. Bei Erfolg sehen Sie eine Vorschau der Daten. Wenn die Verbindung aus irgendeinem Grund nicht zustande kommt, wird eine Fehlermeldung angezeigt, die Sie bei der Fehlerbehebung unterstützt.

![Ergebnis des Braze-Snowflake-Integrationstests mit einer erfolgreichen Vorschau nach Anwendung des Public Key.]({% image_buster /assets/img/mozartdata/mozartdata-braze-testsyncpublickey.png %}){: style="max-width:80%;"}

{% alert note %}
Sie müssen eine Integration erfolgreich testen, bevor sie vom Entwurfsstatus in den aktiven Status übergehen kann. Wenn Sie die Erstellungsseite verlassen müssen, wird Ihre Integration gespeichert, und Sie können die Detailseite erneut aufrufen, um Änderungen vorzunehmen und zu testen.
{% endalert %}

## Verwendung dieser Integration {#using-this-integration}

### Zugriff auf Braze-Daten als Mozart Data-Nutzer:in {#how-to-access-braze-data-as-a-mozart-data-user}
Nach der erfolgreichen Erstellung eines Mozart Data-Kontos können Sie auf Ihre Braze-Daten zugreifen, die mit Ihrem Snowflake Data Warehouse über Mozart Data synchronisiert wurden.

#### Transformationen {#transforms}
Mozart Data bietet eine SQL-Transformationsschicht, mit der Nutzer:innen eine Ansicht oder Tabelle erstellen können. Sie können eine Dimensionstabelle auf Nutzer:innen-Ebene erstellen (zum Beispiel `dim_users`), um die Produktnutzungsdaten, den Transaktionsverlauf und die Engagement-Aktivitäten jeder Nutzer:in mit Braze-Nachrichten zusammenzufassen.

#### Analyse {#analysis}
Mithilfe der Transformationsmodelle oder der von Braze synchronisierten Rohdaten können Sie das Engagement der Nutzer:innen mit Braze-Nachrichten analysieren. Darüber hinaus können Sie die Braze-Daten mit anderen Anwendungsdaten kombinieren und untersuchen, wie die Insights, die Sie aus der Interaktion der Nutzer:innen mit den Braze-Nachrichten gewonnen haben, mit anderen verfügbaren Daten über die Nutzer:innen zusammenhängen. Zum Beispiel mit demografischen Informationen, Einkaufsverlauf, Produktnutzung und Kundenservice-Engagement.

Dies kann Ihnen helfen, fundiertere Entscheidungen über Engagement-Strategien zur Verbesserung der Nutzer:innenbindung zu treffen. All dies kann innerhalb der Mozart Data-Schnittstelle mit dem Query-Tool durchgeführt werden, wo Sie die Ergebnisse in ein Google Sheet oder eine CSV-Datei exportieren können, um eine Präsentation vorzubereiten.

#### Business-Intelligence (BI)
Bereit, Ihre Insights zu visualisieren und mit anderen Team-Mitgliedern zu teilen? Mozart Data lässt sich mit nahezu jedem BI-Tool integrieren. Wenn Sie noch kein BI-Tool haben, kontaktieren Sie Mozart Data, um ein kostenloses Metabase-Konto einzurichten.