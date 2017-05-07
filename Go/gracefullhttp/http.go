package main

import (
	"log"
	"net"
	"net/http"
	"time"
)

type Server struct {
	*http.Server
	connections map[net.Conn]struct{}

	ConnState func(net.Conn, http.ConnState)

	stopped chan struct{}
	quit    chan struct{}
	stop    bool
}

func ListenAndServe(server *http.Server) error {
	srv := &Server{Server: server}
	return srv.ListenAndServe()
}

func (srv *Server) ListenAndServe() error {
	srv.stop = false
	// Create the listener so we can control their lifetime
	addr := srv.Addr
	if addr == "" {
		addr = ":http"
	}
	l, err := net.Listen("tcp", addr)
	if err != nil {
		return err
	}

	return srv.Serve(l)
}

func Serve(server *http.Server, l net.Listener, timeout time.Duration) error {
	srv := &Server{Server: server}
	return srv.Serve(l)
}

func (srv *Server) Serve(listener net.Listener) error {

	srv.connections = make(map[net.Conn]struct{}, 100)
	srv.stopped = make(chan struct{})
	log.Println("Serving")

	srv.Server.ConnState = func(conn net.Conn, state http.ConnState) {
		log.Println("Serving")
		switch state {
		case http.StateNew:
			// Do not accept new connections when we are trying to stop
			log.Println(srv.stop)
			if srv.stop != true {
				srv.connections[conn] = struct{}{}
			}
		case http.StateClosed, http.StateHijacked:
			delete(srv.connections, conn)
		}

		if srv.ConnState != nil {
			srv.ConnState(conn, state)
		}
	}

	err := srv.Server.Serve(listener)
	if err != nil {
		log.Println(err)
		return err
	}

	log.Println("Stopping")
	return err
}

func (srv *Server) Start(mux *http.ServeMux) {
	go func(mux *http.ServeMux) {
		srv = &Server{Server: &http.Server{Addr: ":8080", Handler: mux}}

		if err := srv.ListenAndServe(); err != nil {
			if opErr, ok := err.(*net.OpError); !ok || (ok && opErr.Op != "accept") {
				log.Println(err)
			}
		}
		log.Println("And we are stopped")
		srv.stopped <- struct{}{}
	}(mux)
}

func (srv *Server) Stop() {
	srv.stop = true
}

func main() {

	var srv Server
	mux := http.NewServeMux()
	srv.Start(mux)

	for {
		select {
		case <-time.After(time.Second * time.Duration(10)):
			log.Printf("Calling stop, queue:%d", len(srv.connections))
			srv.Stop()
		case <-srv.stopped:
			log.Println("Stopped")
			break
		}
	}

}
