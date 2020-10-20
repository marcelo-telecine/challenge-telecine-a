## Desafio Telecine
* Consuma informações de filme de uma API Externa (Título, Descrição, Gênero, etc) - FEITO!
* Enriqueça os dados com os dados da mídia, presentes em um banco interno - FEITO!
* Para consumir tanto a API externa quanto a interna é necessário autenticação - FEITO!
* Liste estas informações em múltiplas plataformas (TV, Mobile Apps, Web Browser) - NÃO ENTENDIDO!
* Possua funcionalidade de busca destes filmes integrada a um front end - NÃO DEU TEMPO!
* A arquitetura deve permitir a coleta de informações em tempo real e alimentar um data-lake - NÃO DEU TEMPO!
* Os dados coletados devem ser visualizados pelo time de negócio para saber quais os filmes mais buscados de forma simples, através de uma interface - NÃO DEU TEMPO!
__________________________________________
* Propor um fluxo de trabalho no repositório de código: 
    * FLUXO DEFINIDO NO BLOCO ABAIXO.
* Propor um fluxo de deploy para as diferentes aplicações e diferentes ambientes:
    * MINHA PROPOSTA É A DE IMPLEMENTAÇÃO DE UM CI PARA DEPLOY AUTOMÁTICO CONFOME GITFLOW
        * 1 - UM MERGE NO BRANCH "DEPLOYMENT" A PARTIR DE UM BRANCH DE NOME FEATURE/* DISPARA UM DEPLOY AUTOMATIZADO NO AMBIENTE DE STAGING
        * 2 - UM MERGE NO BRANCH "MASTER" A PARTIR DE UM BRANCH DE NOME RELEASE/* DISPARA UM DEPLOY AUTOMATIZADO NO AMBIENTE DE STAGING
* Descrever testes necessários para cada camada, citando o custo benefício de cada
    * 1 - TESTES UNITARIOS IMPLEMENTADOS
    * 2 - TESTES DE INTEGRAÇÃO IMPLEMENTADOS
    * 3 - TESTES DE CARGA IMPLEMENTADOS
* Descrever o stack de tecnologia proposto
    * 1 - DOCKER
    * 2 - PYTHON
    * 3 - MONGO

__________________________________________

First run:
```
make build
```
Other executions:
```
make run
```
Stopping the application:
```
make stop
```
Running unit tests:    
```
make unittest
```
Running stress test:    
```
make stresstest-build
make stresstest-run
(with the server running)
```
Search:
```
curl --request GET \
  --url 'http://localhost/api/v1/search?query=Marvel' \
  --header 'authorization: Bearer 6bbde6df-a90a-4369-7018-8c3376dc23ff' \
  --header 'cache-control: no-cache' 
```