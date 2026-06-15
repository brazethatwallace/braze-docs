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

Das Feature Data Push von Oracle Crowdtwist erlaubt die Übermittlung von Nutzer:innen- oder Event-Metadaten, sobald ein Update in der Crowdtwist-Plattform stattfindet.

In diesem Leitfaden wird beschrieben, wie Sie die Live-Push-Feeds für Nutzerprofil, Nutzeraktivität und Nutzereinlösung von Oracle Crowdtwist in Ihre Braze-Umgebung integrieren. Es gibt zwei weitere Data-Push-Typen, die in dieser Dokumentation nicht explizit behandelt werden, deren Einrichtung jedoch den gleichen Prinzipien folgt, die unten beschrieben sind.

* [Live Push Nutzerprofil](https://docs.oracle.com/en/cloud/saas/marketing/crowdtwist-develop/Developers/PushUserProfile-withTiersv2.html): Umfasst die Erstellung neuer Profile und Updates für bestehende Profile.

* [Live Push Nutzeraktivität](https://docs.oracle.com/en/cloud/saas/marketing/crowdtwist-develop/Developers/LivePushUserActivity.html): Enthält Daten über abgeschlossene Nutzeraktivitäten.

* [Live Push Nutzereinlösung](https://docs.oracle.com/en/cloud/saas/marketing/crowdtwist-develop/Developers/LivePushUserRedemption.html): Enthält Daten über eingelöste Prämien von Nutzer:innen.

Mit einem Braze-Datentransformations-Template können Sie die Elemente des Data Push herausfiltern, die für Braze nicht relevant sind, und die in Braze benötigten Werte zuweisen, damit sie von den verfügbaren „Zielen“ genutzt werden können.

Verwenden Sie zum Beispiel einen Data Push, um relevante angepasste Events und Attribute an Braze zu übermitteln, z. B. wenn Nutzer:innen die Treuestufe wechseln oder eine Prämie einlösen. Sie können es auch verwenden, um angepasste Attribute in Braze zu protokollieren, sobald diese Daten im Nutzerprofil eines Mitglieds aktualisiert werden, z. B. der Punktestand von Nutzer:innen.

## Voraussetzungen {#prerequisites}


| Anforderung | Beschreibung |
| --- | --- |
| Oracle Crowdtwist-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Oracle Crowdtwist-Konto](https://www.oracle.com/uk/cx/marketing/customer-loyalty/). |
| Braze-Datentransformations-Endpunkt | Diese Integration stützt sich auf das [Datentransformations-Tool]({{site.baseurl}}/user_guide/data/unification/data_transformation/) von Braze. Wenn Sie eine Datentransformation erstellen, generiert Braze einen eindeutigen Endpunkt, den Sie als Ziel für den Data Push von Crowdtwist hinzufügen können.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

Braze und Oracle Crowdtwist haben [Datentransformations-Templates]({{site.baseurl}}/user_guide/data/data_transformation/creating_a_transformation?redirected=1#step-2-create-a-transformation) erstellt, um unseren Kund:innen zu helfen, ihre eigenen Datentransformationen zu entwickeln, die die Events Nutzerprofil, Nutzereinlösung und Nutzeraktivität nutzen.

## 1. Schritt: Datentransformation aus Oracle Crowdtwist Template erstellen {#step-1-create-data-transformation-from-oracle-crowdtwist-template}

Navigieren Sie zu **Dateneinstellungen > Datentransformation > Transformationen erstellen > Vorlage verwenden** und wählen Sie das „BRAZE <> CROWDTWIST“-Template Ihrer Wahl.

Sie finden vier Templates – jeweils eines für die Transformation von Nutzerprofil-, Nutzeraktivitäts- und Nutzereinlösungs-Events sowie ein Master-Template, das mit bedingter Logik auf verschiedene Data-Push-Events angewendet wird.

Wie in der [Data-Push-Dokumentation von Oracle Crowdtwist](https://docs.oracle.com/en/cloud/saas/marketing/crowdtwist-develop/Developers/DataPush.html) gezeigt wird, enthalten Data-Push-Objekte unterschiedliche Metadaten, sodass für jedes Objekt ein eigener Transformations-Code erforderlich ist, um entsprechende Braze-Objekte zu erstellen. Das Master-Template veranschaulicht, wie Sie eine einzelne Datentransformation einrichten, um jede der drei Arten von Objekten zu akzeptieren und eine entsprechende Ausgabe mit Werten aus jedem Objekt zu erstellen.

## 2. Schritt: Template aktualisieren und testen {#step-2-update-and-test-template}

Unten sehen Sie die kommentierten Templates. Der Hauptteil dieser Templates ist für das Ziel `/users/track` bestimmt. Anmerkungen sind durch den `//`-Zeilenanfang und grünen Text gekennzeichnet. Sie können sie löschen, ohne dass der Transformations-Code beeinträchtigt wird.

Die Transformation verwendet JavaScript, das ein Objekt namens „brazecall“ erstellt. In diesem Objekt erstellen Sie den Anfragekörper, der an einen Braze REST API Endpunkt gesendet wird. Hinweise zu den erforderlichen Strukturen der Anfragen an diese Ziele finden Sie unter den Links im Abschnitt „Ziele“.

{% alert note %}
Beachten Sie, dass die „Werte“ der einzelnen „Schlüssel“ mit `payload.` beginnen. Die Payload stellt das von Oracle Crowdtwist empfangene Datenobjekt dar. Verwenden Sie die JavaScript-Punktnotation, um auszuwählen, mit welchen Daten Sie die Elemente Ihres Braze-Objekts füllen möchten. Wenn Sie zum Beispiel `external_id: payload.thirdPartyId` sehen, bedeutet dies, dass die externe ID von Braze durch den in Oracle Crowdtwist gespeicherten Wert `third_party_id` festgelegt wird. Weitere Informationen über das Schema oder den Aufbau der Objekte von Oracle Crowdtwist finden Sie in der [Dokumentation von Oracle](https://docs.oracle.com/en/cloud/saas/marketing/crowdtwist-develop/Developers/LivePushUserActivity.html).
{% endalert %}

{% alert important %}
 Verwenden Sie die von Oracle Crowdtwist gesendeten Objekte, um Nutzer:innen in Braze zu erstellen. Wenn Sie den Schlüssel `update_existing_only` mit dem Wert `false` einfügen und ein Attribut- oder Event-Objekt einen Bezeichner enthält, der in Braze nicht existiert, erstellt Braze ein Nutzerprofil mit den Attributen, die im Event- oder Attributobjekt enthalten sind. Wenn Sie es vorziehen, dass Oracle Crowdtwist nur Profile aktualisiert, die bereits in Braze existieren, setzen Sie dieses Attribut in jedem Attribut- oder Event-Objekt auf `true`.
{% endalert %}

### Templates zur Datentransformation {#data-transformation-templates}
{% tabs %}
{% tab User Profile Event Template%}
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
 //The "tierinfo_current_level" attribute is a flat Braze custom attribute, while "tierInfo" below is a nested object mirroring the Crowdtwist payload; the difference in capitalization is intentional.
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

Die Templates in diesem Leitfaden sind für das Ziel „Nutzer:innen tracken“ erstellt, aber Sie können Ihr Template so gestalten, dass es an jeden der Endpunkte gesendet wird, die in der [Anleitung zur Datentransformation von Braze]({{site.baseurl}}/user_guide/data/data_transformation/creating_a_transformation/#step-2-create-a-transformation) aufgeführt sind, mit Unterstützung der zugehörigen [REST API-Dokumentation]({{site.baseurl}}/api/home/).

### Testen {#testing}

Nachdem Sie das Template nach Ihren Wünschen angepasst haben, müssen Sie überprüfen, ob es korrekt funktioniert. Klicken Sie auf „Validieren“, um eine Vorschau der Ausgabe Ihres Codes zu erhalten und zu prüfen, ob die Anfrage für das gewählte Ziel akzeptabel ist.

![Screenshot der Braze-Datentransformations-UI]({% image_buster /assets/img/crowdtwist_tools/screenshot.png %}){: style="max-width:70%;margin-bottom:15px;border:none;"}

Wenn Sie mit dem Objekt, das Sie im Feld „Ausgabe“ sehen, zufrieden sind, klicken Sie auf **Aktivieren**, damit der Datentransformations-Endpunkt bereit ist, Daten zu empfangen.

Die Webhook-URL Ihrer Datentransformation finden Sie im Panel auf der linken Seite. Kopieren Sie diese und verwenden Sie sie für die Konfiguration innerhalb des Integration Hub von Oracle Crowdtwist.

{% alert important %}
Die Braze-Datentransformations-Endpunkte haben ein Rate-Limit von 1000 Anfragen pro Minute. Überlegen Sie, wie schnell Sie diese Daten in Braze zur Verfügung stellen möchten, und sprechen Sie mit Ihrem Braze Account Manager, wenn Sie ein höheres Rate-Limit für die Datentransformation benötigen.
{% endalert %}

Datentransformationen sind ein sehr dynamisches Werkzeug, und Sie können sie für Zwecke entwerfen, die über die in diesem Dokument beschriebenen hinausgehen – mit JavaScript-Kenntnissen und der Unterstützung unserer REST API-Dokumentation. Wenn Sie Unterstützung oder Fehlerbehebung für komplexe Änderungen an Ihren Datentransformations-Templates benötigen, wenden Sie sich an Ihren Customer-Success-Manager, um zu erfahren, welche Hilfestellungen Ihnen zur Verfügung stehen.