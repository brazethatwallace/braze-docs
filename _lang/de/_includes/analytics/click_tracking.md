{% if include.section == "UTM parameters" %}

Während Sie mit der Linkverkürzung Ihre URLs automatisch verfolgen können, können Sie auch UTM-Parameter zu Ihren URLs hinzufügen, um die Performance von Campaigns in Analytics-Tools von Drittanbietern wie Google Analytics zu verfolgen.

Um UTM-Parameter zu Ihrer URL hinzuzufügen, gehen Sie wie folgt vor:

1. Beginnen Sie mit Ihrer Basis-URL. Dies ist die URL der Seite, die Sie verfolgen möchten (z. B. `https://www.example.com`).
2. Fügen Sie ein Fragezeichen (?) nach Ihrer Basis-URL ein.
3. Fügen Sie jeden UTM-Parameter durch ein kaufmännisches Und (&) getrennt hinzu.

Ein Beispiel ist `https://www.example.com?utm_source=newsletter&utm_medium=sms`.

{% endif %}

{% if include.section == "Frequently Asked Questions" %}

## Häufig gestellte Fragen {#frequently-asked-questions}

### Sind die Links, die ich beim Testversand erhalte, echte URLs? {#are-the-links-i-receive-when-test-sending-real-urls}

Wenn die Campaign vor dem Testversand als Entwurf gespeichert wurde, ja. Andernfalls handelt es sich um einen Platzhalter-Link. Beachten Sie, dass sich die bei einer gestarteten Campaign gesendete URL von der im Testversand gesendeten unterscheiden kann.

### Kann ich UTM-Parameter zu einer URL hinzufügen, bevor sie gekürzt wird? {#can-i-add-utm-parameters-to-a-url-before-it-is-shortened}

Ja. Es können sowohl statische als auch dynamische Parameter hinzugefügt werden.

### Wie lange bleiben verkürzte URLs gültig? {#how-long-do-shortened-urls-remain-valid}

Personalisierte URLs sind ab dem Zeitpunkt der URL-Registrierung zwei Monate lang gültig. Bei der [einheitlichen Linkverkürzung]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening/?sdktab=unified), die keine Unterscheidung zwischen statisch und personalisiert vornimmt, sind alle Links neun Wochen lang gültig.

### Muss das Braze SDK installiert sein, um Links zu kürzen? {#does-the-braze-sdk-need-to-be-installed-in-order-to-shorten-links}

Nein. Die Linkverkürzung funktioniert ohne jegliche SDK-Integration.

{% endif %}

{% if include.section == "Custom Domains" %}

## Angepasste Domains {#custom-domains}

Die Linkverkürzung ermöglicht es Ihnen auch, Ihre eigene Domain zu verwenden, um das Erscheinungsbild Ihrer verkürzten URLs zu personalisieren und so ein konsistentes Markenimage zu vermitteln. Weitere Informationen finden Sie unter [Angepasste Self-Service-Domains]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/custom_domains/).

{% endif %}