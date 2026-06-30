{% assign portal_url = site.baseurl | append: '/user_guide/administer/personal/product_portal' %}
{% assign feature_label = include.feature | default: 'this capability' %}

{% if include.context == 'gap' %}
If you're interested in {{ feature_label }}, submit [product feedback]({{ portal_url }}).
{% elsif include.context == 'new_feature' %}
{% assign feature_label = include.feature | default: 'This capability' %}
{{ feature_label }} is generally available. Share how it's working for your team through [product feedback]({{ portal_url }}).
{% elsif include.context == 'pain_point' and include.channel == 'feature' %}
Want {{ feature_label }}? Consider leaving [product feedback]({{ portal_url }}).
{% elsif include.context == 'pain_point' and include.channel == 'ux' %}
If you have feedback about {{ feature_label }}, open the **Support** menu in the global header and select **Share feedback** to send us your thoughts.
{% endif %}
