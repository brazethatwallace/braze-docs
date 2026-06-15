---
nav_title: Validation de l'e-mail
article_title: Validation des e-mails
alias: "/email_validation/"
page_order: 3
page_type: reference
description: "Le présent article de référence couvre les règles de validation des pièces locales et hôtes pour les adresses e-mail."
channel: email

---

# Validation des e-mails

> Le présent article de référence couvre les règles de validation des pièces locales et hôtes pour les adresses e-mail. La validation est utilisée pour les adresses e-mail du tableau de bord, les adresses e-mail des utilisateurs finaux (vos clients) et les adresses d'expéditeur et de réponse d'un message électronique.

## Fonctionnement

Braze valide une adresse e-mail lorsqu'elle est mise à jour, importée par API, téléchargée au format CSV, SDK ou modifiée dans le tableau de bord. Les adresses e-mail ne doivent pas contenir d'espaces. Si vous utilisez l'API, les espaces blancs renvoient une erreur `400`.

Braze rejette certains caractères et marque l'adresse comme non valide. Si un e-mail est renvoyé, Braze marque l'adresse comme non valide et ne modifie pas le statut de l'abonnement. Si le corps de l'e-mail contient des caractères [ASCII](https://en.wikipedia.org/wiki/ASCII) non standard, Braze n'envoie pas l'e-mail.

{% details Caractères acceptés %}
- Lettres (A-Z)
- Chiffres (0-9)
- Symboles
	- -
	- &#94;
	- +
	- $
	- '
	- &
	- #
	- /
	- %
	- *
	- =
	- `
	- |
	- ~
	- !
	- ?
	- . (seulement entre les lettres ou d'autres caractères)
{% enddetails %}

{% details Caractères non acceptés %}
- Espaces blancs (ASCII et Unicode)
{% enddetails %}

Cette validation est une vérification syntaxique et non un service de validation. L'un des objectifs de ce processus est de prendre en charge les caractères internationaux (tels que l'UTF-8) dans la partie locale de l'adresse e-mail.

Braze valide la syntaxe de la partie locale et de la partie hôte d'une adresse e-mail. La partie locale correspond à tout ce qui précède l'arobase (@) ; la partie hôte correspond à tout ce qui suit. La partie locale peut commencer et se terminer par n'importe quel caractère autorisé, à l'exception du point (.). Ce processus ne vérifie pas si le domaine dispose d'un serveur MX valide ni si un utilisateur existe sur ce domaine.

{% alert important %}
Si la partie domaine contient des caractères ASCII non standard, elle devra être [encodée en Punycode](https://www.punycoder.com/) avant d'être transmise à Braze.
{% endalert %}

Si Braze reçoit une requête pour ajouter un utilisateur avec une adresse e-mail non valide, l'API renvoie une erreur. Pour un téléchargement CSV, Braze crée l'utilisateur mais omet l'adresse e-mail non valide.

## Règles de validation de la partie locale

### Validation générale des e-mails

Pour la plupart des domaines, la partie locale doit respecter les paramètres suivants :
- Peut contenir n'importe quelle lettre ou chiffre, y compris les lettres et chiffres Unicode, ainsi que les caractères suivants : (+) (&) (#) (_) (-) (^) ou (/)
- Peut contenir, mais ne peut pas commencer ni se terminer par le caractère suivant : (.)
- Ne peut pas contenir de guillemets doubles (")
- Doit comporter entre 1 et 64 caractères

L'expression régulière suivante peut être utilisée pour vérifier si une adresse e-mail sera considérée comme valide :
```
/\A([a-zA-Z0-9_\-\^+$'\&#\/!%\*=\?`\|~]|[[^\p{ASCII}\p{Space}]&&\p{Alnum}\p{Punct}\p{S}])(([a-zA-Z0-9_\-\^+$'\&#\/!%\*=\?`\|~\.]|[[^\p{ASCII}\p{Space}]&&\p{Alnum}\p{Punct}\p{S}])*([a-zA-Z0-9_\-\^+$'\&#\/!%\*=\?`\|~]|[[^\p{ASCII}\p{Space}]&&\p{Alnum}\p{Punct}\p{S}]))?\z/
```

### Adresses Gmail

Si la partie domaine est Gmail, la partie locale doit comporter au moins deux caractères et respecter la validation par expression régulière indiquée ci-dessus.

### Domaines Microsoft

Si le domaine hôte inclut « msn », « hotmail », « outlook » ou « live », Braze utilise l'expression régulière suivante pour valider la partie locale : `/\A\w[\-\w]*(?:\.[\-\w]+)*\z/i`

La partie locale d'une adresse Microsoft doit respecter les paramètres suivants :

- Peut commencer par un caractère (a-z), un tiret bas (_) ou un chiffre (0-9).
- Peut contenir n'importe quel caractère alphanumérique (a-z ou 0-9) ou un tiret bas (_)
- Peut contenir les caractères suivants : (.) ou (-)
- Ne peut pas commencer par un point (.)
- Ne peut pas contenir deux points consécutifs ou plus (.)
- Ne peut pas se terminer par un point (.)

Le test de validation vérifie si la partie locale précédant le « + » correspond à l'expression régulière.

## Règles de validation de la partie hôte

La partie hôte ne peut pas être une adresse IPv4 ou IPv6. Le domaine de premier niveau (tel que .com, .org, .net) ne peut pas être entièrement numérique.

L'expression régulière suivante est utilisée pour valider le domaine :<br>
`/^[a-z\d](?:[a-z\d-]{0,61}[a-z\d])?(?:\.[a-z\d](?:[a-z\d-]{0,61}[a-z\d])?)+$/i`

Le nom de domaine doit respecter les paramètres suivants :

- Se compose de deux ou plusieurs libellés séparés par des points
	- Chaque partie d'un nom de domaine est appelée un « libellé ». Par exemple, le nom de domaine « example.com » se compose du libellé « example » et du libellé « com ».
- Doit contenir au moins un point (.)
- Ne peut pas contenir deux points consécutifs ou plus
- Chaque libellé séparé par un point doit :
	- Contenir uniquement des caractères alphanumériques (a-z ou 0-9) et le tiret (-)
	- Commencer par un caractère alphanumérique (a-z ou 0-9)
	- Se terminer par un caractère alphanumérique (a-z ou 0-9)
	- Comporter entre 1 et 63 caractères

### Validation supplémentaire requise

Le dernier libellé du domaine doit être un domaine de premier niveau (TLD) valide, déterminé par tout ce qui suit le dernier point (.). Ce TLD doit figurer dans la [liste des TLD de l'ICANN](https://data.iana.org/TLD/tlds-alpha-by-domain.txt). Le validateur de Braze vérifie uniquement la syntaxe. Il ne détecte pas les fautes de frappe ni les adresses inexistantes.

{% alert important %}
L'Unicode est accepté uniquement pour la partie locale de l'adresse e-mail. L'Unicode n'est pas accepté pour la partie domaine, mais celle-ci peut être encodée en Punycode.
{% endalert %}