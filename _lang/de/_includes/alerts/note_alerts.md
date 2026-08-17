{% if include.alert == 'Content Cards frequency capping' %}

{% alert note %}
Frequency-Capping gilt nicht für Content Cards.
{% endalert %}

{% endif %}

{% if include.alert == 'Custom Attributes time attribute' %}

{% alert note %}
Ein Datums-String wie „12-1-2021“ oder „12/1/2021“ wird in ein Datetime-Objekt umgewandelt und als [Zeitattribut]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes#time) behandelt.
{% endalert %}

{% endif %}

{% if include.alert == 'Manage custom data storage' %}

{% alert note %}
Alle Nutzerprofildaten (angepasste Events, angepasste Attribute, angepasste Daten) werden gespeichert, solange diese Profile aktiv sind.
{% endalert %}

{% endif %}

{% if include.alert == 'Segment profiles first app use' %}

{% alert note %}
Braze erstellt erst dann Profile für Nutzer:innen, wenn diese die App zum ersten Mal verwendet haben. Sie können also keine Nutzer:innen ansprechen, die Ihre App noch nicht geöffnet haben.
{% endalert %}

{% endif %}

{% if include.alert == 'Shopify attributes REST API' %}

{% alert note %}
Alle Attribute stammen aus der Braze REST API.
{% endalert %}

{% endif %}

{% if include.alert == 'subscription group limit' %}

{% alert note %}
Sie können bis zu 450 Abo-Gruppen pro Workspace hinzufügen.
{% endalert %}

{% endif %}

{% if include.alert == 'GIF platform support' %}

{% alert note %}
GIFs werden in Android-Push-Benachrichtigungen nicht unterstützt. Dies ist eine Einschränkung der Android-Plattform, keine Einschränkung von Braze.
<br><br>
- Für In-App-Nachrichten und Content Cards auf Android können Sie GIFs unterstützen, indem Sie eine Drittanbieter-Bildbibliothek wie [Glide](https://bumptech.github.io/glide/) oder [Fresco](https://frescolib.org/) integrieren.
<br>
- Auf iOS unterstützen Push-Benachrichtigungen GIFs. In-App-Nachrichten und Content Cards erfordern einen angepassten GIF-Bildanbieter.
{% endalert %}

{% endif %}