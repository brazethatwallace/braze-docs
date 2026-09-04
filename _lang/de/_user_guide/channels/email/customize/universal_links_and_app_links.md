---
nav_title: "Universal Links und App Links"
article_title: "Universal Links und App Links"
page_order: 6.4
page_type: reference
description: "Dieser Artikel beschreibt, wie Sie Apple Universal Links und Android App Links einrichten."
channel: email
---

# Universal Links und App Links {#universal-links-and-app-links}

> Dieser Artikel beschreibt, wie Sie Apple Universal Links und Android App Links einrichten.

{% alert tip %}
Einen Vergleich der Link-Typen über alle Messaging-Kanäle hinweg und eine Anleitung, wann Sie eine AASA-Datei benötigen, finden Sie im [iOS-Deeplinking-Leitfaden]({{site.baseurl}}/developer_guide/push_notifications/ios_deep_linking_guide).
{% endalert %}

Apple Universal Links und Android App Links sind Mechanismen, die einen nahtlosen Übergang zwischen Web-Inhalten und mobilen Apps ermöglichen. Während Universal Links spezifisch für iOS sind, erfüllen Android App Links denselben Zweck für Android-Anwendungen.

## So funktionieren Universal Links und App Links {#how-universal-links-and-app-links-work}

Universal Links (iOS) und App Links (Android) sind Standard-Weblinks (`http://mydomain.com`), die sowohl auf eine Webseite als auch auf einen Inhalt innerhalb einer App verweisen.

Wenn ein Universal Link oder App Link geöffnet wird, prüft das Betriebssystem, ob eine installierte App für diese Domain registriert ist. Wird eine App gefunden, wird sie sofort gestartet, ohne die Webseite zu laden. Wird keine App gefunden, wird die Web-URL im Standard-Webbrowser der Nutzer:innen geladen, der auch so konfiguriert sein kann, dass er in den App Store bzw. Google Play Store weiterleitet.

Einfach ausgedrückt ermöglichen Universal Links einer Website, ihre Webseiten mit bestimmten App-Bildschirmen zu verknüpfen. Wenn Nutzer:innen also auf einen Link zu einer Webseite klicken, die einem App-Bildschirm entspricht, kann die App direkt geöffnet werden (sofern die App aktuell installiert ist).

{% alert important %}
Firebase Dynamic Links ist veraltet. Braze verfügt über keine direkte Integration mit Firebase, und Deeplinking wird außerhalb der Braze-Plattform verwaltet. Migrieren Sie zu plattformnativen Lösungen (Apple Universal Links und Android App Links, wie in diesem Artikel beschrieben) oder zu alternativen Deeplinking-Anbietern. Informationen zur Migration finden Sie in den [FAQ zur Firebase-Migration](https://firebase.google.com/support/dynamic-links-faq).
{% endalert %}

Diese Tabelle zeigt die wichtigsten Unterschiede zwischen Universal Links und herkömmlichen Deeplinks:

|                        | Universal Links und App Links                                  | Deeplinks                   |
| ---------------------- | -------------------------------------------------------------- | ---------------------------- |
| Plattformkompatibilität | iOS (Version 9 und höher) und Android (Version 6.0 und höher) | Wird in verschiedenen mobilen Betriebssystemen verwendet |
| Zweck                  | Nahtlose Verknüpfung von Web- und App-Inhalten auf iOS- und Android-Geräten | Verknüpfung mit bestimmten App-Inhalten |
| Funktion               | Leitet je nach Kontext zu Webseiten oder App-Inhalten weiter   | Öffnet bestimmte App-Bildschirme |
| App-Installation       | Öffnet die App, wenn sie installiert ist, andernfalls werden Webinhalte geöffnet | Erfordert eine installierte App |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="So funktionieren Universal Links und App Links" }

## Anwendungsfälle {#use-cases}

Universal Links und App Links werden am häufigsten für E-Mail-Campaigns verwendet, da E-Mails sowohl auf Desktop- als auch auf Mobilgeräten geöffnet und angeklickt werden können.

Einige Kanäle funktionieren mit diesen Links nicht gut. Beispielsweise sollten Push-Benachrichtigungen, In-App-Nachrichten und Content Cards schemabasierte Deeplinks (`mydomain://`) verwenden.

{% alert note %}
Android App Links erfordern einen angepassten `IBrazeDeeplinkHandler` mit Logik, um Links von deren Domains getrennt von anderen Web-URLs zu verarbeiten. Es kann einfacher sein, stattdessen Deeplinks zu verwenden und die Verlinkungspraktiken für andere Kanäle als E-Mail einheitlich zu halten.
{% endalert %}

