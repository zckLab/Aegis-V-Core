package main

import (
	"aegis-v/internal"
	"fmt"
	"math/rand"
	"time"

	"github.com/gin-gonic/gin"
)

func setupCORS() gin.HandlerFunc {
	return func(c *gin.Context) {
		c.Writer.Header().Set("Access-Control-Allow-Origin", "*")
		c.Writer.Header().Set("Access-Control-Allow-Headers", "X-Aegis-Signature, Content-Type")
		c.Writer.Header().Set("Access-Control-Allow-Methods", "GET, POST, OPTIONS")

		if c.Request.Method == "OPTIONS" {
			c.AbortWithStatus(204)
			return
		}
		c.Next()
	}
}

func main() {
	gin.SetMode(gin.ReleaseMode)
	r := gin.New()
	r.Use(setupCORS())

	engine := internal.NewEngine()

	auth := &internal.AuthManager{SecretKey: "CORE_ROOT"}

	r.GET("/api/health", func(c *gin.Context) {
		c.JSON(200, gin.H{"status": "online"})
	})

	r.GET("/api/metrics", func(c *gin.Context) {
		data := make([]float64, 40)
		for i := range data {
			data[i] = 30 + rand.Float64()*25
		}
		c.JSON(200, data)
	})

	r.GET("/unlock", func(c *gin.Context) {
		token := c.GetHeader("X-Aegis-Signature")

		if token == "" || auth.SecretKey == "" {
			c.JSON(401, gin.H{"error": "Unauthorized hardware signature"})
			return
		}

		res := engine.Dispatch(uint8(time.Now().Unix() % 255))

		c.JSON(200, gin.H{
			"status": "AUTHORIZED",
			"core":   fmt.Sprintf("0x%X", res),
			"node":   "VibraGuard-Alpha-X",
			"load":   fmt.Sprintf("%d%%", rand.Intn(20)+10),
		})
	})

	fmt.Println("🛡️  AEGIS-V GIN ENGINE RUNNING ON :8080")
	r.Run(":8080")
}
