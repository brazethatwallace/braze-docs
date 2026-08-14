---
nav_title: Feature-Awareness und neue App-Version
article_title: Feature-Awareness und neue App-Version
page_order: 9
page_type: reference
description: "Dieser Referenzartikel beschreibt, wie Sie Ihre Nutzer:innen informiert und begeistert halten, wenn Sie neue Features oder Versionen veröffentlichen."
tool: Campaigns

---

# Feature-Awareness und neue App-Version {#feature-awareness-and-new-app-version}

> Dieser Referenzartikel beschreibt, wie Sie die Braze-Plattform nutzen können, um Ihre Kund:innen über neue Features und Versionen Ihrer App auf dem Laufenden zu halten.

Sie arbeiten kontinuierlich daran, Ihre App zu aktualisieren und zu verbessern, und möchten, dass Ihre Nutzer:innen diese aufregenden neuen Features und App-Versionen erleben. Erfahren Sie, wie Sie Ihren Nutzer:innen die neuen Features näherbringen, die sie noch nicht genutzt haben, und sie ermutigen, die App zu erkunden, um das Beste aus Ihrem Angebot herauszuholen.

Feature-Awareness-Campaigns sind eine großartige Möglichkeit, Nutzer:innen dazu zu ermutigen, mit Ihrer App engagiert zu bleiben, während Sie die Funktionalität Ihrer App weiter verbessern. Nutzer:innen auf dem Laufenden zu halten ist eine hervorragende Methode, um sie aktiv zu halten, Bewertungen zu verbessern und das Engagement der Nutzer:innen sicherzustellen.

## Filtern nach den neuesten App-Versionen {#filtering-by-most-recent-app-versions}

Braze SDKs erfassen automatisch die neueste App-Version einer Nutzer:in. Diese Versionen können in Filtern und Segments verwendet werden, um festzulegen, welche Nutzer:innen eine Nachricht oder Campaign erhalten sollen.

![Das Panel „Targeting-Optionen“ im Schritt „Zielgruppe zusammenstellen“ im Workflow zur Campaign-Erstellung. Der Abschnitt „Zusätzliche Filter“ enthält den folgenden Filter: „Neueste App-Versionsnummer für Android Stopwatch (Android) ist unter 3.7.0 (134.0.0.0)“.]({% image_buster /assets/img_archive/new_app_version.png %}){: style="max-width:90%;"}

{% alert note %}
Es kann einige Zeit dauern, bis die aktuellen App-Versionen befüllt werden. Die App-Version im Nutzerprofil wird aktualisiert, wenn die Informationen vom SDK erfasst werden – das hängt davon ab, wann Nutzer:innen ihre App öffnen. Wenn Nutzer:innen die App nicht öffnen, wird die aktuelle Version nicht aktualisiert. <br><br> Diese Filter gelten außerdem nicht rückwirkend. Es empfiehlt sich, „größer als“ oder „gleich“ für aktuelle und zukünftige Versionen zu verwenden. Die Verwendung von Filtern für vergangene Versionen kann zu unerwartetem Verhalten führen.
{% endalert %}

### App-Versionsnummer {#app-version-number}

Verwenden Sie den Filter **App-Versionsnummer**, um Nutzer:innen nach der Version und Build-Nummer der App zu segmentieren.

Dieser Filter unterstützt numerische Vergleiche, um einen Bereich von App-Versionen anzusprechen. Sie können beispielsweise Nutzer:innen ansprechen, deren App „kleiner als“, „größer als“ oder „gleich“ der App-Version „1.2.3“ ist. Das kann nützlich sein, um ein neues Feature zu bewerben, das ein App-Upgrade erfordert.

Dieser Filter kann den älteren Filter „App-Versionsname“ ersetzen, bei dem jede ältere Version explizit aufgelistet oder ein regulärer Ausdruck verwendet werden musste.

#### Funktionsweise {#how-it-works}

- Jeder Teil der `major.minor.patch`-Version, die in der App-Version Ihrer App gesendet wird, wird als Ganzzahl verglichen.
- Wenn die Hauptversionsnummern gleich sind, vergleicht Braze die Nebenversionsnummern. Wenn die Nebenversionsnummern gleich sind, vergleicht Braze die Patch-Nummern.
- Bei Verwendung der Filter „kleiner als“ oder „kleiner als oder gleich“ gibt der Filter `true` zurück, wenn die App-Version im Profil einer Nutzer:in nicht vorhanden ist, und die Nutzer:in wird als älter als die getestete Version behandelt. Um Nutzer:innen ohne Versionsdaten auszuschließen, verwenden Sie stattdessen die Filter „größer als“ oder „gleich“.

#### Wichtige Hinweise {#important-considerations}

