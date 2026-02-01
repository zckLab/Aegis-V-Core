package internal

import (
	"time"
)

type HardwareEngine struct {
	TaskQueue chan byte
	Results   chan byte
}

func NewEngine() *HardwareEngine {
	e := &HardwareEngine{
		TaskQueue: make(chan byte, 10),
		Results:   make(chan byte, 10),
	}
	go e.worker()
	return e
}

func (e *HardwareEngine) worker() {
	for challenge := range e.TaskQueue {
		time.Sleep(30 * time.Millisecond)
		response := challenge ^ 0x7A
		e.Results <- response
	}
}

func (e *HardwareEngine) Dispatch(b byte) byte {
	e.TaskQueue <- b
	return <-e.Results
}
