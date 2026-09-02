Os IDs de usuário devem ser definidos para cada um de seus usuários. Eles devem ser imutáveis e acessíveis quando um usuário abre o app. Nomear seus IDs de usuário corretamente desde o início é uma das etapas mais **cruciais** na configuração de IDs de usuário. Sugerimos enfaticamente o uso do padrão da Braze de UUIDs e GUIDs (detalhado na seção a seguir). Também recomendamos enfaticamente que você forneça esse identificador, pois isso permitirá:

- Rastrear seus usuários em dispositivos e plataformas, melhorando a qualidade de seus dados comportamentais e demográficos.
- Importar dados de seus usuários usando nossa [API or interface de programação do aplicativo (API) de dados de usuários]({{site.baseurl}}/developer_guide/rest_api/user_data#user-data).
- Direcionar usuários específicos com nossa [API or interface de programação do aplicativo (API) de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging) para mensagens gerais e transacionais.

{% alert note %}
Se tal identificador não estiver disponível, a Braze atribuirá um identificador único aos seus usuários, mas você não terá os recursos listados para IDs de usuário. Você deve evitar definir IDs de usuário para usuários para os quais você não possui um identificador exclusivo vinculado a eles como indivíduos. Passar um identificador de dispositivo não oferece nenhum benefício em comparação com o rastreamento automático de usuários anônimos que a Braze oferece por padrão.
{% endalert %}

{% alert warning %}
Se quiser incluir um valor identificável como ID de usuário, para maior segurança, **recomendamos enfaticamente** adicionar o recurso de [autenticação do SDK or kit de desenvolvimento de software]({{site.baseurl}}/developer_guide/authentication) para evitar a simulação de usuário.
{% endalert %}