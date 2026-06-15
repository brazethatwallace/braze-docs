---
nav_title: Optimierte Zustellung
article_title: WhatsApp-Nachrichten mit optimierter Zustellung
page_order: 1
description: "Dieser Referenzartikel behandelt die Schritte zum Erstellen einer WhatsApp-Nachricht mit optimierter Zustellung."
page_type: reference
tool:
  - Campaigns
channel:
  - WhatsApp
---

# WhatsApp-Nachrichten mit optimierter Zustellung {#whatsapp-messages-with-optimized-delivery}

> Steigern Sie die Zustellbarkeit und das Engagement, indem Sie mehr der richtigen Nutzer:innen auf WhatsApp mit dynamischer, Engagement-basierter Zustellung erreichen.

WhatsApp-Nachrichten mit optimierter Zustellung werden über Metas [Marketing Messages API for WhatsApp](https://developers.facebook.com/docs/whatsapp/marketing-messages-api-for-whatsapp) (MM API for WhatsApp) gesendet, die eine dynamische, Engagement-basierte Zustellung bietet. Das bedeutet, dass Ihre Nachrichten mit hohem Engagement (z. B. solche, die mit höherer Wahrscheinlichkeit gelesen und angeklickt werden) mehr Nutzer:innen erreichen können, die wahrscheinlich damit interagieren. WhatsApp betrachtet Ihre Nachrichten als Nachrichten mit hohem Engagement, wenn sie erwartet, relevant und zeitnah sind und daher mit höherer Wahrscheinlichkeit gelesen und angeklickt werden.

Marken können mit der MM API for WhatsApp eine gleiche oder höhere Zustellbarkeit im Vergleich zur Cloud API erwarten. In Indien wurden bei Marketing-Nachrichten mit hohem Engagement laut Meta bis zu 9 % mehr Nachrichten im Vergleich zur Cloud API zugestellt. Beachten Sie, dass die MM API for WhatsApp dennoch keine 100%ige Zustellbarkeit garantiert.

### Regionale Verfügbarkeit {#regional-availability}

Die Verfügbarkeit und die Optimierungsmöglichkeiten der optimierten Zustellung hängen von der Region der geschäftlichen Telefonnummer und der Nutzer:innen ab. Weitere Informationen finden Sie unter [Geographic availability of features](https://developers.facebook.com/docs/whatsapp/marketing-messages-lite-api/get-started#geographic-availability-of-features).

## Optimierte Zustellung einrichten {#setting-up-optimized-delivery}

1. Gehen Sie in Braze zu **Partner Integrations** > **Technology Partners** > **WhatsApp**.
2. Wählen Sie im Abschnitt **Optimize your sending with optimized delivery** die Option **Upgrade setting**, um den [Embedded-Sign-up-Workflow]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/embedded_signup/) zu starten.

![Der Abschnitt „WhatsApp Message Integration“ mit einer Option zur Optimierung des Versands mit optimierter Zustellung.]({% image_buster /assets/img/whatsapp/whatsapp_messaging_integration.png %})

{: start="3"}
3. Nachdem die optimierte Zustellung aktiviert wurde, zeigen Ihre Kontodetails unter **WhatsApp Business Account Management** den Status der optimierten Zustellung an.

![Der Abschnitt „WhatsApp Business Account Management“ mit einer aufgelisteten Abo-Gruppe, die einen aktiven Nummernstatus hat.]({% image_buster /assets/img/whatsapp/optimized_delivery_message.png %})

Alternativ können Sie die optimierte Zustellung direkt in Ihrem WhatsApp-Manager aktivieren und dann mit dem Versand in Braze beginnen.

### Fehlerbehebung bei der Einrichtung {#troubleshooting-your-setup}

- **Allgemeiner Fehler:** Wenn während des Upgrades etwas schiefgeht, wird dieses Fehlerbanner angezeigt und empfiehlt Ihnen, den [Support zu kontaktieren]({{site.baseurl}}/braze_support/).
- **Fehler wegen fehlender Berechtigung:** Wenn Sie von Meta eingeschränkt sind, wird dieses Fehlerbanner angezeigt: „At least one WhatsApp Business Account is restricted by Meta. Accounts must be in good standing to upgrade.“ Dieses Banner kann erst geschlossen werden, wenn das Problem behoben ist.

## Optimierte Zustellung in Campaigns und Canvases verwenden {#using-optimized-delivery-in-campaigns-and-canvases}

Die optimierte Zustellung sollte für **Marketing-Nachrichten** verwendet werden. Braze entfernt automatisch die Option für optimierte Zustellung bei **Utility-, Authentifizierungs-, Service- und Antwortnachrichten**, die weiterhin über die Cloud API gesendet werden sollten, was die Standardeinstellung ist.

### Zustellmethode auswählen {#selecting-the-delivery-method}

1. Gehen Sie im Braze WhatsApp-Editor für eine Campaign oder einen Canvas-Nachrichtenschritt zum Tab **Settings**.
2. Im Abschnitt **Delivery method** ist das Kontrollkästchen für **Optimized Delivery (Recommended)** standardmäßig aktiviert, wenn Ihr WhatsApp Business Account (WABA) aktiviert ist. Wenn Sie die optimierte Zustellung für diese bestimmte Nachricht nicht verwenden möchten, deaktivieren Sie das Kontrollkästchen.
- Wenn Sie die optimierte Zustellung auswählen, diese aber nicht verfügbar ist, wird die Nachricht automatisch auf die Cloud-API-Methode zurückgesetzt.

![Nachrichten-Editor mit einem Vorschau-Tab, der ein Kontrollkästchen zur Auswahl der optimierten Zustellung enthält.]({% image_buster /assets/img/whatsapp/delivery_method_settings.png %})

### Retargeting von Nutzer:innen auf anderen Braze-Kanälen {#retargeting-users-on-other-braze-channels}

Da die MM API for WhatsApp keine 100%ige Zustellbarkeit bietet, ist es wichtig zu verstehen, wie Sie Nutzer:innen, die Ihre Nachricht möglicherweise nicht erhalten haben, auf anderen Kanälen erneut ansprechen können.

Für das Retargeting von Nutzer:innen empfehlen wir, ein Segment von Nutzer:innen zu erstellen, die eine bestimmte Nachricht nicht erhalten haben. Filtern Sie dazu nach dem Fehlercode `131049`, der angibt, dass eine Marketing-Template-Nachricht aufgrund der WhatsApp-Durchsetzung des Marketing-Template-Limits pro Nutzer:in nicht gesendet wurde. Sie können dies mit Braze-Currents oder SQL-Segmenterweiterungen tun:

- **Braze-Currents:** Exportieren Sie Nachrichtenfehler-Ereignisse mit Braze-Currents. Sie können diese Daten dann verwenden, um ein angepasstes Attribut im Nutzerprofil zu aktualisieren (z. B. `whatsapp_failed_last_msg: true`), das Sie als Filter für Ihre Retargeting-Campaign verwenden können.
- **SQL-Segmenterweiterungen:** Wenn Sie Zugriff auf dieses Feature haben, können Sie SQL verwenden, um die Nachrichtenfehlerprotokolle abzufragen und ein Segment dieser Nutzer:innen zu erstellen. Anschließend können Sie dieses Segment auf einem anderen Kanal ansprechen.