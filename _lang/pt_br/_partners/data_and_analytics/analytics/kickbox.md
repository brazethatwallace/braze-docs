---
nav_title: Kickbox
article_title: Kickbox
alias: /partners/kickbox/
description: "Este artigo de referência descreve a parceria entre a Braze e a Kickbox, uma plataforma de verificação de e-mail usada para validar listas de e-mail ou integrar a verificação em seu aplicativo."
page_type: partner
search_tag: Partner
---

# Kickbox

> [Kickbox](https://kickbox.com/) é uma plataforma de verificação de e-mail tudo-em-um, repleta de recursos, integrações e segurança que você precisa para manter seus dados de e-mail limpos e entregáveis. A integração da Kickbox melhora a entregabilidade das suas Campaigns na Braze usando a verificação de e-mail da Kickbox para identificar endereços de e-mail não entregáveis e de baixa qualidade antes de você enviar.

A Kickbox permite que você valide a qualidade dos endereços de e-mail dos seus usuários no momento em que um perfil de usuário é atualizado na Braze. Isso é alcançado por meio de um Canvas ou fluxo de trabalho de Campaign dedicado, que é acionado pela população do campo `email` de um perfil.

O Canvas ou Campaign enviará um webhook para a Kickbox, compartilhando o endereço de e-mail do usuário. A Kickbox validará o endereço de e-mail e usará o endpoint da REST API da Braze para atualizar o perfil do usuário com um atributo personalizado detalhando sua qualidade.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| --------------------------------------|-------------------------------------------------------------------------------|
| Conta da Kickbox | Uma conta ativa da Kickbox é necessária para usar esta integração. |
| Chave da API REST da Braze | Uma chave da API REST da Braze com permissões `users.track`. <br><br>Isso pode ser criado no dashboard da Braze acessando **Configurações** > **APIs e identificadores** > **Chaves de API** |
| Solicitar acesso à integração. | Peça à equipe de suporte da Kickbox para conceder acesso à integração da Braze. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração {#integration}

Para integrar com a Kickbox, siga as etapas em [Integrando com a Braze](https://docs.kickbox.com/docs/integrating-with-braze#/).

## Casos de uso {#use-cases}

### Verificação em massa {#bulk-verification}

Você também pode optar por verificar toda a sua lista a cada poucos meses ou trimestralmente, para se proteger de e-mails que sofrem churn ou listas que se degradam ao longo do tempo e lentamente diminuem sua entregabilidade.

Para fazer isso, você precisará alterar as **Configurações de entrada** do fluxo de trabalho, conforme descrito pela Kickbox. Em vez de selecionar **Entrega baseada em ação**, selecione **Agendado**. Então escolha um horário agendado para que sua lista seja verificada de uma só vez.

### Crie Segments verificados {#create-verified-segments}

Os atributos personalizados da Kickbox têm um esquema consistente, correspondendo aos seguintes exemplos.

{% raw %}
```json
   {
  "attributes": [
    {
      "email": "example1@kickbox.com",
      "_update_existing_only": true,
      "success": true,
      "code": null,
      "message": null,
      "result": "deliverable",
      "reason": "accepted_email",
      "role": false,
      "free": false,
      "disposable": false,
      "accept_all": false,
      "did_you_mean": null,
      "sendex": 1,
      "user": "example1",
      "domain": "kickbox.com"
    },
    {
      "email": "example2@gamil.com",
      "_update_existing_only": true,
      "success": true,
      "code": "44312",
      "message": "SMTP verification",
      "result": "undeliverable",
      "reason": "rejected_email",
      "role": false,
      "free": false,
      "disposable": false,
      "accept_all": false,
      "did_you_mean": "example2@gmail.com",
      "sendex": 0.23,
      "user": "example2",
      "domain": "gamil.com"
    }
  ]
}
```
{% endraw %}

Isso significa que você pode criar Segments de público com usuários que possuem endereços de e-mail verificados, para que suas Campaigns e Canvas tenham uma taxa de sucesso de entrega mais alta, protegendo sua reputação com os ESPs.

Para fazer isso, siga estas etapas:

1. Na Braze, acesse **Audience** > **Segments** > **Create Segment**.
2. Na seção **Filter Group**, adicione o filtro **Custom Attribute** e selecione "result" no menu suspenso.

Dependendo do seu caso de uso, pode ser apropriado criar um Segment onde o atributo personalizado da Kickbox "result" exista em um perfil de usuário, ou onde seu valor seja igual a "deliverable". Esse filtro pode ser usado sozinho para criar um Segment, ou pode ser parte de todos os Segments futuros para validar todos os usuários dentro deles.