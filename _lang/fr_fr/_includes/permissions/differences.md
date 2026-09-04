{% if include.content == "Differences" %}

Vous pouvez utiliser les [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams), les [ensembles d'autorisations]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions#creating-a-permission-set) et les [rôles utilisateur]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions#creating-a-role) pour gérer l'accès et les responsabilités des utilisateurs de l'entreprise au sein de Braze. Chaque fonctionnalité englobe un ensemble différent d'autorisations et de contrôles d'accès.

### Différences clés {#key-differences}

De manière générale, chaque fonctionnalité a une portée différente :
- Les ensembles d'autorisations déterminent les actions que les utilisateurs de l'entreprise peuvent effectuer dans tous les espaces de travail.
- Les rôles déterminent les actions que les utilisateurs de l'entreprise peuvent effectuer dans des espaces de travail spécifiques.
- Les Teams gèrent les audiences que les utilisateurs de l'entreprise peuvent contacter avec leurs messages.

| Fonctionnalité | Ce que vous pouvez faire | Portée&nbsp;de&nbsp;l'accès |
| - | - | - |
| [Ensembles d'autorisations]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions#creating-a-permission-set) | Regroupez les autorisations liées à des domaines ou à des actions spécifiques (par exemple « Développeurs » et « Marketeurs »), puis appliquez-les aux utilisateurs de l'entreprise qui ont besoin des mêmes autorisations dans différents espaces de travail. | À l'échelle de l'entreprise |
| [Rôles]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions#creating-a-role) | Regroupez les autorisations personnalisées individuelles et les contrôles d'accès à l'espace de travail (par exemple « Marketeur - Fashion Brands », où l'utilisateur dispose de certaines autorisations associées à son rôle de marketeur et est limité aux espaces de travail « Fashion Brands »). Attribuez ensuite un rôle aux utilisateurs de l'entreprise afin de leur accorder directement les autorisations associées et l'accès à l'espace de travail. <br><br>Les utilisateurs disposant de ce niveau d'accès sont généralement des gestionnaires travaillant dans des configurations plus strictement contrôlées, avec de nombreuses marques ou espaces de travail régionaux regroupés dans un seul tableau de bord. | Espaces de travail spécifiques |
| [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams#creating-teams) | Limitez l'accès des utilisateurs de l'entreprise aux ressources en fonction de l'audience (par exemple l'emplacement de la clientèle, la langue et les attributs personnalisés). <br><br>Les utilisateurs disposant de ce niveau d'accès sont généralement responsables d'un domaine spécifique au sein de la marque sur laquelle ils travaillent, comme la création de contenu spécifique à une langue pour une marque multilingue. | Tableau de bord spécifique |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Différences clés" }

{% endif %}