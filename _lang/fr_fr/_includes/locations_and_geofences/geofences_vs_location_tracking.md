Dans Braze, les géorepérages et le suivi de localisation servent des objectifs différents :

| | Suivi de localisation | Géorepérages |
|---|---|---|
| Objectif | Segmenter les utilisateurs en fonction de l'endroit où ils se trouvaient | Déclencher des messages lorsque les utilisateurs entrent dans une zone ou en sortent |
| Utilisation typique | `Most Recent Location` et filtres associés | Campaigns en temps réel lors de l'entrée ou de la sortie d'un géorepérage |
| Moment d'évaluation de la localisation | Mis à jour lorsque l'application est ouverte (début de session) ; reflète la dernière localisation connue de l'utilisateur | Surveillé par le système d'exploitation lorsque les autorisations de localisation le permettent, y compris lorsque l'application est en arrière-plan ou fermée |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Location tracking compared to geofences" }

- **Suivi de localisation :** collecte et stocke la localisation la plus récente de chaque utilisateur sur son profil. Vous utilisez ces données pour une segmentation rétrospective — par exemple, le filtre `Most Recent Location` cible les utilisateurs en fonction de l'endroit où ils ont ouvert votre application pour la dernière fois, pas nécessairement de l'endroit où ils se trouvent en temps réel.
- **Géorepérages :** définissent des limites virtuelles autour d'une latitude, d'une longitude et d'un rayon. Lorsqu'un utilisateur entre dans une limite ou en sort, Braze peut déclencher des actions telles que l'envoi d'une campagne. Les géorepérages nécessitent une configuration supplémentaire du SDK au-delà du suivi de localisation de base.

Ces deux fonctionnalités nécessitent que les utilisateurs accordent les autorisations de localisation. Si un utilisateur désactive le suivi de localisation, les données de localisation précédemment stockées ne sont pas automatiquement supprimées de son profil, mais aucune nouvelle donnée de localisation n'est collectée.