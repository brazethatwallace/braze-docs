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

Um das Braze-Support-Team zu kontaktieren, navigieren Sie zum Braze-Dashboard und wählen Sie **Support** > **Get help with Operator** > **Contact Support** aus.

Dadurch wird BrazeAI Operator<sup>TM</sup> mit der Option geöffnet, direkt ein Support-Ticket einzureichen. Operator kann Ihr Problem mithilfe des Kontexts aus Ihrer Konversation und dem aktuellen Bildschirm beheben. Wenn Operator Ihr Problem nicht lösen kann, können Sie ihn bitten, ein Support-Ticket auf Basis Ihrer Konversation zu erstellen und das Ticket dann im Braze-Support-Portal einzureichen (wenn Sie ein:e designierte:r Support-Kontakt sind) oder über unser Standard-Support-Formular.

Weitere Informationen finden Sie unter [Support-Tickets mit BrazeAI Operator einreichen]({{site.baseurl}}/user_guide/brazeai/operator/support_tickets). Wenn Sie sich nicht sicher sind, ob Sie ein:e Braze-Support-Kontakt sind, wenden Sie sich an den Braze-Administrator Ihres Unternehmens, Ihren Braze-Success-Manager oder den Kontoinhaber.

![Das Dropdown-Menü „Support“ mit der Option „Get help with Operator“.]({% image_buster /assets/img_archive/get_help.png %}){: style="max-width:50%;"}


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

## Best Practices für die Einreichung eines Support-Falls {#best-practices-for-submitting-a-support-case}

### So viele Informationen wie möglich bereitstellen {#provide-as-much-information-as-possible}

Je mehr Insights Sie liefern können, desto besser. Geben Sie Details wie den Workspace, die URL zur Campaign oder zum Segment und alle relevanten externen IDs an. Dies kann uns helfen, Ihr Problem effizienter zu beheben.

### Eine Stichprobe von Nutzer:innen bereitstellen {#provide-a-sample-of-users}

Teilen Sie eine Stichprobe von Nutzer:innen anstelle des gesamten betroffenen Segments. Die Bereitstellung einer kleineren Anzahl von Nutzer:innen hilft uns, den Umfang einzugrenzen und unsere Untersuchungen zu beschleunigen.

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