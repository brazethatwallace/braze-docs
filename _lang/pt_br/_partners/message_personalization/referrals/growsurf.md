---
date_published: "2026-09-08"
nav_title: GrowSurf
article_title: GrowSurf
description: "Este artigo de referência descreve a parceria entre a Braze e a GrowSurf, uma plataforma de programas de indicação e afiliados que sincroniza dados de participantes com a Braze para segmentação e personalização com Liquid."
alias: /partners/growsurf/
page_type: partner
search_tag: Partner
---

# GrowSurf

> A [GrowSurf](https://www.growsurf.com/) envia dados de participantes de programas de indicação e de afiliados para os perfis de usuário da Braze. A integração adiciona links de indicação, detalhes de participantes, contagens de indicações, contagens de convites, contagens de impressões e progresso de marcos como atributos personalizados que você pode usar para segmentação na Braze e personalização com Liquid.

_Essa integração é mantida pela GrowSurf._

## Sobre a integração {#about-the-integration}

A GrowSurf é um software de programas de indicação e afiliados. A integração unidirecional mantém os dados de indicação dos participantes da GrowSurf disponíveis na Braze para que você possa segmentar participantes, personalizar mensagens com links de indicação e progresso, e enviar comunicações oportunas do programa a partir da Braze.

## Casos de uso {#use-cases}

- Adicionar o link de indicação de cada participante às mensagens da Braze.
- Criar segmentos com base no status de indicação, contagens de indicações e progresso de marcos.
- Personalizar Campaigns e Canvas com atributos de participantes e indicadores.

## Pré-requisitos {#prerequisites}

Antes de começar, você precisa do seguinte:

| Pré-requisito | Descrição |
| --- | --- |
| Uma conta GrowSurf | Um plano pago da GrowSurf é necessário para essa integração. |
| Uma chave da API REST da Braze | Uma chave da API REST da Braze com permissões de `users.track`. Crie essa chave no dashboard da Braze em **Configurações** > **APIs e Identificadores** > **Chaves de API**. Para saber mais, consulte [Criando chaves da API REST]({{site.baseurl}}/api/basics#creating-rest-api-keys). |
| Um endpoint REST da Braze | A URL do seu endpoint REST da Braze (por exemplo, `https://rest.iad-01.braze.com`). Para saber mais, consulte [Endpoints da REST API]({{site.baseurl}}/api/basics#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

Siga estas etapas para conectar um programa da GrowSurf à Braze. Para instruções detalhadas, consulte a [documentação de integração da GrowSurf com a Braze](https://docs.growsurf.com/integrations/braze).

### Etapa 1: Criar uma chave da API REST da Braze {#step-1-create-a-braze-rest-api-key}

1. Na Braze, acesse **Configurações** > **APIs e Identificadores** > **Chaves de API**.
2. Crie uma chave da API REST com permissões de `users.track`.
3. Copie a chave de API e anote o endpoint REST do mesmo espaço de trabalho da Braze.

### Etapa 2: Conectar a Braze na GrowSurf {#step-2-connect-braze-in-growsurf}

1. Na GrowSurf, acesse **Program Editor** > **4. Options** > **Integrations** > **Braze**.
2. Selecione o endpoint REST da Braze correspondente.
3. Insira a chave da API REST e selecione **Submit**.

### Etapa 3: Verificar a primeira sincronização de participante {#step-3-verify-the-first-participant-sync}

1. Adicione ou atualize um participante de teste na GrowSurf.
2. Na Braze, acesse **Público** > **Pesquisa de Usuário** e pesquise por e-mail para abrir o perfil de usuário correspondente.
3. Confirme que os atributos personalizados `grsf_` aparecem no perfil.

## Atributos da GrowSurf na Braze {#growsurf-attributes-in-braze}

A GrowSurf disponibiliza 15 atributos de indicação na Braze. A primeira sincronização envia o conjunto completo. Depois disso, a GrowSurf envia atualizações quando os dados do participante mudam. Se um valor for removido na GrowSurf, o atributo correspondente na Braze também será limpo. Os valores de contagem são enviados como números.

### Atributos de string {#string-attributes}

| Atributo personalizado | Descrição |
| --- | --- |
| `grsf_share_url` | A URL de compartilhamento de indicação do participante. |
| `grsf_participant_id` | O ID do participante na GrowSurf. |
| `grsf_referral_status` | O status de indicação do participante. |
| `grsf_participant_first_name` | O nome do participante. |
| `grsf_participant_last_name` | O sobrenome do participante. |
| `grsf_referrer_first_name` | O nome do indicador. |
| `grsf_referrer_last_name` | O sobrenome do indicador. |
| `grsf_referrer_email` | O endereço de e-mail do indicador. |
| `grsf_next_milestone` | O próximo marco que o participante está buscando alcançar. |
| `grsf_next_monthly_milestone` | O próximo marco mensal que o participante está buscando alcançar. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Atributos de string" }

### Atributos numéricos {#number-attributes}

| Atributo personalizado | Descrição |
| --- | --- |
| `grsf_total_referral_count` | A contagem total de indicações do participante. |
| `grsf_monthly_referral_count` | A contagem de indicações do participante no mês atual. |
| `grsf_prev_monthly_referral_count` | A contagem de indicações do participante no mês anterior. |
| `grsf_total_invite_count` | A contagem total de convites do participante. |
| `grsf_total_impression_count` | A contagem total de impressões do link de indicação do participante. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Atributos numéricos" }

## Usar a GrowSurf com a Braze {#use-growsurf-with-braze}

Use os atributos de indicação da GrowSurf para segmentação na Braze e personalização com Liquid. A GrowSurf atualiza esses atributos quando um participante é adicionado ou quando seus dados de indicação mudam. Você também pode sincronizar participantes que já estavam no seu programa.

### Etapa 1: Criar segmentos {#step-1-build-segments}

1. Na Braze, crie um segmento com os atributos personalizados `grsf_` relevantes.
2. Segmente ou exclua participantes por status de indicação, contagens de indicações ou progresso de marcos.

### Etapa 2: Personalizar mensagens {#step-2-personalize-messages}

1. Adicione o atributo personalizado `grsf_share_url` a uma mensagem da Braze com Liquid: {% raw %}`{{custom_attribute.${grsf_share_url}}}`{% endraw %}.

{: start="2"}
2. Use outros atributos `grsf_` para personalizar o status de indicação, contagens e progresso de marcos.

## Considerações {#considerations}

- A GrowSurf envia apenas atributos personalizados. Ela não envia eventos personalizados, compras ou alterações de inscrição.
- A GrowSurf identifica perfis da Braze pelo e-mail do participante. Se não existir um perfil correspondente, a Braze cria um perfil somente com e-mail.
- Se o mesmo e-mail pertencer a participantes em mais de um programa GrowSurf conectado, os dados do programa sincronizado mais recentemente aparecerão nesse perfil da Braze.
- Conecte a Braze antes de importar participantes. Para sincronizar participantes existentes, use a opção de sincronização de participantes existentes da GrowSurf.

## Solução de problemas {#troubleshooting}

- Confirme que a chave da API REST da Braze tem permissões de `users.track` e que o endpoint REST selecionado pertence ao mesmo espaço de trabalho da Braze.
- Se um participante não sincronizar, verifique se ele possui um endereço de e-mail válido.
- Verifique os registros de atividade do participante na GrowSurf para conferir o resultado da sincronização.
- A GrowSurf tenta novamente automaticamente em caso de erros temporários da Braze. Se a GrowSurf não conseguir confirmar uma atualização, ela envia todos os atributos de indicação na próxima vez que esse perfil da Braze for sincronizado. Se a chave de API ou o endpoint REST for inválido, corrija as configurações e reconecte a integração.

Para mais detalhes sobre solução de problemas, consulte a [documentação de integração da GrowSurf com a Braze](https://docs.growsurf.com/integrations/braze#troubleshooting).