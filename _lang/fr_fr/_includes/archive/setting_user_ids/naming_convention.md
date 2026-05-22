Chez Braze, nous **recommandons vivement** de nommer les ID utilisateurs, également appelés ID externes, au format [UUID et GUID](https://en.wikipedia.org/wiki/Universally_unique_identifier). Les UUID et les GUID sont des identifiants universellement uniques constitués d'un nombre de 128 bits utilisé pour identifier les informations dans les systèmes informatiques. Cela signifie que ces UUID sont longs, aléatoires et bien distribués. Si vous choisissez une autre méthode pour nommer vos ID utilisateurs, ils doivent également être longs, aléatoires et bien répartis. Il est également important de noter que les ID utilisateurs sont **sensibles à la casse**. Par exemple, « Abcdef » est un utilisateur différent de « abcdef ».

Si vous constatez que vos ID utilisateurs comprennent des noms, des adresses e-mail, des horodatages ou des incréments, nous vous suggérons d'adopter une nouvelle méthode de nommage plus sûre afin que vos ID utilisateurs ne soient pas faciles à deviner ou à usurper. Si vous choisissez d'inclure ce type d'information dans vos ID utilisateurs, nous **recommandons vivement** d'ajouter notre fonctionnalité d'[authentification SDK]({{site.baseurl}}/developer_guide/authentication/) pour empêcher l'usurpation d'identité.

La communication de ces informations à des tiers peut permettre à des personnes extérieures à votre organisation de comprendre la structure de vos ID utilisateurs, ce qui expose votre organisation à des mises à jour potentiellement malveillantes ou à la suppression d'informations. Le choix d'une convention de nommage correcte dès le départ est l'une des étapes les plus importantes de la mise en place des ID utilisateurs. Toutefois, une migration est possible en utilisant notre [endpoint de migration de l'ID externe]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/).

| Nommage des ID utilisateurs |
| Recommandé | Non recommandé |
| ------------ | ----------- |
| 123e4567-e89b-12d3-a456-836199333115 | JonDoe829525552 |
| 8c0b3728-7fa7-4c68-a32e-12de1d3ed2d5 | Anna@email.com |
| f0a9b506-3c5b-4d86-b16a-94fc4fc3f7b0 | CompanyName-1-2-19 |
| 2d9e96a1-8f15-4eaf-bf7b-eb8c34e25962 | jon-doe-1-2-19 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Table" }