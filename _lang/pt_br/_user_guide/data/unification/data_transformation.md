---
nav_title: Transformação de dados
article_title: Transformação de dados
page_order: 2
layout: dev_guide
guide_top_header: "Transformação de dados"
guide_top_text: "A Transformação de Dados da Braze permite que você crie e gerencie integrações de webhook para automatizar o fluxo de dados de plataformas externas para a Braze. Esses dados de usuários recém-integrados podem então impulsionar casos de uso de marketing ainda mais sofisticados. A Transformação de Dados da Braze pode agilizar sua integração de dados, mesmo que você tenha pouca experiência em codificação, e pode ajudar a substituir a dependência da sua equipe de chamadas manuais de API, ferramentas de integração de terceiros ou até mesmo plataformas de dados do cliente."
page_type: landing
description: "Esta landing page contém artigos sobre a Transformação de Dados da Braze, incluindo como criar uma transformação de dados e casos de uso."
alias: /data_transformation/

guide_featured_title: "Artigos da seção"
guide_featured_list:
  - name: Criar uma transformação
    link: /docs/user_guide/data/unification/data_transformation/creating_a_transformation
    image: /assets/img/braze_icons/flip-forward.svg
  - name: Casos de uso
    link: /docs/user_guide/data/unification/data_transformation/use_cases
    image: /assets/img/braze_icons/users-01.svg
---

## Como funciona {#how-it-works}

Muitas plataformas modernas têm "webhooks", ou notificações de API em tempo real, para enviar informações sobre um novo evento ou novos dados de uma plataforma para outra. A Transformação de Dados fornece:

* Um endereço URL da Braze para receber esses webhooks.
* Funcionalidades para transformar a carga útil do webhook com código JavaScript para criar solicitações válidas para vários endpoints da API da Braze, incluindo `/users/track` ou `/catalogs`. Por exemplo, para o destino `/users/track`, você pode escolher quais informações usar do webhook e como deseja que os dados sejam representados nos perfis de usuário da Braze como atributos de usuário, eventos ou compras.
* Registro para realizar garantia de qualidade, solucionar problemas e monitorar o desempenho de suas transformações.

O resultado final é uma integração de webhook que conecta uma plataforma de origem de sua escolha, transformando seus webhooks em atualizações da Braze.

{% details More on webhooks %}
Webhooks são notificações em tempo real enviadas via uma solicitação HTTP POST para um destino específico. Webhooks são frequentemente usados para enviar dados de um ponto a outro, nos quais o webhook pode transmitir dados sobre uma ação que ocorreu e quem esteve envolvido nessa ação.

Por exemplo, uma plataforma de pesquisa pode enviar um webhook para um destino de sua escolha sempre que uma resposta a um formulário online for recebida. Ou uma plataforma de atendimento ao cliente pode enviar um webhook para um destino de sua escolha sempre que um tíquete de atendimento ao cliente for criado.
{% enddetails %}

## Camadas da Transformação de Dados {#data-transformation-tiers}

A tabela a seguir descreve as diferenças entre a versão gratuita e a versão profissional da Transformação de Dados.

| Área | Versão gratuita | Data Transformation Pro |
|----|----|----|
| Transformações ativas | Até 5 por empresa | Até 55 por empresa |
| Por mês | 300.000 solicitações recebidas por mês | 10.300.000 solicitações recebidas por mês |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Camadas da Transformação de Dados" }

{% alert important %}
Para solicitar um upgrade para o Data Transformation Pro, entre em contato com o seu gerente de conta da Braze ou selecione o botão **Request Upgrade** no dashboard da Braze.
{% endalert %}

### Limites de taxa {#rate-limits}

O limite de taxa para as Transformações de Dados da Braze é de 1.000 solicitações de entrada por minuto por espaço de trabalho. Se você tem o Data Transformation Pro e precisa de um limite de taxa maior, entre em contato com o seu gerente de conta da Braze.

## Perguntas frequentes {#frequently-asked-questions}

### O que é sincronizado com a Transformação de Dados da Braze? {#what-gets-synced-with-braze-data-transformation}

Quaisquer dados que a plataforma externa disponibilize em um webhook podem ser sincronizados com a Braze. Quanto mais uma plataforma externa envia via webhooks, mais opções para escolher o que é sincronizado.

### Sou um profissional de marketing. Preciso de recursos de desenvolvedor para usar a Transformação de Dados da Braze? {#im-a-marketer-do-i-need-developer-resources-to-use-braze-data-transformation}

Embora adoraríamos que os desenvolvedores usassem esse recurso também, você não precisa ser um para usá-lo! Profissionais de marketing também podem configurar transformações com sucesso sem recursos de desenvolvedores.

### Ainda posso usar a Transformação de Dados da Braze se minha plataforma externa fornecer apenas um endereço de e-mail ou número de telefone como identificador? {#can-i-still-use-braze-data-transformation-if-my-external-platform-only-gives-an-email-address-or-phone-number-as-an-identifier}

Sim. Você pode ter suas transformações atualizando o endpoint `/users/track` com o [endereço de e-mail ou número de telefone como identificador]({{site.baseurl}}/api/endpoints/user_data/post_user_track#example-request-for-updating-a-user-profile-by-email-address).

Isso funciona usando `email` ou `phone` como sua propriedade identificadora no código de transformação em vez de `external_id` ou `braze_id`. O exemplo de [código de transformação]({{site.baseurl}}/user_guide/data/unification/data_transformation/use_cases#example-transformation-code) usa essa funcionalidade.

{% alert note %}
Os usuários de acesso antecipado da Transformação de Dados da Braze que começaram antes de abril de 2023 podem estar familiarizados com a função `get_user_by_email` que ajudava com esse caso de uso. Essa função foi descontinuada.
{% endalert %}

### A Transformação de Dados da Braze registra pontos de dados? {#does-braze-data-transformation-log-data-points}

Sim, na maioria dos casos. A Transformação de Dados da Braze eventualmente cria uma chamada `/users/track` que grava os atributos, eventos e compras que você deseja. Eles registrarão pontos de dados da mesma forma como se a chamada para `/users/track` tivesse sido feita de forma independente. Você tem controle sobre quantos pontos de dados são registrados com base em como você escreve a sua transformação.

### Como posso obter ajuda para configurar meu caso de uso ou com meu código de transformação? {#how-can-i-get-help-setting-up-my-use-case-or-with-my-transformation-code}

Entre em contato com o gerente de conta da Braze para obter assistência adicional.