- Android-Apps haben sowohl einen für Menschen lesbaren [`versionName`](https://developer.android.com/reference/android/content/pm/PackageInfo#versionName) als auch einen internen [`versionCode`](https://developer.android.com/reference/android/content/pm/PackageInfo.html#getLongVersionCode()). Der Filter „App-Versionsnummer“ verwendet `versionCode`, da dieser bei jeder App-Store-Veröffentlichung garantiert inkrementiert wird.
- Dies kann zu Verwirrung führen, wenn `versionName` und `versionCode` Ihrer App nicht mehr synchron sind, insbesondere da beide Felder im Braze-Dashboard eingesehen werden können. Als Best Practice sollten Sie sicherstellen, dass `versionName` und `versionCode` Ihrer App gemeinsam inkrementiert werden.
- Wenn Sie stattdessen nach dem für Menschen lesbaren Feld `versionName` filtern müssen (unüblich), verwenden Sie den Filter „App-Versionsname“.

#### SDK-Anforderungen {#sdk-requirements}

Werte für diesen Filter werden ab Braze Android SDK v3.6.0+ und iOS SDK v3.21.0+ erfasst. Auch wenn dieser Filter SDK-Anforderungen hat, können Sie mit diesem Feature dennoch Nutzer:innen ansprechen, die niedrigere (ältere) Versionen Ihrer App verwenden.

Für Android basiert diese Versionsnummer auf dem [Package Long Version Code](https://developer.android.com/reference/android/content/pm/PackageInfo.html#getLongVersionCode()) der App.

Für iOS basiert diese Versionsnummer auf dem [Short Version String](https://developer.apple.com/documentation/bundleresources/information_property_list/cfbundleshortversionstring) der App.

{% alert tip %}
Dieser Filter wird erst mit Werten befüllt, nachdem Nutzer:innen ihre Apps auf die unterstützten Braze-SDK-Versionen aktualisiert haben. Bis dahin zeigt der Filter bei Auswahl keine Versionen an.
{% endalert %}

#### Anwendungsfall {#use-case}

Nehmen wir im folgenden Szenario an, dass Sie in Version `2.0.0` Ihrer App erstmals auf die Braze SDKs aktualisiert haben, die diesen Filter unterstützen.

Sobald Braze Daten von Version 2.0.0 Ihrer App empfängt, können Sie Nutzer:innen mit früheren oder späteren Versionen ansprechen.

| Filter | App-Version der Nutzer:in | Ergebnis |
| :------------- | :----------- | :--------- |
| Kleiner als 2.0.0 | 1.0.0 | Die Nutzer:in ist im Segment, obwohl ihr Braze SDK den Filter „App-Versionsnummer“ nicht unterstützte. |
| Größer als 2.0.0 | 2.5.1 | Die Nutzer:in und alle zukünftigen Installationen sind im Segment. |
| Größer als 2.0.0 | 1.9.9 | Die Nutzer:in ist nicht im Segment. |
| Kleiner als oder gleich 2.0.0 | 3.0.1 | Die Nutzer:in ist nicht im Segment. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Anwendungsfall" }

### App-Versionsname {#app-version-name}

Verwenden Sie den Filter „App-Versionsname“, um Nutzer:innen nach dem für Nutzer:innen sichtbaren „Build-Namen“ der App zu segmentieren.

Dieser Filter unterstützt den Abgleich mit „ist“, „ist nicht“ und regulären Ausdrücken. Sie können beispielsweise Nutzer:innen ansprechen, deren App nicht die Version „1.2.3-test-build“ hat.

Für Android basiert dieser Versionsname auf dem [Package Version Name](https://developer.android.com/reference/android/content/pm/PackageInfo#versionName) der App. Für iOS basiert dieser Versionsname auf dem [Short Version String](https://developer.apple.com/documentation/bundleresources/information_property_list/cfbundleshortversionstring) der App.

### Feature noch nicht verwendet {#have-not-used-feature}

Wenn Sie eine neue App-Version veröffentlichen und neue Features einführen, bemerken Nutzer:innen möglicherweise neue Inhalte nicht. Eine Campaign zur Feature-Bekanntheit ist eine großartige Möglichkeit, Nutzer:innen über neue Features oder Features zu informieren, die sie noch nie verwendet haben. Dazu müssen Sie ein [angepasstes Attribut]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) erstellen, das Nutzer:innen zugewiesen wird, die eine bestimmte Aktion in Ihrer App noch nie ausgeführt haben, oder ein [angepasstes Event]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) verwenden, um eine bestimmte Aktion zu verfolgen. Sie können dieses Attribut (oder Event) verwenden, um die Nutzer:innen zu segmentieren, an die Sie die Campaign senden möchten.

{% alert tip %}
Möchten Sie einen bestimmten Teil Ihrer Zielgruppe erneut ansprechen? Erfahren Sie unter [Retargeting-Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/retargeting_campaigns), wie Sie Campaigns durch Nutzung der bisherigen Aktionen Ihrer Nutzer:innen retargeten können.
{% endalert %}