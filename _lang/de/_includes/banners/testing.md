{% if include.page == "testing" %}Während Sie [Ihre Banner-Nachricht verfassen]({{site.baseurl}}/user_guide/message_building_by_channel/banners/create/#compose-a-banner), wählen Sie{% elsif include.page == "campaigns" %}Wählen Sie{% endif %} **Vorschau**, um eine Vorschau Ihres Banners anzuzeigen oder eine Testnachricht zu senden.

![Tab „Vorschau“ des Banner-Composers.]({% image_buster /assets/img/banners/select_preview.png %}){: style="max-width:50%;"}

Beachten Sie, dass Ihre Vorschau aufgrund von Hardware-Unterschieden möglicherweise nicht mit der endgültigen Darstellung auf dem Gerät einer Nutzer:in identisch ist.

Um eine Testnachricht zu senden, fügen Sie entweder eine Inhalts-Testgruppe oder einzelne Nutzer:innen als **Testempfänger:innen** hinzu und wählen Sie dann **Test senden**. Sie können Ihre Testnachricht bis zu 5 Minuten lang auf dem Gerät ansehen. Anschließend können Sie **Vorschau-Link kopieren** auswählen, um einen teilbaren Vorschau-Link zu generieren und zu kopieren, der zeigt, wie das Banner für eine zufällige Nutzer:in aussehen wird. Der Link ist sieben Tage lang gültig, bevor er neu generiert werden muss.

![Tab „Vorschau“ des Banner-Composers.]({% image_buster /assets/img/banners/preview_banner.png %})

Überprüfen Sie beim Durchsehen Ihres Test-Banners Folgendes:

- Ist Ihre Banner-Campaign einer Platzierung zugewiesen?
- Werden die Bilder und Medien auf Ihren Zielgerätetypen und Bildschirmgrößen wie erwartet angezeigt und verhalten sie sich korrekt?
- Führen Ihre Links und Buttons die Nutzer:innen dorthin, wohin sie gelangen sollen?
- Funktioniert Liquid wie erwartet? Haben Sie einen Standardattributwert für den Fall vorgesehen, dass Liquid keine Informationen zurückgibt?
- Ist Ihr Text klar, prägnant und korrekt?

Weitere Informationen finden Sie unter [Testnachrichten senden]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages/).