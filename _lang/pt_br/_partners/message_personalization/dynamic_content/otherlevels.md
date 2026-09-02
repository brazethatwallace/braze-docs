---
nav_title: OtherLevels
article_title: OtherLevels
alias: /partners/otherlevels/
description: "Este artigo aborda a integração entre a OtherLevels Experience Platform e a Braze."
page_type: partner
search_tag: OtherLevels

---

# OtherLevels

> A [OtherLevels](https://www.otherlevels.com/) Experience Platform usa GenAI para transformar a maneira como marcas esportivas, editores e operadores se conectam com seus clientes, transformando conteúdo tradicional em experiências de mídia avançada e vídeo personalizado de acordo com a marca em escala.

*Essa integração é mantida pela OtherLevels.*

## Visão geral {#overview}

A integração entre a Braze e a OtherLevels permite criar vídeos GenAI personalizados por meio de chamadas de API para a OtherLevels Experience Platform e, em seguida, enviar esses vídeos aos seus usuários como vídeos push para iOS por meio do [Conteúdo conectado da Braze]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call).

Ofereça aos seus usuários uma experiência melhor com as experiências baseadas em IA da OtherLevels. Transforme conteúdo existente e de terceiros em vídeo altamente escalável e mídia avançada para públicos que já consomem conteúdo de forma diferente e respondem fortemente a experiências contextualmente personalizadas.

## Pré-requisitos {#prerequisites}

Antes de começar, você precisará do seguinte:

| Pré-requisito          | Descrição                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Uma conta OtherLevels   | É necessário ter uma conta OtherLevels para aproveitar essa parceria.                                                                     |
| Uma chave da API REST da Braze  | Uma chave da API REST da Braze com permissões de `users.track`. <br><br> Ela pode ser criada no dashboard da Braze em **Configurações** > **Chaves de API**. |
| Um endpoint REST da Braze | [Seu URL de endpoint REST]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints). Seu endpoint dependerá do URL da Braze para sua instância.                                                 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

Essa integração requer a chamada da API da OtherLevels Experience Platform como parte do processo de geração de vídeo antes que as mensagens possam ser enviadas aos seus usuários pela Braze. Exemplos de cURL são fornecidos como parte desta documentação, mas recomendamos o uso de clientes de API como o Postman para automatizar as chamadas de API.

## Casos de uso {#use-cases}

Use os vídeos GenAI criados com a OtherLevels Experience Platform para:
- Criar melhores experiências para proprietários e ligas esportivas, engajamento de fãs, apostas esportivas, iGaming e loterias.
- Ampliar seu marketing de clientes transformando conteúdo baseado em texto em mídia avançada e vídeo, criando experiências humanas e envolventes.
- Aumentar os resultados, da aquisição à retenção, ampliando — e não reequipando — sua integração existente com a Braze.

## Integração da OtherLevels Experience Platform {#integrating-the-otherlevels-experience-platform}

### Etapa 1: Chame a API da OtherLevels Experience Platform para gerar um vídeo {#step-1}

A primeira etapa da integração envolve chamar a API da OtherLevels Experience Platform para gerar um novo vídeo. Note que a geração de vídeo não é instantânea. Dependendo da duração e da complexidade do vídeo, o conteúdo pode levar até meia hora para ser gerado. Planeje suas programações de envio de mensagens e chamadas de API adequadamente para que as chamadas de API para gerar vídeos sejam feitas com antecedência suficiente em relação ao horário programado de envio das mensagens da Braze.

{% alert important %}
A solicitação a seguir usa cURL. Para um gerenciamento mais eficiente das solicitações de API, recomendamos o uso de um cliente de API como o Postman.
{% endalert %}

