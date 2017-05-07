package main

import (
	"fmt"
	"sync"
)

type Site struct {
	hosts []string
	lock  *sync.RWMutex
}

func main() {

	list := make(map[string]Site, 10)
	queue := make(chan Site, 3)

	list["legacy"] = Site{hosts: []string{"shinken"}}
	list["webpod1-cph3"] = Site{hosts: []string{"monitor1", "monitor2"}}
	list["webpod2-cph3"] = Site{hosts: []string{"monitor1", "monitor2"}}
	list["webpod3-cph3"] = Site{hosts: []string{"monitor1", "monitor2"}}
	list["webpod4-cph3"] = Site{hosts: []string{"monitor1", "monitor2"}}
	list["webpod5-cph3"] = Site{hosts: []string{"monitor1", "monitor2"}}

	go func() {
		for {
			tmp := <-queue
			fmt.Printf("Working on %#v\n", tmp.hosts)
		}
	}()

	for {
		for k, v := range list {
			fmt.Printf("Adding %s: %#v\n", k, v)
			queue <- v
		}
	}

}
