setup:
	@echo "🛠️ Instaling Dependencies..."
	cd gateway-proxy && go mod tidy
	pip install -r soc-dashboard/requirements.txt
	@echo "✅ Setup Complete."

run-backend:
	@echo "🛡️ Starting Go Gin Engine..."
	cd gateway-proxy && go run main.go

run-frontend:
	@echo "🚀 Starting Streamlit Dashboard..."
	streamlit run soc-dashboard/app.py

run:
	@echo "🔥 Starting Full Aegis-V System..."
	(cd gateway-proxy && go run main.go) & streamlit run soc-dashboard/app.py