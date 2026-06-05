### Quelles mesures fondamentales immédiates mon entreprise devrait-elle prendre pour prévenir cette fraude ? {#what-immediate-foundational-steps-should-my-company-take-to-prevent-this-fraud}

L'étape la plus critique que votre entreprise puisse franchir au sein de votre plateforme d'engagement client est de minimiser votre surface d'attaque en utilisant des limitations géographiques.

#### Utiliser la liste d'autorisation des autorisations géographiques de Braze {#utilize-the-braze-geographic-permissions-allowlist}

Vous devriez auditer de manière proactive les régions où résident vos clients cibles réels et configurer une liste d'autorisation pour permettre explicitement l'envoi de messages uniquement vers ces pays. Pour les étapes de configuration, consultez [Autorisations géographiques]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups/geographic_permissions/).

##### Bloquer les destinations à haut risque {#block-high-risk-destinations}

Si vous exercez vos activités uniquement en Amérique du Nord ou en Europe occidentale, il n'y a aucune raison de laisser les portes ouvertes aux pays internationaux à coût élevé dans d'autres régions. En règle générale, désactivez de manière proactive tout pays où vous ne commercialisez pas activement ou n'avez pas d'opérations afin d'éliminer toute exposition inutile.

{% if include.detail %}
Évaluez soigneusement toute demande d'ouverture de routes vers des pays signalés comme présentant un **risque élevé de fraude**.

##### Défense en profondeur {#layered-defense}

Les restrictions géographiques constituent une première étape critique, mais ne représentent qu'une couche dans une stratégie de défense en profondeur plus large. Aucun contrôle unique n'est suffisant — la combinaison de plusieurs mesures rend les abus considérablement plus complexes et difficiles à exécuter à grande échelle. Au-delà de la liste d'autorisation géographique, les contrôles clés incluent des protections telles que :

- La validation côté client et côté serveur pour garantir l'intégrité des données
- Une limite de débit raisonnable sur les endpoints vulnérables pour ralentir les soumissions automatisées
- Des jetons CSRF pour s'assurer que les requêtes proviennent de vos formulaires légitimes
- Un CAPTCHA pour dissuader les inscriptions frauduleuses en masse

{% alert note %}
Nous vous recommandons de collaborer avec votre équipe de sécurité interne pour adapter ces suggestions à votre infrastructure spécifique.
{% endalert %}
{% endif %}