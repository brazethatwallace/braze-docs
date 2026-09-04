---
nav_title: "Telefonnummern von Nutzer:innen"
article_title: WhatsApp-Telefonnummern von Nutzer:innen
page_order: 3
description: "Dieser Referenzartikel behandelt die Formatierung von WhatsApp-Telefonnummern, den Import von Telefonnummern sowie das Hinzufügen von Nutzer:innen zu WhatsApp-Abo-Gruppen."
page_type: reference
channel:
  - WhatsApp

---

# Telefonnummern von Nutzer:innen {#user-phone-numbers}

> In diesem Artikel werden verschiedene Themen rund um die Telefonnummern Ihrer Nutzer:innen bzw. Kund:innen behandelt.

Telefonnummern werden im Kundenprofil in lokalen Formaten angezeigt, entsprechen aber nicht dem Format, das Sie zum Importieren der Nummer verwenden (`(724) 123 4567`).

## Telefonnummern importieren {#importing-phone-numbers}

Sie können Telefonnummern importieren, indem Sie [eine CSV-Datei hochladen]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv) oder [über die API]({{site.baseurl}}/api/endpoints/user_data/post_user_track) Nutzer:innen erstellen.

### Formatierung {#formatting}

Es ist wichtig, Nicht-US-Nummern im [`E.164`](https://en.wikipedia.org/wiki/e.164)-Format zu importieren, einschließlich des „+“ und der Landesvorwahl. Alle Telefonnummern, die nicht in diesem Format angegeben werden, werden als US-Nummern interpretiert.

Wenn eine Telefonnummer in das E.164-Format umgewandelt wird, aber die Validierung nicht besteht, kann Braze keine WhatsApp-Nachrichten an diese Nummer senden. Alle Nutzer:innen mit Telefonnummern, die nicht formatierbar sind, verlassen automatisch einen Canvas-Schritt, der WhatsApp enthält.

Alle US-Nummern müssen gültige, 10-stellige Telefonnummern mit einer gültigen Vorwahl sein. Sie können ohne das `+` und die Landesvorwahl eingegeben werden, da Braze alle gültigen, 10-stelligen Telefonnummern als US-Nummern annimmt und zuordnet.

Alle internationalen Nummern sollten mit einem `+` beginnen, gefolgt von der Landesvorwahl und dann der Telefonnummer (z. B. `+442071838750`).

![Screenshot zur Formatierung.]({% image_buster /assets/img/sms/e164.png %}){: style="max-width:50%;border: 0;"}

Um jedoch die Genauigkeit sicherzustellen, wenn Sie in mehrere Regionen mit unterschiedlichen Landes- oder Ortsvorwahlen senden, wird empfohlen, das `E.164`-Format auch für US-basierte Telefonnummern zu verwenden.

Die Unterschiede zwischen der lokalen Nummernformatierung und der universellen `E.164`-Formatierung können Sie in der folgenden Tabelle sehen:

| Land | Lokal | Landesvorwahl | `E.164` |
|---|---|---|---|
| USA | `4155552671` | 1 | `+14155552671` |
| Großbritannien | `02071838750` | 44 | `+442071838750` |
| Brasilien | `1155256325` | 55 | `+551155256325` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Formatierung" }

### Nutzer:innen zu einer WhatsApp-Abo-Gruppe hinzufügen {#adding-users-to-whatsapp-a-subscription-group}

Damit Kund:innen eine WhatsApp-Nachricht erhalten können, müssen sie eine gültige Telefonnummer haben und in eine Abo-Gruppe eingewilligt haben. Weitere Informationen finden Sie unter [WhatsApp-Abo-Gruppen]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups).


### Mehrere Nutzer:innen mit derselben Telefonnummer {#multiple-users-with-the-same-phone-number}

Wenn mehrere Nutzer:innen innerhalb eines Segments einer einzelnen Campaign oder eines Canvas-Schritts dieselbe Telefonnummer haben, dedupliziert Braze den Versand und sendet nur eine Nachricht an diese eine Telefonnummer.