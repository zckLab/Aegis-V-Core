package internal

import (
	"net/http"
	"strings"
)

type AuthManager struct {
	SecretKey string
}

func (a *AuthManager) ValidateHardwareToken(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		token := r.Header.Get("X-Aegis-Signature")
		if !strings.HasPrefix(token, "AEGIS_SEC_INIT_") {
			http.Error(w, "unauthorized", http.StatusUnauthorized)
			return
		}
		next.ServeHTTP(w, r)
	})
}
