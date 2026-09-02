---
nav_title: Judo
article_title: Judo
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Judo, einer serverbasierten No-Code-UI-Plattform, mit der Sie Standortkontext und Tracking zu Ihren iOS- und Android-Apps hinzufügen können."
alias: /partners/judo/
page_type: partner
search_tag: Partner

---

# Judo

> [Judo](https://judo.app) ist eine serverbasierte UI-Plattform, die es Publishern ermöglicht, reichhaltige, ansprechende In-App-Erlebnisse effizient bereitzustellen – ohne App-Updates.

_Diese Integration wird von Judo gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Braze und Judo bietet maßgeschneiderte Erlebnisse in Ihren Campaigns und Canvase. Anstelle einer einfachen, templatebasierten Landing-Page kann eine Braze-Campaign Inhalte enthalten, die mehrere Bildschirme, Modals, Videos, angepasste Schriftarten und Unterstützungseinstellungen wie Dark Mode und Barrierefreiheit umfassen – entwickelt ohne Code und bereitgestellt ohne App-Updates. Daten aus Braze können auch verwendet werden, um personalisierte Inhalte in einem Judo-Erlebnis zu unterstützen. Nutzer:innen-Ereignisse und Daten aus dem Erlebnis können für Attribution und Targeting in Braze zurückgeführt werden.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
|---|---|
| Judo-Konto | Um diese Partnerschaft zu nutzen, benötigen Sie ein [Judo-Konto](https://www.judo.app/). |
| Judo SDK or Software-Development-Kit | Das Judo SDK or Software-Development-Kit muss in Ihre [iOS-](https://github.com/judoapp/judo-ios/) und/oder [Android-Apps](https://github.com/judoapp/judo-android) integriert werden. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Anwendungsfälle {#use-cases}

**Onboarding**: App-Publisher, die Judo verwenden, erstellen und implementieren reichhaltige, native Onboarding-Erlebnisse. Diese Erlebnisse können nun ein Element einer personalisierten, kanalübergreifenden Onboarding-Journey sein, die über Braze koordiniert wird. Die Erlebnisse können personalisiert und ohne App-Updates schnell aktualisiert werden, um die Wirksamkeit verschiedener In-App-Flows zu testen.

**Conversion**: App-Publisher können Daten aus Braze nutzen, um ein personalisiertes, reichhaltiges In-App-Erlebnis zu schaffen, das In-App-Käufe, bezahlte Abos oder kontextuelles Merchandising mithilfe von Integrations-Hooks in Judo fördert. Der Zugriff auf diese Erlebnisse kann über Engagement-Marketing-Campaigns in Braze getriggert werden.

**Ereignisgesteuerte Inhalte**: Judo wird im Sport- und Unterhaltungsbereich vor allem dazu eingesetzt, reichhaltige Erlebnisse zur Vorschau, Bewerbung und Zusammenfassung von Events zu erstellen. Diese Fähigkeit lässt sich auch in anderen Branchen für saisonale und nachrichtenorientierte Inhalte einsetzen. Durch die Verknüpfung von Messaging zur zeitnahen Bewerbung oder Hervorhebung von Events mit reichhaltigen In-App-Erlebnissen können Publisher das Engagement steigern, indem sie kontextuell relevant sind.

## Side-by-side-SDK or Software-Development-Kit-Integration

Judo bietet zusätzliche Bibliotheken, die einen Teil des Aufwands automatisieren, der für die parallele Integration der Judo- und Braze-SDKs in Ihre mobilen Apps erforderlich ist.

### 1. Schritt: Judo-Braze-Integrationsbibliothek installieren {#step-1-install-the-judo-braze-integration-library}

Installieren und richten Sie die Judo-Braze-Integrationsbibliothek in Ihren Apps ein. Dadurch wird das Tracking von Ereignissen automatisch aktiviert.

- [iOS-Installationsanweisungen](https://github.com/judoapp/judo-braze-ios/wiki#installation)
- [Android-Installationsanweisungen](https://github.com/judoapp/judo-braze-android/wiki#installation).

### 2. Schritt: In-App-Nachrichten konfigurieren {#step-2-configure-in-app-messaging}

In diesem Schritt werden angepasste `ABKInAppMessageControllerDelegate`- und `IInAppMessageManagerListener`-Implementierungen für iOS und Android erstellt.

Sehen Sie sich die Dokumentation zur Einrichtung von In-App-Nachrichten an, die für jede der Integrationsbibliotheken mitgeliefert wird:

- [iOS-In-App-Messaging-Einrichtung](https://github.com/judoapp/judo-braze-ios/wiki#in-app-messaging-setup)
- [Android-In-App-Messaging-Einrichtung](https://github.com/judoapp/judo-braze-android/wiki#in-app-messaging-setup).

## Verwendung dieser Integration {#using-this-integration}

Sobald Sie die App-seitige Integration abgeschlossen haben, können Sie sie testen, indem Sie eine Braze-In-App-Nachricht-Campaign für ein Judo-Erlebnis ausführen, um zu überprüfen, ob sie wie erwartet funktioniert.

### 1. Schritt: In-App-Nachricht-Campaign mit angepasstem Code erstellen {#step-1-create-a-custom-code-in-app-message-campaign}

Erstellen Sie auf der Braze-Plattform eine In-App-Nachricht-Campaign mit dem Nachrichtentyp **Custom Code**. Wählen Sie als Nächstes **HTML Upload** als angepassten Typ aus. Stellen Sie sicher, dass Sie den Inhalt der Nachricht mit den Basisfeldern für In-App-Nachrichten ausfüllen; dieser Inhalt wird den Nutzer:innen nicht angezeigt.

![Ein Bild, das zeigt, wie das Dashboard aussieht, wenn Sie den Nachrichtentyp „Custom Code“ auswählen.]({% image_buster /assets/img/judo/braze-campaign-select-custom-type.png %})

Verwenden Sie als Nächstes das folgende minimale HTML-Snippet, um die Formularvalidierung zu erfüllen:
```
<a href="appboy://close">X</a>
```

Beachten Sie, dass dies in der Produktion auf Ihrem Gerät nicht angezeigt wird, da Judo es umschreiben und durch ein Judo-Erlebnis ersetzen wird.

![Ein Bild, das den Formularvalidierungscode zeigt, der dem Verfassen-Schritt Ihrer Campaign hinzugefügt wurde.]({% image_buster /assets/img/judo/braze-html-boilerplate.png %})

### 2. Schritt: Schlüssel-Wert-Paar für Judo festlegen {#step-2-set-a-key-value-pair-for-judo}
![Dieses Bild zeigt das eine Schlüssel-Wert-Paar, das für diese Integration benötigt wird. Der „Schlüssel“ ist „judo-experience“ und der „Wert“ ist Ihr Judo-Link.]({% image_buster /assets/img/judo/braze-campaign-extras-judo-experience.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Legen Sie ein [angepasstes Schlüssel-Wert-Paar]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs/) für die Campaign mit dem Schlüssel `judo-experience` fest. Geben Sie die URL des Judo-Erlebnisses an, das Sie hier anzeigen möchten. Die Judo-Braze-Integrationsbibliothek erkennt dann dieses Schlüssel-Wert-Paar im Handler und verwendet es, um Ihr Judo-Erlebnis anstelle der standardmäßigen Braze-In-App-Nachricht-UI einzuspeisen.
<br><br>
### 3. Schritt: Campaign abschließen {#step-3-finishing-the-campaign}

Schließen Sie abschließend die Campaign ab, indem Sie einen Trigger or triggern für die Campaign einrichten und Nutzer:innen über Segments in den Abschnitten **Delivery** und **Target User** auswählen. Besuchen Sie unseren [Artikel]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/) über In-App-Nachrichten, in dem die verschiedenen Komponenten einer Braze-In-App-Nachricht erläutert werden.