setup:
	@echo "Instalando dependências..."
	pip install streamlit pandas requests
	cd backend && go mod init cyberlock || true
	@echo "Tudo pronto. Use 'make run' para iniciar."

run:
	@echo "Iniciando Sistema Híbrido..."

	go run backend/main.go & streamlit run dashboard/app.py