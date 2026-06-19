{% alert note %}
**Comprendre les champs de date :**
- `TIME` et `TIME_MS` : représentent l'heure à laquelle la mise à jour du profil utilisateur a eu lieu dans Braze (en secondes et en millisecondes, respectivement). Pour les données rétro-alimentées, ces valeurs correspondent à l'heure du remplissage rétroactif.
- `SF_UPDATED_AT` : représente l'heure à laquelle les données ont été persistées pour la dernière fois dans Snowflake. Ce champ est particulièrement utile pour déterminer la fraîcheur des données, c'est-à-dire l'heure à laquelle la ligne a été synchronisée le plus récemment avec votre entrepôt de données.
{% endalert %}