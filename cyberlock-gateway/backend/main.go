package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"time"
)

type Status struct {
	HardwareFound bool   `json:"hardware_found"`
	AuthStatus    string `json:"auth_status"`
	AccessGranted bool   `json:"access_granted"`
	LastChallenge string `json:"last_challenge"`
}

func getStatus(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Access-Control-Allow-Origin", "*")
	// Simulação da lógica que estaria no Assembly
	challenge := fmt.Sprintf("0x%X", time.Now().Unix())

	data := Status{
		HardwareFound: false, // Emula que o hardware está em modo Virtual
		AuthStatus:    "Encrypted via Virtual Assembly Core",
		AccessGranted: true,
		LastChallenge: challenge,
	}
	json.NewEncoder(w).Encode(data)
}

func main() {
	http.HandleFunc("/api/status", getStatus)
	fmt.Println("🚀 Backend Go rodando em http://localhost:8080")
	http.ListenAndServe(":8080", nil)
}
