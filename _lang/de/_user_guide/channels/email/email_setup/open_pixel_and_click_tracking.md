---
nav_title: Öffnungspixel und Klick-Tracking
article_title: E-Mail-Öffnungspixel und Klick-Tracking
page_order: 9
page_type: reference
description: "Dieser Referenzartikel behandelt die Implementierung von Öffnungspixel- und Klick-Tracking."

---

# E-Mail-Öffnungspixel und Klick-Tracking {#email-open-pixel-and-click-tracking}

> [Öffnungspixel-Tracking]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#update-the-placement) und Klick-Tracking können für jedes Kundenprofil ein- oder ausgeschaltet werden. Diese Flexibilität hilft Ihnen, regionale Datenschutzgesetze einzuhalten, wenn ein einzelnes Kundenprofil angibt, dass es nicht mehr getrackt werden möchte.

## Aktivieren des Öffnungspixels oder Klick-Trackings {#turning-on-open-pixel-or-click-tracking}

Wenn Sie ein Kundenprofil über die [API]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields), per [CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv) oder über [Cloud Data Ingestion (CDI)]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion) importieren oder aktualisieren, stehen Ihnen zwei Felder zur Bearbeitung zur Verfügung:

- `email_open_tracking_disabled`: Akzeptiert `true` oder `false`. Setzen Sie den Wert auf `false`, um das Öffnungs-Tracking-Pixel zu allen zukünftigen E-Mails hinzuzufügen, die an diese Nutzer:in gesendet werden.
- `email_click_tracking_disabled`: Akzeptiert `true` oder `false`. Setzen Sie den Wert auf `false`, um Klick-Tracking zu allen Links in zukünftigen E-Mails hinzuzufügen, die an diese Nutzer:in gesendet werden.

Diese Informationen werden zur Referenz im Kundenprofil unter den E-Mail-**Kontakteinstellungen** im Tab **Engagement** angezeigt.

![Felder für E-Mail-Öffnungs- und Klick-Tracking-Pixel im Tab „Engagement“ eines Nutzerprofils]({% image_buster /assets/img_archive/open_click_user_profile.png %}){: style="max-width:60%;"}

## Anforderungen für Klick-Tracking-Links {#click-tracking-link-requirements}

Das Klick-Tracking von Braze schreibt nur Links um, die `http://`- oder `https://`-URLs verwenden. Links, die andere Schemata wie `mailto:` oder `tel:` verwenden, werden nicht per Klick-Tracking erfasst.

Um Klicks auf Telefonnummern oder E-Mail-Adressen zu tracken, verwenden Sie eine `https://`-Weiterleitungs-URL, die stattdessen zum `tel:`- oder `mailto:`-Ziel weiterleitet.

### Klick-Tracking-URL-Muster {#click-tracking-url-patterns}

Wenn Ihr E-Mail-Anbieter (E-Mail-Anbieter) einen Link für das Klick-Tracking umschreibt, verwendet die resultierende URL Ihre Klick-Tracking-Domain und ein E-Mail-Anbieter-spezifisches Pfadpräfix. Die Muster, die jeder E-Mail-Anbieter generiert und die Sie für Firewall-Regeln und Sicherheits-Allowlists benötigen, finden Sie unter [Klick- und Öffnungs-Tracking-URL-Muster]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl#click-and-open-tracking-url-patterns).