---
nav_title: VWO
article_title: Integre o VWO com a Braze
description: "Aprenda como integrar o VWO com a Braze."
alias: /partners/vwo/
page_type: partner
search_tag: Partner
---

# VWO

> [VWO](https://vwo.com/) é uma poderosa plataforma de experimentação que ajuda as marcas a melhorar métricas de negócios importantes, permitindo que as equipes executem programas de otimização de conversão apoiados por dados de comportamento do cliente. Com o VWO, você pode unificar dados de clientes, obter insights comportamentais, construir hipóteses, realizar testes A/B em várias plataformas (servidor, web e mobile), lançar recursos, personalizar experiências e otimizar toda a jornada do cliente.

Ao integrar o VWO com a Braze, você pode aproveitar os dados de experimentos do VWO para criar segmentos direcionados e entregar campanhas personalizadas.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
|-----------------|-------------|
| Conta do VWO | Uma conta do VWO com acesso a dados de experimentação. |
| Conta da Braze | Uma conta ativa da Braze com o [Braze Web SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web) integrado em sua página da web. Você também precisará da segmentação de propriedades de eventos ativada. Para solicitá-la, veja [Considerações](#request-event-property-segmentation). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Integrando o VWO com a Braze {#integrating-vwo-with-braze}

### Etapa 1: Ative a integração da Braze no VWO {#step-1-enable-the-braze-integration-in-vwo}

1. Faça login na sua conta do VWO.
2. No dashboard do VWO, acesse **Configurations > Integrations**. Aqui, você pode ativar integrações no nível do espaço de trabalho, o que aplica a integração a todas as futuras campanhas de teste por padrão.

   ![Configuração de integração do VWO]({% image_buster /assets/img/vwo/vwo1_settings.png %})

4. Selecione a integração da Braze para ativá-la.
5. Opcionalmente, você pode ativar a integração da Braze para quaisquer campanhas existentes. Para fazer isso, selecione uma campanha, depois acesse **Configuration > Integrations** e ative a Braze.

   ![Ativar integração da Braze]({% image_buster /assets/img/vwo/vwo2_enable_braze.png %})

6. Depois de ativar a integração, o VWO começará a enviar dados de experimentos para a Braze no nível da campanha.

### Etapa 2: Crie um segmento na Braze com propriedades de evento do VWO {#step-2-create-a-segment-in-braze-with-vwo-event-properties}

1. No dashboard da Braze, selecione **Segments** > **+ Create Segment**.
3. Na janela **Create Segment**, insira um nome para o segmento e depois selecione **Create Segment**.
4. No seu segmento recém-criado, selecione **Filters** > **Add Filter** e escolha **Custom Event** como o tipo de filtro.
6. No dropdown de filtro, procure por **VWO**.
7. Selecione a propriedade relevante do VWO e especifique o valor necessário.
8. Se necessário, configure o número de visitas e o período de tempo. Quando terminar, selecione **Save**.

   ![Criação de segmento na Braze]({% image_buster /assets/img/vwo/vwo3_braze_segment.png %})

9. Para ver o número de usuários que correspondem aos critérios do seu segmento, selecione **Calculate Exact Statistics**.

   ![Estatísticas de segmento na Braze]({% image_buster /assets/img/vwo/vwo4_braze_segment_calculate_size.png %})

## Fluxo de dados {#data-flow}

O VWO envia os dados do experimento da campanha para a Braze como um evento personalizado usando o seguinte formato:

- **Nome do evento:** VWO
- **Propriedades do evento:** `vwo_campaign_name`, `vwo_variation_name`

{% alert tip %}
Essas propriedades de evento personalizado também podem ser usadas para segmentação e direcionamento.
{% endalert %}

## Considerações {#considerations}

### Solicitar segmentação de propriedades de evento {#request-event-property-segmentation}

Antes de usar a segmentação de propriedades de evento, você precisará ativá-la na Braze. Use o seguinte modelo para entrar em contato com seu gerente de sucesso do cliente da Braze ou a equipe de suporte para obter acesso.

   <table aria-label="Request event property segmentation">
     <caption>Solicitar segmentação de propriedades de evento</caption>
   <thead>
      <tr>
         <th>Campo</th>
         <th>Informações</th>
      </tr>
   </thead>
   <tbody>
      <tr>
         <td><strong>Assunto</strong></td>
         <td>Solicitação para ativar a segmentação de propriedades de evento para integração VWO</td>
      </tr>
      <tr>
         <td><strong>Corpo</strong></td>
         <td>
         Olá, equipe Braze,<br><br>
         Gostaríamos de ativar a segmentação de propriedades de evento para eventos enviados da nossa integração VWO&lt;&gt;Braze. Aqui estão os detalhes:<br><br>
         - <strong>Nome do evento:</strong> VWO<br>
         - <strong>Propriedades do evento:</strong> <code>vwo_campaign_name</code>, <code>vwo_variation_name</code><br><br>
         Por favor, confirme assim que as propriedades forem ativadas em nossa conta.<br><br>
         Obrigado.
         </td>
      </tr>
   </tbody>
   </table>
   {: .reset-td-br-1 .reset-td-br-2 aria-label="Request event property segmentation" }

### Pontos de dados da Braze {#braze-data-points}

O evento personalizado enviado do VWO para a Braze&#8212;incluindo quaisquer propriedades de evento ativadas para segmentação&#8212;registrará pontos de dados na sua instância da Braze.

### Considerações

Atualmente, essa integração não suporta a sincronização em tempo real de dados de teste. Pode haver um atraso de até 15 minutos para que os dados de teste apareçam na Braze.

## Solução de problemas {#troubleshooting}

Se você não estiver vendo dados do VWO na Braze:

1. Clique com o botão direito na página onde sua campanha de teste está rodando e selecione **Inspect Element**.
2. Na guia **Network**, procure por **Braze** para filtrar as chamadas de rede para a Braze.
3. As chamadas de rede são preenchidas à medida que a página carrega. Você pode recarregar a página para visualizar as chamadas de rede.
4. Selecione uma chamada de rede para ver mais detalhes.
5. Acesse a seção **Request Payload** na guia **Payload**, onde você pode encontrar events: que tem name: **ce**, indicando evento personalizado.
6. Expanda 0: e data: para ver n: "VWO" (nome do evento personalizado) e p: {vwo_campaign_name: "<your vwo campaign name>", vwo_variation_name: "<variation name>"}. Isso indica que os valores estão sendo enviados pelo VWO para a Braze.

 ![Solução de problemas da Braze]({% image_buster /assets/img/vwo/vwo5_troubleshooting.png %})

Para suporte adicional, entre em contato com seu gerente de sucesso do cliente do VWO.