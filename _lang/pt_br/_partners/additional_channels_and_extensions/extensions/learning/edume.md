---
nav_title: EduMe
article_title: EduMe
description: "Este artigo de referência descreve a parceria entre a Braze e a EduMe, uma ferramenta de treinamento baseada em dispositivos móveis que permite aproveitar o Conteúdo conectado da Braze para dar aos seus usuários acesso aos cursos e lições da EduMe em suas campanhas Braze."
alias: /partners/edume/
page_type: partner
search_tag: Partner

---

# EduMe

> [A EduMe](https://edume.com) é uma ferramenta de treinamento baseada em dispositivos móveis que oferece à sua força de trabalho o conhecimento de que ela precisa para ter sucesso, quando precisar, onde quer que esteja.

_Essa integração é mantida pela EduMe._

## Sobre a integração {#about-the-integration}

A integração entre a Braze e a EduMe aproveita o [Conteúdo conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/#about-connected-content) da Braze para dar aos seus usuários acesso aos cursos e lições da EduMe em suas campanhas Braze. O progresso individual e do grupo pode então ser rastreado pela funcionalidade de relatórios da EduMe.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
|---|---|
| Conta EduMe | É necessário ter uma conta EduMe para aproveitar essa parceria. |
| Chave de API or interface de programação do aplicativo (API) da EduMe | Você deve solicitar uma chave de API or interface de programação do aplicativo (API) ao seu contato de sucesso do cliente da EduMe. Essa chave é usada na sua chamada de Conteúdo conectado da Braze. |
| Segredo de assinatura de link da EduMe | Você deve solicitar ao seu contato de sucesso do cliente na EduMe a configuração de um segredo de assinatura de link para sua organização. Esse segredo é usado para ativar links contínuos no Conteúdo conectado. Você não precisa fazer nada com esse segredo. |
| IDs de grupo e conteúdo da EduMe | Esses identificadores são necessários para configurar suas chamadas de Conteúdo conectado. Entre em contato com o atendimento ao cliente da EduMe para obter ajuda na obtenção desses identificadores. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

### Crie sua chamada de Conteúdo conectado {#create-your-connected-content-call}

Para dar a um usuário acesso a um curso, lição ou pesquisa eNPS e rastrear o progresso dele em relação ao seu ID de usuário interno na EduMe, siga a chamada de API or interface de programação do aplicativo (API) mostrada neste exemplo:

{% raw %}
```
Welcome to my Rickshaw App platform.
Access your onboarding course at:

{% connected_content
  https://connect.edume.com/
  EDUME-CONTENT-LINK-AND-CONTENT-ID&groupId=5681&externalUserId={{${driver_id}}}
  :headers {
       "x-api-key": "YOUR-EDUME-API-KEY"
  }
%}
```
{% endraw %}

1. Substitua `YOUR-EDUME-API-KEY` pela sua chave de API or interface de programação do aplicativo (API) da EduMe.<br><br>
2. Substitua `EDUME-CONTENT-LINK-AND-CONTENT-ID` pela string de link de conteúdo correspondente e pelo identificador de módulo, lição ou pesquisa. Esses identificadores podem ser encontrados na sua conta EduMe.
  - Curso: `getCourseLink?moduleId=12087`
  - Lição: `getLessonLink?lessonId=25805`
  - Pesquisa eNPS: `getSurveyLink?surveyId=654`<br><br>
3. Os usuários que chegam à EduMe por meio desse link são adicionados a uma equipe ou grupo da EduMe de sua escolha. Substitua `groupId` pelo ID da equipe relevante ou pelo ID do grupo da EduMe. Normalmente, usa-se o ID da equipe, exceto para cursos que exigem inscrição, caso em que se deve usar o ID do grupo.<br><br>
4. Inclua um campo apropriado para mapear o campo `externalUserId`. O exemplo de chamada de Conteúdo conectado usa `driver_id`, embora seu campo provavelmente seja diferente. Esse ID está disponível nos relatórios da EduMe, permitindo que você os correlacione com seus sistemas.<br><br>
5. Por fim, personalize e teste sua mensagem conforme necessário. Recomendamos que você envie pelo menos uma mensagem de teste, acesse o conteúdo da EduMe, conclua a lição ou o curso e verifique se a análise de dados da EduMe está sendo registrada.