---
nav_title: Genehmigungen
article_title: Genehmigungen
page_order: 1
page_type: reference
description: "Dieser Referenzartikel gibt einen Überblick über die verschiedenen Status, die eine Campaign und ein Canvas haben können, und was sie bedeuten."
tool:
    - Campaigns
    - Canvas
---

# Genehmigungen für Campaigns und Canvases {#approvals-for-campaigns-and-canvases}

> Verwenden Sie Genehmigungen, um einen letzten Prüfpunkt für Ihre Campaigns und Canvases vor dem Start hinzuzufügen. Mit diesem Workflow können Sie den Inhalt in allen erforderlichen Abschnitten Ihrer Nachricht überprüfen und genehmigen.

## So funktioniert es {#how-it-works}

Sie können die Details Ihrer Campaign oder Ihres Canvas im letzten Schritt der Bearbeitung überprüfen.

Sowohl für Canvases als auch für Campaigns müssen Sie alle Änderungen vor der Genehmigung speichern, auch wenn es Ihre eigenen Änderungen sind. Nutzer:innen mit den entsprechenden Berechtigungen müssen jeden Abschnitt der Zusammenfassung genehmigen, bevor die Nachricht gestartet werden kann. Der Standardstatus für jeden Abschnitt ist **Pending Approval**.

{% tabs %}
{% tab campaign %}
Um eine Campaign zu starten, müssen Sie diese Komponenten genehmigen:

- **Messages:** Dies ist die Campaign-Nachricht.
- **Delivery:** Dies ist der Zustellungstyp und bestimmt, wann Nutzer:innen die Campaign erhalten.
- **Target Audience:** Dies bestimmt, wer die Campaign erhalten wird.
- **Conversion Events:** Dies ist die Metrik, die Sie für Engagement- und Berichtszwecke verfolgen.
{% endtab %}

{% tab canvas %}
Um ein Canvas zu starten, müssen Sie diese Schlüsselkomponenten genehmigen:

- **Conversion Events:** Dies ist die Metrik, die Sie für Engagement- und Berichtszwecke verfolgen.
- **Entry Schedule:** Dies umfasst den Typ des Entry-Zeitplans und wann Nutzer:innen das Canvas betreten.
- **Target Audience:** Dies bestimmt, wer dieses Canvas betreten wird.
- **Send Settings:** Dies sind die Sendeeinstellungen für alle Schritte im Canvas.
- **Build Canvas:** Dies ist die Canvas-User-Journey.
{% endtab %}
{% endtabs %}

## Den Genehmigungs-Workflow aktivieren {#turning-on-the-approval-workflow}

Standardmäßig ist die Einstellung für den Genehmigungs-Workflow für Campaigns und Canvases deaktiviert. Um dieses Feature zu aktivieren, gehen Sie zu **Settings** > **Approval Workflow** und wählen Sie den entsprechenden Schalter:

- **Use approval workflow for all Campaigns in [Ihrem Workspace]**
- **Use approval workflow for all Canvases in [Ihrem Workspace]**

{% alert important %}
Die Campaign-Genehmigung wird für [API-Kampagnen]({{site.baseurl}}/api/api_campaigns/) und [Transaktions-E-Mail-Kampagnen]({{site.baseurl}}/user_guide/channels/transactional_email/create_a_transactional_email/) nicht unterstützt.
{% endalert %}

## Nutzer:innen-Berechtigungen festlegen {#setting-user-permissions}

Nachdem Sie den Genehmigungs-Workflow aktiviert haben, müssen Sie Nutzer:innen-Berechtigungen festlegen, damit Ihre Unternehmensnutzer:innen Campaigns und Canvases genehmigen oder ablehnen können. Beide Berechtigungen können auch auf Workspaces oder [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams/) angewendet oder einem [Berechtigungsset]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/#permission-sets) hinzugefügt werden.

{% tabs %}
{% tab campaign %}
Sie benötigen die [Berechtigung „Approve and Deny Campaigns“]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/#managing-limited-and-team-role-permissions). Diese Berechtigung steuert, wer den Genehmigungsstatus einer Campaign aktualisieren kann. Mit dieser Berechtigung können Sie Folgendes tun:

- Die Campaign selbst genehmigen
- Die Campaign genehmigen und starten
- Die Campaign genehmigen, aber nicht starten (eine andere Person mit der Berechtigung „Send Campaigns, Canvases“ kann die Campaign starten)
- Die Campaign weder genehmigen noch starten

Nachdem die Genehmigungsstatus im Schritt **Summary** festgelegt wurden, setzen alle nachfolgenden Änderungen an der Campaign beim Speichern alle Genehmigungsstatus zurück. Dies gilt für alle Änderungen, die entweder in einem Campaign-Entwurf oder einer bereits gestarteten Campaign vorgenommen werden. Wenn Sie beispielsweise nur Änderungen an der Zielgruppe vornehmen, setzt der Schritt **Summary** die Genehmigungsstatus für alle Abschnitte auf den Standardstatus **Pending Approval** zurück.

{% endtab %}

{% tab canvas %}
Sie benötigen die [Berechtigung „Approve and Deny Canvases“]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/#managing-limited-and-team-role-permissions). Diese Berechtigung steuert, wer den Genehmigungsstatus eines Canvas aktualisieren kann. Mit dieser Berechtigung können Sie Folgendes tun:

- Das Canvas selbst genehmigen
- Das Canvas genehmigen und starten
- Das Canvas genehmigen, aber nicht starten (eine andere Person mit der Berechtigung „Send Campaigns, Canvases“ kann das Canvas starten)
- Das Canvas weder genehmigen noch starten

Nachdem die Genehmigungsstatus im Schritt **Summary** festgelegt wurden, setzen alle nachfolgenden Änderungen am Canvas beim Speichern alle Genehmigungsstatus zurück. Dies gilt für alle Änderungen, die entweder in einem Canvas-Entwurf oder einem bereits gestarteten Canvas vorgenommen werden. Wenn Sie beispielsweise nur Änderungen an der Zielgruppe vornehmen, setzt der Schritt **Summary** die Genehmigungsstatus für alle Abschnitte auf den Standardstatus **Pending Approval** zurück.

{% alert note %}
**Genehmigungsstatus und Speichern**

- Wenn Sie im Schritt **Summary** für einen Abschnitt auf **Approve** klicken, wird diese Genehmigung sofort gespeichert.
- Der Button **Save** speichert Änderungen am Canvas-Inhalt und den Einstellungen, nicht den Genehmigungsstatus.

Um den Verlust von Genehmigungen zu vermeiden:

1. Nehmen Sie alle benötigten Canvas-Änderungen vor und klicken Sie dann auf **Save**.
2. Nachdem das Canvas gespeichert wurde, genehmigen Sie die relevanten Abschnitte im Schritt **Summary**.
3. Klicken Sie nur dann erneut auf **Save**, wenn Sie nach der Genehmigung weitere Canvas-Änderungen vornehmen. Wenn Sie das Canvas ändern und speichern, werden alle Genehmigungsstatus auf **Pending Approval** zurückgesetzt.
{% endalert %}
{% endtab %}
{% endtabs %}

{% alert important %}
Um eine aktive Campaign zu bearbeiten, benötigen Sie die Berechtigung „Approve and Deny Campaigns“. Nutzer:innen müssen ihre Änderungen genehmigen, da eine Entwurfsversion von Campaigns noch nicht verfügbar ist. Bei Canvases ist dies anders, da Nutzer:innen Änderungen vornehmen und als Entwurf speichern können, und eine andere Person das Canvas genehmigen und starten kann.
{% endalert %}