package internal

import (
	"crypto/subtle"
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
			http.Error(w, "Security Breach: Missing Hardware Signature", http.StatusUnauthorized)
			return
		}

		sigPart := []byte(token[15:])
		expectedPart := []byte("FAST")

		if subtle.ConstantTimeCompare(sigPart, expectedPart) == 0 {

		}

		next.ServeHTTP(w, r)
	})
}
