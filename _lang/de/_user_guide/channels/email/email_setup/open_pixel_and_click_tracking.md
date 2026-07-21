---
nav_title: Öffnungspixel und Klick-Tracking
article_title: E-Mail-Öffnungspixel und Klick-Tracking
page_order: 9
page_type: reference
description: "Dieser Referenzartikel behandelt die Implementierung von Öffnungspixel- und Klick-Tracking."

---

# E-Mail-Öffnungspixel und Klick-Tracking {#email-open-pixel-and-click-tracking}

> [Öffnungspixel-Tracking]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#update-the-placement) und Klick-Tracking können für jedes Nutzerprofil ein- oder ausgeschaltet werden. Diese Flexibilität hilft Ihnen, regionale Datenschutzgesetze einzuhalten, wenn ein einzelnes Nutzerprofil angibt, dass es nicht mehr getrackt werden möchte.

## Öffnungspixel- oder Klick-Tracking aktivieren {#turning-on-open-pixel-or-click-tracking}

Beim Importieren oder Aktualisieren eines Nutzerprofils über [API]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields), [CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv) oder [Cloud-Datenaufnahme (CDI)]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion) stehen Ihnen zwei Felder zur Verfügung:

- `email_open_tracking_disabled`: Akzeptiert `true` oder `false`. Setzen Sie den Wert auf `false`, um das Öffnungs-Tracking-Pixel zu allen zukünftigen E-Mails hinzuzufügen, die an diese:n Nutzer:in gesendet werden. Nur für SparkPost und SendGrid verfügbar.
- `email_click_tracking_disabled`: Akzeptiert `true` oder `false`. Setzen Sie den Wert auf `false`, um Klick-Tracking zu allen Links in zukünftigen E-Mails hinzuzufügen, die an diese:n Nutzer:in gesendet werden. Nur für SparkPost und SendGrid verfügbar.

Zur Referenz: Diese Informationen werden im Nutzerprofil unter den E-Mail-**Kontakteinstellungen** im Tab **Engagement** angezeigt.

![Felder für E-Mail-Öffnungs- und Klick-Tracking-Pixel im Tab „Engagement“ eines Nutzerprofils]({% image_buster /assets/img_archive/open_click_user_profile.png %}){: style="max-width:60%;"}

## Anforderungen für Klick-Tracking-Links {#click-tracking-link-requirements}

Das Klick-Tracking von Braze schreibt nur Links um, die `http://`- oder `https://`-URLs verwenden. Links mit anderen Schemata wie `mailto:` oder `tel:` werden nicht per Klick-Tracking erfasst.

Um Klicks auf Telefonnummern oder E-Mail-Adressen zu tracken, verwenden Sie eine `https://`-Weiterleitungs-URL, die zum `tel:`- oder `mailto:`-Ziel weiterleitet.