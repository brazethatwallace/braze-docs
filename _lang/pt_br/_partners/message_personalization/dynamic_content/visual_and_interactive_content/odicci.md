---
nav_title: Odicci
article_title: Odicci
description: "Guia passo a passo para integrar a Odicci ao Braze para campanhas de marketing personalizadas"
alias: /partners/odicci/
page_type: partner
search_tag: Partner
---

# Integrar a Odicci ao Braze {#integrate-odicci-with-braze}

> Saiba como integrar a Braze com a [Odicci](https://www.odicci.com/), uma plataforma que capacita as empresas a adquirir, engajar e reter clientes por meio de experiências omnicanal orientadas pela fidelidade.

{% alert tip %}
Consulte a [Central de Ajuda da Odicci](https://help.odicci.com) para obter recursos adicionais e perguntas frequentes.
{% endalert %}

## Casos de uso {#use-cases}

Você pode conectar a plataforma Odicci com a Braze para um compartilhamento de dados e gerenciamento de campanhas integrados, o que inclui:

- Envio automático dos dados de público coletados nas experiências da Odicci para a Braze.
- Disparo de campanhas de marketing personalizadas com base nas interações do usuário.
- Mapeamento de campos entre a Odicci e a Braze para garantir a sincronização precisa dos dados.

## Exemplo {#example}

Um varejista usa as experiências gamificadas da Odicci para coletar endereços de e-mail para uma campanha de marketing.

1. Um cliente conclui um jogo na Odicci, fornecendo seu endereço de e-mail.
2. A Odicci sincroniza automaticamente esses dados com a Braze.
3. A Braze dispara um e-mail personalizado de agradecimento e inclui um código de desconto.

## Pré-requisitos {#prerequisites}

Antes de começar, você precisará do seguinte:

| Pré-requisito | Descrição |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Uma conta na Odicci | É necessário ter uma conta na Odicci com acesso à seção **Integrações** para aproveitar essa parceria. |
| Chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze | Uma chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze com as permissões `users.track` e `campaigns.list`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração da Odicci {#integrating-odicci}

### Etapa 1: Ativar a integração na Odicci {#step-1-enable-the-integration-in-odicci}

1. Faça login na sua conta Odicci.
2. Navegue até a seção **Settings > Integrations**.
3. Encontre a integração **Braze** e clique em **Connect**.

   ![Conectar a integração com a Braze]({% image_buster /assets/img/odicci/braze_connect.png %})

4. Insira sua chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze no campo fornecido.
5. Salve as configurações para ativar a integração no nível da conta.

### Etapa 2: Obter sua chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze {#step-2-obtain-your-braze-rest-api-key}

1. Faça login na sua conta Braze.
2. Acesse **Console de desenvolvedor > REST or transferir estado representacional API or interface de programação do aplicativo (API) Keys**.
3. Crie uma nova chave de API or interface de programação do aplicativo (API) ou copie uma existente com a permissão `users.track`.

### Etapa 3: Ativar a integração no nível da experiência {#step-3-activate-the-integration-at-the-experience-level}

1. Crie ou abra uma **Experience** no Odicci Studio.
2. Navegue até **Studio > Settings > Integrations**.
3. Localize a caixa de seleção **Braze** e marque-a para ativar a integração para a experiência.
4. Salve suas alterações.

### Etapa 4: Mapear campos {#step-4-map-fields}

1. Depois de ativar a integração, permaneça na seção **Studio > Settings > Integrations**.
2. Mapeie os campos da sua experiência na Odicci (por exemplo, `Email`, `Name`) para os campos correspondentes na Braze.
3. Salve sua configuração.

   ![Configuração de mapeamento de campos]({% image_buster /assets/img/odicci/braze_field_mapping.png %})

### Etapa 5: Testar a integração {#step-5-test-the-integration}

1. Execute a experiência na Odicci para coletar dados de teste.
2. Verifique se os dados estão sincronizados corretamente com a Braze, conferindo o dashboard da Braze ou os registros de dados.
3. Certifique-se de que os campos mapeados estejam preenchidos corretamente na Braze.

## Solução de problemas {#troubleshooting}

Se você tiver problemas com a integração, considere as seguintes soluções. Para obter mais assistência, entre em contato com o [Suporte da Odicci](https://help.odicci.com).

### Chave de API or interface de programação do aplicativo (API) inválida {#api-key-not-valid}

Verifique novamente sua chave de API or interface de programação do aplicativo (API) da Braze e certifique-se de que ela tenha as permissões necessárias. Em seguida, insira novamente a chave de API or interface de programação do aplicativo (API) nas configurações de integração da Odicci.

### Os dados não estão sendo sincronizados {#data-not-syncing}

Verifique se os campos na seção **Field Mapping** estão configurados corretamente. Em seguida, certifique-se de que a chave de API or interface de programação do aplicativo (API) tenha permissões para importações de dados de usuários.

### A Campaign não está sendo disparada {#campaign-not-triggering}

Verifique as configurações da Campaign na Braze para garantir que o público ou as condições de disparo corretos estejam definidos.