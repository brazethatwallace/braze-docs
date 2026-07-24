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

## Nach neuesten App-Versionen filtern {#filtering-by-most-recent-app-versions}

Braze SDKs erfassen automatisch die neueste App-Version einer Nutzerin oder eines Nutzers. Diese Versionen können in Filtern und Segmenten verwendet werden, um festzulegen, welche Nutzer:innen eine Nachricht oder Campaign erhalten sollen.

![Das Targeting-Optionen-Panel im Schritt „Zielgruppe zusammenstellen“ des Campaign-Erstellungsworkflows. Der Abschnitt „Zusätzliche Filter“ enthält den folgenden Filter: „Most Recent App Version Number for Android Stopwatch (Android) is below 3.7.0 (134.0.0.0)“.]({% image_buster /assets/img_archive/new_app_version.png %}){: style="max-width:90%;"}

{% alert note %}
Es kann einige Zeit dauern, bis die aktuellen App-Versionen angezeigt werden. Die App-Version im Nutzerprofil wird aktualisiert, wenn die Informationen vom SDK erfasst werden, was davon abhängt, wann Nutzer:innen ihre Apps öffnen. Wenn die Nutzerin oder der Nutzer die App nicht öffnet, wird die aktuelle Version nicht aktualisiert. <br><br> Diese Filter gelten außerdem nicht rückwirkend. Es empfiehlt sich, „größer als“ oder „gleich“ für aktuelle und zukünftige Versionen zu verwenden. Die Verwendung von Filtern für vergangene Versionen kann zu unerwartetem Verhalten führen.
{% endalert %}

### App-Versionsnummer {#app-version-number}

Verwenden Sie den Filter **App Version Number**, um Nutzer:innen nach der Version und Build-Nummer der App zu segmentieren.

Dieser Filter unterstützt numerische Vergleiche, um einen Bereich von App-Versionen anzusprechen. Sie können beispielsweise Nutzer:innen ansprechen, deren App „unter“, „über“ oder „gleich“ der App-Version „1.2.3“ liegt, was nützlich sein kann, um ein neues Feature zu bewerben, das ein App-Upgrade erfordert.

Dieser neue Filter kann den älteren Filter „App Version Name“ ersetzen, bei dem jede ältere Version explizit aufgelistet oder ein regulärer Ausdruck verwendet werden musste.

**So funktioniert es**

* Jeder Teil der `major.minor.patch`-Version, die in der App-Version Ihrer App gesendet wird, wird als Ganzzahl verglichen
* Wenn die Hauptversionsnummern gleich sind, werden die Nebenversionsnummern verglichen usw.

**Wichtig**

