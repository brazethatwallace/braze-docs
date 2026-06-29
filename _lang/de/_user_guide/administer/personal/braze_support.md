---
nav_title: Braze-Support
article_title: Braze-Support
page_order: 4
description: "Diese Seite hilft Ihnen, das Braze-Support-Portal zu finden, um Feedback zu Braze-Produkten einzureichen. Diese Seite ist nur für Braze-Kund:innen zugänglich."
alias: /braze_support/
page_type: reference
search_rank: 7
---

# [![Braze-Lernkurs]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/the-braze-support-portal/){: style="float:right;width:120px;border:0;" class="noimgborder"}Braze-Support {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomthe-braze-support-portal-stylefloatrightwidth120pxborder0-classnoimgborderbraze-support}

> Erfahren Sie, wie Sie auf das Braze-Support-Portal zugreifen, Support-Fälle einreichen und nachverfolgen und die für eine effiziente Fehlerbehebung benötigten Informationen bereitstellen.

## Zugriff auf das Support-Portal {#access-the-support-portal}

Um das Braze-Support-Team zu kontaktieren, navigieren Sie zum Braze-Dashboard und wählen Sie **Support** aus. Das Menü bietet zwei Optionen:

- **Get help with Operator** öffnet BrazeAI Operator<sup>TM</sup>, der Ihr Problem direkt mithilfe des Kontexts aus Ihrer Konversation und dem aktuellen Bildschirm beheben kann. Wenn Operator Ihr Problem nicht lösen kann, können Sie ihn bitten, ein Support-Ticket auf Basis Ihrer Konversation zu erstellen. Weitere Informationen finden Sie unter [Support-Tickets mit BrazeAI Operator einreichen]({{site.baseurl}}/user_guide/brazeai/operator/support_tickets).
- **Get help** leitet Sie direkt zum Braze-Support-Portal weiter (wenn Sie ein:e designierte:r Support-Kontakt sind) oder zu unserem Standard-Support-Formular, wo Sie Fälle einreichen und nachverfolgen können. Wenn Sie sich nicht sicher sind, ob Sie ein:e Braze-Support-Kontakt sind, wenden Sie sich an den Braze-Administrator Ihres Unternehmens, Ihren Braze-Success-Manager oder den Kontoinhaber.

![Das Dropdown-Menü „Support“ mit den Optionen „Get help with Operator“ und „Get help“.]({% image_buster /assets/img_archive/get_help.png %}){: style="max-width:50%;"}


## Designierte Support-Kontakte hinzufügen {#adding-designated-support-contacts}

Designierte Support-Kontakte können auf alle Support-Fälle Ihres Unternehmens zugreifen, unabhängig davon, wer sie eingereicht hat. Sie können Nutzer:innen direkt über die Seite **Nutzer:in bearbeiten** als designierte Support-Kontakte festlegen.

1. Gehen Sie zu **Einstellungen** > **Unternehmensnutzer:innen** und suchen Sie nach dem/der Nutzer:in anhand des Namens oder der E-Mail-Adresse.
2. Wählen Sie entweder den Nutzernamen aus oder fahren Sie mit der Maus über die Zeile des Nutzernamens, um ein Menü anzuzeigen.
3. Wählen Sie im Menü **Bearbeiten** aus, um zur Seite **Nutzer:in bearbeiten** weitergeleitet zu werden.
4. Aktivieren Sie das Kontrollkästchen **Set this user as a Designated Support Contact for Braze Support Portal**.

### Zugang erhalten {#gaining-access}

Nachdem ein:e Nutzer:in als Support-Kontakt designiert wurde, sendet das Braze-Support-Portal dieser Person eine Willkommens-E-Mail mit Anweisungen zur Einrichtung des Zugangs.

## Fälle Ihres Unternehmens anzeigen {#view-cases-from-your-company}

Wenn Sie ein:e designierte:r Support-Kontakt sind, verwenden Sie die **My Org's**-Filteransichten im Support-Portal, um alle von Nutzer:innen Ihres Unternehmens eingereichten Fälle anzuzeigen. Fälle aus allen Einreichungskanälen (BrazeAI Operator<sup>TM</sup>, Webformular, E-Mail oder Portal) sind in diesen Ansichten enthalten.

## Screenshots der Entwicklungskonsole bereitstellen {#provide-developer-console-screenshots}

Bei der Kommunikation mit dem Support kann es vorkommen, dass Sie auf Ihre Entwicklungskonsole zugreifen müssen, um zusätzliche Informationen bereitzustellen:
- Chrome
  1. Rechtsklicken Sie auf die Webseite und wählen Sie **Inspect** aus.
  2. Wählen Sie den Tab **Console** im sich öffnenden Fenster aus.
  3. Erstellen Sie einen Screenshot des Console-Tabs.<br><br>
- Firefox
  1. Rechtsklicken Sie auf die Webseite und wählen Sie **Inspect Element** aus.
  2. Wählen Sie den Tab **Console** im sich öffnenden Fenster aus.
  3. Erstellen Sie einen Screenshot des Console-Tabs.<br><br>
