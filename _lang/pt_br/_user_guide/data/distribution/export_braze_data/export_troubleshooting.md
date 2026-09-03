---
nav_title: Solução de problemas
article_title: Solução de problemas de exportação
page_order: 6
page_type: reference
description: "Diagnostique falhas de exportação CSV e API usando um índice de sintomas, um caminho de investigação padrão e orientações de erros específicos por armazenamento."
---

# Solução de problemas de exportação {#export-troubleshooting}

> Use esta página para diagnosticar problemas de exportação CSV e API no dashboard e nas APIs de exportação. Para fluxos de trabalho e limites de exportação, consulte [Exportar dados de segmento para CSV]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv) e [APIs de exportação]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_apis).

## Comece aqui: identifique seu sintoma {#start-here-match-your-symptom}

Encontre o comportamento que você está observando na tabela e acesse a seção correspondente para verificações direcionadas.

| Sintoma | Acessar |
| --- | --- |
| O link de download do CSV retorna `AccessDenied`, `ExpiredToken` ou "file doesn't exist" | [Exportação padrão: erros de CSV](#defaultexport_csv-exports) ou [Armazenamento em nuvem: erros de CSV](#csv-exports-1) |
| A URL de download da exportação via API retorna `403 Forbidden` | [Não consigo baixar um ZIP de segmento exportado](#cant-download-an-exported-segment-zip-from-a-braze-url) |
| A exportação de segmento falha ou diz que o segmento é muito grande | [Segmento muito grande](#segment-is-too-large-or-export-fails-when-my-segment-looks-under-500000-users) |
| Nenhum e-mail de exportação de segmento recebido | [Sem e-mail de exportação de segmento](#not-receiving-segment-export-emails) |
| A contagem de linhas do CSV não corresponde à análise de dados da Campaign | [Divergência na análise de dados de Campaign e Canvas](#number-of-users-in-csv-export-doesnt-match-messages-sent-or-unique-recipients) |
| Colunas esperadas ausentes no arquivo de exportação | [Colunas ausentes](#expected-columns-are-missing-from-a-segment-export-file) |
| A exportação para armazenamento em nuvem mostra `AccessDenied` ou `ExpiredToken` | [Armazenamento em nuvem conectado: erros de API](#common-errors-1) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Sintoma de exportação" }

## Caminho de investigação padrão {#standard-investigation-path}

Use este fluxo de trabalho para cada incidente de exportação. Comece pela etapa 1.

1. Confirme se você está exportando para o bucket S3 padrão da Braze ou para um parceiro de armazenamento em nuvem conectado. A expiração do link e o comportamento de nova tentativa diferem entre os dois.
2. Para exportações CSV do dashboard, confirme que você está logado na Braze ao abrir o link de download. Links do bucket padrão exigem uma sessão ativa no dashboard.
3. Verifique há quanto tempo a exportação foi concluída. Links de download enviados por e-mail do dashboard expiram após quatro horas, independentemente de você usar o bucket padrão da Braze ou um parceiro de armazenamento conectado. Quando um parceiro de armazenamento está conectado, a Braze também entrega uma cópia no seu bucket; essa cópia segue suas políticas de retenção e pode permanecer disponível após o link do e-mail expirar.
4. Para exportações grandes de segmentos, confirme que o público está abaixo do limite de 500.000 usuários para exportação CSV do dashboard. As estimativas do criador de segmentos podem diferir da avaliação do pipeline de exportação.
5. Para exportações via API, aguarde o processamento terminar antes de fazer o download. Use `callback_endpoint` no [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) ou faça polling com backoff exponencial em vez de solicitar a URL imediatamente.
6. Se você ainda estiver bloqueado, entre em contato com o [suporte da Braze]({{site.baseurl}}/braze_support) informando o tipo de exportação (CSV ou API), o ID do segmento ou da Campaign, o timestamp (com fuso horário) e a mensagem de erro exata.

## Destinos de armazenamento {#cloud-storage-connected}

Use as guias para selecionar se você está exportando para o bucket S3 padrão da Braze ou para um parceiro de armazenamento em nuvem. Para orientações sobre armazenamento em nuvem, abra a guia **Armazenamento em nuvem conectado** e revise as seções de CSV e API.

{% sdktabs %}
{% sdktab Default export %}

Quando você não tem um parceiro de armazenamento marcado como seu destino de exportação padrão, a Braze usa seu próprio bucket Amazon S3 para armazenar seus arquivos de exportação. Os arquivos nessa configuração são temporários e expiram após quatro horas.

### Exportações CSV {#csv-exports}

Sintoma: um e-mail de exportação CSV do dashboard chega, mas o link de download falha, ou a exportação nunca é concluída.


Quando você exporta um CSV do dashboard, a Braze envia um link de download por e-mail para o usuário logado. Esse link aponta para um arquivo ZIP hospedado no bucket S3 da Braze. Dentro do ZIP estão vários arquivos menores que juntos compõem sua exportação.

Você deve estar logado no dashboard da Braze para usar o link, e o arquivo fica disponível por apenas quatro horas. Depois disso, o link não funciona mais e os dados são excluídos. Se você encontrar falhas repetidas com exportações muito grandes (mais de 500.000 usuários), a exportação pode falhar. Nesse caso, tente dividir sua exportação em grupos ou campos menores, ou considere configurar um parceiro de armazenamento.

#### Erros comuns {#common-errors}

- Se você vir um erro `AccessDenied`, o arquivo pode já ter expirado ou você pode ter tentado abri-lo antes de estar pronto. Relatórios maiores demoram mais para serem gerados, então aguarde alguns minutos e tente novamente.
- Um erro `ExpiredToken` significa que o período de quatro horas passou. Reexecute a exportação para gerar um novo link.
- A mensagem `Looks like the file doesn't exist anymore` geralmente aparece quando o e-mail é enviado, mas o arquivo ainda não terminou de ser enviado para o S3. Aguardar alguns minutos geralmente resolve o problema.
- Apóstrofos adicionados no início de certos campos (como `-`, `=`, `+` ou `@`) são esperados. Por exemplo, `-1943` se torna `'-1943` no CSV. A Braze faz isso para evitar que programas de planilhas interpretem os dados incorretamente. Isso não se aplica a exportações JSON, como as retornadas pelo [endpoint `/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment).

### Exportações de API {#api-exports}

Sintoma: uma chamada à API de exportação é bem-sucedida, mas a URL de download falha ou retorna dados vazios.


Quando você exporta através das APIs de exportação sem armazenamento em nuvem, a Braze grava os arquivos no seu bucket S3. Você não receberá um e-mail — em vez disso, a resposta da API inclui uma URL de download temporária. A exportação vem como um ZIP contendo vários arquivos JSON, cada um com um usuário por linha.

Assim como as exportações CSV, os links da API expiram após quatro horas. Se você abrir o link cedo demais, pode ver erros porque o arquivo ainda não está pronto. Você pode fornecer um `callback_endpoint` na sua solicitação se quiser que a Braze notifique você quando o arquivo estiver disponível.

Exportações grandes de API também podem atingir o tempo limite. Se isso acontecer, tente fazer solicitações menores ou conecte um parceiro de armazenamento para lidar com o volume.

#### Erros comuns

- `AccessDenied` ou `ExpiredToken` geralmente significam que o link expirou ou ainda não estava pronto. Execute a exportação novamente ou espere um pouco mais.

{% endsdktab %}

{% sdktab Cloud storage connected %}

Quando você conecta um parceiro de armazenamento (como Amazon S3, Google Cloud Storage ou Azure Blob) e o marca como seu destino de exportação padrão na página **Parceiros de Tecnologia** no dashboard, a Braze grava suas exportações diretamente no seu bucket. Essa configuração é geralmente mais confiável para exportações maiores.

### Exportações CSV {#csv-exports-1}

Sintoma: o link de CSV enviado por e-mail falha, mas os arquivos aparecem (ou não aparecem) no seu bucket conectado.


Com exportações CSV, a Braze envia um link de download por e-mail. Esse link expira após um curto período (geralmente cerca de quatro horas). Quando você tem um parceiro de armazenamento conectado e marcado como seu destino de exportação padrão, a Braze também entrega uma cópia da exportação no seu bucket conectado. Essa cópia reside na sua própria infraestrutura, onde a expiração e a retenção seguem suas políticas de armazenamento.

No armazenamento em nuvem, as exportações CSV são agrupadas em um arquivo ZIP. Dentro do ZIP estão vários arquivos CSV menores. Exportações grandes são frequentemente divididas em partes (por exemplo, cerca de 5.000 usuários cada), e o tamanho das partes pode variar. Arquivos menores não indicam dados ausentes. Se o link enviado por e-mail falhar, mas a cópia no seu armazenamento for bem-sucedida, você sempre pode recuperar seus dados diretamente do seu bucket.

#### Erros comuns

- `AccessDenied` significa que a Braze não conseguiu gravar no seu bucket. Verifique se suas credenciais e permissões ainda são válidas.
- `ExpiredToken` aparece se a Braze perdeu o acesso ao seu bucket. Atualize suas credenciais no dashboard da Braze.
- Se alguns arquivos parecerem menores do que o esperado, isso é um comportamento normal. O processo de exportação divide intencionalmente os arquivos para garantir estabilidade.
- Apóstrofos adicionados no início de certos campos (como `-`, `=`, `+` ou `@`) são esperados. Por exemplo, `-1943` se torna `'-1943` no CSV. A Braze faz isso para evitar que programas de planilhas interpretem os dados incorretamente. Isso não se aplica a exportações JSON, como as retornadas pelo [endpoint `/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment).

### Exportações de API

Sintoma: as exportações via API não aparecem no seu bucket ou os arquivos estão incompletos.


Quando você exporta dados através das APIs com um parceiro de armazenamento conectado, os arquivos de exportação são gravados no seu bucket. Nenhum e-mail é enviado. Os objetos subjacentes ficam no seu armazenamento e seguem suas configurações de retenção, mesmo que as URLs de download retornadas pela Braze possam ainda ter limite de tempo.

Os arquivos geralmente aparecem no seu bucket conforme a exportação é executada, então você não precisa esperar o trabalho inteiro terminar para acessar resultados parciais. A Braze faz upload de cada lote concluído de forma incremental, em vez de reter tudo até o final. Exportações grandes são divididas em vários arquivos compactados (ZIP ou GZIP), cada um contendo objetos JSON, um por linha. Isso torna esse método mais confiável para exportações pesadas.

#### Erros comuns {#common-errors-1}

- `AccessDenied` acontece quando a Braze não consegue gravar no seu bucket ou os objetos foram excluídos posteriormente. Verifique as permissões e confirme que nada externo está excluindo arquivos.
- `ExpiredToken` significa que as credenciais de acesso da Braze ao seu bucket estão desatualizadas. Atualize-as no dashboard.
- Se arquivos estiverem ausentes ou menores do que o esperado, primeiro confirme que nada fora da Braze está excluindo objetos. Tamanhos de arquivo menores em si são esperados.

{% endsdktab %}
{% endsdktabs %}

## Análise de dados de Campaign e Canvas {#campaign-and-canvas-analytics}

### O número de usuários na exportação CSV não corresponde a *Messages Sent* ou *Unique Recipients* {#number-of-users-in-csv-export-doesnt-match-messages-sent-or-unique-recipients}

Sintoma: a exportação CSV de uma Campaign mostra uma contagem de usuários diferente de *Messages Sent* ou *Unique Recipients* na página de análise de dados.


A exportação CSV de uma Campaign pode mostrar um número diferente de usuários em relação a *Messages Sent* e *Unique Recipients* pelos seguintes motivos:

#### A reelegibilidade está ativada {#re-eligibility-is-turned-on}

Se os usuários podem (ou puderam em algum momento) receber a Campaign mais de uma vez, os números de análise de dados da Campaign e o número de linhas na exportação de dados de usuários não coincidem. *Messages Sent* conta cada envio, inclusive quando o mesmo usuário recebe a mensagem mais de uma vez. O download de **Exportar dados de usuários em CSV** lista usuários únicos — uma linha por perfil que recebeu a Campaign — e não uma linha por envio. Por exemplo, se *Messages Sent* é 12 e o CSV tem 10 linhas, esses 12 envios foram para 10 usuários distintos (alguns usuários receberam a Campaign mais de uma vez).

#### Usuários foram excluídos ou mesclados desde o envio da Campaign ou do Canvas {#users-were-deleted-or-merged-since-the-campaign-or-canvas-sent}

A exportação CSV fornece um snapshot dos usuários existentes que receberam uma determinada Campaign ou Canvas. Como os usuários podem ser excluídos ou mesclados, a contagem da exportação CSV pode ser menor do que a contagem de destinatários únicos. Por exemplo, se 1.000 usuários recebem uma Campaign, a Campaign mostra 1.000 destinatários únicos, e a exportação CSV no mesmo dia também mostra 1.000 usuários. Se um mês depois 50 desses 1.000 usuários forem excluídos, a exportação CSV conterá 950 usuários, enquanto a contagem incrementada de destinatários únicos ainda será 1.000.

## E-mails de exportação de segmentos do dashboard {#dashboard-segment-export-emails}

### Segmento muito grande ou a exportação falha quando meu segmento parece ter menos de 500.000 usuários {#segment-is-too-large-or-export-fails-when-my-segment-looks-under-500000-users}

Sintoma: a exportação de segmento do dashboard falha ou mostra um erro de tamanho, mesmo que a estimativa do segmento pareça aceitável.


O **tamanho do segmento no dashboard é uma estimativa**. A exportação CSV usa essa estimativa para aplicar o [limite de exportação de 500.000 usuários]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv#segment-csv-export-details); o pipeline de exportação também pode avaliar o tamanho de forma diferente da interface do criador de segmentos. Se as exportações falharem para um segmento próximo desse limite, use [números de bucket aleatórios]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers) ou divida o público em segmentos menores, ou use o [endpoint `/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) conforme descrito em [Exportando segmentos grandes]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv#exporting-large-segments).

### Por que não estou recebendo e-mails de exportação de segmentos? {#not-receiving-segment-export-emails}

Sintoma: uma exportação CSV de segmento foi disparada, mas nenhum e-mail chegou.


Primeiro, verifique sua pasta de SPAM em busca de um e-mail de `no-reply@alerts.braze.com`. Se o e-mail estiver lá, adicione esse endereço à sua lista de remetentes confiáveis para que futuras mensagens de exportação não sejam filtradas.

Se o e-mail não estiver na sua pasta de SPAM, verifique se outra pessoa da sua equipe consegue receber a exportação. Se ninguém conseguir, considere o tamanho da sua exportação. O tempo de entrega varia conforme o tamanho da exportação, mas se o e-mail não chegar após uma hora, entre em contato com o [suporte da Braze]({{site.baseurl}}/braze_support).

## Downloads da API de exportação de segmentos {#segment-export-api-downloads}

### Não consigo baixar um ZIP de segmento exportado a partir de uma URL da Braze {#cant-download-an-exported-segment-zip-from-a-braze-url}

Sintoma: um erro `403 Forbidden` ao fazer download a partir da URL de resposta do `/users/export/segment`.


Se você receber um erro `403 Forbidden` ao usar o [endpoint `/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment), o arquivo pode ainda não estar pronto. Exportações grandes podem demorar para serem processadas. Aguarde até uma hora antes de tentar baixar novamente.

Se você usa um script automatizado para recuperar o arquivo, também pode receber um erro `403 Forbidden` ao solicitar a URL cedo demais. Se você exporta dados de segmentos regularmente, considere conectar sua própria integração de bucket S3 e encaminhar os arquivos para seu próprio pipeline de extração, transformação e carregamento (ETL).

As exportações levam tempo para serem concluídas, então o acesso imediato a partir de um script frequentemente falha. Você pode:

- Consultar a URL de download com backoff exponencial, ou
- Usar o [parâmetro `callback_endpoint`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment#request-parameters) e apontá-lo para um serviço que execute seu script quando a exportação estiver pronta.

## Campos da API de exportação de segmentos e usuários {#segment-and-user-export-api-fields}

### Colunas esperadas estão ausentes em um arquivo de exportação de segmento {#expected-columns-are-missing-from-a-segment-export-file}

Sintoma: uma exportação via API ou dashboard está sem campos que você esperava.


A opção **Exportar dados de usuários em CSV** do dashboard para um segmento usa um conjunto fixo de colunas (consulte [Exportar dados de segmento para CSV]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv#data-included-in-export)). Ela não inclui uma coluna ou parâmetro `fields_to_export`.

Para exportações de segmentos via API, você deve passar `fields_to_export` no corpo da solicitação. Alguns campos puxam dados relacionados automaticamente — por exemplo, solicitar `canvases_received` também requer dados de resumo de jornada no perfil do usuário. Consulte a referência do [endpoint `/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) para nomes de campos válidos e requisitos.

Se colunas estiverem ausentes em um ZIP de exportação via API, confirme que o array `fields_to_export` na sua solicitação inclui todos os campos necessários e que seu espaço de trabalho possui as permissões de exportação exigidas.

## Quando entrar em contato com o suporte {#when-to-contact-support}

Entre em contato com o [suporte da Braze]({{site.baseurl}}/braze_support) se você concluiu o [caminho de investigação padrão](#standard-investigation-path) e ainda precisa de ajuda. Inclua o tipo de exportação, o ID do segmento ou da Campaign, o timestamp (com fuso horário) e a mensagem de erro exata ou o código de status HTTP.