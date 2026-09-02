---
nav_title: Nutzer-IDs festlegen
article_title: Nutzer-IDs festlegen
page_order: 1.1
description: "Erfahren Sie, wie Sie Nutzer-IDs über das Braze SDK or Software-Development-Kit festlegen."
---

# Nutzer-IDs festlegen {#set-user-ids}

> Erfahren Sie, wie Sie Nutzer-IDs über das Braze SDK or Software-Development-Kit festlegen. Dabei handelt es sich um eindeutige Bezeichner, mit denen Sie Nutzer:innen geräte- und plattformübergreifend tracken, ihre Daten über die [Nutzerdaten-API]({{site.baseurl}}/api/endpoints/user_data) importieren und gezielte Nachrichten über die [Messaging-API]({{site.baseurl}}/api/endpoints/messaging) versenden können. Wenn Sie einer Nutzer:in keine eindeutige ID zuweisen, weist Braze stattdessen eine anonyme ID zu. Solange Sie dies nicht tun, können Sie diese Features jedoch nicht nutzen.

{% alert note %}
Für Wrapper-SDKs, die nicht aufgeführt sind, verwenden Sie stattdessen die entsprechende native Android- oder Swift-Methode.
{% endalert %}

## Über anonyme Nutzer:innen {#about-anonymous-users}

{% multi_lang_include anonymous_users/about_anonymous_users.md %}

### Anonymes Nutzer:innen-Tracking verhindern {#preventing-anonymous-user-tracking}

Wenn Ihr Anwendungsfall erfordert, dass keine Daten erfasst werden, bevor ein:e Nutzer:in identifiziert ist, können Sie die Initialisierung des Braze SDK or Software-Development-Kit verzögern, bis sich die Nutzer:in anmeldet und eine `external_id` verfügbar ist. Setzen Sie ein Flag in Ihrem Code, das auf `true` wechselt, wenn sich die Nutzer:in anmeldet, und initialisieren Sie das SDK or Software-Development-Kit erst, wenn dieses Flag gesetzt ist.

{% alert warning %}
Verzögern Sie die Initialisierung nur beim **ersten Mal**, wenn ein:e Nutzer:in Ihre App herunterlädt (bevor eine `external_id` gesetzt wurde). Wenn Sie verhindern, dass das SDK or Software-Development-Kit bei jeder Abmeldung oder bei jedem neuen Sitzungsstart initialisiert wird, beeinträchtigt dies das Vorladen von In-App-Nachrichten und Content-Card-Assets, was zu Zustellbarkeitsfehlern für diese Campaigns führen kann.
{% endalert %}

## Nutzer-ID festlegen {#setting-a-user-id}

