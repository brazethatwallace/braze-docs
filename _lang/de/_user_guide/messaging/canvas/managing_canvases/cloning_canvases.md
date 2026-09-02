---
nav_title: Canvase Klon or klonen
article_title: Canvase Klon or klonen
page_order: 3
alias: "/cloning_canvases/"
description: "Dieser Referenzartikel beschreibt, wie Sie ein Canvas aus dem ursprünglichen Canvas-Editor in den Canvas-Flow-Workflow Klon or klonen."
tool: Canvas
---

# Canvase zu Canvas Flow Klon or klonen {#clone-canvases-to-canvas-flow}

> Wenn Sie ein bestehendes Canvas aus dem ursprünglichen Editor haben, können Sie dieses Canvas Klon or klonen, um eine Kopie in Canvas Flow zu erstellen. Durch den Wechsel zum aktuellen Canvas-Workflow erhalten Sie Zugang zu leichtgewichtigen [Canvas-Komponenten]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components), [persistenten Entry-Eigenschaften]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/canvas_persistent_entry_properties) und [Bearbeitungen nach dem Start]({{site.baseurl}}/post-launch_edits). Ihr ursprüngliches Canvas wird dabei weder verändert noch gelöscht.

{% alert important %}
Sie können keine Canvase mehr mit der ursprünglichen Canvas-Erfahrung erstellen oder duplizieren. Braze empfiehlt, dass Kund:innen, die die ursprüngliche Canvas-Erfahrung nutzen, zu Canvas Flow wechseln – der aktuellen Canvas-Erfahrung.
{% endalert %}

Um Ihr Canvas zu Klon or klonen, gehen Sie wie folgt vor:

1. Gehen Sie zum Canvas-Dashboard.
2. Identifizieren Sie das Canvas, von dem Sie eine Kopie im Canvas-Flow-Workflow erstellen möchten. Sie können Canvase mit dem Status **Draft**, **Active** oder **Stopped** Klon or klonen.
3. Klicken Sie auf <i class="fas fa-ellipsis-vertical"></i> **More actions** und wählen Sie **Klon or klonen to Canvas Flow**.

![Flussdiagramm für den beschriebenen Prozess.]({% image_buster /assets/img_archive/clone_to_v2_workflow.png %}){: style="max-width:25%;"}

{: start="4"}
4. Geben Sie den Namen Ihres neuen Canvas ein und klicken Sie auf **Klon or klonen to Canvas Flow**.

![Beispiel für die modale Platzierung einer Content-Card.]({% image_buster /assets/img_archive/clone_to_v2_modal.png %}){: style="max-width:70%;"}

Jetzt haben Sie zwei Versionen Ihres Canvas: das ursprüngliche Canvas und die Canvas-Flow-Version. Ihr ursprüngliches Canvas behält seinen ursprünglichen Status, und das geklonte Canvas hat den Status **Draft**. Sie können weiterhin auf das ursprüngliche Canvas zugreifen, aber Braze empfiehlt, den Canvas-Flow-Workflow zu verwenden, um Ihre Canvase weiterzubauen.

Zuvor konnten einige Canvase mit Verzweigungen nicht geklont werden. Jetzt können Sie Canvase mit Verzweigungen Klon or klonen. Beachten Sie, dass das Klon or klonen von Canvase mit Verzweigungen zu nicht verbundenen Schritten führen kann. Beheben Sie diese nicht verbundenen Schritte (Schritte, die keinen vorhergehenden verbundenen Schritt haben), um sicherzustellen, dass Ihre Canvas-Journey korrekt abgebildet ist.

{% alert note %}
Wenn Sie ein aktives Canvas Klon or klonen, sendet Braze weiterhin Nutzer:innen durch das ursprüngliche Canvas. Wir empfehlen, ein Canvas vor dem Klon or klonen zu stoppen, um zu vermeiden, dass doppelte Nachrichten von beiden Canvase an Nutzer:innen gesendet werden.
{% endalert %}

![Canvas-Dashboard mit zwei aufgelisteten Canvase: „V2 Copy of Canvas V1“ und „Canvas V1“. Die „V2 Copy of Canvas V1“ hat ein Symbol, das anzeigt, dass sie den Canvas-Flow-Workflow verwendet.]({% image_buster /assets/img_archive/clone_to_v2_dashboard.png %})

Sie haben das Klon or klonen Ihres Canvas in den Canvas-Flow-Workflow abgeschlossen. Jetzt können Sie Ihre Canvase in dieser aktualisierten Erfahrung weiter aufbauen!

## Empfehlungen {#recommendations}

Um bestehenden Nutzer:innen zu ermöglichen, ihre Journey fortzusetzen, nachdem Sie Ihr ursprüngliches Canvas zu Canvas Flow geklont haben, können Sie Filter zu Ihrem bestehenden Canvas hinzufügen, die verhindern, dass neue Nutzer:innen das neue Canvas betreten.

Wenn die Wiedereintritts-Berechtigung deaktiviert ist, fügen Sie den Filter „Entered Canvas Variation“ hinzu. Wenn die Wiedereintritts-Berechtigung aktiviert ist, gibt es folgende mögliche Methoden, um sicherzustellen, dass Nutzer:innen nicht zweimal dasselbe Canvas betreten:
- Update or aktualisieren or aktualisieren Sie das bestehende Canvas mit einem eindeutigen Tag. Fügen Sie für das neue Canvas den Filter „Last Received Message from Campaign or Canvas with Tag“ hinzu. Dies verhindert, dass Nutzer:innen das Canvas nach einem bestimmten Eintrittsdatum zweimal betreten (Gesamtanzahl der Tage nach dem Versand der letzten Nachricht aus dem ursprünglichen Canvas plus dem Conversion-Fenster).
- **Die folgende Methode protokolliert Datenpunkte.** Update or aktualisieren or aktualisieren Sie das ursprüngliche Canvas mit einem Braze-zu-Braze-Webhook, der beim Eintritt ein angepasstes Attribut mit Datums-Zeitstempel triggert. Dieses Attribut kann verwendet werden, um zu verhindern, dass Nutzer:innen das neue Canvas nach dem angegebenen Datum betreten (Gesamtanzahl der Tage nach dem Versand der letzten Nachricht aus dem ursprünglichen Canvas plus dem Conversion-Fenster).

Für API-getriggerte Canvase stimmen Sie sich mit Ihrem Entwicklerteam ab, um sicherzustellen, dass diese Canvase die neue Canvas-ID verwenden, wenn die neuen Canvase startbereit sind.

Weitere Informationen zu den Unterschieden zwischen dem ursprünglichen Canvas-Editor und der Canvas-Flow-Erfahrung finden Sie in den [Canvas-FAQ]({{site.baseurl}}/user_guide/messaging/canvas/faqs#what-are-the-main-differences-between-the-current-and-original-canvas-editors).