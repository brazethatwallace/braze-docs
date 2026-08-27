Braze ajoute les en-têtes suivants aux requêtes de contenu connecté sortantes. La plupart ne sont définis que si vous ne les avez pas déjà fournis dans l'étiquette. Les en-têtes que vous fournissez avec `:headers`, des identifiants ou des options d'étiquette sont envoyés tels quels.

| En-tête | Quand Braze le définit |
| --- | --- |
| `User-Agent` | Si vous ne l'avez pas déjà défini, Braze envoie `Braze Sender <version>`. La chaîne de version peut changer. Si vous filtrez le trafic par `User-Agent`, autorisez toutes les valeurs commençant par `Braze Sender`. Pour envoyer une valeur constante, définissez `User-Agent` dans `:headers`. |
| `X-Braze-Sender-Version` | Toujours défini sur la version de l'expéditeur de contenu connecté. |
| `Accept-Encoding` | Si vous ne l'avez pas déjà défini, Braze envoie `gzip`. |
| `Authorization` | Si l'URL contient un nom d'utilisateur et un mot de passe (`user:pass@host`), Braze ajoute un en-tête Basic `Authorization` dérivé de ces identifiants. Un en-tête `Authorization` explicite le remplace. Préférez [`:basic_auth`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#using-basic-authentication) ou `:headers` plutôt que de placer les identifiants dans l'URL. |
| `Host` | Nom d'hôte extrait de l'URL de la requête (par exemple, `www.example.com` pour `https://www.example.com/abc/123`), sauf si vous définissez un en-tête `Host`. |
| `Content-Length` | Taille du corps de la requête en octets lorsqu'un corps est présent. |
| `BrazeToBraze` | Défini sur `true` uniquement pour les requêtes vers les endpoints REST de Braze. Omis pour les autres destinations. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="En-têtes de requête sortante ajoutés par Braze au contenu connecté" }