# Definição do comando base do Docker Compose (mude para 'docker compose' se usar a versão V2 do Docker)
COMPOSE = docker compose
# O .PHONY garante que o Make não confunda o nome dos comandos com arquivos locais
.PHONY: help build up down restart logs ps shell shell-django migrate makemigrations collectstatic createsuperuser test clean

help: ## Mostra este menu de ajuda com as descrições
	@awk 'BEGIN {FS = ":.*##"; printf "\nUso:\n  make \033[36m<comando>\033[0m\n\nComandos disponíveis:\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-18s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)

build: ## Constrói ou reconstrói as imagens dos containers
	$(COMPOSE) build

up: ## Inicializa os containers em segundo plano (Detached)
	$(COMPOSE) up -d

up-log: ## Inicializa os containers exibindo os logs diretamente no terminal
	$(COMPOSE) up

down: ## Para e remove os containers, redes e volumes anônimos
	$(COMPOSE) down

down-v: ## Para e remove tudo, INCLUINDO os volumes persistentes (reseta o banco de dados)
	$(COMPOSE) down -v

restart: ## Reinicia os containers da aplicação
	$(COMPOSE) restart

logs: ## Exibe e acompanha os logs em tempo real de todos os containers
	$(COMPOSE) logs -f

ps: ## Lista os containers ativos do projeto e suas portas
	$(COMPOSE) ps

shell: ## Abre o terminal Bash dentro do container da aplicação Python (serviço 'web')
	$(COMPOSE) exec web bash

shell-django: ## Abre o shell interativo do Django para testar consultas e códigos Python
	$(COMPOSE) exec web python manage.py shell

makemigrations: ## Verifica alterações nos models e gera os arquivos de migração
	$(COMPOSE) exec web python manage.py makemigrations

migrate: ## Aplica as migrações pendentes no banco de dados
	$(COMPOSE) exec web python manage.py migrate

collectstatic: ## Coleta todos os arquivos estáticos (CSS, JS) para o STATIC_ROOT
	$(COMPOSE) exec web python manage.py collectstatic --noinput

createsuperuser: ## Cria um usuário administrador para acessar o painel /admin do Django
	$(COMPOSE) exec web python manage.py createsuperuser

test: ## Executa a suíte de testes automatizados do Django
	$(COMPOSE) exec web python manage.py test

clean: ## Limpa o cache do sistema e remove containers/imagens órfãs do Docker
	docker system prune -f
	docker volume prune -f