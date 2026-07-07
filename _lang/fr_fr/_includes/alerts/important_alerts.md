{% if include.alert == 'Web push private browsing' %}

{% alert important %}
Les fenêtres de navigation privée ne prennent pas en charge les notifications push Web.
{% endalert %}

{% endif %}

{% if include.alert == 'BCC address billable emails' %}

{% alert important %}
L'ajout d'une adresse CCI à votre campagne ou Canvas entraîne le doublement de vos e-mails facturables pour la campagne ou le composant Canvas, car Braze envoie un message à votre utilisateur et un autre à votre adresse CCI.
{% endalert %}

{% endif %}

{% if include.alert == 'Android notification priority' %}

{% alert important %}
Le paramètre Priorité d'affichage des notifications n'est plus utilisé sur les appareils fonctionnant sous Android O ou version ultérieure. Sur ces appareils, définissez la priorité via [la configuration du canal de notification](https://developer.android.com/training/notify-user/channels#importance).
{% endalert %}

{% endif %}

{% if include.alert == "Email via SMS" %}

{% alert important %}
N'envoyez pas d'e-mails transactionnels légalement obligatoires aux passerelles SMS, car il y a de fortes chances que ces e-mails ne soient pas délivrés.
<br><br>
Bien que les e-mails envoyés en utilisant un numéro de téléphone et le domaine de passerelle du fournisseur (connu sous le nom de MM3) puissent être reçus sous forme de message SMS (texte), certains de nos fournisseurs d'e-mail ne prennent pas en charge ce comportement. Par exemple, si vous envoyez un e-mail à un numéro de téléphone T-Mobile (tel que « 9999999999@tmomail.net »), votre message SMS sera envoyé à la personne qui possède ce numéro de téléphone sur le réseau T-Mobile.
<br><br>
Gardez à l'esprit que même si ces e-mails ne sont pas délivrés à la passerelle SMS, ils seront tout de même comptabilisés dans votre facturation d'e-mails. Pour éviter d'envoyer des e-mails à des passerelles non prises en charge, consultez la [liste des noms de domaine des passerelles non prises en charge](https://www.fcc.gov/consumer-governmental-affairs/about-bureau/consumer-policy-division/can-spam/domain-name-downloads).
{% endalert %}

{% endif %}

{% if include.alert == 'SDK auth' %}

{% alert important %}
Pour renforcer la sécurité, nous vous recommandons d'activer notre fonctionnalité d'[authentification SDK]({{site.baseurl}}/developer_guide/authentication) afin d'empêcher l'usurpation d'identité des utilisateurs.
{% endalert %}

{% endif %}

{% if include.alert == 'Preference Center warning' %}

{% alert important %}
Certains navigateurs, comme les applications Naver Android et iOS, ne prennent pas en charge le centre de préférences de Braze. Si vous pensez que certains de vos utilisateurs utilisent ces navigateurs, envisagez de leur proposer d'autres méthodes pour gérer leurs préférences d'e-mail.
{% endalert %}

{% endif %}

{% if include.alert == 'Purchase event deprecation' %}

{% alert important %}
L'ancien événement d'achat passe en mode maintenance. Les clients Braze existants peuvent continuer à utiliser les anciens événements d'achat. Ils continueront de fonctionner normalement, mais les nouvelles fonctionnalités seront désormais développées sur la base des événements recommandés pour le commerce électronique. Braze vous informera bien à l'avance avant qu'une date de fin de vie ne soit fixée. Les nouveaux clients Braze doivent utiliser les [événements recommandés pour le commerce électronique]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/ecommerce_events), car les anciens événements d'achat ne seront pas disponibles.
{% endalert %}

{% endif %}

{% if include.alert == 'Purchase event deprecation for eCommerce filters' %}

{% alert important %}
L'ancien événement d'achat passera en état obsolète (mode maintenance). Les événements d'achat continueront de fonctionner normalement, mais aucune nouvelle fonctionnalité ne sera développée sur cette base, au profit des [événements recommandés pour le commerce électronique]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/ecommerce_events). Lorsque ce sera le cas, les filtres de segment ne s'afficheront plus sous le comportement d'achat.<br><br> Si vous utilisez actuellement les événements d'achat, vous recevrez un préavis concernant les plans de suppression progressive. Pour l'instant, vous pouvez continuer à utiliser les événements d'achat jusqu'à la date officielle de dépréciation. Pour en savoir plus, consultez l'[aperçu des événements recommandés]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events).
{% endalert %}

{% endif %}

{% if include.alert == 'S3 file bucket export' %}

{% alert important %}
Les fichiers exportés stockés dans les compartiments S3 sont automatiquement supprimés après l'expiration du lien de téléchargement (quatre heures après l'envoi de l'e-mail d'exportation, sauf indication contraire).
{% endalert %}

{% endif %}

{% if include.alert == 'Shopify customer create' %}

