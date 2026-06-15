---
page_order: 5
nav_title: Termes à connaître
article_title: Termes à connaître pour les SMS, MMS et RCS
alias: /sms_terms_to_know/

layout: glossary_page
glossary_top_header: "Termes à connaître"
glossary_top_text: "Consultez les termes suivants pour en savoir plus sur les écosystèmes, technologies et processus liés aux SMS, MMS et RCS."
page_type: glossary
description: "Ce glossaire définit les différents termes relatifs aux SMS, MMS et RCS que vous devez connaître."
channel:
  - SMS
  - MMS
  - RCS

glossaries:
  - name: SMS (Short Message Service)
    description: Un canal de communication créé en 1980 et l'une des plus anciennes technologies de messagerie texte. C'est également l'un des canaux de messagerie texte les plus répandus et les plus fréquemment utilisés. Ce canal est un moyen plus direct d'atteindre vos utilisateurs et clients que la plupart des autres canaux de communication, car il utilise leur numéro de téléphone personnel pour les joindre. De ce fait, les SMS sont soumis à davantage de règles et de réglementations que les autres canaux de communication.
  - name: Short Code
    description: Il s'agit d'une séquence courte et mémorable de 5 à 6 chiffres qui permet aux expéditeurs d'envoyer plus de messages à des débits plus réguliers que les codes longs (un message par seconde).<br><br>Un code court ou un code long est requis.
  - name: Long Code
    description: Il s'agit du numéro de téléphone standard à 10 chiffres (dans la plupart des pays) qui permet aux expéditeurs d'envoyer des messages au rythme d'un message par seconde.<br><br>Un code court ou un code long est requis.
  - name: Encoding
    description: La conversion de n'importe quel contenu en une forme codée. Le contenu SMS peut être encodé en GSM-7 ou en UCS-2.
  - name: GSM-7 Encoding (Global System for Mobile Communications)
    description: Le GSM-7 est la norme d'encodage la plus courante pour la plupart des messages SMS. Il utilise la majorité des alphabets grec et anglais, ainsi que quelques caractères supplémentaires. Vous pouvez en apprendre davantage sur l'encodage GSM-7 et les jeux de caractères utilisables sur <a href='https://en.wikipedia.org/wiki/GSM_03.38#GSM_7-bit_default_alphabet_and_extension_table_of_3GPP_TS_23.038_.2F_GSM_03.38' title="Alphabet par défaut GSM 7 bits et table d'extension">Wikipédia</a>. Les langues telles que le chinois, le coréen ou le japonais doivent être transmises en utilisant l'encodage de caractères 16 bits UCS-2. <br> <br> Vous pouvez estimer que la limite de caractères par segment pour ce type d'encodage est de 128 caractères.
  - name: UCS-2 Encoding (Universal Coded Character Set)
    description: L'encodage UCS-2 est une norme d'encodage de secours, notamment lorsqu'un message ne peut pas être encodé en GSM-7 ou lorsqu'une langue nécessite plus de 128 caractères pour être rendue. L'UCS-2 se mesure mieux en <a href='https://en.wikipedia.org/wiki/Code_point'>points de code</a>, par opposition aux « caractères ». Quoi qu'il en soit, vous pouvez estimer que la limite de caractères par segment pour ce type d'encodage est de 67 caractères.
  - name: Subscription Groups for SMS
    description: Les groupes d'abonnement sont un outil Braze qui vous permet de cibler des niveaux d'abonnement spécifiques d'utilisateurs ou de clients. Les groupes d'abonnement pour les SMS sont construits en interne en fonction de votre service de messagerie et ne peuvent pas être partagés entre les espaces de travail.
  - name: Message Segments
    description: Un segment de message est un regroupement d'un nombre défini de caractères maximum (160 pour l'encodage GSM-7 ; 67 pour l'encodage UCS-2) qui sera envoyé en un seul envoi SMS. Si vous envoyez un SMS de 161 caractères en utilisant l'encodage GSM-7, vous constaterez que deux (2) segments de message ont été envoyés. L'envoi de plusieurs segments de message peut entraîner des frais supplémentaires.
  - name: Message Service
    description: Un ensemble de codes longs, codes courts et identifiants alphanumériques utilisés pour envoyer vos messages SMS avec Braze.
  - name: Keyword
    description: "Un mot court envoyé à un code court ou long pour interagir avec un programme SMS prédéfini ou pour demander le désabonnement d'un programme spécifique ou de tous les programmes sur un code. Par exemple, <code>STOP</code>. Les mots-clés doivent <br> - être alphanumériques <br> - ne pas contenir d'espaces <br> - comporter moins de 10 caractères. <br> <br> Une combinaison spécifique de mot-clé et de code court ne peut être utilisée que sur un seul programme actif à la fois. Si un mot-clé déjà utilisé par un autre programme est saisi, une erreur de validation apparaîtra. <br> <br> Il existe deux catégories de mots-clés obligatoires auxquelles tous les fournisseurs de contenu SMS doivent se conformer : <code>STOP</code> et <code>HELP</code>."
  - name: Mandatory Keyword HELP
    description: Pour chaque programme créé dans la plateforme SMS Campaign Manager, le contenu de ce mot-clé doit être fourni et doit respecter les bonnes pratiques et la conformité des opérateurs par pays ou région dans lesquels le trafic SMS est envoyé et reçu. Dans la plupart des cas, ce contenu doit inclure une brève explication du programme SMS et la procédure de désabonnement.
  - name: Global STOP Keywords
    description: Les variantes incluent <code>STOP</code>, <code>END</code>, <code>QUIT</code>, <code>UNSUBSCRIBE</code>, <code>CANCEL</code>, <code>STOPALL</code>. Ceux-ci sont appelés <code>Global-Stop-Keywords</code>. Si l'un de ces mots-clés est envoyé par SMS à un code court ou long, le numéro de téléphone mobile (le numéro de téléphone mobile d'origine) est désabonné de tous les programmes SMS actifs sur ce code auxquels il est associé.
  - name: Vanity Code
    description: Un code court personnalisé est un numéro de téléphone de 5 à 6 chiffres spécifiquement choisi par une marque. Les codes courts personnalisés sont associés à la marque et plus faciles à mémoriser pour les consommateurs.
  - name: Shared Short Code
    description: Lorsque vous utilisez un code court partagé, tous les messages texte, quelle que soit l'entreprise ou l'organisation qui les envoie, arrivent sur l'appareil mobile du consommateur depuis le même numéro de téléphone de 5 à 6 chiffres. Bien que les codes courts partagés soient relativement peu coûteux et immédiatement disponibles, cela signifie que votre entreprise ne disposera pas d'un code court dédié et sera soumise au respect du protocole par les autres entreprises utilisant votre code court partagé.
  - name: Alphanumeric Sender ID
    description: L'identifiant d'expéditeur alphanumérique vous permet de définir le nom de votre entreprise ou de votre marque comme identifiant d'expéditeur en utilisant des caractères alphanumériques lors de l'envoi de messages unidirectionnels vers les pays pris en charge.
  - name: Toll-Free Number
    description: Un numéro de téléphone gratuit est un numéro pour lequel tous les appels entrants sont facturés au destinataire plutôt qu'à l'abonné téléphonique à l'origine de l'appel. Les numéros gratuits aux États-Unis et au Canada sont compatibles SMS, et les abonnés sont facturés pour les messages texte entrants et sortants.<br><br>La messagerie par numéro gratuit fonctionne mieux lorsque votre cas d'utilisation est de personne à personne, comme le support client ou les ventes, où l'expéditeur et le destinataire échangent par SMS.
  - name: One-Way Messaging
    description: La messagerie unidirectionnelle vous permet de communiquer avec vos clients en envoyant des messages texte. Elle est utile si vous utilisez un identifiant d'expéditeur alphanumérique dans des marchés où les codes longs et courts ne sont pas disponibles.
  - name: Two-Way Messaging
    description: La messagerie bidirectionnelle vous permet de mener une conversation en envoyant et en recevant des messages texte.
  - name: MMS (Multimedia Message Service)
    description: Le MMS est utilisé pour envoyer des messages contenant des ressources multimédias (JPEG, GIF, PNG) vers des téléphones mobiles. Comme les SMS, le MMS est un canal de communication à haute urgence qui vous permet de communiquer immédiatement avec vos clients. Le MMS étend les capacités des SMS en vous offrant la possibilité d'ajouter des médias à des SMS autrement composés uniquement de texte.
  - name: RCS (Rich Communication Services)
    description: Le Rich Communication Services (RCS) enrichit les SMS traditionnels en permettant aux marques de diffuser des messages non seulement informatifs, mais aussi bien plus engageants. Le RCS apporte des fonctionnalités telles que des médias de haute qualité, des boutons interactifs et des profils d'expéditeur de marque directement dans les applications de messagerie préinstallées des utilisateurs.
  - name: RCS-Verified Sender
    description: L'entité émettrice d'un message RCS, ou ce que le destinataire voit sur son appareil pour identifier la provenance du message. Les expéditeurs vérifiés RCS contiennent un nom d'entreprise, une légende, une identité visuelle de marque et un badge de vérification. Après avoir fourni les informations d'enregistrement de l'expéditeur RCS nécessaires à Braze, Braze se charge de l'enregistrement et de la configuration du groupe d'abonnement.
  - name: SMS Fallback
    description: Si un message RCS ne peut pas être livré (par exemple, en raison d'un manque de prise en charge par l'opérateur dans la région), Braze tentera tout de même de livrer le message par SMS lorsqu'un code SMS existe dans le groupe d'abonnement.
  - name: Basic RCS
    description: Messages RCS en texte uniquement de 160 caractères maximum. Facturés comme un seul message. Cette catégorie est utilisée uniquement dans le modèle global.
  - name: Single RCS
    description: Messages RCS en texte uniquement de plus de 160 caractères ou incluant des éléments enrichis, comme des boutons ou des médias. Facturés comme un seul message. Cette catégorie est utilisée uniquement dans le modèle global.
  - name: Rich RCS
    description: Messages RCS en texte uniquement, avec ou sans suggestions ou boutons limités. Facturés par segment (160 octets UTF-8). Cette catégorie est utilisée uniquement dans le modèle des États-Unis.
  - name: Rich Media RCS
    description: Messages RCS incluant un fichier multimédia (image, vidéo) ou une Rich Card. Facturés comme un seul message, quelle que soit la longueur du message. Cette catégorie est utilisée uniquement dans le modèle des États-Unis.
---