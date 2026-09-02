Vor dem Erstellen von WhatsApp-Templates müssen Sie das [WhatsApp-Setup]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/) abschließen und über Folgendes verfügen:
- Ein aktives WhatsApp Business-Konto (WABA), das mit Braze verbunden ist
- Entsprechende Abo-Gruppen, die in Ihrem WABA konfiguriert sind
- Medien-Assets (Bilder oder Videos), die zum Hochladen bereit sind
- Braze-Berechtigungen für Nutzer:innen ohne Administratorrechte
    - Damit Nutzer:innen neue Templates im Template Builder erstellen können:
        - „WhatsApp-Nachrichten-Templates anzeigen“
        - „WhatsApp-Nachrichten-Templates bearbeiten“
    - Damit Nutzer:innen Campaigns oder Canvases mit Karussell-Templates verfassen können:
        - „WhatsApp-Nachrichten-Templates anzeigen“
- Grundkenntnisse in Liquid-Templating (optional, für dynamischen Content)

{% alert important %}
Alle Telefonnummern und Abo-Gruppen innerhalb desselben WhatsApp Business-Kontos (WABA) teilen sich die Templates. Wenn Sie mehrere Abo-Gruppen innerhalb eines WABA haben, können alle auf dieselben Karussell-Templates zugreifen. Templates werden jedoch nicht über verschiedene WABAs hinweg geteilt.
{% endalert %}