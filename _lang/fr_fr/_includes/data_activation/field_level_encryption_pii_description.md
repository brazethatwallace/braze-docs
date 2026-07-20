{% comment %}
  Description du chiffrement au niveau du champ d'identifiant et des informations personnelles identifiables (PII). À utiliser dans la documentation sur le chiffrement au niveau du champ et dans les notes de version.
  Paramètres :
  - link (facultatif) : Si défini, « chiffrement au niveau du champ d'identifiant » sera intégré dans ce lien (e.g. {{site.baseurl}}/user_guide/analytics/field_level_encryption/).
{% endcomment %}
{% if include.link %}
Grâce au [chiffrement au niveau du champ d'identifiant]({{ site.baseurl }}/{{ include.link }}), vous pouvez chiffrer de façon fluide les adresses e-mail avec AWS Key Management Service (KMS) afin de minimiser les informations personnelles identifiables (PII) partagées dans Braze. Le chiffrement remplace les données sensibles par du texte chiffré, c'est-à-dire des informations chiffrées illisibles.
{% else %}
Grâce au chiffrement au niveau du champ d'identifiant, vous pouvez chiffrer de façon fluide les adresses e-mail avec AWS Key Management Service (KMS) afin de minimiser les informations personnelles identifiables (PII) partagées dans Braze. Le chiffrement remplace les données sensibles par du texte chiffré, c'est-à-dire des informations chiffrées illisibles.
{% endif %}