Um eine Nutzer-ID festzulegen, rufen Sie die Methode `changeUser()` auf, nachdem sich die Nutzer:in erstmalig angemeldet hat. IDs sollten eindeutig sein und unseren [Best Practices für die Benennung](#naming-best-practices) folgen.

Wenn Sie stattdessen einen eindeutigen Bezeichner hashen, stellen Sie sicher, dass Sie die Eingabe Ihrer Hash-Funktion normalisieren. Entfernen Sie beispielsweise beim Hashen einer E-Mail-Adresse alle führenden oder nachgestellten Leerzeichen und berücksichtigen Sie die Lokalisierung.

{% tabs local %}
{% tab WEB %}
Für eine Standard-Internet-SDK or Software-Development-Kit-Implementierung können Sie die folgende Methode verwenden:

```javascript
braze.changeUser(YOUR_USER_ID_STRING);
```

Wenn Sie stattdessen Google Tag Manager:in verwenden möchten, können Sie den Tag-Typ **Change User** verwenden, um die [`changeUser`-Methode](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser) aufzurufen. Verwenden Sie ihn immer dann, wenn sich eine Nutzer:in anmeldet oder anderweitig mit dem eindeutigen `external_id`-Bezeichner identifiziert wird.

Geben Sie die eindeutige ID der aktuellen Nutzer:in im Feld **External User ID** ein, das in der Regel über eine von Ihrer Website gesendete Datenschichtvariable befüllt wird.

![Ein Dialogfeld mit den Konfigurationseinstellungen für den Braze Action Tag. Zu den Einstellungen gehören „tag type“ und „external user ID“.]({% image_buster /assets/img/web-gtm/gtm-change-user.png %})
{% endtab %}

{% tab ANDROID %}
{% subtabs %}
{% subtab JAVA %}
```java
Braze.getInstance(context).changeUser(YOUR_USER_ID_STRING);
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
Braze.getInstance(context).changeUser(YOUR_USER_ID_STRING)
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab SWIFT %}
{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.changeUser(userId: "YOUR_USER_ID")
```
{% endsubtab %}
{% subtab objective-c %}
```objc
[AppDelegate.braze changeUser:@"YOUR_USER_ID_STRING"];
```
{% endsubtab %}
{% endsubtabs %}

{% alert note %}
`changeUser` reiht den Nutzerwechsel in die Warteschlange ein und kehrt sofort im aufrufenden Thread zurück. Alle danach auf `braze.user` aufgerufenen Attribut-Setter werden automatisch hinter den von `changeUser` initiierten Operationen serialisiert. Das Lesen von `braze.user.id` blockiert den aufrufenden Thread, bis der Nutzerwechsel vollständig abgeschlossen ist. Verwenden Sie für Main-Thread- oder latenzsensitive Kontexte stattdessen die nicht-blockierenden Alternativen.

{% subtabs local %}
{% subtab Swift %}
```swift
// Completion handler — always delivers on the main thread.
AppDelegate.braze?.user.getId { userId in
  print("User ID:", userId ?? "anonymous")
}

// Async/await (iOS 13.0+, tvOS 13.0+, watchOS 6.0+, macOS 10.15+)
let userId = await AppDelegate.braze?.user.getId()
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
// Completion handler — always delivers on the main thread.
[AppDelegate.braze.user getIdWithCompletion:^(NSString * _Nullable userId) {
  NSLog(@"User ID: %@", userId ?: @"anonymous");
}];
```
{% endsubtab %}
{% endsubtabs local %}
{% endalert %}
{% endtab %}

{% tab CORDOVA %}
```javascript
BrazePlugin.changeUser("YOUR_USER_ID");
```
{% endtab %}

{% tab ROKU %}
```brightscript
m.Braze.setUserId(YOUR_USER_ID_STRING)
```
{% endtab %}

{% tab UNITY %}
```csharp
AppboyBinding.ChangeUser("YOUR_USER_ID_STRING");
```
{% endtab %}

{% tab REACT NATIVE %}
```javascript
Braze.changeUser("YOUR_USER_ID_STRING");
```
{% endtab %}
{% endtabs %}

### So funktioniert `changeUser()` {#how-changeuser-works}

Wenn Sie `changeUser()` aufrufen, gelten die folgenden Verhaltensweisen:

- Der Aufruf von `changeUser()` mit **derselben** Nutzer-ID, die bereits festgelegt ist, hat keine Auswirkung auf die Sitzungsanzahl.
- Der Aufruf von `changeUser()` mit einer **anderen** Nutzer-ID beendet automatisch die aktuelle Sitzung und startet eine neue.
- Wenn eine anonyme Nutzer:in `changeUser()` mit einer **neuen** Nutzer-ID aufruft (eine, die in Braze noch nicht existiert), werden die Daten des anonymen Profils mit dem neuen identifizierten Profil zusammengeführt.
- Wenn eine anonyme Nutzer:in `changeUser()` mit einer **vorhandenen** Nutzer-ID aufruft, werden die Daten des anonymen Profils nicht mit dem identifizierten Profil zusammengeführt.

{% alert note %}
Der Aufruf von `changeUser()` löst im Rahmen des Schließens der Sitzung der aktuellen Nutzer:in einen Daten-Flush aus. Das SDK or Software-Development-Kit sendet automatisch alle ausstehenden Daten der vorherigen Nutzer:in, bevor zur neuen Nutzer:in gewechselt wird. Sie müssen daher keinen manuellen Daten-Flush vor dem Aufruf von `changeUser()` anfordern.
{% endalert %}

{% alert warning %}
Weisen Sie nicht eine einzelne, gemeinsam genutzte Nutzer-ID zu (zum Beispiel eine statische Standard-externe-ID) und rufen Sie `changeUser()` nicht auf, wenn sich eine Nutzer:in abmeldet. Andernfalls können Sie zuvor angemeldete Nutzer:innen auf gemeinsam genutzten Geräten nicht erneut ansprechen, und alle Daten werden unter einer einzigen Nutzer-ID protokolliert, was dazu führen kann, dass andere Features nicht wie erwartet funktionieren. Verfolgen Sie stattdessen alle Nutzer-IDs separat und stellen Sie sicher, dass der Abmeldevorgang Ihrer App den Wechsel zurück zu einer zuvor angemeldeten Nutzer:in ermöglicht. Wenn eine neue Sitzung beginnt, aktualisiert Braze automatisch die Daten für das neu aktive Profil.
{% endalert %}

## Nutzer-Aliase {#user-aliases}

### Funktionsweise {#how-they-work}

{% multi_lang_include anonymous_users/about_user_aliases.md %}

### Einen Nutzer-Alias festlegen {#setting-a-user-alias}

Ein Nutzer-Alias besteht aus zwei Teilen: einem Namen und einer Bezeichnung. Der Name bezieht sich auf den Bezeichner selbst, während die Bezeichnung den Typ des Bezeichners angibt, zu dem er gehört. Wenn Sie beispielsweise eine:n Nutzer:in in einer Drittanbieter-Kundensupport-Plattform mit der externen ID `987654` haben, können Sie dieser Person in Braze einen Alias mit dem Namen `987654` und der Bezeichnung `support_id` zuweisen, um sie plattformübergreifend zu tracken.

{% tabs local %}
{% tab web %}
```javascript
braze.getUser().addAlias(ALIAS_NAME, ALIAS_LABEL);
```
{% endtab %}

{% tab android %}
{% subtabs %}
{% subtab java %}
```java
Braze.getInstance(context).getCurrentUser().addAlias(ALIAS_NAME, ALIAS_LABEL);
```
{% endsubtab %}

{% subtab kotlin %}
```kotlin
Braze.getInstance(context).currentUser?.addAlias(ALIAS_NAME, ALIAS_LABEL)
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab swift %}
{% subtabs %}
{% subtab swift %}
```swift
Appboy.sharedInstance()?.user.addAlias(ALIAS_NAME, ALIAS_LABEL)
```
{% endsubtab %}

{% subtab objective-c %}
```objc
 [[Appboy sharedInstance].user addAlias:ALIAS_NAME withLabel:ALIAS_LABEL];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Representational State Transfer api %}
