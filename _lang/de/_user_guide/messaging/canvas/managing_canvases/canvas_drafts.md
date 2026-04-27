---
nav_title: Entwürfe für Canvas speichern
article_title: Entwürfe für Canvas speichern
alias: "/save_as_draft/"
page_order: 1
description: "Dieser Referenzartikel beschreibt, wie Sie einen Entwurf für ein bereits gestartetes Canvas speichern können."
page_type: reference
tool: Canvas
---

# Entwürfe für Canvas speichern

> Wenn Sie Canvases erstellen und starten, können Sie ein aktives Canvas bearbeiten und als Entwurf speichern, sodass Sie Ihre Änderungen vor einem erneuten Start überprüfen können.

Wenn Sie ein aktives Canvas haben, das umfangreiche Änderungen erfordert, können Sie dieses Feature nutzen, um Änderungen zu erstellen, zu speichern und zu prüfen, **bevor** Sie diese im aktiven Canvas starten.

Wie bei jedem Canvas kann nur eine Person gleichzeitig einen Entwurf bearbeiten, und ein Canvas kann immer nur einen Entwurf haben. Diese Entwürfe verfügen über keine Analytics, da die Entwurfsänderungen noch nicht gestartet wurden.

![Ein Beispiel für ein Canvas im Entwurfsmodus mit einem Banner, das darauf hinweist, dass ein Canvas-Entwurf bearbeitet wird, mit der Option, das aktive Canvas anzuzeigen. In der Fußzeile befinden sich Optionen, um zur Analytics-Ansicht zurückzukehren, als Entwurf zu speichern oder den Entwurf zu starten.]({% image_buster /assets/img_archive/canvas_draft1.png %})

## Einen Entwurf erstellen

So erstellen Sie einen Entwurf:

1. Öffnen Sie ein aktives Canvas.
2. Wählen Sie den Button **Als Entwurf speichern** in der Canvas-Fußzeile aus.

Beachten Sie, dass Änderungen am aktiven Canvas nicht vorgenommen werden können, solange ein Entwurf des Canvas existiert. Sie können das Canvas aktualisieren, um Änderungen anzuwenden, oder den Entwurf verwerfen.

## Das aktive Canvas referenzieren

Um das aktive Canvas zu referenzieren, wählen Sie **Aktives Canvas anzeigen** in der Fußzeile der Analytics-Ansicht oder im Canvas-Header des Entwurfs aus. Um zu einem aktiven Canvas zurückzukehren, wählen Sie **Entwurf bearbeiten** in der Analytics-Ansicht oder der aktiven Canvas-Ansicht aus.

Sie können nur Schritte referenzieren, die bereits vor der Erstellung des Entwurfs gestartet wurden. Das bedeutet: Wenn Sie einen Schritt oder Kanal **nach** der Erstellung des Entwurfs erstellt haben, kann dieser in Ihrem Entwurf nicht referenziert werden.

{% alert note %}
Wenn ein Content-Block in einem Canvas-Entwurf referenziert wird, wird das Canvas in der Einbindungszählung des Content-Blocks aufgeführt. Wird der Content-Block jedoch in einem Entwurf eines **aktiven** Canvas referenziert, wird das Canvas nicht in der Einbindungszählung des Content-Blocks aufgeführt.
{% endalert %}

### Priorisierung von In-App-Nachrichten

Bei Entwürfen eines aktiven Canvas wird die Priorität der In-App-Nachricht innerhalb des Canvas-Builders sofort aktualisiert, wenn jemand die Priorität ändert. Das bedeutet, dass die Canvas-weite Priorität von In-App-Nachrichten sofort auf das aktive Canvas angewendet wird, auch wenn ein Entwurf existiert.

Änderungen der Priorität von In-App-Nachrichten auf Schrittebene werden jedoch als Entwurf gespeichert und erst beim Update des Canvas angewendet. Beispielsweise wird in einem Nachrichtenschritt die Prioritätssortierung erst aktualisiert, wenn der Entwurf gestartet wird, da Schritteinstellungen auf Schrittebene gelten.