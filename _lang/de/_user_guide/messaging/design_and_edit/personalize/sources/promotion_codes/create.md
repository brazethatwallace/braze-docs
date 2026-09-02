---
nav_title: Codes erstellen
article_title: Aktionscodes erstellen
page_order: 0.1
description: "Erfahren Sie, wie Sie Aktionscodes in Ihren Campaigns und Canvase erstellen."
---

# Aktionscodes erstellen {#create-promotion-codes}

> Erfahren Sie, wie Sie Aktionscodes in Ihren Campaigns und Canvase erstellen.

## Eine Aktionscode-Liste erstellen {#create}

### 1. Schritt: Neue Liste erstellen {#step-1-create-a-new-list}

Gehen Sie im Dashboard zu **Dateneinstellungen** > **Aktionscodes** und wählen Sie dann **Aktionscode-Liste erstellen**.

![Button zum Erstellen eines Aktionscodes.]({% image_buster /assets/img/promocodes/promocode1.png %})

### 2. Schritt: Details eingeben {#step-2-enter-the-details}

1. Benennen Sie Ihre Aktionscode-Liste und fügen Sie eine optionale Beschreibung hinzu.
2. Erstellen Sie als Nächstes ein Code-Snippet für den Aktionscode.

Hier sind einige Details, die Sie beim Erstellen eines Code-Snippets beachten sollten:

- Sie können ein Code-Snippet nach dem Speichern nicht mehr bearbeiten.
- Snippets unterscheiden zwischen Groß- und Kleinschreibung. Zum Beispiel erkennt das System „Birthday_promo“ und „birthday_promo“ als zwei verschiedene Snippets.
- Verwenden Sie den Snippet-Namen in Liquid, um auf diesen Satz von Aktionscodes zu verweisen.
- Stellen Sie sicher, dass das Code-Snippet nicht bereits in einer anderen Liste verwendet wird.

![Eine Aktionscode-Liste mit dem Namen „SpringSale2025“ und dem Code-Snippet „spring25“.]({% image_buster /assets/img/promocodes/promocode3.png %}){: style="max-width:80%"}

### 3. Schritt: Aktionscode-Optionen auswählen {#step-3-choose-promotion-code-options}

Jede Aktionscode-Liste hat ein entsprechendes Ablaufdatum und eine Uhrzeit, die bei der Erstellung festgelegt werden. Die maximale Ablaufdauer beträgt sechs Monate ab dem Tag, an dem Sie Ihre Liste erstellen oder bearbeiten.

Innerhalb dieses Zeitraums können Sie das Ablaufdatum wiederholt ändern und Update or aktualisieren or aktualisieren. Dieses Ablaufdatum gilt für alle Codes, die dieser Liste hinzugefügt werden. Nach Ablauf werden die Codes aus dem Braze-System gelöscht, und alle Nachrichten, die das Code-Snippet dieser Liste aufrufen, werden nicht gesendet.

![Einstellungen für den Listenablauf, dass alle verbleibenden Codes am 30. April 2025 um 0:00 Uhr ablaufen.]({% image_buster /assets/img/promocodes/promocode4.png %}){: style="max-width:80%"}

Sie haben außerdem die Möglichkeit, optionale und angepasste Schwellenwert-Benachrichtigungen einzurichten. Wenn diese eingerichtet sind, senden sie eine E-Mail an die/den festgelegte/n Empfänger:in, wenn die Liste nur noch wenige verfügbare Aktionscodes enthält oder wenn Ihre Aktionscode-Liste kurz vor dem Ablauf steht. Die/der Empfänger:in wird einmal täglich benachrichtigt.

![Ein Beispiel für eine Schwellenwert-Benachrichtigung, die „marketing@abc.com“ benachrichtigt, wenn die Aktionscode-Liste in 5 Tagen abläuft.]({% image_buster /assets/img/promocodes/promocode5.png %}){: style="max-width:80%"}

