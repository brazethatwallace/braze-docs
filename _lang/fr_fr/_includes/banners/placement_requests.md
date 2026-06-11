Lorsque vous [créez des emplacements dans votre application ou votre site web]({{site.baseurl}}/developer_guide/banners/placements/#requestBannersRefresh), votre application envoie une requête à Braze afin de récupérer les messages Bannière pour chaque emplacement.

- Vous pouvez demander jusqu'à **10 emplacements par requête d'actualisation**.
- Pour chaque emplacement, Braze renvoie la **Bannière ayant la priorité la plus élevée** que l'utilisateur est éligible à recevoir.
- Si plus de 10 emplacements sont demandés lors d'une actualisation, seuls les 10 premiers sont renvoyés ; les autres sont ignorés.

Par exemple, une application peut demander trois emplacements dans une requête d'actualisation : `homepage_promo`, `cart_abandonment` et `seasonal_offer`. Chaque requête renvoie la Bannière la plus pertinente pour cet emplacement.

#### Limite de débit pour les requêtes d'actualisation {#rate-limiting-for-refresh-requests}

Si vous utilisez des versions du SDK antérieures (avant Swift 13.1.0, Android 38.0.0, Web 6.1.0, React Native 17.0.0 et Flutter 15.0.0), une seule requête d'actualisation est autorisée par session utilisateur.

Si vous utilisez les versions minimales les plus récentes du SDK (Swift 13.1.0+, Android 38.0.0+, Web 6.1.0+, React Native 17.0.0+ et Flutter 15.0.0+), les requêtes d'actualisation sont contrôlées par un algorithme de type « token bucket » afin d'éviter une interrogation excessive :

- Chaque session utilisateur commence avec cinq jetons d'actualisation.
- Les jetons se rechargent à raison d'un jeton toutes les 180 secondes (3 minutes).

Chaque appel explicite à `requestBannersRefresh` consomme un jeton. L'actualisation automatique qui se produit au début d'une nouvelle session ou lorsque `changeUser` est appelé ne consomme pas de jeton, car cette actualisation publie la dernière Bannière mise en cache pour cet utilisateur. Si vous tentez une actualisation alors qu'aucun jeton n'est disponible, le SDK n'effectue pas la requête et enregistre une erreur jusqu'à ce qu'un jeton soit réapprovisionné. Ceci est important pour les mises à jour en cours de session et les mises à jour déclenchées par des événements. Pour mettre en œuvre des mises à jour dynamiques (par exemple, après qu'un utilisateur a effectué une action sur la même page), appelez la méthode d'actualisation après l'enregistrement de l'événement personnalisé, mais tenez compte du délai nécessaire à Braze pour ingérer et traiter l'événement avant que l'utilisateur ne soit éligible à une autre Campaign Bannière.