- Safari
  1. Gehen Sie in der Menüleiste oben auf Ihrem Bildschirm zu Safari und wählen Sie dann **Preferences** aus.
  2. Wählen Sie **Advanced** aus und aktivieren Sie dann das Kontrollkästchen neben **Show Develop menu in menu bar**. Sie können das Fenster anschließend schließen.
  3. Rechtsklicken Sie auf die Webseite und wählen Sie **Inspect Element** aus.
  4. Wählen Sie den Tab **Console** im sich öffnenden Fenster aus.
  5. Erstellen Sie einen Screenshot des Console-Tabs.

## Best Practices für die Einreichung eines Support-Falls {#best-practices-for-submitting-a-support-case}

### So viele Informationen wie möglich bereitstellen {#provide-as-much-information-as-possible}

Je mehr Insights Sie liefern können, desto besser. Geben Sie Details wie den Workspace, die URL zur Campaign oder zum Segment und alle relevanten externen IDs an. Dies kann uns helfen, Ihr Problem effizienter zu beheben.

### Eine Stichprobe von Nutzer:innen bereitstellen {#provide-a-sample-of-users}

Teilen Sie eine Stichprobe von Nutzer:innen anstelle des gesamten betroffenen Segments. Die Bereitstellung einer kleineren Anzahl von Nutzer:innen hilft uns, den Umfang einzugrenzen und unsere Untersuchungen zu beschleunigen.

### Netzwerkprotokolle (HAR-Protokolle) anhängen {#attach-network-logs-har-logs}

Wenn Sie den Support kontaktieren, ist es hilfreich, wenn der/die betroffene Nutzer:in Netzwerkprotokolle (HAR-Protokolle) aus dem Browser erfasst, während das Problem auftritt. Diese zeigen die Netzwerkanfragen zwischen dem Browser und dem Server für die einzelnen Komponenten einer Webseite sowie das Braze-Dashboard an, das der/die Nutzer:in zu öffnen versucht.

Lassen Sie den/die betroffene:n Nutzer:in Folgendes tun:

1. Öffnen Sie die Entwicklertools. In Chrome kann dies mit dem Tastenkürzel `option` + `⌘` + `J` (unter macOS) erfolgen. Unter Windows oder Linux verwenden Sie das Tastenkürzel `shift` + `CTRL` + `J`.
2. Wählen Sie **Network** > **Fetch/XHR** oder **XHR** aus.
3. Erstellen Sie eine Bildschirmaufnahme oder einen Screenshot, der **Name**, **Status**, **Size** und **Time** für die Elemente zeigt.<br><br>![Der Tab „Fetch/XHR“ in einem Chrome-Browser.]({% image_buster /assets/img/network_xhr.png %}){: style="max-width:60%;"}

Hängen Sie dann die Aufnahme oder den Screenshot an das Support-Ticket an. Diese Informationen können die Untersuchung des Supports unterstützen.

### Erwartetes und tatsächliches Verhalten klären {#clarify-expected-versus-actual-behavior}

Teilen Sie uns mit, was Sie erwartet haben und was tatsächlich passiert ist. Dies kann uns helfen, die möglichen Ursachen des Problems einzugrenzen.

### Relevante Bilder anhängen {#attach-relevant-images}

Erwägen Sie, einen Screenshot anzuhängen, um das Problem zu veranschaulichen. Die Bereitstellung dieser Bilder kann unser Verständnis des Problems erheblich verbessern und den Lösungsprozess beschleunigen.

### Auswirkungen bewerten {#assess-the-impact}

Wählen Sie den entsprechenden Schweregrad aus, damit wir die richtigen Ressourcen zur Behebung des Problems zuweisen können.

{% alert important %}
Wenn Sie ein Problem als „Critical“ markieren, bedeutet dies, dass Ihre Produktionsinstanz ausgefallen ist und alle Arbeiten in Braze gestoppt wurden.
{% endalert %}

## Fehlerbehebung bei Ladeproblemen des Dashboards {#troubleshooting-dashboard-load-issues}

Wenn das Braze-Dashboard nicht korrekt geladen wird, versuchen Sie Folgendes, bevor Sie den Support kontaktieren:

1. Öffnen Sie das Dashboard in einem anderen Browser oder in einem Inkognito- bzw. privaten Fenster.
2. [Leeren Sie Ihren Browser-Cache und Ihre Cookies]({{site.baseurl}}/user_guide/administer/personal/accessing_your_account#clearing-your-browser-cache-and-cookies).
3. Deaktivieren Sie Werbeblocker und Browser-Erweiterungen und laden Sie das Dashboard anschließend neu.
4. Wenn Sie ein VPN verwenden, trennen Sie die Verbindung und versuchen Sie es erneut.

Wenn Ihre Browser-Entwicklungskonsole `ERR_BLOCKED_BY_CLIENT` anzeigt, blockiert eine Erweiterung oder ein Werbeblocker Dashboard-Ressourcen. Deaktivieren Sie den Blocker für Ihre Braze-Dashboard-URL und laden Sie die Seite neu.

## Fehlerbehebung beim Zugriff {#troubleshooting-access}

Wenn Sie beim Anmelden am Braze-Support-Portal eine Fehlermeldung erhalten, wie z. B. `Check your entry`, stellen Sie sicher, dass Sie dem Link in Ihrer Willkommens-E-Mail gefolgt sind, um ein Passwort für das Portal festzulegen. Wenn Sie dies bereits getan haben oder sich zuvor am Portal anmelden konnten, erstellen Sie ein Support-Ticket.