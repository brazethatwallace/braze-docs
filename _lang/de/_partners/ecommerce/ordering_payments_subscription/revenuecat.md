---
nav_title: RevenueCat
article_title: RevenueCat
description: "Die Integration von RevenueCat und Braze ermöglicht es Ihnen, die Kauf-Events und Abo-Lebenszyklen Ihrer Kund:innen automatisch plattformübergreifend zu synchronisieren. So können Sie Campaigns erstellen, die auf die Phase des Abo-Lebenszyklus Ihrer Kund:innen reagieren, z. B. die Ansprache von Kund:innen, die sich während der kostenlosen Testphase abgemeldet haben, oder das Versenden von Erinnerungen an Kund:innen mit Rechnungsproblemen."
alias: /partners/revenuecat/
page_type: partner
search_tag: Partner

---

# RevenueCat

> [RevenueCat](https://www.revenuecat.com/) ist die einzige Quelle der Wahrheit für Ihren Abo-Status auf iOS, Android und im Internet. Ganz gleich, ob Sie eine neue App entwickeln oder bereits Millionen von Abonnent:innen haben, mit RevenueCat können Sie plattformübergreifende In-App-Käufe erstellen, Ihre Produkte und Abonnent:innen verwalten und Ihre Daten analysieren – ganz ohne Server-Code.

_Diese Integration wird von RevenueCat gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von RevenueCat und Braze ermöglicht es Ihnen, die Kauf-Events und Abo-Lebenszyklen Ihrer Kund:innen automatisch plattformübergreifend zu synchronisieren. So können Sie Campaigns erstellen, die auf die Phase des Abo-Lebenszyklus Ihrer Kund:innen reagieren, z. B. die Ansprache von Kund:innen, die sich während der kostenlosen Testphase abgemeldet haben, oder das Versenden von Erinnerungen an Kund:innen mit Rechnungsproblemen.

## Voraussetzungen {#prerequisites}

Zumindest müssen Sie die Integration über das RevenueCat-Dashboard aktivieren, um RevenueCat mit Braze zu verbinden. Wenn Sie das Braze SDK or Software-Development-Kit verwenden, können Sie die SDKs von RevenueCat und Braze zusammen verwenden, um die Integration zu verbessern, indem Sie sicherstellen, dass in beiden Systemen derselbe Bezeichner für die Kund:innen verwendet wird.

| Anforderung | Beschreibung |
|---|---|
| RevenueCat-Konto und -App | Ein [RevenueCat-Konto](https://app.revenuecat.com/login) ist erforderlich, um die Vorteile dieser Partnerschaft zu nutzen. Sie müssen außerdem über eine konfigurierte RevenueCat-App verfügen. |
| RevenueCat SDK or Software-Development-Kit | Wir empfehlen, zusätzlich zum erforderlichen Braze SDK or Software-Development-Kit das [RevenueCat SDK or Software-Development-Kit](https://docs.revenuecat.com/docs/configuring-sdk) zu installieren, um Nutzer-Aliase an RevenueCat zu übermitteln. |
| Braze-Instanz | Ihre Braze-Instanz erhalten Sie von Ihrer/Ihrem Braze-Onboarding-Manager:in:in oder auf der [API-Übersichtsseite]({{site.baseurl}}/api/basics#endpoints).<br><br>RevenueCat benötigt die Braze-Instanz, um serverseitig an den richtigen Braze-Representational State Transfer-Endpunkt zu senden. |
| Braze-Representational State Transfer-API-Schlüssel | Ein Braze-Representational State Transfer-API-Schlüssel mit `users.track`-Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze-Test-Representational State Transfer-API-Schlüssel (optional) | Ein Test-API-Schlüssel kann für Test- und Produktionskäufe verwendet werden, wenn Sie möchten, dass diese Anfragen an separate Braze-Instanzen gesendet werden. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Anwendungsfälle {#use-cases}

- Trigger or triggern or triggern Sie eine Onboarding-Campaign, die Ihre Premium-Features hervorhebt, wenn Kund:innen eine kostenlose Testversion starten.
- Senden Sie eine Erinnerung zur Aktualisierung der Abrechnungsinformationen, wenn ein Ereignis „Abrechnungsproblem“ empfangen wird.
- Senden Sie eine Umfrage, nachdem Kund:innen eine kostenlose Testversion gekündigt haben.

## Integration

### Schritt 1: Braze-Nutzer:innen-Identität festlegen {#step-1-set-braze-user-identity}

Im Braze SDK or Software-Development-Kit können Sie die Braze-Nutzer-ID so einstellen, dass sie mit der RevenueCat-App-Nutzer-ID übereinstimmt. So wird sichergestellt, dass die von Braze und RevenueCat gesendeten Ereignisse mit denselben Nutzer:innen synchronisiert werden können.

Konfigurieren Sie das Braze SDK or Software-Development-Kit mit derselben App-Nutzer-ID wie RevenueCat oder verwenden Sie die Braze-SDK or Software-Development-Kit-Methode `.changeUser()`.

{% tabs local %}
{% tab swift %}
```swift
// Configure Purchases SDK
Purchases.configure(withAPIKey: "public_sdk_key", appUserID: "my_app_user_id")

// Change user in Braze SDK
Appboy.sharedInstance()?.changeUser("my_app_user_id")

// Optional User Alias Object attributes
Purchases.shared.setAttributes(["$brazeAliasName" : "name",
                             "$brazeAliasLabel" : "label"])
```
{% endtab %}
{% tab objective-c %}
```objc
// Configure Purchases SDK
[RCPurchases configureWithAPIKey:@"public_sdk_key" appUserID:@"my_app_user_id"];

// Change user in Braze SDK
[[Appboy sharedInstance] changeUser:@"my_app_user_id"];

// Optional User Alias Object attributes
[[RCPurchases sharedPurchases] setAttributes:@{
    @"$brazeAliasName": @"name",
    @"$brazeAliasLabel": @"label"
}];
```
{% endtab %}
{% tab java %}
```java
// Configure Purchases SDK
Purchases.configure(this, "public_sdk_key", "my_app_user_id");

// Change user in Braze SDK
Braze.getInstance(context).changeUser(my_app_user_id);

// Optional User Alias Object attributes
Map<String, String> attributes = new HashMap<String, String>();
attributes.put("$brazeAliasName", "name");
attributes.put("$brazeAliasLabel", "label");

Purchases.getSharedInstance().setAttributes(attributes);
```
{% endtab %}
{% endtabs %}

#### Nutzer-Alias-Objekt an Braze senden (optional) {#send-user-alias-object-to-braze-optional}

Wenn Sie einen alternativen eindeutigen Bezeichner senden möchten, der sich von der RevenueCat-App-Nutzer-ID unterscheidet, Update or aktualisieren or aktualisieren Sie die Nutzer:innen mit den folgenden Daten als RevenueCat-Abonnent:innen-Attribute.

| Schlüssel | Beschreibung |
|---|---|
| `$brazeAliasName` | Der Braze-`alias_name` im [Nutzer-Alias-Objekt]({{site.baseurl}}/api/objects_filters/user_alias_object) |
| `$brazeAliasLabel` | Das Braze-`alias_label` im [Nutzer-Alias-Objekt]({{site.baseurl}}/api/objects_filters/user_alias_object) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Nutzer-Alias-Objekt an Braze senden (optional)" }

Beide Attribute sind erforderlich, damit das [Nutzer-Alias-Objekt]({{site.baseurl}}/api/objects_filters/user_alias_object) zusammen mit Ihren Ereignisdaten gesendet werden kann. Diese Eigenschaften können manuell eingestellt werden, wie jedes andere [RevenueCat-Abonnent:innen-Attribut](https://docs.revenuecat.com/docs/subscriber-attributes). Beispiele für Code-Snippets finden Sie in Schritt 1.

### Schritt 2: RevenueCat-Ereignisse an Braze senden {#step-2-send-revenuecat-events-to-braze}

Nachdem Sie das RevenueCat-Purchases-SDK or Software-Development-Kit und das Braze SDK or Software-Development-Kit so eingerichtet haben, dass sie dieselbe Nutzer:innen-Identität verwenden, können Sie die Integration einschalten und die Ereignisnamen über das RevenueCat-Dashboard konfigurieren.

1. Navigieren Sie zu Ihrem Projekt im RevenueCat-Dashboard und suchen Sie im Navigationsmenü die Karte **Integrations**. Wählen Sie **+ New**.
2. Wählen Sie als Nächstes **Braze** aus den verfügbaren Integrationen aus und fügen Sie Ihre Braze-Instanz und Ihren Braze-Representational State Transfer-API-Schlüssel hinzu.
3. Geben Sie die Ereignisnamen ein, die RevenueCat senden soll, oder wählen Sie die Standard-Ereignisnamen. Weitere Einzelheiten zu den verfügbaren Ereignissen finden Sie in [Schritt 3](#configure-event-names).
4. Wählen Sie aus, ob RevenueCat den Erlös (nach dem App-Shop-Anteil) oder den Umsatz (Bruttoumsatz) melden soll.

![Braze-Einstellungen in RevenueCat mit Feldern für Braze-Instanz, API-Schlüssel-Bezeichner und Sandbox-Bezeichner.]({% image_buster /assets/img/revenuecat/braze_settings_in_revenuecat.png %})

### Schritt 3: Ereignisnamen konfigurieren {#configure-event-names}

Geben Sie die Ereignisnamen ein, die RevenueCat senden soll, oder wählen Sie aus den Standard-Ereignisnamen, indem Sie **Use Default Event Names** auswählen. Die Ereignisse, deren Versand RevenueCat unterstützt, werden in der folgenden Tabelle beschrieben.

| Ereignis | Beschreibung |
|---|---|
| Erster Kauf | Der erste Kauf eines sich automatisch verlängernden Abo-Produkts, das keine kostenlose Testversion enthält. |
| Testversion gestartet | Der Beginn einer kostenlosen Testversion eines sich automatisch verlängernden Abo-Produkts. |
| Testversion konvertiert | Wenn ein sich automatisch verlängerndes Abo-Produkt von einer kostenlosen Testphase in eine normale bezahlte Phase übergeht. |
| Testversion abgebrochen | Wenn Nutzer:innen die Verlängerung eines sich automatisch verlängernden Abo-Produkts während einer kostenlosen Testphase deaktivieren. |
| Verlängerung | Wenn ein sich automatisch verlängerndes Abo-Produkt erneuert wird oder Nutzer:innen das sich automatisch verlängernde Abo-Produkt nach einer Unterbrechung erneut erwerben. |
| Stornierung | Wenn Nutzer:innen die Verlängerung eines sich automatisch verlängernden Abo-Produkts während des normalen Bezahlzeitraums deaktivieren. |
| Kauf ohne Abo | Der Kauf eines Produkts, das kein automatisch verlängerndes Abo ist. |
| Ablauf | Wenn ein Abo ausläuft. |
| Abrechnungsproblem | Wenn es beim Versuch, Nutzer:innen zu belasten, ein Problem gegeben hat. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 3: Ereignisnamen konfigurieren" }

Bei Ereignissen, die Umsatz beinhalten, zeichnet RevenueCat diesen Betrag automatisch zusammen mit dem Ereignis in Braze auf, z. B. bei Conversions von Testversionen und Verlängerungen.

## Verwendung dieser Integration {#using-this-integration}

Nachdem Sie die Braze-Einstellungen in RevenueCat konfiguriert haben, fließen die Ereignisse automatisch von RevenueCat zu Braze, ohne dass Sie weitere Maßnahmen ergreifen müssen.

## Anpassung {#customization}

### Sandbox-API-Schlüssel zum Testen hinzufügen {#add-a-sandbox-api-key-for-testing}

Wenn Sie RevenueCat nur einen Braze-Representational State Transfer-API-Schlüssel zur Verfügung stellen, werden nur Produktionsereignisse gesendet. Wenn Sie auch Sandbox-Testereignisse senden möchten, [erstellen Sie einen weiteren Braze-Representational State Transfer-API-Schlüssel]({{site.baseurl}}/api/basics#creating-rest-api-keys) und fügen Sie ihn zu Ihren Braze-Einstellungen in RevenueCat hinzu.