### 4. Schritt: Aktionscodes hochladen {#step-4-upload-promotion-codes}

Braze verwaltet weder die Code-Erstellung noch die Einlösung. Das bedeutet, dass Sie Ihre Aktionscodes generieren, in eine CSV-Datei exportieren und sie in Braze hochladen müssen.

Stellen Sie sicher, dass Ihre CSV-Datei diese Richtlinien einhält:

- Sie enthält eine Spalte für Aktionscodes.
- Es gibt einen Aktionscode pro Zeile.

Sie können unsere integrierte Integration mit [Voucherify]({{site.baseurl}}/partners/ecommerce/loyalty/voucherify) oder [Talon.One]({{site.baseurl}}/partners/ecommerce/loyalty/talonone) verwenden, um Aktionscodes zu erstellen und zu exportieren.

{% alert important %}
Die maximale Dateigröße beträgt 100&nbsp;MB und die maximale Listengröße beträgt 20 Millionen ungenutzte Codes. Wenn Sie die falsche Datei hochgeladen haben, laden Sie eine neue hoch, um die vorherige Datei zu ersetzen.
{% endalert %}

1. Nachdem der Upload abgeschlossen ist, wählen Sie **Liste speichern**, um alle Details und Codes zu speichern, die Sie gerade eingegeben haben.

![CSV-Datei mit dem Namen „springsale“, die erfolgreich hochgeladen wurde.]({% image_buster /assets/img/promocodes/promocode7.png %})

{:start="2"}
2. Nach dem Speichern erscheint eine neue Zeile im **Importverlauf**.
3. Um die Tabelle zu Update or aktualisieren or aktualisieren und zu prüfen, ob Ihr Import abgeschlossen ist, wählen Sie <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-sync" ></span> **Synchronisieren** oben in der Tabelle.

![Aktionscodes, die gerade hochgeladen werden.]({% image_buster /assets/img/promocodes/promocode8.png %})

{% alert note %}
Größere Dateien benötigen mehrere Minuten für den Import. Während Sie warten, können Sie die Seite verlassen und an etwas anderem arbeiten, während der Import läuft. Wenn der Import abgeschlossen ist, ändert sich der Status in der Tabelle auf **Fertig**.
{% endalert %}

## Eine Aktionscode-Liste Update or aktualisieren or aktualisieren {#updating-a-promotion-code-list}

Um eine Liste zu Update or aktualisieren or aktualisieren, wählen Sie eine Ihrer bestehenden Listen aus. Sie können den Namen, die Beschreibung, den Listenablauf und die Schwellenwert-Benachrichtigungen ändern. Sie können der Liste auch weitere Codes hinzufügen, indem Sie neue Dateien hochladen und **Liste Update or aktualisieren or aktualisieren** auswählen. Alle Codes in der Liste haben dasselbe Ablaufdatum, unabhängig vom Importdatum.

{% alert important %}
Aktionscodes können nicht gelöscht werden.
{% endalert %}

### Eine fehlerhafte Aktionscode-Liste korrigieren {#modifying-an-incorrect-promotion-code-list}

Wenn Sie eine CSV-Datei mit den falschen Aktionscodes hochgeladen und **Liste speichern** ausgewählt haben, können Sie dies mit einer der folgenden Methoden beheben:

- Die gesamte Liste außer Betrieb nehmen: Verwenden Sie die aktuelle Aktionscode-Liste nicht mehr in Campaigns, Canvase oder Templates. Laden Sie dann die CSV-Datei mit den korrekten Codes hoch und verwenden Sie diese in Ihrem Messaging.
- Die fehlerhaften Codes aufbrauchen: Erstellen Sie eine Campaign, die Aktionscodes aus der fehlerhaften Aktionscode-Liste an einen Platzhalter sendet, bis alle fehlerhaften Codes aufgebraucht sind. Laden Sie dann die korrekten Aktionscodes in dieselbe Liste hoch.