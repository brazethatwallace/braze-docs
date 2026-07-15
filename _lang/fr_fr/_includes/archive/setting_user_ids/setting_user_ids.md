Les ID d'utilisateur doivent être définis pour chacun de vos utilisateurs. Ils doivent être immuables et accessibles lorsqu'un utilisateur ouvre l'application. Nommer correctement vos ID d'utilisateur dès le départ est l'une des étapes les plus **cruciales** de la mise en place des ID d'utilisateur. Nous vous recommandons vivement d'utiliser la norme Braze pour les UUID et les GUID (détaillée dans la section suivante). Nous vous recommandons également vivement de fournir cet identifiant, car il vous permettra de :

- Suivre vos utilisateurs sur différents appareils et plateformes, améliorant ainsi la qualité de vos données comportementales et démographiques.
- Importer des données sur vos utilisateurs à l'aide de notre [API de données utilisateur]({{site.baseurl}}/developer_guide/rest_api/user_data#user-data).
- Cibler des utilisateurs spécifiques avec notre [API d'envoi de messages]({{site.baseurl}}/api/endpoints/messaging) pour les messages généraux et transactionnels.

{% alert note %}
Si un tel identifiant n'est pas disponible, Braze attribuera un identifiant unique à vos utilisateurs, mais vous ne disposerez pas des fonctionnalités mentionnées pour les ID d'utilisateur. Évitez de définir des ID d'utilisateur pour les utilisateurs pour lesquels vous ne disposez pas d'un identifiant unique qui leur soit lié en tant qu'individus. La transmission d'un identifiant d'appareil n'offre aucun avantage par rapport au suivi automatique des utilisateurs anonymes que Braze propose par défaut.
{% endalert %}

{% alert warning %}
Si vous souhaitez inclure une valeur identifiable comme ID d'utilisateur, pour plus de sécurité, nous **recommandons vivement** d'ajouter notre fonctionnalité d'[authentification SDK]({{site.baseurl}}/developer_guide/authentication) afin d'empêcher l'usurpation d'identité.
{% endalert %}