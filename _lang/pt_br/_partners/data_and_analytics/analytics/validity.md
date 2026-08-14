---
nav_title: Validity
article_title: Validity
alias: /partners/validity/
description: "Este artigo de referência descreve a parceria entre a Braze e a Validity, uma plataforma de entregabilidade de e-mail que sincroniza listas de seed do Everest com a Braze e automatiza testes de posicionamento na caixa de entrada para Campaigns e Canvas."
page_type: partner
search_tag: Partner
---

# Validity

> O [Validity Everest](https://www.validity.com/everest/) é uma plataforma de entregabilidade de e-mail que ajuda você a medir o posicionamento na caixa de entrada e proteger sua reputação de envio. A integração entre a Braze e a Validity sincroniza sua lista de seed do Everest com a Braze, faz o seeding automático de Campaigns e Canvas qualificados e envia métricas de engajamento de volta ao Validity Inbox para que você possa comparar o posicionamento baseado em seed com o engajamento real dos assinantes.

_Esta integração é mantida pela Validity._

## Sobre a integração {#about-the-integration}

A Validity cria e mantém usuários de lista de seed de e-mail na Braze para que os endereços de seed permaneçam ativos e não suprimidos. Quando uma Campaign ou Canvas está pronta para o seeding, a Validity envia uma cópia para essa lista de seed e exibe métricas de engajamento — entregas, bounces, aberturas, cliques e cancelamentos de inscrição — no Validity Inbox junto com os dados de posicionamento na caixa de entrada.

## Casos de uso {#use-cases}

### Auto-seeding

Com o auto-seeding da Validity, a Validity detecta quando uma Campaign ou Canvas da Braze atinge um volume de envio qualificado e envia uma cópia do conteúdo dessa Campaign para sua lista de seed da Validity. Os envios de seed direcionam usuários em que o atributo personalizado `validity_seed` está definido como `true`.

## Pré-requisitos {#prerequisites}

Antes de começar, você precisa do seguinte:

| Requisito | Descrição |
| ----------- | ----------- |
| Uma conta Validity | Uma conta Validity é necessária para aproveitar esta parceria. |
| Uma chave da API REST da Braze | Uma chave da API REST da Braze com as seguintes permissões: `users.track`, `users.delete`, `email.bounce.remove`, `email.spam.remove`, `campaigns.list`, `campaigns.details`, `campaigns.data_series`, `canvas.list`, `canvas.details`, `canvas.data_series`, `content_blocks.list`, `content_blocks.info` e `messages.send`. <br><br> Crie essa chave no dashboard da Braze em **Configurações** > **APIs e identificadores**. |
| Um endpoint REST da Braze | [A URL do seu endpoint REST]({{site.baseurl}}/api/basics#endpoints). Seu endpoint depende da URL da Braze para sua instância. Por exemplo, `rest.iad-01.braze.com`. |
| Um identificador de app da Braze | O identificador de app da Braze ao qual os envios de seed devem ser atribuídos. Encontre-o em **Configurações** > **APIs e identificadores** > **Identificadores de app**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integrando a Validity {#integrating-validity}

### Etapa 1: Compartilhe as credenciais da Braze com a Validity {#step-1-share-braze-credentials-with-validity}

A Validity precisa de três credenciais de **Configurações** > **APIs e identificadores** no dashboard da Braze:

- Sua chave da API REST (com as permissões listadas em [Pré-requisitos](#prerequisites))
- Seu endpoint REST
- Seu identificador de app

Compartilhe essas credenciais com seu representante da Validity, que concluirá a configuração da integração para você. A Validity valida as credenciais com uma chamada de teste ao vivo para a Braze antes de ativar a integração. Se você não sabe quem é seu contato na Validity, envie um e-mail para [support@validity.com](mailto:support@validity.com).

Após a integração ser ativada, a Validity sincroniza sua lista de seed do Everest com a Braze em um ciclo recorrente (a cada 10 minutos). A Validity cria, atualiza e remove usuários de seed na Braze para mantê-los alinhados com sua lista de seed atual no Everest.

### Etapa 2: Opcionalmente, crie um Segment na Braze para usuários de seed da Validity {#step-2-optionally-create-a-braze-segment-for-validity-seed-users}

Criar um Segment é opcional. O auto-seeding envia e-mails de teste usando um objeto [Connected Audience]({{site.baseurl}}/api/objects_filters/connected_audience) filtrado pelo atributo personalizado `validity_seed` sempre que um envio qualificado é detectado. Você não precisa criar um Segment ou anexá-lo às suas Campaigns.

Se quiser visualizar esse público dentro da Braze para referência, crie um Segment em **Público** > **Segments** com o filtro `validity_seed` igual a `true`.

A Validity cria usuários por meio do endpoint [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) usando o seguinte esquema:

```bash
curl -X POST "https://YOUR_API_ENDPOINT/users/track" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_BRAZE_API_KEY" \
  -d '{
    "attributes": [
      {
        "email": "example1@example.com",
        "validity_seed": true
      },
      {
        "email": "example2@example.com",
        "validity_seed": true
      }
    ],
    "events": [
      {
        "email": "example1@example.com",
        "name": "validity_seed_event",
        "time": "2026-07-02T18:00:00.000Z"
      }
    ]
  }'
```

Esses usuários sempre incluem o atributo personalizado `validity_seed` com o valor booleano `true`. A Validity também envia um evento personalizado `validity_seed_event` para cada usuário de seed para que eles sejam registrados como usuários ativos na sua conta da Braze.

## Considerações {#considerations}

### Como os envios de seed funcionam {#how-seed-sends-work}

A Validity obtém o corpo da Campaign, o assunto e o endereço de remetente por meio dos endpoints de detalhes de Campaign e Canvas, e então entrega uma cópia desse conteúdo para a lista de seed por meio do endpoint [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) da Braze. Seu dashboard da Braze continua exibindo apenas a Campaign original.

### Limite de auto-seeding {#auto-seeding-threshold}

A Validity detecta quando uma Campaign ou Canvas ultrapassa o limite de volume de envio configurado (10.000 envios por padrão) e envia o teste de seed nesse momento. Você não precisa adicionar o público de seed às suas Campaigns ou Canvas.

Um teste de seed envia sua Campaign de e-mail para os endereços da lista de seed, coleta dados de posicionamento e ajuda você a identificar problemas antes ou durante os envios para seu público. As métricas de posicionamento na caixa de entrada mostram se sua Campaign chega à caixa de entrada, à pasta de SPAM ou se é perdida. Use essas métricas para confirmar o posicionamento na caixa de entrada e detectar problemas de entregabilidade.

Os testes de seed também podem ajudar a diagnosticar por que os e-mails caem na pasta de SPAM ou são perdidos. Verificar dados de cabeçalho, autenticação (SPF, DKIM e DMARC), validação de links e renderização de design pode mostrar quais etapas tomar para melhorar sua taxa de posicionamento na caixa de entrada.

### Integridade da lista de seed {#seed-list-health}

A Validity monitora os usuários da lista de seed e pode atualizá-los ou removê-los se começarem a perder eficácia — por exemplo, se provedores de serviços de e-mail (ESPs) começarem a sinalizar membros do público da lista de seed como SPAM. Essas permissões permitem que a Validity monitore a integridade da lista de seed e atualize a lista conforme necessário.

### Como o conteúdo dinâmico é tratado {#how-dynamic-content-is-handled}

Os e-mails da Braze frequentemente usam personalização Liquid vinculada ao perfil de um destinatário real. Como os endereços de seed não possuem esses dados de perfil, a Validity executa cada e-mail por meio de um sanitizador antes do seeding. O sanitizador resolve Content Blocks, avalia a lógica básica de Liquid e substitui tudo o que não consegue resolver (como um nome) por um placeholder visível `[REDACTED]`. Seções construídas inteiramente a partir de APIs de Connected Content em tempo real são renderizadas em branco no seed.

Você pode ativar ou desativar o sanitizador. Quando ele está desativado, a Braze resolve a personalização Liquid para envios de seed da mesma forma que faria para um destinatário real.

### Inbox Aggregate

Ativar o auto-seeding também ativa o Inbox Aggregate. Esse recurso obtém métricas de engajamento — enviados, entregues, bounces, aberturas, cliques e cancelamentos de inscrição — dos seus envios reais da Braze (separadamente dos envios de seed) e as exibe no Validity Inbox junto com seus dados de posicionamento na caixa de entrada. Os dois recursos operam em cronogramas independentes e não precisam ser gerenciados separadamente.