* Android-Apps haben sowohl einen für Menschen lesbaren [`versionName`](https://developer.android.com/reference/android/content/pm/PackageInfo#versionName) als auch einen internen [`versionCode`](https://developer.android.com/reference/android/content/pm/PackageInfo.html#getLongVersionCode()). Der Filter „App Version Number“ verwendet `versionCode`, da dieser garantiert mit jeder App-Store-Veröffentlichung inkrementiert wird.
* Dies kann zu Verwirrung führen, wenn `versionName` und `versionCode` Ihrer App nicht synchron sind, insbesondere da beide Felder im Braze-Dashboard eingesehen werden können. Als Best Practice sollten Sie sicherstellen, dass `versionName` und `versionCode` Ihrer App gemeinsam inkrementiert werden.
* Wenn Sie stattdessen nach dem für Menschen lesbaren Feld `versionName` filtern müssen (unüblich), verwenden Sie den Filter „App Version Name“.

#### SDK-Anforderungen {#sdk-requirements}

Werte für diesen Filter werden ab Braze Android SDK v3.6.0+ und iOS SDK v3.21.0+ erfasst. Auch wenn dieser Filter SDK-Anforderungen hat, können Sie mit diesem Feature trotzdem Nutzer:innen ansprechen, die niedrigere (ältere) Versionen Ihrer App verwenden!

Für Android basiert diese Versionsnummer auf dem [Package Long Version Code](https://developer.android.com/reference/android/content/pm/PackageInfo.html#getLongVersionCode()) der App.

Für iOS basiert diese Versionsnummer auf dem [Short Version String](https://developer.apple.com/documentation/bundleresources/information_property_list/cfbundleshortversionstring) der App.

{% alert tip %}
Dieser Filter wird erst mit Werten befüllt, nachdem Nutzer:innen ihre Apps auf die unterstützten Braze-SDK-Versionen aktualisiert haben. Bis dahin zeigt der Filter bei Auswahl keine Versionen an.
{% endalert %}

#### Anwendungsfall {#use-case}

Im folgenden Szenario nehmen wir an, dass Sie zuerst auf die Braze SDKs aktualisiert haben, die diesen Filter unterstützen, und zwar in Version `2.0.0` Ihrer App.

Sobald Braze Daten von Version 2.0.0 Ihrer App erhält, können Sie Nutzer:innen mit früheren oder späteren Versionen ansprechen.

| Filter  | App-Version der Nutzerin/des Nutzers  | Ergebnis |
| :------------- | :----------- | :--------- |
| Kleiner als 2.0.0 | 1.0.0 | Die Nutzerin/der Nutzer ist im Segment, auch wenn ihr/sein Braze SDK den Filter „App Version Number“ nicht unterstützte. |
| Größer als 2.0.0 | 2.5.1 | Die Nutzerin/der Nutzer und alle zukünftigen Installationen werden im Segment sein. |
| Größer als 2.0.0 | 1.9.9 | Die Nutzerin/der Nutzer ist nicht im Segment. |
| Kleiner oder gleich 2.0.0 | 3.0.1 | Die Nutzerin/der Nutzer ist nicht im Segment. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Anwendungsfall" }

### App-Versionsname {#app-version-name}

Verwenden Sie den Filter „App Version Name“, um Nutzer:innen nach dem für Nutzer:innen sichtbaren „Build-Namen“ der App zu segmentieren.

Dieser Filter unterstützt den Abgleich mit „ist“, „ist nicht“ und regulären Ausdrücken. Sie können beispielsweise Nutzer:innen ansprechen, deren App nicht die Version „1.2.3-test-build“ hat.

Für Android basiert dieser Versionsname auf dem [Package Version Name](https://developer.android.com/reference/android/content/pm/PackageInfo#versionName) der App. Für iOS basiert dieser Versionsname auf dem [Short Version String](https://developer.apple.com/documentation/bundleresources/information_property_list/cfbundleshortversionstring) der App.

### Feature noch nicht genutzt {#have-not-used-feature}

Wenn Sie eine neue App-Version veröffentlichen und neue Features einführen, bemerken Nutzer:innen möglicherweise neue Inhalte nicht. Eine Feature-Awareness-Campaign durchzuführen ist eine großartige Möglichkeit, Nutzer:innen über neue Features oder Features, die sie noch nie genutzt haben, zu informieren. Dazu müssen Sie ein [angepasstes Attribut]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) erstellen, das Nutzer:innen zugewiesen wird, die eine bestimmte Aktion in Ihrer App noch nie ausgeführt haben, oder ein [angepasstes Event]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) verwenden, um eine bestimmte Aktion zu verfolgen. Sie können dieses Attribut (oder Event) verwenden, um die Nutzer:innen zu segmentieren, an die Sie die Campaign senden möchten.

{% alert tip %}
Möchten Sie einen bestimmten Teil Ihrer Zielgruppe erneut ansprechen? Lesen Sie [Retargeting-Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/retargeting_campaigns), um zu erfahren, wie Sie Campaigns durch Nutzung der bisherigen Aktionen Ihrer Nutzer:innen retargeten können.
{% endalert %}