```json
{
  "alias_name" : (required, string),
  "alias_label" : (required, string)
}
```
{% endtab %}

{% tab react native %}
```javascript
Braze.addAlias("ALIAS_NAME", "ALIAS_LABEL");
```
{% endtab %}
{% endtabs %}

## Best Practices für die ID-Benennung {#naming-best-practices}

Wir empfehlen Ihnen, Nutzer-IDs nach dem [UUID-Standard (Universally Unique Identifier)](https://en.wikipedia.org/wiki/Universally_unique_identifier) zu erstellen, d. h. es handelt sich um 128-Bit-Strings, die zufällig und gut verteilt sind.

Alternativ können Sie einen vorhandenen eindeutigen Bezeichner (z. B. einen Namen oder eine E-Mail-Adresse) hashen, um Ihre Nutzer-IDs zu generieren. Wenn Sie dies tun, stellen Sie sicher, dass Sie eine [SDK or Software-Development-Kit-Authentifizierung]({{site.baseurl}}/developer_guide/sdk_integration/authentication) implementieren, damit Sie einen Identitätswechsel verhindern können.

{% alert warning %}
Verwenden Sie für Ihre Nutzer-ID keine leicht zu erratenden Werte oder fortlaufende Zahlen. Dies könnte Ihr Unternehmen böswilligen Angriffen oder Datenexfiltration aussetzen.

Für zusätzliche Sicherheit verwenden Sie die [SDK or Software-Development-Kit-Authentifizierung]({{site.baseurl}}/developer_guide/sdk_integration/authentication).
{% endalert %}

Es ist zwar wichtig, dass Sie Ihre Nutzer-IDs von Anfang an richtig benennen, aber Sie können sie in Zukunft jederzeit mit dem [`/users/external_ids/rename`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration)-Endpunkt umbenennen.

| Nicht empfohlene ID-Typen | Nicht empfohlenes Beispiel |
| ------------ | ----------- |
| Sichtbare Profil-ID oder Nutzername | JonDoe829525552 |
| E-Mail-Adresse | Anna@email.com |
| Automatisch inkrementierende Nutzer-ID | 123 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Best Practices für die ID-Benennung" }

{% alert warning %}
Vermeiden Sie es, Details darüber preiszugeben, wie Sie Nutzer-IDs erstellen, da dies Ihr Unternehmen böswilligen Angriffen oder Datenexfiltration aussetzen könnte.
{% endalert %}