## Voraussetzungen {#prerequisites}

Um Universal Links und App Links zu verwenden:

- Ihre Website muss über HTTPS zugänglich sein
- Ihre App muss im App Store (iOS) oder Google Play Store (Android) verfügbar sein

## Einrichtung von Universal Links und App Links {#setting-up-universal-links-and-app-links}

Damit Apps Universal Links oder App Links unterstützen, ist sowohl für iOS als auch für Android eine spezielle Berechtigungsdatei erforderlich, die auf der Link-Domain gehostet wird. Diese Datei enthält Definitionen darüber, welche Apps Links von dieser Domain öffnen dürfen und – bei iOS – welche Pfade diese Apps öffnen dürfen:

- **iOS:** Apple App Site Association (AASA)-Datei
- **Android:** Digital Asset Links-Datei

Zusätzlich zu dieser Berechtigungsdatei gibt es fest codierte Definitionen, welche Link-Domains die App öffnen darf. Diese werden innerhalb der App konfiguriert:

- **iOS:** Als „Associated Domains“ in Xcode festgelegt
- **Android:** In der `AndroidManifest.xml`-Datei der App definiert

Diese zweiseitige Domain-App-Verknüpfung ist erforderlich, damit ein Universal Link oder App Link funktioniert, und verhindert, dass eine beliebige App Links von einer bestimmten Domain übernimmt oder eine beliebige Domain eine bestimmte App öffnet.

{% tabs %}
<!--iOS instructions-->
{% tab iOS %}

