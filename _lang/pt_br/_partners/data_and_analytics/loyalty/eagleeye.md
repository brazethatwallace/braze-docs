---
nav_title: Eagle Eye
article_title: Eagle Eye
description: Saiba como integrar a Eagle Eye com a Braze.
alias: /partners/eagle_eye/
page_type: partner
search_tag: Partner
---

# Eagle Eye

> A [Eagle Eye](https://eagleeye.com/) é uma empresa líder em SaaS e tecnologia de IA que permite que marcas de varejo, viagens e hospitalidade conquistem a fidelidade de seus clientes finais, potencializando suas atividades de marketing ao consumidor em tempo real, omnicanal e personalizado, em escala.

_Essa integração é mantida pela Eagle Eye._

## Visão geral {#overview}

O Eagle Eye Connect é uma integração bidirecional entre a Braze e o AIR que permite que as marcas ativem dados de fidelidade e promocionais diretamente na Braze. Os clientes podem emitir recompensas no AIR para os consumidores que entram em um público no AIR. Isso permite que os profissionais de marketing personalizem o engajamento dos clientes usando dados em tempo real, como saldos de pontos, promoções e atividades de recompensas.

## Casos de uso {#use-cases}

- Dispare Campaigns na Braze com base em eventos de fidelidade, como limites de pontos ou recompensas obtidas.
- Enriqueça os perfis de usuários da Braze com dados de fidelidade em tempo real para possibilitar um direcionamento mais personalizado.
- Rastreie e gere relatórios sobre a eficácia de Campaigns vinculadas a resgates de recompensas.
- Emita recompensas no AIR quando os usuários entrarem em Campaigns na Braze.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
|--------------------------|-------------|
| Conta Eagle Eye AIR | Você precisa de uma conta ativa do Eagle Eye AIR para aproveitar essa parceria. Para começar, entre em contato com a equipe de Parcerias da Eagle Eye em [partnerships@eagleeye.com](mailto:partnerships@eagleeye.com). |
| Chave da API REST da Braze | Uma chave da API REST da Braze com permissões `users.track`. <br><br>Isso pode ser criado no dashboard da Braze em **Configurações > Chaves de API**. |
| Endpoint REST da Braze | [Sua URL de endpoint REST]({{site.baseurl}}/api/basics/#endpoints). Seu endpoint depende da URL da Braze para sua instância. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Saída vs. entrada {#outbound-vs-inbound}

As tabelas a seguir descrevem os dois tipos de integrações suportadas entre a Braze e o Eagle Eye AIR. O Eagle Eye Connect é o middleware que possibilita a troca de dados entre o AIR e os sistemas de parceiros, como a Braze. Para saber mais, consulte a [documentação da Eagle Eye sobre a Braze](https://developer.eagleeye.com/docs/braze).

{% tabs local %}
{% tab outbound %}
<table aria-label="Saída vs. entrada">
  <caption>Saída vs. entrada</caption>
  <thead>
    <tr>
      <th>Direção</th>
      <th>Iniciado por</th>
      <th>Fluxo de dados</th>
      <th>Finalidade</th>
      <th>Exemplo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Eagle Eye → Braze</td>
      <td>Eagle Eye</td>
      <td>Para a API da Braze</td>
      <td>
        Envie dados de fidelidade para os perfis de usuários da Braze como atributos personalizados por meio de eventos personalizados. Na Braze, os dados ingeridos podem ser usados para:
        <ul>
          <li>segmentar usuários, disparar Campaigns</li>
          <li>personalizar mensagens</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>Envio de pontos de fidelidade ou status de nível para a Braze (<code>ee_loyalty.points.current</code>, <code>ee_loyalty.tier.tierId</code>)</li>
          <li>Atualização do perfil de um usuário quando ele recebe ou resgata um cupom.</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Saída vs. entrada" }
{% endtab %}

{% tab inbound %}
<table aria-label="Saída vs. entrada">
  <caption>Saída vs. entrada</caption>
  <thead>
    <tr>
      <th>Direção</th>
      <th>Iniciado por</th>
      <th>Fluxo de dados</th>
      <th>Finalidade</th>
      <th>Exemplo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Braze → Eagle Eye</td>
      <td>Braze</td>
      <td>Para a API da Eagle Eye via webhook</td>
      <td>
        Quando um consumidor entra em um público na Braze a partir de qualquer fonte, a Braze pode disparar um webhook para o EE Connect, permitindo que a EE emita uma recompensa (cupom ou pontos).<br><br>
        Após a conclusão da ação no AIR, a Braze receberia um evento de saída do AIR.
      </td>
      <td>
        <ul>
          <li>Recompensas (cupom ou pontos) são emitidas a um consumidor por sua adesão ao programa de fidelidade</li>
          <li>Recompensas são emitidas para um consumidor que teve uma entrega atrasada</li>
          <li>Recompensas de aniversário</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Saída vs. entrada" }
{% endtab %}
{% endtabs %}

{% alert tip %}
Para saber mais sobre os dados personalizados que você pode enviar para a Braze como atributos ou eventos personalizados, consulte a [documentação da Eagle Eye sobre a Braze](https://developer.eagleeye.com/docs/braze#data-model).
{% endalert %}

## Visão geral da integração {#integration-overview}

Atualmente, os conectores de entrada e saída só podem ser configurados via API com suporte direto da equipe da Eagle Eye — no entanto, uma opção de autoatendimento dentro do dashboard do AIR está a caminho!

Ao trabalhar com a sua equipe Eagle Eye, você concluirá o seguinte:

### Etapa 1: Fornecer detalhes de configuração {#step-1-provide-configuration-details}

Primeiro, você fornecerá os seguintes detalhes à sua equipe Eagle Eye:

| Você fornece | Descrição |
|------------------------|-------------|
| Credenciais da API da Braze | Compartilhe seu endpoint REST da Braze, identificador de app e chave de API com segurança com seu contato na Eagle Eye. |
| Correspondência de identificadores | Determine e compartilhe o identificador de usuário principal para atualizações de perfil que é comum no AIR e na Braze, como ID externo ou e-mail. |
| Chave de autenticação | Determine e compartilhe uma chave de autenticação secreta para cada conector de entrada e saída. |
| Código da moeda | Compartilhe o código de moeda de 3 dígitos para exibir valores monetários de compra (por exemplo, USD). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 1: Fornecer detalhes de configuração" }

### Etapa 2: Configurar o Eagle Eye Connect {#step-2-configure-eagle-eye-connect}

Sua equipe Eagle Eye configurará o Eagle Eye Connect usando os detalhes fornecidos, juntamente com as credenciais exclusivas da API do AIR e os eventos de saída para os conectores.

### Etapa 3: Configurar ações de comportamento social no AIR {#step-3-configure-social-behavioral-actions-in-air}

Em seguida, você configurará uma ou mais ações de comportamento social no AIR com referências de ação exclusivas para emitir pontos ou cupons.

### Etapa 4: Configurar a Braze {#step-4-configure-braze}

Na Braze, você concluirá o seguinte:

- Configure Campaigns na Braze para emitir recompensas no AIR
- Configure quaisquer comunicações para os consumidores quando os eventos do AIR forem recebidos

### Etapa 5: Testar sua integração {#step-5-test-your-integration}

Faça chamadas de API no AIR e observe o fluxo de dados de eventos no seu espaço de trabalho da Braze. Valide os dados recebidos do AIR e confirme se os atributos estão sendo atualizados conforme o esperado.

Além disso, adicione usuários aos públicos e confirme se as recompensas são emitidas no AIR.

### Etapa 6: Lançar em produção {#step-6-launch-to-production}

Depois que o teste for bem-sucedido, a integração poderá entrar em operação para enviar dados continuamente para a Braze. As mesmas etapas de configuração são necessárias para ambientes de produção no AIR e na Braze.

Entre em contato com o seu gerente de sucesso do cliente da Eagle Eye para que um recurso seja atribuído a você para configurar o EE Connect.

## Suporte {#support}

Para obter suporte de integração ou solução de problemas, entre em contato com a equipe de suporte da Eagle Eye em [support@eagleeye.com](mailto:support@eagleeye.com).