---
nav_title: Solução de problemas
article_title: Solução de problemas de exportação
page_order: 6
page_type: reference
description: "Este artigo de referência cobre cenários comuns de solução de problemas para exportações em fluxos de trabalho CSV e API."
---

# Solução de problemas de exportação

> Esta página cobre cenários comuns de solução de problemas para exportações em fluxos de trabalho CSV e API.

Use as guias para selecionar se você está exportando para o **bucket S3 padrão da Braze** ou para um **parceiro de armazenamento em nuvem**.

{% sdktabs %}
{% sdktab Default export %}

Quando você não tem um parceiro de armazenamento marcado como seu destino de exportação padrão, a Braze usa seu próprio bucket Amazon S3 para armazenar seus arquivos de exportação. Os arquivos nessa configuração são temporários e expiram após quatro horas.

## Exportações CSV
Quando você exporta um CSV do dashboard, a Braze envia um link de download por e-mail para o usuário logado. Esse link aponta para um arquivo ZIP hospedado no bucket S3 da Braze. Dentro do ZIP estão vários arquivos menores que juntos compõem sua exportação.

Você deve estar logado no dashboard da Braze para usar o link, e o arquivo fica disponível por apenas quatro horas. Depois disso, o link não funciona mais e os dados são excluídos. Se você encontrar falhas repetidas com exportações muito grandes (mais de 500.000 usuários), a exportação pode falhar. Nesse caso, tente dividir sua exportação em grupos ou campos menores, ou considere configurar um parceiro de armazenamento.

### Erros comuns

- Se você vir um erro `AccessDenied`, o arquivo pode já ter expirado ou você pode ter tentado abri-lo antes de estar pronto. Relatórios maiores demoram mais para serem gerados, então aguarde alguns minutos e tente novamente.
- Um erro `ExpiredToken` significa que o período de quatro horas passou. Reexecute a exportação para gerar um novo link.
- A mensagem `Looks like the file doesn't exist anymore` geralmente aparece quando o e-mail é enviado, mas o arquivo ainda não terminou de ser enviado para o S3. Aguardar alguns minutos geralmente resolve o problema.
- Apóstrofos adicionados no início de certos campos (como `-`, `=`, `+` ou `@`) são esperados. Por exemplo, `-1943` se torna `'-1943` no CSV. A Braze faz isso para evitar que programas de planilhas interpretem os dados incorretamente. Isso não se aplica a exportações JSON, como as retornadas pelo [endpoint `/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/).

## Exportações de API
Quando você exporta através das APIs de exportação sem armazenamento em nuvem, a Braze grava os arquivos no seu bucket S3. Você não receberá um e-mail — em vez disso, a resposta da API inclui uma URL de download temporária. A exportação vem como um ZIP contendo vários arquivos JSON, cada um com um usuário por linha.

Assim como as exportações CSV, os links da API expiram após quatro horas. Se você clicar no link cedo demais, pode ver erros porque o arquivo ainda não está pronto. Você pode fornecer um `callback_endpoint` na sua solicitação se quiser que a Braze notifique você quando o arquivo estiver disponível.

Exportações grandes de API também podem atingir o tempo limite. Se isso acontecer, tente fazer solicitações menores ou conecte um parceiro de armazenamento para lidar com o volume.

### Erros comuns
- `AccessDenied` ou `ExpiredToken` geralmente significam que o link expirou ou ainda não estava pronto. Execute a exportação novamente ou espere um pouco mais.

{% endsdktab %}

{% sdktab Cloud storage connected %}

Quando você conecta um parceiro de armazenamento (como Amazon S3, Google Cloud Storage ou Azure Blob) e o marca como seu destino de exportação padrão na página **Parceiros de tecnologia** no dashboard, a Braze grava suas exportações diretamente no seu bucket. Essa configuração é geralmente mais confiável para exportações maiores.

## Exportações CSV
Com exportações CSV, a Braze envia um link de download por e-mail. Esse link expira após um curto período (geralmente cerca de quatro horas). Quando você tem um parceiro de armazenamento conectado e marcado como seu destino de exportação padrão, a Braze também entrega uma cópia da exportação no seu bucket conectado. Essa cópia reside na sua própria infraestrutura, onde a expiração e a retenção seguem suas políticas de armazenamento.

No armazenamento em nuvem, as exportações CSV são agrupadas em um arquivo ZIP. Dentro do ZIP estão vários arquivos CSV menores. Exportações grandes são frequentemente divididas em partes (por exemplo, cerca de 5.000 usuários cada), e o tamanho das partes pode variar. Arquivos menores não indicam dados ausentes. Se o link enviado por e-mail falhar, mas a cópia no seu armazenamento for bem-sucedida, você sempre pode recuperar seus dados diretamente do seu bucket.

### Erros comuns

- `AccessDenied` significa que a Braze não conseguiu gravar no seu bucket. Verifique se suas credenciais e permissões ainda são válidas.
- `ExpiredToken` aparece se a Braze perdeu o acesso ao seu bucket. Atualize suas credenciais no dashboard da Braze.
- Se alguns arquivos parecerem menores do que o esperado, isso é um comportamento normal. O processo de exportação divide intencionalmente os arquivos para garantir estabilidade.
- Apóstrofos adicionados no início de certos campos (como `-`, `=`, `+` ou `@`) são esperados. Por exemplo, `-1943` se torna `'-1943` no CSV. A Braze faz isso para evitar que programas de planilhas interpretem os dados incorretamente. Isso não se aplica a exportações JSON, como as retornadas pelo [endpoint `/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/).

## Exportações de API
Quando você exporta dados através das APIs com um parceiro de armazenamento conectado, os arquivos de exportação são gravados no seu bucket. Nenhum e-mail é enviado. Os objetos subjacentes ficam no seu armazenamento e seguem suas configurações de retenção, mesmo que as URLs de download retornadas pela Braze possam ainda ter limite de tempo. Cada arquivo ZIP contém objetos JSON, um por linha. Exportações grandes podem ser divididas em vários arquivos ZIP em vez de um único ZIP, o que geralmente torna esse método mais confiável para exportações pesadas.

### Erros comuns

- `AccessDenied` acontece quando a Braze não consegue gravar no seu bucket ou os objetos foram excluídos posteriormente. Verifique as permissões e confirme que nada externo está excluindo arquivos.
- `ExpiredToken` significa que as credenciais de acesso da Braze ao seu bucket estão desatualizadas. Atualize-as no dashboard.
- Se arquivos estiverem ausentes ou menores do que o esperado, primeiro confirme que nada fora da Braze está excluindo objetos. Tamanhos de arquivo menores em si são esperados.

{% endsdktab %}
{% endsdktabs %}