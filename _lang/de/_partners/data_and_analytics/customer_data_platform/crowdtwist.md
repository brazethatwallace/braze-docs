---
nav_title: Oracle Crowdtwist
article_title: Crowdtwist
description: "Dieser Artikel beschreibt die Partnerschaft zwischen Braze und Oracle Crowdtwist mithilfe speziell erstellter Braze-Datentransformations-Templates und der Data-Push-Objekte von Crowdtwist."
alias: /partners/crowdtwist/
page_type: partner
search_tag: Partner
---

# Oracle Crowdtwist

> [Oracle Crowdtwist](https://www.oracle.com/uk/cx/marketing/customer-loyalty/) ist eine führende Cloud-native Lösung zur Kundenbindung, mit der Marken personalisierte Kundenerlebnisse anbieten können. Die Lösung bietet mehr als 100 sofort einsatzbereite Engagement-Pfade, die Marketern eine schnellere Wertschöpfung ermöglichen, um eine umfassendere Sicht auf die Kund:innen zu entwickeln.

Das Feature Data Push von Oracle Crowdtwist erlaubt die Übermittlung von Nutzer:innen- oder Event-Metadaten, sobald ein Update or aktualisieren in der Crowdtwist-Plattform stattfindet.

In diesem Leitfaden wird beschrieben, wie Sie die Live-Push-Feeds für Kundenprofil or Nutzerprofil, Nutzeraktivität und Nutzereinlösung von Oracle Crowdtwist in Ihre Braze-Umgebung integrieren. Es gibt zwei weitere Data-Push-Typen, die in dieser Dokumentation nicht explizit behandelt werden, deren Einrichtung jedoch den gleichen Prinzipien folgt, die in diesem Leitfaden beschrieben sind.

* [Live Push Kundenprofil or Nutzerprofil](https://docs.oracle.com/en/cloud/saas/marketing/crowdtwist-develop/Developers/PushUserProfile-withTiersv2.html): Umfasst die Erstellung neuer Profile und Updates für bestehende Profile.

* [Live Push Nutzeraktivität](https://docs.oracle.com/en/cloud/saas/marketing/crowdtwist-develop/Developers/LivePushUserActivity.html): Enthält Daten über abgeschlossene Nutzeraktivitäten.

* [Live Push Nutzereinlösung](https://docs.oracle.com/en/cloud/saas/marketing/crowdtwist-develop/Developers/LivePushUserRedemption.html): Enthält Daten über eingelöste Prämien von Nutzer:innen.

Mit einem Braze-Datentransformations-Template können Sie die Elemente des Data Push herausfiltern, die für Braze nicht relevant sind, und die in Braze benötigten Werte zuweisen, damit sie von den verfügbaren „Zielen“ genutzt werden können.

Verwenden Sie zum Beispiel einen Data Push, um relevante angepasste Events und Attribute an Braze zu übermitteln, z. B. wenn Nutzer:innen die Treuestufe wechseln oder eine Prämie einlösen. Sie können es auch verwenden, um angepasste Attribute in Braze zu protokollieren, sobald diese Daten im Kundenprofil or Nutzerprofil eines Mitglieds aktualisiert werden, z. B. der Punktestand von Nutzer:innen.

## Voraussetzungen {#prerequisites}


| Anforderung | Beschreibung |
| --- | --- |
| Oracle Crowdtwist-Konto | Ein [Oracle Crowdtwist-Konto](https://www.oracle.com/uk/cx/marketing/customer-loyalty/) ist erforderlich, um diese Partnerschaft zu nutzen. |
| Braze Datentransformation-Endpunkt | Diese Integration basiert auf dem [Datentransformationstool]({{site.baseurl}}/user_guide/data/unification/data_transformation) von Braze. Wenn Sie eine Datentransformation erstellen, generiert Braze einen eindeutigen Endpunkt, den Sie als Ziel für den Data Push von Crowdtwist hinzufügen können. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

Braze und Oracle Crowdtwist haben [Datentransformations-Templates]({{site.baseurl}}/user_guide/data/unification/data_transformation/creating_a_transformation?redirected=1#step-2-create-a-transformation) erstellt, um unseren Kund:innen zu helfen, ihre eigenen Datentransformationen zu entwickeln, die die Events Kundenprofil or Nutzerprofil, Nutzereinlösung und Nutzeraktivität nutzen.

## Schritt 1: Datentransformation aus Oracle Crowdtwist-Template erstellen {#step-1-create-data-transformation-from-oracle-crowdtwist-template}

Navigieren Sie zu **Dateneinstellungen > Datentransformation > Transformationen erstellen > Template verwenden** und wählen Sie das „BRAZE <> CROWDTWIST“-Template Ihrer Wahl aus.

Sie finden vier Templates – jeweils eines für die Transformation von Kundenprofil or Nutzerprofil-, Nutzeraktivitäts- und Nutzereinlösungs-Events sowie ein Master-Template, das bedingte Logik verwendet, um verschiedene Data-Push-Events zu verarbeiten.

Wie in der [Data-Push-Dokumentation von Oracle Crowdtwist](https://docs.oracle.com/en/cloud/saas/marketing/crowdtwist-develop/Developers/DataPush.html) beschrieben, enthalten Data-Push-Objekte unterschiedliche Metadaten, sodass jedes seinen eigenen Transformations-Code benötigt, um geeignete Braze-Objekte zu erstellen. Das Master-Template zeigt, wie Sie eine einzelne Datentransformation einrichten, die jeden der drei Objekttypen akzeptiert, und erstellt eine passende Ausgabe mit Werten aus jedem Objekt.

## Schritt 2: Template Update or aktualisieren or aktualisieren und testen {#step-2-update-and-test-template}

In diesem Abschnitt sehen Sie die annotierten Templates. Der Rumpf dieser Templates ist darauf ausgelegt, an das Ziel `/users/track` gesendet zu werden. Annotationen sind durch `//` am Zeilenanfang und grünen Text gekennzeichnet. Sie können sie löschen, ohne die Funktionsweise des Transformations-Codes zu beeinträchtigen.

Die Transformation verwendet JavaScript und erstellt ein Objekt namens „brazecall“. In diesem Objekt erstellen Sie den Anfrage-Rumpf, der an einen Braze Representational State Transfer API-Endpunkt gesendet wird. Hinweise zu den erforderlichen Strukturen der Anfragen an diese Ziele finden Sie über die Links im Abschnitt „Ziele“.

{% alert note %}
Beachten Sie, dass die „Werte“ jedes „Schlüssels“ mit `payload.` beginnen. Die Payload repräsentiert das Datenobjekt, das von Oracle Crowdtwist empfangen wird. Verwenden Sie die JavaScript-Dot-Notation, um auszuwählen, welches Datenstück die Elemente Ihres Braze-Objekts befüllen soll. Wenn Sie z. B. `external_id: payload.thirdPartyId` sehen, bedeutet das, dass die externe Braze-ID durch den in Oracle Crowdtwist gespeicherten `third_party_id`-Wert gesetzt wird. Weitere Informationen zum Schema oder Aufbau der von Oracle Crowdtwist kommenden Objekte finden Sie in der [Dokumentation von Oracle](https://docs.oracle.com/en/cloud/saas/marketing/crowdtwist-develop/Developers/LivePushUserActivity.html).
{% endalert %}

{% alert important %}
Verwenden Sie die von Oracle Crowdtwist gesendeten Objekte, um Nutzer:innen in Braze zu erstellen. Indem Sie den Schlüssel `update_existing_only` mit dem Wert `false` einbeziehen, erstellt Braze ein Kundenprofil or Nutzerprofil mit den enthaltenen Attributen, wenn ein Attribut- oder Event-Objekt einen Bezeichner enthält, der in Braze nicht existiert. Wenn Sie möchten, dass Oracle Crowdtwist nur bereits in Braze vorhandene Profile aktualisiert, setzen Sie dieses Attribut in jedem Attribut- oder Event-Objekt auf `true`.
{% endalert %}

### Datentransformations-Templates {#data-transformation-templates}
{% tabs %}
{% tab Kundenprofil or Nutzerprofil Event Template%}
```javascript
let brazecall = {
 "attributes": [
   {
     //You must include an appropriate identifier for your attribute or event object from data available in Oracle Crowdtwist. This could be an external ID, Braze ID, user alias, phone, or email address for attribute or event objects.
     "external_id": payload.thirdPartyId,
     "email": payload.emailAddress,
   // **Important** To allow Oracle Crowdtwist events to create users in Braze, set the value of "_update_existing_only" to false. Otherwise, set this value to true in your event and attribute objects.
     "_update_existing_only": false,
     "crowdtwist_loyalty_points": payload.redeemablePoints,
 //In this example, the "tierInfo" object from Crowdtwist is transformed into a Braze Nested Custom Attribute. Use the "_merge_objects" value to avoid duplications in a data point efficient manner.
 //The "tierinfo_current_level" attribute is a flat Braze custom attribute, while the following "tierInfo" value is a nested object mirroring the Crowdtwist payload; the difference in capitalization is intentional.
     "tierinfo_current_level": payload.tierInfo.currentLevel,
     "_merge_objects" : true,
     "tierInfo" : {
       "resetDate": payload.tierInfo.resetDate,
       "dateReached":payload.tierInfo.dateReached,
        "scoreNeededToReach": payload.tierInfo.scoreNeededToReach,
        "nextLevel":{
        "minValue":payload.tierInfo.nextLevel.minValue,
        "maxValue":payload.tierInfo.nextLevel.maxValue,
        "title":payload.tierInfo.nextLevel.title
     }
     }
   }
 ]
,
//Below we show how to create both custom attributes and events from a single Crowdtwist User Profile object.
 "events": [
   {
     "external_id": payload.thirdPartyId,
     "email": payload.emailAddress,
     "name": "assignedByEvent",
//Below we can see how to write a timestamp in your object, which is a required value for some objects, like the Event Object.
     "time": new Date().toISOString(),
     "properties": {
       "assigned_by_event": payload.tierInfo.assignedByEvent,
       "date_assigned": payload.tierInfo.dateAssigned
     },
           "_update_existing_only": false
   }
 ]
};
// After the /users/track request is assigned to brazecall, return brazecall to create an output.
return brazecall;

```

{% endtab %}
{% tab User Activity Event Template %}
```javascript
let brazecall = {
"events": [
   {
     "external_id": payload.thirdPartyId,
     "_update_existing_only": false,
     "activityId": payload.activityId,
     "name": payload.activityName,
     "time": new Date().toISOString(),
     "properties": {
       "description": payload.description,
       "date_assigned": payload.dateAwarded
     }
   }
 ]
};
return brazecall;
```
{% endtab %}
{% tab Redemption Event Template %}
```javascript
let brazecall = {
 "attributes": [
   {
   "external_id": payload.thirdPartyId,
   //A user redemption event may not have a third party id, in which case you can instead provide the opportunity to include a user alias.
   "user_alias": { "alias_name" : "crowdtwist_redemption_username", "alias_label" : payload.userName},
   "_update_existing_only": false,
   "redeemed_coupon": payload.couponCode,
   "total_points_redeemed": payload.totalPointsRedeemed
      }
]
}
return brazecall;

```
{%endtab%}
{% tab Master Template %}
```javascript
//The master template uses JavaScript's conditional operators to determine the output of the Data Transformation. This example shows how to apply JavaScript to your transformation to allow for a dynamic range of sources or inputs.

 // We open the transformation with a simple "if" function. We're checking if the value "payload.tierInfo" is present. "tierInfo" is a value that is always populated in the User Profile Live Push object, but is not present in the others.

if (payload.tierInfo) {
let brazecall = {
 "attributes": [
   {
     "external_id": payload.thirdPartyId,
     "email": payload.emailAddress,
     "_update_existing_only": false,
     "crowdtwist_loyalty_points": payload.redeemablePoints,
     "tierinfo_current_level": payload.tierInfo.currentLevel,
     "_merge_objects" : true,
     "tierInfo" : {
       "resetDate": payload.tierInfo.resetDate,
       "dateReached":payload.tierInfo.dateReached,
        "scoreNeededToReach": payload.tierInfo.scoreNeededToReach,
        "nextLevel":{
        "minValue":payload.tierInfo.nextLevel.minValue,
        "maxValue":payload.tierInfo.nextLevel.maxValue,
        "title":payload.tierInfo.nextLevel.title
     }
     }
   }
 ]
,
 "events": [
   {
     "external_id": payload.thirdPartyId,
     "email": payload.emailAddress,
     "name": "assignedByEvent",
     "time": new Date().toISOString(),
     "properties": {
       "assigned_by_event": payload.tierInfo.assignedByEvent,
       "date_assigned": payload.tierInfo.dateAssigned
     },
           "_update_existing_only": false
   }
 ]
};
return brazecall;
//Now we use an "else if" operator to change the "brazecall" body if the object is a User Activity event by checking if the unique key "activityId" has been populated.
} else if (payload.activityId) {
 let brazecall = {
"events": [
   {
     "external_id": payload.thirdPartyId,
     "_update_existing_only": false,
     "activityId": payload.activityId,
     "name": payload.activityName,
     "time": new Date().toISOString(),
     "properties": {
       "description": payload.description,
       "date_assigned": payload.dateAwarded
     }
   }
 ]
};
return brazecall;
//Finally, this conditional statement triggers if the Data Push object is a User Redemption event, based on whether a value populates in the key "rewardId".
} else if (payload.rewardId) {
 let brazecall = {
 "attributes": [
   {
   "external_id": payload.thirdPartyId,
   "_update_existing_only": false,
   "redeemed_coupon": payload.couponCode,
   "total_points_redeemed": payload.totalPointsRedeemed
      }
]
}
return brazecall;
} else {
 //Include this error message to help with troubleshooting in the log if a call fails. Replace the text in the parentheses with anything that might be clearer to your team based on your Data Transformation.
 throw new Error("No appropriate Identifiers found");
}

```
{% endtab %}
{% endtabs %}

### Ziele {#destinations}

Die Templates in dieser Anleitung sind darauf ausgelegt, an das Ziel „Track Users“ zu senden, aber Sie können Ihr Template so gestalten, dass es an jeden der Endpunkte sendet, die im [Datentransformations-Leitfaden von Braze]({{site.baseurl}}/user_guide/data/data_transformation/creating_a_transformation#step-2-create-a-transformation) aufgeführt sind, mit Unterstützung der zugehörigen [Representational State Transfer API-Dokumentation]({{site.baseurl}}/api/home).

### Testen {#testing}

Nachdem Sie das Template nach Ihren Wünschen angepasst haben, müssen Sie überprüfen, ob es korrekt funktioniert. Wählen Sie im Transformationseditor **Validate** aus, um eine Vorschau im Abschnitt **Output** zu generieren und zu bestätigen, dass Braze die zugeordnete Anfrage für Ihr gewähltes Ziel akzeptiert.

Wenn Sie mit dem Objekt zufrieden sind, das Sie im Feld **Output** sehen, wählen Sie **Activate** aus, damit der Datentransformations-Endpunkt bereit ist, Daten zu empfangen.

Sie finden die Webhook-URL Ihrer Datentransformation im Panel mit den Transformationsdetails. Kopieren Sie diese und verwenden Sie sie für die Konfiguration im Integration Hub von Oracle Crowdtwist.

{% alert important %}
Die Braze-Datentransformations-Endpunkte haben ein Rate-Limit von 1.000 Anfragen pro Minute. Überlegen Sie, wie schnell diese Daten in Braze verfügbar sein sollen, und sprechen Sie mit Ihrem Braze Account Manager:in, wenn Sie ein höheres Datentransformations-Rate-Limit benötigen.
{% endalert %}

Datentransformationen sind ein sehr dynamisches Werkzeug, und Sie können sie mit JavaScript-Kenntnissen und mithilfe unserer Representational State Transfer API-Dokumentation für Zwecke gestalten, die über das in diesem Dokument Beschriebene hinausgehen. Für Unterstützung oder Fehlerbehebung bei komplexen Änderungen an Ihren Datentransformations-Templates sprechen Sie mit Ihrem CSM or Customer-Success-Manager or Customer-Success-Manager:in, um mehr über die verfügbare Beratung zu erfahren.