Diese Schritte sind aus der Apple-Entwicklerdokumentation adaptiert. Weitere Informationen finden Sie unter [Allowing apps and websites to link to your content](https://developer.apple.com/documentation/xcode/allowing-apps-and-websites-to-link-to-your-content?language=objc).

### Schritt 1: App-Berechtigungen konfigurieren {#step-1-configure-your-app-entitlements}

{% alert note %}
[Ab Xcode 13](https://developer.apple.com/help/account/reference/provisioning-with-managed-capabilities/) kann Xcode die Berechtigungsbereitstellung automatisch für Sie übernehmen. Sie können voraussichtlich direkt zu [Schritt&nbsp;1c](#step-1c) springen und bei Problemen auf diese Anleitung zurückkommen.
{% endalert %}

#### Schritt 1a: App registrieren {#step-1a}

1. Rufen Sie developer.apple.com auf und melden Sie sich an.
2. Klicken Sie auf **Certificates, Identifiers & Profiles**.
3. Klicken Sie auf **Identifiers**.
4. Wenn Sie noch keinen registrierten App Identifier haben, klicken Sie auf +, um einen zu erstellen.
   a. Geben Sie einen **Name** ein. Dieser kann beliebig gewählt werden.
   b. Geben Sie die **Bundle ID** ein. Sie finden Ihre Bundle ID im Tab **General** Ihres Xcode-Projekts für das entsprechende Build-Target.

#### Schritt 1b: Associated Domains in Ihrem App Identifier aktivieren {#step-1b-turn-on-associated-domains-in-your-app-identifier}

1. Suchen Sie in Ihrem bestehenden oder neu erstellten App Identifier den Abschnitt **App Services**.
2. Wählen Sie **Associated Domains** aus.
3. Klicken Sie auf **Save**.

![Abschnitt „App Services“]({% image_buster /assets/img_archive/universal_links_1b.png %}){: style="max-width:75%;"}

#### Schritt 1c: Associated Domains in Ihrem Xcode-Projekt aktivieren {#step-1c}

Stellen Sie vor dem Fortfahren sicher, dass in Ihrem Xcode-Projekt dasselbe Team ausgewählt ist, unter dem Sie gerade Ihren App Identifier registriert haben.

1. Öffnen Sie in Xcode den Tab **Capabilities** Ihrer Projektdatei.
2. Aktivieren Sie **Associated Domains**.

##### Tipp zur Fehlerbehebung {#troubleshooting-tip}

Wenn der Fehler „An App ID with Identifier 'your-app-id' is not available. Please enter a different string“ angezeigt wird, gehen Sie wie folgt vor:

1. Überprüfen Sie, ob das richtige Team ausgewählt ist.
2. Stellen Sie sicher, dass die Bundle ID ([Schritt 1a](#step-1a)) Ihres Xcode-Projekts mit der beim Registrieren des App Identifiers verwendeten übereinstimmt.

#### Schritt 1d: Domain-Berechtigung hinzufügen {#step-1d-add-the-domain-entitlement}

Fügen Sie im Abschnitt „Domains“ den entsprechenden Domain-Tag hinzu. Er muss das Präfix `applinks:` haben. In diesem Fall wurde `applinks:yourdomain.com` hinzugefügt.

![Abschnitt „Associated Domains“]({% image_buster /assets/img_archive/universal_links_1d.png %})

#### Schritt 1e: Bestätigen, dass die Berechtigungsdatei im Build enthalten ist {#step-1e-confirm-that-the-entitlements-file-is-included-at-build}

Stellen Sie im Projektbrowser sicher, dass Ihre neue Berechtigungsdatei unter **Target Membership** ausgewählt ist.

Xcode sollte dies automatisch erledigen.

### Schritt 2: Ihre Website für das Hosting der AASA-Datei konfigurieren {#step-2-configure-your-website-to-host-the-aasa-file}

Um Ihre Website-Domain mit Ihrer nativen App unter iOS zu verknüpfen, müssen Sie die Apple App Site Association (AASA)-Datei auf Ihrer Website hosten. Diese Datei dient als sichere Methode zur Überprüfung des Domain-Eigentums gegenüber iOS. Vor iOS 9 konnten Entwickler:innen jedes beliebige URI-Schema registrieren, um ihre Apps zu öffnen – ohne jegliche Überprüfung. Mit AASA ist dieser Prozess jedoch deutlich sicherer und zuverlässiger geworden.

Die AASA-Datei enthält ein JSON-Objekt mit einer Liste von Apps und den URL-Pfaden auf der Domain, die als Universal Links ein- oder ausgeschlossen werden sollen. Hier ist eine Beispiel-AASA-Datei:

```json
{
  "applinks": {
    "apps": [],
    "details": [
      {
        "appID": "JHGFJHHYX.com.facebook.ios",
        "paths": [
          "*"
        ]
      }
    ]
  }
}
```

- `appID`: Wird zusammengesetzt aus der **Team ID** Ihrer App (rufen Sie `https://developer.apple.com/account/#/membership/` auf, um die Team ID zu erhalten) und dem **Bundle Identifier**. In diesem Beispiel ist „JHGFJHHYX“ die Team ID und „com.facebook.ios“ die Bundle ID.
- `paths`: Ein Array von Strings, das festlegt, welche Pfade in die Verknüpfung ein- oder davon ausgeschlossen werden. Sie können `NOT` vor einem Pfad verwenden, um Pfade zu deaktivieren. In diesem Beispiel werden alle Links auf diesem Pfad im Web geöffnet, anstatt die App zu öffnen. Sie können `*` als Platzhalter verwenden, um alle Pfade in einem Verzeichnis zu aktivieren, und `?`, um ein einzelnes Zeichen abzugleichen (z. B. /archives/201?/, um alle Zahlen von 2010–2019 abzudecken).

{% alert note %}
Diese Strings sind case-sensitive. Abfragestrings und Fragment-Bezeichner werden ignoriert.
{% endalert %}

### Schritt 3: AASA-Datei auf Ihrer Domain hosten {#step-3-host-the-aasa-file-on-your-domain}

Wenn Ihre AASA-Datei fertig ist, können Sie sie auf Ihrer Domain hosten – entweder unter `https://<<yourdomain>>/apple-app-site-association` oder unter `https://<<yourdomain>>/.well-known/apple-app-site-association`.

Laden Sie die Datei `apple-app-site-association` auf Ihren HTTPS-Webserver hoch. Sie können die Datei im Stammverzeichnis Ihres Servers oder im Unterverzeichnis `.well-known` ablegen. Fügen Sie dem Dateinamen kein `.json` hinzu.

{% alert important %}
iOS versucht die AASA-Datei nur über eine sichere Verbindung (HTTPS) abzurufen.
{% endalert %}

Stellen Sie beim Hosting der AASA-Datei sicher, dass die Datei folgende Richtlinien erfüllt:

- Wird über HTTPS bereitgestellt.
- Verwendet den MIME-Typ `application/json`.
- Überschreitet nicht 128 KB (Anforderung ab iOS 9.3.1).

### Schritt 4: Ihre App für die Verarbeitung von Universal Links vorbereiten {#step-4-prepare-your-app-to-handle-universal-links}

Wenn Nutzer:innen auf einem iOS-Gerät auf einen Universal Link tippen, startet das Gerät die App und sendet ihr ein [NSUserActivity](https://developer.apple.com/documentation/foundation/nsuseractivity)-Objekt. Die App kann dann das NSUserActivity-Objekt abfragen, um festzustellen, wie sie gestartet wurde.

Um Universal Links in Ihrer App zu unterstützen, führen Sie die folgenden Schritte aus:

1. Fügen Sie eine Berechtigung hinzu, die die von Ihrer App unterstützten Domains angibt.
2. Aktualisieren Sie Ihren App Delegate, damit er angemessen reagiert, wenn er das NSUserActivity-Objekt empfängt.

Öffnen Sie in Xcode den Abschnitt **Associated Domains** im Tab **Capabilities** und fügen Sie für jede Domain, die Ihre App unterstützt, einen Eintrag mit dem Präfix `applinks:` hinzu. Zum Beispiel: `applinks:www.mywebsite.com`.

{% alert note %}
Apple empfiehlt, diese Liste auf nicht mehr als 20 bis 30 Domains zu beschränken.
{% endalert %}

### Schritt 5: Universal Link testen {#step-5-test-your-universal-link}

Fügen Sie den Universal Link in eine E-Mail ein und senden Sie diese an ein Testgerät. Das direkte Einfügen eines Universal Links in das Safari-URL-Feld führt nicht dazu, dass die App automatisch geöffnet wird. In diesem Fall müssen Sie die Website manuell nach unten ziehen, damit oben eine Aufforderung erscheint, die entsprechende App zu öffnen.

{% endtab %}

<!--Android instructions-->
{% tab Android %}

Diese Schritte sind aus der Android-Entwicklerdokumentation adaptiert. Weitere Informationen finden Sie unter [Add Android App Links](https://developer.android.com/training/app-links#add-app-links) und [Create Deep Links to App Content](https://developer.android.com/training/app-links/deep-linking).

{% alert note %}
Android App Links erfordern einen benutzerdefinierten `IBrazeDeeplinkHandler` mit Logik, um Links von deren Domains getrennt von anderen Web-URLs zu verarbeiten. Es kann einfacher sein, stattdessen Deeplinks zu verwenden und die Verlinkungspraxis für andere Kanäle als E-Mail einheitlich zu halten.
{% endalert %}

### Schritt 1: Deeplinks erstellen {#step-1-create-deep-links}

Zunächst müssen Sie Deeplinks für Ihre Android-App erstellen. Dies kann durch das Hinzufügen von [Intent-Filtern](https://developer.android.com/guide/components/intents-filters) in Ihrer `AndroidManifest.xml`-Datei erfolgen. Der Intent-Filter sollte die Aktion `VIEW` und die Kategorie `BROWSABLE` zusammen mit der URL Ihrer Website im Datenelement enthalten.

### Schritt 2: App mit Ihrer Website verknüpfen {#step-2-associate-your-app-with-your-website}

Sie müssen Ihre App mit Ihrer Website verknüpfen. Dies kann durch das Erstellen einer Digital Asset Links-Datei erfolgen. Diese Datei sollte im JSON-Format vorliegen und Details zu den Android-Apps enthalten, die Links zu Ihrer Website öffnen dürfen. Sie sollte im Verzeichnis `.well-known` Ihrer Website abgelegt werden.

### Schritt 3: App-Manifest-Datei aktualisieren {#step-3-update-your-app-manifest-file}

Fügen Sie in Ihrer `AndroidManifest.xml`-Datei ein Meta-Data-Element innerhalb des Application-Elements hinzu. Das Meta-Data-Element sollte ein `android:name`-Attribut mit dem Wert „asset_statements“ und ein `android:resource`-Attribut haben, das auf eine Ressourcendatei mit einem String-Array verweist, das die URL Ihrer Website enthält.

### Schritt 4: App für die Verarbeitung von Deeplinks vorbereiten {#step-4-prepare-your-app-to-handle-deep-links}

In Ihrer Android-App müssen Sie die eingehenden Deeplinks verarbeiten. Dazu können Sie den Intent abrufen, der Ihre Activity gestartet hat, und die Daten daraus extrahieren.

### Schritt 5: Deeplinks testen {#step-5-testing-your-deep-links}

Abschließend können Sie Ihre Deeplinks testen. Senden Sie sich selbst einen Link über eine Messaging-App oder E-Mail und tippen Sie darauf. Wenn alles korrekt eingerichtet ist, sollte Ihre App geöffnet werden.

{% endtab %}
{% endtabs %}

## Universal Links, App Links und Klick-Tracking {#universal-links-app-links-and-click-tracking}

{% alert note %}
Klick-Tracking-Links werden in der Regel im Rahmen Ihres Onboardings für E-Mail eingerichtet. Wenn dies während des Onboardings nicht abgeschlossen wurde, wenden Sie sich an Ihren Account Manager:in, um Hilfe zu erhalten.
{% endalert %}

Unsere E-Mail-Versandpartner verwenden Klick-Tracking-Domains, um alle Links zu umschließen und URL-Parameter für das Klick-Tracking in Braze-E-Mails einzufügen.

Beispielsweise wird ein Link wie `https://www.example.com` zu etwas wie `https://links.email.example.com/uni/wf/click?upn=abcdef123456…`.

Damit E-Mail-Links mit Klick-Tracking als Universal Links oder App Links funktionieren, müssen Sie einige zusätzliche Konfigurationsschritte durchführen. Stellen Sie sicher, dass Sie die Klick-Tracking-Domain (`links.email.example.com`) als Domain hinzufügen, die die App öffnen darf. Darüber hinaus sollte die Klick-Tracking-Domain die AASA-Datei (iOS) oder Digital Asset Links (Android) bereitstellen. So wird sichergestellt, dass E-Mail-Links mit Klick-Tracking nahtlos funktionieren.

Wenn nicht jeder Klick-Tracking-Link ein Universal Link oder App Link sein soll, können Sie je nach E-Mail-Versandpartner festlegen, welche Links als Universal Links behandelt werden sollen. Weitere Details finden Sie in den folgenden Tabs.

{% tabs %}
{% tab SendGrid %}

So behandeln Sie einen SendGrid-Klick-Tracking-Link als Universal Link:

1. Richten Sie Ihre AASA- oder AndroidManifest-pathPrefix-Werte so ein, dass nur Links mit `/uni/` im URL-Pfad als Universal Links behandelt werden.
2. Fügen Sie das Attribut `universal="true"` zum Anker-Tag (`<a>`) Ihres Links hinzu. Dadurch wird der URL-Pfad des umschlossenen Links so geändert, dass er `/uni/` enthält.

{% alert note %}
Für AMP-E-Mails sollte dieses Attribut data-universal="true" lauten.
{% endalert %}

Zum Beispiel:

```html
<a href=”https://www.example.com” universal="true">
```

{:start="3"}
3. Stellen Sie sicher, dass Ihre App so eingerichtet ist, dass sie die umschlossenen Links korrekt verarbeitet. Lesen Sie den SendGrid-Artikel [Resolving SendGrid click Tracking Links](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-sendgrid-click-tracking-links) und folgen Sie den Schritten für Ihr Betriebssystem. Dieser Artikel enthält Beispielcode für [iOS](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-links-in-ios) und [Android](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-links-in-android).

Mit dieser Konfiguration funktionieren Links mit `/uni/` im URL-Pfad als Universal Links, während alle anderen Links als Web-Links funktionieren.

{% endtab %}
{% tab SparkPost %}

So behandeln Sie einen SparkPost-Klick-Tracking-Link als Universal Link: Fügen Sie das folgende Attribut im Abschnitt „Attribute“ des Drag-and-Drop-Editors für E-Mail hinzu, oder bearbeiten Sie den Link-HTML manuell, um das folgende Attribut im Anker-Tag Ihres Links einzufügen: `data-msys-sublink="custom_path"`.

Dieser angepasste Pfad ermöglicht es Ihnen, URLs mit diesem Wert selektiv als Universal Link zu behandeln.

Zum Beispiel:

```html
<a href=”https://www.example.com” data-msys-sublink="open-in-app">
```

Stellen Sie dann sicher, dass Ihre App so eingerichtet ist, dass sie den angepassten Pfad korrekt verarbeitet. Lesen Sie den SparkPost-Artikel [Using SparkPost click tracking on deep links](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#preferred-solution-using-sparkpost-click-tracking-on-deep-links). Dieser Artikel enthält Beispielcode für [iOS](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#ios-swift-forwarding-clicks-to-sparkpost) und [Android](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#forwarding-clicks-from-android-to-sparkpost).

{% endtab %}
{% tab Amazon SES %}

Verwenden Sie angepasste Pfade, um Pfadsegmente zu E-Mail-Klick-Tracking-URLs hinzuzufügen. Dadurch entstehen vorhersehbare URL-Muster, die mobile Betriebssysteme für Universal Links und App Links erkennen können.

Wenn Nutzer:innen auf mobilen Geräten auf E-Mail-Links tippen, helfen angepasste Pfade Ihnen zu steuern, ob Links in Ihrer Haupt-App, einer spezialisierten App oder dem mobilen Browser geöffnet werden (zum Beispiel Produktseiten, Kundenbindungs-Programme, Abmeldelinks oder rechtliche Seiten).

So behandeln Sie einen Amazon SES-Klick-Tracking-Link als Universal Link oder App Link:

1. Fügen Sie `ses:custom-path`-Attribute zu Ihren Anker-Tags im E-Mail-HTML hinzu, oder fügen Sie das Attribut im Abschnitt **Attribute** des Drag-and-Drop-Editors für E-Mail hinzu. Der angepasste Pfad wird in die umschlossene Klick-Tracking-URL eingefügt.

Zum Beispiel:

```html
<!-- Opens main shopping app -->
<a href="https://yourstore.com/product" ses:custom-path="shop">Shop Now</a>
<!-- Opens loyalty app -->
<a href="https://yourstore.com/rewards" ses:custom-path="rewards">My Rewards</a>
<!-- Opens specialized app -->
<a href="https://yourstore.com/limited" ses:custom-path="limited">Limited Edition</a>
<!-- Stays in browser -->
<a href="https://yourstore.com/unsubscribe" ses:no-track>Unsubscribe</a>
```

Stellen Sie sicher, dass Ihre angepassten Pfade diesen Anforderungen entsprechen:

- **Format:** Nur alphanumerische Zeichen, Punkte, Unterstriche und Bindestriche
- **Länge:** 1–32 Zeichen
- **Groß-/Kleinschreibung:** Pfade unterscheiden Groß- und Kleinschreibung, um den Anforderungen mobiler Betriebssysteme zu entsprechen

{:start="2"}
2. Überprüfen Sie, ob Ihre umschlossenen Tracking-URLs das angepasste Pfadsegment enthalten. Ohne das Attribut verwenden getrackte Links `track.yourstore.com/CL0/{encodedUrl}/...`. Mit dem Attribut folgen sie diesem Format: `track.yourstore.com/CL1/{customPath}/{encodedUrl}/...`

Zum Beispiel:

- `track.yourstore.com/CL1/shop/...`
- `track.yourstore.com/CL1/rewards/...`

{:start="3"}
3. Konfigurieren Sie Ihre Site-Zuordnungsdateien auf Ihrer Klick-Tracking-Domain so, dass die Pfade `/CL1/{customPath}/` entsprechen.

**iOS (Apple App Site Association):**

```json
{
  "applinks": {
    "apps": [],
    "details": [{
      "appID": "TEAMID.com.yourcompany.mainapp",
      "paths": ["/CL1/shop/*", "/CL1/rewards/*"]
    }, {
      "appID": "TEAMID.com.yourcompany.limitedapp",
      "paths": ["/CL1/limited/*"]
    }]
  }
}
```

**Android (Digital Asset Links):**

```json
[{
  "relation": ["delegate_permission/common.handle_all_urls"],
  "target": {
    "namespace": "android_app",
    "package_name": "com.yourcompany.mainapp",
    "sha256_cert_fingerprints": ["..."]
  }
}]
```

Android gleicht Pfade in Ihrer App ab, nicht in `assetlinks.json`. Setzen Sie `android:pathPrefix="/CL1/{customPath}/"` im Intent-Filter in Ihrer `AndroidManifest.xml` für jeden angepassten Pfad, den Ihre App verarbeitet.

Stellen Sie sicher, dass Ihre App so eingerichtet ist, dass sie diese umschlossenen Links verarbeitet. Fügen Sie Ihre Klick-Tracking-Domain zu den zugehörigen Domains Ihrer App (iOS) oder den Intent-Filtern (Android) hinzu und hosten Sie die AASA- oder Digital Asset Links-Datei auf dieser Domain, wie weiter oben in diesem Artikel beschrieben.

{% endtab %}
{% endtabs %}

### Klick-Tracking pro Link deaktivieren {#turning-off-click-tracking-on-a-link-to-link-basis}

Sie können das Klick-Tracking für bestimmte Links deaktivieren, indem Sie HTML-Code zu Ihrer E-Mail-Nachricht für den HTML-Editor oder zu einem HTML-Block für den Drag-and-Drop-Editor hinzufügen.

#### SendGrid

Wenn Ihr E-Mail-Anbieter SendGrid ist, verwenden Sie den HTML-Code `clicktracking=off` wie folgt:

```HTML
<a clicktracking=off href="[INSERT https LINK HERE]">click here</a>
```

#### SparkPost

Wenn Ihr E-Mail-Anbieter SparkPost ist, verwenden Sie den HTML-Code `data-msys-clicktrack="0"` wie folgt:

```HTML
<a data-msys-clicktrack="0" href="[INSERT https LINK HERE]">click here</a>
```

#### Amazon SES

Wenn Ihr E-Mail-Anbieter Amazon SES ist, verwenden Sie den HTML-Code `ses:no-track` wie folgt:

```HTML
<a ses:no-track href="[INSERT https LINK HERE]">click here</a>
```

#### Drag-and-Drop-Editor {#drag-and-drop-editor}

Wenn Sie den Drag-and-Drop-E-Mail-Editor verwenden, geben Sie Ihren HTML-Code als angepasstes Attribut ein, wenn Ihr Link an einen Text, einen Button oder ein Bild angehängt ist.

##### Angepasstes Attribut für einen Textlink {#custom-attribute-for-a-text-link}

#### SendGrid

Wählen Sie Folgendes für das angepasste Attribut:

- **Name:** `clicktracking`
- **Wert:** `off`

#### SparkPost

Wählen Sie Folgendes für das angepasste Attribut:

- **Name:** `data-msys-clicktrack`
- **Wert:** `0`

![Ein angepasstes Attribut für einen Textlink.]({% image_buster /assets/img/text_click_tracking_off.png %}){: style="max-width:60%;"}

##### Angepasstes Attribut für einen Button oder ein Bild {#custom-attribute-for-a-button-or-image}

#### SendGrid

Wählen Sie Folgendes für das angepasste Attribut:

- **Name:** `clicktracking`
- **Wert:** `off`
- **Typ:** Link

#### SparkPost

Wählen Sie Folgendes für das angepasste Attribut:

- **Name:** `data-msys-clicktrack`
- **Wert:** `0`
- **Typ:** Link

![Ein angepasstes Attribut für einen Button.]({% image_buster /assets/img/button_click_tracking_off.png %}){: style="max-width:60%;"}

### Fehlerbehebung bei Universal Links mit Klick-Tracking {#troubleshooting-universal-links-with-click-tracking}

Wenn Ihre Universal Links in Ihren E-Mails nicht wie erwartet funktionieren, z. B. wenn Empfänger:innen von ihrer E-Mail-App zum Webbrowser navigiert werden, bevor sie schließlich zur App weitergeleitet werden, lesen Sie diese Tipps zur Fehlerbehebung Ihrer Universal-Link-Einrichtung.

#### Outlook zeigt `[?it=` oder rohen URL-Text anstelle eines Buttons an {#outlook-shows-it-or-raw-url-text-instead-of-a-button}

Outlook zeigt möglicherweise Call-to-Action-Text wie `[?it=` an oder gibt einen Teil der `href`-URL aus, wenn ein Link kein gültiges **`http://`- oder `https://`**-URL-Schema verwendet. Angepasste Schemas, fehlende Schemas oder fehlerhafte URLs werden nicht als Hyperlinks behandelt, sodass der Client stattdessen den Attributtext anzeigt. Bestätigen Sie, dass jeder Button, jeder Bildlink und jede getrackte URL eine vollständige `https://`- (oder `http://`-) Zieladresse verwendet. Dies gilt sowohl für Universal Links als auch für Standard-Web-Links.

#### Dateispeicherort der Linkdatei überprüfen {#verify-link-file-location}

Stellen Sie sicher, dass sich die AASA-Datei (iOS) oder die Digital Asset Links-Datei (Android) am richtigen Speicherort befindet:

- **iOS:** `https://click.tracking.domain/.well-known/apple-app-site-association`
- **Android:** `https://click.tracking.domain/.well-known/assetlinks.json`

Es ist wichtig sicherzustellen, dass diese Dateien immer öffentlich zugänglich sind. Wenn Sie nicht darauf zugreifen können, haben Sie möglicherweise einen Schritt bei der Einrichtung von Universal Links für E-Mail übersprungen.

#### Domain-Definitionen überprüfen {#verify-domain-definitions}

Stellen Sie sicher, dass Sie die korrekten Definitionen für Domains haben, die Ihre App öffnen darf.

- **iOS:** Überprüfen Sie die zugehörigen Domains, die in Xcode für Ihre App eingerichtet wurden ([Schritt 1c: Zugehörige Domains in Ihrem Xcode-Projekt aktivieren]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links?tab=ios#step-1c)). Prüfen Sie, ob die Klick-Tracking-Domain in dieser Liste enthalten ist.
- **Android:** Öffnen Sie die App-Info-Seite (langes Drücken auf das App-Symbol und Klick auf ⓘ). Suchen Sie im App-Info-Menü nach **Standardmäßig öffnen** und tippen Sie darauf. Es sollte ein Bildschirm mit allen verifizierten Links angezeigt werden, die die App öffnen darf. Prüfen Sie, ob die Klick-Tracking-Domain in dieser Liste enthalten ist.

#### Jeder E-Mail-Link öffnet die App {#every-email-link-opens-the-app}

Wenn jeder Link in einer E-Mail Ihre App öffnet, einschließlich Links, von denen Sie erwarten, dass sie im Browser geöffnet werden, stimmen die AASA-`paths`-Werte (iOS) oder Android-`pathPrefix`-Werte auf Ihrer Klick-Tracking-Domain mit der gesamten Domain überein (zum Beispiel `*` oder `/*`).

Beschränken Sie diese Muster auf die URLs, die die App öffnen sollen. Für SendGrid verwenden Sie `/uni/` als Übereinstimmung und fügen Sie `universal="true"` nur bei diesen Links hinzu. Siehe [Universal Links, App Links und Klick-Tracking](#universal-links-app-links-and-click-tracking).

#### Tracking-Domain kann keine .well-known-Dateien bereitstellen {#tracking-domain-cant-serve-well-known-files}

In einigen Fällen kann Ihre Klick-Tracking-Domain die erforderlichen `.well-known`-Dateien aufgrund von E-Mail-Anbieter-Einschränkungen oder Infrastruktur-Beschränkungen möglicherweise nicht hosten. Wenn Sie die AASA- oder Digital Asset Links-Datei nicht auf Ihrer Tracking-Domain hosten können, ziehen Sie die folgenden Optionen in Betracht:

- **Klick-Tracking für Deeplink-URLs selektiv deaktivieren:** Sie können das Klick-Tracking für bestimmte Universal Links deaktivieren, damit sie direkt zu Ihrer Hauptdomain führen (auf der Sie die AASA- oder Digital Asset Links-Datei hosten können). Beachten Sie, dass bei dieser Methode die Klick-Analyse für diese bestimmten Links verloren gehen kann. Anleitungen finden Sie unter [Klick-Tracking pro Link deaktivieren](#turning-off-click-tracking-on-a-link-to-link-basis).
- **Tracking-Subdomain mit einem CDN vorschalten:** Wenn Sie vollständiges Klick-Tracking und Deeplinking benötigen, können Sie ein CDN (wie Cloudflare oder CloudFront) vor Ihre Tracking-Subdomain schalten. Konfigurieren Sie das CDN so, dass es die `.well-known`-Dateien lokal bereitstellt und den gesamten übrigen Datenverkehr an Ihren E-Mail-Anbieter weiterleitet. Dieser Ansatz ist aufwendiger, gibt Ihnen aber die volle Kontrolle über sowohl Klick-Tracking als auch Universal Links.

#### Links funktionieren in einem Workspace, aber nicht in einem anderen {#links-working-in-one-workspace-but-not-another}

Wenn Universal Links oder App Links in Ihrem Produktions-Workspace korrekt funktionieren, aber in Ihrem Entwicklungs- oder Test-Workspace fehlschlagen, überprüfen Sie, ob die Domain der sendenden E-Mail-Adresse mit der Tracking-Domain übereinstimmt, die in den E-Mail-Einstellungen des jeweiligen Workspaces konfiguriert ist. Inkonsistente Konfiguration zwischen Workspaces kann dazu führen, dass sich Links unterschiedlich verhalten, auch wenn dieselben E-Mail-Templates und AASA- oder Digital Asset Links-Dateien verwendet werden.

So überprüfen Sie Ihre E-Mail-Konfiguration:

1. Gehen Sie im Braze-Dashboard zu **Einstellungen** > **E-Mail-Einstellungen**.
2. Überprüfen Sie die **Einstellungen für ausgehende E-Mails** unter **Versandkonfiguration**.
3. Bestätigen Sie, dass Ihre Versanddomain und Tracking-Domain für den Workspace, in dem die Links nicht funktionieren, korrekt aufeinander abgestimmt sind.

Wenn sich Ihre Versanddomain zwischen Workspaces unterscheidet, stellen Sie sicher, dass jeder Workspace die entsprechenden DNS-Einträge konfiguriert hat und dass Ihre AASA- (iOS) oder Digital Asset Links-Dateien (Android) von jeder Tracking-Domain aus zugänglich sind.