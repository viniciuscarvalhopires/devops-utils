## vinicpires/get-namespaces:v3

A imagem *vinicpires/get-namespaces:fastapi* utiliza scripts em python para a automação da coleta de namespaces e não possui arquivo de configuração de cluster inserido, portanto, ao aplicar os manifestos da pasta **manifestos**, certifique-se de que a ClusterRole, ClusterRoleBinding e ServiceAccount foram criadas corretamente.

| :warning: O endpoint **/delete** recebe uma requisição POST através do form html.
|-----------------------------------------|

## Documentação da API

#### Home

```http
  GET /
```

#### Lista todos os namespaces

```http
  GET /namespaces
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `string` | **Obrigatório**. O ID do item que você quer |

#### Deletar namespace

```http
  POST /delete
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `namespace`      | `string` | **Obrigatório**. Namespace a ser deletado |

#### Deletar namespace

```http
  POST /create
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `namespace`      | `string` | **Obrigatório**. Namespace a ser criado |