Consulte o exemplo a seguir para saber como estruturar sua chamada de API. Para saber mais sobre como personalizar os detalhes do vídeo e estruturar sua chamada de API, consulte [Personalização do vídeo GenAI](#customizing-the-genai-video).

{% raw %}
```bash
curl --request POST \
  --url 'https://exp-platform-api.prod.awsotherlevels.com/v1/app/OTHERLEVELS_PROJECT_KEY/media?=' \
  --header 'Content-Type: application/json' \
  --header 'User-Agent: insomnia/10.3.0' \
  --data '{
    "task": {
        "type": "tasks",
        "tasks": {
            "image_video_overlay": {
                "width": "= .orientation == '\''portrait'\'' ? '\''1080'\'' : .orientation == '\''landscape'\'' ? '\''1920'\''",
                "height": "= .orientation == '\''portrait'\'' ? '\''1920'\'' : .orientation == '\''landscape'\'' ? '\''1080'\''",
                "color": "255,255,255,0",
                "y_pos": "0",
                "x_pos": "0",
                "image_input": "= tasks.resize_image.jpg ?? tasks.resize_image.png",
                "video_input": "= tasks.talking_talent_replace_bg.mp4",
                "type": "compose.ImageVideoOverlay"
            },
            "resize_image": {
                "media_input": "= tasks.bg_image.jpg ?? tasks.bg_image.png",
                "type": "compose.MediaResize",
                "width": "= .orientation == '\''portrait'\'' ? '\''1080'\'' : .orientation == '\''landscape'\'' ? '\''1920'\''",
                "height": "= .orientation == '\''portrait'\'' ? '\''1920'\'' : .orientation == '\''landscape'\'' ? '\''1080'\''"
            },
            "bg_image": {
                "type": "load",
                "url": "BACKGROUND_IMAGE_URL",
                "refresh_interval": "12h"
            },
            "talking_head": {
                "test": false,
                "title": "INSERT_TITLE",
                "caption": false,
                "templateId": "TALENT_TEMPLATE",
                "type": "TALENT_MODEL",
                "variables": {
                    "script": {
                        "name": "script",
                        "properties": {
                            "content": "= tasks.translate_text.text"
                        },
                        "type": "text"
                    }
                }
            },
            "translate_text": {
                "type": "translate_text",
                "source": "en",
                "target": "en",
                "text": "INSERT_SCRIPT"
            },
            "talking_talent_speed": {
                "type": "compose.VideoSetSpeed",
                "speed": "1.0",
                "video_input": "= tasks.talking_head.mp4"
            },
            "talking_talent_replace_bg": {
                "type": "compose.VideoReplaceBg",
                "video_background": "= tasks.resize_image.jpg ?? tasks.resize_image.png",
                "video_input": "= tasks.talking_talent_speed.mp4"
            }
        },
        "output": "image_video_overlay"
    }
}'
```
{% endraw %}

Substitua o seguinte:

| Espaço reservado          | Descrição                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| `OTHERLEVELS_PROJECT_KEY`   | Uma chave de projeto OtherLevels será fornecida quando você for provisionado com uma conta OtherLevels.                                                                     |
| `BACKGROUND_IMAGE_URL`  | Um URL HTTPS para o plano de fundo do vídeo. |
| `INSERT_TITLE` | O título do vídeo. Trata-se de uma referência interna e não será exibido no vídeo.                                                 |
| `TALENT_TEMPLATE` | Um ID de modelo de talento. A OtherLevels trabalhará com você durante o provisionamento da conta para criar um talento (avatar). Você receberá um ou vários IDs de talento que podem ser usados.                                                 |
| `TALENT_MODEL` | Um ID de modelo de talento. A OtherLevels trabalhará com você durante o provisionamento da conta para criar um talento (avatar). Você receberá um ou vários modelos de talento que podem ser usados.                                                 |
| `INSERT_SCRIPT` | O roteiro exato que você gostaria que o talento dissesse durante o vídeo.                                                 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 1: Chame a API da OtherLevels Experience Platform para gerar um vídeo" }

Como parte da resposta da API, a OtherLevels retornará uma carga útil JSON indicando uma chamada de API bem-sucedida. O JSON conterá um `recipe_id` exclusivo para identificar o vídeo gerado. O `recipe_id` será necessário na próxima etapa.

Aqui está um exemplo de resposta da API:

{% raw %}
```bash
{"$schema":"https://exp-platform-api.prod.awsotherlevels.com/schemas/GenerateMediaResBody.json","message":"success","recipe_id":"LMINHWXV2BBD6JGV5VF3ZNZV7BDDRR7FH5FJH6MMX4BVLTPRKTWQ","media_short_id":"LMINHWX","status":"triggered"}
```
{% endraw %}

### Etapa 2: Definir o `recipe_id` como um atributo personalizado {#step-2-setting-the-recipe_id-as-a-custom-attribute}

O `recipe_id` recebido na [Etapa 1](#step-1) agora é definido como um atributo personalizado da Braze para o(s) usuário(s) para o(s) qual(is) você deseja enviar os vídeos.

Dependendo do seu caso de uso, você pode ter gerado um único vídeo destinado a um grande público e, nesse caso, o mesmo `recipe_id` pode ser definido para vários usuários. Como alternativa, você pode ter gerado vários vídeos exclusivos, cada um direcionado a um usuário diferente; nesse caso, cada usuário deve ter seu `recipe_id` personalizado definido como atributos personalizados da Braze.

{% alert important %}
A solicitação a seguir usa cURL. Para um gerenciamento mais eficiente das solicitações de API, recomendamos o uso de um cliente de API como o Postman.
{% endalert %}

{% raw %}
```bash
curl --location --request POST 'BRAZE_API_ENDPOINT/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer BRAZE_API_KEY' \
--data-raw '{
  "attributes": [
    {
      "external_id": "USER_ID",
      "olxpmedia": "RECIPE_ID"
    }
  ]
}'
```
{% endraw %}

Substitua o seguinte:

| Espaço reservado             | Descrição                                                                                                                                                                                     |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `BRAZE_API_ENDPOINT`    | O URL do endpoint REST da Braze da sua instância atual. Para saber mais, consulte [Chaves da API REST]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab#rest-api-keys). |
| `BRAZE_API_KEY`         | Sua chave da API REST da Braze com a permissão `users.track`.                                                                                                                                      |
| `USER_ID`              | O ID do usuário que receberá esse vídeo específico. Para mais exemplos dos identificadores que podem ser usados, consulte [/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track).                                                                                                                                                  |
| `RECIPE_ID`       | O `recipe_id` recebido da resposta da API da OtherLevels na [Etapa 1](#step-1).                                                                                                                                                                            |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 2: Definir o recipe_id como um atributo personalizado" }

### Etapa 3: Envio por meio do Conteúdo conectado da Braze {#step-3-sending-through-braze-connected-content}

Para enviar os vídeos GenAI como mensagens push para iOS aos seus usuários, siga estas etapas:

1. Crie uma Campaign de notificação por push para iOS na Braze.
2. Enquanto estiver criando sua Campaign, acesse a seção **Assets** e cole a seguinte sintaxe de Conteúdo conectado no campo **Add from URL**.

{% raw %}
```
{% connected_content https://exp-platform-api-external.prod.awsotherlevels.com/v1/app/OTHERLEVELS_PROJECT_KEY/media/{{custom_attribute.${olxpmedia}}} %}
```
{% endraw %}

Em seguida, substitua `OTHERLEVELS_PROJECT_KEY` pela chave do projeto fornecida pela OtherLevels.

{: start="3"}
3. No menu suspenso de **URL file format**, selecione **MP4**.
4. Configure o restante da Campaign (como conteúdo da mensagem, cronograma de envio e público-alvo) com base nas suas preferências.

![Exemplo de campos de ativos para Conteúdo conectado.]({% image_buster /assets/img/otherlevels/1.png %})

## Personalização do vídeo GenAI {#customizing-the-genai-video}

### Tamanho e atributos do vídeo {#video-size-and-attributes}

O plano de fundo do vídeo pode ser especificado na chave `bg_image`.

| Parâmetro             | Descrição                  |
|-------------------------|----------------------------|
| `url`    | URL HTTPS para a imagem de fundo. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tamanho e atributos do vídeo" }

O tamanho do plano de fundo do vídeo pode ser especificado na chave `resize_image`. Recomendamos que a imagem de fundo tenha o mesmo tamanho configurado aqui.

| Parâmetro             | Descrição                  |
|-------------------------|----------------------------|
| `width`    | Largura da imagem de fundo, com opções para os modos retrato e paisagem. |
| `height`     | Altura da imagem de fundo, com opções para os modos retrato e paisagem.                              |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tamanho e atributos do vídeo" }

As opções de sobreposição de vídeo podem ser especificadas na chave `image_video_overlay`.

| Parâmetro             | Descrição                  |
|-------------------------|----------------------------|
| `width`    | Largura da sobreposição, com opções para os modos retrato e paisagem. |
| `height`         | Altura da sobreposição, com opções para os modos retrato e paisagem.                                              |
| `color`              | Cor da sobreposição especificada em RGB junto com a transparência do vídeo.                                                                   |
| `y_pos`       | Deslocamento do eixo Y em relação ao centro.                                                              |
| `x_pos`    | Deslocamento do eixo X em relação ao centro. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tamanho e atributos do vídeo" }

### Talento e roteiro {#talent-and-script}

Como parte do provisionamento, a OtherLevels trabalhará com você para gerar um ou vários talentos (às vezes chamados de avatares) para uso em seus vídeos. Dependendo do seu caso de uso e da sua marca, isso pode ser feito na forma de um dos embaixadores existentes da sua marca ou de uma criação exclusiva.

Depois que forem criados, você receberá IDs `TALENT_TEMPLATE` e `TALENT_MODEL` utilizáveis para usar com nossa API.

O modelo de voz usado para processar scripts de entrada funciona melhor quando você fornece um roteiro natural que um ser humano leria. Na maioria dos casos, você não precisa de pontuação extra para orientar manualmente o roteiro. No entanto, recomendamos testar todos os seus roteiros antes de enviá-los a um público real. A velocidade com que o talento lê o roteiro pode ser especificada na chave `talking_talent_speed`.

| Parâmetro             | Descrição                  |
|-------------------------|----------------------------|
| `speed`    | Especifique a velocidade na qual o talento lerá o roteiro. Por exemplo, `1.5`.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Talento e roteiro" }

## Considerações adicionais {#additional-considerations}

- Somente a plataforma de notificações por push do iOS suporta nativamente mídia de vídeo. As notificações por push do Android não oferecem suporte nativo a vídeos, portanto essa integração só pode ser usada com seu público do iOS.
- Ao receber notificações por push de vídeo em dispositivos iOS, os usuários precisam pressionar e segurar a notificação por push para que o vídeo seja carregado e reproduzido. Esse é o comportamento padrão na plataforma iOS e não pode ser personalizado.