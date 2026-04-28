---
nav_title: Unterschied zwischen Blocklisting und Löschen
article_title: Unterschied zwischen Blocklisting und Löschen
page_order: 2

page_type: solution
description: "Dieser Hilfeartikel erläutert den Unterschied zwischen dem Blocklisting und dem Löschen von Attributen."
---

# Unterschied zwischen Blocklisting und Löschen {#difference-between-blocklisting-and-deleting}

Um den Unterschied zwischen dem Blocklisting und dem Löschen angepasster Daten in Braze zu verstehen, sehen Sie sich die Ergebnisse der jeweiligen Aktion an:

- **Blocklisting:** Wenn angepasste Attribute, Ereignisse oder Käufe auf die Blocklist gesetzt werden, bleiben sie in den Nutzerprofilen erhalten, aber Braze verarbeitet keine neuen Daten mehr für diese Objekte.
- **Löschen:** Wenn angepasste Attribute, Ereignisse oder Käufe gelöscht werden, entfernt Braze diese Daten aus den Nutzerprofilen. Gelöschte angepasste Attribute und Ereignisse werden für sieben Tage in den Status `Trashed` verschoben, in dem Sie sie wiederherstellen können. Nach sieben Tagen löscht Braze sie endgültig. Das Löschen verhindert außerdem nicht den Eingang neuer Daten. Stellen Sie daher sicher, dass die Daten nicht mehr über Ihr SDK, Ihre API oder CSV-Importe gesendet werden, bevor Sie sie löschen.

## Was sollte ich tun? {#which-should-i-do}

Für das Blocklisting muss Braze die Blocklisting-Informationen an das Gerät jeder Nutzerin und jedes Nutzers senden, was eine datenintensive Operation ist, die idealerweise vermieden werden sollte. Wenn die Liste zu groß ist (> 100 Attribute, Ereignisse oder Käufe), kann Ihre App zudem langsamer werden.

Wenn Sie nicht mehr vorhaben, Attribute an Braze zu senden, wäre das Löschen der empfohlene Ansatz.

Unabhängig von Ihrem Vorgehen erscheinen die entfernten angepassten Attribute, Ereignisse und Käufe nicht mehr auf der Seite **Workspace verwalten**, wodurch sie auch als Segment-Filter entfernt werden. Wenn Sie angepasste Daten löschen, entfernt Braze diese Daten auf Nutzerebene aus den Profilen.