{% alert important %}
L'intégration Shopify prend en charge les webhooks de création et de mise à jour des clients Shopify, qui se trouvent dans vos paramètres de configuration des données. Lorsqu'un profil utilisateur est créé ou mis à jour dans Shopify, un profil utilisateur correspondant est créé ou mis à jour dans Braze. <br><br>Ces actions ne déclenchent pas d'événements personnalisés dans Braze et servent uniquement à [synchroniser les données utilisateur Shopify avec Braze]({{site.baseurl}}/partners/ecommerce/shopify/shopify_overview#how-the-integration-works). Les données synchronisées comprennent les [attributs personnalisés]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features#supported-shopify-custom-attributes), les [attributs standard]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features#supported-shopify-standard-attributes) et, si cette option est activée dans votre configuration, les [états des groupes d'abonnement]({{site.baseurl}}/partners/ecommerce/shopify/shopify_overview#syncing-shopify-email-and-sms-marketing-opt-ins).
{% endalert %}

{% endif %}

{% if include.alert == 'context variable' %}

{% alert important %}
Les propriétés d'entrée Canvas font partie des variables de contexte Canvas. Cela signifie que `canvas_entry_properties` est référencé en tant que `context`. Chaque variable `context` comprend un nom, un type de données et une valeur pouvant inclure du Liquid. Actuellement, `canvas_entry_properties` reste rétrocompatible. Pour plus de détails, consultez les sections [Contexte]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context#how-it-works) et [Objet de contexte Canvas]({{site.baseurl}}/api/objects_filters/context_object).
{% endalert %}

{% endif %}

{% if include.alert == 'Braze Agents' %}

{% alert important %}
Ce partenaire n'apparaît sur votre page **Partenaires technologiques** que si vous avez activé [Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents). Pour obtenir de l'aide pour démarrer, contactez votre gestionnaire de la satisfaction client.
{% endalert %}

{% endif %}

{% if include.alert == 'time filter types' %}

{% alert important %}
**Choix entre les types de filtre « Jour de l'année » et « Heure »** : lorsque vous filtrez des variables de contexte contenant des dates, sélectionnez le type de comparaison approprié selon que la date se répète chaque année ou non :

- **Utilisez « Jour de l'année »** lorsque la date se répète chaque année (par exemple, les anniversaires, les dates commémoratives ou les fêtes comme Noël). Ce type de comparaison se base sur le jour de l'année (1-365/366), sans tenir compte de l'année.
- **Utilisez « Heure »** lorsque la date est absolue et ne se répète pas (par exemple, les dates de fin de contrat, les dates de rendez-vous ou les dates de renouvellement d'abonnement). Ce type de comparaison se base sur l'horodatage complet, année incluse.

L'utilisation de « Jour de l'année » pour des dates absolues peut produire des résultats incorrects ou inattendus, car le calcul ignore la composante année. Par exemple, si vous comparez une date de fin de contrat en avril pour déterminer si elle se situe dans les 63 prochains jours, « Jour de l'année » peut générer des correspondances erronées, car seuls les numéros de jour sont comparés (119 contre 359) sans tenir compte du fait qu'avril est en réalité dans 188 jours.

**Règle générale** : cette date se répète-t-elle chaque année ? **Oui** → Utilisez « Jour de l'année ». **Non** → Utilisez « Heure ».
{% endalert %}

{% endif %}

{% if include.alert == 'granular permissions ea' %}

{% alert important %}
Les autorisations granulaires sont en accès anticipé. Lorsque la migration sera planifiée pour votre société, vos administrateurs Braze recevront des e-mails et des bannières dans le tableau de bord les informant de la [migration des autorisations granulaires]({{site.baseurl}}/granular_permissions_migration).
{% endalert %}

{% endif %}

{% if include.alert == 'WhatsApp audio and documents' %}

{% alert note %}
La [bibliothèque multimédia de Braze]({{site.baseurl}}/media_library) ne prend en charge que les images et les vidéos. Les fichiers audio et les documents doivent être référencés via une URL hébergée.
{% endalert %}

{% endif %}

{% if include.alert == 'Meta MP4 video issue' %}

{% alert important %}
Meta présente un problème connu qui peut empêcher la lecture de certaines vidéos MP4 sur les appareils Android en raison de paramètres d'encodage ou de conteneur spécifiques. En attendant un correctif permanent, le reformatage du fichier MP4 résout le problème pour la plupart des expéditeurs. Testez toutes les vidéos sur des appareils Android pour vérifier la bonne livrabilité. <br><br>Vous pouvez reformater le fichier MP4 à l'aide d'un outil en ligne, tel que [CloudConvert](https://cloudconvert.com/mp4-converter). Importez votre fichier MP4 dans l'outil, convertissez-le à nouveau en MP4, puis téléchargez le fichier converti.
{% endalert %}

{% endif %}

{% if include.alert == 'Shopify cart token alias' %}

{% alert important %}
Pour cette intégration, l'alias d'utilisateur doit respecter le format suivant afin que Braze puisse associer les webhooks au profil utilisateur correspondant :<br><br>
- `alias_label` : `shopify_cart_${cartToken}`
- `alias_name` : `shopify_cart_token`
{% endalert %}

{% endif %}

{% if include.alert == 'network dependency' %}

{% alert important %}
Les Content Cards, les messages in-app, les bannières et les indicateurs de fonctionnalité dépendent de la connectivité de l'appareil pour se synchroniser avec les serveurs Braze. Les conditions réseau pouvant varier, il est possible que le contenu ou les mises à jour ne soient pas synchronisés, affichés ou supprimés immédiatement (par exemple, si un utilisateur est hors ligne). Nous vous recommandons d'éviter ces canaux pour les mises à jour critiques et urgentes.
{% endalert %}

{% endif %}

{% if include.alert == 'dynamic image URL' %}

{% alert important %}
Si vous intégrez des images via le [contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) ou [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid), assurez-vous que l'URL de votre image commence par `https://`. L'utilisation de `http://` provoquera le plantage de votre application.
{% endalert %}

{% endif %}