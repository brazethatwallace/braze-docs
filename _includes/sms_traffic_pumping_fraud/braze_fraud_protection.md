{% if include.detail %}
### How else does Braze help protect your company against fraud?

While your engineering team controls the front-end entry points on your website, Braze deploys robust internal alerting and real-time anomaly detection capabilities behind the scenes to actively monitor potentially fraudulent send volume spikes across our entire infrastructure.

If a bot network hits your site and triggers an unusual velocity spike or a sudden wave of traffic to high-cost international destinations, our internal systems flag that abnormal behavior. This allows us to quickly identify threats and work with you to mitigate impact, protecting both your delivery rates and your billing integrity.
{% else %}
### What else does Braze do to protect your company against fraud?

In addition to guidance and support from your account team and [Geographic permissions]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups/geographic_permissions/), Braze maintains internal monitoring for unusual patterns and will proactively engage with customers when we identify anomalous activity on their account.
{% endif %}
